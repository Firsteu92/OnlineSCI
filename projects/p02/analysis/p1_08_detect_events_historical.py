"""
P1-08: Kelvin wave event detection on the 1993-2022 historical DUACS record.

Pre-registered hypothesis test (A18/R21, Q20): does the within-TIW-zone
correlation between Lambda_2 and amplitude ratio (r = 0.69 at n = 7, 2023
events) hold at n >= 20 across multiple ENSO cycles?

Method identical to p1_04 + p1_05 (2023 catalog), applied to 30 years:
  - 2S-2N mean SLA Hovmoller, monthly climatology removed
  - ray tracing eastward at 1.95 deg/day from 150-180E starts
  - mean along-ray SLA > 0.03 m, valid duration >= 30 days
  - overlap dedup, then tau = t_start - lon0/c ridge clustering (10 d)

Designed to run on the office WSL box against
/mnt/d/p02_data/duacs_hist/duacs_eqpac_<YYYY>.nc (0.125 deg, sla).
No matplotlib dependency; JSON output only.

Output: /mnt/d/p02_data/duacs_hist/kelvin_event_catalog_historical.json
"""
import glob
import json
import os
import sys

import numpy as np
import xarray as xr

DATA_DIR = sys.argv[1] if len(sys.argv) > 1 else "/mnt/d/p02_data/duacs_hist"
OUT = os.path.join(DATA_DIR, "kelvin_event_catalog_historical.json")

C_KELVIN = 2.5  # m/s
DEG_PER_DAY = C_KELVIN * 86400 / 111000  # ~1.95
MEAN_SLA_MIN = 0.03
MIN_DAYS = 30
TRACK_DAYS = 80
TAU_CLUSTER_DAYS = 10

files = sorted(glob.glob(os.path.join(DATA_DIR, "duacs_eqpac_[0-9]*.nc")))
print(f"Loading {len(files)} yearly files...", flush=True)
ds = xr.open_mfdataset(files, combine="by_coords")
sla = ds["sla"].sel(latitude=slice(-2, 2)).mean("latitude")
sla = sla.sel(longitude=slice(130, 280))
print(f"Hovmoller: {sla.sizes}", flush=True)

# monthly climatology over the full record
clim = sla.groupby("time.month").mean("time")
anom = (sla.groupby("time.month") - clim).load()
data = anom.values  # (time, lon)
times = anom.time.values
lons = anom.longitude.values
print(f"Loaded {data.shape[0]} days x {data.shape[1]} lons", flush=True)

lon_start_idx = np.where((lons >= 150) & (lons <= 180))[0]

candidates = []
n_scanned = 0
for t_idx in range(0, len(times) - 60, 5):
    for li in lon_start_idx[::8]:  # every 1 deg at 0.125 deg grid
        n_scanned += 1
        lon0 = lons[li]
        ray_sla, ray_t, ray_lon = [], [], []
        for dt in range(TRACK_DAYS):
            ti = t_idx + dt
            if ti >= len(times):
                break
            lon_t = lon0 + DEG_PER_DAY * dt
            if lon_t > 275:
                break
            lj = np.searchsorted(lons, lon_t)
            lj = min(lj, len(lons) - 1)
            v = data[ti, lj]
            if np.isfinite(v):
                ray_sla.append(v)
                ray_t.append(ti)
                ray_lon.append(lons[lj])
        if len(ray_sla) >= MIN_DAYS:
            m = float(np.mean(ray_sla))
            if m > MEAN_SLA_MIN:
                candidates.append({
                    "start": str(times[ray_t[0]])[:10],
                    "end": str(times[ray_t[-1]])[:10],
                    "lon0": round(float(ray_lon[0]), 2),
                    "lon1": round(float(ray_lon[-1]), 2),
                    "days": len(ray_sla),
                    "mean_sla": round(m, 4),
                    "max_sla": round(float(np.max(ray_sla)), 4),
                    "t_idx": int(ray_t[0]),
                })
print(f"Scanned {n_scanned} rays -> {len(candidates)} candidates", flush=True)

# stage 1: overlap dedup (keep strongest per time-lon neighbourhood)
candidates.sort(key=lambda e: (-e["mean_sla"], e["start"]))
unique = []
for e in candidates:
    dup = False
    for u in unique:
        t_overlap = (e["start"] <= u["end"]) and (e["end"] >= u["start"])
        if t_overlap and abs(e["lon0"] - u["lon0"]) < 15:
            dup = True
            break
    if not dup:
        unique.append(e)
print(f"After overlap dedup: {len(unique)}", flush=True)

# stage 2: ridge-intercept (tau) clustering
ref = np.datetime64("1993-01-01")
for e in unique:
    d_ref = (np.datetime64(e["start"]) - ref) / np.timedelta64(1, "D")
    e["tau"] = float(d_ref - e["lon0"] / DEG_PER_DAY)
unique.sort(key=lambda e: e["tau"])

clusters, cur = [], [unique[0]]
for e in unique[1:]:
    if abs(e["tau"] - cur[-1]["tau"]) < TAU_CLUSTER_DAYS:
        cur.append(e)
    else:
        clusters.append(cur)
        cur = [e]
clusters.append(cur)

events = []
for cl in sorted(clusters, key=lambda c: min(e["start"] for e in c)):
    rep = max(cl, key=lambda e: e["days"])
    i = len(events) + 1
    events.append({
        "id": f"KH{i:02d}",
        "start": rep["start"],
        "end": rep["end"],
        "lon0": min(e["lon0"] for e in cl),
        "lon1": max(e["lon1"] for e in cl),
        "days": rep["days"],
        "mean_sla": round(max(e["mean_sla"] for e in cl), 4),
        "max_sla": round(max(e["max_sla"] for e in cl), 4),
        "phase_speed_mps": C_KELVIN,
        "tau_intercept": round(float(np.mean([e["tau"] for e in cl])), 1),
        "cluster_size": len(cl),
        "confidence": "high" if rep["mean_sla"] > 0.06 else "moderate",
        "source_wind_flag": "pending_era5",
    })

with open(OUT, "w") as f:
    json.dump(events, f, indent=2)
print(f"Saved {len(events)} independent events -> {OUT}", flush=True)

years = {}
for e in events:
    years[e["start"][:4]] = years.get(e["start"][:4], 0) + 1
print("Events per year:", dict(sorted(years.items())), flush=True)
print("DETECTION DONE", flush=True)

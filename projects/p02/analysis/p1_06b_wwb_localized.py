"""
P1-06b: Localized WWB detection (replaces the box-mean method of p1_06).

p1_06 averaged u10 over the full 150-180°E x 5°S-5°N box, which dilutes
localized WWBs (~10° longitude x few° latitude) below detection — all 7
events returned "no" despite documented 2023 El Niño WWB activity. This is
the same spatial-dilution failure mode ClaudeB identified for zone-averaged
Λ (R19).

Method here:
  1. Meridional mean u10 over 2°S-2°N (equatorial Kelvin projection band).
  2. 5° running mean in longitude (20 pts at 0.25°).
  3. Daily maximum westerly over longitude → u_loc(t).
  4. Classification (raw westerly against ~4-5 m/s climatological easterlies,
     so u_loc > 3 m/s implies a westerly anomaly ≳ 7 m/s):
       confirmed: ≥ 3 days with u_loc > 3 m/s
       marginal:  peak u_loc > 2 m/s but persistence criterion not met
       no:        otherwise
  5. edge_limited flag if the peak sits within 1° of the western domain
     boundary (signal may extend west of 150°E; see p0_03 extended download).

Input:  data/era5/u10_wwb_<event_start>.nc  (from p1_06)
        data/era5/u10_eq_fullyear_130E-180E.nc  (preferred if present)
Output: data/era5/wwb_event_confirmation_localized.json
        figures/p1_wwb_localized.png
"""
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import yaml

BASE = Path(__file__).resolve().parents[1]
with open(BASE / "config.yaml") as f:
    cfg = yaml.safe_load(f)

CATALOG = BASE / cfg["data"]["events"]["catalog"]
ERA5_DIR = BASE / "data" / "era5"
FIG_DIR = BASE / "figures"

with open(CATALOG) as f:
    events = json.load(f)

FULLYEAR = ERA5_DIR / "u10_eq_fullyear_130E-180E.nc"
LEAD_DAYS = 20
POST_DAYS = 5
SMOOTH_PTS = 20  # 5° at 0.25°
THRESH_CONFIRM = 3.0  # m/s westerly
THRESH_MARGINAL = 2.0
MIN_DAYS = 3


def load_event_u10(event):
    """Return daily u10 (time, lat, lon) for the event window."""
    t0 = np.datetime64(event["start"]) - np.timedelta64(LEAD_DAYS, "D")
    t1 = np.datetime64(event["start"]) + np.timedelta64(POST_DAYS, "D")
    if FULLYEAR.exists():
        try:
            ds = xr.open_dataset(FULLYEAR)
            return ds["u10"].sel(time=slice(str(t0), str(t1))), "130E-180E (full-year)"
        except OSError:
            pass  # file incomplete (download in progress) — use per-event files
    f = ERA5_DIR / f"u10_wwb_{event['start']}.nc"
    if not f.exists():
        return None, None
    return xr.open_dataset(f)["u10"], "150E-180E (per-event)"


def detect_wwb(u10):
    """Localized westerly detection. Returns dict of diagnostics."""
    lat = u10["latitude"]
    u_eq = u10.sel(latitude=lat[(lat <= 2) & (lat >= -2)]).mean("latitude")
    u_sm = u_eq.rolling(longitude=SMOOTH_PTS, center=True, min_periods=10).mean()

    daymax = u_sm.max("longitude")
    peak = float(daymax.max())
    it, ix = np.unravel_index(np.nanargmax(u_sm.values), u_sm.shape)
    peak_day = str(u_sm.time.values[it])[:10]
    peak_lon = float(u_sm.longitude.values[ix])

    days_confirm = int((daymax > THRESH_CONFIRM).sum())
    days_marginal = int((daymax > THRESH_MARGINAL).sum())

    if days_confirm >= MIN_DAYS:
        verdict = "confirmed"
    elif peak > THRESH_MARGINAL:
        verdict = "marginal"
    else:
        verdict = "no"

    lon_min = float(u_sm.longitude.values.min())
    edge_limited = bool(peak_lon <= lon_min + 1.0)

    return {
        "wwb_detected": verdict,
        "peak_westerly_ms": round(peak, 2),
        "peak_day": peak_day,
        "peak_lon": round(peak_lon, 1),
        "days_westerly_gt3ms": days_confirm,
        "days_westerly_gt2ms": days_marginal,
        "edge_limited": edge_limited,
    }, u_eq


results = []
hovs = []
for event in events:
    u10, domain = load_event_u10(event)
    if u10 is None:
        results.append({"event_id": event["id"], "wwb_detected": "unknown"})
        hovs.append(None)
        continue
    diag, u_eq = detect_wwb(u10)
    diag["event_id"] = event["id"]
    diag["event_start"] = event["start"]
    diag["search_domain"] = domain
    diag["window"] = f"start-{LEAD_DAYS}d to start+{POST_DAYS}d, 2S-2N"
    results.append(diag)
    hovs.append(u_eq.compute())
    print(f"{event['id']} ({event['start']}): {diag['wwb_detected']:9s} "
          f"peak={diag['peak_westerly_ms']:+.2f} m/s @ {diag['peak_day']} "
          f"{diag['peak_lon']}E, days>3={diag['days_westerly_gt3ms']}"
          f"{' [EDGE]' if diag['edge_limited'] else ''}")

out_file = ERA5_DIR / "wwb_event_confirmation_localized.json"
with open(out_file, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved: {out_file}")

n_conf = sum(1 for r in results if r["wwb_detected"] == "confirmed")
n_marg = sum(1 for r in results if r["wwb_detected"] == "marginal")
print(f"Summary: {n_conf} confirmed, {n_marg} marginal, "
      f"{len(results) - n_conf - n_marg} no/unknown of {len(results)}")

# --- Figure: per-event equatorial u10 Hovmöller (time x lon) ---
fig, axes = plt.subplots(2, 4, figsize=(16, 7), constrained_layout=True)
axes = axes.ravel()
for i, (event, u_eq, r) in enumerate(zip(events, hovs, results)):
    ax = axes[i]
    if u_eq is None:
        ax.set_axis_off()
        continue
    t = u_eq.time.values
    lon = u_eq.longitude.values
    pm = ax.pcolormesh(lon, t, u_eq.values, cmap="RdBu_r", vmin=-10, vmax=10)
    ax.axhline(np.datetime64(event["start"]), color="k", lw=1, ls="--")
    ax.plot(r["peak_lon"], np.datetime64(r["peak_day"]), "k*", ms=10)
    ax.set_title(f"{event['id']}: {r['wwb_detected']}"
                 f" (peak {r['peak_westerly_ms']:+.1f} m/s)", fontsize=10)
    ax.set_xlabel("Longitude (°E)", fontsize=8)
    ax.tick_params(labelsize=7)
axes[7].set_axis_off()
fig.colorbar(pm, ax=axes[7], label="u10 (m/s)", shrink=0.8)
fig.suptitle("ERA5 equatorial (2°S–2°N) zonal wind around Kelvin event onsets — "
             "localized WWB detection", fontsize=12)
fig.savefig(FIG_DIR / "p1_wwb_localized.png", dpi=150)
print(f"Saved: {FIG_DIR / 'p1_wwb_localized.png'}")

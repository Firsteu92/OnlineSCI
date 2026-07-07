"""
P4-02: Along-ray local Λ — answers R19 Q17.

p4_01 used zone-averaged |ζ|, which dilutes TIW vortex cores ~5-7x and put
all Λ at 5-8 regardless of zone. Here Λ is computed from the perturbation
the wave actually encounters: for each day the Kelvin ray transits a zone,
take the local maximum perturbation in a window centred on the ray position
(±1.5° lon × ±3° lat, the equatorial trapping scale), then

  Λ_min    = Δω_eff / max_t δω_loc(t)   (strongest perturbation met)
  Λ_median = Δω_eff / median_t δω_loc(t)

δω_loc = pointwise max(|ζ|/2, |U|·k_x) after 0.5° boxcar smoothing of the
GLORYS fields (suppresses grid-scale noise; TIW cores are ~3-5° wide and
survive). Raw-grid Λ_min also recorded for sensitivity.

Caveat (for Discussion): GLORYS uo,vo contain the Kelvin wave's own signal.
At the equator the wave contributes mostly to U (Doppler term), little to ζ
(∂u/∂y = 0 at the equatorial SSH maximum); ζ-dominated Λ is therefore
robust to self-contamination.

Input:  data/glorys/glorys_uv_<event>_<zone>.nc  (from p4_01, 21 files)
Output: data/glorys/lambda_along_ray.json
        figures/p4_lambda_along_ray.png
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

GLORYS_DIR = BASE / "data" / "glorys"
FIG_DIR = BASE / "figures"

with open(BASE / cfg["data"]["events"]["catalog"]) as f:
    events = json.load(f)

DELTA_OMEGA_EFF = float(cfg["physics"]["delta_omega_eff"])
C1 = float(cfg["physics"]["c1"])
KELVIN_PERIOD_DAYS = 30
KELVIN_WAVELENGTH_DEG = C1 * KELVIN_PERIOD_DAYS * 86400 / 111000
K_X = 2 * np.pi / (KELVIN_WAVELENGTH_DEG * 111000)
RAY_SPEED_DEG_DAY = C1 * 86400 / 111000  # ~1.95 deg/day

RAY_HALF_LON = 1.5  # deg, window around ray position
RAY_HALF_LAT = 3.0  # deg, equatorial trapping scale
SMOOTH_PTS = 6      # 0.5° boxcar at 1/12°

zones = [
    {"name": "Gilbert Islands", "lon": 175, "width": 8},
    {"name": "Line Islands", "lon": 202, "width": 8},
    {"name": "TIW zone", "lon": 245, "width": 20},
]


def smooth2d(a, n):
    """Boxcar smooth over the last two axes, NaN-aware."""
    da = xr.DataArray(a)
    return (
        da.rolling({da.dims[-1]: n}, center=True, min_periods=1).mean()
        .rolling({da.dims[-2]: n}, center=True, min_periods=1).mean()
        .values
    )


def along_ray_lambda(event, zone):
    fname = GLORYS_DIR / f"glorys_uv_{event['id']}_{zone['name'].replace(' ', '_')}.nc"
    if not fname.exists():
        return None

    ds = xr.open_dataset(fname)
    lon_name = "longitude" if "longitude" in ds.dims else "lon"
    lat_name = "latitude" if "latitude" in ds.dims else "lat"

    lon_vals = ds[lon_name].values
    to_neg = bool(np.any(lon_vals < 0))

    def conv(lon):  # catalog/zone lons are 0-360
        return lon - 360 if (to_neg and lon > 180) else lon

    sub = ds.sel({lat_name: slice(-RAY_HALF_LAT, RAY_HALF_LAT)})
    if sub[lat_name].size == 0:  # latitude stored descending
        sub = ds.sel({lat_name: slice(RAY_HALF_LAT, -RAY_HALF_LAT)})
    if "depth" in sub.dims:
        sub = sub.isel(depth=0)

    t0 = np.datetime64(event["start"])
    lon0 = event["lon0"]
    times = sub.time.values
    days = (times - t0) / np.timedelta64(1, "D")
    ray_lon = lon0 + RAY_SPEED_DEG_DAY * days

    z_lo, z_hi = zone["lon"] - zone["width"], zone["lon"] + zone["width"]
    transit = (days >= 0) & (ray_lon >= z_lo) & (ray_lon <= z_hi)
    if transit.sum() == 0:
        ds.close()
        return None

    dx = 0.083 * 111000
    dy = 0.083 * 111000

    dw_loc_sm, dw_loc_raw = [], []
    for it in np.where(transit)[0]:
        rl = conv(float(ray_lon[it]))
        win = sub.isel(time=it).sel({lon_name: slice(rl - RAY_HALF_LON, rl + RAY_HALF_LON)})
        if win[lon_name].size < 5:
            continue
        uo = win["uo"].values
        vo = win["vo"].values
        zeta = np.gradient(vo, dx, axis=-1) - np.gradient(uo, dy, axis=-2)
        dw_raw = np.fmax(np.abs(zeta) / 2, np.abs(uo) * K_X)
        zeta_sm = smooth2d(zeta, SMOOTH_PTS)
        uo_sm = smooth2d(uo, SMOOTH_PTS)
        dw_sm = np.fmax(np.abs(zeta_sm) / 2, np.abs(uo_sm) * K_X)
        if np.all(np.isnan(dw_sm)):
            continue
        dw_loc_sm.append(float(np.nanmax(dw_sm)))
        dw_loc_raw.append(float(np.nanmax(dw_raw)))
    ds.close()

    if not dw_loc_sm:
        return None

    dw_sm_arr = np.array(dw_loc_sm)
    return {
        "event_id": event["id"],
        "zone": zone["name"],
        "n_transit_days": len(dw_loc_sm),
        "lambda_min": round(DELTA_OMEGA_EFF / dw_sm_arr.max(), 2),
        "lambda_median": round(DELTA_OMEGA_EFF / np.median(dw_sm_arr), 2),
        "lambda_min_rawgrid": round(DELTA_OMEGA_EFF / max(dw_loc_raw), 2),
        "max_dw_loc": round(dw_sm_arr.max(), 8),
    }


results = []
for event in events:
    for zone in zones:
        r = along_ray_lambda(event, zone)
        if r:
            results.append(r)
            print(f"{r['event_id']} x {r['zone']:16s}: Λ_min={r['lambda_min']:5.2f} "
                  f"Λ_med={r['lambda_median']:5.2f} (raw {r['lambda_min_rawgrid']:.2f}, "
                  f"{r['n_transit_days']} transit days)")

out = GLORYS_DIR / "lambda_along_ray.json"
with open(out, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved: {out}")

# zone summaries, alongside p4_01 zone-mean values
with open(GLORYS_DIR / "lambda_event_zone.json") as f:
    zonal = {(r["event_id"], r["zone"]): r["lambda"] for r in json.load(f)}

print("\nZone summary (along-ray Λ_min vs zone-mean Λ):")
for zone in zones:
    zr = [r for r in results if r["zone"] == zone["name"]]
    lam_min = [r["lambda_min"] for r in zr]
    lam_zonal = [zonal[(r["event_id"], r["zone"])] for r in zr if (r["event_id"], r["zone"]) in zonal]
    print(f"  {zone['name']:16s}: Λ_min = {np.mean(lam_min):.2f} ± {np.std(lam_min):.2f} "
          f"(range {min(lam_min):.2f}-{max(lam_min):.2f}) | zone-mean Λ = {np.mean(lam_zonal):.2f}")

# --- figure: zone-mean vs along-ray, per zone ---
fig, ax = plt.subplots(figsize=(7, 5))
colors = {"Gilbert Islands": "#1f77b4", "Line Islands": "#2ca02c", "TIW zone": "#d62728"}
for zone in zones:
    zr = [r for r in results if r["zone"] == zone["name"]]
    x = [zonal.get((r["event_id"], r["zone"]), np.nan) for r in zr]
    y = [r["lambda_min"] for r in zr]
    ax.scatter(x, y, c=colors[zone["name"]], label=zone["name"], s=50, zorder=3)
lims = [0, 9]
ax.plot(lims, lims, "k--", lw=0.8, alpha=0.5)
ax.axhline(1.0, color="gray", lw=0.8, ls=":")
ax.text(0.2, 1.1, r"$\Lambda_c \sim 1$", fontsize=9, color="gray")
ax.set_xlim(lims), ax.set_ylim(lims)
ax.set_xlabel(r"Zone-averaged $\Lambda$ (p4_01)")
ax.set_ylabel(r"Along-ray $\Lambda_\mathrm{min}$ (local max $|\zeta|$, 0.5° smoothed)")
ax.legend()
ax.set_title("Spatial resolution of the spectral-gap parameter")
fig.tight_layout()
fig.savefig(FIG_DIR / "p4_lambda_along_ray.png", dpi=150)
print(f"Saved: {FIG_DIR / 'p4_lambda_along_ray.png'}")

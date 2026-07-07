"""
P1-04: Automatic Kelvin wave event detection from DUACS Hovmöller
Method: Radon transform-like approach — detect linear features with slope
matching Kelvin wave phase speed (~2.5 m/s ≈ 1.95 deg/day eastward)
"""
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = str(_ROOT / "data/duacs")
FIG_DIR = str(_ROOT / "figures")

ds = xr.open_dataset(os.path.join(DATA_DIR, "duacs_eqpac_daily_2023_2025.nc"))
sla = ds["sla"]

# Remap to 0-360 Pacific view
lon = sla.longitude.values
lon_360 = np.where(lon < 0, lon + 360, lon)
sort_idx = np.argsort(lon_360)
sla_sorted = sla.isel(longitude=sort_idx)
lon_sorted = lon_360[sort_idx]

mask_lon = (lon_sorted >= 130) & (lon_sorted <= 280)
sla_pac = sla_sorted.isel(longitude=mask_lon)
lon_pac = lon_sorted[mask_lon]

# Equatorial mean (2S-2N)
sla_eq = sla_pac.sel(latitude=slice(-2, 2)).mean(dim="latitude")

# Remove climatological monthly mean
sla_clim = sla_eq.groupby("time.month").mean("time")
sla_anom = sla_eq.groupby("time.month") - sla_clim
data = sla_anom.values  # (time, lon)
times = sla_anom.time.values

# Kelvin wave detection: eastward-propagating positive SLA
# Phase speed: c = 2.5 m/s → ~1.95 deg/day at equator
c_kelvin = 2.5  # m/s
deg_per_day = c_kelvin * 86400 / 111000  # ~1.95

# For each starting point in western Pacific (150-180E),
# track the eastward-propagating signal along the Kelvin ray
lon_start_range = (lon_pac >= 150) & (lon_pac <= 180)
lon_start_idx = np.where(lon_start_range)[0]

events = []
for t_idx in range(0, len(times) - 60, 5):  # scan every 5 days
    for li in lon_start_idx[::4]:  # scan every 4th starting longitude
        lon0 = lon_pac[li]
        # Track ray from (t_idx, lon0) eastward at c_kelvin
        ray_sla = []
        ray_times = []
        ray_lons = []
        for dt in range(0, 80):  # follow for up to 80 days
            if t_idx + dt >= len(times):
                break
            lon_at_t = lon0 + deg_per_day * dt
            if lon_at_t > 275:
                break
            li_nearest = np.argmin(np.abs(lon_pac - lon_at_t))
            val = data[t_idx + dt, li_nearest]
            if not np.isnan(val):
                ray_sla.append(val)
                ray_times.append(times[t_idx + dt])
                ray_lons.append(lon_pac[li_nearest])

        if len(ray_sla) >= 30:  # at least 30 days of tracking
            mean_sla = np.mean(ray_sla)
            if mean_sla > 0.03:  # positive SLA along ray
                lon_range = ray_lons[-1] - ray_lons[0]
                events.append({
                    "start_time": str(ray_times[0])[:10],
                    "end_time": str(ray_times[-1])[:10],
                    "start_lon": round(float(ray_lons[0]), 1),
                    "end_lon": round(float(ray_lons[-1]), 1),
                    "duration_days": len(ray_sla),
                    "mean_sla": round(mean_sla, 4),
                    "max_sla": round(max(ray_sla), 4),
                    "lon_range": round(lon_range, 1),
                })

# Deduplicate: merge events that overlap in time and space
events_sorted = sorted(events, key=lambda e: (-e["mean_sla"], e["start_time"]))
unique_events = []
for e in events_sorted:
    is_dup = False
    for u in unique_events:
        t_overlap = (e["start_time"] <= u["end_time"] and e["end_time"] >= u["start_time"])
        lon_overlap = abs(e["start_lon"] - u["start_lon"]) < 15
        if t_overlap and lon_overlap:
            is_dup = True
            break
    if not is_dup:
        unique_events.append(e)

print(f"Detected {len(unique_events)} unique Kelvin wave events")
print(f"{'#':>3} {'Start':>12} {'End':>12} {'Lon0':>6} {'Lon1':>6} {'Days':>5} {'Mean SLA':>9} {'Max SLA':>9}")
for i, e in enumerate(unique_events[:20]):
    print(f"{i+1:3d} {e['start_time']:>12} {e['end_time']:>12} {e['start_lon']:6.1f} {e['end_lon']:6.1f} {e['duration_days']:5d} {e['mean_sla']:9.4f} {e['max_sla']:9.4f}")

# Plot: Hovmöller with detected events overlaid
fig, ax = plt.subplots(figsize=(14, 8))
pcm = ax.pcolormesh(lon_pac, times, data, cmap="RdBu_r", vmin=-0.15, vmax=0.15, shading="auto")
for i, e in enumerate(unique_events[:15]):
    t0 = np.datetime64(e["start_time"])
    t1 = np.datetime64(e["end_time"])
    ax.plot([e["start_lon"], e["end_lon"]], [t0, t1], "k-", linewidth=2, alpha=0.7)
    ax.text(e["end_lon"] + 2, t1, f"K{i+1}", fontsize=8, va="center")

ax.set_xlabel("Longitude (°E)")
ax.set_ylabel("Time")
ax.set_title(f"Kelvin Wave Events Detected ({len(unique_events)} events, c ≈ 2.5 m/s)")
ax.yaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
ax.yaxis.set_major_locator(mdates.MonthLocator(interval=2))
plt.colorbar(pcm, ax=ax, label="SLA (m)", shrink=0.8)
plt.tight_layout()
out_path = os.path.join(FIG_DIR, "p1_kelvin_events_detected.png")
plt.savefig(out_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"\nFigure saved: {out_path}")

# Save event catalog
import json
catalog_path = os.path.join(os.path.dirname(DATA_DIR), "kelvin_event_catalog.json")
with open(catalog_path, "w") as f:
    json.dump(unique_events[:20], f, indent=2)
print(f"Event catalog saved: {catalog_path}")

ds.close()

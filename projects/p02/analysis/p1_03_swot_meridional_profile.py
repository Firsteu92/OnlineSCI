"""
P1-03: Extract SWOT meridional SSH profile across equator
Run on remote WSL

Pick a pass during a known Kelvin wave event (2023 El Nino buildup, ~Oct 2023)
and extract the cross-track SSH profile to check equatorial trapping structure.
"""
import xarray as xr
import numpy as np
import json, glob, os

base = "/mnt/d/v2_0_1/Basic"
out_dir = "/mnt/e/Documents/temp"

# Use cycle 20 (~mid-2024) which overlaps with El Nino Kelvin waves
cycle = 20
cycle_dir = os.path.join(base, f"cycle_{cycle:03d}")
files = sorted(glob.glob(os.path.join(cycle_dir, "*.nc")))

# Find passes crossing equatorial central Pacific (180-220E)
best_passes = []
for f in files:
    try:
        ds = xr.open_dataset(f)
        lat = ds["latitude"].values
        lon = ds["longitude"].values
        eq_mask = (lat > -5) & (lat < 5)
        eq_lines = np.any(eq_mask, axis=1)
        if eq_lines.sum() > 100:
            eq_idx = np.where(eq_lines)[0]
            eq_lon = float(np.nanmean(lon[eq_idx, :]))
            if 180 <= eq_lon <= 220:
                ssha = ds["ssha_filtered"].values[eq_idx, :]
                valid = np.sum(~np.isnan(ssha)) / ssha.size * 100
                if valid > 50:
                    best_passes.append((f, eq_lon, valid, eq_idx))
        ds.close()
    except:
        pass

print(f"Found {len(best_passes)} good passes in central Pacific for cycle {cycle}")

if len(best_passes) == 0:
    print("No passes found. Try different cycle or longitude range.")
    exit(1)

# Take the best one (highest valid %)
best_passes.sort(key=lambda x: -x[2])
f, eq_lon, valid, eq_idx = best_passes[0]
print(f"Best pass: {os.path.basename(f)}, lon={eq_lon:.1f}E, valid={valid:.1f}%")

# Extract meridional profile
ds = xr.open_dataset(f)
lat_full = ds["latitude"].values
lon_full = ds["longitude"].values
ssha = ds["ssha_filtered"].values

# Get equatorial segment (10S-10N for wider view)
wide_mask = np.any((lat_full > -10) & (lat_full < 10), axis=1)
wide_idx = np.where(wide_mask)[0]

lat_seg = lat_full[wide_idx, :]
lon_seg = lon_full[wide_idx, :]
ssha_seg = ssha[wide_idx, :]

# Average across track (69 pixels) for meridional profile
lat_mean = np.nanmean(lat_seg, axis=1)
ssha_mean = np.nanmean(ssha_seg, axis=1)

# Also get cross-track structure at equator
eq_narrow = np.where((lat_mean > -1) & (lat_mean < 1))[0]
if len(eq_narrow) > 0:
    ssha_eq_crosstrack = ssha_seg[eq_narrow[len(eq_narrow)//2], :]
    lon_crosstrack = lon_seg[eq_narrow[len(eq_narrow)//2], :]

# Save results
result = {
    "filename": os.path.basename(f),
    "cycle": cycle,
    "eq_lon": eq_lon,
    "lat": lat_mean.tolist(),
    "ssha_meridional": [float(x) if not np.isnan(x) else None for x in ssha_mean],
    "lon_crosstrack": lon_crosstrack.tolist() if len(eq_narrow) > 0 else [],
    "ssha_crosstrack": [float(x) if not np.isnan(x) else None for x in ssha_eq_crosstrack] if len(eq_narrow) > 0 else [],
}

out_file = os.path.join(out_dir, "swot_meridional_profile.json")
with open(out_file, "w") as fj:
    json.dump(result, fj)

print(f"\nMeridional profile:")
print(f"  Lat range: {lat_mean[0]:.2f} to {lat_mean[-1]:.2f}")
print(f"  N points: {len(lat_mean)}")
print(f"  SSHA range: {np.nanmin(ssha_mean):.4f} to {np.nanmax(ssha_mean):.4f} m")
print(f"  SSHA at equator: {ssha_mean[len(ssha_mean)//2]:.4f} m")
print(f"Saved to {out_file}")

ds.close()

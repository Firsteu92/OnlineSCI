"""
P4-01: Compute real Λ from GLORYS12 background flow for each event × zone.

Λ = Δω_eff / δω_pert

where:
  Δω_eff = √(β·c₁) ≈ 7.6e-6 s⁻¹  (from config.yaml)
  δω_pert = max(|ζ|/2, |U·k_x|)    (V1 simplified)
    ζ = relative vorticity from GLORYS12 daily U,V
    U = zonal current, k_x = 2π/(λ_K) where λ_K ≈ 2·c₁·T_K

Data: CMEMS GLORYS12 (GLOBAL_MULTIYEAR_PHY_001_030)
  Dataset: cmems_mod_glo_phy_my_0.083deg_P1D-m
  Variables: uo (eastward velocity), vo (northward velocity)
  Region: equatorial Pacific 5°S-5°N, 130°E-80°W
  Depth: surface (0 m)

Output: data/glorys/lambda_event_zone.json + figure
"""
import json
import os
from pathlib import Path

import numpy as np
import yaml

BASE = Path(__file__).resolve().parents[1]
with open(BASE / "config.yaml") as f:
    cfg = yaml.safe_load(f)

GLORYS_DIR = BASE / "data" / "glorys"
GLORYS_DIR.mkdir(parents=True, exist_ok=True)
FIG_DIR = BASE / "figures"

CATALOG = BASE / cfg["data"]["events"]["catalog"]
with open(CATALOG) as f:
    events = json.load(f)

DELTA_OMEGA_EFF = float(cfg["physics"]["delta_omega_eff"])
C1 = float(cfg["physics"]["c1"])
KELVIN_PERIOD_DAYS = 30
KELVIN_WAVELENGTH_DEG = C1 * KELVIN_PERIOD_DAYS * 86400 / 111000
K_X = 2 * np.pi / (KELVIN_WAVELENGTH_DEG * 111000)

zones = [
    {"name": "Gilbert Islands", "lon": 175, "width": 8},
    {"name": "Line Islands", "lon": 202, "width": 8},
    {"name": "TIW zone", "lon": 245, "width": 20},
]

print(f"Δω_eff = {DELTA_OMEGA_EFF:.2e} s⁻¹")
print(f"c₁ = {C1} m/s")
print(f"Kelvin k_x = {K_X:.2e} m⁻¹ (λ ≈ {KELVIN_WAVELENGTH_DEG:.0f}°)")


def download_glorys_subset(event, zone):
    """Download GLORYS12 U,V for event time window around perturbation zone."""
    import copernicusmarine

    t_start = event["start"]
    t_end = event["end"]
    lon_c = zone["lon"]
    lon_w = zone["width"]

    out_file = GLORYS_DIR / f"glorys_uv_{event['id']}_{zone['name'].replace(' ', '_')}.nc"
    if out_file.exists():
        print(f"  Cached: {out_file.name}")
        return out_file

    print(f"  Downloading GLORYS12 for {event['id']} × {zone['name']}...")
    try:
        copernicusmarine.subset(
            dataset_id="cmems_mod_glo_phy_my_0.083deg_P1D-m",
            variables=["uo", "vo"],
            minimum_longitude=lon_c - lon_w - 5,
            maximum_longitude=lon_c + lon_w + 5,
            minimum_latitude=-5,
            maximum_latitude=5,
            start_datetime=f"{t_start}T00:00:00",
            end_datetime=f"{t_end}T23:59:59",
            minimum_depth=0,
            maximum_depth=1,
            output_filename=str(out_file.name),
            output_directory=str(GLORYS_DIR),
            force_download=True,
            disable_progress_bar=True,
        )
        return out_file
    except Exception as e:
        print(f"  GLORYS download failed: {e}")
        return None


def compute_lambda(glorys_file, zone):
    """Compute Λ from GLORYS U,V in the perturbation zone."""
    import xarray as xr

    if glorys_file is None or not glorys_file.exists():
        return None

    ds = xr.open_dataset(glorys_file)
    lon_c = zone["lon"]
    lon_w = zone["width"]

    try:
        if "longitude" in ds.dims:
            lon_name, lat_name = "longitude", "latitude"
        else:
            lon_name, lat_name = "lon", "lat"

        lon_vals = ds[lon_name].values
        if np.any(lon_vals < 0):
            lon_c_use = lon_c - 360 if lon_c > 180 else lon_c
        else:
            lon_c_use = lon_c

        sub = ds.sel(
            **{lon_name: slice(lon_c_use - lon_w, lon_c_use + lon_w),
               lat_name: slice(-3, 3)}
        )

        if "depth" in sub.dims:
            sub = sub.isel(depth=0)

        uo = sub["uo"].values
        vo = sub["vo"].values

        dx = 0.083 * 111000 * np.cos(np.radians(0))
        dy = 0.083 * 111000

        dvdx = np.gradient(vo, dx, axis=-1)
        dudy = np.gradient(uo, dy, axis=-2)
        zeta = dvdx - dudy

        mean_abs_zeta = float(np.nanmean(np.abs(zeta)))
        mean_abs_U = float(np.nanmean(np.abs(uo)))

        dw_zeta = mean_abs_zeta / 2
        dw_doppler = mean_abs_U * K_X
        dw_pert = max(dw_zeta, dw_doppler)

        lam = DELTA_OMEGA_EFF / (dw_pert + 1e-20)

        return {
            "lambda": round(float(lam), 2),
            "delta_omega_eff": DELTA_OMEGA_EFF,
            "delta_omega_zeta": round(float(dw_zeta), 8),
            "delta_omega_doppler": round(float(dw_doppler), 8),
            "delta_omega_pert": round(float(dw_pert), 8),
            "mean_abs_zeta": round(float(mean_abs_zeta), 8),
            "mean_abs_U": round(float(mean_abs_U), 4),
            "dominant_perturbation": "vorticity" if dw_zeta > dw_doppler else "doppler",
        }
    finally:
        ds.close()


results = []
for event in events:
    for zone in zones:
        print(f"\nEvent {event['id']} × {zone['name']}:")
        glorys_file = download_glorys_subset(event, zone)
        lam_result = compute_lambda(glorys_file, zone)
        if lam_result:
            lam_result["event_id"] = event["id"]
            lam_result["zone"] = zone["name"]
            results.append(lam_result)
            print(f"  Λ = {lam_result['lambda']:.1f} "
                  f"(ζ/2={lam_result['delta_omega_zeta']:.2e}, "
                  f"U·k={lam_result['delta_omega_doppler']:.2e}, "
                  f"dominant={lam_result['dominant_perturbation']})")
        else:
            print(f"  Λ = N/A (data unavailable)")

out_file = GLORYS_DIR / "lambda_event_zone.json"
with open(out_file, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved: {out_file}")
print(f"Total: {len(results)} Λ estimates from {len(events)} events × {len(zones)} zones")

if results:
    lam_vals = [r["lambda"] for r in results]
    print(f"\nΛ statistics: min={min(lam_vals):.1f}, max={max(lam_vals):.1f}, "
          f"mean={np.mean(lam_vals):.1f}, median={np.median(lam_vals):.1f}")

    for zone in zones:
        z_lam = [r["lambda"] for r in results if r["zone"] == zone["name"]]
        if z_lam:
            print(f"  {zone['name']}: Λ = {np.mean(z_lam):.1f} ± {np.std(z_lam):.1f}")

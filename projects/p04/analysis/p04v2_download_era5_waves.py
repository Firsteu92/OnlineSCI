#!/usr/bin/env python3
"""
P04 v2: Download ERA5 monthly wave products for Southern Ocean
Run on remote desktop WSL

Products:
  - Significant wave height (SWH)
  - Mean wave period (MWP)
  - Mean wave direction (MWD)
  - 10m u/v wind (for fetch calculation)
  - Sea ice concentration (for MIZ boundary)

All monthly means, 1979-2024, Southern Ocean (40S-75S)
"""

import cdsapi
import os

OUT_DIR = os.path.expanduser("~/p04v2_data")
os.makedirs(OUT_DIR, exist_ok=True)

c = cdsapi.Client()

# --- 1. ERA5 wave products (0.5° native wave grid) ---
print("Downloading ERA5 wave products...")
c.retrieve(
    "reanalysis-era5-single-levels-monthly-means",
    {
        "product_type": "monthly_averaged_reanalysis",
        "variable": [
            "significant_height_of_combined_wind_waves_and_swell",
            "mean_wave_period",
            "mean_wave_direction",
        ],
        "year": [str(y) for y in range(1979, 2025)],
        "month": [f"{m:02d}" for m in range(1, 13)],
        "time": "00:00",
        "area": [-40, -180, -75, 180],
        "format": "netcdf",
    },
    f"{OUT_DIR}/era5_waves_SO_1979_2024.nc",
)
print(f"  -> {OUT_DIR}/era5_waves_SO_1979_2024.nc")

# --- 2. ERA5 10m wind (0.25° atmosphere grid) ---
print("Downloading ERA5 10m wind...")
c.retrieve(
    "reanalysis-era5-single-levels-monthly-means",
    {
        "product_type": "monthly_averaged_reanalysis",
        "variable": [
            "10m_u_component_of_wind",
            "10m_v_component_of_wind",
        ],
        "year": [str(y) for y in range(1979, 2025)],
        "month": [f"{m:02d}" for m in range(1, 13)],
        "time": "00:00",
        "area": [-40, -180, -75, 180],
        "format": "netcdf",
    },
    f"{OUT_DIR}/era5_wind_SO_1979_2024.nc",
)
print(f"  -> {OUT_DIR}/era5_wind_SO_1979_2024.nc")

# --- 3. ERA5 sea ice concentration ---
print("Downloading ERA5 SIC...")
c.retrieve(
    "reanalysis-era5-single-levels-monthly-means",
    {
        "product_type": "monthly_averaged_reanalysis",
        "variable": "sea_ice_cover",
        "year": [str(y) for y in range(1979, 2025)],
        "month": [f"{m:02d}" for m in range(1, 13)],
        "time": "00:00",
        "area": [-40, -180, -75, 180],
        "format": "netcdf",
    },
    f"{OUT_DIR}/era5_sic_SO_1979_2024.nc",
)
print(f"  -> {OUT_DIR}/era5_sic_SO_1979_2024.nc")

print("\nAll downloads complete!")
print(f"Output directory: {OUT_DIR}")
print("Transfer to Mac via Nutcloud: cp {OUT_DIR}/*.nc /mnt/e/Documents/temp/")

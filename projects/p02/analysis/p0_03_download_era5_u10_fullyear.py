"""
P0-03: Download ERA5 daily u10 for the full study period, extended domain.

Covers 2022-12-01 to 2024-01-15, 130°E-180°, 5°S-5°N — one dataset usable
for all 7 Kelvin events. Extends west of 150°E because p1_06b found the
KE01-KE03 westerly peaks pinned at the 150°E domain edge.

Downloads per month (zarr long-stream asyncio crashes on the monolithic
request), then merges. Re-runnable: completed months are skipped.

Uses ARCO-ERA5 zarr on GCS (anonymous access).
Output: data/era5/u10_eq_fullyear_130E-180E.nc
"""
from pathlib import Path

import numpy as np
import pandas as pd
import xarray as xr

BASE = Path(__file__).resolve().parents[1]
ERA5_DIR = BASE / "data" / "era5"
TMP_DIR = ERA5_DIR / "monthly_tmp"
TMP_DIR.mkdir(parents=True, exist_ok=True)

OUT = ERA5_DIR / "u10_eq_fullyear_130E-180E.nc"
if OUT.exists():
    print(f"Already exists: {OUT}")
    raise SystemExit(0)

months = pd.date_range("2022-12-01", "2024-01-01", freq="MS")

for m0 in months:
    m1 = min(m0 + pd.offsets.MonthBegin(1), pd.Timestamp("2024-01-16"))
    mfile = TMP_DIR / f"u10_{m0:%Y-%m}.nc"
    if mfile.exists():
        print(f"{m0:%Y-%m}: exists, skip", flush=True)
        continue
    print(f"{m0:%Y-%m}: downloading...", flush=True)
    for attempt in range(3):
        try:
            ds_full = xr.open_zarr(
                "gs://gcp-public-data-arco-era5/ar/full_37-1h-0p25deg-chunk-1.zarr-v3",
                chunks={"time": 24},
                storage_options={"token": "anon"},
            )
            sub = ds_full["10m_u_component_of_wind"].sel(
                latitude=slice(5, -5),
                longitude=slice(130, 180),
                time=slice(str(m0.date()), str((m1 - pd.Timedelta(hours=1)))),
            )
            daily = sub.resample(time="1D").mean().compute()
            daily.to_dataset(name="u10").to_netcdf(mfile)
            print(f"{m0:%Y-%m}: done ({mfile.stat().st_size // 1024} KB)", flush=True)
            break
        except Exception as e:
            print(f"{m0:%Y-%m}: attempt {attempt + 1} failed — {str(e)[:120]}", flush=True)
            if mfile.exists():
                mfile.unlink()
else:
    pass

mfiles = sorted(TMP_DIR.glob("u10_*.nc"))
print(f"Merging {len(mfiles)} monthly files...", flush=True)
ds = xr.open_mfdataset(mfiles, combine="by_coords")
ds = ds.sel(time=slice("2022-12-01", "2024-01-15"))
ds.to_netcdf(OUT)
print(f"Saved: {OUT} ({len(ds.time)} days)", flush=True)

#!/usr/bin/env python3
"""
P04 v2 Revision Step 3: Partial Granger (conditioning on wind)

Addresses Reviewer 1 concern: SIC→SWH may be confounded by SAM
driving both variables. Test: does SIC still Granger-cause SWH
after removing wind's predictive contribution?
"""

import numpy as np
import xarray as xr
import pandas as pd
from pathlib import Path
from scipy import stats
import json

REPO = str(Path(__file__).resolve().parents[3])
P04 = f'{REPO}/projects/p04'
DATA = f'{P04}/data'
OUT = f'{P04}/analysis'

def partial_granger(y, x, z, max_lag=6):
    """Test if x Granger-causes y AFTER controlling for z.
    Full model: y = lag(y) + lag(x) + lag(z)
    Reduced model: y = lag(y) + lag(z)   (x removed)
    """
    n = len(y)
    best_aic = np.inf; best_lag = 1; best_f = 0; best_p = 1
    for lag in range(1, max_lag+1):
        T = n - lag; Y = y[lag:]
        # Build reduced model: intercept + lag(y) + lag(z)
        X_red = np.ones((T, 1))
        for l in range(1, lag+1):
            X_red = np.column_stack([X_red, y[lag-l:n-l]])
        for l in range(1, lag+1):
            X_red = np.column_stack([X_red, z[lag-l:n-l]])
        red_cols = X_red.shape[1]
        # Full model: reduced + lag(x)
        X_full = X_red.copy()
        for l in range(1, lag+1):
            X_full = np.column_stack([X_full, x[lag-l:n-l]])
        try:
            b_f = np.linalg.lstsq(X_full, Y, rcond=None)[0]
            rss_full = np.sum((Y - X_full @ b_f)**2)
            b_r = np.linalg.lstsq(X_red, Y, rcond=None)[0]
            rss_red = np.sum((Y - X_red @ b_r)**2)
            dfn = X_full.shape[1] - red_cols
            dfd = T - X_full.shape[1]
            if dfd <= 0 or rss_full <= 0 or dfn <= 0: continue
            F = ((rss_red - rss_full) / dfn) / (rss_full / dfd)
            p = 1 - stats.f.cdf(F, dfn, dfd)
            aic = T * np.log(rss_full/T) + 2 * X_full.shape[1]
            if aic < best_aic:
                best_aic = aic; best_lag = lag; best_f = F; best_p = p
        except np.linalg.LinAlgError:
            continue
    return best_f, best_p, best_lag

print('='*60)
print('REVISION STEP 3: PARTIAL GRANGER (CONTROL FOR WIND)')
print('='*60)

# Load precomputed variables
print('\n1. Loading data and computing variables...')
ds_sic = xr.open_dataset(f'{DATA}/era5_sic_SO_1979_2024.nc')
if 'expver' in ds_sic.dims: ds_sic = ds_sic.sel(expver=1)
sic_var = 'siconc' if 'siconc' in ds_sic else 'ci'
sic_data = np.clip(ds_sic[sic_var].values, 0, 1)
lat_s = ds_sic.latitude.values; lon_s = ds_sic.longitude.values
times = pd.to_datetime(ds_sic.valid_time.values)
ds_sic.close()

ds_w = xr.open_dataset(f'{DATA}/era5_wind_SO_1979_2024.nc')
if 'expver' in ds_w.dims: ds_w = ds_w.sel(expver=1)
wspd = np.sqrt(ds_w['u10'].values**2 + ds_w['v10'].values**2)
ds_w.close()

ds_swh = xr.open_dataset(f'{DATA}/era5_waves_SO_1979_2024.nc')
if 'expver' in ds_swh.dims: ds_swh = ds_swh.sel(expver=1)
swh_data = ds_swh['swh'].values
lat_w = ds_swh.latitude.values; lon_w = ds_swh.longitude.values
ds_swh.close()

nt = len(times)
cos_lat = np.cos(np.deg2rad(lat_s))
ice_mask = (lat_s >= -75) & (lat_s <= -55)
swh_lat_idx = np.array([np.argmin(np.abs(lat_w - ls)) for ls in lat_s])

# Compute monthly variables
swh_at_edge = np.full(nt, np.nan)
sic_mean = np.full(nt, np.nan)
wspd_mean = np.full(nt, np.nan)

for t in range(nt):
    swh_vals = []
    for j in range(0, len(lon_s), 2):
        col = sic_data[t, :, j]
        for i in range(len(lat_s)):
            if col[i] > 0.15 and -74 < lat_s[i] < -50:
                eq_i = max(0, i - 8)
                swh_ji = np.argmin(np.abs(lon_w - lon_s[j]))
                sv = swh_data[t, swh_lat_idx[eq_i], swh_ji]
                if np.isfinite(sv): swh_vals.append(sv)
                break
    if swh_vals: swh_at_edge[t] = np.mean(swh_vals)
    w = cos_lat[ice_mask][:, np.newaxis]
    s = sic_data[t, ice_mask, :]; ok = np.isfinite(s)
    sic_mean[t] = np.nansum(s*w)/np.nansum(w*ok) if np.nansum(w*ok)>0 else np.nan
    ws = wspd[t, ice_mask, :]; ok_w = np.isfinite(ws)
    wspd_mean[t] = np.nansum(ws*w)/np.nansum(w*ok_w) if np.nansum(w*ok_w)>0 else np.nan

del sic_data, wspd, swh_data

# Deseasonalize + standardize
months = times.month.values
anom = {}
for name, vals in [('SIC', sic_mean), ('SWH', swh_at_edge), ('Wind', wspd_mean)]:
    clim = np.array([np.nanmean(vals[months == m]) for m in range(1, 13)])
    a = vals - clim[months - 1]
    sigma = np.nanstd(a)
    anom[name] = (a - np.nanmean(a)) / sigma if sigma > 0 else a * 0

ok = np.isfinite(anom['SIC']) & np.isfinite(anom['SWH']) & np.isfinite(anom['Wind'])

# ---- Standard Granger (no control) ----
print('\n2. Standard Granger (no wind control)...')
from p04v2_revision_step1 import granger_test as gt_import
# Redefine to avoid import issues
def granger_test(y, x, max_lag=6):
    n = len(y)
    best_aic = np.inf; best_lag = 1; best_f = 0; best_p = 1
    for lag in range(1, max_lag+1):
        T = n - lag; Y = y[lag:]
        X_full = np.ones((T, 1))
        for l in range(1, lag+1):
            X_full = np.column_stack([X_full, y[lag-l:n-l]])
        x_col = X_full.shape[1]
        for l in range(1, lag+1):
            X_full = np.column_stack([X_full, x[lag-l:n-l]])
        try:
            b = np.linalg.lstsq(X_full, Y, rcond=None)[0]
            rss_full = np.sum((Y - X_full @ b)**2)
            b_r = np.linalg.lstsq(X_full[:, :x_col], Y, rcond=None)[0]
            rss_red = np.sum((Y - X_full[:, :x_col] @ b_r)**2)
            dfn = lag; dfd = T - X_full.shape[1]
            if dfd <= 0 or rss_full <= 0: continue
            F = ((rss_red - rss_full) / dfn) / (rss_full / dfd)
            p = 1 - stats.f.cdf(F, dfn, dfd)
            aic = T * np.log(rss_full/T) + 2 * X_full.shape[1]
            if aic < best_aic:
                best_aic = aic; best_lag = lag; best_f = F; best_p = p
        except np.linalg.LinAlgError:
            continue
    return best_f, best_p, best_lag

F_std, p_std, lag_std = granger_test(anom['SWH'][ok], anom['SIC'][ok])
print(f'  SIC -> SWH (standard):  F={F_std:.2f}, p={p_std:.4f}, lag={lag_std}')

F_wind, p_wind, lag_wind = granger_test(anom['SWH'][ok], anom['Wind'][ok])
print(f'  Wind -> SWH (standard): F={F_wind:.2f}, p={p_wind:.4f}, lag={lag_wind}')

# ---- Partial Granger: SIC -> SWH | Wind ----
print('\n3. Partial Granger: SIC -> SWH | Wind...')
F_partial, p_partial, lag_partial = partial_granger(
    anom['SWH'][ok], anom['SIC'][ok], anom['Wind'][ok])
print(f'  SIC -> SWH | Wind:  F={F_partial:.2f}, p={p_partial:.4f}, lag={lag_partial}')

# ---- Partial Granger: Wind -> SWH | SIC ----
print('\n4. Partial Granger: Wind -> SWH | SIC...')
F_partial_w, p_partial_w, lag_partial_w = partial_granger(
    anom['SWH'][ok], anom['Wind'][ok], anom['SIC'][ok])
print(f'  Wind -> SWH | SIC:  F={F_partial_w:.2f}, p={p_partial_w:.4f}, lag={lag_partial_w}')

# ---- Winter-only partial Granger ----
print('\n5. Winter (JJA) partial Granger...')
jja = np.isin(months, [6, 7, 8])
ok_jja = ok & jja
if ok_jja.sum() >= 50:
    F_jja, p_jja, lag_jja = partial_granger(
        anom['SWH'][ok_jja], anom['SIC'][ok_jja], anom['Wind'][ok_jja])
    print(f'  SIC -> SWH | Wind (JJA): F={F_jja:.2f}, p={p_jja:.4f}, lag={lag_jja}, n={ok_jja.sum()}')
else:
    F_jja, p_jja, lag_jja = 0, 1, 0
    print(f'  JJA: insufficient data ({ok_jja.sum()})')

# Save
results = {
    'standard_SIC_SWH': {'F': round(F_std, 2), 'p': round(p_std, 6), 'lag': lag_std},
    'standard_Wind_SWH': {'F': round(F_wind, 2), 'p': round(p_wind, 6), 'lag': lag_wind},
    'partial_SIC_SWH_given_Wind': {'F': round(F_partial, 2), 'p': round(p_partial, 6), 'lag': lag_partial},
    'partial_Wind_SWH_given_SIC': {'F': round(F_partial_w, 2), 'p': round(p_partial_w, 6), 'lag': lag_partial_w},
    'partial_SIC_SWH_JJA_given_Wind': {'F': round(F_jja, 2), 'p': round(p_jja, 6), 'lag': lag_jja},
}
with open(f'{OUT}/p04v2_revision_step3.json', 'w') as f:
    json.dump(results, f, indent=2)

print(f'\n=== SUMMARY ===')
print(f'Standard:  SIC->SWH p={p_std:.4f}, Wind->SWH p={p_wind:.4f}')
print(f'Partial:   SIC->SWH|Wind p={p_partial:.4f}, Wind->SWH|SIC p={p_partial_w:.4f}')
print(f'JJA only:  SIC->SWH|Wind p={p_jja:.4f}')
print(f'\nIf SIC->SWH|Wind is still significant, the SIC effect is NOT')
print(f'just a confound of wind driving both variables.')
print('\nDone.')

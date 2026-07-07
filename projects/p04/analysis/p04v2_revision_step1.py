#!/usr/bin/env python3
"""
P04 v2 Revision Step 1: Multiple testing correction + sub-period Granger

Addresses Reviewer 1 concerns:
  1. Bonferroni correction on 6 Granger tests
  2. Sub-period Granger (pre-2016 vs post-2016 separately)
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
            X_red = X_full[:, :x_col]
            b_r = np.linalg.lstsq(X_red, Y, rcond=None)[0]
            rss_red = np.sum((Y - X_red @ b_r)**2)
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

print('='*60)
print('REVISION STEP 1: BONFERRONI + SUB-PERIOD GRANGER')
print('='*60)

# Load and prepare data (same as phase2c)
print('\n1. Loading data...')
ds_sic = xr.open_dataset(f'{DATA}/era5_sic_SO_1979_2024.nc')
if 'expver' in ds_sic.dims: ds_sic = ds_sic.sel(expver=1)
sic_var = 'siconc' if 'siconc' in ds_sic else 'ci'
sic = np.clip(ds_sic[sic_var].values, 0, 1)
lat_s = ds_sic.latitude.values; lon_s = ds_sic.longitude.values
times = pd.to_datetime(ds_sic.valid_time.values)
ds_sic.close()

ds_w = xr.open_dataset(f'{DATA}/era5_wind_SO_1979_2024.nc')
if 'expver' in ds_w.dims: ds_w = ds_w.sel(expver=1)
wspd = np.sqrt(ds_w['u10'].values**2 + ds_w['v10'].values**2)
ds_w.close()

ds_swh = xr.open_dataset(f'{DATA}/era5_waves_SO_1979_2024.nc')
if 'expver' in ds_swh.dims: ds_swh = ds_swh.sel(expver=1)
swh = ds_swh['swh'].values; lat_w = ds_swh.latitude.values; ds_swh_lon = ds_swh.longitude.values
ds_swh.close()

nt = len(times)
cos_lat = np.cos(np.deg2rad(lat_s))
ice_mask = (lat_s >= -75) & (lat_s <= -55)
swh_lat_idx = np.array([np.argmin(np.abs(lat_w - ls)) for ls in lat_s])

# Compute ice edge + fetch + SWH at edge
print('2. Computing variables...')
ice_edge_lat = np.full(nt, np.nan)
fetch_proxy = np.full(nt, np.nan)
swh_at_edge = np.full(nt, np.nan)
sic_mean = np.full(nt, np.nan)
wspd_mean = np.full(nt, np.nan)

for t in range(nt):
    edge_lats = []; swh_vals = []
    for j in range(0, len(lon_s), 2):
        col = sic[t, :, j]
        for i in range(len(lat_s)):
            if col[i] > 0.15 and -74 < lat_s[i] < -50:
                edge_lats.append(lat_s[i])
                eq_i = max(0, i - 8)
                lon_w = ds_swh_lon
                swh_ji = np.argmin(np.abs(lon_w - lon_s[j]))
                sv = swh[t, swh_lat_idx[eq_i], swh_ji]
                if np.isfinite(sv): swh_vals.append(sv)
                break
    if edge_lats:
        m = np.mean(edge_lats)
        ice_edge_lat[t] = m
        fetch_proxy[t] = abs(m - (-40.0)) * np.pi / 180 * 6371.0
    if swh_vals:
        swh_at_edge[t] = np.mean(swh_vals)
    w = cos_lat[ice_mask][:, np.newaxis]
    s = sic[t, ice_mask, :]
    ok = np.isfinite(s)
    sic_mean[t] = np.nansum(s*w)/np.nansum(w*ok) if np.nansum(w*ok)>0 else np.nan
    ws = wspd[t, ice_mask, :]
    ok_w = np.isfinite(ws)
    wspd_mean[t] = np.nansum(ws*w)/np.nansum(w*ok_w) if np.nansum(w*ok_w)>0 else np.nan

del sic, wspd, swh

# Deseasonalize
print('3. Deseasonalizing...')
months = times.month.values
variables = {'IceEdge': ice_edge_lat, 'Fetch': fetch_proxy,
             'SWH_edge': swh_at_edge, 'SIC': sic_mean, 'Wind': wspd_mean}
anom = {}
for name, vals in variables.items():
    clim = np.array([np.nanmean(vals[months == m]) for m in range(1, 13)])
    anom[name] = vals - clim[months - 1]

# Standardize
std = {}
for name, vals in anom.items():
    sigma = np.nanstd(vals)
    std[name] = (vals - np.nanmean(vals)) / sigma if sigma > 0 else vals * 0

pairs = [
    ('SIC', 'Fetch', 'SIC -> Fetch'),
    ('Fetch', 'SWH_edge', 'Fetch -> SWH'),
    ('SWH_edge', 'IceEdge', 'SWH -> IceEdge'),
    ('IceEdge', 'SIC', 'IceEdge -> SIC'),
    ('Wind', 'SWH_edge', 'Wind -> SWH'),
    ('SIC', 'SWH_edge', 'SIC -> SWH'),
]

# ---- FULL PERIOD ----
print('\n4. Full period Granger + Bonferroni...')
results_full = []
for x_name, y_name, label in pairs:
    x = std[x_name]; y = std[y_name]
    ok = np.isfinite(x) & np.isfinite(y)
    F, p, lag = granger_test(y[ok], x[ok])
    results_full.append({'label': label, 'F': round(F, 2), 'p': round(p, 6),
                         'p_bonf': round(min(p * 6, 1.0), 6), 'lag': lag})

print(f'  {"Link":25s} {"F":>6s} {"p":>8s} {"p_bonf":>8s} {"lag":>4s}')
for r in results_full:
    sig = '*' if r['p_bonf'] < 0.05 else 'ns'
    print(f'  {r["label"]:25s} {r["F"]:6.2f} {r["p"]:8.4f} {r["p_bonf"]:8.4f} {r["lag"]:4d} {sig}')

# ---- SUB-PERIOD: PRE-2016 ----
print('\n5. Pre-2016 Granger...')
pre_mask = times < '2016-01-01'
results_pre = []
for x_name, y_name, label in pairs:
    x = std[x_name][pre_mask]; y = std[y_name][pre_mask]
    ok = np.isfinite(x) & np.isfinite(y)
    if ok.sum() < 50:
        results_pre.append({'label': label, 'F': 0, 'p': 1, 'p_bonf': 1, 'lag': 0, 'n': int(ok.sum())})
        continue
    F, p, lag = granger_test(y[ok], x[ok])
    results_pre.append({'label': label, 'F': round(F, 2), 'p': round(p, 6),
                        'p_bonf': round(min(p*6, 1.0), 6), 'lag': lag, 'n': int(ok.sum())})

print(f'  {"Link":25s} {"F":>6s} {"p":>8s} {"p_bonf":>8s} {"n":>4s}')
for r in results_pre:
    sig = '*' if r['p_bonf'] < 0.05 else 'ns'
    print(f'  {r["label"]:25s} {r["F"]:6.2f} {r["p"]:8.4f} {r["p_bonf"]:8.4f} {r["n"]:4d} {sig}')

# ---- SUB-PERIOD: POST-2016 ----
print('\n6. Post-2016 Granger...')
post_mask = times >= '2016-01-01'
results_post = []
for x_name, y_name, label in pairs:
    x = std[x_name][post_mask]; y = std[y_name][post_mask]
    ok = np.isfinite(x) & np.isfinite(y)
    if ok.sum() < 50:
        results_post.append({'label': label, 'F': 0, 'p': 1, 'p_bonf': 1, 'lag': 0, 'n': int(ok.sum())})
        continue
    F, p, lag = granger_test(y[ok], x[ok])
    results_post.append({'label': label, 'F': round(F, 2), 'p': round(p, 6),
                         'p_bonf': round(min(p*6, 1.0), 6), 'lag': lag, 'n': int(ok.sum())})

print(f'  {"Link":25s} {"F":>6s} {"p":>8s} {"p_bonf":>8s} {"n":>4s}')
for r in results_post:
    sig = '*' if r['p_bonf'] < 0.05 else 'ns'
    print(f'  {r["label"]:25s} {r["F"]:6.2f} {r["p"]:8.4f} {r["p_bonf"]:8.4f} {r["n"]:4d} {sig}')

# Save
output = {'full': results_full, 'pre2016': results_pre, 'post2016': results_post}
with open(f'{OUT}/p04v2_revision_step1.json', 'w') as f:
    json.dump(output, f, indent=2)
print(f'\nSaved to {OUT}/p04v2_revision_step1.json')
print('Done.')

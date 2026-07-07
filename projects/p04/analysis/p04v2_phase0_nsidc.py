#!/usr/bin/env python3
"""
P04 v2 Phase 0: NSIDC sea ice extent baseline analysis
Uses locally available NSIDC Sea Ice Index CSVs.

Produces:
  1. Annual mean extent time series + Pettitt change point
  2. Seasonal breakdown (DJF/MAM/JJA/SON) to identify which seasons drive the decline
  3. MIZ-proxy: month-to-month variability as proxy for MIZ instability
"""

import numpy as np
import pandas as pd
from pathlib import Path
from scipy import stats
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt

REPO = str(Path(__file__).resolve().parents[3])
DATA = f'{REPO}/data/NSIDC Sea Ice Index'
FIG = f'{REPO}/projects/p04/figures'
OUT = f'{REPO}/projects/p04/analysis'
Path(FIG).mkdir(parents=True, exist_ok=True)

def pettitt_test(y):
    n = len(y)
    U = np.zeros(n)
    for t in range(1, n):
        s = 0
        for i in range(t):
            for j in range(t, n):
                s += np.sign(y[i] - y[j])
        U[t] = abs(s)
    K = U.max()
    cp = int(U.argmax())
    p = 2 * np.exp(-6 * K**2 / (n**3 + n**2))
    return cp, K, p

# Load all months
print('Loading NSIDC Sea Ice Index...')
all_data = []
for m in range(1, 13):
    fp = f'{DATA}/S_{m:02d}_extent_v4.0.csv'
    df = pd.read_csv(fp, skiprows=1, names=['year','mo','source','region','extent','area'])
    df['year'] = df['year'].astype(int)
    df['extent'] = pd.to_numeric(df['extent'], errors='coerce')
    df['area'] = pd.to_numeric(df['area'], errors='coerce')
    df.loc[df['extent'] < -100, 'extent'] = np.nan
    for _, row in df.iterrows():
        all_data.append({'year': row['year'], 'month': m,
                        'extent': row['extent'], 'area': row['area']})

df = pd.DataFrame(all_data)
df['time'] = pd.to_datetime(df.apply(lambda r: f"{int(r['year'])}-{int(r['month']):02d}-01", axis=1))
df = df.sort_values('time').dropna(subset=['extent'])
print(f'  {len(df)} monthly records, {df.year.min()}-{df.year.max()}')

# Annual means
ann = df.groupby('year')['extent'].mean()
ann = ann[ann.index >= 1979]

# Seasonal means
seasons = {'DJF': [12, 1, 2], 'MAM': [3, 4, 5], 'JJA': [6, 7, 8], 'SON': [9, 10, 11]}
seasonal = {}
for sname, months in seasons.items():
    mask = df['month'].isin(months) & (df['year'] >= 1979)
    seasonal[sname] = df[mask].groupby('year')['extent'].mean()

# Pettitt test on annual
print('\nPettitt change point detection (annual extent):')
vals = ann.values
yrs = ann.index.values
cp_idx, K, p = pettitt_test(vals)
cp_year = yrs[cp_idx]
pre_mean = vals[:cp_idx].mean()
post_mean = vals[cp_idx:].mean()
pct_change = (post_mean - pre_mean) / pre_mean * 100
sig = '***' if p < 0.001 else '**' if p < 0.01 else '*' if p < 0.05 else 'ns'
print(f'  CP = {cp_year}, K = {K:.0f}, p = {p:.4f} {sig}')
print(f'  Pre: {pre_mean:.2f}, Post: {post_mean:.2f} ({pct_change:+.1f}%)')

# Pettitt for each season
print('\nSeasonal Pettitt tests:')
for sname, s in seasonal.items():
    sv = s.values
    sy = s.index.values
    ok = np.isfinite(sv)
    if ok.sum() < 15:
        print(f'  {sname}: insufficient data')
        continue
    ci, Ki, pi = pettitt_test(sv[ok])
    cyr = sy[ok][ci]
    pre_s = sv[ok][:ci].mean()
    post_s = sv[ok][ci:].mean()
    pct_s = (post_s - pre_s) / pre_s * 100
    sig_s = '***' if pi < 0.001 else '**' if pi < 0.01 else '*' if pi < 0.05 else 'ns'
    print(f'  {sname}: CP={cyr}, p={pi:.4f} {sig_s}, {pre_s:.2f} → {post_s:.2f} ({pct_s:+.1f}%)')

# Trend analysis: pre-2016 vs post-2016
print('\nLinear trends:')
for label, mask in [('Full (1979-2024)', slice(None)),
                     ('Pre-2016', yrs < 2016),
                     ('Post-2016', yrs >= 2016)]:
    y = vals[mask]
    x = yrs[mask].astype(float)
    if len(y) < 3:
        continue
    slope, intercept, r, pv, se = stats.linregress(x, y)
    print(f'  {label}: slope = {slope:.4f} Mkm²/yr, R² = {r**2:.3f}, p = {pv:.4f}')

# ---- Figures ----
plt.rcParams.update({'font.size': 11, 'figure.dpi': 150})

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel A: Annual mean + change point
ax = axes[0, 0]
ax.plot(yrs, vals, 'o-', color='steelblue', lw=1.5, ms=4)
ax.axvline(cp_year, color='r', ls='--', lw=1.5, alpha=0.7)
ax.axhline(pre_mean, color='steelblue', ls=':', lw=1, alpha=0.5)
ax.axhline(post_mean, color='red', ls=':', lw=1, alpha=0.5)
ax.fill_between([yrs[0], cp_year], pre_mean-0.5, pre_mean+0.5, alpha=0.1, color='blue')
ax.fill_between([cp_year, yrs[-1]], post_mean-0.5, post_mean+0.5, alpha=0.1, color='red')
ax.set_ylabel('Extent (million km²)')
ax.set_title(f'(a) Annual Mean Extent\nPettitt CP={cp_year}, p={p:.4f} {sig}')
ax.grid(True, alpha=0.3)

# Panel B: Seasonal trends
ax = axes[0, 1]
colors = {'DJF': '#e41a1c', 'MAM': '#ff7f00', 'JJA': '#377eb8', 'SON': '#4daf4a'}
for sname, s in seasonal.items():
    ax.plot(s.index, s.values, 'o-', color=colors[sname], lw=1, ms=3, label=sname, alpha=0.8)
ax.axvline(cp_year, color='k', ls='--', lw=1, alpha=0.5)
ax.set_ylabel('Extent (million km²)')
ax.set_title('(b) Seasonal Mean Extent')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel C: Monthly time series
ax = axes[1, 0]
ax.plot(df['time'], df['extent'], color='steelblue', lw=0.3, alpha=0.5)
roll = df.set_index('time')['extent'].rolling(12, center=True).mean()
ax.plot(roll.index, roll.values, 'k-', lw=1.5, label='12-mo mean')
ax.axvline(pd.Timestamp(f'{cp_year}-01-01'), color='r', ls='--', lw=1.5, alpha=0.7)
ax.set_ylabel('Extent (million km²)')
ax.set_title('(c) Monthly Extent + 12-mo Running Mean')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel D: Year-to-year change (acceleration)
ax = axes[1, 1]
dext = np.diff(vals)
ax.bar(yrs[1:], dext, color=['red' if d < 0 else 'steelblue' for d in dext], alpha=0.7)
ax.axhline(0, color='k', lw=0.5)
ax.axvline(cp_year, color='k', ls='--', lw=1, alpha=0.5)
ax.set_ylabel('ΔExtent (million km²/yr)')
ax.set_title('(d) Year-to-Year Change')
ax.grid(True, alpha=0.3)

plt.suptitle('P04 v2: Antarctic Sea Ice Extent Baseline (NSIDC)', fontsize=14, y=1.01)
plt.tight_layout()
plt.savefig(f'{FIG}/p04v2_fig_nsidc_baseline.png', bbox_inches='tight')
plt.close()
print(f'\n  -> {FIG}/p04v2_fig_nsidc_baseline.png')

# Save summary
with open(f'{OUT}/p04v2_nsidc_summary.txt', 'w') as f:
    f.write(f'Pettitt CP: {cp_year}, K={K:.0f}, p={p:.6f}\n')
    f.write(f'Pre-{cp_year} mean: {pre_mean:.3f} Mkm²\n')
    f.write(f'Post-{cp_year} mean: {post_mean:.3f} Mkm² ({pct_change:+.1f}%)\n')
    for label, mask in [('Full', slice(None)), ('Pre-2016', yrs < 2016), ('Post-2016', yrs >= 2016)]:
        y = vals[mask]; x = yrs[mask].astype(float)
        if len(y) >= 3:
            slope, _, r, pv, _ = stats.linregress(x, y)
            f.write(f'{label} trend: {slope:.4f} Mkm²/yr, R²={r**2:.3f}, p={pv:.4f}\n')

print('\nDone.')

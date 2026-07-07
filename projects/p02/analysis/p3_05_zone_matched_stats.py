"""
P3-05: Zone-matched statistics for the historical (n=84) robustness metrics.

Two purposes:
1. Expose and correct the zone-composition confound in the naive
   kelvin-vs-rossby comparison: the westward Rossby control starts at
   zone_east + 25 deg, which for the TIW zone (245+20+25 = 290E) exceeds
   the domain, so the Rossby group contains NO TIW-zone measurements while
   the Kelvin group does. Cross-group comparisons must be zone-matched.
2. Test the paper's central observational claim with the 30-year sample:
   TIW-zone amplitude loss versus island-chain preservation (Kelvin rays,
   rms_up > 0.01 m quality filter), block bootstrap with events as blocks.

Input:  data/duacs/robustness_metrics_historical.json (from p3_04, remote)
Output: data/duacs/zone_matched_stats_historical.json
"""
import json
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parents[1]
IN = BASE / "data" / "duacs" / "robustness_metrics_historical.json"
OUT = BASE / "data" / "duacs" / "zone_matched_stats_historical.json"

RMS_UP_MIN = 0.01
N_BOOT = 10000
rng = np.random.default_rng(2026)

with open(IN) as f:
    R = json.load(f)


def by_event(data, zones=None, metric="amp_ratio", rms_min=0.0):
    d = {}
    for r in data:
        if zones and r["zone"] not in zones:
            continue
        if r["rms_up"] < rms_min:
            continue
        d.setdefault(r["event"], []).append(r[metric])
    return d


def boot_diff(da, db):
    common = sorted(set(da) & set(db))
    a = [np.mean(da[e]) for e in common]
    b = [np.mean(db[e]) for e in common]
    obs = float(np.mean(a) - np.mean(b))
    n = len(common)
    diffs = []
    for _ in range(N_BOOT):
        i = rng.integers(0, n, n)
        diffs.append(np.mean([a[j] for j in i]) - np.mean([b[j] for j in i]))
    lo, hi = (float(x) for x in np.percentile(diffs, [2.5, 97.5]))
    return {"diff": round(obs, 4), "ci": [round(lo, 4), round(hi, 4)],
            "n_events": n, "significant": bool(lo > 0 or hi < 0)}


results = {}

# zone composition (documents the rossby gap)
results["zone_composition"] = {
    g: {z: sum(1 for r in R[g] if r["zone"] == z)
        for z in sorted({r["zone"] for r in R[g]})}
    for g in R
}

# corrected control comparisons (zone-matched)
isl = ["Gilbert Islands", "Line Islands"]
results["kelvin_vs_rossby_islands_only"] = boot_diff(
    by_event(R["kelvin"], isl), by_event(R["rossby"], isl))
results["kelvin_vs_stationary_all_zones"] = boot_diff(
    by_event(R["kelvin"]), by_event(R["stationary"]))
results["kelvin_vs_time_shifted_all_zones"] = boot_diff(
    by_event(R["kelvin"]), by_event(R["time_shifted"]))

# central claim: perturbation-type dependence within the Kelvin group
tiw = by_event(R["kelvin"], ["TIW zone"], rms_min=RMS_UP_MIN)
line = by_event(R["kelvin"], ["Line Islands"], rms_min=RMS_UP_MIN)
gil = by_event(R["kelvin"], ["Gilbert Islands"], rms_min=RMS_UP_MIN)
results["tiw_minus_line_amp_ratio"] = boot_diff(tiw, line)
results["tiw_minus_gilbert_amp_ratio"] = boot_diff(tiw, gil)
results["zone_means"] = {
    name: {"mean": round(float(np.mean(v)), 3),
           "median": round(float(np.median(v)), 3), "n": len(v)}
    for name, v in [("TIW zone", [x for vs in tiw.values() for x in vs]),
                    ("Line Islands", [x for vs in line.values() for x in vs]),
                    ("Gilbert Islands", [x for vs in gil.values() for x in vs])]
}

with open(OUT, "w") as f:
    json.dump(results, f, indent=2)

for k, v in results.items():
    print(k, "->", json.dumps(v))
print(f"\nSaved: {OUT}")

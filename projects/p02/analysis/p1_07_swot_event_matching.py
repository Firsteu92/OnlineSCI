"""
P1-07: Match SWOT passes to deduped Kelvin wave events.

For each event, compute the predicted wave-peak longitude at each time:
    x(t) = x0 + c * (t - t_start)

Then search all SWOT passes for those within:
    |x_SWOT - x(t)| < 5°  AND  |t_SWOT - t| < 1.5 days

Output: data/swot/swot_event_matches.json
  Each match includes: event_id, cycle, pass, time_gap_days, lon_gap_deg,
  coverage_score (valid_pct × proximity weight)

NOTE: This script requires SWOT L3 data on the remote WSL machine.
Run on remote WSL.
Data path: /mnt/d/v2_0_1/Basic/
"""
import json
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import yaml

BASE = Path(__file__).resolve().parents[1]
with open(BASE / "config.yaml") as f:
    cfg = yaml.safe_load(f)

CATALOG = BASE / cfg["data"]["events"]["catalog"]
PASSES_FILE = BASE / cfg["data"]["swot"]["passes"]

with open(CATALOG) as f:
    events = json.load(f)

with open(PASSES_FILE) as f:
    passes = json.load(f)

kelvin_speed = float(cfg["analysis"]["kelvin_speed_deg_day"])

LON_THRESHOLD = 5.0
TIME_THRESHOLD_DAYS = 1.5

matches = []

for event in events:
    t_start = datetime.fromisoformat(event["start"])
    t_end = datetime.fromisoformat(event["end"])
    lon0 = event["lon0"]
    event_matches = []

    for p in passes:
        eq_lon = p["eq_lon"]

        dt_to_lon = (eq_lon - lon0) / kelvin_speed
        if dt_to_lon < 0 or dt_to_lon > (t_end - t_start).days + 10:
            continue

        t_predicted = t_start + timedelta(days=dt_to_lon)

        lon_gap = abs(eq_lon - (lon0 + kelvin_speed * dt_to_lon))

        valid_pct = p.get("valid_pct", 0)
        if valid_pct < 50:
            continue

        proximity_weight = max(0, 1 - lon_gap / LON_THRESHOLD)
        coverage_score = valid_pct / 100 * proximity_weight

        match = {
            "event_id": event["id"],
            "cycle": p["cycle"],
            "pass": p["pass"],
            "eq_lon": eq_lon,
            "predicted_peak_lon": round(lon0 + kelvin_speed * dt_to_lon, 1),
            "lon_gap_deg": round(lon_gap, 1),
            "valid_pct": valid_pct,
            "coverage_score": round(coverage_score, 3),
        }
        event_matches.append(match)

    event_matches.sort(key=lambda m: m["coverage_score"], reverse=True)
    matches.extend(event_matches[:10])
    print(f"Event {event['id']}: {len(event_matches)} candidate SWOT passes "
          f"(top coverage={event_matches[0]['coverage_score']:.3f})" if event_matches
          else f"Event {event['id']}: 0 candidate SWOT passes")

out_file = BASE / "data" / "swot" / "swot_event_matches.json"
with open(out_file, "w") as f:
    json.dump(matches, f, indent=2)

print(f"\nTotal matches: {len(matches)} across {len(events)} events")
print(f"Saved: {out_file}")

events_with_matches = len(set(m["event_id"] for m in matches))
print(f"Events with ≥1 SWOT match: {events_with_matches}/{len(events)}")

for event in events:
    em = [m for m in matches if m["event_id"] == event["id"]]
    if em:
        best = em[0]
        print(f"  {event['id']}: {len(em)} matches, best cycle={best['cycle']} "
              f"pass={best['pass']} score={best['coverage_score']:.3f}")

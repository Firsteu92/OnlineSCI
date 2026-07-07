"""
P0-05 (remote, office WSL): GLORYS12 surface u,v for historical events.

Reads the historical catalog (p1_08) and downloads one subset per
event x perturbation zone, same windows as p4_01 used for the 2023 events.
Handles the my/myint dataset boundary (GLORYS12 multiyear ends 2021-06-30;
later dates use the interim product).

Run AFTER p1_08 completes:
  python3 p0_05_download_glorys_historical.py

Output: /mnt/d/p02_data/glorys_hist/glorys_uv_<KH>_<zone>.nc
"""
import json
import os
import sys

import copernicusmarine

DATA_DIR = "/mnt/d/p02_data"
CATALOG = os.path.join(DATA_DIR, "duacs_hist", "kelvin_event_catalog_historical.json")
OUT_DIR = os.path.join(DATA_DIR, "glorys_hist")
os.makedirs(OUT_DIR, exist_ok=True)

MY_END = "2021-06-30"
DS_MY = "cmems_mod_glo_phy_my_0.083deg_P1D-m"
DS_MYINT = "cmems_mod_glo_phy_myint_0.083deg_P1D-m"

zones = [
    {"name": "Gilbert Islands", "lon": 175, "width": 8},
    {"name": "Line Islands", "lon": 202, "width": 8},
    {"name": "TIW zone", "lon": 245, "width": 20},
]

with open(CATALOG) as f:
    events = json.load(f)
print(f"{len(events)} events x {len(zones)} zones", flush=True)

n_ok = n_skip = n_fail = 0
for ev in events:
    dataset = DS_MY if ev["end"] <= MY_END else DS_MYINT
    for z in zones:
        tag = z["name"].replace(" ", "_")
        out = os.path.join(OUT_DIR, f"glorys_uv_{ev['id']}_{tag}.nc")
        if os.path.exists(out):
            n_skip += 1
            continue
        lon_c = z["lon"] - 360 if z["lon"] > 180 else z["lon"]
        try:
            copernicusmarine.subset(
                dataset_id=dataset,
                variables=["uo", "vo"],
                minimum_longitude=lon_c - z["width"] - 5,
                maximum_longitude=lon_c + z["width"] + 5,
                minimum_latitude=-5, maximum_latitude=5,
                start_datetime=f"{ev['start']}T00:00:00",
                end_datetime=f"{ev['end']}T23:59:59",
                minimum_depth=0, maximum_depth=1,
                output_filename=os.path.basename(out),
                output_directory=OUT_DIR,
                disable_progress_bar=True,
            )
            n_ok += 1
            print(f"{ev['id']} x {tag}: done ({dataset.split('_')[3]})", flush=True)
        except Exception as e:
            n_fail += 1
            print(f"{ev['id']} x {tag}: FAILED — {str(e)[:100]}", flush=True)

print(f"GLORYS DONE: {n_ok} downloaded, {n_skip} cached, {n_fail} failed", flush=True)

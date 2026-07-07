# SWOT Simulator & OSSE Planning Notes (ClaudeB)

> Phase 2 preparation. Findings from pre-research on OSSE tools.

## SWOT Simulator Tool

**Primary tool**: CNES/swot_simulator
- GitHub: https://github.com/CNES/swot_simulator
- Docs: https://swot-simulator.readthedocs.io
- Python ≥ 3.6, deps: numpy, scipy, xarray, netCDF4, numba, pyinterp

**Capabilities**:
- Takes arbitrary SSH field (NetCDF) → simulated SWOT swath observations
- Orbit options: science orbit (21-day repeat), calval fast orbit (1-day), contingency
- Error budget: KaRIn noise (SWH-dependent), roll error, baseline dilation, phase, timing, wet tropo
- Nadir gap (~20 km) inherently modeled
- Output: ssh_karin, ssh_karin_true, individual error fields

## Shortcut: Pre-computed SWOT Synthetic Products

**Critical finding**: AVISO and PO.DAAC provide pre-computed simulated SWOT L2 SSH based on LLC4320 and GLORYS. These are already orbit-sampled + noise-added.

- AVISO: https://www.aviso.altimetry.fr → simulated SWOT products
- PO.DAAC: pre-launch synthetic SWOT SSH datasets (released 2022-01)

**Implication for P02**: If the equatorial Pacific region is covered in these products, A can skip running the simulator entirely for the OSSE Phase 2a. Instead:
1. Download pre-computed SWOT-sampled LLC4320 SSH for equatorial Pacific
2. Use original LLC4320 as "truth"
3. Apply mode decomposition pipeline to both
4. Quantify error

This could save 2+ weeks in Phase 2.

## OSSE Design for Equatorial Wave Decomposition

### Tier 1: Pre-computed products (if available for equatorial Pacific)

1. Get LLC4320 SSH original + SWOT-sampled version from AVISO/PO.DAAC
2. Extract Kelvin/Yanai events from LLC4320 truth (Hovmöller + known dynamics)
3. Apply full analysis pipeline to SWOT-sampled data
4. Compare: mode amplitudes, robustness metrics (B, C, M, L), Λ values

### Tier 2: Custom simulator run (if Tier 1 doesn't cover region/period)

1. Run 1.5-layer equatorial shallow water model (Matsuno 1966 setup)
2. Generate synthetic Kelvin + Yanai + Rossby + TIW signals
3. Add background perturbations (mean shear, vortex field, island topography)
4. Run CNES/swot_simulator with science orbit
5. Apply analysis pipeline to simulator output
6. Compare with known truth

### Tier 3: Hybrid

Use LLC4320 for realistic background + inject controlled synthetic Kelvin wave perturbations. This gives realistic noise + known signal.

## No Existing Equatorial Wave OSSE

No prior study has used the SWOT simulator specifically for equatorial wave mode decomposition. Relevant prior work:
- Benkiran et al. (2021, Frontiers) — SWOT data assimilation, TIW region improvements
- Li et al. (2019, JGR-Oceans) — equatorial upwelling region OSSE

P02's OSSE would be novel.

## Recommendation

A should first check whether the pre-computed AVISO/PO.DAAC SWOT synthetic products cover the equatorial Pacific for a time period with known Kelvin wave activity. If yes, start with Tier 1 (much faster). If not, proceed with Tier 2.

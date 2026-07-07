# Response to Editor and Reviewer R0

**Project:** P03 — Testing Neglected Eddy Boundary Signals with SWOT Altimetry
**Revision:** R1 (2026-06-15)
**Type:** Project-stage continuous revision after Stage-1 prototype completion

---

## Part A: What We Have Done (已完成)

### Stage-1 Rim-Radius Offset Pilot — Completed with Corrected Pipeline

The original P03 D0 proposal tested whether SWOT systematically shifts the high-gradient eddy rim radius relative to DUACS/PET. We completed the Stage-1 prototype with the following concrete outputs:

**Data pipeline (all completed):**

| Step | Content | Output |
|------|---------|--------|
| st_01 | DUACS PET eddy detection (816 days) | 1632 NC files |
| st_02 | Kuroshio eddy center extraction | 36,543 eddy centers |
| st_03a | SWOT pass scanning | 2,891 passes |
| st_03b | SWOT-eddy matching | 7,057 matches |
| st_03c | Case selection | 16 prototype cases |
| FIG_01 | Radial profile comparison (v2 corrected) | 16 figures |

**v2 corrections applied:**
- DUACS: ADT → SLA (anomaly field, not absolute)
- Gradient index spacing → explicit lon/lat grid spacing
- SWOT gradient computation → local Cartesian plane fitting (not lat/lon fitting)
- Single 360° profile → three-line comparison (full / masked / SWOT)
- Added 4 QC gates
- Units: ×1000 → ×1e6 µm/m

**Stage-1 result — 5 clean cases:**

| Case | Polarity | R_PET (km) | R_DUACS_masked (km) | R_SWOT (km) | ΔR (km) |
|------|----------|-----------|---------------------|-------------|---------|
| 02 | AE | 59 | 47 | 79 | +32 |
| 05 | CE | 52 | 55 | 51 | −4 |
| 12 | AE | 43 | 65 | 99 | +34 |
| 13 | AE | 166 | 129 | 125 | −4 |
| 14 | AE | 168 | 117 | 115 | −2 |

**The five clean cases have mixed-sign ΔR values (+32, −4, +34, −4, −2 km). The sample is not large enough to estimate a population median reliably. The results do not support rim-radius offset as a robust primary hypothesis.**

This is not a "failed" experiment. It excludes a lower-level interpretation: SWOT does not simply shift the conventional eddy boundary systematically outward or inward. The null/weak result is informative — it tells us the missing variable is not the mean rim radius.

---

## Part B: Why We Revised the Direction (方向调整依据)

The Stage-1 result prompted us to re-examine the literature with a different question: if SWOT is not simply redrawing the eddy rim, what IS it seeing around catalogued eddies that conventional altimetry cannot?

Two recent papers provided the framework for a revised question:

1. **Zhang et al. (2019, Nature Communications):** Demonstrated that mesoscale geostrophic strain rate (S_g) is a stronger organizing variable for ageostrophic kinetic energy and chlorophyll response than geostrophic kinetic energy, using a global drifter–altimetry–ocean-color framework. The key methodological insight is predictor-response separation: define the physical strain predictor first, then test the tracer response independently.

2. **Dong et al. (2025, Nature Communications):** Showed that strain along mesoscale eddy edges can sharpen lateral buoyancy gradients through frontogenesis, drive ageostrophic secondary circulation, and produce warm-ring SST responses (~0.4°C, 1–10 km scale) around both cyclones and anticyclones in the Lofoten Basin. This provides mechanism support: eddy-edge strain can organize surface thermal responses.

These papers, combined with Archer et al. (2025, Nature) establishing SWOT's capability to resolve 1–100 km fine-scale SSH globally, led us to a revised question that is a **deepening, not a replacement**, of the original P03:

> **Do catalogued mesoscale eddies show statistically significant SWOT-resolved peripheral fine-scale strain enhancement relative to matched controls?**

This is NOT a new project. We inherit:
- The same eddy registry (DUACS/PET, 7,057 SWOT–eddy matches)
- The same processing chain (SwotDiag fitting kernel, Archer pipeline, De Marez gap-handling)
- The same core strategy (AVISO detect → SWOT measure)
- The Stage-1 conclusion as the logical foundation

---

## Part C: Revised Design (下一步计划)

### C1. Two-Layer Lock-Box Framework

```
Layer 1 (SWOT-only physical test):
  Define peripheral strain state using ONLY SWOT SSH.
  Do not touch SST or Chl-a at this stage.

Layer 2 (Independent tracer response):
  Only after Layer 1 signal survives controls,
  test whether strain-rich eddies show stronger SST/Chl-a signatures.
```

This prevents circularity: we do not use tracer fields to define the physical state.

### C2. Control Suite (three matched controls + one sensitivity stratification)

| Control | Type | Method | Confound Addressed |
|---------|------|--------|-------------------|
| A: Same-swath random | Secondary matched | Random centers on same swath, same latitude, same coverage | Swath geometry + observation noise |
| B: Local displaced | **Primary matched** | Real eddy center shifted by 3–5R | Large-scale currents + frontal environment |
| C: Background-strain matched | Secondary matched | Matched on low-pass DUACS strain/EKE | "Eddies prefer high-strain regions" |
| D: Isolated-eddy subset | Sensitivity stratification | Exclude eddies with neighbors < 3R | Eddy-eddy interaction / saddle misattribution |

**Additional mandatory sensitivity (Exp 3):** Front-orientation control — rotate eddy-relative annulus by random azimuth to test whether excess strain is specific to eddy-relative coordinates or aligned with background front orientation.

### C3. Five-Experiment Route (for Stage 2 development)

| Exp | Question | Output |
|-----|---------|--------|
| 1 | Does excess peripheral strain exist? | Radial profile E(r/R), composite maps |
| 2 | Spatial extent & filter-scale sensitivity? | Heatmap (filter × r/R), regional profiles |
| 3 | Artifact exclusion (4 controls)? | Control summary, retained effect size |
| 4 | Does peripheral strain predict SST/Chl-a response? | F_edge vs tracer, quantile composites |
| 5 | Distribution morphology (continuous vs. bimodal)? | Distribution, dip test |

### C4. Key Guardrails (已定)

1. We do NOT claim eddy peripheries are more important than eddy cores. Frame: core mode + peripheral strain mode coexist.
2. We do NOT claim genesis in the first-stage analysis. First claim: eddy-associated peripheral strain excess after matched controls.
3. We do NOT use "halo" as a primary term. Main term: **eddy-periphery fine-scale strain enhancement**. "Halo" only if data support annular continuity + radial localization + azimuthal coverage.
4. We do NOT split P03 into sub-projects. This is a continuous P03 revision.
5. We do NOT claim causation for tracer response. Language: "predicts / covaries with."

### C5. Statistical Design

- **Sampling unit:** individual eddy snapshot (SWOT–eddy match), not pixel. For eddies with multiple SWOT matches, use clustered bootstrap by eddy ID or average to one eddy-level statistic.
- **Primary control:** local displaced centers (Control B), because it best preserves regional background while removing eddy-centric organization. Controls A and C serve as secondary validation; Control D (isolated subset) is a sensitivity stratification, not a matched control.
- **Primary statistic:** E_i = S_periphery_i − S_displaced_control_i (eddy-level strain excess relative to primary control).
- **Primary test:** clustered bootstrap confidence interval on median E_i (eddy ID as resampling unit). Report effect size (median difference or Cliff's delta) with 95% CI.
- **Claim survives controls only if:** excess strain is positive under primary control (B) AND at least two secondary controls (A, C) show consistent sign.
- **Inclusion threshold:** N ≥ 30 eddy snapshots per stratum for exploratory display; primary claims require effect-size stability under bootstrap.

### C6. Temporal Sampling and Snapshot Validity (Response to Editor Comment 4)

We acknowledge the editor's concern that SWOT's 21-day repeat cycle limits temporal interpretation. The revised P03 makes only **snapshot statistical claims**. Our approach to this limitation:

1. **Snapshot claim only.** The primary physical test asks whether SWOT snapshots, when composited across many parent eddies, show statistically significant peripheral fine-scale strain enhancement. We do not track individual eddy evolution or claim persistence of peripheral strain structures between SWOT revisits.

2. **Eddy lifecycle stratification.** PET tracking provides eddy age, translation speed, and lifecycle stage for each match. We will stratify by young (<30 day), mature (30–100 day), and old (>100 day) eddies to test whether peripheral strain enhancement varies with lifecycle phase.

3. **Repeated-sampling handling.** If the same eddy appears in multiple SWOT matches, we will use clustered bootstrap by eddy ID to avoid pseudoreplication, or average to one eddy-level statistic before significance testing.

4. **Tracer lag windows.** For the gated tracer-response extension, we use ±1–3 day lag windows relative to the SWOT snapshot — not the 21-day revisit — to test association between instantaneous strain state and near-synchronous tracer fields.

5. **Strain decorrelation timescale.** Before Stage 2, we will review eddy-resolving model literature to estimate the expected decorrelation time of peripheral fine-scale strain around mesoscale eddies. This will provide upper-bound guidance on snapshot validity and inform any temporal-persistence claims.

This limitation is now explicit in the guardrails: **we do not interpret SWOT snapshots as temporal persistence or lifecycle claims without separate validation.**

---

## Response to Specific Reviewer Comments

### Reviewer Major 1 — Novelty beyond resolution improvement

**Status of original issue:** Stage 1 tested the rim-radius-offset hypothesis and found no robust systematic offset — the five clean cases have mixed-sign ΔR values. Stage 1 therefore addresses one lower-level version of the resolution concern: SWOT does not simply impose a systematic rim-radius displacement. The revised strain-enhancement hypothesis still requires matched controls and filter-scale sensitivity tests to rule out resolution artifacts.

**How this changes P03:** We no longer claim systematic rim-radius displacement. The revised question — peripheral strain enhancement after matched controls — is a qualitatively different physical claim than a resolution comparison.

**Next implementation:** The revised primary physical test will evaluate control-subtracted strain excess across matched controls.

### Reviewer Major 2 — Fair-resolution test

**Status of original issue:** The original binary survives/disappears test was logically weak, as the reviewer noted. Stage 1's continuous scale-sensitivity approach confirmed that signal stability depends on filter-scale choices.

**How this changes P03:** We replaced the binary test with a continuous filter-scale sweep (30/50/70/100 km high-pass). The question is whether the eddy-associated strain excess is stable across a reasonable range of scale choices.

### Reviewer Major 3 — Background front confound

**Status of original issue:** The reviewer correctly noted that apparent rim tracer anomalies could be explained by pre-existing background fronts. The Stage-1 analysis and the R0 critique together made clear that tracer-aligned comparisons without matched physical controls would be insufficient to distinguish eddy-associated signals from background fronts.

**How this changes P03:** This is now addressed by the two-layer lock-box design. Tracer fields (SST, Chl-a) are NOT used to define the physical state.

**Front-orientation control (promoted to Exp 3):** We have promoted front-orientation testing from a planned tracer-stage extension to a mandatory Exp 3 sensitivity test. The procedure:
1. Match background SST gradient magnitude and orientation near each eddy.
2. Rotate the eddy-relative annulus by a random azimuth and recompute E(r/R).
3. Compare true periphery strain excess with front-parallel pseudo-periphery strain.
4. Report whether the excess strain is specific to the eddy-relative coordinate, or equally well explained by alignment with the background front.

**Synthetic-front null for tracer causality (Response to Editor Comment 2):** For the gated tracer-response stage, we will implement an explicit synthetic-front null model beyond the physical matched controls:
1. Generate synthetic SST and Chl-a fields that preserve the observed large-scale gradient spectrum, seasonal cycle, and front width distribution of the study region, but contain no eddy-organized tracer structure.
2. Apply the same SWOT sampling masks, eddy positions, and F_edge labels to these synthetic fields.
3. Run the same composite pipeline and report the false-positive rate: how often do synthetic fields produce an F_edge–tracer association as strong as observed?
4. The observed association is considered robust only if it exceeds the 95th percentile of the synthetic-null distribution.

This directly addresses Editor Comment #2 and replaces the previous generic commitment with a concrete protocol.

### Reviewer Major 4 — PET as baseline

**Status of original issue:** Stage 1 confirmed that comparing SWOT-derived and PET-derived geometric radii embeds DUACS gridding and algorithm choices into the comparison. The reviewer correctly identified this as a confound.

**How this changes P03:** In the revised design, PET/DUACS provides only the parent-eddy registry (center, polarity, radius, amplitude, age). It is no longer the comparison target. The primary comparison is SWOT peripheral strain vs. matched controls, not SWOT vs. PET.

### Reviewer Major 5 — PACE sample size

PACE remains exploratory. Minimum threshold: N ≥ 30 cloud-free collocations per region before inclusion in primary figures. SST and OC-CCI Chl-a are the primary tracer products.

---

## Summary

| Aspect | Original D0 (2026-06-07) | Revised (2026-06-15) |
|--------|-------------------------|---------------------|
| Core question | Does SWOT shift the eddy rim? | Do eddies show peripheral strain enhancement? |
| Primary metric | ΔR (rim radius offset) | E_i (control-subtracted strain excess) |
| Comparison target | DUACS/PET radius | Matched controls (4 types) |
| Tracer role | Part of primary claim | Independent response, lock-box gated |
| PET role | Baseline for comparison | Parent-eddy registry only |
| Main term | Eddy rim / boundary | Eddy-periphery fine-scale strain enhancement |
| Publication framing | Resolution comparison risk | Physical organization test |

---

> **Core statement:**
> P03 began by testing whether SWOT redraws the eddy rim. The corrected Stage-1 prototype shows that systematic rim-radius displacement is not the missing variable — the five clean cases have mixed ΔR signs and no stable bias. The revised P03 now tests whether SWOT reveals eddy-associated fine-scale strain enhancement around catalogued mesoscale eddies — a peripheral strain mode that coexists with traditional core-mode eddy impacts and can be evaluated against independent SST and Chl-a responses.

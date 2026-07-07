# P04 Editorial Decision — R0

**Journal:** Nature Climate Change
**Manuscript:** SWOT KaRIn Reveals Antarctic Sea Ice Tipping Point Signals
**Decision: Major Revision**
**Date:** 2026-06-08

---

Dear Authors,

The question of whether the post-2016 Antarctic sea ice decline constitutes a climate tipping point is among the most pressing in contemporary climate science. We believe this work has significant potential, but several fundamental issues must be addressed before it can proceed to peer review.

## Revision Requirements

### R1. Replace synthetic data with real observations (highest priority)

The current `p04_analysis.py` generates all data synthetically using `np.random.default_rng`. All figures and quantitative conclusions (SSH variability increase of 30–50%, EKE increase of 20–40%) are predetermined inputs, not computed results. This must be completely rebuilt using real observational data:

| Variable | Data Source | Access |
|---|---|---|
| Sea ice concentration/extent | NSIDC Sea Ice Index v3 + ESA CCI SIC | nsidc.org / climate.copernicus.eu |
| SSH anomaly | CMEMS DUACS DT2024 multi-mission gridded SSH (1993–2025, single homogeneous product) | Copernicus Marine Service API |
| Wind field | ERA5 10m wind / wind stress | CDS API |
| SWOT SSH | SWOT L3 KaRIn SSH (supplementary only, not for before/after comparison) | AVISO+ / PO.DAAC |

**Critical principle:** The before/after comparison must use a single homogeneous product (CMEMS DUACS) spanning both periods. SWOT data should only be used to demonstrate submesoscale features invisible to conventional altimetry — not as the primary comparison baseline. Otherwise, resolution differences between SWOT and conventional altimetry will create spurious signals.

### R2. Formal attribution analysis to exclude natural variability

The post-2016 period coincides with multiple large-scale climate driver changes (strong El Nino 2015–2016, SAM trend, IPO phase shift). The manuscript must demonstrate that SSH/EKE changes exceed the envelope of natural variability.

Specific approach:
1. Download SAM index (Marshall 2003), Nino 3.4 index, IPO index
2. Build multivariate linear regression using 1993–2015 data: `SSH_var = beta_1 * SAM + beta_2 * ENSO + beta_3 * IPO + epsilon`
3. Use this model to predict 2016–2025 SSH variability
4. Compute residuals: `Delta_unexplained = observed - predicted`
5. Test whether residuals are significant (>2 sigma) — only this component is a candidate sea-ice signal

### R3. Replace "tipping point" with "regime shift"

In climate science, a tipping point (sensu Lenton et al. 2008) requires evidence of: (i) threshold crossing, (ii) qualitative state change, and (iii) irreversibility on policy-relevant timescales. With ~2 years of SWOT data, irreversibility cannot be demonstrated.

**Required:**
- Revise title to: "SWOT Altimetry Reveals Southern Ocean Dynamic Regime Shift Following Antarctic Sea Ice Decline" (or similar)
- Restrict "tipping point" to the Discussion section as one possible interpretation
- Explicitly state the conditions under which future observations could distinguish tipping point from regime shift from prolonged extreme event

### R4. Add CMIP6 model comparison

Extract Southern Ocean SSH variability and EKE from CMIP6 historical + SSP2-4.5/SSP5-8.5 experiments:
- Select 5–10 models with reasonable Southern Ocean sea ice representation (e.g., CESM2, ACCESS-ESM1.5, UKESM1, MPI-ESM1.2)
- Test whether models reproduce the post-2016 EKE shift
- If models show similar changes → independent verification
- If models do not → observations capture processes missing from models (equally valuable)

### R5. Complete reference verification

All 10 references are marked unverified. Prioritize:
- Fu et al. (2024) — find the formal SWOT mission performance publication and DOI
- Gille et al. (2025) — confirm publication status; if unpublished, mark as "in prep" or remove
- Turner et al. (2017) GRL and Lenton et al. (2008) PNAS — these should be straightforward to verify

## Suggested Revision Timeline

| Step | Content | Estimated time |
|---|---|---|
| Step 1 | Data download (CMEMS SSH + NSIDC SIC + ERA5) | 3 days |
| Step 2 | Rebuild SSH variability and EKE analysis with real data | 5 days |
| Step 3 | SAM/ENSO attribution regression analysis | 3 days |
| Step 4 | CMIP6 model data extraction and comparison | 5 days |
| Step 5 | Rewrite results and discussion, revise title | 3 days |
| Step 6 | Reference verification | 2 days |

---

We look forward to receiving your revised manuscript. The scientific question is excellent and timely — with real data and rigorous attribution, this work could make a significant contribution.

Sincerely,
*Editorial Office*

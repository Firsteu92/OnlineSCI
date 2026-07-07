# P03 Editorial Decision — R0

**Journal:** Nature Communications
**Manuscript:** Testing Neglected Eddy Boundary Signals with SWOT Altimetry
**Decision: Major Revision required before further consideration**
**Date:** 2026-06-08

---

Dear Authors,

Thank you for submitting your proposal. The question of whether SWOT-resolved eddy rims provide a better organizing coordinate for tracer anomalies is timely and potentially impactful. However, several critical issues must be addressed before this work can be considered for Nature Communications.

## 1. Insufficient demonstration of physical novelty beyond resolution improvement

The current framing presents a resolution comparison (SWOT vs. AVISO), which risks reducing the contribution to: "a higher-resolution instrument sees more detail." This is expected, not novel.

**Required:** Demonstrate that the SWOT-resolved rim reveals qualitatively different physics — not merely quantitatively sharper gradients. Specifically:
- Does the rim offset (H2) systematically bias existing estimates of eddy-induced heat/salt/carbon transport? Provide a quantitative estimate of how transport budgets change when rim-aligned vs. core-aligned coordinates are used.
- Is there a dynamical regime (e.g., eddy age, strain rate, background shear) where rim-core offset is large enough to matter for climate-relevant fluxes?

Without this, Stage 1 alone is a methods/validation paper suitable for JGR-Oceans or Remote Sensing of Environment, not Nature Communications.

## 2. Stage 2 requires stronger causal framework

The proposal correctly notes that "tracer alignment is not causality" (Guardrail §5), yet the entire Stage 2 hypothesis (H3) rests on demonstrating stronger tracer concentration at the rim. The confound is clear: SSH gradient maxima are inherently co-located with frontal zones where tracer gradients are expected to be large, regardless of any eddy "organizing" effect.

**Required:**
- A formal null model: generate synthetic tracer fields with realistic frontal structure but no eddy-rim organization, and show that your rim-composite metric can distinguish the two.
- Consider cross-eddy compositing in a Lagrangian frame (following eddy propagation) rather than purely Eulerian snapshots, to reduce contamination from background fronts.

## 3. Statistical rigor for composite analysis

Nature Communications requires that statistical claims withstand bootstrap/permutation testing at the individual eddy level, not pixel level. The proposal mentions this but does not commit to specific statistical tests.

**Required:**
- Pre-register the primary statistical test (e.g., paired Wilcoxon signed-rank test on rim-aligned vs. core-aligned composite peak amplitude, with eddies as the sampling unit).
- Report effect size, not just p-values.
- Declare minimum sample size per region/season stratum before data analysis begins.

## 4. SWOT temporal sampling limitation must be explicitly addressed

The 21-day repeat cycle means each eddy is sampled at most 2–3 times during a single SWOT cycle. The proposal does not adequately address how snapshot-based rim detection handles eddy evolution between SWOT passes.

**Required:** Quantify the expected rim evolution timescale (from literature or eddy-resolving models) and demonstrate that snapshot rim detection is valid over the SWOT revisit interval.

## 5. Scope and journal fit

If Stage 1 alone is the primary result, the appropriate venue is a specialized journal. For Nature Communications, the manuscript must deliver Stage 2 cross-tracer evidence with robust statistics across multiple ocean basins. A single-region, single-tracer result is insufficient.

---

I encourage the authors to address these points and resubmit. The underlying question is important, but the current proposal needs to demonstrate that SWOT rims change our physical understanding of eddy-tracer interactions — not merely our ability to resolve eddy boundaries.

Sincerely,
*Editorial Office*

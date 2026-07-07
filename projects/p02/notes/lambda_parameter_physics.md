# Λ Parameter: Physical Derivation Notes (ClaudeB)

> Working notes for R01 Block #1 resolution. Not a deliverable — guidance for A's v0.2 revision.

## The Problem

README_research v0.1 defines:

Λ = Δω_eff / (|∂_y U| + |ζ| + α·E_IT + β·E_sub + γ·D)

The numerator has units s⁻¹ (frequency). The denominator mixes:
- |∂_y U|: s⁻¹ (shear rate) ✓
- |ζ|: s⁻¹ (vorticity) ✓
- E_IT: J/m² or m²/s² (energy density) ✗
- E_sub: same ✗
- D: dissipation rate, units unclear ✗

Even with fitting coefficients α, β, γ, the formula is physically unmotivated.

## Why the Gap Matters (Topological Argument)

In Delplace et al. (2017), topological protection arises because:
1. Coriolis parameter f changes sign across the equator
2. This creates a frequency gap Δω between Rossby and Poincaré bands
3. Kelvin/Yanai modes exist inside this gap (protected by Chern number ±2)
4. Protection fails when the gap closes — i.e., when perturbations shift frequencies enough to merge bands

Therefore, the physically correct criterion compares:
- **Numerator**: the frequency gap Δω_gap
- **Denominator**: the perturbation-induced frequency shift δω_pert

Both in units of s⁻¹ → Λ is dimensionless.

## What Is the Gap in the Real Ocean?

In the idealized equatorial β-plane shallow water model, the minimum gap frequency occurs at k_x = 0:

Δω_gap = √(β·c_n)

where c_n is the phase speed of the nth baroclinic mode and β = 2Ω/R_E ≈ 2.3 × 10⁻¹¹ m⁻¹s⁻¹.

For the first baroclinic mode (c₁ ≈ 2.5 m/s in the equatorial Pacific):

Δω₁ = √(2.3 × 10⁻¹¹ × 2.5) ≈ 2.4 × 10⁻⁶ s⁻¹ ≈ 0.21 cpd (period ~5 days)

This is also equal to f at latitude y = L_eq (the equatorial deformation radius):

L_eq = √(c₁/β) ≈ 330 km ≈ 3°

The gap is the Coriolis frequency at the edge of the equatorial waveguide.

**In the real ocean**: c_n varies spatially (from Argo stratification profiles). Hence Δω_eff = √(β·c_n(x,y,t)) is a function of location and time. For P02, estimate c₁ from Argo T/S profiles along the equatorial Pacific.

## What Are the Perturbation Frequencies?

Each perturbation type contributes an effective frequency modification:

### 1. Background vorticity (most direct)

Relative vorticity ζ modifies the effective Coriolis parameter:

f_eff = f + ζ/2

This directly shifts the gap. The perturbation frequency is:

δω_vort = |ζ|/2

For TIW regions: |ζ| ~ 10⁻⁵ s⁻¹ → δω_vort ~ 5 × 10⁻⁶ s⁻¹ (comparable to Δω₁!)
For quiescent regions: |ζ| ~ 10⁻⁶ s⁻¹ → δω_vort ~ 5 × 10⁻⁷ s⁻¹ (much smaller than Δω₁)

### 2. Mean flow Doppler shift

A background mean flow U₀ Doppler-shifts the Kelvin wave frequency:

δω_Doppler = |U₀| · k_x

For U₀ ~ 0.5 m/s, Kelvin wave k_x ~ 2π/(5000 km) ≈ 1.3 × 10⁻⁶ m⁻¹:
δω_Doppler ~ 6.3 × 10⁻⁷ s⁻¹ (smaller than gap, but not negligible)

### 3. Meridional shear

Shear ∂_y U modifies the effective β, hence the gap:

β_eff = β - ∂²U/∂y²

The perturbation is:

δω_shear ~ |∂_y U| · L_eq (shear integrated over the waveguide width)

For |∂_y U| ~ 5 × 10⁻⁶ s⁻¹/m × 3 × 10⁵ m ≈ 1.5 × 10⁻⁶... no wait. |∂_y U| itself has units s⁻¹, and its contribution to effective vorticity is just ∂_y U (which contributes to ζ). So this is already captured by item 1.

### 4. Island/topographic scattering

From McPhaden & Gill (1987): scattering efficiency depends on r = H₀/H₁ (layer ratio) and γ (density jump ratio). Not directly a frequency shift — topography breaks translational symmetry and enables mode coupling. Hard to cast as a frequency.

Alternative: for topographic scattering, the relevant comparison is the topographic length scale L_topo vs the equatorial deformation radius L_eq. When L_topo << L_eq, the topography is a small perturbation; when L_topo ~ L_eq, scattering is strong.

Topographic contribution to Λ might be better handled as a separate binary indicator rather than folded into the denominator.

## Proposed Revised Formulation

### V1 (simple, dimensionally correct):

**Λ_V1 = Δω_eff / (|ζ|/2)**

where:
- Δω_eff = √(β · c₁(x,t)) from Argo stratification
- |ζ| from GLORYS12 surface relative vorticity

Physical meaning: ratio of the topological gap frequency to the vorticity-induced gap modification. When |ζ|/2 approaches Δω_eff, the effective gap closes → protection fails.

### V2 (extended, still dimensionally correct):

**Λ_V2 = Δω_eff / max(|ζ|/2, |U₀·k_x|, σ_TIW)**

where σ_TIW is the TIW-induced frequency broadening (estimable from SST oscillation period ~20-30 days).

### Topographic term (separate indicator):

For island scattering events, add a binary/categorical indicator rather than folding into Λ:
- Distance to nearest island chain (km)
- Ridge height / equivalent depth ratio

## Order-of-Magnitude Estimates

| Scenario | Δω_eff (s⁻¹) | |ζ|/2 (s⁻¹) | Λ_V1 | Expected robustness |
|---|---|---|---|---|
| Quiescent equatorial Pacific | 2.4 × 10⁻⁶ | 5 × 10⁻⁷ | ~5 | Strong protection |
| Moderate TIW region | 2.4 × 10⁻⁶ | 2 × 10⁻⁶ | ~1.2 | Marginal |
| Strong TIW / eddy | 2.4 × 10⁻⁶ | 5 × 10⁻⁶ | ~0.5 | Protection fails |
| Cold tongue front (strong shear) | 2.4 × 10⁻⁶ | 3 × 10⁻⁶ | ~0.8 | Marginal-fail |

These estimates suggest Λ_c ~ 1 is a physically reasonable threshold, consistent with the gap-closing interpretation.

## Recommendation for A

1. Adopt Λ_V1 as the primary formulation for Phase 4
2. Present V2 as sensitivity test
3. Handle topographic scattering as a separate analysis (categorical, not continuous Λ)
4. Compute order-of-magnitude estimates above in Phase 1 to verify the framework makes physical sense before investing in full analysis

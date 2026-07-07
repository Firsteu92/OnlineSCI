"""Fig.1: Theoretical framework and observational approach.
Nature Communications schematic-led composite.
Hero panel (c): study region. Supporting theory panels (a, b).
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os
from pathlib import Path

# ── Nature rcParams ──────────────────────────────────────────
mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "svg.fonttype": "none",
    "pdf.fonttype": 42,
    "font.size": 7,
    "axes.linewidth": 0.6,
    "axes.spines.right": False,
    "axes.spines.top": False,
    "legend.frameon": False,
    "xtick.major.width": 0.5,
    "ytick.major.width": 0.5,
    "xtick.major.size": 2.5,
    "ytick.major.size": 2.5,
})

OUT = str(Path(__file__).resolve().parent)

# ── Palette (Nature material/mechanism style) ────────────────
C_POINCARE = "#3775BA"
C_ROSSBY = "#41AB5D"
C_KELVIN = "#D9544D"
C_YANAI = "#E28E2C"
C_SWOT = "#7C6CCF"
C_GILBERT = "#41AB5D"
C_LINE = "#3775BA"
C_TIW = "#D9544D"
C_OCEAN = "#EDF5FB"
C_LAND = "#E0DDD8"
C_WAVEGUIDE = "#F5E6C8"
C_NEUTRAL = "#767676"

# ── Figure layout: hero bottom (c), theory top (a, b) ───────
fig = plt.figure(figsize=(7.09, 5.0))
gs = gridspec.GridSpec(2, 2, figure=fig,
                       height_ratios=[0.85, 1.0],
                       width_ratios=[1, 1],
                       hspace=0.45, wspace=0.42)

# ============================================================
# Panel (a): Dispersion relation
# ============================================================
ax_a = fig.add_subplot(gs[0, 0])

kx = np.linspace(-3, 3, 400)

# Poincaré bands
omega_p = np.sqrt(1 + kx**2)
ax_a.fill_between(kx, omega_p, 3.2, alpha=0.04, color=C_POINCARE, lw=0)
ax_a.fill_between(kx, -omega_p, -3.2, alpha=0.04, color=C_POINCARE, lw=0)
ax_a.plot(kx, omega_p, color=C_POINCARE, lw=0.9, zorder=2)
ax_a.plot(kx, -omega_p, color=C_POINCARE, lw=0.9, zorder=2)

# Rossby
omega_r = -0.3 * kx / (1 + kx**2)
ax_a.plot(kx, omega_r, color=C_ROSSBY, lw=0.9, zorder=2)

# Kelvin (edge mode)
kk = np.linspace(0, 2.5, 100)
ax_a.plot(kk, 0.8 * kk, color=C_KELVIN, lw=1.8, zorder=4)

# Yanai (edge mode)
ky = np.linspace(-1.3, 2.5, 100)
omega_y = 0.45 * 0.5 * (ky + np.sqrt(ky**2 + 4))
ax_a.plot(ky, omega_y, color=C_YANAI, lw=1.8, zorder=3)

# Axes
ax_a.axhline(0, color="#D0D0D0", lw=0.3, zorder=0)
ax_a.axvline(0, color="#D0D0D0", lw=0.3, zorder=0)
ax_a.set_xlim(-3, 3.2)
ax_a.set_ylim(-2.8, 2.8)
ax_a.set_xticks([])
ax_a.set_yticks([])
ax_a.spines["left"].set_visible(False)
ax_a.spines["bottom"].set_visible(False)
ax_a.set_xlabel("Zonal wavenumber $k_x$", fontsize=7, labelpad=2)
ax_a.set_ylabel("Frequency $\\omega$", fontsize=7, labelpad=2)

# Gap annotation
ax_a.annotate("", xy=(2.7, 0.95), xytext=(2.7, 0.12),
              arrowprops=dict(arrowstyle="<->", color=C_NEUTRAL, lw=0.6,
                              shrinkA=0, shrinkB=0))
ax_a.text(2.85, 0.53, "$\\Delta\\omega$\ngap", fontsize=5.5, color=C_NEUTRAL,
          ha="left", va="center", linespacing=0.9)

# Chern numbers — subtle
ax_a.text(-1.8, 2.0, "$\\mathcal{C}_+ = +2$", fontsize=6,
          color=C_POINCARE, alpha=0.7, ha="center")
ax_a.text(-1.8, -2.0, "$\\mathcal{C}_- = -2$", fontsize=6,
          color=C_POINCARE, alpha=0.7, ha="center")
ax_a.text(-2.2, -0.28, "$\\mathcal{C}_0 = 0$", fontsize=5.5,
          color=C_ROSSBY, alpha=0.7, ha="center")

# Legend (direct lines + labels, Nature style)
leg_x, leg_y0, leg_dy = -2.6, 2.6, 0.33
for i, (c, lab, lw_) in enumerate([
    (C_POINCARE, "Poincaré", 0.9),
    (C_ROSSBY, "Rossby", 0.9),
    (C_KELVIN, "Kelvin", 1.8),
    (C_YANAI, "Yanai", 1.8),
]):
    yy = leg_y0 - i * leg_dy
    ax_a.plot([leg_x, leg_x + 0.55], [yy, yy], color=c, lw=lw_, clip_on=False)
    ax_a.text(leg_x + 0.65, yy, lab, fontsize=5.5, va="center", color="#333333")

# Panel label
ax_a.text(-0.08, 1.04, "a", transform=ax_a.transAxes, fontsize=9,
          fontweight="bold", va="bottom", ha="left")

# ============================================================
# Panel (b): Coriolis parameter
# ============================================================
ax_b = fig.add_subplot(gs[0, 1])

lat = np.linspace(-30, 30, 300)
f_norm = np.sin(np.radians(lat))

# Hemisphere shading
ax_b.fill_between(lat, 0, f_norm, where=(f_norm > 0),
                  alpha=0.06, color=C_KELVIN, lw=0)
ax_b.fill_between(lat, 0, f_norm, where=(f_norm < 0),
                  alpha=0.06, color=C_POINCARE, lw=0)
ax_b.plot(lat, f_norm, color="#272727", lw=1.1, zorder=3)

# Reference lines
ax_b.axhline(0, color="#D0D0D0", lw=0.4, zorder=0)
ax_b.axvline(0, color="#D0D0D0", lw=0.4, linestyle=":", zorder=0)

# Hemisphere labels
ax_b.text(17, 0.42, "$f > 0$", fontsize=6.5, color=C_KELVIN, alpha=0.8,
          ha="center", fontweight="bold")
ax_b.text(17, 0.28, "Northern\nHemisphere", fontsize=5.5, color=C_KELVIN,
          alpha=0.6, ha="center", linespacing=0.9)
ax_b.text(-17, -0.42, "$f < 0$", fontsize=6.5, color=C_POINCARE, alpha=0.8,
          ha="center", fontweight="bold")
ax_b.text(-17, -0.28, "Southern\nHemisphere", fontsize=5.5, color=C_POINCARE,
          alpha=0.6, ha="center", va="top", linespacing=0.9)

# Equator label
ax_b.text(1.5, 0.07, "Equator, $f = 0$", fontsize=5.5, color=C_NEUTRAL,
          style="italic")

# Edge mode annotation
ax_b.annotate("Kelvin / Yanai\nedge modes", xy=(1, 0.02),
              xytext=(14, -0.62), fontsize=5.5, color=C_KELVIN,
              fontweight="bold", ha="center",
              arrowprops=dict(arrowstyle="-|>", color=C_KELVIN,
                              lw=0.8, shrinkB=2))

ax_b.set_xlabel("Latitude (°)", fontsize=7, labelpad=2)
ax_b.set_ylabel("$f \\,/\\, 2\\Omega$", fontsize=7, labelpad=2)
ax_b.set_xlim(-32, 32)
ax_b.set_ylim(-0.75, 0.75)
ax_b.set_xticks([-30, -15, 0, 15, 30])
ax_b.set_yticks([-0.5, 0, 0.5])

ax_b.text(-0.08, 1.04, "b", transform=ax_b.transAxes, fontsize=9,
          fontweight="bold", va="bottom", ha="left")

# ============================================================
# Panel (c): Study region — hero panel, full width
# Strategy: clean ocean + thin top-edge color bars for zones
#           + Kelvin arrow in clear center + bottom annotations
# ============================================================
ax_c = fig.add_subplot(gs[1, :])

ax_c.set_facecolor(C_OCEAN)

# Simplified land
ax_c.fill([130, 155, 155, 147, 130], [-10, -10, -1, 1, 1],
          color=C_LAND, edgecolor="#B0ACA5", linewidth=0.4, zorder=2)
ax_c.fill([277, 280, 280, 277], [-10, -10, 10, 10],
          color=C_LAND, edgecolor="#B0ACA5", linewidth=0.4, zorder=2)

# Equatorial waveguide — very subtle horizontal band, no text overlap
ax_c.axhspan(-3, 3, alpha=0.10, color=C_WAVEGUIDE, lw=0, zorder=1)
ax_c.annotate("$\\pm L_{\\mathrm{eq}}$", xy=(276, 3), fontsize=5,
              color="#C4A04A", ha="right", va="bottom", style="italic")

# Equator
ax_c.axhline(0, color="#999999", lw=0.4, ls="--", alpha=0.5, zorder=3)

# ── Perturbation zones: thin colored bars at top + dashed vertical extent ──
zone_cfg = [
    (175, 8, "Gilbert Is.", C_GILBERT, "spectrally\nmismatched"),
    (200, 8, "Line Is.", C_LINE, "spectrally\nmismatched"),
    (240, 30, "TIW zone", C_TIW, "resonant\n$(k,\\omega)$ channel"),
]
bar_y_top = 9.5
bar_h = 1.2
for lon, w, name, color, mech in zone_cfg:
    # Top color bar (solid, small)
    ax_c.fill_between([lon - w/2, lon + w/2], bar_y_top, bar_y_top + bar_h,
                      color=color, alpha=0.6, lw=0, zorder=5,
                      clip_on=False)
    # Zone name above bar
    ax_c.text(lon, bar_y_top + bar_h + 0.3, name, fontsize=6,
              ha="center", va="bottom", color=color, fontweight="bold",
              clip_on=False, zorder=6)
    # Thin dashed vertical lines showing zone extent
    ax_c.plot([lon - w/2, lon - w/2], [-9, bar_y_top], color=color,
              lw=0.4, ls=":", alpha=0.4, zorder=2)
    ax_c.plot([lon + w/2, lon + w/2], [-9, bar_y_top], color=color,
              lw=0.4, ls=":", alpha=0.4, zorder=2)
    # Mechanism annotation below
    ax_c.text(lon, -10.2, mech, fontsize=5, ha="center", va="top",
              color=color, fontweight="bold", linespacing=0.9, zorder=5)

# ── SWOT swaths: thin purple tick marks at top ──
for sx in [162, 192, 222, 252]:
    ax_c.plot([sx, sx], [7, 9], color=C_SWOT, lw=1.5, alpha=0.35,
              zorder=3, solid_capstyle="round")
ax_c.text(262, 8, "SWOT", fontsize=4.5, color=C_SWOT, ha="left",
          style="italic", alpha=0.7, zorder=5)

# ── Kelvin wave arrow (hero element — clear, unobstructed) ──
ax_c.annotate("", xy=(268, 0), xytext=(157, 0),
              arrowprops=dict(arrowstyle="-|>", color=C_KELVIN,
                              lw=2.5, mutation_scale=14),
              zorder=6)
ax_c.text(212, -2.0, "Kelvin wave (eastward)", fontsize=7.5,
          ha="center", color=C_KELVIN, fontweight="bold", zorder=6)

# Axis styling
ax_c.set_xlim(128, 282)
ax_c.set_ylim(-11.5, 12)
ax_c.set_xlabel("Longitude (°E)", fontsize=7, labelpad=3)
ax_c.set_ylabel("Latitude (°N)", fontsize=7, labelpad=3)
ax_c.set_xticks(range(140, 281, 20))
ax_c.set_yticks([-10, -5, 0, 5, 10])
ax_c.spines["left"].set_visible(True)
ax_c.spines["bottom"].set_visible(True)
ax_c.spines["right"].set_visible(True)
ax_c.spines["top"].set_visible(True)
for sp in ax_c.spines.values():
    sp.set_color("#B0B0B0")
    sp.set_linewidth(0.4)

ax_c.text(-0.04, 1.06, "c", transform=ax_c.transAxes, fontsize=9,
          fontweight="bold", va="bottom", ha="left")

# ── Save ─────────────────────────────────────────────────────
fig.savefig(os.path.join(OUT, "fig1_framework.pdf"), bbox_inches="tight", dpi=600)
fig.savefig(os.path.join(OUT, "fig1_framework.png"), bbox_inches="tight", dpi=300)
plt.close()
print("Fig.1 saved (Nature Comms schematic-led composite)")

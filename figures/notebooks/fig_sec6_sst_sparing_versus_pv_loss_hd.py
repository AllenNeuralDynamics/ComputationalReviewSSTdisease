"""Figure: SST/NOS/NPY and parvalbumin interneuron measures in Huntington's disease.

Every plotted value is verbatim from the source sentence recorded for its study.
Panels sit on separate axes with separate units; nothing is pooled, converted or
back-calculated. Error bars reproduce the printed "+/-" values; no source states
whether they are SD or SEM, so they are drawn dashed and labelled as such.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import matplotlib.pyplot as plt
from shared_style import COLORS, apply_style, save_figure

apply_style()
HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- panel A data
# S06-C01R: four single-study rows, each its own quantity and its own unit.
ROWS_A = [
    dict(title="STRIATUM | Rallapalle 2021 — BACHD, dorsal striatum, 12–14 mo   (p = 0.4957, n.s.)",
         unit="SOM-immunoreactive cells per 1 x 10$^6$ $\\mu$m$^2$\n(unit label taken from the companion PV sentence of the same paper)",
         bars=[("WT", 28.8, 2.7, COLORS["sst"], "28.8 $\\pm$ 2.7"),
               ("BACHD", 28.1, 4.0, COLORS["sst"], "28.1 $\\pm$ 4.0")],
         err=True, xmax=40),
    dict(title="STRIATUM | Rajput 2011 — R6/2, striatum, age not given in any source here\n"
               "(same paper states SST+ neurons are selectively spared in HD)",
         unit="reported % reduction of marker-positive neurons\n(counted profiles vs immunoreactive signal not established)",
         bars=[("SST+", 8.0, None, COLORS["sst"], "8%"),
               ("bNOS+", 14.0, None, COLORS["npy_nos"], "14%")],
         err=False, xmax=20),
    dict(title="CORTEX | Molero 2026 — BACHD, cortex, early postnatal stage not named\n"
               "(p = 0.0157; 10 mice per genotype; developmental MGE-lineage study)",
         unit="SST-immunoreactive count on the study's own scale\n(no denominator stated; not a density)",
         bars=[("control", 203.4, 9.8, COLORS["sst"], "203.4 $\\pm$ 9.8"),
               ("BACHD", 167.6, 9.2, COLORS["sst"], "167.6 $\\pm$ 9.2")],
         err=True, xmax=280),
    dict(title="CORTEX | Voelkl 2022 — R6/2, cortex, symptomatic age not stated\n"
               "(genetically labelled cell numbers unchanged in the same study)",
         unit="% reduction in interneuron CELL BODY SIZE\n(morphometric measurement, not a cell count)",
         bars=[("SST+", 16.0, None, COLORS["sst"], "16%"),
               ("PV+", 15.0, None, COLORS["pv"], "15%"),
               ("VIP+", 13.0, None, COLORS["vip"], "13%")],
         err=False, xmax=22),
]

# ---------------------------------------------------------------- panel B data
# S06-C02a: the one shared convention - % fewer counted PV+ cells than control.
BARS_B = [
    ("Lallani 2019\nrHD1 caudate head", 46.0, False),
    ("Lallani 2019\nrHD1 caudate body", 79.0, False),
    ("Lallani 2019\nrHD7 caudate head", 56.0, False),
    ("Lallani 2019\nrHD7 caudate body", 75.0, False),
    ("Kim 2014\nhuman ACC\nmood-dominant", 80.0, True),   # abstract-only source
]

# ---------------------------------------------------------------- panel C data
# S06-C02b: single-study paired density, absolute units, no percent conversion.
BARS_C = [("WT", 44.0, 9.1, "44.0 $\\pm$ 9.1"), ("BACHD", 34.2, 7.0, "34.2 $\\pm$ 7.0")]

fig = plt.figure(figsize=(7.2, 12.4))
gs = fig.add_gridspec(6, 1, height_ratios=[1.0, 1.0, 1.0, 1.0, 1.45, 1.25],
                      hspace=1.45, top=0.935, bottom=0.045, left=0.22, right=0.97)

# ============================================================== PANEL A (4 rows)
for i, row in enumerate(ROWS_A):
    ax = fig.add_subplot(gs[i, 0])
    names = [b[0] for b in row["bars"]]
    for yi, (nm, v, e, c, disp) in enumerate(row["bars"]):
        ax.barh(yi, v, height=0.55, color=c, edgecolor="black", linewidth=0.6)
        if row["err"] and e is not None:
            ax.plot([v - e, v + e], [yi, yi], color="black", lw=0.9, ls="--")
            for xe in (v - e, v + e):
                ax.plot([xe, xe], [yi - 0.12, yi + 0.12], color="black", lw=0.9)
            ax.text(v + e + row["xmax"] * 0.02, yi, disp, va="center", ha="left", fontsize=8)
        else:
            ax.text(v + row["xmax"] * 0.02, yi, disp, va="center", ha="left", fontsize=8)
    ax.set_yticks(range(len(names)))
    ax.set_yticklabels(names, fontsize=8)
    ax.set_xlim(0, row["xmax"])
    ax.set_xlabel(row["unit"], fontsize=7.5, labelpad=2)
    ax.set_title(row["title"], fontsize=8, loc="left", pad=4)
    if i == 0:
        ax.text(-0.235, 1.95, "A", transform=ax.transAxes, fontsize=14, fontweight="bold")

fig.text(0.22, 0.975, "Heterogeneous comparison — values not pooled: four non-interconvertible "
                      "quantities, one sub-axis each",
         fontsize=8.5, color=COLORS["conflict_marker"], ha="left")
fig.text(0.22, 0.960, "Error bars reproduce printed \"+/-\" values; dispersion type not stated "
                      "in any source (drawn dashed)",
         fontsize=7.5, color="#444444", ha="left")

# ===================================================================== PANEL B
axb = fig.add_subplot(gs[4, 0])
for xi, (lab, v, abstract_only) in enumerate(BARS_B):
    axb.bar(xi, v, width=0.6, color=COLORS["pv"], edgecolor="black",
            linewidth=0.9, linestyle="--" if abstract_only else "-",
            hatch="//" if abstract_only else None)
    axb.text(xi, v + 2.0, f"{v:g}%", ha="center", fontsize=8)
axb.set_xticks(range(len(BARS_B)))
axb.set_xticklabels([b[0] for b in BARS_B], fontsize=7.5)
axb.set_ylabel("% fewer counted PV-immunoreactive\ncells than control", fontsize=9)
axb.set_ylim(0, 105)
axb.set_title("Percent PV+ interneuron reduction — the only reporting convention these two studies share\n"
              "Heterogeneous comparison — values not pooled. Macaque bars: single animals, no dispersion, "
              "no group statistics.\nHuman bar: mood-dominant subgroup, p = 0.005; no interneuron loss in "
              "motor-dominant cases. Hatched + dashed edge = abstract-only source.",
              fontsize=7.8, loc="left", pad=6)
axb.yaxis.set_label_coords(-0.085, 0.5)
axb.text(-0.165, 1.30, "B", transform=axb.transAxes, fontsize=14, fontweight="bold")

# ===================================================================== PANEL C
axc = fig.add_subplot(gs[5, 0])
for xi, (lab, v, e, disp) in enumerate(BARS_C):
    axc.bar(xi, v, width=0.45, color=COLORS["pv"], edgecolor="black", linewidth=0.6)
    axc.plot([xi, xi], [v - e, v + e], color="black", lw=0.9, ls="--")
    for ye in (v - e, v + e):
        axc.plot([xi - 0.08, xi + 0.08], [ye, ye], color="black", lw=0.9)
    axc.text(xi + 0.28, v, disp, va="center", fontsize=8)
axc.set_xticks(range(len(BARS_C)))
axc.set_xticklabels([b[0] for b in BARS_C], fontsize=8.5)
axc.set_xlim(-0.55, 1.95)
axc.set_ylim(0, 62)
axc.set_ylabel("PV+ cells per\n1 x 10$^6$ $\\mu$m$^2$", fontsize=8.5)
axc.set_title("Rallapalle 2021 — BACHD vs WT, dorsal striatum, 12–14 months; absolute density, p < 0.0001\n"
              "Single-study panel on its own axis; no percent reduction derived. Dashed bars reproduce printed "
              "\"+/-\" values\n(dispersion type not stated); no animal-level n — the denominator is interneurons "
              "counted per unit striatal area.",
              fontsize=7.8, loc="left", pad=6)
axc.yaxis.set_label_coords(-0.075, 0.5)
axc.text(-0.165, 1.30, "C", transform=axc.transAxes, fontsize=14, fontweight="bold")

save_figure(fig, os.path.join(HERE, "..", "fig_sec6_sst_sparing_versus_pv_loss_hd.png"))

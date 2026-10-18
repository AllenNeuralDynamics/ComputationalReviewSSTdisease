"""Figure: cell and vector interventions, five quantities on five axes (section 10).

Panels A and B carry two different published quantities in two different
(undefined) units and therefore never share an axis. Panels C, D and E
carry three percentages with three different denominators, so each has its
own short axis whose label names the denominator and no two bars share a
baseline. All values are quoted from their entries' own source sentences.
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath("__file__")) if "__file__" not in globals() else os.path.dirname(os.path.abspath(__file__)))

import matplotlib.pyplot as plt
from shared_style import COLORS, apply_style, save_figure

apply_style()
OUTDIR = ".."   # notebooks live in figures/notebooks/; figures are written to figures/

# A: seizure frequency after MGE graft in epileptic hippocampus (Hunt 2013)
HUNT = dict(value=0.17, err=0.09, n=8)
# B: cortical slow-oscillation measure, vehicle vs donor-transplanted (Yokomizo 2025)
YOKO = dict(vehicle=0.22, vehicle_err=0.10, donor=1.1, donor_err=0.47)
# C: SST+ fraction of transplanted MGE-derived cells (Wang 2025)
WANG = dict(value=21.6, err=1.2)
# D: GAD67+ fraction of vector-transduced cells (Dimidschstein 2016)
DIMI = dict(value=95.0)
# E: survival of treated Scn1a+/- animals (Diaz 2026)
DIAZ = dict(start=50.0, end=84.0)

fig = plt.figure(figsize=(7.08, 6.0))
gs_top = fig.add_gridspec(1, 2, wspace=0.60, left=0.105, right=0.985,
                          top=0.94, bottom=0.60)
gs_bot = fig.add_gridspec(1, 3, wspace=0.95, left=0.105, right=0.985,
                          top=0.47, bottom=0.215)

# ----- A -----------------------------------------------------------------
axA = fig.add_subplot(gs_top[0, 0])
axA.bar([0], [HUNT["value"]], width=0.45, color=COLORS["mixed_GABAergic"],
        edgecolor="black", lw=0.6, zorder=2)
axA.errorbar([0], [HUNT["value"]], yerr=[HUNT["err"]], fmt="none", ecolor="#333333",
             elinewidth=1.0, capsize=3, zorder=3)
axA.text(0, HUNT["value"] + HUNT["err"] + 0.012, "0.17 \u00b1 0.09", ha="center",
         va="bottom", fontsize=8)
axA.set_xticks([0])
axA.set_xticklabels(["MGE graft into\nepileptic hippocampus"], fontsize=8)
axA.set_xlim(-0.6, 0.6)
axA.set_ylim(0, 0.42)
axA.set_ylabel("seizure frequency after graft\n(units as published)")
axA.set_title("A   Hunt 2013 \u2014 epilepsy model", loc="left", fontsize=9.5,
              fontweight="bold")
axA.text(0.03, 0.97, 'reported as a "92% reduction"; the pre-graft\nrate is not reported by the source\nn = 8 grafted epileptic animals',
         transform=axA.transAxes, fontsize=8, va="top", ha="left", color="#333333")

# ----- B -----------------------------------------------------------------
axB = fig.add_subplot(gs_top[0, 1])
axB.bar([0, 1], [YOKO["vehicle"], YOKO["donor"]], width=0.45,
        color=[COLORS["neutral_gray"], COLORS["mixed_GABAergic"]],
        edgecolor="black", lw=0.6, zorder=2)
axB.errorbar([0, 1], [YOKO["vehicle"], YOKO["donor"]],
             yerr=[YOKO["vehicle_err"], YOKO["donor_err"]], fmt="none",
             ecolor="#333333", elinewidth=1.0, capsize=3, zorder=3)
for x, v, e in ((0, YOKO["vehicle"], YOKO["vehicle_err"]), (1, YOKO["donor"], YOKO["donor_err"])):
    axB.text(x, v + e + 0.05, "{:g} \u00b1 {:g}".format(v, e), ha="center", va="bottom",
             fontsize=8)
axB.set_xticks([0, 1])
axB.set_xticklabels(["vehicle", "donor-transplanted"], fontsize=8)
axB.set_xlim(-0.6, 1.6)
axB.set_ylim(0, 2.1)
axB.set_ylabel("cortical slow-oscillation measure\n(\u00d7 10$^{-7}$ control; units as published)")
axB.set_title("B   Yokomizo 2025 \u2014 APP/PS1 amyloid model", loc="left",
              fontsize=9.5, fontweight="bold")
axB.text(0.03, 0.97, "p = 0.0033; group size not reported\nimaging-derived, control-referenced",
         transform=axB.transAxes, fontsize=8, va="top", ha="left", color="#333333")

# ----- C, D, E: three denominators, three axes ---------------------------
axC = fig.add_subplot(gs_bot[0, 0])
axC.bar([0], [WANG["value"]], width=0.4, color=COLORS["SST"], edgecolor="black",
        lw=0.6, zorder=2)
bars = axC.errorbar([0], [WANG["value"]], yerr=[WANG["err"]], fmt="none",
                    ecolor="#333333", elinewidth=1.0, capsize=3, zorder=3)
for b in bars[2]:
    b.set_linestyle("--")
axC.text(0, WANG["value"] + WANG["err"] + 1.5, "21.6 \u00b1 1.2", ha="center",
         va="bottom", fontsize=8)
axC.set_xticks([0])
axC.set_xticklabels(["Fmr1-KO\nhippocampus"], fontsize=8)
axC.set_xlim(-0.6, 0.6)
axC.set_ylim(0, 100)
axC.set_ylabel("SST+ cells\n(% of transplanted MGE-derived cells)", fontsize=8.5)
axC.set_title("C   Wang 2025", loc="left", fontsize=9.5, fontweight="bold")
axC.text(0.5, 0.86, "dispersion type\nnot stated;\nno group size", transform=axC.transAxes,
         fontsize=8, va="top", ha="left", color="#333333")

axD = fig.add_subplot(gs_bot[0, 1])
axD.bar([0], [DIMI["value"]], width=0.4, color=COLORS["mixed_GABAergic"],
        edgecolor="black", lw=0.6, zorder=2)
axD.text(0, DIMI["value"] + 1.5, "~95", ha="center", va="bottom", fontsize=8)
axD.set_xticks([0])
axD.set_xticklabels(["mDlx-enhancer AAV,\nwild-type brain"], fontsize=8)
axD.set_xlim(-0.6, 0.6)
axD.set_ylim(0, 100)
axD.set_ylabel("GAD67+ cells\n(% of vector-transduced cells)", fontsize=8.5)
axD.set_title("D   Dimidschstein 2016", loc="left", fontsize=9.5, fontweight="bold")
axD.text(0.5, 0.86, "source's own\napproximation;\nno group size", transform=axD.transAxes,
         fontsize=8, va="top", ha="left", color="#333333")

axE = fig.add_subplot(gs_bot[0, 2])
axE.bar([0, 1.4], [DIAZ["start"], DIAZ["end"]], width=0.5,
        color=[COLORS["neutral_gray"], COLORS["primary_green"]],
        edgecolor="black", lw=0.6, zorder=2)
for x, v in ((0, DIAZ["start"]), (1.4, DIAZ["end"])):
    axE.text(x, v + 1.5, "{:g}".format(v), ha="center", va="bottom", fontsize=8)
axE.set_xticks([0, 1.4])
axE.set_xticklabels(["from", "to"], fontsize=8.5)
axE.set_xlim(-0.9, 2.3)
axE.set_ylim(0, 100)
axE.set_ylabel("animals surviving\n(% of Scn1a+/- animals)", fontsize=8.5)
axE.set_title("E   Diaz 2026", loc="left", fontsize=9.5, fontweight="bold")
axE.text(0.0, -0.13, 'quoted: survival "from 50% to 84%"\nin AAV9-AntagoNAT-treated mice;\nno group size reported',
         transform=axE.transAxes, fontsize=8, va="top", ha="left", color="#333333")

fig.text(0.105, 0.095,
         "Heterogeneous comparison \u2014 values not pooled. Five quantities, five axes: no magnitude is comparable across panels, and no two bars share a baseline.",
         fontsize=7.5, style="italic", color=COLORS["conflict_marker"], ha="left")
fig.text(0.105, 0.062,
         "Host models: confirmed epilepsy (A), APP/PS1 amyloid (B), Fragile X syndrome (C), wild-type vector characterisation (D), Scn1a+/- Dravet syndrome (E).",
         fontsize=7.5, color="#444444", ha="left")
fig.text(0.105, 0.029,
         "All values extracted from the source papers' full text. Units in A and B are not defined by their sources.",
         fontsize=7.5, color="#444444", ha="left")

save_figure(fig, os.path.join(OUTDIR, "fig_sec10_cell_and_circuit_interventions.png"))

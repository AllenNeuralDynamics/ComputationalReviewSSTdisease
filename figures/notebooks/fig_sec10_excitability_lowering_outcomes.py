"""Figure: excitability-lowering drugs, three outcome types on three axes (section 10).

Three panels with three different nulls (a proportion, a mean difference in
points against zero, and a hazard ratio against one) and no pooled summary.
The review-level benchmark is quoted as text in the margin and has no
position on any axis. Values are quoted from their entries' own source
sentences; abstract-only entries are drawn with dashed marker edges.
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath("__file__")) if "__file__" not in globals() else os.path.dirname(os.path.abspath(__file__)))

import matplotlib.pyplot as plt
from shared_style import COLORS, apply_style, save_figure

apply_style()
OUTDIR = ".."   # notebooks live in figures/notebooks/; figures are written to figures/

CRETIN = dict(value=72.7, label="16 of 22 patients")
VOSSEL = dict(value=0.07, lo=-0.18, hi=0.32)
FERREIRA = dict(value=0.73, lo=0.61, hi=0.88)
LOSCHER_QUOTE = ('Loscher 2021 (benchmark, no axis position): "Most ASMs achieve 20-30% median '
                 'seizure frequency reduction over and above\nplacebo effect and a 30-50% responder rate." '
                 'Unselected epilepsy patients in regulatory trials - not a dementia population. '
                 'This is a percent\nreduction in seizure frequency, not a percent of patients, '
                 'so it shares no denominator with panel A and is not a comparable data point.')

fig = plt.figure(figsize=(7.08, 5.1))
gs = fig.add_gridspec(1, 3, wspace=0.80, left=0.095, right=0.985, top=0.93, bottom=0.50)

# ----- A: proportion seizure-free ---------------------------------------
axA = fig.add_subplot(gs[0, 0])
axA.bar([0], [CRETIN["value"]], width=0.42, color=COLORS["primary_green"],
        edgecolor="black", lw=0.6, zorder=2)
axA.text(0, CRETIN["value"] + 2, "72.7", ha="center", va="bottom", fontsize=8.5)
axA.set_xticks([0])
axA.set_xticklabels(["routine ASM,\nsingle arm"], fontsize=8)
axA.set_xlim(-0.6, 0.6)
axA.set_ylim(0, 100)
axA.set_ylabel("patients seizure-free\n(% of the 22-patient cohort)", fontsize=8.5)
axA.set_title("A   Cretin 2026\nseizure control", loc="left", fontsize=9, fontweight="bold")
axA.text(0.0, -0.22, "16 of 22 patients; no comparator;\nauthors describe the cohort as\nexploratory and underpowered",
         transform=axA.transAxes, fontsize=8, va="top", ha="left", color="#333333")

# ----- B: cognitive composite, mean difference vs placebo ----------------
axB = fig.add_subplot(gs[0, 1])
axB.axhline(0, color="#444444", lw=0.9, ls="--", zorder=1)
axB.plot([0, 0], [VOSSEL["lo"], VOSSEL["hi"]], color=COLORS["primary_purple"], lw=1.6, zorder=3)
for yv in (VOSSEL["lo"], VOSSEL["hi"]):
    axB.plot([-0.07, 0.07], [yv, yv], color=COLORS["primary_purple"], lw=1.6, zorder=3)
axB.plot([0], [VOSSEL["value"]], marker="s", ms=7, color=COLORS["primary_purple"],
         markeredgecolor="black", markeredgewidth=0.8, zorder=4)
axB.text(0.11, VOSSEL["value"], "0.07*\n[-0.18, 0.32]\nP = .55", fontsize=8, va="center",
         ha="left")
axB.set_xticks([0])
axB.set_xticklabels(["levetiracetam\nvs placebo"], fontsize=8)
axB.set_xlim(-0.45, 0.95)
axB.set_ylim(-0.45, 0.55)
axB.set_ylabel("NIH-EXAMINER composite,\nmean difference vs placebo (points)", fontsize=8.5)
axB.set_title("B   Vossel 2021\ncognition in AD", loc="left", fontsize=9, fontweight="bold")

# ----- C: hazard ratio for incident dementia -----------------------------
axC = fig.add_subplot(gs[0, 2])
axC.set_yscale("log")
axC.axhline(1.0, color="#444444", lw=0.9, ls="--", zorder=1)
axC.plot([0, 0], [FERREIRA["lo"], FERREIRA["hi"]], color=COLORS["primary_orange"],
         lw=1.6, zorder=3)
for yv in (FERREIRA["lo"], FERREIRA["hi"]):
    axC.plot([-0.07, 0.07], [yv, yv], color=COLORS["primary_orange"], lw=1.6, zorder=3)
axC.plot([0], [FERREIRA["value"]], marker="s", ms=7, color=COLORS["primary_orange"],
         markeredgecolor="black", markeredgewidth=0.8, zorder=4)
axC.text(0.11, FERREIRA["value"], "0.73*\n[0.61, 0.88]", fontsize=8, va="center", ha="left")
axC.set_xticks([0])
axC.set_xticklabels(["sodium channel blockers\nvs levetiracetam/brivaracetam"], fontsize=7.5)
axC.set_xlim(-0.45, 0.95)
axC.set_ylim(0.5, 1.6)
axC.set_yticks([0.5, 0.7, 1.0, 1.4])
axC.set_yticklabels(["0.5", "0.7", "1.0", "1.4"])
axC.minorticks_off()
axC.set_ylabel("hazard ratio for incident\nall-cause dementia (log scale)", fontsize=8.5)
axC.set_title("C   Ferreira-Atuesta 2026\nincident dementia", loc="left", fontsize=9,
              fontweight="bold")
axC.text(0.40, 0.98, "analysed cohort\nnot reported", transform=axC.transAxes,
         fontsize=8, va="top", ha="left", color="#333333")

# ----- margin: benchmark quoted as text, no axis position ----------------
fig.patches.append(plt.Rectangle((0.095, 0.145), 0.89, 0.150, transform=fig.transFigure,
                                 facecolor="#F4F4F4", edgecolor="#CCCCCC", lw=0.6,
                                 zorder=0))
fig.text(0.107, 0.283, LOSCHER_QUOTE, fontsize=7.5, va="top", ha="left", color="#333333",
         linespacing=1.45)

fig.text(0.095, 0.105, "Heterogeneous comparison \u2014 values not pooled; the three panels have three different null values "
                       "(a proportion, zero, and one) and no summary estimate is drawn.",
         fontsize=7.5, style="italic", color=COLORS["conflict_marker"], ha="left")
fig.text(0.095, 0.065, "* Value extracted from the abstract; full text was not accessible. "
                       "Panel A's value comes from the source's full text.",
         fontsize=7.5, color="#444444", ha="left")
fig.text(0.095, 0.025, "Levetiracetam is the index drug in panel B and the reference drug in panel C.",
         fontsize=7.5, color="#444444", ha="left")

save_figure(fig, os.path.join(OUTDIR, "fig_sec10_excitability_lowering_outcomes.png"))

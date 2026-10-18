import os
import sys

# Resolve the directory that holds shared_style.py so the notebook runs from the
# repository root or from figures/notebooks.
BASE = next(p for p in (".", "figures/notebooks", os.path.join(os.getcwd(), "figures", "notebooks"))
            if os.path.exists(os.path.join(p, "shared_style.py")))
sys.path.insert(0, BASE)
FIGDIR = os.path.normpath(os.path.join(BASE, ".."))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from shared_style import COLORS, apply_style, save_figure

apply_style()

# Counts of the 90 recorded cross-study disagreements of this review, tabulated
# from the recorded inventory: each conflict is counted once, under the primary
# axis recorded for it, although 77 of the 90 involve more than one axis.
axes_rows = [
    "Measurement modality and\nwhat was counted",
    "Species, region and\ncircuit context",
    "Model construct and\nspecies transfer",
    "Cohort composition, stage\nand comorbidity",
    "Design rigor and\nstatistical unit",
]
status_cols = ["open", "unresolved", "partially\nresolved", "resolved by\nmethod"]
counts = np.array([
    [16, 8, 5, 8],   # measurement modality and what was counted (37)
    [11, 2, 0, 8],   # species, region and circuit context (21)
    [9, 0, 3, 5],    # model construct and species transfer (17)
    [6, 1, 1, 0],    # cohort composition, stage and comorbidity (8)
    [3, 0, 2, 2],    # design rigor and statistical unit (7)
])
per_section = [
    ("SST interneuron identity", 7),
    ("Selective vulnerability", 9),
    ("Alzheimer's disease", 11),
    ("Parkinson's and Lewy body", 8),
    ("Huntington's disease", 10),
    ("ALS, FTD and other", 11),
    ("Circuit consequences", 5),
    ("Human evidence", 11),
    ("Therapeutic strategies", 9),
    ("Conflicts and limitations", 9),
]

fig, (axM, axS) = plt.subplots(1, 2, figsize=(7.4, 4.6),
                               gridspec_kw={"width_ratios": [1.75, 1.0], "wspace": 0.95})

im = axM.imshow(counts, cmap="Blues", vmin=0, vmax=counts.max())
axM.set_xticks(range(len(status_cols)))
axM.set_xticklabels(status_cols, fontsize=8)
axM.set_yticks(range(len(axes_rows)))
axM.set_yticklabels(axes_rows, fontsize=8)
axM.xaxis.set_ticks_position("top")
axM.tick_params(length=0)
for sp in axM.spines.values():
    sp.set_visible(False)
for i in range(counts.shape[0]):
    for j in range(counts.shape[1]):
        v = counts[i, j]
        axM.text(j, i, str(v), ha="center", va="center", fontsize=9.5,
                 color="white" if v >= 10 else "black")
for i in range(counts.shape[0]):
    axM.text(counts.shape[1] - 0.38, i, f"{counts[i].sum()}", ha="left", va="center",
             fontsize=9, fontweight="bold")
axM.text(counts.shape[1] - 0.42, -0.78, "total", ha="left", va="center", fontsize=8,
         fontweight="bold")
axM.set_title("A  By axis and status (n = 90)", fontsize=9.5, loc="left", fontweight="bold",
              pad=36)

ys = np.arange(len(per_section))
axS.barh(ys, [p[1] for p in per_section], color=COLORS["sst"], edgecolor="black", linewidth=0.7,
         height=0.68)
axS.set_yticks(ys)
axS.set_yticklabels([p[0] for p in per_section], fontsize=8)
axS.invert_yaxis()
axS.set_xlabel("Recorded disagreements", fontsize=9)
axS.set_xlim(0, 13)
axS.spines["top"].set_visible(False)
axS.spines["right"].set_visible(False)
for y, p in zip(ys, per_section):
    axS.text(p[1] + 0.25, y, str(p[1]), va="center", fontsize=8)
axS.set_title("B  By topic area", fontsize=9.5, loc="left", fontweight="bold", pad=36)

fig.text(0.5, -0.13,
         "Each conflict is counted once, under the primary axis recorded for it; 77 of the 90 involve more than one "
         "axis, so a conflict can belong to more\nthan one axis row. Axis labels classify the recorded disagreement "
         "text and are not a measurement. The searches for disconfirming evidence were\ncapped per query, so this "
         "inventory is a top-relevance sample of the disagreement in this literature rather than a census.",
         ha="center", va="top", fontsize=7.6)

save_figure(fig, os.path.join(FIGDIR, "fig_sec11_conflict_atlas.png"))
print("saved")

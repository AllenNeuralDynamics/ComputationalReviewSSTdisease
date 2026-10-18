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
from matplotlib.gridspec import GridSpec
from shared_style import COLORS, apply_style, save_figure

apply_style()

# ---------------------------------------------------------------------------
# Panel B counts are the records assembled for this review, per topic area:
# (records read in full text, total records, recorded cross-study disagreements).
# ---------------------------------------------------------------------------
areas = [
    ("SST interneuron identity",            54, 79,  7),
    ("Vulnerability: ageing and insult",    26, 80,  9),
    ("Alzheimer's disease",                 61, 112, 11),
    ("Parkinson's / Lewy body disease",     25, 80,  8),
    ("Huntington's disease",                40, 80,  10),
    ("ALS, FTD and other conditions",       53, 84,  11),
    ("Circuit consequences",                77, 77,  5),
    ("Human postmortem and CSF",            22, 87,  11),
    ("Therapeutic strategies",              58, 86,  9),
    ("Conflicts and model limitations",     45, 79,  9),
]

acts = [
    ("Act 1 - what is established", ["1 Introduction", "2 SST interneuron identity",
                                     "3 Vulnerability in ageing and insult"]),
    ("Act 2 - where the complications arise", ["4 Alzheimer's disease", "5 Parkinson's / Lewy body",
                                               "6 Huntington's disease", "7 ALS, FTD and others"]),
    ("Act 3 - resolution and synthesis", ["8 Circuit consequences", "9 Human evidence",
                                          "10 Therapeutic strategies", "11 Conflicts and limitations",
                                          "12 Conclusion"]),
]

fig = plt.figure(figsize=(9.2, 5.8))
gs = GridSpec(1, 2, width_ratios=[0.95, 1.30], wspace=0.62, figure=fig)

# ---- Panel A: the argument -------------------------------------------------
axA = fig.add_subplot(gs[0]); axA.axis("off")
axA.set_title("(A) The argument", fontsize=9.5, loc="left", fontweight="bold")
act_colors = [COLORS["mixed_gabaergic"], COLORS["sst"], COLORS["npy_nos"]]
y = 0.97
positions = {}
for (title, nodes), col in zip(acts, act_colors):
    axA.text(0.02, y, title, fontsize=8.2, fontweight="bold", color=col, transform=axA.transAxes)
    y -= 0.055
    for n in nodes:
        axA.plot(0.08, y, marker="o", ms=6, color=col, transform=axA.transAxes, clip_on=False)
        axA.text(0.13, y, n, fontsize=7.8, va="center", transform=axA.transAxes)
        positions[n.split()[0]] = y
        y -= 0.052
    y -= 0.025
# principal forward references from the introduction
for target in ["2", "3", "9", "11", "12"]:
    axA.annotate("", xy=(0.055, positions[target]), xytext=(0.055, positions["1"]),
                 xycoords=axA.transAxes, textcoords=axA.transAxes,
                 arrowprops=dict(arrowstyle="->", color=COLORS["neutral_gray"], lw=0.7,
                                 connectionstyle="arc3,rad=-0.45"))
axA.text(0.02, 0.02, "Arrows: the principal forward references made\nfrom the introduction to later sections.",
         fontsize=7.0, transform=axA.transAxes, color=COLORS["neutral_gray"])

# ---- Panel B: evidence depth ----------------------------------------------
axB = fig.add_subplot(gs[1])
ys = range(len(areas))[::-1]
for y, (name, ft, tot, conf) in zip(ys, areas):
    axB.barh(y, tot, color=COLORS["light_gray"], edgecolor="black", lw=0.6, height=0.62)
    axB.barh(y, ft, color=COLORS["sst"], edgecolor="black", lw=0.6, height=0.62)
    axB.text(tot + 2, y, "{} / {}".format(ft, tot), va="center", fontsize=7.4)
    axB.text(152, y, str(conf), va="center", ha="center", fontsize=7.4)
axB.set_yticks(list(ys)); axB.set_yticklabels([a[0] for a in areas], fontsize=7.6)
axB.set_xlim(0, 168)
axB.set_xticks([0, 25, 50, 75, 100])
axB.set_xlabel("records behind each topic area", labelpad=4)
axB.text(152, len(areas) - 0.25, "recorded\ndisagreements", ha="center", va="bottom", fontsize=7.0)
axB.set_title("(B) Depth of the evidence behind it", fontsize=9.5, loc="left", fontweight="bold")
axB.spines[["top", "right"]].set_visible(False)
axB.grid(axis="x", color=COLORS["light_gray"], lw=0.5, alpha=0.6)
axB.set_axisbelow(True)
fig.text(0.015, 0.012, "Blue = records read in full text; grey = abstract only. Counts are of records assembled for this review, not of the published literature.",
         fontsize=7.2, va="bottom")

save_figure(fig, os.path.join(FIGDIR, "fig_sec1_evidence_base_and_argument_arc.png"))
print("saved")

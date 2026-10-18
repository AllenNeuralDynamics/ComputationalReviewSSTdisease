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
# Every value below is verbatim from the source sentence recorded for that
# entry. Nothing is converted, back-calculated, rescaled or estimated.
# ---------------------------------------------------------------------------
drake = [("Control", 2176, 97), ("DGC-Pten KO", 1901, 68)]          # cells/mm3
jolk = [("Septal end", 63), ("Temporal end", 21)]                    # % surviving
buck_gad_pos = 13                                                    # % of GAD+ population
smej_geno = [("APP/PS1 6 mo\narea 36", 57), ("APP/PS1 6 mo\narea 35", 61)]
smej_age = [("Area 36\ndeep layers", -55.99, 9.13), ("Area 35\ndeep layers", -57.28, 10.96)]
regions = ["Frontal cortex", "Parietal cortex", "Cortex\n(undifferentiated)", "Striatum", "Hypothalamus"]
studies = ["Florio 1991\n(percent change)", "SONNTAG 1990\n(percent of young)"]
matrix = {
    ("Frontal cortex", 0): ("-49%", "decline"),
    ("Parietal cortex", 0): ("-80%", "decline"),
    ("Striatum", 0): ("-69%", "decline"),
    ("Hypothalamus", 0): ("no statistical differences", "null"),
    ("Cortex\n(undifferentiated)", 1): ("similar across ages:\n0.54 +/- 0.11,  0.60 +/- 0.08,  0.51 +/- 0.04", "null"),
    ("Hypothalamus", 1): ("approximately 50% of levels in young", "decline"),
}

fig = plt.figure(figsize=(7.1, 13.8))
gs = GridSpec(6, 2, figure=fig, height_ratios=[1.0, 1.0, 1.0, 1.0, 1.35, 0.1],
              hspace=1.25, wspace=0.66)

def tidy(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

# ---- A: Futacsi 2025, design-based stereology, null with no numeral --------
axA = fig.add_subplot(gs[0, 0]); tidy(axA)
axA.axhline(0, color=COLORS["neutral_gray"], lw=0.8)
axA.plot([0], [0], marker="s", ms=10, mfc="white", mec=COLORS["sst"], mew=1.8, zorder=3)
axA.set_xlim(-1, 1); axA.set_ylim(-1, 1)
axA.set_xticks([]); axA.set_yticks([0])
axA.set_ylabel("Change in SST-IR\ncell number", fontsize=8.5)
axA.set_title("A  Stereology, TgF344-AD rat", fontsize=9.5, loc="left", fontweight="bold")
axA.text(0, -0.3, "no numeric value reported\n(source reports no change in cell numbers)",
         ha="center", va="top", fontsize=7.6, color=COLORS["neutral_gray"])
axA.text(0, 0.62, "7-8 months, hippocampus", ha="center", va="bottom", fontsize=7.6,
         color=COLORS["neutral_gray"])

# ---- B: Drake 2024, eGFP-SST density ------------------------------------
axB = fig.add_subplot(gs[0, 1]); tidy(axB)
xs = [0, 1]; vals = [d[1] for d in drake]; errs = [d[2] for d in drake]
axB.bar(xs, vals, width=0.5, color=[COLORS["no_change"], COLORS["decrease"]],
        edgecolor="black", linewidth=0.8)
for x, v, er in zip(xs, vals, errs):
    axB.errorbar(x, v, yerr=er, fmt="none", ecolor="black", elinewidth=0.9, capsize=3,
                 capthick=0.9, linestyle="--")
    axB.text(x, v + er + 110, f"{v:,} +/- {er}", ha="center", va="bottom", fontsize=8)
axB.set_xticks(xs); axB.set_xticklabels([d[0] for d in drake], fontsize=8.5)
axB.set_ylim(0, 2800); axB.set_xlim(-0.6, 1.6)
axB.set_ylabel("eGFP-SST density\n(cells/mm3)", fontsize=8.5)
axB.set_title("B  Fate mapping, DGC-Pten KO mouse", fontsize=9.5, loc="left", fontweight="bold")
axB.text(0.5, -0.30, "p = 0.0402;  dispersion type not stated", ha="center", va="bottom",
         fontsize=7.6, transform=axB.transAxes, color=COLORS["neutral_gray"])

# ---- C: Jolkkonen 1997, percent surviving --------------------------------
axC = fig.add_subplot(gs[1, 0]); tidy(axC)
xs = [0, 1]; vals = [j[1] for j in jolk]
axC.bar(xs, vals, width=0.5, color=COLORS["sst"], edgecolor="black", linewidth=0.9,
        linestyle="--")
for x, v in zip(xs, vals):
    axC.text(x, v + 2.5, f"{v}%", ha="center", va="bottom", fontsize=8.5)
axC.set_xticks(xs); axC.set_xticklabels([j[0] for j in jolk], fontsize=8.5)
axC.set_ylim(0, 100); axC.set_xlim(-0.6, 1.6)
axC.set_ylabel("SST-IR hilar neurons\nsurviving (%)", fontsize=8.5)
axC.set_title("C  Immunoreactive somata, kainate rat", fontsize=9.0, loc="left", fontweight="bold")
axC.text(0.5, 0.92, "kainate-only arms", ha="center", va="top", fontsize=7.6,
         transform=axC.transAxes, color=COLORS["neutral_gray"])

# ---- D: Buckmaster 1999, GAD-positive denominator ------------------------
axD = fig.add_subplot(gs[1, 1]); tidy(axD)
axD.bar([0], [buck_gad_pos], width=0.4, color=COLORS["mixed_gabaergic"], edgecolor="black",
        linewidth=0.9, linestyle="--")
axD.text(0, buck_gad_pos + 1.5, "13%", ha="center", va="bottom", fontsize=8.5)
axD.set_xticks([0]); axD.set_xticklabels(["GAD-positive dentate\ninterneurons"], fontsize=8.5)
axD.set_ylim(0, 95); axD.set_xlim(-0.9, 2.1)
axD.set_ylabel("Loss of GAD-positive\npopulation (%)", fontsize=8.5)
axD.set_title("D  GAD-positive denominator, kainate rat", fontsize=9.0, loc="left", fontweight="bold")
axD.text(1.1, 92,
         "83% of the missing GAD-positive neurons\nare SST-immunoreactive\n(composition statistic, not plotted)\n\n"
         "52% GAD-negative hilar neurons:\na different population, not plotted",
         ha="center", va="top", fontsize=7.2, color=COLORS["neutral_gray"])

# ---- E: Sanchez-Mejias 2019 genotype contrast + Sos 2020 null ------------
axE = fig.add_subplot(gs[2, :]); tidy(axE)
xs = [0, 1]; vals = [s[1] for s in smej_geno]
axE.bar(xs, vals, width=0.42, color=COLORS["sst"], edgecolor="black", linewidth=0.8)
for x, v in zip(xs, vals):
    axE.text(x, v + 1.8, f"{v}%", ha="center", va="bottom", fontsize=8.5)
axE.axvspan(1.5, 3.4, color="#F2F2F2", zorder=0)
axE.plot([2.45], [0], marker="s", ms=10, mfc="white", mec=COLORS["no_change"], mew=1.8, zorder=3)
axE.text(2.45, 12,
         "reported null, no axis position:\nno significant change (p = 0.6625);\n"
         "wild-type arm 300 (270-350) cells/mm3\nin 3 WT mice; knock-in arm absent\n"
         "from the retrieved text, so no\npercent change is shown",
         ha="center", va="bottom", fontsize=7.2, color=COLORS["neutral_gray"])
axE.set_xticks([0, 1, 2.45])
axE.set_xticklabels([smej_geno[0][0], smej_geno[1][0], "AppNL-F 24 mo\nCA1 stratum oriens"], fontsize=8.5)
axE.set_xlim(-0.6, 3.4); axE.set_ylim(0, 100)
axE.set_ylabel("Decrease in SOM-positive\nneurons vs wild-type (%)", fontsize=8.5)
axE.set_title("E  Transgenic versus wild-type, somatostatin  (perirhinal cortex, areas 36 and 35)",
              fontsize=9.5, loc="left", fontweight="bold")

# ---- F: Sanchez-Mejias 2019 age contrast --------------------------------
axF = fig.add_subplot(gs[3, 0]); tidy(axF)
xs = [0, 1]; vals = [s[1] for s in smej_age]; errs = [s[2] for s in smej_age]
axF.bar(xs, vals, width=0.5, color=COLORS["sst"], edgecolor="black", linewidth=0.8)
for x, v, er in zip(xs, vals, errs):
    axF.errorbar(x, v, yerr=er, fmt="none", ecolor="black", elinewidth=0.9, capsize=3,
                 capthick=0.9, linestyle="--")
    axF.text(x, v - er - 4, f"{v} +/- {er}", ha="center", va="top", fontsize=8)
axF.axhline(0, color="black", lw=0.8)
axF.set_xticks(xs); axF.set_xticklabels([s[0] for s in smej_age], fontsize=8.5)
axF.set_xlim(-0.6, 1.6); axF.set_ylim(-88, 6)
axF.set_ylabel("Decrease in SOM-positive\nneurons, 6 vs 4 months (%)", fontsize=8.5)
axF.set_title("F  Within-genotype age contrast\n     (dispersion type not stated)", fontsize=9.5, loc="left", fontweight="bold")


# ---- G: Giesers 2020, calretinin and parvalbumin -------------------------
axG = fig.add_subplot(gs[3, 1]); tidy(axG)
axG.bar([0], [30], width=0.45, color=COLORS["vip"], edgecolor="black", linewidth=0.8)
axG.text(0, 32, "about 30%", ha="center", va="bottom", fontsize=8)
axG.bar([1], [40], width=0.45, color=COLORS["pv"], edgecolor="black", linewidth=0.8)
axG.annotate("", xy=(1, 56), xytext=(1, 41.5), arrowprops=dict(arrowstyle="-|>", color="black", lw=1.0))
axG.text(1, 58, "more than 40%", ha="center", va="bottom", fontsize=8)
axG.plot([2], [0], marker="s", ms=10, mfc="white", mec=COLORS["no_change"], mew=1.8, zorder=3)
axG.text(2, 6, "Tg4-42:\nno reduction\ndetected", ha="center", va="bottom", fontsize=7.6,
         color=COLORS["neutral_gray"])
axG.set_xticks([0, 1, 2]); axG.set_xticklabels(["CR\n5XFAD", "PV\n5XFAD", "CR and PV\nTg4-42"], fontsize=8.5)
axG.set_xlim(-0.7, 2.7); axG.set_ylim(0, 80)
axG.set_ylabel("Reduction in neuron\nnumber vs wild-type (%)", fontsize=8.5)
axG.set_title("G  Calretinin and parvalbumin, not somatostatin", fontsize=9.5, loc="left",
              fontweight="bold")

# ---- H: transcript matrix -----------------------------------------------
axH = fig.add_subplot(gs[4, :])
axH.set_xlim(0, 2); axH.set_ylim(0, len(regions))
axH.set_xticks([0.5, 1.5]); axH.set_xticklabels(studies, fontsize=9)
axH.set_yticks([len(regions) - i - 0.5 for i in range(len(regions))])
axH.set_yticklabels(regions, fontsize=9)
axH.xaxis.set_ticks_position("top"); axH.xaxis.set_label_position("top")
for sp in axH.spines.values():
    sp.set_visible(False)
axH.tick_params(length=0)
for i, reg in enumerate(regions):
    y = len(regions) - i - 1
    for j in range(2):
        key = (reg, j)
        if key in matrix:
            txt, kind = matrix[key]
            face = "#C6DBEF" if kind == "decline" else "#EDEDED"
            edge = COLORS["decrease"] if kind == "decline" else COLORS["neutral_gray"]
            axH.add_patch(plt.Rectangle((j + 0.03, y + 0.08), 0.94, 0.84, facecolor=face,
                                        edgecolor=edge, lw=1.0))
            axH.text(j + 0.5, y + 0.5, txt, ha="center", va="center", fontsize=7.4)
        else:
            axH.add_patch(plt.Rectangle((j + 0.03, y + 0.08), 0.94, 0.84, facecolor="white",
                                        edgecolor=COLORS["light_gray"], lw=0.8, hatch="///"))
            axH.text(j + 0.5, y + 0.5, "not measured", ha="center", va="center", fontsize=7.6,
                     color=COLORS["neutral_gray"])
axH.add_patch(plt.Rectangle((0.0, 0.0), 2.0, 1.0, facecolor="none",
                            edgecolor=COLORS["conflict_marker"], lw=1.8, zorder=5))
axH.text(1.0, -0.18,
         "outlined row: the one region both studies report - a decline in one study, an explicit null in the other",
         ha="center", va="top", fontsize=7.6, color=COLORS["conflict_marker"])
axH.set_title("H  Somatostatin transcript in aged rodent brain, each cell in its own study's convention\n"
              "     (animal n not reported in either study; fill marks declines versus explicit nulls only)",
              fontsize=9.5, loc="left", fontweight="bold", pad=30)

axnote = fig.add_subplot(gs[5, :]); axnote.axis("off")
axnote.text(0.0, 0.5,
            "Heterogeneous comparison - values not pooled. Dashed bar and marker edges mark values taken from an "
            "abstract rather than from full text;\nopen squares mark reported nulls whose sources state no numeral.",
            ha="left", va="center", fontsize=7.6)

save_figure(fig, os.path.join(FIGDIR, "fig_sec11_measurement_determines_the_answer.png"))
print("saved")

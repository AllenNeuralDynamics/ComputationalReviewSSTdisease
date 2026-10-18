# Figure: SST taxonomy and subtype fractions (section 02, panels A-D).
# Every plotted number is quoted verbatim from the source sentence of its own
# study; nothing is summed, converted or back-calculated. No panel shares an
# axis with another and no value is pooled.
import os, sys, textwrap

NB_DIR = os.path.abspath("figures/notebooks") if os.path.isdir("figures/notebooks") else os.path.abspath(".")
sys.path.insert(0, NB_DIR)
OUT_DIR = os.path.abspath(os.path.join(NB_DIR, ".."))

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from shared_style import COLORS, apply_style, save_figure

apply_style()

# ---------------------------------------------------------------- panel data
# (A) number of SST groups reported by three classification schemes
TABLE_HEADER = ["Study", "Count", "Hierarchy level", "Species",
                "Tissue extent", "Exclusions stated"]
TABLE_ROWS = [
    ["Gouwens 2020", "13",
     "met-type (multimodal morpho-electric-transcriptomic integration)",
     "mouse", "primary visual cortex (one cortical area)", "none stated"],
    ["Hodge 2019", "11", "snRNA-seq transcriptomic cluster (t-type)",
     "human", "middle temporal gyrus (one cortical area)",
     'none stated; the source qualifies the value as types "that were spatially restricted", possibly a subset of the total'],
    ["Yao 2021", "11", "supertype (intermediate tier above clusters)",
     "mouse",
     'whole isocortex and hippocampal formation ("~1.3 million cells covering the entire adult mouse isocortex and HPF", study abstract)',
     "Sst Chodl (long-range projecting) kept as a separate group and excluded from the 11"],
]
COL_W = [12, 5, 16, 7, 20, 26]          # wrap width in characters, per column
COL_X = [0.00, 0.165, 0.235, 0.415, 0.505, 0.735]   # left edge, axes fraction

# (B) fraction of SOM cells classified as Martinotti cells, by definition
B_VALUES = [70.0, 54.0]                      # printed as "~70%" and "54 +/- 1%"
B_PRINTED = ["~70%", "54 \u00b1 1%"]
B_ERR = [None, 1.0]
B_LABELS = ["Axonal morphology\nV1 L2/3 + L5\n133/190 recovered cells",
            "Retrograde layer-1 label\nS1, all layers\nN = 17 (unit not stated)"]

# (C) SST share of cortical GABAergic neurons: one primary count, one review estimate
C_VALUES = [30.0, 30.0]
C_PRINTED = ["30% \u00b1 1.5", "~30%"]
C_ERR = [1.5, None]
C_LABELS = ["Primary count\nSst-Cre / GAD67-GFP\nmouse V1, all layers",
            "Review estimate\nno area or species in\nthe reporting sentence"]

# (D) structure-specific fractions, separate axes, never summed
D_CORTEX_BAND = (20.0, 30.0)                 # "Approximately 20-30% of GABA neurons"
D_STRIATUM_VALUES = [7.5, 7.6]
D_STRIATUM_LABELS = ["SST/NPY\nsubclass", "SST/NPY/DACH1\nsubclass"]

# -------------------------------------------------------------------- layout
fig = plt.figure(figsize=(7.09, 9.4))
gs = GridSpec(3, 2, figure=fig, height_ratios=[1.45, 1.0, 0.95],
              hspace=0.60, wspace=0.36)

axA = fig.add_subplot(gs[0, :])
axB = fig.add_subplot(gs[1, 0])
axC = fig.add_subplot(gs[1, 1])
axD1 = fig.add_subplot(gs[2, 0])
axD2 = fig.add_subplot(gs[2, 1])


def style_axis(ax, ylabel, ymax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_ylim(0, ymax)
    ax.set_ylabel(ylabel, fontsize=10)
    ax.tick_params(axis="x", length=0)


def panel_title(ax, text):
    ax.set_title(text, fontsize=10, fontweight="bold", loc="left", pad=6)


# ------------------------------------------------------------------ panel A
axA.axis("off")
panel_title(axA, "A   Number of SST groups reported by three classification schemes "
                 "\u2014 counts are not comparable units")
fig.canvas.draw()
a_height_in = axA.get_position().height * fig.get_figheight()
line_step = 1.32 * 8 / 72 / a_height_in      # one 8 pt text line, in axes fraction


y = 1.0
for x, h in zip(COL_X, TABLE_HEADER):
    axA.text(x, y, h, fontsize=8, fontweight="bold", va="top", ha="left",
             transform=axA.transAxes)
y -= 1.6 * line_step
axA.plot([0, 1], [y + 0.4 * line_step, y + 0.4 * line_step], color="black",
         lw=0.8, transform=axA.transAxes, clip_on=False)
for row in TABLE_ROWS:
    cells = [textwrap.fill(c, w) for c, w in zip(row, COL_W)]
    nlines = max(c.count("\n") + 1 for c in cells)
    for x, c in zip(COL_X, cells):
        axA.text(x, y, c, fontsize=8, va="top", ha="left",
                 transform=axA.transAxes,
                 fontweight="bold" if c in ("13", "11") else "normal")
    y -= (nlines + 0.7) * line_step
    axA.plot([0, 1], [y + 0.35 * line_step, y + 0.35 * line_step],
             color=COLORS["light_gray"], lw=0.6, transform=axA.transAxes,
             clip_on=False)

# ------------------------------------------------------------------ panel B
axB.bar([0, 1], B_VALUES, width=0.55, color=COLORS["sst"], edgecolor="black",
        linewidth=0.8)
axB.errorbar([1], [B_VALUES[1]], yerr=[B_ERR[1]], fmt="none", ecolor="black",
             elinewidth=1.0, capsize=4, capthick=1.0, linestyle="--")
for i, (v, p) in enumerate(zip(B_VALUES, B_PRINTED)):
    axB.text(i, v + 4, p, ha="center", fontsize=9, fontweight="bold")
axB.set_xticks([0, 1])
axB.set_xticklabels(B_LABELS, fontsize=8)
style_axis(axB, "SOM cells classified as\nMartinotti cells (%)", 108)
panel_title(axB, "B   Martinotti fraction by definition")
axB.text(0.99, 0.99, "error bar dashed:\ndispersion type and unit\nof replication not stated",
         transform=axB.transAxes, fontsize=8, ha="right", va="top",
         color=COLORS["neutral_gray"])

# ------------------------------------------------------------------ panel C
axC.bar([0], [C_VALUES[0]], width=0.55, color=COLORS["sst"], edgecolor="black",
        linewidth=0.8)
axC.errorbar([0], [C_VALUES[0]], yerr=[C_ERR[0]], fmt="none", ecolor="black",
             elinewidth=1.0, capsize=4, capthick=1.0, linestyle="--")
axC.bar([1], [C_VALUES[1]], width=0.55, facecolor="white",
        edgecolor=COLORS["neutral_gray"], linewidth=1.2, linestyle="--")
for i, (v, p) in enumerate(zip(C_VALUES, C_PRINTED)):
    axC.text(i, v + 2.2, p, ha="center", fontsize=9, fontweight="bold")
axC.text(1, C_VALUES[1] / 2, "review\nestimate", ha="center", va="center",
         fontsize=8, color=COLORS["neutral_gray"])
axC.set_xticks([0, 1])
axC.set_xticklabels(C_LABELS, fontsize=8)
style_axis(axC, "SST share of cortical\nGABAergic neurons (%)", 48)
panel_title(axC, "C   Primary count vs review estimate")

# ----------------------------------------------------------------- panel D-i
axD1.axhspan(D_CORTEX_BAND[0], D_CORTEX_BAND[1], xmin=0.12, xmax=0.88,
             facecolor=COLORS["sst"], alpha=0.25, edgecolor=COLORS["sst"],
             linewidth=1.2, linestyle="--")
axD1.text(0.5, sum(D_CORTEX_BAND) / 2, "20\u201330%", ha="center", va="center",
          fontsize=9, fontweight="bold")
axD1.set_xlim(0, 1)
axD1.set_xticks([])
style_axis(axD1, "SST+ share of cortical\nGABA neurons (%)", 35)
panel_title(axD1, "D (i)   Rodent neocortex")
axD1.text(0.5, 0.04, "review estimate, compiled\nimmunohistochemical counts, no n;\na reported range, not a point estimate",
          transform=axD1.transAxes, fontsize=8, ha="center", va="bottom",
          color=COLORS["neutral_gray"])

# ---------------------------------------------------------------- panel D-ii
axD2.bar([0, 1], D_STRIATUM_VALUES, width=0.5, color=COLORS["npy_nos"],
         edgecolor="black", linewidth=0.8)
for i, v in enumerate(D_STRIATUM_VALUES):
    axD2.text(i, v + 0.3, f"{v}%", ha="center", fontsize=9, fontweight="bold")
axD2.set_xticks([0, 1])
axD2.set_xticklabels(D_STRIATUM_LABELS, fontsize=8)
style_axis(axD2, "subclass share of striatal\ninterneuron nuclei (%)", 13)
panel_title(axD2, "D (ii)   Human dorsal striatum")
axD2.text(0.5, 0.97, "subclasses shown separately,\nnever summed — no summed value\nis reported by the source",
          transform=axD2.transAxes, fontsize=8, ha="center", va="top",
          color=COLORS["neutral_gray"])

fig.text(0.01, 0.004,
         "Heterogeneous comparison \u2014 values not pooled; every panel carries its own axis. "
         "Dashed bar or band outline = value taken from an abstract\nonly or from a review-level synthesis.",
         fontsize=8, ha="left", va="bottom", color=COLORS["neutral_gray"])

save_figure(fig, os.path.join(OUT_DIR, "fig_sec2_sst_taxonomy_and_subtype_fractions.png"))
print("saved", os.path.join(OUT_DIR, "fig_sec2_sst_taxonomy_and_subtype_fractions.png"))

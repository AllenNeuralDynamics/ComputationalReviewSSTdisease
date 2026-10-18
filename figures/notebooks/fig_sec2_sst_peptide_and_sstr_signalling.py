# Figure: somatostatin signalling with the evidential status of each step
# (section 02). Line style encodes what supports each arrow:
#   solid  - a primary measurement exists in the literature cited here
#   dashed - the step appears only as a review-level assertion
#   dotted - no primary evidence was retrieved for this step (marked ?)
# The only numeral in the diagram is quoted verbatim from its source sentence.
import os, sys

NB_DIR = os.path.abspath("figures/notebooks") if os.path.isdir("figures/notebooks") else os.path.abspath(".")
sys.path.insert(0, NB_DIR)
OUT_DIR = os.path.abspath(os.path.join(NB_DIR, ".."))

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.lines import Line2D
from shared_style import COLORS, apply_style, save_figure

apply_style()

SOLID, DASHED, DOTTED = "-", (0, (4, 2.0)), (0, (1.4, 2.2))

# key: (x, y, w, h, text, facecolor)
BOXES = {
    "pro":  (0.02, 0.80, 0.24, 0.12, "Prosomatostatin\n(Sst / SST transcript)", "#E8EEF4"),
    "pept": (0.02, 0.60, 0.24, 0.12, "Somatostatin-14\nSomatostatin-28", "#E8EEF4"),
    "cell": (0.02, 0.34, 0.24, 0.17, "SST interneuron\ndense-core vesicles\n+ GABA vesicles", "#CFE2F0"),
    "ecs":  (0.38, 0.62, 0.27, 0.16, "Extracellular space\nvolume transmission:\nsynchronised within\n130 \u00b5m of release", "#F2F2F2"),
    "rec":  (0.70, 0.73, 0.29, 0.14, "SSTR1\u2013SSTR5\nG\u03b1i-coupled receptors", "#DDEDE5"),
    "ac":   (0.33, 0.80, 0.30, 0.10, "\u2193 adenylyl cyclase / cAMP\ncommon to all five receptors", "#F6F6F0"),
    "eff":  (0.70, 0.19, 0.29, 0.29, "Effectors measured directly\nGi-mediated cAMP inhibition\nat SSTR2\n"
            "\u2191 M-current (CA1 and layer 5\npyramidal cells)\nhyperpolarisation of L2/3\n"
            "pyramidal cells\npresynaptic depression of\nglutamate release", "#DDEDE5"),
    "targ": (0.38, 0.33, 0.27, 0.16, "Postsynaptic partners\npyramidal / PV / VIP\nwhich receptor sits\non which cell?", "#F2F2F2"),
    "nep":  (0.70, 0.03, 0.29, 0.12, "Neprilysin / amyloid axis\n(developed later in\nthe review)", "#FFFFFF"),
    "gaba": (0.38, 0.05, 0.27, 0.12, "Fast GABAergic output\nonto distal dendrites", "#CFE2F0"),
}

# (start, start_side, end, end_side, linestyle, question_mark)
ARROWS = [
    ("pro", "b", "pept", "t", DOTTED, True),
    ("pept", "b", "cell", "t", SOLID, False),
    ("cell", "r", "ecs", "l", DOTTED, True),
    ("ecs", "r", "rec", "l", SOLID, False),
    ("rec", "l", "ac", "r", DASHED, False),
    ("rec", "b", "eff", "t", SOLID, False),
    ("rec", "b", "targ", "r", DOTTED, True),
    ("cell", "b", "gaba", "l", SOLID, False),
    ("gaba", "t", "targ", "b", DASHED, False),
    ("eff", "b", "nep", "t", DOTTED, True),
]

# label text placed in free space, with its own anchor
LABELS = [
    (0.265, 0.740, "left", "center", "processing\nnot measured"),
    (0.290, 0.500, "center", "center", "release\nnot measured"),
    (0.845, 0.915, "center", "center", "binding at cloned SSTR1 / SSTR2"),
    (0.800, 0.545, "center", "center", "cell-type-resolved receptor\nmap: not retrieved"),
    (0.515, 0.245, "center", "center", "co-release with GABA:\nreview-level assertion only"),
]


def anchor(key, side):
    x, y, w, h, *_ = BOXES[key]
    return {"r": (x + w, y + h / 2), "l": (x, y + h / 2),
            "t": (x + w / 2, y + h), "b": (x + w / 2, y),
            "c": (x + w / 2, y + h / 2)}[side]


fig, ax = plt.subplots(figsize=(7.09, 6.2))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

for key, (x, y, w, h, text, fc) in BOXES.items():
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0.004,rounding_size=0.010",
                                linewidth=0.9, edgecolor=COLORS["neutral_gray"],
                                facecolor=fc, zorder=2))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=8,
            zorder=3)

for a, sa, b, sb, style, mark in ARROWS:
    p0, p1 = anchor(a, sa), anchor(b, sb)
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=11,
                                 linewidth=1.1, linestyle=style, color="black",
                                 shrinkA=1, shrinkB=3, zorder=4))
    if mark:
        mx, my = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
        ax.text(mx + 0.016, my + 0.016, "?", fontsize=11, fontweight="bold",
                ha="center", va="center", color=COLORS["primary_red"],
                zorder=6,
                bbox=dict(boxstyle="circle,pad=0.08", facecolor="white",
                          edgecolor="none"))

for x, y, ha, va, text in LABELS:
    ax.text(x, y, text, fontsize=8, ha=ha, va=va, color=COLORS["neutral_gray"],
            bbox=dict(boxstyle="round,pad=0.20", facecolor="white",
                      edgecolor="none"), zorder=5)

legend_handles = [
    Line2D([0], [0], color="black", linestyle=SOLID, lw=1.1,
           label="primary measurement in the cited literature"),
    Line2D([0], [0], color="black", linestyle=DASHED, lw=1.1,
           label="review-level assertion only"),
    Line2D([0], [0], color="black", linestyle=DOTTED, lw=1.1,
           label="no primary evidence retrieved (marked ?)"),
]
ax.legend(handles=legend_handles, loc="upper center",
          bbox_to_anchor=(0.5, 1.07), ncol=3, frameon=False, fontsize=8,
          handlelength=2.4, columnspacing=1.2)
ax.text(0.145, 0.955, "Line style encodes evidential status, not strength of effect.",
        fontsize=8, style="italic", color=COLORS["neutral_gray"], ha="center")

save_figure(fig, os.path.join(OUT_DIR, "fig_sec2_sst_peptide_and_sstr_signalling.png"))
print("saved", os.path.join(OUT_DIR, "fig_sec2_sst_peptide_and_sstr_signalling.png"))

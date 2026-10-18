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
from shared_style import COLORS, apply_style, save_figure

apply_style()

# Values verbatim from each entry's source sentence; nothing converted or estimated.
# Panel A - specificity: percent of labelled cells that are somatostatin-positive
specificity = [
    ("SST-IRES-Cre\nCA3 pyramidal\ncell layer", 37.8, "48/127", "fulltext"),
    ("SST-IRES-Cre\nCA3 stratum\noriens", 82.0, "82/100", "fulltext"),
    ("SST-IRES-Cre\nCA3 stratum\nradiatum", 82.4, "61/74", "fulltext"),
    ("Sst-Cre\npresubiculum", 71.0, "n not reported", "abstract"),
    ("X98\npresubiculum", 89.0, "n not reported", "abstract"),
]
# Panel B - coverage: percent of somatostatin-positive cells that the line labels
coverage = [
    ("GIN line\nbarrel cortex\nlayer II/III", 44.0, "44%", "n not reported", "abstract"),
    ("GIN line\nbarrel cortex\nlayers IV and Va", 35.0, "around 35%", "n not reported", "abstract"),
]

fig, (axA, axB) = plt.subplots(1, 2, figsize=(7.4, 4.8), gridspec_kw={"width_ratios": [2.9, 1.0],
                                                                      "wspace": 0.38})
for ax in (axA, axB):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_ylim(0, 112)
    ax.set_yticks([0, 20, 40, 60, 80, 100])

xs = range(len(specificity))
for x, (lab, val, denom, access) in zip(xs, specificity):
    ls = "--" if access == "abstract" else "-"
    axA.bar(x, val, width=0.62, color=COLORS["sst"], edgecolor="black", linewidth=0.9, linestyle=ls)
    axA.text(x, val + 2, f"{val}%", ha="center", va="bottom", fontsize=8.5)
    axA.text(x, 4, denom, ha="center", va="bottom", fontsize=7.2, color="white"
             if val > 20 else COLORS["neutral_gray"], rotation=90)
axA.set_xticks(list(xs))
axA.set_xticklabels([s[0] for s in specificity], fontsize=7.0)
axA.set_ylabel("Labelled cells that are\nsomatostatin-positive (%)", fontsize=9)
axA.set_title("A  Specificity", fontsize=9.5, loc="left", fontweight="bold")
axA.text(0.5, 0.985, "SST mRNA in situ hybridisation for the CA3 entries;\nSST peptide immunolabel for the presubicular entries",
         transform=axA.transAxes, fontsize=7.4, va="top", ha="center", color=COLORS["neutral_gray"])

xs2 = range(len(coverage))
for x, (lab, val, shown, denom, access) in zip(xs2, coverage):
    axB.bar(x, val, width=0.5, color=COLORS["npy_nos"], edgecolor="black", linewidth=0.9,
            linestyle="--")
    axB.text(x, val + 2, shown, ha="center", va="bottom", fontsize=8.5)
    axB.text(x, 4, denom, ha="center", va="bottom", fontsize=7.2, color="white", rotation=90)
axB.set_xticks(list(xs2))
axB.set_xticklabels(["Layer\nII/III", "Layers\nIV and Va"], fontsize=8)
axB.set_xlim(-0.7, 1.7)
axB.set_ylabel("Somatostatin-positive cells\nthat the line labels (%)", fontsize=9)
axB.set_title("B  Coverage", fontsize=9.5, loc="left", fontweight="bold")
axB.text(0.5, 0.985, "GIN line, barrel cortex;\nSST peptide immunolabel", transform=axB.transAxes,
         fontsize=7.4, va="top", ha="center", color=COLORS["neutral_gray"])

fig.text(0.5, -0.12,
         "Panels A and B share a 0-100% scale but not a quantity: bars must not be compared across panels.\n"
         "Dashed bar edges mark values taken from an abstract rather than from full text; cell denominators are "
         "printed inside the bars where the source states them.\n"
         "Heterogeneous comparison - values not pooled; four driver or reporter lines are shown and line is "
         "confounded with region.",
         ha="center", va="top", fontsize=7.6)

save_figure(fig, os.path.join(FIGDIR, "fig_sec11_genetic_label_fidelity.png"))
print("saved")

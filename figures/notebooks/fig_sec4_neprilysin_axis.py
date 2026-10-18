import os
import sys

# Resolve the directory that holds shared_style.py so the notebook runs from the
# repository root or from figures/notebooks.
BASE = next(p for p in (".", "figures/notebooks", os.path.join(os.getcwd(), "figures", "notebooks"))
            if os.path.exists(os.path.join(p, "shared_style.py")))
sys.path.insert(0, BASE)
FIGDIR = os.path.normpath(os.path.join(BASE, ".."))
import matplotlib.pyplot as plt
import textwrap
from shared_style import COLORS, apply_style, save_figure

apply_style()

# --- Entry records, verbatim from the comparison -----------------------------

WEBSTER = {
    "label": "Webster 2014", "value": 20.0, "value_text": "20-fold increase",
    "source": "By using a directed evolution approach, we have generated a variant of NEP "
              "that shows 20-fold increased catalytic efficiency on Abeta1-40 and up to "
              "3.2x10^3-fold reduced cleavage of a range of off-target peptides.",
    "annotation": "purified enzyme kinetics on synthetic Abeta1-40; no somatostatin in this "
                  "system; no sample size reported",
    "text_access": "fulltext",
}

ROFO = {
    "label": "Rofo 2022", "value": 20.0, "value_text": "20-fold at very high Abeta",
    "source": "The capacity the muNEP had in degrading Abeta40 compared to the wild-type NEP "
              "varied depending on a Abeta concentration with what seemed to be substantially "
              "reduced activity at low concentrations and a 20-fold enhanced ability to degrade "
              "at very high concentrations.",
    "annotation": "ELISA degradation capacity at very high Abeta only; the same sentence reports "
                  "substantially reduced activity at low concentrations; the paper's other 20-fold "
                  "value refers to brain uptake, not degradation; no sample size reported",
    "text_access": "fulltext",
}

SANDOVAL = {
    "label": "Sandoval 2019",
    "bars": [("Sstr4", 4.9), ("neprilysin", 9.3), ("insulin degrading\nenzyme", 14.8),
             ("catalase", 3.6)],
    "source": "At 24 h, NNC 26-9100 treatment increased the cortical expression of Sstr4 "
              "(4.9-fold), Abeta-degrading enzymes neprilysin (9.3-fold) and insulin degrading "
              "enzyme (14.8-fold), and the antioxidant catalase (3.6-fold).",
    "annotation": "in vivo 3xTg-AD mouse cortex, NNC 26-9100 (0.2 ug, i.c.v.), tissue at 24 h; "
                  "cortical expression only - the corresponding subcortical effects did not reach "
                  "statistical significance; no sample size reported",
    "text_access": "abstract_only",
}

fig = plt.figure(figsize=(7.1, 5.3))
gs = fig.add_gridspec(2, 3, height_ratios=[1.0, 0.70], width_ratios=[0.8, 0.8, 1.6],
                      hspace=0.34, wspace=0.85)

def annotate_band(col, text, width=30):
    ax = fig.add_subplot(gs[1, col]); ax.axis("off")
    ax.text(0.0, 1.0, textwrap.fill(text, width=width), fontsize=8, va="top", ha="left",
            transform=ax.transAxes)

# ---- Panel A1: cell-free catalytic efficiency ratio --------------------------
ax1 = fig.add_subplot(gs[0, 0])
ax1.bar([0], [WEBSTER["value"]], width=0.5, color=COLORS["primary_purple"],
        edgecolor="black", linewidth=0.9)
ax1.text(0, WEBSTER["value"] + 0.6, WEBSTER["value_text"], ha="center", va="bottom", fontsize=8)
ax1.set_xticks([0]); ax1.set_xticklabels([WEBSTER["label"]], fontsize=9)
ax1.set_xlim(-0.6, 0.6); ax1.set_ylim(0, 26)
ax1.set_ylabel("fold increase in catalytic\nefficiency (kcat/KM) on\nAbeta1-40, cell-free", fontsize=10)
ax1.set_title("A1  kinetics", fontsize=11, fontweight="bold", loc="left")
annotate_band(0, WEBSTER["annotation"])

# ---- Panel A2: cell-free ELISA degradation capacity --------------------------
ax2 = fig.add_subplot(gs[0, 1])
ax2.bar([0], [ROFO["value"]], width=0.5, color=COLORS["primary_purple"],
        edgecolor="black", linewidth=0.9)
ax2.text(0, ROFO["value"] + 0.6, "20-fold", ha="center", va="bottom", fontsize=8)
ax2.set_xticks([0]); ax2.set_xticklabels([ROFO["label"]], fontsize=9)
ax2.set_xlim(-0.6, 0.6); ax2.set_ylim(0, 26)
ax2.set_ylabel("fold enhancement of Abeta40\ndegradation capacity at very\nhigh Abeta, cell-free", fontsize=10)
ax2.set_title("A2  ELISA", fontsize=11, fontweight="bold", loc="left")
annotate_band(1, ROFO["annotation"])

# ---- Panel B: in vivo cortical transcript response ---------------------------
axB = fig.add_subplot(gs[0, 2])
xs = list(range(len(SANDOVAL["bars"])))
vals = [b[1] for b in SANDOVAL["bars"]]
axB.bar(xs, vals, width=0.6, color=COLORS["sst"], edgecolor="black", linewidth=0.9,
        linestyle="dashed")
for x, v in zip(xs, vals):
    axB.text(x, v + 0.3, str(v) + "-fold", ha="center", va="bottom", fontsize=8)
axB.set_xticks(xs)
axB.set_xticklabels(["Sstr4", "neprilysin", "IDE", "catalase"], fontsize=8,
                    rotation=25, ha="right")
axB.set_xlim(-0.6, len(xs) - 0.4); axB.set_ylim(0, 18)
axB.set_ylabel("cortical mRNA fold change at 24 h\nafter SSTR4 agonist (qRT-PCR)", fontsize=10)
axB.set_title("B  in vivo transcript response", fontsize=11, fontweight="bold", loc="left")
annotate_band(2, SANDOVAL["annotation"], width=52)

fig.text(0.5, 0.03,
         "Heterogeneous comparison - values are not pooled. The two 20-fold values are different "
         "quantities that coincide numerically by chance and are\nnever placed on one scale. Panels A "
         "and B are not two stages of one causal chain: the cell-free measurements carry no "
         "somatostatin\nmanipulation and the in vivo panel carries no enzyme-activity measurement. "
         "Bars with a dashed outline are values reported in a paper's abstract.", fontsize=8, ha="center", va="top")

save_figure(fig, os.path.join(FIGDIR, "fig_sec4_neprilysin_axis.png"))
print("saved " + os.path.join(FIGDIR, "fig_sec4_neprilysin_axis.png"))
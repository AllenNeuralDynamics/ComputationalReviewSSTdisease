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
# value_source_sentence is retained beside every number so the figure is auditable.

MAZUREK = {
    "label": "Mazurek 1991",
    "low": -65.0, "high": -45.0,          # "decreased by 45 to 65%"
    "value_text": "-45% to -65%",
    "source": "Somatostatin concentrations measured in the same tissue extracts "
              "were consistently decreased by 45 to 65%.",
    "annotation": "14 AD cases / 17 age-matched controls; 11 cortical areas "
                  "examined; radioimmunoassay of tissue extracts",
    "text_access": "abstract_only",
}

SANDOVAL = {
    "label": "Sandoval 2024",
    "value_text": "approximately -50%",
    "annotation": "literature reference (review), value attributed to a\n"
                  "1985 primary report - not plotted as a data point",
    "text_access": "fulltext",
}

CONSENS = {
    "label": "Consens 2022",
    "beta": -0.48,
    "stat": "p_bonf = 8.98e-9",
    "source": "The strongest AD-associated cell type in mega-analysis was the "
              "somatostatin (SST) interneuron (beta = -0.48, p bonf = 8.98 x 10-9)",
    "annotation": "1037 post-mortem samples, six neocortical regions;\n"
                  "deconvolved relative cell-type proportion, not a cell count",
    "text_access": "fulltext",
}

SOLARSKI = {
    "label": "Solarski 2018",
    "value_text": "approximately -50%",
    "annotation": "literature reference (perspective article), value\n"
                  "attributed to refs 20-21; region stated only as\n"
                  "'various brain areas' - not plotted",
    "text_access": "fulltext",
}

CASTANHO = {
    "label": "Castanho 2025",
    "bars": [("AD vs resilient", -0.52, "adj-P = 3.54e-29"),
             ("AD vs control",   -0.41, "adj-P = 1.79e-22")],
    "source": "We observed lower levels of SST gene expression in EC inhibitory "
              "neurons in AD (ADvsRES: log2FC = -0.52, adj-P = 3.54e-29, "
              "ADvsCTRL: log2FC = -0.41, adj-P = 1.79e-22).",
    "annotation": "48 individuals; SST transcript level within entorhinal-cortex\n"
                  "inhibitory neurons as a class - not a count or proportion of SST cells",
    "text_access": "fulltext",
}

# Panel D: one row per entry, fields exactly as recorded.
TABLE = [
    ("Mazurek 1991",
     "tissue somatostatin concentration, percent change | 11 cortical areas | all somatostatin "
     "peptide in tissue | AD vs age-matched controls | 14 AD cases and 17 age-matched controls"),
    ("Sandoval 2024",
     "total SST density, percent change (reported in a review) | frontal cortex BA 6, 9, 10 and "
     "temporal cortex BA 21 | all somatostatin peptide in tissue | AD vs age-matched controls | "
     "no cohort size reported"),
    ("Solarski 2018",
     "number of somatostatinergic neurons, percent reduction (reported in a perspective article) | "
     "various brain areas | somatostatinergic neurons | AD vs control | no cohort size reported"),
    ("Consens 2022",
     "standardized regression coefficient (beta) for SST interneuron relative cell-type proportion | "
     "six neocortical regions, individual regions unspecified in the source used here | SST "
     "interneurons | AD cases vs controls | 1037 post-mortem brain samples"),
    ("Castanho 2025",
     "SST transcript log2 fold change | entorhinal cortex | inhibitory neurons as a class, "
     "gene-level readout | AD vs cognitively resilient donors; AD vs control | 48 individuals"),
]

EDGE = {"abstract_only": "dashed", "fulltext": "solid"}

fig = plt.figure(figsize=(7.1, 9.4))
gs = fig.add_gridspec(3, 3, height_ratios=[1.0, 0.62, 1.30], hspace=0.30, wspace=0.62)

def annotate_band(col, text):
    ax = fig.add_subplot(gs[1, col]); ax.axis("off")
    ax.text(0.0, 1.0, textwrap.fill(text, width=33), fontsize=8, va="top", ha="left",
            transform=ax.transAxes)

# ---- Panel A: tissue peptide concentration, drawn as the reported interval ----
axA = fig.add_subplot(gs[0, 0])
axA.bar([0], [MAZUREK["high"] - MAZUREK["low"]], bottom=MAZUREK["low"], width=0.5,
        color=COLORS["sst"], edgecolor="black", linewidth=0.9,
        linestyle=EDGE[MAZUREK["text_access"]])
axA.text(0, MAZUREK["high"] + 3, MAZUREK["value_text"], ha="center", va="bottom", fontsize=8)
axA.set_xticks([0]); axA.set_xticklabels([MAZUREK["label"]], fontsize=9)
axA.set_xlim(-0.6, 0.6); axA.set_ylim(-80, 15)
axA.axhline(0, color="black", linewidth=0.8)
axA.set_ylabel("percent change in tissue\nsomatostatin concentration", fontsize=10)
axA.set_title("A  tissue peptide", fontsize=11, fontweight="bold", loc="left")
annotate_band(0, MAZUREK["annotation"] + ". " + SANDOVAL["label"] + ": " +
              SANDOVAL["value_text"] + ", " + SANDOVAL["annotation"].replace("\n", " "))

# ---- Panel B: standardized regression coefficient ----------------------------
axB = fig.add_subplot(gs[0, 1])
axB.bar([0], [CONSENS["beta"]], width=0.5, color=COLORS["sst"],
        edgecolor="black", linewidth=0.9, linestyle=EDGE[CONSENS["text_access"]])
axB.text(0, CONSENS["beta"] - 0.03, "beta = " + str(CONSENS["beta"]) + "\n" + CONSENS["stat"],
         ha="center", va="top", fontsize=8)
axB.set_xticks([0]); axB.set_xticklabels([CONSENS["label"]], fontsize=9)
axB.set_xlim(-0.6, 0.6); axB.set_ylim(-0.70, 0.12)
axB.axhline(0, color="black", linewidth=0.8)
axB.set_ylabel("standardized coefficient (beta),\nSST relative proportion", fontsize=10)
axB.set_title("B  cell-type proportion", fontsize=11, fontweight="bold", loc="left")
annotate_band(1, CONSENS["annotation"].replace("\n", " ") + ". " + SOLARSKI["label"] + ": " +
              SOLARSKI["value_text"] + " cells, " + SOLARSKI["annotation"].replace("\n", " "))

# ---- Panel C: transcript log2 fold change ------------------------------------
axC = fig.add_subplot(gs[0, 2])
xs = [0, 1]
axC.bar(xs, [b[1] for b in CASTANHO["bars"]], width=0.5, color=COLORS["sst"],
        edgecolor="black", linewidth=0.9, linestyle=EDGE[CASTANHO["text_access"]])
for x, (lab, v, stat) in zip(xs, CASTANHO["bars"]):
    axC.text(x, 0.02, str(v), ha="center", va="bottom", fontsize=8)
axC.set_xticks(xs)
axC.set_xticklabels([b[0].replace(" ", "\n") for b in CASTANHO["bars"]], fontsize=9)
axC.set_xlim(-0.6, 1.6); axC.set_ylim(-0.70, 0.12)
axC.axhline(0, color="black", linewidth=0.8)
axC.set_ylabel("SST transcript log2 fold change,\nentorhinal inhibitory neurons", fontsize=10)
axC.set_title("C  transcript", fontsize=11, fontweight="bold", loc="left")
annotate_band(2, "AD vs resilient: log2FC = -0.52, adj-P = 3.54e-29. AD vs control: "
                 "log2FC = -0.41, adj-P = 1.79e-22. " + CASTANHO["annotation"].replace("\n", " "))

# ---- Panel D: tabular summary, one row per entry ------------------------------
axD = fig.add_subplot(gs[2, :])
axD.axis("off")
axD.set_title("D  metric, unit, region, population, comparator and reported sample size",
              fontsize=11, fontweight="bold", loc="left")
axD.text(0.0, 1.01, "study", fontsize=8, fontweight="bold", va="top", transform=axD.transAxes)
axD.text(0.155, 1.01,
         "metric and unit  |  region  |  population  |  comparator  |  reported sample size",
         fontsize=8, fontweight="bold", va="top", transform=axD.transAxes)
y = 0.93
for label, fields in TABLE:
    wrapped = textwrap.fill(fields, width=92)
    axD.text(0.0, y, label, fontsize=8, va="top", transform=axD.transAxes)
    axD.text(0.155, y, wrapped, fontsize=8, va="top", transform=axD.transAxes)
    y -= 0.05 * (wrapped.count(chr(10)) + 1) + 0.04
axD.text(0.0, y - 0.01,
         "Heterogeneous comparison - values are not pooled. A percent change in tissue peptide "
         "concentration, a standardized\nregression coefficient on deconvolved cell-type proportions "
         "and a per-cell transcript log2 fold change are not\ninterconvertible, so each panel carries "
         "its own axis. Bars with a dashed outline are values reported in a paper's abstract.\n"
         "Review-sourced values appear as annotations, not as bars.",
         fontsize=8, va="top", transform=axD.transAxes)

save_figure(fig, os.path.join(FIGDIR, "fig_sec4_deficit_magnitude_scales.png"))
print("saved " + os.path.join(FIGDIR, "fig_sec4_deficit_magnitude_scales.png"))
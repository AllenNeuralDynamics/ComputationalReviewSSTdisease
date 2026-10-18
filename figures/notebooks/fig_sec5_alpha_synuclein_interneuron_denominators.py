# Figure: alpha-synuclein and inhibitory interneurons - three quantities with
# three different denominators. No value is placed on a shared axis; each panel
# writes its denominator into its own axis label. The 'more than 50%' comparison
# term is printed as a verbatim text annotation only: it is given no axis
# position, because its denominator is not resolvable from the source clause.
import textwrap
import os
import sys

# Resolve the directory that holds shared_style.py so the notebook runs from the
# repository root or from figures/notebooks.
BASE = next(p for p in (".", "figures/notebooks", os.path.join(os.getcwd(), "figures", "notebooks"))
            if os.path.exists(os.path.join(p, "shared_style.py")))
sys.path.insert(0, BASE)
FIGDIR = os.path.normpath(os.path.join(BASE, ".."))
import matplotlib.pyplot as plt
from shared_style import COLORS, apply_style, save_figure

apply_style()

PANEL_A = dict(
    entry_id="S05-C05-E1",
    row_label="Ubeda-Banon et al. 2010,\nas relayed by Saiz-Sanchez 2020 (review)",
    value=8, display="around 8%",
    annotation="as quoted; denominator not resolvable from the source:\n"
               "\"more than 50% of calcium-binding protein-expressing cells\"\n"
               "(a lower bound, not a point estimate; given no axis position here)",
    axis="percentage of cells containing Lewy pathology in the\n"
         "olfactory bulb that are somatostatinergic cells (%)",
    source="Postmortem studies have reported that around 8% of cells containing Lewy pathology "
           "in the olfactory bulb are somatostatinergic cells, as compared to more than 50% of "
           "calcium-binding protein-expressing cells, particularly those expressing calbindin "
           "(CB) and calretinin (CR) and to a lesser extent parvalbumin-expressing cells (PV) "
           "( Ubeda-Banon et al., 2010 ).")

PANEL_B_BAR = dict(
    entry_id="S05-C05-E3", row_label="Bernstein 2011", value=2, display="2%",
    axis="percentage of parvalbumin-expressing interneurons\n"
         "laden with alpha-synuclein immunoreactive material (%)",
    source="Double immunolabelling experiments showed that only 2% of parv expressing "
           "interneurons were laden with alpha-synuclein immunoreactive material.")

PANEL_B_ROW = dict(
    entry_id="S05-C05-E4", row_label="Bernstein 2011", outcome="reduced",
    text="parvalbumin-immunoreactive neuron density in DLB:\n"
         "significant decreases in dentate/hilus and CA1;\nno magnitude reported in the source",
    source="Quantitative estimation of parv-ir neuron density revealed significant decreases in "
           "the dentate (DG)/hilus region as well as in the CA1 subfield.")

PANEL_C = dict(
    entry_id="S05-C05-E5", row_label="Taguchi 2014", value=89, display="89",
    err_text="+/- 1.4%\ndispersion type not stated;\nno error bar drawn",
    n_text="6 coverslips\n(technical replicates)",
    axis="percentage of GAD-positive neurons displaying\nNO expression of alpha-synuclein (%)",
    source="89+/-1.4% of GAD-positive neurons displayed no expression of alpha-synuclein "
           "(6 coverslips were analyzed).")

fig = plt.figure(figsize=(7.09, 6.6))
gs = fig.add_gridspec(4, 1, height_ratios=[1.0, 0.85, 0.75, 1.0], hspace=1.15)
axA = fig.add_subplot(gs[0])
axB1 = fig.add_subplot(gs[1])
axB2 = fig.add_subplot(gs[2])
axC = fig.add_subplot(gs[3])

# ---- Panel A: one axis value plus one verbatim text annotation ------------
axA.barh([0], [PANEL_A["value"]], height=0.34, color=COLORS["sst"], edgecolor="black",
         linewidth=0.8)
axA.annotate(PANEL_A["display"], (PANEL_A["value"], 0), textcoords="offset points",
             xytext=(8, 0), va="center", fontsize=9, fontweight="bold", color=COLORS["sst"])
axA.annotate(PANEL_A["annotation"], (19, 0), va="center", ha="left", fontsize=7.0,
             color=COLORS["excitatory"])
axA.set_yticks([0]); axA.set_yticklabels([PANEL_A["row_label"]], fontsize=7.4)
axA.set_ylim(-0.5, 0.5)
axA.set_xlim(0, 60)
axA.set_xlabel(PANEL_A["axis"], fontsize=8)
axA.set_title("A   Olfactory bulb Lewy pathology, as quoted by the relaying review. One axis "
              "value only:\n     the clause's comparison term is printed verbatim and is given "
              "no axis position", fontsize=8.5, loc="left")

# ---- Panel B, upper: inclusion burden within the parvalbumin class ---------
axB1.barh([0], [PANEL_B_BAR["value"]], height=0.34, color=COLORS["pv"], edgecolor="black",
          linewidth=0.8)
axB1.annotate(PANEL_B_BAR["display"], (PANEL_B_BAR["value"], 0), textcoords="offset points",
              xytext=(8, 0), va="center", fontsize=9, fontweight="bold", color=COLORS["pv"])
axB1.set_yticks([0]); axB1.set_yticklabels([PANEL_B_BAR["row_label"]], fontsize=7.4)
axB1.set_ylim(-0.5, 0.5)
axB1.set_xlim(0, 10)
axB1.set_xlabel(PANEL_B_BAR["axis"], fontsize=8)
axB1.set_title("B   Hippocampal parvalbumin interneurons in dementia with Lewy bodies "
               "(note the 0-10% range)", fontsize=8.5, loc="left")

# ---- Panel B, lower: the categorical density row, immediately beneath ------
axB2.scatter([0.015], [0], s=170, marker="s", color=COLORS["decrease"], edgecolors="black",
             linewidths=0.8, clip_on=False)
axB2.annotate(PANEL_B_ROW["outcome"], (0.045, 0), va="center", ha="left", fontsize=8.5,
              fontweight="bold", color=COLORS["decrease"])
axB2.annotate(PANEL_B_ROW["text"], (0.165, 0), va="center", ha="left",
              fontsize=7.0, color=COLORS["excitatory"])
axB2.set_yticks([0]); axB2.set_yticklabels([PANEL_B_ROW["row_label"]], fontsize=7.4)
axB2.set_xlim(0, 1); axB2.set_ylim(-0.5, 0.5)
axB2.set_xticks([])
axB2.spines["bottom"].set_visible(False)
axB2.set_title("     Same study, categorical row: low inclusion burden coexists with reduced "
               "marker density (no numeric axis)", fontsize=8.5, loc="left")

# ---- Panel C: reversed polarity, baseline expression in culture ------------
axC.barh([0], [PANEL_C["value"]], height=0.34, color=COLORS["mixed_gabaergic"],
         edgecolor="black", linewidth=0.8)
axC.annotate(PANEL_C["display"], (PANEL_C["value"], 0), textcoords="offset points",
             xytext=(8, 0), va="center", fontsize=9, fontweight="bold")
axC.annotate(PANEL_C["err_text"].replace("\n", " ") + "; " + PANEL_C["n_text"].replace("\n", " "),
             (2, 0.33), va="bottom", ha="left", fontsize=7.0, color=COLORS["excitatory"])
axC.set_yticks([0]); axC.set_yticklabels([PANEL_C["row_label"]], fontsize=7.4)
axC.set_ylim(-0.5, 0.65)
axC.set_xlim(0, 100)
axC.set_xlabel(PANEL_C["axis"], fontsize=8)
axC.set_title("C   Primary mouse hippocampal culture, basal conditions, no synuclein challenge.\n"
              "     Reversed polarity: this is ABSENCE of expression, not pathology burden",
              fontsize=8.5, loc="left")

fig.text(0.5, -0.02, "heterogeneous comparison - values not pooled; the panels do not share an "
                     "axis and their denominators are different in kind.\nOnly panel A concerns "
                     "somatostatinergic cells; panel B quantifies parvalbumin interneurons and "
                     "panel C the broad GAD-positive class.",
         ha="center", fontsize=8, style="italic", color=COLORS["excitatory"])
fig.text(0.5, -0.075, "* The 8%, the quoted 'more than 50%' and the 89 +/- 1.4% with 6 coverslips "
                      "were extracted from full text; Bernstein 2011's 2% and density row were "
                      "extracted from its abstract.",
         ha="center", fontsize=7.5, color=COLORS["excitatory"])

save_figure(fig, os.path.join(FIGDIR, "fig_sec5_alpha_synuclein_interneuron_denominators.png"))

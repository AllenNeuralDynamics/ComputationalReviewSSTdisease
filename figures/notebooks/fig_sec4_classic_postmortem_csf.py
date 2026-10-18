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

ROSSOR = {
    "label": "Rossor 1980", "value": 47.0, "value_text": "47%",
    "source": "The fall in ChAT activity observed in the temporal cortex was "
              "accompanied by a significant reduction (47%) in immunoreactive somatostatin.",
    "annotation": "15 SDAT cases / 16 controls; temporal cortex; clinically diagnosed SDAT; "
                  "radioimmunoassay",
    "text_access": "abstract_only",
}

DAVIES = {
    "label": "Davies 1981", "value_text": "7 of 8 regions",
    "source": "ChAT activity was significantly lower in all 8 brain regions of demented "
              "patients and the SLI concentration was significantly reduced in 7 of the the 8.",
    "annotation": "8-region panel; 12 dementia cases and 12 normal individuals; significant "
                  "in 7 of the 8 regions; the source does not name which regions, and does not "
                  "characterise them as cortical and subcortical; mixed presenile and senile dementia.",
    "text_access": "abstract_only",
}

ARAI = {
    "label": "Arai 1984",
    "regions": ["orbital cortex", "hippocampus", "putamen"],
    "panel_size_text": "of 21 regions measured",
    "source": "SLI was significantly reduced in the orbital cortex, hippocampus and putamen "
              "of ATD brains. || Somatostatin- and vasoactive intestinal polypeptide (VIP)-like "
              "immunoreactivities were measured, by radioimmunoassay, in 21 regions of postmortem "
              "brains from 7 histologically verified cases of patients with Alzheimer-type dementia "
              "(ATD) and 10 histologically normal controls.",
    "annotation": "21-region panel; 7 histologically verified ATD cases and 10 histologically "
                  "normal controls; significant regions named individually; histologically verified ATD",
    "text_access": "abstract_only",
}

ATACK = {
    "label": "Atack 1988",
    "bars": [("DAT", 17.5, 5.0), ("EDAT", 16.4, 5.0), ("control", 23.1, 8.2)],
    "source": "In patients with DAT and EDAT, the concentrations of somatostatin "
              "(17.5 +/- 5.0 and 16.4 +/- 5.0 pg/mL, respectively) were significantly reduced "
              "relative to age-matched control subjects (23.1 +/- 8.2 pg/mL) but were unrelated "
              "to dementia severity and did not change significantly during the progression of "
              "the disease.",
    "annotation": "26 healthy normal / 27 DAT / 7 DAT with extrapyramidal signs; cerebrospinal "
                  "fluid, sampling site not stated in the source; EDAT denotes DAT with "
                  "extrapyramidal signs; error bars are the reported +/- "
                  "values, dispersion type (standard deviation or standard error) not stated in "
                  "the source; clinically defined DAT with an extrapyramidal subgroup",
    "text_access": "abstract_only",
}

fig = plt.figure(figsize=(7.1, 6.6))
gs = fig.add_gridspec(2, 3, height_ratios=[1.0, 0.95], hspace=0.32, wspace=0.55)

def annotate_band(col, text, width=34):
    ax = fig.add_subplot(gs[1, col]); ax.axis("off")
    ax.text(0.0, 1.0, textwrap.fill(text, width=width), fontsize=8, va="top", ha="left",
            transform=ax.transAxes)

# ---- Panel A: percent reduction in tissue immunoreactive somatostatin --------
axA = fig.add_subplot(gs[0, 0])
axA.bar([0], [ROSSOR["value"]], width=0.5, color=COLORS["sst"], edgecolor="black",
        linewidth=0.9, linestyle="dashed")
axA.text(0, ROSSOR["value"] + 2, ROSSOR["value_text"], ha="center", va="bottom", fontsize=8)
axA.set_xticks([0]); axA.set_xticklabels([ROSSOR["label"]], fontsize=9)
axA.set_xlim(-0.6, 0.6); axA.set_ylim(0, 70)
axA.set_ylabel("percent reduction in immunoreactive\nsomatostatin vs control", fontsize=10)
axA.set_title("A  tissue peptide", fontsize=11, fontweight="bold", loc="left")
annotate_band(0, ROSSOR["annotation"])

# ---- Panel B: regional extent strip (asymmetric by source) -------------------
axB = fig.add_subplot(gs[0, 1])
axB.set_xlim(0, 1); axB.set_ylim(-0.8, 4.4)
axB.set_yticks([3.6, 1.6]); axB.set_yticklabels([DAVIES["label"], ARAI["label"]], fontsize=9)
axB.get_xaxis().set_visible(False)
axB.spines["bottom"].set_visible(False)
axB.text(0.06, 3.6, DAVIES["value_text"] + "\n(regions not named\nin the source)",
         fontsize=8, va="center", ha="left")
for i, region in enumerate(ARAI["regions"]):
    y = 2.1 - i * 0.7
    axB.plot([0.09], [y], marker="o", markersize=7, color=COLORS["sst"],
             markeredgecolor="black", linestyle="none")
    axB.text(0.17, y, region, fontsize=8, ha="left", va="center")
axB.text(0.06, -0.45, ARAI["panel_size_text"], fontsize=8, va="center", ha="left")
axB.set_title("B  regional extent", fontsize=11, fontweight="bold", loc="left")
annotate_band(1, DAVIES["annotation"] + "  " + ARAI["annotation"] +
              "  No fraction is plotted for either entry; the strip is asymmetric because the "
              "sources are, not by design.")

# ---- Panel C: cerebrospinal fluid concentration ------------------------------
axC = fig.add_subplot(gs[0, 2])
xs = list(range(3))
cols = [COLORS["sst"], COLORS["sst"], COLORS["neutral_gray"]]
for x, (lab, v, err), c in zip(xs, ATACK["bars"], cols):
    axC.bar([x], [v], width=0.6, color=c, edgecolor="black", linewidth=0.9, linestyle="dashed")
    axC.errorbar([x], [v], yerr=[err], fmt="none", ecolor="black", elinewidth=1.0,
                 capsize=3, linestyle="dashed")
    axC.text(x, v + err + 0.8, str(v), ha="center", va="bottom", fontsize=8)
axC.set_xticks(xs); axC.set_xticklabels([b[0] for b in ATACK["bars"]], fontsize=9)
axC.set_xlim(-0.6, 2.6); axC.set_ylim(0, 36)
axC.set_ylabel("cerebrospinal fluid somatostatin\nconcentration (pg/mL)", fontsize=10)
axC.set_title("C  cerebrospinal fluid", fontsize=11, fontweight="bold", loc="left")
annotate_band(2, ATACK["annotation"])

fig.text(0.5, 0.015,
         "Heterogeneous comparison - values are not pooled. A percent reduction in dissected tissue, "
         "the regional extent of significant reduction within\ndifferently sized region panels, and an "
         "absolute cerebrospinal fluid concentration share no axis. Bars with a dashed outline are "
         "values reported in\na paper's abstract.",
         fontsize=8, ha="center", va="top")

save_figure(fig, os.path.join(FIGDIR, "fig_sec4_classic_postmortem_csf.png"))
print("saved " + os.path.join(FIGDIR, "fig_sec4_classic_postmortem_csf.png"))
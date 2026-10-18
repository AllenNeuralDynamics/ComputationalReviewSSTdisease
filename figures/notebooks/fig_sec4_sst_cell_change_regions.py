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

GONZALEZ = {
    "label": "Gonzalez-Rodriguez 2021", "value": -50.0, "value_text": "-50%",
    "source": "In the Hip, the number of SST cells was reduced by 50%, p-value = 0.0066, "
              "t = 3.640 df = 8 (Figure 4C).",
    "annotation": "human AD vs non-AD, hippocampus, SST immunoreactivity; n = 5 AD vs 5 non-AD "
                  "(formalin-fixed cases, 4 sections per case); the same abstract reports SST cells "
              "preserved in the olfactory bulb",
    "text_access": "fulltext",
}

# Four percentages, all drawn as decreases; the source calls the transgenic-versus-
# control pair "a dramatic decrease". Numerals exactly as reported.
SANCHEZ = {
    "label": "SanchezMejias 2019",
    "age_contrast": [("area 36", -55.99, 9.13), ("area 35", -57.28, 10.96)],
    "tg_contrast":  [("area 36", -57.0), ("area 35", -61.0)],
    "source": "The decrease in SOM-positive neurons in 6-month-old APP/PS1 mice was also "
              "significant when compared to 4-month-old mice (-55.99 +/- 9.13% and "
              "-57.28 +/- 10.96% in the deep layers of both areas 36 and 35, respectively). || "
              "SOM-positive neurons were notably sensitive and exhibited a dramatic decrease in "
              "the perirhinal cortex of 6-month-old transgenic mice (57% and 61% in areas 36 and "
              "35, respectively).",
    "annotation": "APP/PS1, perirhinal cortex deep layers; animals per group not reported; error "
                  "bars on the age contrast are the reported +/- values, dispersion type "
                  "(standard deviation or standard error) not stated in the source; the "
                  "transgenic-versus-control pair is reported without a dispersion term",
    "text_access": "fulltext",
}

ALBUQUERQUE = {
    "label": "Albuquerque 2015", "direction": "decrease",
    "marker_text": "SOM-IR cells decreased\n(p = 0.049 overall; p = 0.040 CA1/2)\n"
                   "no effect magnitude reported",
    "source": "Regarding SOM-IR cells, a significant decrease was observed both overall "
              "(p = 0.049; Figure 4A) and in CA1/2 (p = 0.040; Figure 4B).",
    "annotation": "6 month-old TgCRND8 vs wild type; CA1-CA2 (stratum oriens) and stratum "
                  "radiatum of CA3; stereological counts of SOM-immunoreactive neurons; the "
                  "source reports no significant decrease of SOM neurons in the dentate gyrus, "
                  "a null without a magnitude, so none is drawn",
    "text_access": "fulltext",
}

REN = {
    "label": "Ren 2025",
    "markers": [("PV+ -16.67%", "decrease"), ("SOM+ not reduced\n(no magnitude reported)", "no_change")],
    "source": "The average number of PV+ neurons in prelimbic area decreased by 16.67% in "
              "9-month-old AD model mice (Figure S1B), whereas the number of SOM+ neurons was "
              "not reduced (Figure S1C) in AD model mice.",
    "annotation": "AD model mouse at 9 months, prelimbic prefrontal cortex, Cre-reporter labelled "
                  "rather than peptide-immunoreactive; supplementary cell census, while the "
                  "paper's primary measurement is the proportion of input neurons projecting to "
                  "PV versus SST neurons; animals per group not reported",
    "text_access": "fulltext",
}

fig = plt.figure(figsize=(7.1, 8.2))
gs = fig.add_gridspec(4, 2, height_ratios=[1.0, 0.60, 0.80, 0.62],
                      width_ratios=[0.85, 1.15], hspace=0.45, wspace=0.45)

def band(ax, text, width=44):
    ax.axis("off")
    ax.text(0.0, 1.0, textwrap.fill(text, width=width), fontsize=8, va="top", ha="left",
            transform=ax.transAxes)

# ---- Panel A: human postmortem -----------------------------------------------
axA = fig.add_subplot(gs[0, 0])
axA.bar([0], [GONZALEZ["value"]], width=0.5, color=COLORS["decrease"], edgecolor="black",
        linewidth=0.9)
axA.text(0, GONZALEZ["value"] - 3, GONZALEZ["value_text"] + "\nn = 5 AD vs 5 non-AD",
         ha="center", va="top", fontsize=8)
axA.set_xticks([0]); axA.set_xticklabels(["hippocampus"], fontsize=9)
axA.set_xlim(-0.6, 0.6); axA.set_ylim(-80, 28)
axA.axhline(0, color="black", linewidth=0.8)
axA.set_ylabel("percent change in\nSST-immunoreactive cell\nnumber vs control (human)", fontsize=10)
axA.set_title("A  human postmortem", fontsize=11, fontweight="bold", loc="left")

# ---- Panel B: amyloid mouse models, grouped by region ------------------------
axB = fig.add_subplot(gs[0, 1])
xs = [0, 1]; w = 0.33
age_vals = [v for _, v, _ in SANCHEZ["age_contrast"]]
age_err = [e for _, _, e in SANCHEZ["age_contrast"]]
tg_vals = [v for _, v in SANCHEZ["tg_contrast"]]
axB.bar([x - w / 2 for x in xs], age_vals, width=w, color=COLORS["decrease"],
        edgecolor="black", linewidth=0.9, label="6 vs 4 months, within genotype")
axB.errorbar([x - w / 2 for x in xs], age_vals, yerr=age_err, fmt="none", ecolor="black",
             elinewidth=1.0, capsize=3, linestyle="dashed")
axB.bar([x + w / 2 for x in xs], tg_vals, width=w, color=COLORS["mixed_gabaergic"],
        edgecolor="black", linewidth=0.9, label="transgenic vs control, 6 months")
for x, v, e in zip([x - w / 2 for x in xs], age_vals, age_err):
    axB.text(x, v - e - 2, str(v) + "%", ha="center", va="top", fontsize=8)
for x, v in zip([x + w / 2 for x in xs], tg_vals):
    axB.text(x, v - 2, str(int(v)) + "%", ha="center", va="top", fontsize=8)
axB.set_xticks(xs); axB.set_xticklabels(["area 36", "area 35"], fontsize=9)
axB.set_xlim(-0.6, 1.6); axB.set_ylim(-85, 28)
axB.axhline(0, color="black", linewidth=0.8)
axB.set_ylabel("percent change in\nSOM-immunoreactive neuron\nnumber (mouse models)", fontsize=10)
axB.set_title("B  amyloid model, perirhinal cortex", fontsize=11, fontweight="bold", loc="left")
axB.legend(fontsize=8, loc="upper center", frameon=False, handlelength=1.4)

band(fig.add_subplot(gs[1, 0]), GONZALEZ["label"] + ": " + GONZALEZ["annotation"], width=36)
band(fig.add_subplot(gs[1, 1]), SANCHEZ["label"] + ": " + SANCHEZ["annotation"], width=50)

# ---- Panel C: direction-only strip, off the percent axis ----------------------
axC = fig.add_subplot(gs[2, :])
axC.set_xlim(0, 1); axC.set_ylim(-0.9, 2.9)
axC.set_yticks([2, 1, 0])
axC.set_yticklabels([ALBUQUERQUE["label"], REN["label"] + " (PV+)", REN["label"] + " (SOM+)"],
                    fontsize=9)
axC.get_xaxis().set_visible(False)
axC.spines["bottom"].set_visible(False)
rows = [(2, ALBUQUERQUE["marker_text"], COLORS["decrease"], "o"),
        (1, REN["markers"][0][0] + ", Cre-reporter labelled", COLORS["decrease"], "s"),
        (0, REN["markers"][1][0] + ", Cre-reporter labelled", COLORS["no_change"], "s")]
for y, label, colour, mk in rows:
    axC.plot([0.04], [y], marker=mk, markersize=8, color=colour, markeredgecolor="black",
             linestyle="none")
    axC.text(0.08, y, label, fontsize=8, va="center", ha="left")
axC.set_title("C  direction only (no magnitude axis)", fontsize=11, fontweight="bold", loc="left")

# ---- Closing band: panel C provenance and the heterogeneity statement ---------
axN = fig.add_subplot(gs[3, :]); axN.axis("off")
axN.text(0.0, 1.0, textwrap.fill(
    ALBUQUERQUE["label"] + ": " + ALBUQUERQUE["annotation"] + ".  " +
    REN["label"] + ": " + REN["annotation"], width=116),
    fontsize=8, va="top", ha="left", transform=axN.transAxes)
axN.text(0.0, 0.18, textwrap.fill(
    "Heterogeneous comparison - values are not pooled. Human postmortem and mouse-model "
    "measurements are in separate panels and are not one progression. Ren 2025 counts "
    "Cre-reporter-labelled cells while the other entries count SST/SOM-immunoreactive cells, so a "
    "reporter-labelled null does not refute an immunoreactivity loss. Regional selectivity is a "
    "hypothesis for the discrepancy, not an established reconciliation.", width=116),
    fontsize=8, va="top", ha="left", transform=axN.transAxes)

save_figure(fig, os.path.join(FIGDIR, "fig_sec4_sst_cell_change_regions.png"))
print("saved " + os.path.join(FIGDIR, "fig_sec4_sst_cell_change_regions.png"))
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

ALGAMAL = {
    "label": "Algamal 2022", "value": 2.7, "value_text": "2.7-fold higher",
    "source": "Our results show that SOM interneuron event rates were 2.7-fold higher in "
              "APP-SOM mice relative to WT-SOM mice (Figure 1d, 1e).",
    "annotation": "chronic plaque-bearing amyloidosis, spontaneous activity, awake two-photon "
                  "imaging of the cortical field imaged in vivo; bioRxiv preprint, not peer "
                  "reviewed; interneuron and mouse counts not stated in the source sentence",
    "text_access": "fulltext",
}

LEE = {
    "label": "Lee 2026",
    # (label, value, reported +/-, colour, value as written in the source sentence)
    "bars": [("SST+\nscrambled", 1.000, 0.391, COLORS["sst"], "1.000"),
             ("SST+\noligomeric", 0.600, 0.237, COLORS["sst"], "0.600"),
             ("PV+\nscrambled", 1.000, 0.772, COLORS["pv"], "1.000"),
             ("PV+\noligomeric", 0.448, 0.233, COLORS["pv"], "0.448")],
    "stats": "SST+ p = 0.0002; PV+ p = 0.0038",
    "source": "We found that 250 nM soluble Abeta42 oligomers (oAbeta42) treatment significantly "
              "reduced nicotine-induced activity in both PV+ and SST+ interneurons compared to "
              "neurons treated with 250 nM scrambled Abeta42 (sAbeta42) (PV+ interneurons, "
              "sAbeta42, 1.000 +/- 0.772 dF/F0 and oAbeta42, 0.448 +/- 0.233 dF/F0, p = 0.0038 "
              "and SST+ interneurons, sAbeta42, 1.000 +/- 0.391 dF/F0 and oAbeta42, "
              "0.600 +/- 0.237 dF/F0, p = 0.0002).",
    "annotation": "acute 250 nM soluble Abeta42 oligomers, nicotine-evoked (not spontaneous), "
                  "hippocampus; SST+ and PV+ pairs both plotted; the control value 1.000 is a "
                  "normalization constant, not a measured amplitude; error bars are the reported "
                  "+/- values, which that study's methods state are standard deviations; neuron "
                  "counts not stated in the source sentence",
    "text_access": "fulltext",
}

fig = plt.figure(figsize=(7.1, 5.6))
gs = fig.add_gridspec(2, 2, height_ratios=[1.0, 0.78], width_ratios=[0.8, 1.2],
                      hspace=0.45, wspace=0.45)

def band(ax, text, width=40):
    ax.axis("off")
    ax.text(0.0, 1.0, textwrap.fill(text, width=width), fontsize=8, va="top", ha="left",
            transform=ax.transAxes)

# ---- Panel A: chronic amyloidosis, spontaneous event rate --------------------
axA = fig.add_subplot(gs[0, 0])
axA.bar([0], [ALGAMAL["value"]], width=0.5, color=COLORS["sst"], edgecolor="black", linewidth=0.9)
axA.axhline(1.0, color=COLORS["neutral_gray"], linewidth=1.0, linestyle=":")
axA.text(0.55, 1.0, "wild type = 1", fontsize=8, va="bottom", ha="right",
         color=COLORS["neutral_gray"])
axA.text(0, ALGAMAL["value"] + 0.05, ALGAMAL["value_text"], ha="center", va="bottom", fontsize=8)
axA.set_xticks([0]); axA.set_xticklabels(["SOM interneurons\n(APP/PS1)"], fontsize=9)
axA.set_xlim(-0.6, 0.6); axA.set_ylim(0, 3.4)
axA.set_ylabel("spontaneous calcium event rate,\nfold relative to wild type", fontsize=10)
axA.set_title("A  chronic amyloidosis", fontsize=11, fontweight="bold", loc="left")
band(fig.add_subplot(gs[1, 0]), ALGAMAL["label"] + ": " + ALGAMAL["annotation"], width=36)

# ---- Panel B: acute oligomer exposure, nicotine-evoked amplitude -------------
axB = fig.add_subplot(gs[0, 1])
xs = [0, 1.4, 3.2, 4.6]
for x, (lab, v, err, colour, vtext) in zip(xs, LEE["bars"]):
    axB.bar([x], [v], width=0.6, color=colour, edgecolor="black", linewidth=0.9)
    axB.errorbar([x], [v], yerr=[err], fmt="none", ecolor="black", elinewidth=1.0,
                 capsize=3, linestyle="dashed")
    axB.text(x, v + err + 0.04, vtext, ha="center", va="bottom", fontsize=8)
axB.set_xticks(xs); axB.set_xticklabels([b[0] for b in LEE["bars"]], fontsize=8)
axB.set_xlim(-0.9, 5.5); axB.set_ylim(0, 2.1)
axB.set_ylabel("nicotine-evoked calcium amplitude\n(dF/F0, scrambled Abeta42 = 1.000)", fontsize=10)
axB.set_title("B  acute oligomer exposure", fontsize=11, fontweight="bold",
              loc="left")
band(fig.add_subplot(gs[1, 1]), LEE["label"] + ": " + LEE["stats"] + "; " + LEE["annotation"], width=54)

fig.text(0.5, 0.01,
         "Heterogeneous comparison - values are not pooled. A spontaneous calcium event-rate ratio "
         "under chronic plaque-bearing amyloidosis and a\nnicotine-evoked amplitude after acute "
         "oligomer exposure share no axis; the opposing directions reflect the different "
         "manipulations and\nreadouts, not a contradiction. Panel B plots both SST+ and PV+ "
         "interneurons, so the population shown is not SST-only.",
         fontsize=8, ha="center", va="top")

save_figure(fig, os.path.join(FIGDIR, "fig_sec4_sst_activity_direction.png"))
print("saved " + os.path.join(FIGDIR, "fig_sec4_sst_activity_direction.png"))
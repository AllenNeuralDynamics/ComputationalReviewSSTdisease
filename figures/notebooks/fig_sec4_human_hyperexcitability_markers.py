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

SZABO = {
    "label": "B. Szabo 2026",
    "bars": [("suspicious EEG\nfeatures", 57.0, "4/7", "57%"),
             ("no suspicious\nEEG features", 17.0, "4/23", "17%")],
    "stat": "p = 0.037",
    "source": "Of note, EpiQ+ symptoms were more common in patients with any suspicious EEG "
              "features in step 1 (4/7, 57%) than in those without (4/23, 17%; p = 0.037), "
              "suggesting that current morphological criteria may exclude true epileptiform "
              "activity in this patient population.",
    "annotation": "30 early-stage AD patients without a history of epilepsy and 30 age-matched "
                  "controls; subgroup denominators 7 and 23; cohort-level interictal epileptiform "
                  "discharges in 3 patients (10%) and 1 control (3.33%), not statistically "
                  "significant (p = 0.612); the plotted contrast is a secondary subgroup analysis "
                  "within patients, with no control arm",
    "text_access": "fulltext",
}

PRABHU = {
    "label": "Prabhu 2024",
    "bars": [("AD patients\n(50)", -0.235, COLORS["primary_blue"]),
             ("controls\n(35)", 0.312, COLORS["neutral_gray"])],
    "stat": "P = 0.037",
    "source": "The average normalized PAC of gamma amplitudes that showed reduced coupling for "
              "the 6-8 Hz phase at cohort level was -0.235 for AD patients and 0.312 for controls "
              "(Fig. 3A, P = 0.037).",
    "annotation": "50 AD patients with positive AD biomarkers / 35 age-matched cognitively "
                  "unimpaired controls; left parahippocampal cortex; 6-8 Hz phase band; "
                  "dimensionless signed index, not a percentage",
    "text_access": "fulltext",
}

fig = plt.figure(figsize=(7.1, 5.6))
gs = fig.add_gridspec(2, 2, height_ratios=[1.0, 0.72], hspace=0.50, wspace=0.45)

def band(ax, text, width=46):
    ax.axis("off")
    ax.text(0.0, 1.0, textwrap.fill(text, width=width), fontsize=8, va="top", ha="left",
            transform=ax.transAxes)

# ---- Panel A: within-patient stratification, no control arm ------------------
axA = fig.add_subplot(gs[0, 0])
xs = [0, 1]
for x, (lab, v, frac, vtext) in zip(xs, SZABO["bars"]):
    axA.bar([x], [v], width=0.55, color=COLORS["primary_blue"], edgecolor="black", linewidth=0.9)
    axA.text(x, v + 1.5, vtext + " (" + frac + ")", ha="center", va="bottom", fontsize=8)
axA.set_xticks(xs); axA.set_xticklabels([b[0] for b in SZABO["bars"]], fontsize=8)
axA.set_xlim(-0.6, 1.6); axA.set_ylim(0, 100)
axA.set_ylabel("percent of patients positive on the\nepilepsy questionnaire", fontsize=10)
axA.set_title("A  within patients", fontsize=11, fontweight="bold", loc="left")
axA.text(0.5, 97, "both arms are AD patients;\nno control arm in this panel\n" + SZABO["stat"],
         fontsize=8, ha="center", va="top")
band(fig.add_subplot(gs[1, 0]), SZABO["label"] + ": " + SZABO["annotation"], width=46)

# ---- Panel B: case-control comparison, signed dimensionless index ------------
axB = fig.add_subplot(gs[0, 1])
for x, (lab, v, colour) in zip(xs, PRABHU["bars"]):
    axB.bar([x], [v], width=0.55, color=colour, edgecolor="black", linewidth=0.9)
    off = 0.03 if v > 0 else -0.03
    axB.text(x, v + off, str(v), ha="center", va="bottom" if v > 0 else "top", fontsize=8)
axB.axhline(0, color="black", linewidth=0.8)
axB.set_xticks(xs); axB.set_xticklabels([b[0] for b in PRABHU["bars"]], fontsize=8)
axB.set_xlim(-0.6, 1.6); axB.set_ylim(-0.45, 0.62)
axB.set_ylabel("normalized theta-gamma\nphase-amplitude coupling\n(dimensionless, signed)", fontsize=10)
axB.set_title("B  case-control comparison", fontsize=11, fontweight="bold", loc="left")
axB.text(0.5, 0.56, PRABHU["stat"], fontsize=8, ha="center", va="top")
band(fig.add_subplot(gs[1, 1]), PRABHU["label"] + ": " + PRABHU["annotation"], width=46)

fig.text(0.5, 0.01, textwrap.fill(
    "Heterogeneous comparison - values are not pooled. A proportion of patients positive on a "
    "symptom questionnaire and a dimensionless signed coupling index are different in kind and "
    "share no axis. The p = 0.037 appearing in both panels refers to two unrelated tests. Scope: "
    "cohorts defined by Down syndrome with AD and cohorts defined by new-onset seizures are not "
    "shown.", width=114), fontsize=8, ha="center", va="top")

save_figure(fig, os.path.join(FIGDIR, "fig_sec4_human_hyperexcitability_markers.png"))
print("saved " + os.path.join(FIGDIR, "fig_sec4_human_hyperexcitability_markers.png"))
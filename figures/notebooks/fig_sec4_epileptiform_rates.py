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

VOSSEL = {
    "label": "Vossel 2016",
    "bars": [("AD patients\n(33)", 42.4, COLORS["primary_blue"], "42.4%"),
             ("controls\n(19)", 10.5, COLORS["neutral_gray"], "10.5%")],
    "stat": "p = 0.02",
    "source": "Results Subclinical epileptiform activity was detected in 42.4% of AD patients "
              "and 10.5% of controls (p = 0.02).",
    "annotation": "33 AD patients / 19 age-matched cognitively normal controls; overnight "
                  "video-EEG plus magnetoencephalography; AD patients with no history of seizures",
    "text_access": "abstract_only",
}

CHEN = {
    "label": "Chen 2024",
    "bars": [("dementia patients\n(1617)", 3.0, COLORS["primary_blue"], "3%")],
    "source": "In a study of 1617 dementia patients undergoing routine EEG recordings, "
              "epileptiform discharge were noted in 42 (3%) subjects, 60% of whom did not exhibit "
              "any clinical seizures.",
    "annotation": "1617 dementia patients, routine short EEG; secondary report of a cited study, "
                  "not a cohort the review conducted; 60% of discharge-positive subjects had no "
                  "clinical seizures",
    "text_access": "fulltext",
}

GAO = {
    "label": "Gao 2026", "low": 42.0, "high": 64.0, "value_text": "42%-64%",
    "source": "A striking clinical feature of AD is the higher prevalence of temporal lobe "
              "epilepsy (TLE) and 42%-64% of AD patients exhibit overt epileptic seizures or "
              "subclinical epileptic activity.",
    "annotation": "hatched band drawn outside the bar series with its own legend entry and no n, "
                  "not a data point; range quoted from cited publications; the host paper studies "
                  "tau pathology in mice and reports no clinical cohort; its lower bound is "
                  "numerically near Vossel 2016's primary rate, so the band is probably not "
                  "independent of that cohort",
    "text_access": "fulltext",
}

fig = plt.figure(figsize=(7.1, 5.4))
gs = fig.add_gridspec(2, 1, height_ratios=[1.0, 0.66], hspace=0.55)

ax = fig.add_subplot(gs[0, 0])

# Measured bars, grouped by detection protocol.
positions = [0, 0.8, 2.2]
entries = VOSSEL["bars"] + CHEN["bars"]
for x, (lab, v, colour, vtext) in zip(positions, entries):
    ax.bar([x], [v], width=0.55, color=colour, edgecolor="black", linewidth=0.9,
           linestyle="dashed" if (lab.startswith("AD") or lab.startswith("controls")) else "solid")
    ax.text(x, v + 1.2, vtext, ha="center", va="bottom", fontsize=8)
ax.text(0.4, 58, "overnight video-EEG\nplus magnetoencephalography", fontsize=8,
        ha="center", va="bottom")
ax.text(2.2, 58, "routine (short) EEG,\ndementia patients\n(secondary report)", fontsize=8,
        ha="center", va="bottom")
ax.text(0.4, 53.5, VOSSEL["stat"], fontsize=8, ha="center", va="bottom")

# Quoted literature range, drawn outside the bar series with its own legend entry.
band_x0, band_x1 = 3.2, 4.0
ax.fill_between([band_x0, band_x1], GAO["low"], GAO["high"], facecolor="none",
                edgecolor=COLORS["neutral_gray"], hatch="///", linewidth=0.9,
                label="quoted literature range (no cohort, no n)")
ax.text((band_x0 + band_x1) / 2, GAO["high"] + 1.2, GAO["value_text"], ha="center",
        va="bottom", fontsize=8)
ax.text((band_x0 + band_x1) / 2, GAO["low"] - 2.0, GAO["label"], ha="center", va="top",
        fontsize=8)

ax.set_xticks(positions + [(band_x0 + band_x1) / 2])
ax.set_xticklabels([e[0] for e in entries] + ["quoted range\n(not a cohort)"], fontsize=8)
ax.set_xlim(-0.6, 4.4); ax.set_ylim(0, 92)
ax.set_ylabel("percent of cohort with\nepileptiform activity", fontsize=10)
ax.set_title("Reported rates of epileptiform activity, grouped by detection protocol",
             fontsize=11, fontweight="bold", loc="left")
ax.legend(fontsize=8, loc="upper left", frameon=False)

axN = fig.add_subplot(gs[1, 0]); axN.axis("off")
axN.text(0.0, 1.0, textwrap.fill(
    VOSSEL["label"] + ": " + VOSSEL["annotation"] + ".  " +
    CHEN["label"] + ": " + CHEN["annotation"] + ".  " +
    GAO["label"] + ": " + GAO["annotation"] + ".", width=112),
    fontsize=8, va="top", ha="left", transform=axN.transAxes)
axN.text(0.0, 0.33, textwrap.fill(
    "Heterogeneous comparison - values are not pooled. Detection protocol determines the rate: 3% "
    "refers to routine short EEG in unselected dementia patients and 42.4% to overnight video-EEG "
    "with magnetoencephalography in AD patients without a seizure history. The countable "
    "denominators behind the two bars are 33 AD patients and 1617 dementia patients as reported. "
    "Bars with a dashed outline are values reported in a paper's abstract.", width=112), fontsize=8, va="top", ha="left", transform=axN.transAxes)

save_figure(fig, os.path.join(FIGDIR, "fig_sec4_epileptiform_rates.png"))
print("saved " + os.path.join(FIGDIR, "fig_sec4_epileptiform_rates.png"))
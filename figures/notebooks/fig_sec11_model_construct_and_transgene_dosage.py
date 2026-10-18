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

# Values verbatim from each entry's source sentence. No ratio or fold-change
# notation is emitted for the knock-in or the native-promoter MAPT entry: the
# first source states an equivalence with no numeral, the second an upper bound
# in percent.
guo_upper_bound_percent = 35          # "less than a 35% increase"

fig, (axA, axB) = plt.subplots(1, 2, figsize=(7.1, 4.1),
                               gridspec_kw={"width_ratios": [1.0, 1.0], "wspace": 0.45})
for ax in (axA, axB):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

# ---- Panel A: full-length APP, reported equivalence, no numeral -----------
axA.axhline(0, color=COLORS["neutral_gray"], lw=0.8)
axA.plot([0], [0], marker="s", ms=11, mfc="white", mec=COLORS["sst"], mew=1.8, zorder=3)
axA.set_xlim(-1, 1); axA.set_ylim(-1, 1)
axA.set_xticks([]); axA.set_yticks([0])
axA.set_ylabel("Difference in full-length APP\n(22C11) between arms", fontsize=9)
axA.set_title("A  Full-length APP", fontsize=9.5, loc="left", fontweight="bold")
axA.text(0, -0.25,
         "reported equivalence, no ratio stated:\nsimilar levels in the knock-in (NA) arm\n"
         "and the NOG background strain\nat 3, 6 and 9 months (cortex;\nno numeric value reported)",
         ha="center", va="top", fontsize=7.6, color=COLORS["neutral_gray"])

# ---- Panel B: tau, upper bound in the source's own convention -------------
axB.set_xlim(-0.8, 0.8); axB.set_ylim(0, 60)
axB.bar([0], [guo_upper_bound_percent], width=0.42, color=COLORS["pv"], edgecolor="black",
        linewidth=0.9)
axB.annotate("", xy=(0, 20), xytext=(0, 34), arrowprops=dict(arrowstyle="-|>", color="black", lw=1.1))
axB.text(0, guo_upper_bound_percent + 3, "less than a 35% increase", ha="center", va="bottom",
         fontsize=8.5)
axB.set_xticks([0])
axB.set_xticklabels(["genomic human MAPT\nunder its native promoter"], fontsize=8.5)
axB.set_ylabel("Increase in human tau over\nwild-type mouse tau (%)", fontsize=9)
axB.set_title("B  Tau", fontsize=9.5, loc="left", fontweight="bold")
axB.text(0, 18, "upper bound,\nnot a point estimate", ha="center", va="center", fontsize=7.8,
         color="white", rotation=90)

# rTg4510: review-sourced value, no axis position, placed clear of the panel B axis
fig.text(0.5, -0.13,
         "rTg4510, value as reported in a review article rather than measured there, and not placed on either axis:\n"
         "P301L tau at about 13 times endogenous levels, reducible to about 3 times with doxycycline, a reduction "
         "that reversed\nbehavioural impairment while neurofibrillary tangles continued to increase. The primary "
         "measurement is not represented here.",
         ha="center", va="top", fontsize=7.8,
         bbox=dict(boxstyle="round,pad=0.45", facecolor="#F7F7F7", edgecolor=COLORS["neutral_gray"],
                   linewidth=0.8))
fig.text(0.5, -0.33,
         "Heterogeneous comparison - values not pooled. The two panels measure different proteins and share no axis, "
         "so heights must not be compared\nacross them. No entry states an animal n in the retrieved sentences and no "
         "entry reports a confidence interval.",
         ha="center", va="top", fontsize=7.6)

save_figure(fig, os.path.join(FIGDIR, "fig_sec11_model_construct_and_transgene_dosage.png"))
print("saved")

import sys, os

# Resolve paths so the notebook runs from either its own directory or the repo root.
HERE = os.path.abspath(".") if os.path.exists("shared_style.py") else os.path.abspath("figures/notebooks")
sys.path.insert(0, HERE)
OUTDIR = os.path.normpath(os.path.join(HERE, ".."))

import matplotlib.pyplot as plt
from shared_style import COLORS, apply_style, save_figure

apply_style()
plt.rcParams.update({"font.size": 10, "legend.fontsize": 9})  # figure authored at the 10 pt document size

# --- Values: every number below is verbatim in that entry's source sentence ---
# Antonoudiou et al. 2020 (10.1523/jneurosci.0261-20.2020) -> panel A
A = dict(value=0.69, err=0.057, stat="t = 5.40, p < 0.001 (one-sample t test)\nn not reported")
# Liu et al. 2020 (10.1126/sciadv.aay4073) -> panel B
B = dict(sst=0.39, sst_err=0.02, sst_n=25, pv=0.50, pv_err=0.01, pv_n=22,
         stat="P < 0.0001, unpaired t test")
# Udakis et al. 2020 (10.1038/s41467-020-18074-8) -> panel C
C = dict(base=0.53, base_err=0.04, post=0.5, post_err=0.08,
         stat="n = 8, p > 0.05\nwithin-condition null")

fig, axes = plt.subplots(1, 3, figsize=(7.1, 3.3))
fig.subplots_adjust(wspace=0.70, bottom=0.30)

# ---------------- Panel A: fraction of baseline gamma power -------------------
ax = axes[0]
ax.errorbar([0], [A["value"]], yerr=[A["err"]], fmt="o", ms=7,
            color=COLORS["sst"], ecolor=COLORS["sst"], elinewidth=1.2,
            capsize=4, linestyle="none")
ax.axhline(1.0, ls=":", lw=1.0, color=COLORS["neutral_gray"])
ax.text(0.62, 1.01, "baseline", fontsize=8, va="bottom", ha="right",
        color=COLORS["neutral_gray"])
ax.annotate("", xy=(0.55, 0.30), xytext=(0.55, 0.75),
            arrowprops=dict(arrowstyle="->", lw=1.1, color=COLORS["decrease"]))
ax.text(0.60, 0.52, "larger\neffect", fontsize=8, va="center", ha="left",
        color=COLORS["decrease"])
ax.text(0, A["value"] + A["err"] + 0.06, "0.69", fontsize=8, ha="center")
ax.set_xlabel(A["stat"], fontsize=8, labelpad=6)
ax.set_xlim(-0.6, 1.1); ax.set_ylim(0, 1.3)
ax.set_xticks([0]); ax.set_xticklabels(["SST+\nphotoinhibition"], fontsize=9)
ax.set_ylabel("Slow gamma power\n(fraction of baseline period)")
ax.set_title("A  Antonoudiou 2020", fontsize=11, fontweight="bold", loc="left")

# ---------------- Panel B: firing-suppression index ---------------------------
ax = axes[1]
ax.errorbar([0], [B["sst"]], yerr=[B["sst_err"]], fmt="o", ms=7, color=COLORS["sst"],
            ecolor=COLORS["sst"], elinewidth=1.2, capsize=4, linestyle="none")
ax.errorbar([1], [B["pv"]], yerr=[B["pv_err"]], fmt="s", ms=7, color=COLORS["pv"],
            ecolor=COLORS["pv"], elinewidth=1.2, capsize=4, linestyle="none")
ax.text(0, B["sst"] - B["sst_err"] - 0.03, "0.39\nn = 25", fontsize=8, ha="center", va="top")
ax.text(1, B["pv"] + B["pv_err"] + 0.03, "0.50\nn = 22", fontsize=8, ha="center", va="bottom")
ax.annotate("", xy=(1.62, 0.60), xytext=(1.62, 0.30),
            arrowprops=dict(arrowstyle="->", lw=1.1, color=COLORS["increase"]))
ax.text(1.57, 0.45, "stronger\nsuppression", fontsize=8, va="center", ha="right",
        color=COLORS["increase"])
ax.set_xlabel(B["stat"], fontsize=8, labelpad=6)
ax.set_xlim(-0.4, 1.75); ax.set_ylim(0, 0.72)
ax.set_xticks([0, 1]); ax.set_xticklabels(["SST\nactivation", "PV\nactivation"], fontsize=9)
ax.set_ylabel("Wide-spiking unit\nfiring-suppression index")
ax.set_title("B  Liu 2020", fontsize=11, fontweight="bold", loc="left")

# ---------------- Panel C: spike probability ----------------------------------
ax = axes[2]
ax.errorbar([0, 1], [C["base"], C["post"]], yerr=[C["base_err"], C["post_err"]],
            fmt="o", ms=7, color=COLORS["excitatory_pyramidal"],
            ecolor=COLORS["excitatory_pyramidal"], elinewidth=1.2, capsize=4,
            linestyle="-", lw=1.0)
ax.text(0, C["base"] + C["base_err"] + 0.05, "0.53", fontsize=8, ha="center")
ax.text(1, C["post"] + C["post_err"] + 0.05, "0.5", fontsize=8, ha="center")
ax.set_xlabel(C["stat"], fontsize=8, labelpad=6)
ax.set_xlim(-0.5, 1.5); ax.set_ylim(0, 0.95)
ax.set_xticks([0, 1]); ax.set_xticklabels(["baseline", "after\nSST-iLTP"], fontsize=9)
ax.set_ylabel("Spike probability\n(Schaffer-collateral stimulation)")
ax.set_title("C  Udakis 2020", fontsize=11, fontweight="bold", loc="left")

for ax in axes:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

fig.text(0.5, 0.005,
         "Heterogeneous comparison - values not pooled: three different quantities on three independent axes. "
         "Error bars are the source sentences' own +/- terms (dispersion type not stated).\n"
         "Preparations: ventral hippocampal CA3 ex vivo (A), prefrontal cortex in vivo (B), CA1 slices (C).",
         ha="center", va="bottom", fontsize=8, color=COLORS["neutral_gray"])

save_figure(fig, os.path.join(OUTDIR, "fig_sec8_dendritic_versus_perisomatic_signature.png"))

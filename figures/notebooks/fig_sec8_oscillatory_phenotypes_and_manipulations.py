import sys, os

# Resolve paths so the notebook runs from either its own directory or the repo root.
HERE = os.path.abspath(".") if os.path.exists("shared_style.py") else os.path.abspath("figures/notebooks")
sys.path.insert(0, HERE)
OUTDIR = os.path.normpath(os.path.join(HERE, ".."))

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from shared_style import COLORS, apply_style, save_figure

apply_style()

# --- Values: every number below is verbatim in that entry's source sentence ---
# Xiao et al. 2017 (10.7554/elife.23798) -> panel A
XIAO = [("WT", 5.1, 0.73), ("Nptx2-/-", 3.8, 0.63), ("hAPP", 3.9, 0.79),
        ("hAPP/\nNptx2-/-", 1.7, 0.68)]
XIAO_STAT = "p = 0.0199, one-way ANOVA; n not stated"
# Etter et al. 2019 (10.1038/s41467-019-13260-9) -> statistics row in panel A
ETTER = ("Etter 2019 (statistic only, no point estimate, no axis position):\n"
         "slow (30-60 Hz) gamma F(1,56) = 9.89, p = 0.0027;\n"
         "fast (60-120 Hz) gamma F(1,56) = 0.8096, p = 0.3721; n = 6")
# Viney et al. 2022 (10.1016/j.celrep.2022.111646) -> panel B, band-local axes
VINEY = {"slow gamma (IMF4)": [("ntg", 28.7, 0.7, 6), ("tg", 29.3, 1.2, 5)],
         "mid gamma (IMF3)":  [("ntg", 56.8, 0.8, 5), ("tg", 59.3, 4.1, 4)]}
# Rhee et al. 2026 (10.1038/s41398-026-04060-z) -> panel C
RHEE = [("control", 8.78, 0.11), ("PV-Grik1-/-", 9.46, 0.12)]
# Hadler et al. 2024 (10.1126/sciadv.adj7427) -> panel D (model output)
HADLER = (2.5, 3.0)

fig = plt.figure(figsize=(7.1, 5.8))
gs = GridSpec(2, 4, figure=fig, hspace=1.05, wspace=1.00)

# ---------------- Panel A: gamma POWER in amyloid models ----------------------
axA = fig.add_subplot(gs[0, 0:2])
xs = range(len(XIAO))
axA.errorbar(list(xs), [v for _, v, _ in XIAO], yerr=[e for _, _, e in XIAO],
             fmt="o", ms=6, color=COLORS["mixed_gabaergic"],
             ecolor=COLORS["mixed_gabaergic"], elinewidth=1.2, capsize=4,
             linestyle="none")
for x, (lab, v, e) in zip(xs, XIAO):
    axA.text(x, v + e + 0.25, f"{v}", fontsize=8, ha="center")
axA.set_xticks(list(xs)); axA.set_xticklabels([lab for lab, _, _ in XIAO], fontsize=8)
axA.set_ylim(0, 7.0); axA.set_xlim(-0.5, 3.6)
axA.set_ylabel("Normalised hippocampal\ngamma power (z-score)")
axA.set_xlabel(XIAO_STAT, fontsize=8, labelpad=6)
axA.set_title("A  Gamma power (Xiao 2017)", fontsize=10,
              fontweight="bold", loc="left")
axA.text(0.0, -0.40, ETTER, fontsize=8, va="top", ha="left",
         transform=axA.transAxes, color=COLORS["neutral_gray"])

# ---------------- Panel B: gamma PEAK FREQUENCY, tauopathy model --------------
band_axes = [fig.add_subplot(gs[0, 2]), fig.add_subplot(gs[0, 3])]
for ax, (band, pts) in zip(band_axes, VINEY.items()):
    for x, (lab, v, e, n) in enumerate(pts):
        col = COLORS["neutral_gray"] if lab == "ntg" else COLORS["increase"]
        ax.errorbar([x], [v], yerr=[e], fmt="o", ms=6, color=col, ecolor=col,
                    elinewidth=1.2, capsize=4, linestyle="none")
        ax.text(x, v + e + 0.35, f"{v}\nn = {n}", fontsize=8, ha="center")
    ax.set_xticks([0, 1]); ax.set_xticklabels([lab for lab, _, _, _ in pts], fontsize=8)
    ax.set_xlim(-0.6, 1.6)
    lo = min(v - e for _, v, e, _ in pts) - 2.0
    hi = max(v + e for _, v, e, _ in pts) + 3.2
    ax.set_ylim(lo, hi)
    ax.set_title(band, fontsize=9, loc="left")
band_axes[0].set_ylabel("Gamma peak frequency (Hz)")
band_axes[0].text(-0.20, 1.34, "B  Gamma peak frequency (Viney 2022)",
                  fontsize=10, fontweight="bold", transform=band_axes[0].transAxes)
band_axes[1].set_xlabel('"similar distributions for\nboth genotypes";\nno test statistic reported',
                        fontsize=8, labelpad=6)

# ---------------- Panel C: theta peak frequency, PV-side manipulation ---------
axC = fig.add_subplot(gs[1, 0:2])
for x, (lab, v, e) in enumerate(RHEE):
    col = COLORS["neutral_gray"] if lab == "control" else COLORS["pv"]
    axC.errorbar([x], [v], yerr=[e], fmt="s", ms=6, color=col, ecolor=col,
                 elinewidth=1.2, capsize=4, linestyle="none")
    axC.text(x, v + e + 0.08, f"{v}", fontsize=8, ha="center")
axC.set_xticks([0, 1]); axC.set_xticklabels([lab for lab, _, _ in RHEE], fontsize=9)
axC.set_xlim(-0.6, 1.6); axC.set_ylim(8.3, 9.9)
axC.set_ylabel("Hippocampal theta\npeak frequency (Hz)")
axC.set_xlabel("p = 0.0007, unpaired t test; no difference in mPFC (p = 0.264);\n"
               "n not reported", fontsize=8, labelpad=6)
axC.set_title("C  Theta frequency (Rhee 2026)", fontsize=10,
              fontweight="bold", loc="left")

# ---------------- Panel D: simulated low-gamma power fold change --------------
axD = fig.add_subplot(gs[1, 2:4])
axD.bar([0], [HADLER[1] - HADLER[0]], bottom=[HADLER[0]], width=0.45,
        color="white", edgecolor=COLORS["simulated"], hatch="///", linewidth=1.0)
axD.axhline(1.0, ls=":", lw=1.0, color=COLORS["neutral_gray"])
axD.text(0.45, 1.02, "no change", fontsize=8, ha="right", va="bottom",
         color=COLORS["neutral_gray"])
axD.text(0, HADLER[1] + 0.15, "2.5 to 3", fontsize=8, ha="center")
axD.set_xticks([0]); axD.set_xticklabels(["PYR + PVI-LTP\n(model condition)"], fontsize=8)
axD.set_xlim(-0.6, 0.6); axD.set_ylim(0, 3.8)
axD.set_ylabel("Peak low-gamma power\n(fold change)")
axD.set_xlabel("model output (simulated); no biological sample size", fontsize=8, labelpad=6)
axD.set_title("D  Simulated gamma (Hadler 2024)", fontsize=10,
              fontweight="bold", loc="left")

for ax in [axA, axC, axD] + band_axes:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

fig.text(0.5, -0.04,
         "Heterogeneous comparison - values not pooled. Power (A), peak frequency (B), theta frequency (C) and a "
         "simulated fold change (D) occupy four independent axes.\nError bars are the source sentences' own +/- terms "
         "(dispersion type not stated). Panels C and D manipulate parvalbumin-side elements, not somatostatin neurons.",
         ha="center", va="top", fontsize=8, color=COLORS["neutral_gray"])

save_figure(fig, os.path.join(OUTDIR, "fig_sec8_oscillatory_phenotypes_and_manipulations.png"))

import sys, os

# Resolve paths so the notebook runs from either its own directory or the repo root.
HERE = os.path.abspath(".") if os.path.exists("shared_style.py") else os.path.abspath("figures/notebooks")
sys.path.insert(0, HERE)
OUTDIR = os.path.normpath(os.path.join(HERE, ".."))

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from shared_style import COLORS, apply_style, save_figure

apply_style()

# --- Values: every number below is verbatim in that entry's source sentence,
# --- except the two trial totals (32; 22), which come from the named abstracts.
# Panel A: table rows (Kam et al. 2019; Wunderlin et al. 2023)
TABLE_COLS = ["Design", "Spindle\nmeasure", "Outcome", "Statistic (type named)", "n"]
TABLE_ROWS = [
    ["Kam 2019\nobservational,\ncross-sectional",
     "N2 spindle\ndensity",
     "lower spindle density\nwith higher CSF tau\n(negative association)",
     "incremental variance\nexplained in CSF total tau:\ndelta R2 = 0.284 (p = 0.001)",
     "not\nstated"],
    ["Wunderlin 2023\nbetween-subject\nsham-controlled\n3-night trial",
     "SO-coupled\nspindle\ncount",
     "+24% (intervention)\nvs 0% (control)",
     "paired t statistic: t = 2.81,\nP = 0.01; group difference\nt = -2.41, P = 0.02",
     "32 total\n(abstract)"],
]
# Panel B: direction glyphs (Yu et al. 2026; Kolling et al. 2026)
GLYPHS = [
    dict(label="Yu 2026 (APP amyloid model)\nslow-oscillation (0.5-1 Hz) and\ndelta (1-4 Hz) power vs own baseline",
         direction="up", stat="significant increase; no effect size reported",
         method="chronic EEG"),
    dict(label="Kolling 2026 (tau in dorsal raphe\n5-HT neurons) nREM percent delta\ncomposition vs a control-virus group",
         direction="down", stat="virus effect p = 0.0328 (3-way ANOVA);\np = 0.0189 (2-way ANOVA)",
         method="longitudinal EEG"),
]
# Panel C: human statistics, one column each (Wunderlin et al. 2026; Dikici et al. 2026)
WUND26 = "beta = 2.5, p = 0.006\n(regression interaction,\nthird experimental night)"
DIKICI = dict(value=24.1, sd=72.1, n=10,
              stat="pairwise p = 0.077;\ninteraction p = 0.068")

fig = plt.figure(figsize=(7.1, 7.4))
gs = GridSpec(3, 2, figure=fig, height_ratios=[1.25, 0.85, 1.05], hspace=0.75, wspace=0.45)

# ---------------- Panel A: table-form figure ---------------------------------
axA = fig.add_subplot(gs[0, :]); axA.axis("off")
axA.set_title("A  Sleep spindles and Alzheimer biomarkers: one association, one trial",
              fontsize=10, fontweight="bold", loc="left", pad=10)
xpos = [0.00, 0.175, 0.305, 0.575, 0.925]
ytop = 0.88
for x, col in zip(xpos, TABLE_COLS):
    axA.text(x, ytop, col, fontsize=8.5, fontweight="bold", va="top", ha="left",
             transform=axA.transAxes)
axA.plot([0, 1], [ytop - 0.09] * 2, lw=0.8, color=COLORS["neutral_gray"],
         transform=axA.transAxes, clip_on=False)
for r, row in enumerate(TABLE_ROWS):
    y = ytop - 0.17 - r * 0.42
    for x, cell in zip(xpos, row):
        axA.text(x, y, cell, fontsize=8, va="top", ha="left", transform=axA.transAxes)
    if r == 0:
        axA.plot([0, 1], [y - 0.30] * 2, lw=0.5, color=COLORS["light_gray"],
                 transform=axA.transAxes, clip_on=False)
axA.text(0, -0.30, "Not comparable percentages: an unsigned variance statistic and a relative change; "
                   "never drawn as bars.", fontsize=8, va="top", ha="left",
         transform=axA.transAxes, color=COLORS["neutral_gray"])

# ---------------- Panel B: direction glyphs, mouse ---------------------------
axB = fig.add_subplot(gs[1, :]); axB.axis("off")
axB.set_title("B  Mouse NREM oscillation changes: direction of effect only",
              fontsize=10, fontweight="bold", loc="left", pad=10)
for i, g in enumerate(GLYPHS):
    y = 0.72 - i * 0.55
    col = COLORS["increase"] if g["direction"] == "up" else COLORS["decrease"]
    arrow = (0.055, y - 0.16, 0, 0.26) if g["direction"] == "up" else (0.055, y + 0.10, 0, -0.26)
    axB.arrow(arrow[0], arrow[1], arrow[2], arrow[3], width=0.012, head_width=0.045,
              head_length=0.09, color=col, transform=axB.transAxes,
              length_includes_head=True, clip_on=False)
    axB.text(0.12, y + 0.08, g["label"], fontsize=8, va="top", ha="left",
             transform=axB.transAxes)
    axB.text(0.58, y + 0.08, g["stat"] + "\n" + g["method"] + "; group sizes not stated",
             fontsize=8, va="top", ha="left", transform=axB.transAxes,
             color=COLORS["neutral_gray"])
axB.text(0, -0.28, "No magnitude axis: no effect size is available from either source. "
                   "Kolling et al. report the sleep effects as primarily sex-divergent.",
         fontsize=8, va="top", ha="left", transform=axB.transAxes,
         color=COLORS["neutral_gray"])

# ---------------- Panel C: human statistics, non-pooled -----------------------
axC1 = fig.add_subplot(gs[2, 0]); axC1.axis("off")
axC1.set_title("C  Wunderlin 2026 (statistic, no axis)", fontsize=9.5,
               fontweight="bold", loc="left", pad=8)
axC1.text(0.5, 0.60, WUND26, fontsize=9, ha="center", va="center",
          transform=axC1.transAxes)
axC1.text(0.5, 0.18, "subgroup-restricted: per the source, the\ncoupling-amyloid benefit applies to\n"
                     "cognitively impaired individuals.\nUnits and scaling of beta not stated.",
          fontsize=8, ha="center", va="center", transform=axC1.transAxes,
          color=COLORS["neutral_gray"])

axC2 = fig.add_subplot(gs[2, 1])
axC2.errorbar([0], [DIKICI["value"]], yerr=[DIKICI["sd"]], fmt="o", ms=7,
              color=COLORS["mixed_gabaergic"], ecolor=COLORS["mixed_gabaergic"],
              elinewidth=1.2, capsize=4, linestyle="none")
axC2.axhline(0, ls=":", lw=1.0, color=COLORS["neutral_gray"])
axC2.text(0.12, DIKICI["value"], "+24.1%\n(SD 72.1%)", fontsize=8, ha="left", va="center")
axC2.set_xticks([0])
axC2.set_xticklabels([f"anodal so-tDCS\nvs sham\n(n = {DIKICI['n']} of 22 [abstract],\nintermediate-to-evening\nchronotypes)"],
                     fontsize=8)
axC2.set_xlim(-0.5, 1.1); axC2.set_ylim(-60, 110)
axC2.set_ylabel("NREM spindle power\nchange (%)")
axC2.set_xlabel(DIKICI["stat"], fontsize=8, labelpad=6)
axC2.set_title("Dikici 2026", fontsize=9.5, fontweight="bold", loc="left", pad=8)
axC2.spines["top"].set_visible(False); axC2.spines["right"].set_visible(False)

fig.text(0.5, -0.085,
         "Heterogeneous comparison - values not pooled. Mouse cortical EEG (B) and human scalp EEG (A, C) are not "
         "comparable in absolute terms, and the\nhuman statistics in panel C share no axis. The two Wunderlin entries "
         "plausibly share participants and are not independent replications.",
         ha="center", va="top", fontsize=8, color=COLORS["neutral_gray"])

save_figure(fig, os.path.join(OUTDIR, "fig_sec8_sleep_oscillations_tau_and_memory.png"))

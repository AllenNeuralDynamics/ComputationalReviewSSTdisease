"""Figure: gamma stimulation in humans, ordered by design (section 10).

Three panels, three measurement families, no pooling. Panel A carries two
sham- or control-referenced interval estimates whose scales differ and are
therefore annotated row by row. Panel B carries a test statistic, which is
not an effect size, and so has no magnitude axis. Panel C carries two
structural percent-change measures from a single randomized cohort.
Every number is quoted from its entry's own source sentence.
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath("__file__")) if "__file__" not in globals() else os.path.dirname(os.path.abspath(__file__)))

import matplotlib.pyplot as plt
from shared_style import COLORS, apply_style, save_figure

apply_style()
OUTDIR = ".."   # notebooks live in figures/notebooks/; figures are written to figures/

# ---------------------------------------------------------------- panel A
# Interval estimates in patient populations. Scales are NOT comparable.
PANEL_A = [
    dict(label="Ang 2025",
         value=0.16, lo=-0.36, hi=0.68,
         metric="pooled standardized mean difference, cognition vs control "
                "(P = 0.55, null)",
         detail="meta-analysis of randomized 40 Hz light stimulation trials; "
                "11 studies, 341 participants; AD and MCI"),
    dict(label="Lim 2026",
         value=0.059, lo=0.007, hi=0.111,
         metric="composite cognitive z-score difference at Day 56, active - sham "
                "(p = 0.028)",
         detail="prespecified exploratory <45-year subgroup, subgroup size not reported; "
                "43 randomized / 41 analysed;\npost-COVID cognitive impairment; "
                "transcranial + intranasal photobiomodulation, 8 weeks"),
]

# ---------------------------------------------------------------- panel B
PANEL_B = dict(
    label="Attokaren 2026",
    stat="Kruskal-Wallis \u03c7\u00b2(2) = 7.98, p = 0.018",
    note="test statistic, not an effect size \u2014 no magnitude axis",
    detail="62 healthy adults; single 1-hour session of 40 Hz audiovisual flicker "
           "vs constant light vs random flicker; psychomotor vigilance accuracy",
)

# ---------------------------------------------------------------- panel C
# Percent change from baseline over 6 months, active vs sham (one trial).
PANEL_C = [
    dict(structure="Cerebral white matter volume\n(Da 2024; N = 38)",
         active=0.17, active_err=1.08, sham=-2.54, sham_err=1.38),
    dict(structure="Corpus callosum area\n(Da 2024; N = 50, 33 active / 17 sham)",
         active=0.20, active_err=0.70, sham=-2.08, sham_err=0.87),
]

fig = plt.figure(figsize=(7.08, 7.4))
gs = fig.add_gridspec(3, 1, height_ratios=[1.25, 0.50, 1.20], hspace=0.55,
                      left=0.11, right=0.985, top=0.955, bottom=0.085)

# ----- Panel A -----------------------------------------------------------
axA = fig.add_subplot(gs[0])
ys = [1.70, 0.0]
for y, e in zip(ys, PANEL_A):
    axA.plot([e["lo"], e["hi"]], [y, y], color=COLORS["SST"], lw=1.6,
             solid_capstyle="butt", zorder=3)
    axA.plot([e["lo"], e["lo"]], [y - 0.10, y + 0.10], color=COLORS["SST"], lw=1.6, zorder=3)
    axA.plot([e["hi"], e["hi"]], [y - 0.10, y + 0.10], color=COLORS["SST"], lw=1.6, zorder=3)
    axA.plot([e["value"]], [y], marker="s", ms=6, color=COLORS["SST"],
             markeredgecolor="black", markeredgewidth=0.6, zorder=4)
    axA.annotate("{:g}  [{:g}, {:g}]".format(e["value"], e["lo"], e["hi"]),
                 xy=(e["value"], y), xytext=(0, -13), textcoords="offset points",
                 ha="center", va="top", fontsize=7.5, color="#111111")
    axA.text(0.005, y + 0.62, e["metric"], transform=axA.get_yaxis_transform(),
             fontsize=7.5, va="bottom", ha="left", color="#333333")
    axA.text(0.005, y + 0.56, e["detail"], transform=axA.get_yaxis_transform(),
             fontsize=7, va="top", ha="left", color="#666666", linespacing=1.4)

axA.axvline(0, color="#444444", lw=0.8, ls="--", zorder=1)
axA.set_yticks(ys)
axA.set_yticklabels([e["label"] for e in PANEL_A], fontweight="bold", fontsize=8.5)
axA.set_ylim(-0.75, 2.85)
axA.set_xlim(-0.65, 0.95)
axA.set_xlabel("effect estimate (row-specific scale; positions not comparable between rows)")
axA.set_title("A   Interval estimates in patient populations", loc="left",
              fontsize=10, fontweight="bold")
axA.spines["left"].set_visible(False)
axA.tick_params(axis="y", length=0)

# ----- Panel B -----------------------------------------------------------
axB = fig.add_subplot(gs[1])
axB.axis("off")
axB.set_title("B   Acute single session in healthy adults", loc="left",
              fontsize=10, fontweight="bold")
axB.add_patch(plt.Rectangle((0.0, 0.05), 1.0, 0.82, transform=axB.transAxes,
                            facecolor="#F4F4F4", edgecolor="#CCCCCC", lw=0.6))
axB.text(0.02, 0.68, PANEL_B["label"], transform=axB.transAxes, fontsize=8.5,
         fontweight="bold", va="center")
axB.text(0.22, 0.68, PANEL_B["stat"], transform=axB.transAxes, fontsize=9, va="center",
         color=COLORS["SST"])
axB.text(0.22, 0.44, PANEL_B["note"], transform=axB.transAxes, fontsize=7.5,
         va="center", style="italic", color=COLORS["conflict_marker"])
axB.text(0.02, 0.19, PANEL_B["detail"], transform=axB.transAxes, fontsize=7,
         va="center", color="#666666")

# ----- Panel C -----------------------------------------------------------
axC = fig.add_subplot(gs[2])
xs = [0, 1]
wbar = 0.3
for i, e in enumerate(PANEL_C):
    for off, key, errkey, colour, arm in ((-wbar / 2 - 0.02, "active", "active_err",
                                           COLORS["active_arm"], "active"),
                                          (+wbar / 2 + 0.02, "sham", "sham_err",
                                           COLORS["sham_arm"], "sham")):
        x = xs[i] + off
        axC.bar(x, e[key], width=wbar, color=colour, edgecolor="black", lw=0.6,
                zorder=2, label=arm if i == 0 else None)
        bars = axC.errorbar(x, e[key], yerr=e[errkey], fmt="none", ecolor="#333333",
                            elinewidth=1.0, capsize=3, zorder=3)
        for b in bars[2]:
            b.set_linestyle("--")
        va = "bottom" if e[key] >= 0 else "top"
        dy = e[errkey] + 0.18 if e[key] >= 0 else -(e[errkey] + 0.18)
        axC.text(x, e[key] + dy, "{:+.2f}".format(e[key]), ha="center", va=va,
                 fontsize=7.5)

axC.axhline(0, color="#444444", lw=0.8)
axC.set_xticks(xs)
axC.set_xticklabels([e["structure"] for e in PANEL_C], fontsize=8)
axC.set_ylabel("change from baseline over 6 months\n(percent of baseline)")
axC.set_xlim(-0.6, 1.6)
axC.set_ylim(-4.4, 2.2)
axC.legend(frameon=False, fontsize=8, loc="upper right", ncol=2)
axC.set_title("C   Structural measures, active versus sham (one randomized cohort, OVERTURE NCT03556280)",
              loc="left", fontsize=9.5, fontweight="bold")
axC.text(0.0, -0.30, "Error bars dashed: dispersion type not stated in either source. "
                     "The two structures are nested (corpus callosum lies within the white matter\n"
                     "compartment) and come from overlapping, unequal subsets of one trial \u2014 "
                     "not independent replication.",
         transform=axC.transAxes, fontsize=7, color="#666666", va="top", ha="left")

fig.text(0.11, 0.018, "Heterogeneous comparison \u2014 values not pooled; no summary estimate is drawn. "
                      "All values extracted from the source papers' full text.",
         fontsize=7.5, style="italic", color=COLORS["conflict_marker"], ha="left")

save_figure(fig, os.path.join(OUTDIR, "fig_sec10_gamma_stimulation_evidence_ladder.png"))

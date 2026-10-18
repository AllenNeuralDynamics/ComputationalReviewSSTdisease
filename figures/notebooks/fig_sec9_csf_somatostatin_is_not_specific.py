"""Figure: cerebrospinal fluid somatostatin across diagnoses (section 09).

Built strictly from the final figure plan for section_09. Every printed
numeral is verbatim from a cited source sentence. Dispersion terms are
labelled only where the source states them; where the source does not, the
error bar is drawn dashed and labelled "dispersion type not stated".
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else ".")

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from shared_style import COLORS, apply_style, save_figure

apply_style()

DAGGER = "\u2021"

# ------------------------------------------------------------------- data
A_rows = [
    ("Dupont 1982*\nParkinson's disease", "down", "\u2018about 40% less\u2019",
     "88.0 \u00b1 4.1 vs 147.3 \u00b1 5.1 pg per milliliter;\ndispersion type not stated; 39 patients"),
    ("Masson 1990*\nParkinson's disease", "down", "P less than .02",
     "35 patients, 11 controls; values lowest\nin the untreated group"),
    ("Strittmatter 1997* " + DAGGER + "\nSDAT", "down", "p < 0.05",
     "53 patients, 12 elderly controls; long-term neuroleptics\nsignificantly raised the measure"),
    ("Sunderland 1987*\nAD and late-life depression", "down", "no number reported",
     "three-group study: 12 Alzheimer's disease, 15 age-matched\ncontrols, 20 older depressed subjects"),
]

B_rows = [
    ("Strittmatter 1997* " + DAGGER, "SDAT; 53 patients", "dementia score\n(higher = worse)",
     "r = -0.65, p < 0.05", "down"),
    ("Minthon 1997*", "Alzheimer's disease;\n34 patients, no controls", "severity of dementia\n(higher = worse)",
     "p < 0.013 (negative)", "down"),
    ("Sunderland 1987*", "pooled three-group cohort;\nall 47 subjects", "cognitive functioning\n(higher = better)",
     "significant positive correlation;\nnot significant within groups", "up"),
    ("Duron 2018", "memory clinic; 43 with mild\ncognitive impairment", "annotation row:\nwithin-cohort associations",
     "amyloid-beta 1-42 p = 0.01;\nblood total cholesterol p = 0.03", "neutral"),
]

C_groups = [
    # label, value, err, err_stated, is_comparison_group, study
    ("DAT\nn = 27", 17.5, 5.0, False, False, "Atack 1988*"),
    ("DAT + EPS\nn = 7", 16.4, 5.0, False, False, "Atack 1988*"),
    ("controls\nn = 26", 23.1, 8.2, False, True, "Atack 1988*"),
    ("AD\nn = 10", 14.6, 1.5, True, False, "Serby 1984*"),
    ("other neuro.\npatients, n = 9", 26.7, 3.2, True, True, "Serby 1984*"),
]

D_groups = [
    ("SDAT,\nGDS 7", 18.6, 7.9, False),
    ("Binswanger's\ndisease", 19.7, 11.6, False),
    ("controls\nsize not reported", 30.5, 8.6, True),
]

# ----------------------------------------------------------------- figure
fig = plt.figure(figsize=(7.1, 11.6))
gs = GridSpec(4, 2, figure=fig, height_ratios=[0.95, 1.55, 1.35, 0.25],
              hspace=0.95, wspace=0.42)


def tidy(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def head(ax, letter, title, note=None, fs=10.2, ytitle=1.22, ynote=1.05):
    ax.text(0.0, ytitle, f"{letter}   {title}", transform=ax.transAxes,
            fontsize=fs, fontweight="bold", va="bottom")
    if note:
        ax.text(0.0, ynote, note, transform=ax.transAxes, fontsize=7.4,
                style="italic", va="bottom", color=COLORS["annotation"])


GLYPH = {"down": ("\u25bc", COLORS["decrease"]),
         "up": ("\u25b2", COLORS["increase"]),
         "neutral": ("\u25cb", COLORS["neutral_gray"])}

# ---- A : direction and significance strip, no numeric axis
axA = fig.add_subplot(gs[0, :])
axA.axis("off")
head(axA, "A", "Patient-versus-control difference: direction and the reported statistic",
     "no shared numeric axis \u2014 the rows are not comparable in magnitude", ytitle=1.06, ynote=0.96)
n = len(A_rows)
for i, (lab, direction, stat, note) in enumerate(A_rows):
    y = 0.80 - i * 0.235
    g, c = GLYPH[direction]
    axA.text(0.0, y, lab, fontsize=7.2, va="center", transform=axA.transAxes)
    axA.text(0.235, y, g, fontsize=9, va="center", color=c, transform=axA.transAxes)
    axA.text(0.270, y, stat, fontsize=7.2, va="center", fontweight="bold",
             transform=axA.transAxes)
    axA.text(0.530, y, note, fontsize=7.0, va="center", color=COLORS["annotation"],
             transform=axA.transAxes)

# ---- B : table-form clinical-association panel
axB = fig.add_subplot(gs[1, :])
axB.axis("off")
head(axB, "B", "Relationship with clinical state: one row per study, verbatim statistic",
     "table form, no numeric axis \u2014 no two rows report the same statistic",
     ytitle=1.04, ynote=0.96)
cols = [0.0, 0.185, 0.44, 0.665]
hdr = ["study", "cohort and n", "clinical variable", "reported statistic"]
for x, h in zip(cols, hdr):
    axB.text(x, 0.84, h, fontsize=7.2, fontweight="bold", va="center",
             color=COLORS["annotation"], transform=axB.transAxes)
axB.plot([0.0, 1.0], [0.79, 0.79], color=COLORS["light_gray"], lw=0.8,
         transform=axB.transAxes, clip_on=False)
for i, row in enumerate(B_rows):
    y = 0.66 - i * 0.215
    g, c = GLYPH[row[4]]
    for x, cell in zip(cols, row[:4]):
        axB.text(x, y, cell, fontsize=6.9, va="center", transform=axB.transAxes)
    axB.text(0.965, y, g, fontsize=9, va="center", color=c, transform=axB.transAxes)
axB.text(0.0, -0.10, DAGGER + " same research group and a same-sized 53-patient cohort as the "
         "Alzheimer row in panel D, reporting the identical coefficient; bracketed as one observation, "
         "not two replications.", fontsize=7.0, va="top", color=COLORS["annotation"],
         transform=axB.transAxes)

# ---- C : absolute concentrations, pg/mL
axC = fig.add_subplot(gs[2, 0])
xs = [0, 1.35, 2.7, 4.5, 5.85]
for x, (lab, val, err, stated, is_ctrl, study) in zip(xs, C_groups):
    col = COLORS["neutral_gray"] if is_ctrl else COLORS["SST"]
    axC.errorbar(x, val, yerr=err, fmt="o", ms=7, color=col, ecolor=col,
                 capsize=3.5, lw=1.1, elinewidth=1.1,
                 linestyle="none")
    if not stated:
        axC.plot([x, x], [val - err, val + err], color=col, lw=1.6, ls=(0, (2, 1.6)))
    axC.text(x, val + err + 1.0, f"{val}", fontsize=7.0, ha="center")
axC.axvline(3.6, color=COLORS["light_gray"], lw=0.8)
axC.set_xticks(xs)
axC.set_xticklabels([g[0] for g in C_groups], fontsize=6.2)
axC.set_xlim(-0.9, 6.7)
axC.set_ylim(0, 52)
axC.set_ylabel("CSF somatostatin (pg/mL)", fontsize=8.5)
axC.text(1.35, 51, "Atack 1988*\ndispersion type not stated\n(dashed bars)", fontsize=6.8,
         ha="center", va="top", color=COLORS["annotation"])
axC.text(5.15, 51, "Serby 1984*\nS.E.M.", fontsize=6.8, ha="center", va="top",
         color=COLORS["annotation"])
axC.text(0.0, -0.26, "EPS = extrapyramidal signs, not early onset", fontsize=6.6,
         color=COLORS["annotation"], transform=axC.transAxes)
head(axC, "C", "Absolute concentrations, pg/mL", fs=9.6,
     note="each group beside its own comparison group",
     ytitle=1.22, ynote=1.06)
tidy(axC)

# ---- D : absolute concentrations, fmol/ml
axD = fig.add_subplot(gs[2, 1])
xsD = [0, 1, 2]
for x, (lab, val, err, is_ctrl) in zip(xsD, D_groups):
    col = COLORS["neutral_gray"] if is_ctrl else COLORS["SST"]
    axD.errorbar(x, val, yerr=err, fmt="o", ms=7, color=col, ecolor=col,
                 capsize=3.5, lw=1.1, linestyle="none")
    axD.plot([x, x], [val - err, val + err], color=col, lw=1.6, ls=(0, (2, 1.6)))
    axD.text(x, val + err + 1.2, f"{val}", fontsize=7.0, ha="center")
axD.set_xticks(xsD)
axD.set_xticklabels([g[0] for g in D_groups], fontsize=6.2)
axD.set_xlim(-0.6, 2.6)
axD.set_ylim(0, 58)
axD.set_ylabel("CSF somatostatin (fmol/ml)", fontsize=8.5)
axD.text(-0.55, 57, "Strittmatter 1996* " + DAGGER + "; p < 0.01 for both\n"
                    "patient groups; error-term type not\nspecified (dashed bars)",
         fontsize=6.8, ha="left", va="top", color=COLORS["annotation"])
head(axD, "D", "Absolute concentrations, fmol/ml", fs=9.6,
     note="separate axis; no unit conversion",
     ytitle=1.22, ynote=1.06)
tidy(axD)

# ---- footer box
axF = fig.add_subplot(gs[3, :])
axF.axis("off")
axF.text(0.5, 0.75, "No retrieved study reports a sensitivity, a specificity, an area under the curve "
                    "or a cut-off for this measure.",
         fontsize=8.2, ha="center", va="center", transform=axF.transAxes,
         bbox=dict(boxstyle="round,pad=0.45", facecolor="#F2F2F2",
                   edgecolor=COLORS["neutral_gray"], linewidth=0.8))
axF.text(0.0, 0.02, "* denotes a value reported only in that paper's abstract. "
                    "The cerebrospinal fluid sampling site is not reported for any cohort in this figure.",
         fontsize=7.0, va="top", color=COLORS["annotation"], transform=axF.transAxes)

save_figure(fig, "../fig_sec9_csf_somatostatin_is_not_specific.png")

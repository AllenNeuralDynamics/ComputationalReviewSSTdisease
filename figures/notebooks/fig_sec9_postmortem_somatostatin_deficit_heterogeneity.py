"""Figure: the human postmortem somatostatin record (section 09).

Panels A-F are built strictly from the final figure plan for section_09.
Every printed numeral is verbatim from a cited source sentence; no value is
converted, rescaled, averaged or back-calculated. Rows reporting a result
without a number carry no axis position.
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else ".")

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from shared_style import COLORS, apply_style, save_figure

apply_style()

HET = "heterogeneous comparison \u2014 values not pooled"
RCOL = 104          # x position of the right-hand annotation column (data units)
XMAX = 205          # axis limit that makes room for that column

# ---------------------------------------------------------------- panel data
A_points = [
    ("Gaspar 1989* \u00b7 area 9",               80.0, "point", "SST-28-selective antibody"),
    ("Gaspar 1989* \u00b7 area 25",              60.0, "point", "SST-28-selective antibody"),
    ("Kumar 2005* \u00b7 'AD cortical region'",   70.0, "bound", "lower bound; SST and NPY pooled; isoform selectivity not stated"),
    ("Gonzalez-Rodriguez 2021 \u00b7 hippocampus", 50.0, "point", "isoform selectivity not stated"),
]
A_offaxis = [
    ("direction row", "Davies 1990*: significantly fewer SST-immunoreactive neurones, temporal layers II + III; no percentage"),
    ("reported null", "Nakamura 1986*: SST-immunoreactive cell density in neocortex did not decrease in SDAT vs aged normals"),
    ("reported null", "Li 1996*: no difference in the number of somatostatin neurons between the two study groups"),
    ("sparing, same study", "Gaspar 1989*: no significant reduction in the bed nucleus of the stria terminalis"),
    ("sparing, same study", "Gonzalez-Rodriguez 2021: somatostatin-expressing cells preserved in the olfactory bulb"),
]

B_points = [
    ("frontal cortex, grey matter",   41.0, False),
    ("frontal cortex, white matter",  66.0, False),
    ("hippocampus",                   44.0, False),
    ("parahippocampal, WHITE MATTER", 40.0, False),
    ("parahippocampal, overall",      59.0, True),
]

C_points = [("APOE E2/3\n(n = 19)", 0.71, 0.05), ("APOE E4\n(n = 13)", 0.42, 0.06)]

D_points = [
    ("Rossor 1980* \u00b7 temporal",            47.0, None,    "SDAT"),
    ("Reinikainen 1987* \u00b7 frontal",        42.0, None,    "Alzheimer's disease"),
    ("Reinikainen 1987* \u00b7 temporal",       28.0, None,    "Alzheimer's disease"),
    ("Reinikainen 1987* \u00b7 parietal",       42.0, None,    "Alzheimer's disease"),
    ("Beal 1986* \u00b7 frontal (BA6)",         40.0, "approx", "parkinsonian dementia (Alzheimer-type cortical pathology)"),
    ("Beal 1986* \u00b7 temporal (BA21)",       40.0, "approx", "parkinsonian dementia (Alzheimer-type cortical pathology)"),
    ("Kish 1993* \u00b7 parietal/occipital\nand frontal eye fields", (42.0, 58.0), "range", "olivopontocerebellar atrophy"),
]
D_offaxis = [
    ("reported null", "Epelbaum 1987*: in PSP, somatostatin concentrations not different from controls in any region tested"),
    ("sparing, same study", "Reinikainen 1987*: thalamus and putamen not reduced (stated in the same sentence)"),
    ("sparing, same study", "Kish 1993*: other cortical areas, including two temporal subdivisions, normal in OPCA"),
    ("sparing, same study", "Beal 1986*: non-demented parkinsonian donors had normal concentrations in every region"),
]

E_rows = [
    ("frontal cortex (Brodmann areas 6, 9, 10)\nand temporal cortex (Brodmann area 21)",
     "level\n(percent of control)", "\u201creduced to approximately\n50 percent of control values\u201d"),
    ("hippocampus", "reduction\n(percent change)", "\u201cA 40 percent reduction was\nseen in the hippocampus\u201d"),
    ("cingulate cortex, postcentral gyrus,\ntemporal pole, superior temporal gyrus",
     "reported null", "\u201cno significant changes\nwere found\u201d"),
]

F_point = ("Kish 1993* \u00b7 caudate nucleus", 46.0)

# ------------------------------------------------------------------- figure
fig = plt.figure(figsize=(7.1, 15.0))
gs = GridSpec(7, 2, figure=fig,
              height_ratios=[1.10, 0.95, 1.05, 1.75, 0.80, 1.10, 0.55],
              hspace=1.35, wspace=0.55)


def tidy(ax, xbound=None):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    if xbound is not None:
        ax.spines["bottom"].set_bounds(*xbound)


def head(ax, letter, title, note=None, fs=10.2, ytitle=1.22, ynote=1.05):
    ax.text(0.0, ytitle, f"{letter}   {title}", transform=ax.transAxes,
            fontsize=fs, fontweight="bold", va="bottom")
    if note:
        ax.text(0.0, ynote, note, transform=ax.transAxes, fontsize=7.4,
                style="italic", va="bottom", color=COLORS["annotation"])


def textblock(ax, rows, title):
    ax.axis("off")
    ax.text(0.0, 1.0, title, transform=ax.transAxes, fontsize=7.8,
            style="italic", va="bottom", color=COLORS["annotation"])
    n = len(rows)
    for i, (tag, bodytxt) in enumerate(rows):
        y = 1.0 - (i + 0.7) / n
        c = COLORS["decrease"] if tag == "direction row" else COLORS["no_change"]
        ax.plot(0.008, y, marker="s", ms=5, color=c, transform=ax.transAxes, clip_on=False)
        ax.text(0.030, y, tag, transform=ax.transAxes, fontsize=7.0, va="center",
                fontweight="bold", color=COLORS["annotation"])
        ax.text(0.300, y, bodytxt, transform=ax.transAxes, fontsize=7.0, va="center")


# ---- A
axA = fig.add_subplot(gs[0, :])
ysA = list(range(len(A_points)))[::-1]
for y, (lab, val, kind, note) in zip(ysA, A_points):
    if kind == "bound":
        axA.plot(val, y, marker="o", ms=8, color=COLORS["decrease"], zorder=3)
        axA.annotate("", xy=(val + 20, y), xytext=(val, y),
                     arrowprops=dict(arrowstyle="-|>", color=COLORS["decrease"], lw=1.3))
    else:
        axA.plot(val, y, marker="o", ms=8, color=COLORS["decrease"], zorder=3)
    axA.text(RCOL, y, note, fontsize=7.0, va="center", color=COLORS["annotation"])
axA.set_yticks(ysA)
axA.set_yticklabels([p[0] for p in A_points], fontsize=7.6)
axA.set_ylim(-0.7, len(A_points) - 0.3)
axA.set_xlim(0, XMAX)
axA.set_xticks([0, 20, 40, 60, 80, 100])
axA.set_xlabel("reported reduction in somatostatin-immunoreactive somata (%)", fontsize=9)
head(axA, "A", "Immunoreactive somata: reported percent reductions", HET)
tidy(axA, (0, 100))

# ---- A off-axis
axAo = fig.add_subplot(gs[1, :])
textblock(axAo, A_offaxis,
          "no axis position \u2014 reported nulls, a direction without a percentage, and within-study sparing")

# ---- B
axB = fig.add_subplot(gs[2, 0])
ysB = list(range(len(B_points)))[::-1]
for y, (lab, val, sig) in zip(ysB, B_points):
    axB.plot(val, y, marker="o", ms=7.5, zorder=3,
             color=COLORS["decrease"] if sig else "white",
             mec=COLORS["decrease"], mew=1.3)
    if sig:
        axB.text(val + 3, y, "P < 0.05", fontsize=7.0, va="center", color=COLORS["annotation"])
axB.set_yticks(ysB)
axB.set_yticklabels([p[0] for p in B_points], fontsize=7.2)
axB.set_ylim(-0.7, len(B_points) - 0.3)
axB.set_xlim(0, 88)
axB.set_xticks([0, 20, 40, 60, 80])
axB.set_xlabel("reduction in somatostatin mRNA-\ncontaining cell density (%)", fontsize=8.5)
head(axB, "B", "Transcript-containing cells", fs=9.6,
     note="six brains; filled = significant, open = not",
     ytitle=1.30, ynote=1.08)
tidy(axB, (0, 80))

# ---- C
axC = fig.add_subplot(gs[2, 1])
for x, (lab, val, sem) in zip([0, 1], C_points):
    axC.errorbar(x, val, yerr=sem, fmt="o", ms=8, color=COLORS["SST"],
                 ecolor=COLORS["SST"], capsize=4, lw=1.2)
    axC.text(x + 0.10, val, f"{val:.2f} \u00b1 {sem:.2f}", fontsize=7.4, va="center")
axC.set_xticks([0, 1])
axC.set_xticklabels([p[0] for p in C_points], fontsize=7.6)
axC.set_xlim(-0.5, 1.7)
axC.set_ylim(0, 0.9)
axC.set_ylabel("somatostatin\n(ng/mg wet weight)", fontsize=8.5)
head(axC, "C", "Genotype contrast within patients", fs=9.6,
     note="one study, P < 0.001; error bars SEM, as stated by the source",
     ytitle=1.30, ynote=1.08)
tidy(axC)

# ---- D
axD = fig.add_subplot(gs[3, :])
ysD = list(range(len(D_points)))[::-1]
for y, (lab, val, kind, diag) in zip(ysD, D_points):
    if kind == "range":
        lo, hi = val
        axD.plot([lo, hi], [y, y], color=COLORS["decrease"], lw=3.2,
                 solid_capstyle="butt", zorder=2)
        axD.plot([lo, hi], [y, y], ls="none", marker="|", ms=10,
                 color=COLORS["decrease"], zorder=3)
        axD.text(hi + 3, y, "range", fontsize=7.0, va="center",
                 color=COLORS["annotation"])
    else:
        axD.plot(val, y, marker="o", ms=8, color=COLORS["decrease"], zorder=3)
        if kind == "approx":
            axD.text(val - 3.5, y, "\u2248", fontsize=10, va="center", ha="right",
                     color=COLORS["decrease"])
    axD.text(RCOL, y, diag, fontsize=7.0, va="center", color=COLORS["annotation"])
axD.set_yticks(ysD)
axD.set_yticklabels([p[0] for p in D_points], fontsize=7.2)
axD.set_ylim(-0.7, len(D_points) - 0.3)
axD.set_xlim(0, XMAX)
axD.set_xticks([0, 20, 40, 60, 80, 100])
axD.set_xlabel("reported reduction in bulk tissue somatostatin-like immunoreactivity (%)", fontsize=9)
head(axD, "D", "Bulk tissue peptide (radioimmunoassay): reported reductions only",
     HET + "; \u2248 marks the value reported as \u2018approximately 40%\u2019; no study in this panel reports an error term")
tidy(axD, (0, 100))

# ---- D off-axis
axDo = fig.add_subplot(gs[4, :])
textblock(axDo, D_offaxis, "no axis position \u2014 the reported null and within-study regional sparing")

# ---- E
axE = fig.add_subplot(gs[5, :])
axE.axis("off")
axE.text(0.0, 1.00, "E   Somatostatin receptor binding: statement rows, not a numeric axis",
         transform=axE.transAxes, fontsize=10.2, fontweight="bold", va="bottom")
axE.text(0.0, 0.88, "a level and a reduction cannot share a scale, and the paper reports no converted value",
         transform=axE.transAxes, fontsize=7.4, style="italic", va="bottom",
         color=COLORS["annotation"])
for i, (region, qclass, statement) in enumerate(E_rows):
    y = 0.66 - i * 0.33
    c = COLORS["no_change"] if qclass == "reported null" else COLORS["decrease"]
    axE.plot(0.008, y, marker="s", ms=5, color=c, transform=axE.transAxes, clip_on=False)
    axE.text(0.030, y, region, fontsize=7.2, va="center", transform=axE.transAxes)
    axE.text(0.420, y, qclass, fontsize=7.2, va="center", style="italic",
             transform=axE.transAxes, color=COLORS["annotation"])
    axE.text(0.620, y, statement, fontsize=7.2, va="center", transform=axE.transAxes)

# ---- F
axF = fig.add_subplot(gs[6, :])
lab, val = F_point
axF.plot(val, 0, marker="o", ms=8, color=COLORS["increase"], zorder=3)
axF.text(RCOL, 0, "significantly elevated by 46%; r = -0.66 with choline-acetyltransferase activities\n"
                  "in the same material, where the cholinergic deficit in that region was -81%",
         fontsize=7.0, va="center", color=COLORS["annotation"])
axF.set_yticks([0])
axF.set_yticklabels([lab], fontsize=7.2)
axF.set_ylim(-0.8, 0.8)
axF.set_xlim(0, XMAX)
axF.set_xticks([0, 20, 40, 60, 80, 100])
axF.set_xlabel("reported elevation relative to control (%)", fontsize=9)
head(axF, "F", "The one reported increase, on its own axis",
     "same nine donors as this study's reduction row in panel D \u2014 one study, not two",
     ytitle=1.95, ynote=1.45)
tidy(axF, (0, 100))

fig.text(0.0, 0.004, "* denotes a value reported only in that paper's abstract.",
         fontsize=7.2, color=COLORS["annotation"])

save_figure(fig, "../fig_sec9_postmortem_somatostatin_deficit_heterogeneity.png")

"""Figure: single-nucleus and deconvolution evidence for somatostatin neuron
depletion in Alzheimer's disease (section 09).

Built strictly from the final figure plan for section_09. The panel is a table
of verbatim statistics with direction as the only graphical encoding; there is
no numeric axis anywhere. The direction glyph is applied only to rows whose own
source sentence names somatostatin.
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else ".")

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from shared_style import COLORS, apply_style, save_figure

apply_style()

GLYPH = {"down": ("\u25bc", COLORS["decrease"]),
         "none": ("\u25cb", COLORS["no_change"]),
         "open": ("\u25cb", COLORS["neutral_gray"])}

# study, region, cell-type label, cohort size, pathology axis, statistic, direction
ROWS = [
    ("Mathys 2023", "dorsolateral\nprefrontal cortex", "SST subclass and its\nthree vulnerable subtypes",
     "427 individuals;\n2.3 million cells", "level of AD\npathology",
     "quasi-binomial regression;\nno magnitude reported", "down"),
    ("Cain 2023", "frontal cortex", "deconvolution-inferred\nsomatostatin subset",
     "638 bulk-profiled;\n24-donor reference", "Alzheimer's\ndisease status",
     "no statistic in the\nsource sentence", "down"),
    ("Cain 2023\n(protein)", "frontal cortex", "SST protein, bulk tissue\n(not cell-resolved)",
     "638 bulk-profiled;\n24-donor reference", "amyloid burden", "P < 0.01", "down"),
    ("Mathys 2024", "six brain regions", "inhibitory subtypes;\nsomatostatin NOT specified",
     "48 individuals;\n1.3 million cells", "tangle density",
     "Benjamini-Hochberg-\nadjusted P < 0.05\n(vulnerability threshold)", "open"),
    ("Gabitto 2024", "middle temporal\ngyrus", "superficial Sst\nsupertypes", "84 donors",
     "continuous pseudo-\nprogression score", "lost during the early\nepoch; no magnitude", "down"),
    ("Joshi 2024", "middle temporal\ngyrus", "Sst neuron number",
     "no donor count;\ndf in donor-by-type units", "categorical AD\nstage groups",
     "F(3,81) = 4.381,\np = 0.0066", "down"),
    ("Joshi 2024\n(same data)", "middle temporal\ngyrus", "Sst proportion", "same donors",
     "same grouping", "t(6) = 1.333,\np = 0.2309", "none"),
]

RESTRICTED = [
    ("Mathys 2023", "dorsolateral prefrontal cortex; SST subclass and subtypes",
     "quasi-binomial regression", "down"),
    ("Gabitto 2024", "middle temporal gyrus; superficial Sst supertypes",
     "snRNA-seq and spatial transcriptomics", "down"),
]

COLS = [0.00, 0.150, 0.290, 0.510, 0.670, 0.808]
GLYPH_X = 0.113
HDR = ["study", "region", "cell-type label", "cohort size and\nwhat n counts",
       "pathology axis", "reported statistic"]

fig = plt.figure(figsize=(7.1, 8.2))
gs = GridSpec(2, 1, figure=fig, height_ratios=[2.55, 0.70], hspace=0.50)

# ------------------------------------------------------------------ main
ax = fig.add_subplot(gs[0])
ax.axis("off")
ax.text(0.0, 1.06, "What each cohort actually reports about somatostatin neurons in Alzheimer's disease",
        fontsize=10.2, fontweight="bold", va="bottom", transform=ax.transAxes)
ax.text(0.0, 1.005, "table of verbatim statistics \u2014 no numeric axis; the direction glyph is used only on rows "
        "whose own source sentence names somatostatin",
        fontsize=7.2, style="italic", va="bottom", color=COLORS["annotation"], transform=ax.transAxes)

for x, h in zip(COLS, HDR):
    ax.text(x, 0.955, h, fontsize=7.0, fontweight="bold", va="top",
            color=COLORS["annotation"], transform=ax.transAxes)
ax.plot([0.0, 1.0], [0.905, 0.905], color=COLORS["light_gray"], lw=0.8,
        transform=ax.transAxes, clip_on=False)

y0, dy = 0.835, 0.125
for i, row in enumerate(ROWS):
    y = y0 - i * dy
    for x, cell in zip(COLS, row[:6]):
        ax.text(x, y, cell, fontsize=6.5, va="center", transform=ax.transAxes)
    g, c = GLYPH[row[6]]
    ax.text(GLYPH_X, y, g, fontsize=9, va="center", color=c, transform=ax.transAxes)
    if i < len(ROWS) - 1:
        ax.plot([0.0, 1.0], [y - dy / 2, y - dy / 2], color="#EEEEEE", lw=0.6,
                transform=ax.transAxes, clip_on=False)

# shared-cohort bracket over the first four rows
top, bot = y0 + 0.045, y0 - 3 * dy - 0.045
bx = -0.035
ax.plot([bx, bx], [top, bot], color=COLORS["bracket"], lw=1.4,
        transform=ax.transAxes, clip_on=False)
for yy in (top, bot):
    ax.plot([bx, bx + 0.012], [yy, yy], color=COLORS["bracket"], lw=1.4,
            transform=ax.transAxes, clip_on=False)
ax.text(bx - 0.012, (top + bot) / 2, "not independent", rotation=90, va="center",
        ha="center", fontsize=6.8, color=COLORS["bracket"], transform=ax.transAxes)

ax.text(0.0, y0 - 6 * dy - 0.075,
        "Bracket: the prefrontal atlas and the deconvolution study draw on the same parent study population, and the later\n"
        "study describes its result as consistent with the earlier one from the same research group, so the agreement of these\n"
        "rows is not independent replication. The two somatostatin rows that fall outside this lineage are shown again below.",
        fontsize=6.8, va="top", color=COLORS["annotation"], transform=ax.transAxes)

# -------------------------------------------------------------- restricted
ax2 = fig.add_subplot(gs[1])
ax2.axis("off")
ax2.text(0.0, 1.02, "Compositional tests on the two cohorts outside that lineage",
         fontsize=10.2, fontweight="bold", va="bottom", transform=ax2.transAxes)
ax2.text(0.0, 0.90, "direction and the named statistical model only \u2014 neither study reports an effect magnitude for this comparison",
         fontsize=7.2, style="italic", va="bottom", color=COLORS["annotation"], transform=ax2.transAxes)
for i, (study, scope, model, direction) in enumerate(RESTRICTED):
    y = 0.62 - i * 0.30
    g, c = GLYPH[direction]
    ax2.text(0.0, y, study, fontsize=7.2, va="center", transform=ax2.transAxes)
    ax2.text(0.145, y, g, fontsize=9, va="center", color=c, transform=ax2.transAxes)
    ax2.text(0.185, y, scope, fontsize=7.0, va="center", transform=ax2.transAxes)
    ax2.text(0.700, y, model, fontsize=7.0, va="center", color=COLORS["annotation"],
             transform=ax2.transAxes)
ax2.text(0.0, 0.02, "Regions, cell-type resolutions and pathology axes differ between the two rows, so they agree on direction, "
         "not on which cells.", fontsize=6.8, va="top", color=COLORS["annotation"], transform=ax2.transAxes)

save_figure(fig, "../fig_sec9_single_nucleus_cohort_convergence.png")

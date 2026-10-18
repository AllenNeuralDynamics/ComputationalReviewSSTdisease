
import os, sys
if os.path.basename(os.getcwd()) == "notebooks":
    os.chdir(os.path.join("..", ".."))
sys.path.insert(0, os.path.join("figures", "notebooks"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D
from shared_style import COLORS, apply_style, save_figure

apply_style()
plt.rcParams.update({"font.size": 10, "legend.fontsize": 9})  # figure authored at the 10 pt document size

# ======================================================================= panel A
# Matrix. Row order is fixed so that the Hayashi et al. 1997 block is contiguous.
rows = ["hippocampus", "frontal cortex", "temporal cortex", "motor cortex",
        "somatosensory cortex", "visual cortex", "parietal cortex", "striatum",
        "cortex (not subdivided in source)", "hypothalamus"]
cols = ["Hayashi et al. 1997\nmacaque (2, 10, >30 y)\nSRIF mRNA/G3PDH ratio\nreported as a decrease",
        "Sonntag et al. 1990\nFischer 344 rat (3-4 vs 22 mo)\nsomatostatin mRNA/poly A+ RNA\nreported as % of young levels",
        "Florio et al. 1991\nrat (25 months)\npre-prosomatostatin mRNA\nreported as percent change"]

NOT_MEASURED, NO_CHANGE, REPORTED = "not_measured", "no_change", "reported"
cells = {}
for r in rows:
    for c in range(3):
        cells[(r, c)] = (NOT_MEASURED, "not reported")
# Hayashi: one merged cell over the six regions named in the source sentence.
hayashi_rows = rows[0:6]
# Sonntag
cells[("cortex (not subdivided in source)", 1)] = (NO_CHANGE, "measured,\nno significant change")
cells[("hypothalamus", 1)] = (REPORTED, "approximately 50%\nof young levels")
# Florio
cells[("frontal cortex", 2)] = (REPORTED, "-49%")
cells[("parietal cortex", 2)] = (REPORTED, "-80%")
cells[("striatum", 2)] = (REPORTED, "-69%")
cells[("hypothalamus", 2)] = (NO_CHANGE, "measured,\nno significant change")

FILL = {NOT_MEASURED: "#FFFFFF", NO_CHANGE: COLORS["no_change"], REPORTED: "#C6DBEF"}

fig = plt.figure(figsize=(7.4, 14.6))
gs = fig.add_gridspec(3, 1, height_ratios=[1.25, 1.45, 0.80], hspace=0.70)
axA = fig.add_subplot(gs[0])
gsB = gs[1].subgridspec(3, 1, hspace=1.95)
gsC = gs[2].subgridspec(1, 2, wspace=0.55)

nr, nc = len(rows), len(cols)
for i, r in enumerate(rows):
    y = nr - 1 - i
    for c in range(nc):
        if c == 0 and r in hayashi_rows:
            continue
        kind, text = cells[(r, c)]
        axA.add_patch(Rectangle((c, y), 1, 1, facecolor=FILL[kind],
                                edgecolor=COLORS["neutral_gray"], lw=0.7))
        axA.text(c + 0.5, y + 0.5, text, ha="center", va="center", fontsize=7.5,
                 color="black" if kind != NOT_MEASURED else COLORS["neutral_gray"])
# merged Hayashi cell
y_top = nr - 1 - rows.index(hayashi_rows[0]) + 1
y_bot = nr - 1 - rows.index(hayashi_rows[-1])
axA.add_patch(Rectangle((0, y_bot), 1, y_top - y_bot, facecolor="#C6DBEF",
                        edgecolor=COLORS["neutral_gray"], lw=0.7))
axA.text(0.5, (y_top + y_bot) / 2,
         "60-70% decrease\n\none interval reported jointly for\nthese six regions; printed once,\n"
         "not resolved into per-region values",
         ha="center", va="center", fontsize=7.5)

axA.set_xlim(0, nc)
axA.set_ylim(0, nr)
axA.set_xticks([c + 0.5 for c in range(nc)])
axA.set_xticklabels(cols, fontsize=7.5)
axA.xaxis.set_ticks_position("top")
axA.xaxis.set_label_position("top")
axA.set_yticks([nr - 0.5 - i for i in range(nr)])
axA.set_yticklabels(rows, fontsize=8)
axA.tick_params(length=0)
for s in axA.spines.values():
    s.set_visible(False)
axA.set_title("a   Region-resolved age-related change in somatostatin transcript\n"
              "heterogeneous comparison \u2014 values not pooled; each cell prints the quantity in its "
              "source's own convention",
              loc="left", fontsize=10.5, fontweight="bold", pad=52)
legend_handles = [Rectangle((0, 0), 1, 1, facecolor="#C6DBEF", edgecolor=COLORS["neutral_gray"],
                            label="reported change"),
                  Rectangle((0, 0), 1, 1, facecolor=COLORS["no_change"],
                            edgecolor=COLORS["neutral_gray"], label="measured, no significant change"),
                  Rectangle((0, 0), 1, 1, facecolor="#FFFFFF", edgecolor=COLORS["neutral_gray"],
                            label="not among the regions that study reports")]
axA.legend(handles=legend_handles, loc="upper left", bbox_to_anchor=(0.0, -0.02),
           ncol=3, frameon=False, fontsize=8)

# ======================================================================= panel B
panelB = [
    dict(value_text="-42.4%",
         axis_label="percent change in somatostatin expression (BA9)\npeptide, measured by radioimmunoassay",
         xlabel="CDR 5 versus lower CDR (within one cohort;\nnot AD versus non-demented control)",
         cohort="171 subjects with and without AD at different levels of\ncognitive impairment; per-stratum n not reported",
         note="that study concludes the BA9 synaptic-marker changes are\na late event only weakly related to AD dementia",
         title="b1   Poirel et al. 2018 \u2014 prefrontal cortex BA9"),
    dict(value_text="10-fold\ndownregulation",
         axis_label="linear fold-change in somatostatin protein\nabundance (frontal cortex)",
         xlabel="AD versus age-matched control\n(frontal cortex proteome)",
         cohort="discovery proteomic cohort size not stated by that study",
         note="discovery-stage tandem-mass-tag estimate; somatostatin was not\namong that study's validated targets",
         title="b2   Sathe et al. 2020 \u2014 frontal cortex"),
    dict(value_text="log FC = -2.2\n(base not stated\nin source)",
         axis_label="log fold-change in SST RNA-seq counts (precuneus)",
         xlabel="AD versus control, precuneus\n(moderately affected region)",
         cohort="ten age-, gender- and RNA quality-matched post-mortem brains",
         note=("downregulation reported for the precuneus; that study reports\n"
               "no somatostatin result for primary visual cortex, so no null there is implied"),
         title="b3   Guennewig et al. 2021 \u2014 precuneus"),
]

for k, spec in enumerate(panelB):
    ax = fig.add_subplot(gsB[k])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    if k == 0:
        ax.text(0.0, 2.05,
                "b   Direction of cortical somatostatin depletion in Alzheimer disease,\n"
                "reported separately by assay, region and comparator",
                fontsize=10.5, fontweight="bold", va="bottom")
        ax.text(0.0, 1.60,
                "Each sub-panel has its own scale and its own comparator; the shared element is the "
                "direction of effect, which is\ndownward in all three. Magnitudes are not comparable "
                "across sub-panels and no conversion was applied.",
                fontsize=7.5, style="italic", va="bottom")
    ax.text(0.0, 1.14, spec["title"], fontsize=10, fontweight="bold", va="bottom")
    ax.annotate("", xy=(0.045, 0.28), xytext=(0.045, 0.92),
                arrowprops=dict(arrowstyle="-|>", color=COLORS["decrease"], lw=2.4))
    ax.text(0.09, 0.60, spec["value_text"], fontsize=11, fontweight="bold",
            va="center", color=COLORS["decrease"])
    ax.text(0.42, 1.02,
            spec["axis_label"] + "\n" + spec["xlabel"] + "\n" + spec["cohort"]
            + "\n" + spec["note"],
            fontsize=7.2, va="top", linespacing=1.75)

# ======================================================================= panel C
panelC = [
    dict(title="c1   Atack et al. 1988\nAlzheimer-type dementia",
         groups=[("age-matched\ncontrol (n = 26)", 23.1, 8.2),
                 ("DAT\n(n = 27)", 17.5, 5.0),
                 ("DAT with extrapyramidal\nsigns (seven patients)", 16.4, 5.0)],
         note="reduction was unrelated to dementia severity and did not\nchange significantly during disease progression",
         ymax=36),
    dict(title="c2   Dupont et al. 1982\nParkinson disease",
         groups=[("controls\n(n not reported)", 147.3, 5.1),
                 ("parkinsonian patients\n(n = 39)", 88.0, 4.1)],
         note="about 40% less than in controls, as reported; values were not\nrelated to duration of disease, severity, specific signs, or treatment",
         ymax=175),
]

for k, spec in enumerate(panelC):
    ax = fig.add_subplot(gsC[k])
    xs = range(len(spec["groups"]))
    for x, (lab, mean, err) in zip(xs, spec["groups"]):
        ax.errorbar(x, mean, yerr=err, fmt="D", ms=8, markerfacecolor="white",
                    markeredgecolor=COLORS["SST"], markeredgewidth=1.6,
                    ecolor="black", elinewidth=1.0, capsize=4)
        ax.annotate("%s +/- %s" % (mean, err), (x, mean + err), textcoords="offset points",
                    xytext=(0, 7), ha="center", fontsize=7.5)
    ax.set_xticks(list(xs))
    ax.set_xticklabels([g[0] for g in spec["groups"]], fontsize=7, rotation=20, ha="right")
    ax.set_xlim(-0.6, len(spec["groups"]) - 0.4)
    ax.set_ylim(0, spec["ymax"])
    ax.set_ylabel("CSF somatostatin (pg/mL)\nmean +/- error term as reported\n(type not stated by that study)",
                  fontsize=8)
    ax.set_title(spec["title"], loc="left", fontsize=9.5, fontweight="bold", pad=10)
    ax.annotate(spec["note"], (0.0, -0.72), xycoords="axes fraction", fontsize=7, va="top")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

fig.text(0.01, -0.012,
         "Each study is shown against its own control group on its own axis; absolute concentrations are not "
         "comparable across the two studies\nand no ratio between them is computed. Open diamonds mark values "
         "extracted from an abstract only.",
         fontsize=7.5, style="italic")

save_figure(fig, "figures/fig_sec3_marker_level_readouts_transcript_peptide_csf.png")
print("saved")

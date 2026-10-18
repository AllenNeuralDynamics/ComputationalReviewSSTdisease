
import os, sys
if os.path.basename(os.getcwd()) == "notebooks":
    os.chdir(os.path.join("..", ".."))
sys.path.insert(0, os.path.join("figures", "notebooks"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from shared_style import COLORS, apply_style, save_figure

apply_style()

# Every numeric token below is verbatim from the quoted source sentence of its study.
panelA = [
    dict(label=("Johansen et al. 1987 \u2014 rat, dentate hilus + CA3c,\n"
                "transient forebrain ischaemia; quantitated at day 1, 2, 3 and 4,\n"
                "interval not assigned to a single day (n not reported)"),
         kind="interval", lo=60, hi=80, access="abstract_only"),
    dict(label="", kind="spacer"),
    dict(label=("Matsuyama et al. 1993 \u2014 gerbil, dentate hilus,\n"
                "2 min ischaemia, 1 day (n not reported)"),
         kind="point", value=40, access="abstract_only"),
    dict(label=("Matsuyama et al. 1993 \u2014 gerbil, dentate hilus,\n"
                "2 min ischaemia, 7 days (n not reported)"),
         kind="point", value=60, access="abstract_only"),
]

panelB = [
    dict(label=("Komitova et al. 2013 \u2014 mouse, cortical interneurons\n"
                "(subregion not stated in the source), hypoxic rearing\n"
                "9.5-10.5% O2 P3-P11, assessed P15 (n not reported)"),
         value=-32, access="abstract_only",
         note=("marker expression, juvenile timepoint: same study reports no change in\n"
               "total GAD67-EGFP+ cell number and no evidence of increased interneuron\n"
               "death, and that enrichment from P21 normalized the marker deficit")),
    dict(label=("Lacaille et al. 2019 \u2014 mouse, prefrontal cortex upper layers,\n"
                "maternal immune activation + chronic sublethal hypoxia,\n"
                "adult (n not reported)"),
         value=-32, access="fulltext",
         note=("adult, persistent loss reproduced only by the\n"
               "combined insult, not by either insult alone")),
]

panelC = dict(label=("Hencz et al. 2023 \u2014 rat, dentate hilus,\n16% O2 for 1 h\n"
                     "(n = 10 as reported; unit not stated in source)"),
              value=23.57, sem=8.8, access="fulltext")


def face(access):
    return "white" if access == "abstract_only" else COLORS["SST"]


fig = plt.figure(figsize=(7.4, 10.4))
gs = fig.add_gridspec(3, 1, height_ratios=[1.2, 1.0, 0.7], hspace=1.05)
axA, axB, axC = (fig.add_subplot(gs[i]) for i in range(3))

# ------------------------------------------------------------------- panel A
ypos, labels = [], []
y = len(panelA)
for row in panelA:
    y -= 1
    ypos.append(y)
    labels.append(row["label"])
    if row["kind"] == "interval":
        axA.plot([row["lo"], row["hi"]], [y, y], color=COLORS["SST"], lw=2.5,
                 solid_capstyle="butt", zorder=2)
        for x in (row["lo"], row["hi"]):
            axA.plot([x, x], [y - 0.14, y + 0.14], color=COLORS["SST"], lw=2.0, zorder=2)
        axA.annotate("60%-80% as reported\n(range; no point estimate stated)",
                     (row["hi"], y), textcoords="offset points", xytext=(8, 0),
                     va="center", fontsize=8)
    elif row["kind"] == "point":
        axA.plot(row["value"], y, "o", ms=9, markerfacecolor=face(row["access"]),
                 markeredgecolor=COLORS["SST"], markeredgewidth=1.6, zorder=3)
        axA.annotate("%d%%" % row["value"], (row["value"], y), textcoords="offset points",
                     xytext=(0, 11), ha="center", fontsize=8)

axA.set_yticks(ypos)
axA.set_yticklabels(labels, fontsize=7.5)
axA.set_xlim(0, 100)
axA.set_ylim(-0.9, len(panelA) - 0.4)
axA.set_xlabel("loss of somatostatin-immunoreactive neurons relative to control (%)")
axA.set_title("a   Acute transient ischaemia \u2014 dentate hilus / CA3c\n"
              "heterogeneous comparison \u2014 values not pooled; row order is not a time course",
              loc="left", fontsize=10.5, fontweight="bold", pad=10)
axA.annotate(("Repeated 2-min periods of ischemia, which induced ischemic tolerance by vulnerable CA1\n"
              "neurons, caused almost complete loss of hilar SS neurons \u2014 no percentage is reported\n"
              "for that regime; annotated, not plotted."),
             (0.0, -0.33), xycoords="axes fraction", fontsize=7.5, va="top")

# ------------------------------------------------------------------- panel B
ypos, labels = [], []
y = len(panelB)
for row in panelB:
    y -= 1
    ypos.append(y)
    labels.append(row["label"])
    axB.plot(row["value"], y, "o", ms=9, markerfacecolor=face(row["access"]),
             markeredgecolor=COLORS["SST"], markeredgewidth=1.6, zorder=3)
    axB.annotate("-32%", (row["value"], y), textcoords="offset points", xytext=(0, 11),
                 ha="center", fontsize=8)
    axB.annotate(row["note"], (row["value"], y), textcoords="offset points",
                 xytext=(12, -2), va="center", fontsize=7)

axB.set_yticks(ypos)
axB.set_yticklabels(labels, fontsize=7.5)
axB.set_xlim(-42, 4)
axB.set_ylim(-0.7, len(panelB) - 0.3)
axB.axvline(0, color=COLORS["light_gray"], lw=0.8)
axB.set_xlabel("change in number or density of somatostatin-marker-positive\n"
               "cortical interneurons versus control (%)  [not a cell-loss axis]")
axB.set_title("b   Perinatal insult \u2014 cortex (own axis; not comparable to panel a)\n"
              "heterogeneous comparison \u2014 values not pooled; the two rows print the same figure\n"
              "for two different quantities measured in different ways",
              loc="left", fontsize=10.5, fontweight="bold", pad=10)

# ------------------------------------------------------------------- panel C
axC.errorbar(panelC["value"], 0, xerr=panelC["sem"], fmt="o", ms=9,
             markerfacecolor=COLORS["SST"], markeredgecolor=COLORS["SST"],
             markeredgewidth=1.6, ecolor="black", elinewidth=1.0, capsize=4)
axC.annotate("23.57%  (SEM = 8.8, n = 10 as reported)", (panelC["value"], 0),
             textcoords="offset points", xytext=(0, 14), ha="center", fontsize=8)
axC.annotate("no control (21% O2) proportion is reported; no control point is drawn",
             (0.02, 0.08), xycoords="axes fraction", fontsize=7.5)
axC.set_yticks([0])
axC.set_yticklabels([panelC["label"]], fontsize=7.5)
axC.set_xlim(0, 60)
axC.set_ylim(-0.7, 0.9)
axC.set_xlabel("share of silver-impregnated ('dark') neurons that were\n"
               "somatostatin-immunoreactive (%) \u2014 denominator is injured neurons,\n"
               "not control SST+ neurons")
axC.set_title("c   Mild short-term hypoxia \u2014 single study, separate denominator",
              loc="left", fontsize=10.5, fontweight="bold", pad=10)

for ax in (axA, axB, axC):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(axis="y", length=0)

handles = [Line2D([], [], marker="o", linestyle="none", ms=8, markerfacecolor="white",
                  markeredgecolor=COLORS["SST"], markeredgewidth=1.6,
                  label="value extracted from abstract only"),
           Line2D([], [], marker="o", linestyle="none", ms=8,
                  markerfacecolor=COLORS["SST"], markeredgecolor=COLORS["SST"],
                  markeredgewidth=1.6, label="value extracted from full text")]
axA.legend(handles=handles, loc="lower left", frameon=False, fontsize=8)

fig.text(0.01, 0.005,
         "Marker-based counts cannot distinguish loss of somatostatin immunoreactivity from loss of the neuron.",
         fontsize=7.5)

save_figure(fig, "figures/fig_sec3_sst_depletion_across_insults.png")
print("saved")

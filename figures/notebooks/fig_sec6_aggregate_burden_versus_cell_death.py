"""Figure: aggregate burden, somatic CAG expansion and reported cell loss by class.

A qualitative table with NO magnitude axis: aggregate prevalence, somatic repeat
expansion and cell loss are different quantities and are never placed on a shared
axis. Blank cells mean "not measured", never zero. Rows derived from an unrefereed
preprint are hatched and labelled in the table body itself.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from shared_style import COLORS, apply_style, save_figure

apply_style()
plt.rcParams["hatch.color"] = "#B0B0B0"
plt.rcParams["hatch.linewidth"] = 0.5
HERE = os.path.dirname(os.path.abspath(__file__))

HEADERS = ["Cell class", "Aggregate\nburden", "Somatic CAG\nexpansion",
           "Reported\nloss", "Quantity measured and source"]

ROWS = [
    dict(cls="Cortical NADPH-d\ninterneurons (human)",
         agg="multiple perikaryal\naggregates in\nalmost all", exp="", loss="",
         src="aggregate prevalence,\nearly grade HD cases\n(case count not stated)\nKuemmerle 1999, abstract only",
         preprint=False),
    dict(cls="Striatal \"spared\"\nNADPH-d interneurons\n(human)",
         agg="approximately 50%\nof the spared\nstriatal neurons", exp="",
         loss="termed \"spared\"\nin the source",
         src="aggregate prevalence,\nearly grade HD cases\n(case count not stated)\nKuemmerle 1999, abstract only",
         preprint=False),
    dict(cls="Cortical chandelier\nand somatostatin+\ninterneurons",
         agg="only modest\naggregation", exp="only modest\nrepeat expansion",
         loss="lost\n(direction only,\nunquantified)",
         src="spatial transcriptomics;\n428,173 cells imaged for\ncell-type vulnerability\nVazquez-Sanchez 2025\nPREPRINT, NOT PEER REVIEWED",
         preprint=True),
    dict(cls="L5-6 NP and L6b\ndeep-layer EXCITATORY\nneurons (not interneurons)",
         agg="", exp="very large\n(>380 $\\pm$ 55)\nsomatic expansions", loss=">50% loss",
         src="within-study contrast;\nexpansion and aggregation\nmeasured in 185,721 cells\nVazquez-Sanchez 2025\nPREPRINT, NOT PEER REVIEWED",
         preprint=True),
]

COLX = [0.000, 0.260, 0.430, 0.600, 0.740]
COLW = [0.260, 0.170, 0.170, 0.140, 0.260]
ROWH = [0.170, 0.180, 0.200, 0.200]
FS = 6.6

fig, ax = plt.subplots(figsize=(7.2, 6.0))
fig.subplots_adjust(left=0.02, right=0.99, top=0.99, bottom=0.01)
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")

ax.text(0.0, 0.998, "Aggregate load, somatic CAG expansion and reported cell loss are different "
                    "quantities —\nno magnitude axis and no shared scale",
        fontsize=8.3, color=COLORS["conflict_marker"], va="top")
ax.text(0.0, 0.915, "Blank cell = that study made no such measurement (never zero). Hatched rows "
                    "come from an unrefereed preprint and are provisional.",
        fontsize=7.2, color="#444444", va="bottom")

ytop = 0.845
for x, w, c in zip(COLX, COLW, HEADERS):
    ax.add_patch(Rectangle((x, ytop), w, 0.062, facecolor=COLORS["light_gray"],
                           edgecolor="black", linewidth=0.6))
    ax.text(x + 0.007, ytop + 0.031, c, fontsize=7.2, fontweight="bold", va="center")

y = ytop
for row, h in zip(ROWS, ROWH):
    y -= h
    cells = [row["cls"], row["agg"], row["exp"], row["loss"], row["src"]]
    for j, (x, w, txt) in enumerate(zip(COLX, COLW, cells)):
        ax.add_patch(Rectangle((x, y), w, h, facecolor="white", edgecolor="black",
                               linewidth=0.6, hatch="//" if row["preprint"] else None))
        if txt:
            ax.text(x + 0.007, y + h / 2, txt, fontsize=FS, va="center",
                    fontweight="bold" if j == 0 else "normal",
                    bbox=dict(facecolor="white", edgecolor="none", pad=1.2, alpha=0.95))
        else:
            ax.text(x + w / 2, y + h / 2, "not measured", fontsize=6.4, va="center",
                    ha="center", color="#8A8A8A", style="italic",
                    bbox=dict(facecolor="white", edgecolor="none", pad=1.2, alpha=0.95))

ax.text(0.0, y - 0.030, "NADPH-diaphorase histochemistry (1999) and transcriptomically defined "
                        "somatostatin+ interneuron subclasses (2025)\nare not established as the "
                        "same population and are not aligned to a common row. Imaged cells are not "
                        "independent\nunits comparable to donors or cases.",
        fontsize=7.0, color="#444444", va="top")

save_figure(fig, os.path.join(HERE, "..", "fig_sec6_aggregate_burden_versus_cell_death.png"))

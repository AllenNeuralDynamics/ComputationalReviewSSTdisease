import sys, pathlib
sys.path.insert(0, str(pathlib.Path.cwd()))

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from shared_style import COLORS, apply_style, save_figure

apply_style()
OUT = "../fig_sec7_pv_versus_sst_depletion_across_conditions.png"

# Every value below is quoted verbatim from the source sentence recorded beside
# it. Nothing is converted, summed, rescaled or back-calculated.

PANEL_A = [  # cortical PV+ cell-count / density reductions (%)
    dict(value=27.1,  label="Lin 2021 — TDP-43 Q331K mouse, frontal cortex",
         src="We found that the frontal cortex showed a reduction (by 27.1%) in PV+ "
             "interneuron density in mutant mice."),
    dict(value=25.0,  label="White 2018 — TDP-43 Q331K/Q331K mouse, frontal cortex (reported as ~25%)",
         src="We therefore immunostained for parvalbumin and found a ~25% reduction in "
             "parvalbumin-positive cells in the frontal cortex of TDP-43 Q331K/Q331K mice."),
    dict(value=47.6,  label="Magliozzi 2021 — human progressive MS, motor cortex (MS high)",
         src="... in both MS high cases (47.6%; P < 0.0001) and MS low cases (31.5%; "
             "P < 0.0001) with respect to controls."),
    dict(value=31.5,  label="Magliozzi 2021 — human progressive MS, motor cortex (MS low)",
         src="... in both MS high cases (47.6%; P < 0.0001) and MS low cases (31.5%; "
             "P < 0.0001) with respect to controls."),
    dict(value=29.53, label="May 2024 — rat blast TBI, cortical layer 5 (7 days post-injury)",
         src="... a reduction of 29.53% for 7-days and 45.73% for 1-month post-injury "
             "relative to control ..."),
    dict(value=45.73, label="May 2024 — rat blast TBI, cortical layer 5 (1 month post-injury)",
         src="... a reduction of 29.53% for 7-days and 45.73% for 1-month post-injury "
             "relative to control ..."),
]

PANEL_B = [  # hippocampal PV+ cell-count reductions (%) — two quantities, see caption
    dict(value=39.0, kind="loss vs separate control group",
         label="Mishra 2015 — rat status epilepticus (vehicle arm), dentate gyrus",
         src="The reductions were 39% for PV + interneurons (p < 0.0001) ..."),
    dict(value=42.0, kind="uncorrected within-group total reduction",
         label="Thielsen 2013 — wobbler mouse, hippocampal formation (total)",
         src="However, the reductions were considerably more extensive in the wobbler mice "
             "(total reduction: wobbler 42%; control 18%) ..."),
    dict(value=18.0, kind="uncorrected within-group total reduction",
         label="Thielsen 2013 — control, same interval",
         src="However, the reductions were considerably more extensive in the wobbler mice "
             "(total reduction: wobbler 42%; control 18%) ..."),
]

PANEL_C1 = dict(  # PV-immunoreactive AREA fraction — not cell number
    value=52.2, label="Falco 2014 — EAE mouse, M1",
    src="the area occupied by PV was reduced by 52.2 %, while the area occupied by vGAT "
        "was reduced by 56.5 %")

PANEL_C2 = [  # absolute PV+ density, neurons/mm2 — never converted to a percentage
    dict(value=11.2, sd=15.3, label="non-demented"),
    dict(value=9.7,  sd=15.8, label="AD dementia"),
]
PANEL_C2_SRC = ("The mean density of PV+ neurons per mm 2 was similar between ND and ADD cases "
                "(mean ± SD: 11.2 PV+ ± 15.3 neurons/mm 2 and 9.7 PV+ ± 15.8 neurons/mm 2 , "
                "respectively ...)")

PANEL_D = [  # % reduction in labelled interneurons (SST, except Levenga 2013)
    dict(value=65.0, population="SST", reporter=True,
         label="Frankowski 2022 — mouse TBI, hilus, virally labelled cells (reported as ~65%)",
         src="We observed ~65% reduction in GFP+ cells in the hilus ..."),
    dict(value=46.0, population="SST", reporter=False,
         label="Mishra 2015 — rat status epilepticus (vehicle arm), dentate gyrus, stereological counts",
         src="The reductions were ... 46% for SST + interneurons (p < 0.001) ..."),
    dict(value=20.0, population="PV + SST combined", reporter=False,
         label="Levenga 2013 — PV + SST combined (CA1), aged tau transgenic mouse, "
               "immunohistochemical counts (reported as ~20%)",
         src="We found that the number of both PV and SST interneuron subtypes were "
             "significantly decreased (~20%) in area CA1 of Tg mice compared to WT mice."),
]

PANEL_E = dict(  # a pathology burden, not a loss — own axis
    value=40.0, label="Morrone 2022 — TgF344-AD rat, hippocampus, 15 months (reported as >40%)",
    src="... the dystrophic SST neurons made up > 40% of the SST hippocampal population at "
        "15 months of age ...")

fig = plt.figure(figsize=(7.4, 11.6))
gs = GridSpec(3, 3, figure=fig, height_ratios=[1.15, 1.0, 1.0],
              hspace=1.45, wspace=0.70, left=0.30, right=0.985, top=0.945, bottom=0.105)

HET = "heterogeneous comparison — values not pooled"
GREY = COLORS["neutral_gray"]

def barh(ax, values, labels, colors, hatches=None, xmax=70, xlabel=""):
    hatches = hatches or [None] * len(values)
    for i, (v, c, h) in enumerate(zip(values, colors, hatches)):
        ax.barh(i, v, color=c, edgecolor="black", linewidth=0.5, height=0.60, hatch=h)
        ax.text(v + xmax * 0.015, i, f"{v:g}", va="center", ha="left", fontsize=8)
    ax.set_yticks(list(range(len(values))))
    ax.set_yticklabels(labels, fontsize=7.2)
    ax.invert_yaxis()
    ax.set_xlim(0, xmax)
    ax.set_xlabel(xlabel, fontsize=8.8)

def panel_title(ax, text, note=None):
    ax.set_title(text, loc="left", fontsize=11, fontweight="bold", pad=16)
    if note:
        ax.annotate(note, xy=(0.0, 1.02), xycoords="axes fraction", ha="left",
                    fontsize=7.8, style="italic", color=GREY)

def footnote(ax, text, dy=-0.60):
    ax.annotate(text, xy=(0.0, dy), xycoords="axes fraction", ha="left",
                fontsize=7.4, color=GREY)

# ---- Panel A -------------------------------------------------------------
axA = fig.add_subplot(gs[0, :])
barh(axA, [e["value"] for e in PANEL_A], [e["label"] for e in PANEL_A],
     [COLORS["pv"]] * len(PANEL_A), xmax=60,
     xlabel="% reduction in PV-immunoreactive cell density or number")
panel_title(axA, "A  Cortical PV+ cell-count / density reductions", HET)
footnote(axA, "Three species and three disease entities on one axis; Lin 2021 and "
              "White 2018 report the same TDP-43 Q331K model.", dy=-0.42)

# ---- Panel B -------------------------------------------------------------
axB = fig.add_subplot(gs[1, 0])
barh(axB, [e["value"] for e in PANEL_B], [e["label"] for e in PANEL_B],
     [COLORS["pv"], COLORS["pv"], COLORS["no_change"]],
     hatches=[None, "//", "//"], xmax=60,
     xlabel="% reduction in PV+ cell number")
panel_title(axB, "B  Hippocampal PV+", HET)
footnote(axB, "Not one quantity: plain bar is a loss against a separate control\n"
              "group; hatched bars are uncorrected within-group total reductions\n"
              "over the study interval.", dy=-0.72)

# ---- Panel C (two independent axes) --------------------------------------
axC1 = fig.add_subplot(gs[1, 1])
barh(axC1, [PANEL_C1["value"]], ["Falco 2014"], [COLORS["pv"]], xmax=70,
     xlabel="% reduction in PV-immunoreactive\ncortical AREA")
panel_title(axC1, "C  Differ in kind")
footnote(axC1, "EAE mouse, M1. Area fraction conflates\ncell number with per-cell "
               "immunoreactivity;\nit is not a cell count.", dy=-0.92)

axC2 = fig.add_subplot(gs[1, 2])
xs = list(range(len(PANEL_C2)))
axC2.bar(xs, [e["value"] for e in PANEL_C2], yerr=[e["sd"] for e in PANEL_C2],
         capsize=3, color=COLORS["pv"], edgecolor="black", linewidth=0.5,
         width=0.55, error_kw=dict(linewidth=0.8))
axC2.set_xticks(xs)
axC2.set_xticklabels([e["label"] for e in PANEL_C2], fontsize=7.4)
axC2.set_ylabel("PV+ neurons/mm$^2$", fontsize=8.8)
axC2.set_ylim(-8, 30)
axC2.axhline(0, color="black", linewidth=0.6)
for i, e in enumerate(PANEL_C2):
    axC2.text(i, e["value"] + e["sd"] + 1.0, f"{e['value']:g}", ha="center", fontsize=8)
axC2.set_title("Merino-Serrais 2025", loc="right", fontsize=8.4, pad=16)
footnote(axC2, "Human; region not resolved in the available\nmaterial. Error bars are SD and exceed the\nmean; the report says only 'similar' and\nquotes no test.", dy=-0.62)

# ---- Panel D -------------------------------------------------------------
axD = fig.add_subplot(gs[2, :2])
colsD = [COLORS["sst"] if e["population"] == "SST" else COLORS["mixed_gabaergic"]
         for e in PANEL_D]
barh(axD, [e["value"] for e in PANEL_D], [e["label"] for e in PANEL_D], colsD,
     hatches=["xx" if e["reporter"] else None for e in PANEL_D], xmax=80,
     xlabel="% reduction in labelled interneurons\n(SST, except Levenga 2013 = PV and SST counted together)")
panel_title(axD, "D  Somatostatin interneuron depletion",
            HET + "; bars are not ordered by subfield or by severity")
footnote(axD, "Cross-hatched bar is a reporter-based count: labelling efficiency after "
              "injury cannot be\nseparated from cell loss. Subfield is perfectly confounded "
              "with study, species, insult,\ntimepoint and labelling method, so no gradient "
              "across the bars may be inferred.", dy=-0.66)

# ---- Panel E -------------------------------------------------------------
axE = fig.add_subplot(gs[2, 2])
axE.bar([0], [PANEL_E["value"]], color=COLORS["sst"], edgecolor="black",
        linewidth=0.5, width=0.45, hatch="..")
axE.text(0, PANEL_E["value"] + 1.5, "40", ha="center", fontsize=8)
axE.set_xticks([0])
axE.set_xticklabels(["Morrone 2022"], fontsize=7.6)
axE.set_ylim(0, 60)
axE.set_ylabel("% of SST hippocampal population\nwith dystrophic tau (15 months)",
               fontsize=7.9)
axE.set_title("E  Tau burden, not loss", loc="left", fontsize=11, fontweight="bold", pad=16)
footnote(axE, "TgF344-AD rat, hippocampus, 15 months;\nreported as >40%. The denominator is\n"
              "itself depleted, so this is a pathology\nburden and not a loss.", dy=-0.42)

fig.text(0.30, 0.655,
         "All plotted values were extracted from the source papers' full text. No bar in this "
         "figure carries a stated group size,\nand no value was converted between quantity types."
         ,
         fontsize=7.4, color=GREY)

save_figure(fig, OUT)
print("saved", OUT)

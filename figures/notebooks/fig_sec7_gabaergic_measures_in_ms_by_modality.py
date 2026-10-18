import sys, pathlib, textwrap
sys.path.insert(0, str(pathlib.Path.cwd()))

import matplotlib.pyplot as plt
from shared_style import COLORS, apply_style, save_figure

apply_style()
OUT = "../fig_sec7_gabaergic_measures_in_ms_by_modality.png"

# ---------------------------------------------------------------------------
# A units-explicit table: no axis, no bars, no pooled summary. Every number is
# verbatim from the source sentence recorded with its column. The Ziccardi 2024
# group means are not printed: they contradicted the direction stated in that
# study's own sentence and abstract and could not be resolved, so they were
# deleted rather than tabulated.
# ---------------------------------------------------------------------------
STUDIES = [
    dict(head="Edited MRS\n(MEGA-PRESS, 3 T)\nCao 2017",
         level="Bulk tissue GABA+ pool (neurotransmitter)",
         region="Posterior cingulate cortex; left hippocampus (null in medial prefrontal cortex)",
         cohort="Twenty-eight RRMS patients and twenty-six healthy controls (enrolled; analysed set may be smaller)",
         value="p = 0.036 (posterior cingulate); p = 0.039 (left hippocampus); no concentration reported",
         direction="LOWER GABA+ in MS; magnitude not reported",
         dkey="decrease",
         src="Patients had significantly lower GABA+ levels in the PCC (p = 0.036) and left "
             "hippocampus (p = 0.039) compared to healthy controls."),
    dict(head="7T MRS\nMadsen 2024",
         level="Bulk tissue GABA pool (neurotransmitter)",
         region="Cortical MRS voxel (lesion-matched)",
         cohort="Forty-seven patients with MS (34 RRMS, 13 SPMS) and 23 healthy controls",
         value="-0.71 log(mm3) per unit GABA (95% CI -1.24 to -0.18), p = 0.01",
         direction="Not a patient-vs-control contrast: a within-patient association",
         dkey="no_change",
         src="Conversely, higher GABA concentration was associated with lower cortical lesion "
             "volume (-0.71, 95% CI -1.24 to -0.18 log(mm3), p = 0.01) in the corresponding "
             "MRS voxel."),
    dict(head="[11C]flumazenil PET\nKang 2020",
         level="Postsynaptic GABA-A receptor availability",
         region="Global cortical grey matter (6 regions of interest)",
         cohort="Sixteen MS patients; Ten age-matched healthy controls (pilot study)",
         value="BPND 5.72 (SD 0.91) in MS vs 4.79 (SD 0.41) in controls, p = 0.002; the abstract states 4.70 for the control group",
         direction="HIGHER GABA-A receptor binding in MS",
         dkey="increase",
         src="The global cortical FMZ-PET BPND in patients was higher than that of HC "
             "(5.72 +/- 0.91 versus 4.79 +/- 0.41, p = 0.002) ..."),
    dict(head="CSF immunoassay\nZiccardi 2024",
         level="Parvalbumin interneuron marker protein in fluid",
         region="Cerebrospinal fluid (no region)",
         cohort="72 patients with MS; no control group",
         value="p = 0.033 (direction only; no concentration tabulated)",
         direction="blank: this study has no control group",
         dkey="no_change",
         src="CSF PVALB levels were higher in sCI patients than in CN (p = 0.033)."),
]
FIELDS = [("level",     "Level of the\nsystem indexed"),
          ("region",    "Region"),
          ("cohort",    "Cohort as the\nabstract states it"),
          ("value",     "Reported value\n(own units)"),
          ("direction", "Direction vs\ncontrols")]

WRAP = 20
COL_X = [0.0, 0.190, 0.395, 0.600, 0.805]
ROW_Y = [0.845, 0.705, 0.520, 0.320, 0.130]

fig, ax = plt.subplots(figsize=(7.1, 6.6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")
ax.set_title("GABAergic measures in multiple sclerosis cortex, one column per modality",
             loc="left", fontsize=10.5, fontweight="bold", pad=22)
ax.annotate("units-explicit table — no shared axis, no bars, no pooled summary",
            xy=(0.0, 1.035), xycoords="axes fraction", fontsize=8,
            style="italic", color=COLORS["neutral_gray"])

for x, s in zip(COL_X[1:], STUDIES):
    ax.text(x, 0.985, s["head"], fontsize=7.6, fontweight="bold", va="top", ha="left",
            transform=ax.transAxes)
ax.plot([0, 1], [0.895, 0.895], color="black", linewidth=0.8, transform=ax.transAxes)

for y, (key, label) in zip(ROW_Y, FIELDS):
    ax.text(COL_X[0], y, label, fontsize=7.4, fontweight="bold", va="top", ha="left",
            transform=ax.transAxes)
    for x, s in zip(COL_X[1:], STUDIES):
        colour = COLORS[s["dkey"]] if key == "direction" else "black"
        weight = "bold" if key == "direction" and s["dkey"] in ("decrease", "increase") else "normal"
        ax.text(x, y, textwrap.fill(s[key], WRAP), fontsize=7.0, va="top", ha="left",
                color=colour, fontweight=weight, transform=ax.transAxes)

ax.annotate("Only the cerebrospinal fluid column is interneuron-specific: MRS GABA is a bulk tissue "
            "metabolite pool and\nflumazenil binding is postsynaptic receptor availability, so the "
            "opposite directions are not contradictory\nmeasurements of one quantity. No summed "
            "participant total is printed and no concentration column appears.",
            xy=(0.0, -0.015), xycoords="axes fraction", fontsize=7.2,
            color=COLORS["neutral_gray"])

save_figure(fig, OUT)
print("saved", OUT)

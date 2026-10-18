# Figure: cortical somatostatin in Lewy body disease, by cognitive and
# neuropathological status. Panel A holds the two series that report a magnitude;
# panel B is a direction-only matrix with no numeric axis. Null results are never
# drawn as a bar at zero. All values are quoted verbatim from the source sentences.
import os
import sys

# Resolve the directory that holds shared_style.py so the notebook runs from the
# repository root or from figures/notebooks.
BASE = next(p for p in (".", "figures/notebooks", os.path.join(os.getcwd(), "figures", "notebooks"))
            if os.path.exists(os.path.join(p, "shared_style.py")))
sys.path.insert(0, BASE)
FIGDIR = os.path.normpath(os.path.join(BASE, ".."))
import textwrap
import matplotlib.pyplot as plt
from shared_style import COLORS, apply_style, save_figure

apply_style()

PANEL_A = [
    dict(entry_id="S05-C02a-E1", study="Flint Beal 1988",
         row="demented PD with Alzheimer-type cortical pathology",
         region="17 of twenty-two cortical regions with significant reductions",
         groups="12 control, 13 demented Parkinsonian patients",
         groups_source="Somatostatin-like immunoreactivity (SLI) and neuropeptide Y-like "
                       "immunoreactivity (NPYLI) were measured in postmortem brain tissue from "
                       "12 control patients and 13 demented Parkinsonian patients who had "
                       "Alzheimer-type cortical pathology.",
         lo=50, hi=60, display="typically 50-60%", kind="range",
         source="Twenty-two cortical regions were examined. Significant reductions in cortical "
                "SLI were found in 17 regions, while significant reductions in cortical NPYLI "
                "were found in nine regions. The reductions in SLI were typically 50-60%, while "
                "NPYLI reductions were 20-30%."),
    dict(entry_id="S05-C02a-E2", study="Beal 1986",
         row="demented PD with Alzheimer-type cortical pathology",
         region="Brodmann area 6 and Brodmann area 21",
         groups="15 control, 7 non-demented, 7 demented parkinsonian patients",
         groups_source="Somatostatin-like immunoreactivity (SLI) was measured in postmortem brain "
                       "tissue from 15 control patients, 7 non-demented parkinsonian patients and "
                       "7 demented parkinsonian patients who had Alzheimer-type cortical "
                       "pathology.",
         lo=40, hi=40, display="approximately 40%", kind="point",
         source="Demented parkinsonian patients with Alzheimer-type cortical pathology had "
                "significantly reduced (approximately 40%) levels of SLI in both the frontal "
                "(Brodmann area 6) and temporal (Brodmann area 21) cortex."),
]

PANEL_B = [
    dict(entry_id="S05-C02b-E1", study="Beal 1986", cohort="non-demented PD",
         region="cortex and subcortex", assay="RIA of SLI", outcome="unchanged", note="",
         source="The non-demented parkinsonian patients had normal concentrations of SLI in the "
                "cerebral cortex, hippocampus, amygdala, putamen, caudate or globus pallidus."),
    dict(entry_id="S05-C02b-E2", study="Whitford 1988",
         cohort="presenile and senile AD; mentally normal and cognitively impaired PD",
         region="BA9 and BA21", assay="RIA of SLI + [3H]somatostatin binding",
         outcome="unchanged",
         note="no significant change between any of the disease groups;\none row covers peptide content and receptor binding",
         source="No significant changes in SLI or somatostatin binding in the frontal and "
                "temporal cortex were found between any of the disease groups."),
    dict(entry_id="S05-C02b-E3", study="Leake 1991", cohort="SDLT and SDAT",
         region="temporal neocortex", assay="RIA of SRIF", outcome="reduced", note="",
         source="The concentration of temporal and occipital neocortical CRH was diminished in "
                "both SDAT and SDLT compared to control values, whereas SRIF was reduced only in "
                "temporal cortex in both these conditions."),
    dict(entry_id="S05-C02b-E4", study="Leake 1991", cohort="SDLT and SDAT",
         region="occipital neocortex", assay="RIA of SRIF", outcome="unchanged",
         note="inferred by exclusion from the source's word 'only'",
         source="The concentration of temporal and occipital neocortical CRH was diminished in "
                "both SDAT and SDLT compared to control values, whereas SRIF was reduced only in "
                "temporal cortex in both these conditions."),
    dict(entry_id="S05-C02b-E5", study="Leake 1991", cohort="Parkinson's disease",
         region="temporal and occipital neocortex", assay="RIA of SRIF",
         outcome="unchanged", note="",
         source="In contrast, the concentrations of both CRH and SRIF were unaltered in PD."),
    dict(entry_id="S05-C02b-E6", study="Khundakar 2016", cohort="DLB and AD",
         region="primary visual cortex", assay="somatostatin ELISA", outcome="unchanged",
         note="p = 0.40 (DLB) and p = 0.09 (AD), uncorrected; printed as row text",
         source="Somatostatin levels in primary visual cortex were unchanged in DLB (p = 0.40, "
                "uncorrected) or in AD (p = 0.09, uncorrected) compared to control."),
]

OUTCOME_COLOR = {"reduced": COLORS["decrease"], "unchanged": COLORS["no_change"]}

fig, (axA, axB) = plt.subplots(2, 1, figsize=(7.09, 8.0),
                               gridspec_kw=dict(height_ratios=[1.0, 1.75], hspace=0.46))

# ---- Panel A: reported magnitudes -----------------------------------------
for i, e in enumerate(PANEL_A[::-1]):
    y = i
    if e["kind"] == "range":
        axA.plot([e["lo"], e["hi"]], [y, y], color=COLORS["decrease"], lw=7,
                 solid_capstyle="butt", zorder=2)
    else:
        axA.plot([e["lo"]], [y], marker="o", ms=11, color=COLORS["decrease"],
                 markeredgecolor="black", markeredgewidth=0.8, zorder=2)
    axA.annotate(e["display"], (e["hi"], y), textcoords="offset points", xytext=(12, 0),
                 va="center", fontsize=9, color=COLORS["decrease"], fontweight="bold")
    axA.annotate(e["row"] + "\n" + e["region"] + "\n" + e["groups"], (1.5, y),
                 textcoords="offset points", xytext=(0, -14), va="top", ha="left",
                 fontsize=7.4, color=COLORS["excitatory"])
axA.set_yticks(range(len(PANEL_A)))
axA.set_yticklabels([e["study"] for e in PANEL_A[::-1]], fontsize=9)
axA.set_xlim(0, 78)
axA.set_ylim(-0.75, len(PANEL_A) - 0.25)
axA.set_xlabel("reduction in somatostatin-like immunoreactivity versus control, as reported (%)")
axA.set_title("A   Magnitude of cortical somatostatin reduction, reported only in parkinsonian\n"
              "     dementia with Alzheimer-type cortical pathology (no dispersion reported;\n"
              "     no error bars; region sets are not commensurable)", fontsize=9, loc="left")

# ---- Panel B: direction-only matrix, no numeric axis -----------------------
for i, e in enumerate(PANEL_B[::-1]):
    y = i
    axB.scatter([0.022], [y], s=170, marker="s", color=OUTCOME_COLOR[e["outcome"]],
                edgecolors="black", linewidths=0.8, zorder=3, clip_on=False)
    axB.annotate(e["outcome"], (0.055, y), va="center", ha="left", fontsize=8.5,
                 fontweight="bold", color=OUTCOME_COLOR[e["outcome"]])
    txt = "\n".join(textwrap.wrap(e["cohort"] + "  |  " + e["region"] + "  |  " + e["assay"], 74))
    axB.annotate(txt, (0.235, y), va="center", ha="left", fontsize=7.4)
    if e["note"]:
        nlines = txt.count("\n") + 1
        axB.annotate(e["note"], (0.235, y), textcoords="offset points",
                     xytext=(0, -(5.0 * nlines + 7.0)), va="top", ha="left", fontsize=7.0,
                     color=COLORS["excitatory"])
axB.set_yticks(range(len(PANEL_B)))
axB.set_yticklabels([e["study"] for e in PANEL_B[::-1]], fontsize=8)
axB.set_xlim(0, 1)
axB.set_ylim(-0.8, len(PANEL_B) - 0.2)
axB.set_xticks([])
axB.spines["bottom"].set_visible(False)
axB.set_title("B   Direction-of-change matrix, one row per study x region x cohort.\n"
              "     No numeric axis: nulls are not plotted at zero percent change", fontsize=9,
              loc="left")

fig.text(0.5, 0.055, "heterogeneous comparison - values not pooled; regions, cohorts and assays "
                     "differ and are printed on every row",
         ha="center", fontsize=8, style="italic", color=COLORS["excitatory"])
fig.text(0.5, 0.028, "* Khundakar 2016's p values were extracted from the full text; the other "
                     "five entries were extracted from the source abstracts.",
         ha="center", fontsize=7.5, color=COLORS["excitatory"])

save_figure(fig, os.path.join(FIGDIR, "fig_sec5_cortical_somatostatin_conditional_on_copathology.png"))

(sec-introduction)=

# Introduction

Somatostatin-expressing (SST) interneurons are the inhibitory cell class most often named as a shared casualty of neurodegeneration. The nomination rests on an observation that has survived four decades of remeasurement.

In Alzheimer's disease (AD) cortex, the observation arrives from assay families that cannot be converted into one another:

- somatostatin immunoreactivity falls in proportion to neuritic plaque and tangle counts, while neuropeptide Y (NPY) in the same tissue does not {cite:p}`Dawbarn1986`
- reduced somatostatin in cerebrospinal fluid has been tied to parietal glucose hypometabolism on positron emission tomography {cite:p}`Tamminga1987`
- somatostatin messenger RNA-containing neurons are less dense in hippocampus and cortex, although among the labelled cell densities in that series only the overall parahippocampal reduction of −59% reached significance, and the authors read it as partial preservation of cortical cells' ability to express the transcript {cite:p}`Dournaud1994`
- unbiased tandem-mass-tag proteomics of frontal cortex recovers somatostatin among the most strongly downregulated proteins, as a discovery-stage estimate that the study did not carry through to validation {cite:p}`Sathe2020`
- RNA sequencing of precuneus places *SST* among the most strongly downregulated transcripts {cite:p}`Guennewig2021`

Deconvolution of 1037 postmortem cortical samples then identified fewer SST inhibitory neurons as the strongest cell-type association with AD in that dataset (β = −0.48, p_bonf = 8.98 × 10⁻⁹) {cite:p}`Consens2022b`. Four non-interconvertible assay families, independent groups, one direction: few observations in the evidence assembled here are this reproducible.

The observation is attractive because the cell class it points to would, if lost, explain several disease phenotypes at once. SST interneurons supply inhibition to distal dendrites and not to the soma. Activating hippocampal oriens-lacunosum moleculare (O-LM) cells suppresses dendritic calcium signals in stratum radiatum without changing somatic depolarisation {cite:p}`Udakis2025`. Potentiating SST-mediated inhibition leaves the probability of spiking from Schaffer-collateral input essentially unchanged (0.53 ± 0.04 against 0.5 ± 0.08) {cite:p}`Udakis2020`. Recruitment of the class is also state-dependent, with bistratified and PV+ basket cells firing 16.9 and 19.2 Hz faster than O-LM cells during sleep {cite:p}`Katona2014`.

Models put a weight on that anatomy. In a detailed model of human layer 2/3 cortex, reducing SST-mediated inhibition alone raised baseline pyramidal firing by 68% (0.72 ± 0.03 to 1.21 ± 0.03 Hz) while changing the stimulus-evoked response by 3% {cite:p}`Yao2025`. But in circuit models carrying several interneuron classes, the sign of the network response to an SST perturbation depends on the operating regime and not on the perturbation alone {cite:p}`Bos2025`.

Three properties make the class a plausible single point of failure:

- it gates dendritic integration
- it is required for phase-locking to a context-dependent low-gamma rhythm ({ref}`sec-circuit-consequences`)
- it releases a peptide as well as GABA ({ref}`sec-sst-identity`)

Failure of such a class would be expected to produce hyperexcitability, oscillatory disorganisation and memory impairment together.

Reductions of the somatostatin signal are also reported after a wide range of insults, in hippocampus and cortex alike. Hilar somatostatin-immunoreactive density is reduced in human and experimental temporal lobe epilepsy, and the surviving cells receive increased excitatory drive {cite:p}`Halabisky2010`. Status epilepticus halves the population of GFP-labelled hilar SST interneurons {cite:p}`Buckmaster2011`. Controlled cortical impact removes roughly 65% of virally labelled hilar SST cells, with rabies-traced starter neurons falling from 48.0 ± 3.7 cells to 9.4 ± 0.9 cells; yet lateral fluid percussion injury produces no obvious loss of any interneuron subset in motor cortex {cite:p}`Frankowski2022, Carron2019`.

Ageing moves the signal in the same direction. Somatostatin and NPY transcripts are the GABAergic markers most frequently reduced in aged rat hippocampus, with parvalbumin (PV) mRNA least often affected {cite:p}`Vela2003`. In rat primary auditory cortex the composition of the interneuron pool shifts across the lifespan, with SST-expressing cells falling to about a fifth of all interneurons by P350 {cite:p}`Ouellet2014`.

This generality is part of the problem. A marker that declines with age, injury, seizure and amyloid alike is not by itself evidence of a disease-specific lesion.

(sec-01-measurement)=

## A marker is not a cell

The deeper difficulty is that in most of this literature the cell is identified by the molecule being measured. When somatostatin immunoreactivity falls, a neuron that has stopped expressing the peptide and a neuron that has died produce the same reading.

The experiments that break the tie label the cells independently. Genetic fate mapping in a *Pten* knockout model found the density of eGFP-labelled SST cells reduced in hilus (4,395 ± 182 to 3,411 ± 322 cells/mm³, p = 0.0334), with no difference in oxidative-stress marking between genotypes and no colocalisation with cleaved caspase-3 {cite:p}`Drake2024`. The change is smaller and more layer-specific than marker counts in comparable models report, and it arrives without a death signal.

In human tissue the spread of reported values brackets zero:

- stereological counting gives a 50% reduction in SST-immunoreactive cell number in AD hippocampus (p = 0.0066) {cite:p}`GonzalezRodriguez2021`
- immunohistochemical counts in cortex find no difference between aged controls and cases {cite:p}`Li1996b`
- a knock-in model carrying amyloid at endogenous dosage shows no significant change in SOM interneuron density in CA1 stratum oriens even at 24 months {cite:p}`Sos2020`

The genetic tools that could settle such questions are themselves imperfect reporters. SST-immunonegative tdTomato-positive cells in SST-Cre tissue were numerous enough to force an entire region out of one whole-brain mapping analysis {cite:p}`Muhsinov2026`. The label also aggregates many cell types: eleven spatially restricted SST types in human middle temporal gyrus {cite:p}`Hodge2019`, mapping onto distinct morpho-electric phenotypes {cite:p}`Lee2023b`.

{numref}`fig-sec1-sst-loss-landscape` collects these measurements in the units each source reports, which is the only way they can be shown together.

:::{figure} ../figures/fig_sec1_sst_loss_landscape.png
:name: fig-sec1-sst-loss-landscape
:width: 100%
**The same headline, five incompatible measurements.** Reported change in the somatostatin signal across insult and disease, grouped by the unit in which each source reports it; values are not pooled and panels do not share an axis. (A) Entries reported as a percentage reduction: loss of virally labelled hilar SST cells after controlled cortical impact, given in the source as approximately 65% {cite:p}`Frankowski2022`; a 50% reduction in SST-immunoreactive cell number in AD hippocampus, p = 0.0066 {cite:p}`GonzalezRodriguez2021`; and five rows from one in-situ-hybridisation series measuring the density of cells containing somatostatin messenger RNA in AD: four regional values (frontal grey matter −41%, frontal white matter −66%, hippocampus −44%, parahippocampal white matter −40%) and, separately, the overall parahippocampal reduction of −59%, the only one of these densities to reach significance {cite:p}`Dournaud1994`. (B) Entries reported as cell densities, printed as the source prints them and not converted to a percentage: hilar eGFP-SST density in a *Pten* knockout model, 4,395 ± 182 against 3,411 ± 322 cells/mm³, p = 0.0334, dispersion type not stated in the source sentence {cite:p}`Drake2024`. (C) Entries that cannot be placed on the panel A axis, drawn as annotated markers rather than omitted, because omitting them biases the visible distribution towards loss: reduced hilar density in human and experimental temporal lobe epilepsy with no magnitude in the retrieved text {cite:p}`Halabisky2010`; GFP-labelled hilar SST interneurons reduced to 48% (vehicle) and 55% (rapamycin) of control after status epilepticus, p < 0.001 — a percentage of control rather than a percentage reduction, so not plottable on the panel A axis {cite:p}`Buckmaster2011`; and two nulls, no difference in somatostatin-immunoreactive cell number in AD cortex {cite:p}`Li1996b` and no significant change in SOM density in CA1 stratum oriens of an endogenous-dosage knock-in at 24 months {cite:p}`Sos2020`. Heterogeneous comparison — values are not pooled. Species (mouse, rat, human), region (hilus, CA1, whole hippocampus, neocortex), insult and the definition of the counted population differ across every row; two entries count a reporter-defined subset rather than the whole population, and one counts transcript-labelled cells, which confounds cell loss with transcript downregulation.
:::

:::{dropdown} 📓 Figure code
```python
import os
import sys

# Resolve the directory that holds shared_style.py so the notebook runs from the
# repository root or from figures/notebooks.
BASE = next(p for p in (".", "figures/notebooks", os.path.join(os.getcwd(), "figures", "notebooks"))
            if os.path.exists(os.path.join(p, "shared_style.py")))
sys.path.insert(0, BASE)
FIGDIR = os.path.normpath(os.path.join(BASE, ".."))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from shared_style import COLORS, apply_style, save_figure

apply_style()

# ---------------------------------------------------------------------------
# Every value below is verbatim from the source sentence recorded for that
# entry. Nothing is converted, back-calculated, rescaled or estimated.
# ---------------------------------------------------------------------------
# (row label, reported %, marker kind, abstract_only, filled, note)
pct = [
    ("Frankowski 2022 - hilar SST cells, virally labelled\n(mouse, controlled cortical impact)",
     65, "rodent", False, True, "source states ~65%"),
    ("Gonzalez-Rodriguez 2021 - SST-immunoreactive cell\nnumber (human AD hippocampus)",
     50, "human", False, True, "p = 0.0066"),
    ("Dournaud 1994 - frontal grey matter [abstract only]", 41, "human", True, False, ""),
    ("Dournaud 1994 - frontal white matter [abstract only]", 66, "human", True, False, ""),
    ("Dournaud 1994 - hippocampus [abstract only]", 44, "human", True, False, ""),
    ("Dournaud 1994 - parahippocampal white matter [abstract only]", 40, "human", True, False, ""),
    ("Dournaud 1994 - parahippocampal, overall [abstract only]", 59, "human", True, True, "the only value\nreaching significance"),
]
drake = [("Control", 4395, 182), ("DGC-Pten KO", 3411, 322)]   # cells/mm3, hilus, p = 0.0334

nonum = [
    ("Halabisky 2010 [abstract only] - hilar SST-immunoreactive density reduced in human and\nexperimental temporal lobe epilepsy; no magnitude in the retrieved text", "abstract"),
    ("Buckmaster 2011 - GFP-labelled hilar SST interneurons reduced to 48% (vehicle) and 55%\n"
     "(rapamycin) of control after status epilepticus, p < 0.001: a percentage of control, not a\n"
     "percentage reduction, so not plottable on the panel A axis", "fulltext"),
    ("Li 1996 [abstract only] - no difference in somatostatin-immunoreactive cell number,\nhuman AD cortex (reported null, no number)", "abstract"),
    ("Sos 2020 - no significant change in SOM density, CA1 stratum oriens,\nendogenous-dosage knock-in at 24 months (reported null)", "fulltext"),
]

fig = plt.figure(figsize=(7.4, 8.2))
gs = GridSpec(3, 1, height_ratios=[1.9, 0.75, 1.05], hspace=0.55, figure=fig)

# ---- Panel A --------------------------------------------------------------
axA = fig.add_subplot(gs[0])
labs, ys = [], []
for i, (lab, v, sp, abs_only, filled, note) in enumerate(pct):
    y = -i
    mk = "o" if sp == "human" else "s"
    axA.plot(v, y, marker=mk, ms=9,
             mfc=COLORS["decrease"] if filled else "white",
             mec=COLORS["decrease"], mew=1.4,
             ls=(0, (2, 1.5)) if abs_only else "-")
    if note:
        axA.annotate(note, (v, y), textcoords="offset points", xytext=(11, 0),
                     fontsize=7.2, va="center")
    labs.append(lab); ys.append(y)
axA.set_yticks(ys); axA.set_yticklabels(labs, fontsize=7.6)
axA.set_ylim(min(ys) - 0.7, 0.7)
axA.set_xlim(0, 100)
axA.set_xlabel("reported reduction (%), each against that study's own control")
axA.set_title("(A) Entries reported as a percentage - three different counted quantities,\n"
              "     plotted one row per reported value and never averaged",
              fontsize=9.5, loc="left", fontweight="bold")
axA.spines[["top", "right"]].set_visible(False)
axA.grid(axis="x", color=COLORS["light_gray"], lw=0.5, alpha=0.6)
axA.set_axisbelow(True)

# ---- Panel B --------------------------------------------------------------
axB = fig.add_subplot(gs[1])
xs = [0, 1]
vals = [d[1] for d in drake]; errs = [d[2] for d in drake]
axB.bar(xs, vals, width=0.4, color=[COLORS["no_change"], COLORS["decrease"]],
        edgecolor="black", lw=0.8)
for x, v, e in zip(xs, vals, errs):
    axB.errorbar(x, v, yerr=e, fmt="none", ecolor="black", elinewidth=0.9, capsize=3, ls="--")
    axB.annotate("{:,} +/- {}".format(v, e), (x, v + e), textcoords="offset points",
                 xytext=(0, 4), ha="center", fontsize=7.5)
axB.set_xticks(xs); axB.set_xticklabels([d[0] for d in drake], fontsize=8)
axB.set_xlim(-0.6, 1.6)
axB.set_ylabel("eGFP-SST cells / mm$^3$\n(hilus)", fontsize=8.5)
axB.set_ylim(0, 5400)
axB.set_title("(B) Drake 2024 - reported as densities, printed as the source prints them and not converted\n"
              "     to a percentage; p = 0.0334, dispersion type (SD or SEM) not stated in the source sentence",
              fontsize=9.5, loc="left", fontweight="bold")
axB.spines[["top", "right"]].set_visible(False)

# ---- Panel C --------------------------------------------------------------
axC = fig.add_subplot(gs[2]); axC.axis("off")
axC.set_title("(C) Entries that cannot be placed on the panel A axis - shown, not omitted", fontsize=9.5,
              loc="left", fontweight="bold")
for i, (txt, acc) in enumerate(nonum):
    yy = 0.86 - i * 0.235
    axC.plot(0.02, yy, marker="o", ms=8, mfc="white", mec=COLORS["neutral_gray"], mew=1.4,
             ls=(0, (2, 1.5)) if acc == "abstract" else "-", transform=axC.transAxes, clip_on=False)
    axC.text(0.07, yy, txt, fontsize=7.4, va="center", transform=axC.transAxes)
axC.text(0.0, -0.10,
         "Heterogeneous comparison - values are not pooled and no summary estimate is shown. Filled marker = value reported as significant or as a\n"
         "point estimate; open circle in (C) = value absent or reported on a scale the panel A axis cannot carry; square = rodent model, circle = human\n"
         "postmortem; rows marked [abstract only] carry values read from an abstract rather than from full text. Species, region, insult and the definition of the\n"
         "counted population differ across every row.",
         fontsize=7.0, va="top", transform=axC.transAxes)

save_figure(fig, os.path.join(FIGDIR, "fig_sec1_sst_loss_landscape.png"))
print("saved")
```
:::

(sec-01-question)=

## The question, and the shape of the answer

This review asks whether loss or dysfunction of SST interneurons is a shared, causally important feature across neurodegenerative disease. Three questions follow from it:

- if it is such a feature, which mechanisms drive it — cell-intrinsic fragility, peptide and somatostatin receptor (SSTR1–SSTR5) signalling, or circuit dysregulation
- how robust the human and model evidence is
- whether any of it justifies SST-targeted biomarkers and therapies

Answering them requires separating the reproducible observation from the inference habitually fused to it, and that separation organises what follows.

{ref}`sec-sst-identity` establishes what the SST label spans and what the genetic toolbox actually reports. {ref}`sec-selective-vulnerability` then asks what happens to that aggregate under ageing and insult, finding region- and insult-specificity where the field often reads class-intrinsic fragility.

The four disease sections test the same claim in four literatures:

- {ref}`sec-alzheimers`, where the deficit is most reproducible and the proposed amyloid-clearance mechanism is directly disputed
- {ref}`sec-parkinsons-lewy-body`, where the cortical deficit appears conditional on Alzheimer-type co-pathology
- {ref}`sec-huntingtons`, where a textbook claim of sparing rests on peptide concentrations measured in atrophic tissue
- {ref}`sec-als-ftd`, where cortical inhibition is well measured in patients while this cell class is barely measured in human tissue at all

Five sections then close the argument:

- {ref}`sec-circuit-consequences` changes the level of description and shows why a fall in somatostatin signalling degrades dendritic gating and oscillations whether or not a neuron dies
- {ref}`sec-human-evidence` assembles the human measurements, which carry both the strongest and the weakest claims here
- {ref}`sec-therapeutics` treats intervention as the direct test of the causal reading
- {ref}`sec-conflicts-limitations` sorts the accumulated disagreements
- {ref}`sec-conclusion` states the conditional answer and the experiments that would change it

(sec-01-evidence-base)=

## What this review can and cannot settle

Four axes recur across all four disease literatures, and they are named here so that the reader can watch them arrive:

- what was measured — peptide, transcript, immunoreactive soma, genetically labelled soma, transcriptomically defined nucleus
- where
- in which model construct
- in which cohort

They are enough to flip the sign of a result. Somatostatin concentrations are elevated instead of reduced in Huntington's disease basal ganglia (caudate 247 ± 24 against 85 ± 11 ng/gm) {cite:p}`Aronin1983`, while somatostatin-positive density is decreased in the Parkinson's disease amygdala {cite:p}`FloresCuadrado2017`. Peptide assay against cell counting: part of the cross-disease reversal is a reversal of method.

Within amyloid models the same class is reported in incompatible states:

- SOM interneuron calcium event rates are elevated above wild type, with hyperactivity greatest near plaques {cite:p}`Algamal2022b`
- dystrophic SST neurons make up more than 40% of the hippocampal SST population of a tau–amyloid rat at 15 months {cite:p}`Morrone2022`
- cholinergic drive onto O-LM interneurons falls without any missing cell being counted {cite:p}`Schmid2016`

Functional hyperactivity, structural dystrophy, synaptic weakening and preserved number are reported for the same class in different constructs. Candidate cell-intrinsic causes — endoplasmic-reticulum stress generated by processing of the somatostatin precursor {cite:p}`Tomoda2022` — have been reported outside amyloid pathology in a single uncorroborated study with n = 4 per group. The trisomic literature is itself split: dendritic inhibition involving Martinotti cells is reported strengthened in one single-laboratory study, and SST-evoked inhibition of granule cells is reported age-dependently reduced in another {cite:p}`ZorrillaDeSanMartin2020, Gutmann2026`. And the one account that assigns SST interneurons the leading mechanistic role in an ALS model rests on a single mouse study {cite:p}`Zhang2016`.

This review assembles 726 primary and secondary reports and the disagreements between them, but it is not a census of the field. Retrieval was dominated by one bibliographic database and did not chase citations forward or backward, so every statement that an experiment was not found is a statement about these searches and not about the literature as a whole. Full text was obtained unevenly across topic areas — all 77 records behind the circuit literature, 22 of the 87 behind the human postmortem and fluid evidence — with the shortfall concentrated in closed-access radioimmunoassay and cerebrospinal fluid work published before 2000. The shortfall is why the human synthesis in {ref}`sec-human-evidence` rests on the modern open-access cohorts and treats the historical series as an abstract-level record. Searches for disconfirming results were capped, so reported nulls are a top-relevance sample and not an exhaustive one. {numref}`fig-sec1-evidence-base-and-argument-arc` shows where the evidence is thick and where it is thin before any claim is made.

Several of the disagreements catalogued in {ref}`sec-conflicts-limitations` are left open at the end of this review, and the conclusion in {ref}`sec-conclusion` is correspondingly conditional.

:::{figure} ../figures/fig_sec1_evidence_base_and_argument_arc.png
:name: fig-sec1-evidence-base-and-argument-arc
:width: 100%
**The argument, and the depth of the evidence behind each part of it.** (A) The three movements of the review and the sections that carry them, with the principal forward references drawn as edges. (B) For each topic area, the number of records read in full text against the total number of records behind that area, with the number of recorded cross-study disagreements printed at the right. Grey is the abstract-only share. The human postmortem and fluid literature has the lowest full-text coverage (22 of 87) and the circuit literature the highest (77 of 77); the shortfall is concentrated in closed-access work published before 2000, which bears directly on how firmly the oldest radioimmunoassay series can be read. Counts are of records assembled for this review, not of the published literature.
:::

:::{dropdown} 📓 Figure code
```python
import os
import sys

# Resolve the directory that holds shared_style.py so the notebook runs from the
# repository root or from figures/notebooks.
BASE = next(p for p in (".", "figures/notebooks", os.path.join(os.getcwd(), "figures", "notebooks"))
            if os.path.exists(os.path.join(p, "shared_style.py")))
sys.path.insert(0, BASE)
FIGDIR = os.path.normpath(os.path.join(BASE, ".."))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from shared_style import COLORS, apply_style, save_figure

apply_style()

# ---------------------------------------------------------------------------
# Panel B counts are the records assembled for this review, per topic area:
# (records read in full text, total records, recorded cross-study disagreements).
# ---------------------------------------------------------------------------
areas = [
    ("SST interneuron identity",            54, 79,  7),
    ("Vulnerability: ageing and insult",    26, 80,  9),
    ("Alzheimer's disease",                 61, 112, 11),
    ("Parkinson's / Lewy body disease",     25, 80,  8),
    ("Huntington's disease",                40, 80,  10),
    ("ALS, FTD and other conditions",       53, 84,  11),
    ("Circuit consequences",                77, 77,  5),
    ("Human postmortem and CSF",            22, 87,  11),
    ("Therapeutic strategies",              58, 86,  9),
    ("Conflicts and model limitations",     45, 79,  9),
]

acts = [
    ("Act 1 - what is established", ["1 Introduction", "2 SST interneuron identity",
                                     "3 Vulnerability in ageing and insult"]),
    ("Act 2 - where the complications arise", ["4 Alzheimer's disease", "5 Parkinson's / Lewy body",
                                               "6 Huntington's disease", "7 ALS, FTD and others"]),
    ("Act 3 - resolution and synthesis", ["8 Circuit consequences", "9 Human evidence",
                                          "10 Therapeutic strategies", "11 Conflicts and limitations",
                                          "12 Conclusion"]),
]

fig = plt.figure(figsize=(9.2, 5.8))
gs = GridSpec(1, 2, width_ratios=[0.95, 1.30], wspace=0.62, figure=fig)

# ---- Panel A: the argument -------------------------------------------------
axA = fig.add_subplot(gs[0]); axA.axis("off")
axA.set_title("(A) The argument", fontsize=9.5, loc="left", fontweight="bold")
act_colors = [COLORS["mixed_gabaergic"], COLORS["sst"], COLORS["npy_nos"]]
y = 0.97
positions = {}
for (title, nodes), col in zip(acts, act_colors):
    axA.text(0.02, y, title, fontsize=8.2, fontweight="bold", color=col, transform=axA.transAxes)
    y -= 0.055
    for n in nodes:
        axA.plot(0.08, y, marker="o", ms=6, color=col, transform=axA.transAxes, clip_on=False)
        axA.text(0.13, y, n, fontsize=7.8, va="center", transform=axA.transAxes)
        positions[n.split()[0]] = y
        y -= 0.052
    y -= 0.025
# principal forward references from the introduction
for target in ["2", "3", "9", "11", "12"]:
    axA.annotate("", xy=(0.055, positions[target]), xytext=(0.055, positions["1"]),
                 xycoords=axA.transAxes, textcoords=axA.transAxes,
                 arrowprops=dict(arrowstyle="->", color=COLORS["neutral_gray"], lw=0.7,
                                 connectionstyle="arc3,rad=-0.45"))
axA.text(0.02, 0.02, "Arrows: the principal forward references made\nfrom the introduction to later sections.",
         fontsize=7.0, transform=axA.transAxes, color=COLORS["neutral_gray"])

# ---- Panel B: evidence depth ----------------------------------------------
axB = fig.add_subplot(gs[1])
ys = range(len(areas))[::-1]
for y, (name, ft, tot, conf) in zip(ys, areas):
    axB.barh(y, tot, color=COLORS["light_gray"], edgecolor="black", lw=0.6, height=0.62)
    axB.barh(y, ft, color=COLORS["sst"], edgecolor="black", lw=0.6, height=0.62)
    axB.text(tot + 2, y, "{} / {}".format(ft, tot), va="center", fontsize=7.4)
    axB.text(152, y, str(conf), va="center", ha="center", fontsize=7.4)
axB.set_yticks(list(ys)); axB.set_yticklabels([a[0] for a in areas], fontsize=7.6)
axB.set_xlim(0, 168)
axB.set_xticks([0, 25, 50, 75, 100])
axB.set_xlabel("records behind each topic area", labelpad=4)
axB.text(152, len(areas) - 0.25, "recorded\ndisagreements", ha="center", va="bottom", fontsize=7.0)
axB.set_title("(B) Depth of the evidence behind it", fontsize=9.5, loc="left", fontweight="bold")
axB.spines[["top", "right"]].set_visible(False)
axB.grid(axis="x", color=COLORS["light_gray"], lw=0.5, alpha=0.6)
axB.set_axisbelow(True)
fig.text(0.015, 0.012, "Blue = records read in full text; grey = abstract only. Counts are of records assembled for this review, not of the published literature.",
         fontsize=7.2, va="bottom")

save_figure(fig, os.path.join(FIGDIR, "fig_sec1_evidence_base_and_argument_arc.png"))
print("saved")
```
:::

Nothing in what follows reverses the direction of the Alzheimer cortical finding, although {ref}`sec-human-evidence` records cortical counting studies that report no difference at all. The argument is about what that fall is a measurement of. The first requirement is to fix what an SST interneuron is and what the somatostatin signal reports — the task of {ref}`sec-sst-identity`.

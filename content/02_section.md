(sec-sst-identity)=

# SST Interneuron Identity: Transcriptomic Subtypes, Connectivity, and Somatostatin Receptor Signaling

The disease literature measures somatostatin and infers a neuron. What that inference buys depends on what the label covers, and the identity literature answers that it covers a great deal: a dozen or more transcriptomic and morpho-electric types, differing in laminar position, in postsynaptic partner and in behavioural-state modulation, reached through driver lines that are not exclusive to the class.

Four conventions are fixed here and used throughout the review:

- *Martinotti cell* names an axonal-projection phenotype — an SST cell whose axon ascends to layer 1 — and is not a synonym for SST. The two criteria in use, reconstructed axonal morphology and retrograde labelling from layer 1, are different operational definitions, and they have not been applied to the same cells {cite:p}`Jiang2015, Hostetler2023`.
- Receptor names are standardised to SSTR1–SSTR5, a convention the primary sources do not share. IUPHAR guidance reserves sst1–5 for recombinant receptors without defined functional characteristics and SST1–5 for fully characterised ones, and it explicitly discourages the SSTR form adopted here {cite:p}`Gunther2018`; other primary sources write Sst1–5 {cite:p}`Lin2013`.
- Where a source scored its cells by somatostatin immunoreactivity and called them SOM-positive, that label is kept wherever its values are reported, and it denotes the same measurement as SST-immunoreactive.
- *The somatostatin signal* appears only where a cited measurement cannot separate peptide content, transcript level and cell number. That ambiguity is the explicit subject of {ref}`sec-selective-vulnerability`.

The companion markers that recur throughout are abbreviated PV (parvalbumin), VIP (vasoactive intestinal peptide) and NPY (neuropeptide Y).

(sec-02-taxonomy)=

## From one marker to a dozen types

Three large surveys each resolved roughly a dozen SST groups.

- {cite:t}`Gouwens2020` identified 13 Sst met-types in mouse visual cortex by integrating Patch-seq morphology, intrinsic physiology and transcriptome in the same cells, substantially more than earlier morphological or electrophysiological schemes had described.
- {cite:t}`Yao2021` divided the Sst subclass into 11 supertypes across the entire mouse isocortex and hippocampal formation, keeping *Sst Chodl*, the long-range projecting group, as a separate entity outside that count.
- {cite:t}`Hodge2019` reported 11 SST types that were spatially restricted in human middle temporal gyrus, among them distinctive deep-layer *SST TH* and *SST NPY* types.

The near-coincidence of those counts is an artefact of three incommensurable counting schemes and not agreement. Met-types, supertypes and transcriptomic clusters are three levels of three taxonomies, and they are not interconvertible: the counts differ in hierarchy level, in species and in region surveyed, and none of those dimensions orders them, as {numref}`fig-sec2-sst-taxonomy-and-subtype-fractions` sets out side by side.

What anchors the taxonomy to cells are the correspondences:

- *Sst Chodl* maps onto the Nos1-positive long-range projecting population {cite:p}`Tasic2018`
- an upper-layer Calb2-expressing type corresponds to the Calb2-positive Martinotti cells labelled in GIN mice {cite:p}`Tasic2016`
- large hyperpolarisation sag and rebound separate Sst neurons electrophysiologically in motor cortex Patch-seq {cite:p}`Scala2020`
- 7 of 11 embryonic medial ganglionic eminence (MGE) SST identities match one-to-one with adult types — four Martinotti, two non-Martinotti and one long-range projecting — with the programmes reported as conserved between mouse and human {cite:p}`Shi2021`

That last conservation claim rests on developmental transcriptional programmes and not on matched adult morpho-electric types, and human SST subtype data are sparser than mouse throughout. Intersectional genetic targeting across the breadth of the class finds that each subtype occupies a stereotyped laminar position and carries a stereotyped axonal projection pattern {cite:p}`Wu2023`, which is the anatomical reason the class is not a functional unit.

The denominator that disease studies implicitly use is less well anchored than its ubiquity suggests. Cre-line co-labelling in mouse V1 placed Sst-Cre cells at 30% ± 1.5 of the GAD67-GFP population, against 36% ± 0.5 for Pvalb-Cre and 17% ± 1 for VIP-Cre {cite:p}`Pfeffer2013`. Three further sources frame the same denominator:

- a review-level compilation of immunohistochemical counts gives approximately 20–30% of mouse somatosensory cortical GABA neurons as somatostatin-expressing, with 40–50% parvalbumin-positive and no overlap between the two {cite:p}`Lin2013`
- a second compilation reports parvalbumin cells as the most frequent class, at 40–50% of all interneurons {cite:p}`Williams2021`
- the parvalbumin, SST and 5HT3aR groups together account for nearly all GABAergic neurons of somatosensory cortex {cite:p}`Rudy2010`

Of the three SST-share values, only the Cre-line count is a primary measurement; the other two are literature syntheses, so their agreement is weaker evidence than it looks.

Within the class, the Martinotti fraction moves with the criterion applied. Axonal reconstruction made Martinotti cells of about 70% of recovered SOM-positive neurons in layers 2/3 and 5 of adult V1 (133/190) {cite:p}`Jiang2015`. By contrast, retrograde labelling from layer 1 classified 54 ± 1% (N = 17) of all SOM cells across all layers of somatosensory cortex as bona fide Martinotti cells {cite:p}`Hostetler2023`. Morphoelectric classification of layer 5 alone gives approximately 10% T-shaped Martinotti, 50% fanning-out Martinotti and 40% non-Martinotti cells {cite:p}`Nigro2018`. The older GAD67-GFP lines had already separated these phenotypes: X98 labels infragranular calbindin-containing layer-1-targeting cells, and X94 labels stuttering, quasi-fast-spiking cells lying in and targeting thalamorecipient layers {cite:p}`Ma2006`.

Co-marker composition varies by area as well. NPY is co-expressed in about a third of SOM-positive interneurons in cingulate cortex, but in fewer than 10% in somatosensory cortex {cite:p}`Riedemann2019`.

:::{admonition} Evidence conflict: is non-Martinotti identity a property of layer 4 or of cortical area?
:class: warning
Patch-seq mapping of layer 4 interneurons onto transcriptomic SST types sets the earlier view — that layer-4-targeting SOM-positive cells form a single morphological population, the non-Martinotti cells, whose axons remain in layer 4 rather than ascending to layer 1 — against its own result: non-fast-spiking SOM-positive neurons in visual cortex layer 4 are predominantly Martinotti cells, in contrast to somatosensory cortex layer 4 where almost all SOM-positive neurons are non-Martinotti, and the two correspond to different transcriptomic types {cite:p}`Scala2019`. Paired recordings across two sensory areas report the same areal split, finding strong morphological differences among layer 4 SST cells, which fell into the non-Martinotti subclass in somatosensory cortex but showed Martinotti-like features in visual cortex {cite:p}`Rachel2025`. The disagreement is between the earlier single-population view, in which non-Martinotti identity belongs to layer 4, and these two studies, in which it belongs to the area; it is open, and it matters because laminar disease findings are routinely generalised across cortex. Quantified morphology and connectivity for non-Martinotti cells outside layer 4 of rodent somatosensory and visual cortex — in association cortices, hippocampus or human tissue — was not retrieved by these searches, so the proportions above should not be assumed to transfer.
:::

:::{figure} ../figures/fig_sec2_sst_taxonomy_and_subtype_fractions.png
:name: fig-sec2-sst-taxonomy-and-subtype-fractions
:width: 100%
**What the SST label covers.** Four panels, each on its own terms; no value is pooled across panels and no cross-panel difference is annotated. (A) Number of SST groups resolved by three classification schemes, with hierarchy level, species, tissue extent surveyed and stated exclusions given per row {cite:p}`Gouwens2020, Hodge2019, Yao2021`. Counts are not comparable units: met-types (multimodal, mouse V1), snRNA-seq clusters (human MTG) and supertypes (whole mouse isocortex plus hippocampal formation) occupy different levels of three different taxonomies and are not interconvertible. Hodge 2019's 11 is the number of SST types reported as spatially restricted and may not be the total number of SST types in human MTG. Yao 2021's 11 supertypes exclude the Sst Chodl (long-range projecting) group; the other two counts carry no stated exclusion. Species and regional coverage differ: one mouse cortical area, one human cortical area, and the entire mouse isocortex plus hippocampal formation. These three counts cannot be ordered by hierarchy level, species or extent surveyed, and this material does not establish how a type count depends on the extent of tissue surveyed. No entry reports a cell-number denominator or any measure of clustering stability. (B) Fraction of SOM cells classified as Martinotti cells under two operational definitions {cite:p}`Jiang2015, Hostetler2023`. Denominators differ: ~70% is of SOM+ cells with recovered morphology in V1 layers 2/3 and 5 only (133/190); 54 ± 1% is of all SOM cells across all layers of somatosensory cortex, a denominator that includes layer 4, where SOM cells are largely non-Martinotti. Martinotti identity is assigned by reconstructed axonal morphology in one study and by retrograde labelling from layer 1 in the other; these are different operational definitions. The retrograde-labelling value is reported as "54 ± 1% (N = 17)"; what N = 17 counts is not stated in the sentence that reports it or in that study's abstract, so the error bar cannot be interpreted and the difference between the two values must not be read as a measured discrepancy. The all-layer denominator lowers the fraction independently of any areal difference, so the direction of the gap is at least partly a layer-sampling artefact. The ">40% of all SOM cells" accounting reported in the same retrograde-labelling study is a different quantity and is not plotted here. The morphology-based fraction is conditioned on successful morphological recovery, a sampling step biased toward cells with recoverable long axons. (C) SST share of cortical GABAergic neurons from one primary count and one review estimate {cite:p}`Pfeffer2013, Rudy2010`. The ~30% value is a review-level literature estimate (synthesis of marker studies, no reported n), not an independent primary measurement; the agreement between the two values must not be read as independent replication. The review estimate is stated for GABAergic neurons with no cortical area or species specified in the sentence that reports it; only the primary measurement is area-specific (mouse V1, all layers). No regional difference between the two values may be asserted. The two values use different labelling bases: Sst-Cre reporter cells against a GAD67-GFP denominator versus immunohistochemical and in situ SST marker counts. Neither entry supplies a cell-count denominator; the ± 1.5 cannot be read as a standard error over a known number of animals or sections. Whether and how much non-SST labelling Sst-Cre adds is not established by the sources behind this panel, and no value for it is plotted. (D) SST-expressing fractions reported for rodent neocortex and for human dorsal striatum, on separate axes {cite:p}`Lin2013, Garma2024`. The cortical and striatal values have different denominators (all cortical GABAergic neurons, histologically counted and literature-derived, versus human striatal interneuron nuclei after single-nucleus RNA-seq QC) and different species; they are plotted on separate axes and the difference between them is not a measured regional difference in SST abundance. The cortical value is a review-level literature estimate compiled from immunohistochemical counts, drawn as a range rather than a point estimate, with no reported n. The striatal figure is reported as two separate transcriptomic subclasses (7.5% and 7.6%); they are shown separately and are not summed, because no summed value is reported by the source and the taxonomy's fourteen subclasses are not established to make these two exhaustive. The cortical panel rests on a single secondary literature estimate and does not constitute replication. Bar and band edges carry source provenance: a dashed outline marks a value taken from an abstract only or from a review-level synthesis.
:::

:::{dropdown} 📓 Figure code
```python
# Figure: SST taxonomy and subtype fractions (section 02, panels A-D).
# Every plotted number is quoted verbatim from the source sentence of its own
# study; nothing is summed, converted or back-calculated. No panel shares an
# axis with another and no value is pooled.
import os, sys, textwrap

NB_DIR = os.path.abspath("figures/notebooks") if os.path.isdir("figures/notebooks") else os.path.abspath(".")
sys.path.insert(0, NB_DIR)
OUT_DIR = os.path.abspath(os.path.join(NB_DIR, ".."))

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from shared_style import COLORS, apply_style, save_figure

apply_style()

# ---

# ---------------------------------------------------------------- panel data
# (A) number of SST groups reported by three classification schemes
TABLE_HEADER = ["Study", "Count", "Hierarchy level", "Species",
                "Tissue extent", "Exclusions stated"]
TABLE_ROWS = [
    ["Gouwens 2020", "13",
     "met-type (multimodal morpho-electric-transcriptomic integration)",
     "mouse", "primary visual cortex (one cortical area)", "none stated"],
    ["Hodge 2019", "11", "snRNA-seq transcriptomic cluster (t-type)",
     "human", "middle temporal gyrus (one cortical area)",
     'none stated; the source qualifies the value as types "that were spatially restricted", possibly a subset of the total'],
    ["Yao 2021", "11", "supertype (intermediate tier above clusters)",
     "mouse",
     'whole isocortex and hippocampal formation ("~1.3 million cells covering the entire adult mouse isocortex and HPF", study abstract)',
     "Sst Chodl (long-range projecting) kept as a separate group and excluded from the 11"],
]
COL_W = [12, 5, 16, 7, 20, 26]          # wrap width in characters, per column
COL_X = [0.00, 0.165, 0.235, 0.415, 0.505, 0.735]   # left edge, axes fraction

# (B) fraction of SOM cells classified as Martinotti cells, by definition
B_VALUES = [70.0, 54.0]                      # printed as "~70%" and "54 +/- 1%"
B_PRINTED = ["~70%", "54 \u00b1 1%"]
B_ERR = [None, 1.0]
B_LABELS = ["Axonal morphology\nV1 L2/3 + L5\n133/190 recovered cells",
            "Retrograde layer-1 label\nS1, all layers\nN = 17 (unit not stated)"]

# (C) SST share of cortical GABAergic neurons: one primary count, one review estimate
C_VALUES = [30.0, 30.0]
C_PRINTED = ["30% \u00b1 1.5", "~30%"]
C_ERR = [1.5, None]
C_LABELS = ["Primary count\nSst-Cre / GAD67-GFP\nmouse V1, all layers",
            "Review estimate\nno area or species in\nthe reporting sentence"]

# (D) structure-specific fractions, separate axes, never summed
D_CORTEX_BAND = (20.0, 30.0)                 # "Approximately 20-30% of GABA neurons"
D_STRIATUM_VALUES = [7.5, 7.6]
D_STRIATUM_LABELS = ["SST/NPY\nsubclass", "SST/NPY/DACH1\nsubclass"]

# ---

# -------------------------------------------------------------------- layout
fig = plt.figure(figsize=(7.09, 9.4))
gs = GridSpec(3, 2, figure=fig, height_ratios=[1.45, 1.0, 0.95],
              hspace=0.60, wspace=0.36)

axA = fig.add_subplot(gs[0, :])
axB = fig.add_subplot(gs[1, 0])
axC = fig.add_subplot(gs[1, 1])
axD1 = fig.add_subplot(gs[2, 0])
axD2 = fig.add_subplot(gs[2, 1])


def style_axis(ax, ylabel, ymax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_ylim(0, ymax)
    ax.set_ylabel(ylabel, fontsize=10)
    ax.tick_params(axis="x", length=0)


def panel_title(ax, text):
    ax.set_title(text, fontsize=10, fontweight="bold", loc="left", pad=6)


# ------------------------------------------------------------------ panel A
axA.axis("off")
panel_title(axA, "A   Number of SST groups reported by three classification schemes "
                 "\u2014 counts are not comparable units")
fig.canvas.draw()
a_height_in = axA.get_position().height * fig.get_figheight()
line_step = 1.32 * 8 / 72 / a_height_in      # one 8 pt text line, in axes fraction


y = 1.0
for x, h in zip(COL_X, TABLE_HEADER):
    axA.text(x, y, h, fontsize=8, fontweight="bold", va="top", ha="left",
             transform=axA.transAxes)
y -= 1.6 * line_step
axA.plot([0, 1], [y + 0.4 * line_step, y + 0.4 * line_step], color="black",
         lw=0.8, transform=axA.transAxes, clip_on=False)
for row in TABLE_ROWS:
    cells = [textwrap.fill(c, w) for c, w in zip(row, COL_W)]
    nlines = max(c.count("\n") + 1 for c in cells)
    for x, c in zip(COL_X, cells):
        axA.text(x, y, c, fontsize=8, va="top", ha="left",
                 transform=axA.transAxes,
                 fontweight="bold" if c in ("13", "11") else "normal")
    y -= (nlines + 0.7) * line_step
    axA.plot([0, 1], [y + 0.35 * line_step, y + 0.35 * line_step],
             color=COLORS["light_gray"], lw=0.6, transform=axA.transAxes,
             clip_on=False)

# ------------------------------------------------------------------ panel B
axB.bar([0, 1], B_VALUES, width=0.55, color=COLORS["sst"], edgecolor="black",
        linewidth=0.8)
axB.errorbar([1], [B_VALUES[1]], yerr=[B_ERR[1]], fmt="none", ecolor="black",
             elinewidth=1.0, capsize=4, capthick=1.0, linestyle="--")
for i, (v, p) in enumerate(zip(B_VALUES, B_PRINTED)):
    axB.text(i, v + 4, p, ha="center", fontsize=9, fontweight="bold")
axB.set_xticks([0, 1])
axB.set_xticklabels(B_LABELS, fontsize=8)
style_axis(axB, "SOM cells classified as\nMartinotti cells (%)", 108)
panel_title(axB, "B   Martinotti fraction by definition")
axB.text(0.99, 0.99, "error bar dashed:\ndispersion type and unit\nof replication not stated",
         transform=axB.transAxes, fontsize=8, ha="right", va="top",
         color=COLORS["neutral_gray"])

# ------------------------------------------------------------------ panel C
axC.bar([0], [C_VALUES[0]], width=0.55, color=COLORS["sst"], edgecolor="black",
        linewidth=0.8)
axC.errorbar([0], [C_VALUES[0]], yerr=[C_ERR[0]], fmt="none", ecolor="black",
             elinewidth=1.0, capsize=4, capthick=1.0, linestyle="--")
axC.bar([1], [C_VALUES[1]], width=0.55, facecolor="white",
        edgecolor=COLORS["neutral_gray"], linewidth=1.2, linestyle="--")
for i, (v, p) in enumerate(zip(C_VALUES, C_PRINTED)):
    axC.text(i, v + 2.2, p, ha="center", fontsize=9, fontweight="bold")
axC.text(1, C_VALUES[1] / 2, "review\nestimate", ha="center", va="center",
         fontsize=8, color=COLORS["neutral_gray"])
axC.set_xticks([0, 1])
axC.set_xticklabels(C_LABELS, fontsize=8)
style_axis(axC, "SST share of cortical\nGABAergic neurons (%)", 48)
panel_title(axC, "C   Primary count vs review estimate")

# ----------------------------------------------------------------- panel D-i
axD1.axhspan(D_CORTEX_BAND[0], D_CORTEX_BAND[1], xmin=0.12, xmax=0.88,
             facecolor=COLORS["sst"], alpha=0.25, edgecolor=COLORS["sst"],
             linewidth=1.2, linestyle="--")
axD1.text(0.5, sum(D_CORTEX_BAND) / 2, "20\u201330%", ha="center", va="center",
          fontsize=9, fontweight="bold")
axD1.set_xlim(0, 1)
axD1.set_xticks([])
style_axis(axD1, "SST+ share of cortical\nGABA neurons (%)", 35)
panel_title(axD1, "D (i)   Rodent neocortex")
axD1.text(0.5, 0.04, "review estimate, compiled\nimmunohistochemical counts, no n;\na reported range, not a point estimate",
          transform=axD1.transAxes, fontsize=8, ha="center", va="bottom",
          color=COLORS["neutral_gray"])

# ---------------------------------------------------------------- panel D-ii
axD2.bar([0, 1], D_STRIATUM_VALUES, width=0.5, color=COLORS["npy_nos"],
         edgecolor="black", linewidth=0.8)
for i, v in enumerate(D_STRIATUM_VALUES):
    axD2.text(i, v + 0.3, f"{v}%", ha="center", fontsize=9, fontweight="bold")
axD2.set_xticks([0, 1])
axD2.set_xticklabels(D_STRIATUM_LABELS, fontsize=8)
style_axis(axD2, "subclass share of striatal\ninterneuron nuclei (%)", 13)
panel_title(axD2, "D (ii)   Human dorsal striatum")
axD2.text(0.5, 0.97, "subclasses shown separately,\nnever summed — no summed value\nis reported by the source",
          transform=axD2.transAxes, fontsize=8, ha="center", va="top",
          color=COLORS["neutral_gray"])

fig.text(0.01, 0.004,
         "Heterogeneous comparison \u2014 values not pooled; every panel carries its own axis. "
         "Dashed bar or band outline = value taken from an abstract\nonly or from a review-level synthesis.",
         fontsize=8, ha="left", va="bottom", color=COLORS["neutral_gray"])

# ---

save_figure(fig, os.path.join(OUT_DIR, "fig_sec2_sst_taxonomy_and_subtype_fractions.png"))
print("saved", os.path.join(OUT_DIR, "fig_sec2_sst_taxonomy_and_subtype_fractions.png"))
```
:::

(sec-02-regional-variants)=

## Regional variants are different cells, not the same cell elsewhere

Hippocampal and striatal SST populations are not cortical Martinotti cells under another name. That distinction matters, because the cross-regional vulnerability comparison drawn in {ref}`sec-huntingtons` is a comparison between different cells.

Single-cell profiling of CA1 divides Sst- and Grm1-expressing stratum oriens cells into Npy/Ngf-positive hippocamposeptal clusters and Pnoc/Reln-positive, Npy-negative clusters identified with oriens-lacunosum moleculare (O-LM) cells {cite:p}`Harris2018`. Three-dimensional electron microscopy separates those two families by dendritic and synaptic architecture, with spine synapses systematically smaller than dendritic shaft synapses on both — 0.123 µm² against 0.141 µm² for glutamatergic inputs onto O-LM dendrites {cite:p}`Takacs2024`.

Functionally they diverge from the cortical scheme in two ways. The first is output compartment. Chrna2-Cre-defined O-LMα2 cells inhibit CA1 pyramidal cells chiefly at the distal apical dendrite {cite:p}`Leao2012`, whereas bistratified cells, also somatostatin-positive, innervate small pyramidal dendritic shafts co-aligned with the Schaffer collateral input {cite:p}`Klausberger2003`. In the dentate gyrus, SOM-positive hilar perforant-path-associated (HIPP) cells inhibit parvalbumin basket cells while rarely receiving reciprocal input from them — one study, so far unreplicated {cite:p}`Savanthrapadian2014`. The second is projection. Somatostatin- and mGluR1α-positive stratum oriens neurons project to subiculum, other cortical areas and the medial septum {cite:p}`Jinno2007`, and dentate SOM-positive axon collaterals run along the fimbria to the medial septum and diagonal band {cite:p}`Yuan2017`.

Long-range coordination extends beyond the hippocampal formation. Voltage imaging indicates that beta-frequency synchronisation between SST interneuron populations in ventral hippocampus and basolateral amygdala tracks anxiety-related behaviour {cite:p}`Jackson2024`.

The striatal population shares the marker and little else. Striatal persistent low-threshold-spiking interneurons are NADPH-diaphorase-positive, which was taken as evidence that they release nitric oxide {cite:p}`Kawaguchi1993`. In human dorsal striatum, single-nucleus profiling resolves transcriptomically defined nitrergic interneurons as SST/NPY and SST/NPY/DACH1 subclasses, accounting for 7.5% and 7.6% of striatal interneurons respectively {cite:p}`Garma2024`; the rodent physiological literature has not matched those subclasses cell for cell.

Their output inverts the dense cortical motif. Individual persistent low-threshold-spiking cells are weakly and sparsely connected, while fast-spiking interneurons carry the bulk of feedforward inhibition {cite:p}`Gittis2010`; paired recordings only rarely elicited inhibitory responses in spiny projection neurons from NPY-expressing persistent low-threshold-spiking cells {cite:p}`IbanezSandoval2011`. Beyond those sparse paired recordings, quantitative output connectivity for adult striatal cells of this class is unestablished, and so is its correspondence to the modern transcriptomic subclasses.

Cortex and striatum are not independent compartments either: motor-cortical SOM-positive corticostriatal neurons innervate direct-pathway, indirect-pathway and cholinergic striatal neurons at comparable rates (29%, 22% and 40%) {cite:p}`Melzer2017`, so SST-positive long-range axons link the two. A further nitrergic population complicates marker-based reasoning — deep-layer neocortical neurogliaform cells expressing Id2 and Nkx2.1, weakly immunoreactive for neuronal nitric oxide synthase, are selectively active during the non-REM down state {cite:p}`Valero2021`. The striatal SST/NPY/nitrergic class defined here is the population whose sparing is debated in {ref}`sec-huntingtons`.

(sec-02-input-output)=

## Input-output logic: dendritic targeting, disinhibition and recurrence

The motif the disease sections need is dendritic inhibition with a gain-control signature, and it is well supported:

- optical activation of SOM interneurons significantly reduced calcium signals in 57% (73/127) of randomly imaged pyramidal spines {cite:p}`Chiu2013`
- disynaptic inhibition between layer 5 pyramidal cells is mediated by Martinotti cells {cite:p}`Silberberg2007`
- silencing SOM interneurons in running mice increased the probability of CA1 pyramidal burst firing, from 45% more spike doublets to 280% more bursts of five or more spikes {cite:p}`Royer2012`

Two further properties fit a gain-control role. The lateral footprint of SST-mediated inhibition in V1 is broader than that of parvalbumin-mediated inhibition, which a circuit model, anatomical tracing and subthreshold measurements link to divisive and not subtractive control of contrast sensitivity {cite:p}`DelRosario2025`. The Martinotti-to-pyramidal synapse is pharmacologically distinguished by α5-containing GABA-A receptors, which those cells do not express at the other synapses they make {cite:p}`Donato2022`.

Output is not uniform across the class, however. Layer 4 SOM interneurons in barrel cortex connected to fast-spiking interneurons far more often than to principal neurons (62%, 37/60 versus 35%, 31/89) {cite:p}`Xu2013`. In the same preparation, reducing their activity increased layer 4 fast-spiking firing by 32.8% during up states — a disinhibitory role in place of a dendrite-gating one. Against that sits a reported 100% connection probability for layer 2/3 Sst cells onto nearby pyramids in V1, a value stated jointly for Pvalb and Sst cells and without a pair denominator {cite:p}`Pfeffer2013`.

Dense electron-microscopic reconstruction of mouse visual cortex reaches a compatible conclusion without molecular labels: inhibitory neurons show widespread target specificity, and groups with similar subclass-level targeting differ in which postsynaptic compartment they target — an organising principle for inhibitory connectivity that the authors describe as complementary to, but distinct from, cell types {cite:p}`SchneiderMizell2025`. In awake animals the class is state-dependent as well, with layer 2/3 SOM neurons of barrel cortex hyperpolarising and reducing firing during both passive and active whisker sensing while nearby cell types are excited {cite:p}`Gentet2012`.

Inputs onto SST cells are the second half of the motif. Three studies bear on VIP-mediated inhibition of the class:

- paired recordings in V1 layer 2/3 found VIP cells inhibiting Sst cells with a connection probability of 62.5%, against only about 12.5% onto pyramids {cite:p}`Pfeffer2013`
- inactivating VIP interneurons during motor cortex input reduced inhibition of SST interneurons by about half in barrel cortex {cite:p}`Lee2013`
- brief activation of the sparse VIP population changed firing rates in about 20% of cortical cells {cite:p}`Pi2013`

But the quantitative picture fragments, because the hit rate depends on the laminar motif. Approximately 40–45% of tested layer 4 SST cells were inhibited by layer 2/3 VIP cells in both somatosensory and visual cortex {cite:p}`Rachel2025`, whereas intralaminar layer 5 pairs gave 21.1% (15/71) for VIP-to-SST and a comparable 24.7% (18/73) for PV-to-SST {cite:p}`Preuss2025`. {numref}`fig-sec2-sst-connectivity-motif-disagreements` places each value beside the laminar scope it was measured in. These are different statistics as well as different motifs, and the second study reports its own translaminar rate as similar to its intralaminar one, so the gap is not evidence of a laminar gradient.

Connectivity also does not guarantee control. Chemogenetic silencing of CA1 VIP interneurons left excitatory input processing in superficial pyramidal cells unchanged at maximal stimulation intensity {cite:p}`Iloun2026`, set against that 40–45% hit rate {cite:p}`Rachel2025`. A measured synapse is not a measured function.

State modulation has been contested in the same way. Locomotion suppressed calcium responses of V1 SST cells in one study {cite:p}`Fu2014` and generally increased their baseline activity in another {cite:p}`Dipoppa2018`; the later work attributes the sign difference to visual condition and not to the cells. In-situ-transcriptomic recording resolves the class further still, with *Sst Tac1* cells most active during synchronised states and *Sst Reln* cells more active during running — a subtype-level dissociation reported once and not yet replicated {cite:p}`Bugeon2022`.

Additional control layers continue to be added on top of the motif:

- NDNF-expressing layer 1 interneurons are reported to suppress SOM interneuron output in a layer-specific manner in auditory cortex, on the strength of a single report {cite:p}`Naumann2025`
- GABA-B receptor activation reduced spontaneous SST interneuron firing by 60% {cite:p}`Kanigowski2023`
- GABAergic synapses onto CA1 SST and PV interneurons differ in integrin-dependent modulation {cite:p}`Brzdak2023`
- theta-patterned stimulation of pyramidal axons potentiates excitatory input onto O-LM interneurons to 144 ± 15% of control {cite:p}`Sammari2022`
- associative learning produces a durable, target-specific reduction of SST output that depends on stimulus–reward contingency instead of stimulus exposure {cite:p}`Park2025`

These last results are single studies; their direction matters more than their magnitude for now. Dendritic targeting and the VIP–SST–PV motif are the mechanism by which SST dysfunction becomes an oscillatory and mnemonic phenotype in {ref}`sec-circuit-consequences`.

:::{admonition} Evidence conflict: do SST cells inhibit each other?
:class: warning
Paired recordings in mouse V1 reported more similarities than differences between layer 2/3 and layer 5 inhibitory networks, including a comparable *lack* of Sst-to-Sst and Pvalb-to-Sst connections in both {cite:p}`Pfeffer2013`. Large-scale multipatch recordings in mouse and human neocortex explicitly contradict this, observing connections between Sst neurons in every layer {cite:p}`Campagnola2022`. The candidate explanations are measurement scale, detection sensitivity and driver-line specificity rather than biology — the larger survey probed far more pairs — though none has been tested directly, and the subtype-resolved confirmation of these connections rests on a small number of probed pairs, a count carried by no quoted sentence from that study, so a subtype-resolved recurrent-connectivity estimate at scale remains unavailable. Functional evidence favours some recurrent inhibition, since the increase in cooperative recruitment among SOM cells was significantly reduced to 16 ± 7% under GABA receptor blockade {cite:p}`Karnani2016`. The conflict is unresolved, and it is consequential: whether the class can disinhibit itself changes the predicted network effect of losing part of it.
:::

:::{figure} ../figures/fig_sec2_sst_connectivity_motif_disagreements.png
:name: fig-sec2-sst-connectivity-motif-disagreements
:width: 100%
**Connection probabilities with their scope attached.** Each sub-panel carries its own axis; values are never pooled and no difference between sub-panels is annotated or implied. (A) SST output onto local excitatory targets, reported separately for two presynaptic populations {cite:p}`Pfeffer2013, Xu2013`. In the layer 4 source the excitatory target is the minority pathway: layer 4 SOM interneurons there target mainly fast-spiking interneurons, and it is layer 2/3 SOM interneurons in that study that target mainly pyramidal cells. The two values are not two estimates of one connection probability: layer 2/3 Sst cells onto local pyramidal neurons in V1 versus layer 4 SOM interneurons, a predominantly non-Martinotti population whose axons stay within layer 4, onto layer 4 principal neurons in S1. The 100% value carries no reported pair denominator and is stated in its source jointly for Pvalb and Sst cells; the 35% value is 31 of 89 tested pairs. The absence of an error bar on the former is not a statement of precision. The inter-somatic distance window is specified for one entry and unreported for the other; connection probability falls steeply with distance, so part of any apparent gap is a sampling-window artefact. Only the SOM-to-principal-neuron value (35%) is plotted from Xu 2013; that study's SOM-to-fast-spiking-interneuron value is a different postsynaptic population and is not shown. Area and layer differ together (V1 layer 2/3 versus S1 layer 4); the comparison cannot separate areal from laminar effects. The two values are shown on separate axes and are not two values of one measured quantity. (B) Inhibitory input onto SST cells, grouped by laminar motif {cite:p}`Rachel2025, Preuss2025`. The two values are different connectivity motifs: translaminar layer 2/3 VIP onto layer 4 SST cells (reported for both S1 and V1) versus intralaminar layer 5 VIP onto layer 5 SST cells in S1. The 40–45% figure is a range reported across two cortical areas, not a single pooled fraction, and no tested-pair denominator is given; the 21.1% figure is 15 of 71 tested pairs. The layer 4 SST cells behind the 40–45% value are morphologically heterogeneous by the source study's own account (non-Martinotti in S1, Martinotti-like in V1) and are pooled in that single value. The difference between the two values must not be read as a laminar gradient in VIP-to-SST connectivity: the layer 5 study reports that its own translaminar layer 2/3 VIP to layer 5 SST rate is similar to its intralaminar rate. The two values are also different statistics: a per-cell hit rate versus a per-pair connection rate. The layer 5 PV-to-SST value (24.7%, 18/73) is a within-study reference from the same source sentence, not a cross-study comparator. Dashed edges mark values taken from abstracts only.
:::

:::{dropdown} 📓 Figure code
```python
# Figure: SST connectivity motifs, each value with its own axis (section 02).
# Separate sub-panels, separate axes, no shared probability scale, no bracket
# and no cross-panel difference annotation. Every number is quoted verbatim
# from its own source sentence.
import os, sys

NB_DIR = os.path.abspath("figures/notebooks") if os.path.isdir("figures/notebooks") else os.path.abspath(".")
sys.path.insert(0, NB_DIR)
OUT_DIR = os.path.abspath(os.path.join(NB_DIR, ".."))

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from shared_style import COLORS, apply_style, save_figure

apply_style()

# ---

# ---------------------------------------------------------------- panel data
# (A i) L2/3 Sst-Cre cells -> local pyramidal neurons: a ceiling value with no
# reported pair denominator, stated in its source jointly for Pvalb and Sst
# cells. Rendered as a labelled text annotation, never as a bar on a shared
# probability axis.
A1_VALUE_TEXT = "100%"
A1_NOTES = ["denominator not reported",
            "stated jointly for Pvalb and Sst cells",
            "ceiling value, precision unknown",
            "distance window specified in the source",
            "but not reproduced here as a number"]

# (A ii) L4 SOM interneurons -> L4 principal neurons
A2_VALUE = 35.0
A2_PRINTED = "35%"
A2_DENOM = "31/89 tested pairs"
A2_LABEL = ("L4 SOM INs (non-Martinotti,\naxons remain in L4) \u2192 L4 principal\n"
            "neurons incl. spiny stellate, mouse S1\nno distance window reported")

# (B i) translaminar L2/3 VIP -> L4 SST: a range across two areas, per-cell hit rate
B1_BAND = (40.0, 45.0)
B1_PRINTED = "40\u201345%"

# (B ii) intralaminar L5 pairs, per-pair connection rates from one sentence
B2_VALUES = [21.1, 24.7]
B2_PRINTED = ["21.1%", "24.7%"]
B2_DENOM = ["15/71 tested pairs", "18/73 tested pairs"]
B2_LABELS = ["L5 VIP \u2192 L5 SST\nS1, per-pair rate",
             "L5 PV \u2192 L5 SST\nS1, within-study reference"]
B2_COLORS = [COLORS["vip"], COLORS["pv"]]

# ---

# -------------------------------------------------------------------- layout
fig = plt.figure(figsize=(7.09, 7.0))
gs = GridSpec(2, 2, figure=fig, height_ratios=[1.0, 1.0], hspace=0.95,
              wspace=0.36)
axA1 = fig.add_subplot(gs[0, 0])
axA2 = fig.add_subplot(gs[0, 1])
axB1 = fig.add_subplot(gs[1, 0])
axB2 = fig.add_subplot(gs[1, 1])


def style_axis(ax, ylabel, ymax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_ylim(0, ymax)
    ax.set_ylabel(ylabel, fontsize=10)
    ax.tick_params(axis="x", length=0)


def panel_title(ax, text):
    ax.set_title(text, fontsize=10, fontweight="bold", loc="left", pad=6)


# ----------------------------------------------------------------- panel A-i
axA1.axis("off")
panel_title(axA1, "A (i)   V1 L2/3 Sst-Cre \u2192 local pyramids")
axA1.text(0.5, 0.74, A1_VALUE_TEXT, ha="center", va="center", fontsize=22,
          fontweight="bold", color=COLORS["sst"], transform=axA1.transAxes)
axA1.text(0.5, 0.50, "connection probability reported\nfor local pyramidal targets",
          ha="center", va="center", fontsize=8, transform=axA1.transAxes)
axA1.text(0.5, 0.30, "\n".join(A1_NOTES), ha="center", va="top", fontsize=8,
          color=COLORS["neutral_gray"], transform=axA1.transAxes)
axA1.text(0.5, 0.95, "no numeric axis \u2014 not comparable with (A ii)",
          ha="center", va="top", fontsize=8, style="italic",
          color=COLORS["neutral_gray"], transform=axA1.transAxes)

# ---------------------------------------------------------------- panel A-ii
axA2.bar([0], [A2_VALUE], width=0.45, color=COLORS["sst"], edgecolor="black",
         linewidth=0.8)
axA2.text(0, A2_VALUE + 8.0, A2_PRINTED, ha="center", fontsize=9,
          fontweight="bold")
axA2.text(0, A2_VALUE + 2.0, A2_DENOM, ha="center", fontsize=8)
axA2.set_xticks([0])
axA2.set_xticklabels([A2_LABEL], fontsize=8)
axA2.set_xlim(-0.6, 0.6)
style_axis(axA2, "connections / tested pairs (%)", 50)
panel_title(axA2, "A (ii)   S1 L4 SOM INs \u2192 L4 principal")
axA2.text(0.02, 0.96, "own axis; not a second\nestimate of (A i)", ha="left",
          va="top", fontsize=8, color=COLORS["neutral_gray"],
          transform=axA2.transAxes)

# ----------------------------------------------------------------- panel B-i
axB1.axhspan(B1_BAND[0], B1_BAND[1], xmin=0.12, xmax=0.88,
             facecolor=COLORS["vip"], alpha=0.30, edgecolor=COLORS["vip"],
             linewidth=1.2, linestyle="--")
axB1.text(0.5, sum(B1_BAND) / 2, B1_PRINTED, ha="center", va="center",
          fontsize=9, fontweight="bold")
axB1.set_xlim(0, 1)
axB1.set_xticks([])
style_axis(axB1, "tested L4 SST cells inhibited\nby L2/3 VIP cells (%)", 55)
panel_title(axB1, "B (i)   Translaminar: L2/3 VIP \u2192 L4 SST")
axB1.text(0.5, 0.05,
          "range across S1 and V1,\nnot a pooled fraction;\n"
          "denominator not reported;\nper-cell hit rate;\n"
          "L4 SST cells pooled across\nnon-Martinotti (S1) and\nMartinotti-like (V1) cells",
          transform=axB1.transAxes, fontsize=8, ha="center", va="bottom",
          color=COLORS["neutral_gray"])

# ---------------------------------------------------------------- panel B-ii
bars = axB2.bar([0, 1], B2_VALUES, width=0.5, color=B2_COLORS,
                edgecolor="black", linewidth=0.8)
bars[1].set_hatch("//")
for i, (v, p, dn) in enumerate(zip(B2_VALUES, B2_PRINTED, B2_DENOM)):
    axB2.text(i, v + 8.0, p, ha="center", fontsize=9, fontweight="bold")
    axB2.text(i, v + 2.0, dn, ha="center", fontsize=8)
axB2.set_xticks([0, 1])
axB2.set_xticklabels(B2_LABELS, fontsize=8)
style_axis(axB2, "connections / tested pairs (%)", 55)
panel_title(axB2, "B (ii)   Intralaminar: L5 \u2192 L5 SST")
axB2.text(0.5, 0.96, "both values from one source sentence;\nhatched bar is a within-study reference",
          transform=axB2.transAxes, fontsize=8, ha="center", va="top",
          color=COLORS["neutral_gray"])

fig.text(0.01, 0.004,
         "Separate axes throughout; values are not pooled and no difference between sub-panels is annotated or implied.\n"
         "Dashed band outline = value taken from an abstract only.",
         fontsize=8, ha="left", va="bottom", color=COLORS["neutral_gray"])

# ---

save_figure(fig, os.path.join(OUT_DIR, "fig_sec2_sst_connectivity_motif_disagreements.png"))
print("saved", os.path.join(OUT_DIR, "fig_sec2_sst_connectivity_motif_disagreements.png"))
```
:::

(sec-02-peptide)=

## Somatostatin as a transmitter: processing, release and SSTR1-SSTR5 signalling

Somatostatin is a diffusible neuromodulator as well as a cell-identity marker, so the peptide deserves treatment as a signal in its own right.

All five receptors are described as sharing Gαi-dependent inhibition of adenylyl cyclase, with SSTR5 additionally engaging protein tyrosine phosphatases, MAPK and cytosolic calcium and potassium signalling {cite:p}`Gunther2018` — a review-level account, with no primary measurement standing behind the pan-receptor claim. Two primary results sit under the receptor pharmacology proper. Cloned SSTR1 and SSTR2 expressed in Chinese hamster ovary cells bind somatostatin-14 with apparently higher affinity than somatostatin-28 {cite:p}`Yamada1992`. Structure-guided mutagenesis of the SSTR2 ligand-binding pocket shows that disrupting an intramolecular bridge leaves less than 20% inhibition of cAMP production where wild-type receptor inhibition is complete {cite:p}`Heo2022`. Receptor subtypes are also described as influencing one another when co-expressed in the same cell, with SSTR5 affecting SSTR2 internalisation and trafficking — again a review-level statement and not a primary measurement {cite:p}`Lin2013`.

Cellular recordings put that signalling onto identified neurons:

- both somatostatin-28 and somatostatin-14 elicit a steady outward current in CA1 pyramidal neurons by selectively augmenting the M-current {cite:p}`Moore1988`
- pharmacological SSTR activation hyperpolarises layer 2/3 prelimbic pyramidal neurons, recapitulating optogenetic recruitment of SST interneurons {cite:p}`Brockway2023`
- selective SSTR4 agonism augmented the M-current in layer V pyramidal neurons (p = 0.016) but not in interneurons (p = 0.53) or layer II–IV pyramidal neurons (p = 0.56), a cell-type specificity that one study reports and none has yet replicated {cite:p}`Kecskes2020`

Peptidergic and GABAergic output are mechanistically separable. Somatostatin depresses glutamatergic transmission presynaptically, while its postsynaptic effects are pronounced in pyramidal cells and little to absent in SST interneurons and layer 1 interneurons {cite:p}`Riedemann2024`.

In human cortex the substrate exists. *SST*, *SSTR1* and *SSTR2* are among the most highly expressed interneuron neuropeptide–receptor transcript pairs in prefrontal cortex {cite:p}`Zhong2022`, and a humanised SSTR4 reporter line maps human promoter-driven expression onto defined forebrain populations {cite:p}`Nemes2021`.

Receptor-level pharmacology nonetheless remains thin. Newly characterised small-molecule SSTR4 agonists showed efficacies and potencies merely comparable to the established reference compound {cite:p}`Biskup2026`. In *Sstr2*-null mice, intrahippocampal kainate produced a 52% reduction in EEG ictal activity relative to wild-type littermates — a single result now more than two decades old and still unreplicated {cite:p}`Moneta2002`. The receptor pharmacology summarised here is the target rationale examined in {ref}`sec-therapeutics`, and the peptide-processing account feeds the somatostatin–neprilysin–amyloid axis in {ref}`sec-alzheimers`.

Three load-bearing links in that account are, however, not established, and {numref}`fig-sec2-sst-peptide-and-sstr-signalling` draws them as such.

First, no primary study directly measures prosomatostatin processing into somatostatin-14 and somatostatin-28, or activity-dependent peptide release from identified cortical or hippocampal SST interneurons. What stands in their place is four results of a different kind:

- an assay for inducing and inhibiting somatostatin release from prefrontal slices under optogenetic stimulation {cite:p}`Dao2019`
- light-triggered release of somatostatin-14 from implanted nanovesicles read out by near-infrared receptor-based sensing, which showed reduced but synchronised transmission within 130 µm and markedly smaller, delayed transmission at longer distances {cite:p}`Xiong2022`
- direct nanosampling of extracellular fluid detecting somatostatin among the prominent cortical prohormone-derived peptides, in a preparation whose neuropeptide concentrations lie in the nanomolar-to-picomolar range {cite:p}`Li2025`
- genetically encoded sensors able to detect peptide binding at nanomolar concentrations {cite:p}`Wang2023b`

All four are exogenous release, bulk stimulation or detection-capability results instead of measurements of endogenous release during behaviour, so the dose and spatial range of physiological somatostatin signalling remain unestablished.

Second, SSTR1–SSTR5 have not been mapped onto identified postsynaptic cell types — pyramidal versus PV versus VIP — by transcriptomics or immunohistochemistry, a gap that sits directly beneath every subtype-selective therapeutic proposal.

Third, the co-release of somatostatin with GABA from the same terminals is widely repeated and appears here only as a review-level assertion {cite:p}`Gunther2018`. The primary demonstration at identified synapses, with separable time courses, is missing, and what it would settle is consequential: whether the peptide and the transmitter are co-packaged determines whether peptidergic signalling tracks fast inhibition or operates as an independent, activity-threshold-gated channel.

:::{figure} ../figures/fig_sec2_sst_peptide_and_sstr_signalling.png
:name: fig-sec2-sst-peptide-and-sstr-signalling
:width: 100%
**Somatostatin signalling and its evidential status.** Schematic of prosomatostatin processing to somatostatin-14 and somatostatin-28, peptide release from an SST interneuron, SSTR1–SSTR5 on postsynaptic partners, Gαi coupling and the downstream effectors. Line style encodes what supports each step rather than its importance: solid for links with a primary measurement in the literature cited here — somatostatin-14 and somatostatin-28 binding at cloned SSTR1 and SSTR2 {cite:p}`Yamada1992`, Gi-mediated inhibition of cAMP production at SSTR2 {cite:p}`Heo2022`, M-current augmentation in CA1 pyramidal neurons {cite:p}`Moore1988` and in layer V pyramidal neurons under selective SST4 agonism {cite:p}`Kecskes2020`, hyperpolarisation of layer 2/3 pyramidal neurons by SSTR activation {cite:p}`Brockway2023`, presynaptic depression of glutamatergic transmission {cite:p}`Riedemann2024`, an assay demonstrating the induction and inhibition of somatostatin release in prefrontal slices {cite:p}`Dao2019`, and synchronised transmission within 130 µm after light-triggered release of somatostatin-14 {cite:p}`Xiong2022`; dashed for steps found only as review-level assertions, namely Gαi-dependent inhibition of adenylyl cyclase common to all five receptors and co-release of somatostatin with GABA {cite:p}`Gunther2018`; dotted and marked with a question mark for links with no primary evidence retrieved here — prosomatostatin processing in these neurons, activity-dependent peptide release from identified SST interneurons under physiological firing, and the cell-type-resolved distribution of SSTR1–SSTR5 across pyramidal, PV and VIP targets. The neprilysin branch is drawn dotted because no primary evidence for it is presented in this section; it is developed in {ref}`sec-alzheimers`. No quantity in this diagram is a measurement except the labelled distance, which is quoted from its source.
:::

:::{dropdown} 📓 Figure code
```python
# Figure: somatostatin signalling with the evidential status of each step
# (section 02). Line style encodes what supports each arrow:
#   solid  - a primary measurement exists in the literature cited here
#   dashed - the step appears only as a review-level assertion
#   dotted - no primary evidence was retrieved for this step (marked ?)
# The only numeral in the diagram is quoted verbatim from its source sentence.
import os, sys

NB_DIR = os.path.abspath("figures/notebooks") if os.path.isdir("figures/notebooks") else os.path.abspath(".")
sys.path.insert(0, NB_DIR)
OUT_DIR = os.path.abspath(os.path.join(NB_DIR, ".."))

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.lines import Line2D
from shared_style import COLORS, apply_style, save_figure

apply_style()

# ---

SOLID, DASHED, DOTTED = "-", (0, (4, 2.0)), (0, (1.4, 2.2))

# key: (x, y, w, h, text, facecolor)
BOXES = {
    "pro":  (0.02, 0.80, 0.24, 0.12, "Prosomatostatin\n(Sst / SST transcript)", "#E8EEF4"),
    "pept": (0.02, 0.60, 0.24, 0.12, "Somatostatin-14\nSomatostatin-28", "#E8EEF4"),
    "cell": (0.02, 0.34, 0.24, 0.17, "SST interneuron\ndense-core vesicles\n+ GABA vesicles", "#CFE2F0"),
    "ecs":  (0.38, 0.62, 0.27, 0.16, "Extracellular space\nvolume transmission:\nsynchronised within\n130 \u00b5m of release", "#F2F2F2"),
    "rec":  (0.70, 0.73, 0.29, 0.14, "SSTR1\u2013SSTR5\nG\u03b1i-coupled receptors", "#DDEDE5"),
    "ac":   (0.33, 0.80, 0.30, 0.10, "\u2193 adenylyl cyclase / cAMP\ncommon to all five receptors", "#F6F6F0"),
    "eff":  (0.70, 0.19, 0.29, 0.29, "Effectors measured directly\nGi-mediated cAMP inhibition\nat SSTR2\n"
            "\u2191 M-current (CA1 and layer 5\npyramidal cells)\nhyperpolarisation of L2/3\n"
            "pyramidal cells\npresynaptic depression of\nglutamate release", "#DDEDE5"),
    "targ": (0.38, 0.33, 0.27, 0.16, "Postsynaptic partners\npyramidal / PV / VIP\nwhich receptor sits\non which cell?", "#F2F2F2"),
    "nep":  (0.70, 0.03, 0.29, 0.12, "Neprilysin / amyloid axis\n(developed later in\nthe review)", "#FFFFFF"),
    "gaba": (0.38, 0.05, 0.27, 0.12, "Fast GABAergic output\nonto distal dendrites", "#CFE2F0"),
}

# (start, start_side, end, end_side, linestyle, question_mark)
ARROWS = [
    ("pro", "b", "pept", "t", DOTTED, True),
    ("pept", "b", "cell", "t", SOLID, False),
    ("cell", "r", "ecs", "l", DOTTED, True),
    ("ecs", "r", "rec", "l", SOLID, False),
    ("rec", "l", "ac", "r", DASHED, False),
    ("rec", "b", "eff", "t", SOLID, False),
    ("rec", "b", "targ", "r", DOTTED, True),
    ("cell", "b", "gaba", "l", SOLID, False),
    ("gaba", "t", "targ", "b", DASHED, False),
    ("eff", "b", "nep", "t", DOTTED, True),
]

# label text placed in free space, with its own anchor
LABELS = [
    (0.265, 0.740, "left", "center", "processing\nnot measured"),
    (0.290, 0.500, "center", "center", "release\nnot measured"),
    (0.845, 0.915, "center", "center", "binding at cloned SSTR1 / SSTR2"),
    (0.800, 0.545, "center", "center", "cell-type-resolved receptor\nmap: not retrieved"),
    (0.515, 0.245, "center", "center", "co-release with GABA:\nreview-level assertion only"),
]

# ---

def anchor(key, side):
    x, y, w, h, *_ = BOXES[key]
    return {"r": (x + w, y + h / 2), "l": (x, y + h / 2),
            "t": (x + w / 2, y + h), "b": (x + w / 2, y),
            "c": (x + w / 2, y + h / 2)}[side]


fig, ax = plt.subplots(figsize=(7.09, 6.2))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

for key, (x, y, w, h, text, fc) in BOXES.items():
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0.004,rounding_size=0.010",
                                linewidth=0.9, edgecolor=COLORS["neutral_gray"],
                                facecolor=fc, zorder=2))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=8,
            zorder=3)

for a, sa, b, sb, style, mark in ARROWS:
    p0, p1 = anchor(a, sa), anchor(b, sb)
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=11,
                                 linewidth=1.1, linestyle=style, color="black",
                                 shrinkA=1, shrinkB=3, zorder=4))
    if mark:
        mx, my = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
        ax.text(mx + 0.016, my + 0.016, "?", fontsize=11, fontweight="bold",
                ha="center", va="center", color=COLORS["primary_red"],
                zorder=6,
                bbox=dict(boxstyle="circle,pad=0.08", facecolor="white",
                          edgecolor="none"))

for x, y, ha, va, text in LABELS:
    ax.text(x, y, text, fontsize=8, ha=ha, va=va, color=COLORS["neutral_gray"],
            bbox=dict(boxstyle="round,pad=0.20", facecolor="white",
                      edgecolor="none"), zorder=5)

legend_handles = [
    Line2D([0], [0], color="black", linestyle=SOLID, lw=1.1,
           label="primary measurement in the cited literature"),
    Line2D([0], [0], color="black", linestyle=DASHED, lw=1.1,
           label="review-level assertion only"),
    Line2D([0], [0], color="black", linestyle=DOTTED, lw=1.1,
           label="no primary evidence retrieved (marked ?)"),
]
ax.legend(handles=legend_handles, loc="upper center",
          bbox_to_anchor=(0.5, 1.07), ncol=3, frameon=False, fontsize=8,
          handlelength=2.4, columnspacing=1.2)
ax.text(0.145, 0.955, "Line style encodes evidential status, not strength of effect.",
        fontsize=8, style="italic", color=COLORS["neutral_gray"], ha="center")

# ---

save_figure(fig, os.path.join(OUT_DIR, "fig_sec2_sst_peptide_and_sstr_signalling.png"))
print("saved", os.path.join(OUT_DIR, "fig_sec2_sst_peptide_and_sstr_signalling.png"))
```
:::

(sec-02-toolbox)=

## What the genetic toolbox actually reports

Every rodent cell count in the sections that follow is bounded by what its driver line reports. Three-dimensional mapping of genetically identified interneurons through the caudoputamen found no significant anteroposterior density gradient for SST cells (β = 4.9, p = 0.66) where parvalbumin cells showed a strong one (β = −146.2, p = 3.0 × 10⁻¹⁷) {cite:p}`Muhsinov2026`. In the same dataset, SST-immunonegative tdTomato-positive clusters in ventral striatum forced the exclusion of an entire region from the analysis.

Both reported failure modes run in the same direction — cells the reporter counts as SST that are not SST, whether by immunoreactivity or by physiology. Sst-IRES-Cre also labels some Pvalb-like fast-spiking cells, a confound invoked to explain why large multipatch surveys detect Sst-to-Sst connections that an earlier paired-recording survey of mouse V1 did not {cite:p}`Campagnola2022, Pfeffer2013`. Whether these lines additionally miss SST cells is unresolved. A percentage for the parvalbumin-expressing fraction that Sst-Cre labels travels with the same study that supplies the 30% denominator, but it is attached to no quoted measurement and is therefore not reproduced here, and no independent quantification of non-SST labelling is available. The practical consequence is a measurement-validity problem and not a biological one.

:::{admonition} Evidence conflict: is Cre-reporter density a valid proxy for SST interneuron number?
:class: warning
One study treats a reduced density of eGFP-labelled SST cells as a change in the SST population while finding no accompanying death or oxidative-stress signal in those same cells: the proportion of eGFP-positive cells that were 3-nitrotyrosine-positive did not differ between genotypes (p = 0.9684), and no colocalisation of eGFP with cleaved caspase-3 was observed {cite:p}`Drake2024`. The other reports SST-immunonegative tdTomato-positive cells in SST-Cre tissue, in numbers that forced an entire region to be excluded from the analysis before a genetically defined SST distribution could be described {cite:p}`Muhsinov2026`. Stated side by side, the two disagree on whether reporter-positive density reports SST interneuron number at all — a disagreement about what was counted rather than about the biology, and one that is unresolved. Every reporter-based cell count in the disease sections inherits it.
:::

Resolving that requires tools designed for it, and they exist: the intersectional, retrograde-tracing and layer-1-targeting transgenic strategies already described above {cite:p}`Wu2023, Hostetler2023, Ma2006`, together with Patch-seq or in-situ transcriptomic recording, which assigns a recorded cell to a transcriptomic type in place of a marker class {cite:p}`Scala2019, Bugeon2022`. None of these was used in the older disease literature, and several are rarely used in the current one.

Two limits of the evidence behind this section should be read into everything above. The first is coverage: a single full-text index, no citation chasing, and of the 72 papers cited here depth recorded for 70 — 45 in full text and 25 as abstracts only. Statements of absence above, and every call of a result as unreplicated, are bounded by that coverage and are not claims that no such work exists. The second is the shape of the disconfirming evidence. Published null results are sparse here: the disconfirming material reports preserved, unchanged or non-significant outcomes instead of failed replications of a specific connectivity or receptor claim, and the targeted searches for contradictions were capped and not exhaustive. The apparent consistency of the identity literature may therefore partly reflect what gets published. These bounds on Cre-line fidelity and on coverage reappear as a general constraint on rodent cell counts in {ref}`sec-conflicts-limitations`.

Taken together, the SST label aggregates cells that differ in axonal target, postsynaptic partner, co-marker composition, developmental identity and state modulation, and it is read out by tools that count cells the marker itself does not confirm. Whether that aggregate is selectively vulnerable in neurodegenerative disease is the next question — and in {ref}`sec-selective-vulnerability` the aggregation itself turns out to be part of why the claim is hard to test.

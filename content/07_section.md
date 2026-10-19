(sec-als-ftd)=

# ALS, Frontotemporal Dementia, and Other Neurodegenerative Conditions

Striatal interneurons in Huntington's disease are numerically preserved and functionally abnormal, as {ref}`sec-huntingtons` showed; the measurement problem there is that cell counts and peptide content disagree. In amyotrophic lateral sclerosis (ALS) and frontotemporal lobar degeneration (FTLD) the evidential problem inverts. Cortical inhibition is measured in living patients more directly than in most conditions covered here, and the deficit it reveals is one of the most consistently reproduced findings in ALS neurophysiology {cite:p}`Higashihara2024, VanDenBos2024`.

But the cell class this review is about is barely measured in human tissue at all, and the mechanistic account that gives it a leading role rests on one mouse study {cite:p}`Zhang2016`. What follows separates the physiology, which is strong, from the cellular attribution, which is an inference carried by PV counts and, for SST, by that single mouse study.

(sec-07-als-disinhibition)=

## Cortical disinhibition in ALS: robust at the group level, heterogeneous within cohorts

Short-interval intracortical inhibition (SICI), the paired-pulse transcranial magnetic stimulation (TMS) index of GABA-A-mediated cortical inhibition, is reduced in ALS across cohorts and techniques {cite:p}`Higashihara2024, Geevasinga2015`. The deficit survives a change of recording platform: a TMS–electroencephalography paired-pulse analogue shows it in place of the conventional motor-evoked-potential measure {cite:p}`VanDenBos2024`.

{cite:t}`Higashihara2024` pooled threshold-tracking TMS studies and reported a standardised mean difference of −0.99 (95% CI −1.12 to −0.87, p < 0.001) with moderate heterogeneity (I² = 40%) — a pooled meta-analytic estimate over 25 separate threshold-tracking studies. {cite:t}`Geevasinga2015` supplies the single-cohort anatomy of that effect:

- mean SICI was 1.2% in C9orf72 familial ALS and 1.6% in sporadic ALS, against 11.8% in healthy controls
- asymptomatic C9orf72 expansion carriers sat at 10.2% and did not differ from controls (P = .20)

Inhibitory failure therefore arrives after symptom onset and not before it. Paired-pulse TMS combined with electroencephalography reproduces the deficit at the level of evoked cortical potentials, and the deficit scales with disease duration (P60, P < 0.01; N100, P < 0.005; r = −0.698 for the N100 correlation) {cite:p}`VanDenBos2024`.

The reduction is not uniform, however. It is absent in a pyramidal phenotype group {cite:p}`Tankisi2025`, and cohorts that stratify patients split them into hyperexcitable, normally excitable and cortically inexcitable groups {cite:p}`Pavey2024`. Two further results qualify the picture without contradicting it. {cite:t}`Tankisi2025` found SICI reduced at all interstimulus intervals in bulbar-onset patients but normal in a pyramidal phenotype group (n = 12 pyramidal, n = 20 classic). {cite:t}`McMackin2026` found no ALS-versus-control difference in long-interval intracortical inhibition (LICI), the GABA-B-mediated measure (Hedge's g ≤ 0.14, P ≥ 0.44), a result that stands in tension with the SICI literature and is treated as contested.

Cortical disinhibition in ALS is therefore specific to a GABA-A circuit, undetectable in the one asymptomatic C9orf72 expansion carrier group that has been measured (n = 11), and phenotype-dependent, as {numref}`fig-sec7-cortical-inhibition-across-als-cohorts` lays out with each entry on its own units. The presymptomatic rodent evidence discussed below points the other way.

:::{admonition} Evidence Conflict
:class: warning
{cite:t}`Higashihara2024` present reduced intracortical inhibition as the most sensitive group-level TMS signature of ALS on the strength of a pooled estimate, an aggregate sensitivity rather than a claim about every individual patient, whereas {cite:t}`Pavey2024` phenotyped 417 patients with the same technique and found cortical hyperexcitability in 210 (50.3%), frank cortical inexcitability in 110 (26.4%) and normal excitability in 97 (23.3%). The disagreement is between a pooled mean effect and a within-cohort distribution, and it bears directly on whether GABAergic interneuron failure is a disease-wide or a subgroup phenomenon. It is partially resolved: a large mean reduction and a bimodal cohort are arithmetically compatible, because the cortically inexcitable quarter contributes no SICI value at all rather than a normal one. What would settle it — a longitudinal within-patient study tracking transition between excitability phenotypes — has not been reported in the material retrieved here, and no primary data reconciling the pooled estimate with the distribution were found.
:::

The same measures in frontotemporal degeneration are pharmacological instead of purely observational, and they carry the strongest interventional evidence in this section for a GABAergic contribution to a cortical physiological index in these dementias. Three findings line up:

- magnetic resonance spectroscopy shows reduced GABA in right inferior frontal cortex but not occipital cortex in behavioural-variant frontotemporal dementia (bvFTD) and progressive supranuclear palsy, with the frontal GABA and glutamate deficits tracking failures of response inhibition (F(1) = 8.67, P = 0.005; occipital P = 0.81) {cite:p}`Murley2020`
- enhancing GABA with tiagabine normalises task-related beta power in the same region {cite:p}`Hughes2025`
- generative modelling of magnetoencephalography, recorded under an auditory oddball paradigm and not the response-inhibition task, infers increased tonic inhibition of deep inhibitory populations {cite:p}`Adams2021`

Two limits sit on that alignment. The drug effect is on the cortical physiological index, not a reversal of the behavioural deficit. And the modelling inference needs a caveat the source itself implies: the inhibitory "populations" of a dynamic causal model are model parameters, not counted cells, and no interneuron is measured by that method.

Reviews that assemble this material around PV interneuron dysfunction as the shared substrate of cortical hyperexcitability across dementias {cite:p}`Smeralda2024` restate a hypothesis, not a measurement. The cerebrospinal fluid peptide literature is correspondingly fragile. Somatostatin and NPY correlate with each other in FTD (n = 22) but not in Alzheimer's disease (n = 34) (p < 0.02) {cite:p}`Minthon1997`. And CSF somatostatin in demented patients rises over three months of an activating care programme {cite:p}`WiderloV1989`, which makes it a state-dependent measure and not a fixed index of interneuron integrity — a point developed in {ref}`sec-human-evidence`.

Rodent work supplies the causal arrow that human recordings cannot. In late pre-symptomatic SOD1-G93A mice, chemogenetically raising the activity of layer 5 motor-cortex PV interneurons {cite:p}`Khademullah2020` has four effects:

- intracortical inhibition is restored
- pyramidal hyperexcitability falls
- motor deficit onset is delayed
- survival is extended

Inhibitory interneuron pathology also precedes motor neuron loss in the spinal cord across several models:

- V1 subpopulations are depleted at P63 and P112 {cite:p}`MontananaRosell2024`
- glycinergic stress appears early and synaptic output falls in mutant sod1 zebrafish {cite:p}`McGown2012`
- GlyT2+ interneurons change morphologically and functionally {cite:p}`Cavarsan2023`
- depolarising inhibitory events fail to control low-input-resistance motoneurons embryonically {cite:p}`Zhu2024`

In the same model, cortical GABAergic interneurons remodel structurally while losing intrinsic excitability (neurite path length 3380 µm against 2363 µm in wild type) {cite:p}`Clark2018`. NPY-expressing interneuron density also rises by 29% supragranularly and 30% infragranularly in motor but not somatosensory cortex {cite:p}`Clark2017` — remodelling, not simply depletion.

Two results bound the generality. Progressive dynein impairment causes motor axonal pathology without loss of any major spinal interneuron population {cite:p}`Christoforidou2026`. TrkB.T1 deletion restores PV interneuron numbers to physiological level in the mutant SOD1 hippocampus, the result that study reports for CA1, while in CA3 the compensation is incomplete (344.79 ± 27.13 against 433.86 ± 118.50 in wild type, p < 0.001) {cite:p}`Quarta2018`. The C9orf72 promoter is active in inhibitory as well as excitatory neurons, so a cell-autonomous route is possible {cite:p}`Langseth2017`.

:::{admonition} Evidence Conflict
:class: warning
{cite:t}`Amalyan2022` report that asymptomatic C9orf72 model mice already show reduced inhibitory drive onto surviving primary motor cortex layer 5 pyramidal neurons, with enhanced cortical output during high-speed locomotion, whereas {cite:t}`Bonthron2024` find no change in the relative abundance of excitatory versus inhibitory synapses onto spinal motor neurons at presymptomatic stages across multiple ALS models. The compartments differ — functional inhibitory drive onto cortical pyramidal neurons against anatomical synaptic puncta ratios onto spinal motor neurons — as do the genotypes, so the two are not strictly incompatible; both are recorded as contested. Status: open. The disagreement matters because the widely repeated claim that interneuron loss causes rather than follows cortical hyperexcitability in ALS has no primary demonstration in human tissue: the human evidence retrieved here is either an indirect paired-pulse physiological proxy or a cross-sectional post-mortem density, and the causal experiments exist only in rodents.
:::

(sec-07-pv-versus-sst)=

## Which interneurons? PV depletion is measured, SST is inferred

Where cells are counted in these conditions, the marker is almost always parvalbumin, and the reported reductions cluster in a band around a quarter to a half.

In TDP-43 proteinopathy, {cite:t}`Lin2021` found PV+ interneuron density reduced by 27.1% in mouse frontal cortex, by 50.1% in cingulate cortex, and by 24.6% in post-mortem human ALS cortex including C9orf72-linked and sporadic cases. {cite:t}`White2018` reported a ~25% reduction in frontal cortex of the same TDP-43 Q331K knock-in line, which makes it a confirmation within one model and not an independent replication. {cite:t}`Lin2020` traced the deficit back to postnatal day 14 while reporting the same paucity in human sporadic and C9orf72 ALS prefrontal cortex.

Comparable magnitudes recur under unrelated insults:

- 47.6% and 31.5% reductions in PVALB+ cell density in the motor cortex of post-mortem progressive multiple sclerosis (MS) cases stratified by meningeal inflammation {cite:p}`Magliozzi2021`
- layer-selective interneuron loss beneath subpial MS lesions {cite:p}`Nicholas2015`
- selective layer 2 PV loss with calretinin cells unchanged in MS motor cortex {cite:p}`Clements2008`
- a 52.2% reduction in PV-occupied cortical area in experimental autoimmune encephalomyelitis {cite:p}`Falco2014`
- 29.53% and 45.73% reductions in layer 5 PV density at seven days and one month after blast injury in a rat model {cite:p}`May2024`
- 39% in the dentate gyrus after status epilepticus {cite:p}`Mishra2015`
- a 42% total reduction over the study interval in wobbler mouse hippocampus against 18% in controls {cite:p}`Thielsen2013`

{numref}`fig-sec7-pv-versus-sst-depletion-across-conditions` puts these side by side without pooling them, because the convergence is partly an artefact of a shared metric: an area fraction, a stereological count and an uncorrected within-group reduction are not one quantity.

:::{admonition} Evidence Conflict
:class: warning
Against that convergence, {cite:t}`MerinoSerrais2025` quantified PV+ neuron density in human post-mortem hippocampal formation and entorhinal cortex with phospho-tau staging and reported the two groups as similar (11.2 ± 15.3 neurons/mm² in non-demented against 9.7 ± 15.8 in dementia cases), with no statistical test reported for that comparison and the region behind the two densities — hippocampal formation, entorhinal cortex or both — not resolved in the available material; the standard deviation exceeds the mean in both groups. Region, species and proteinopathy all differ from {cite:t}`Lin2021` — frontal cortex in a TDP-43 knock-in mouse plus ALS cortex, against human hippocampal formation in tau-associated dementia — so the conflict is as much about where one counts as about whether PV cells die. Status: open, and this study is itself recorded as contested. The deeper problem is that nearly every deficit above is immunoreactivity-based: no study combining a PV-independent interneuron label with PV immunoreactivity in the same degenerating human tissue was retrieved by these searches, so marker downregulation and cell death remain unseparated, and the therapeutic implication inverts between them.
:::

The SST evidence in these conditions is thinner, and part of it measures something else. Four quantitative entries exist:

- a 46% reduction in SST+ interneurons in the dentate gyrus after status epilepticus — larger than the 39% PV reduction in the same study and smaller than the 56% NPY reduction {cite:p}`Mishra2015`
- a ~65% loss of virally labelled hilar SST cells after traumatic brain injury (TBI), with rabies-traced starter neurons collapsing from 48.0 ± 3.7 to 9.4 ± 0.9 {cite:p}`Frankowski2022`
- a ~20% decrease reported jointly for PV and SST interneurons in CA1 of aged tau transgenic mice {cite:p}`Levenga2013`
- dystrophic tau-bearing SST neurons making up more than 40% of the hippocampal SST population at 15 months in a tau/amyloid rat, while PV neurons are relatively preserved {cite:p}`Morrone2022` — the tau-bearing dystrophic survivors described in {ref}`sec-alzheimers`

The last of those is a pathology burden, not a loss.

Transcript-level work reaches the population without counting cells, though mostly outside human ALS tissue:

- somatostatin, NPY and cholecystokinin transcripts are downregulated in the brainstem of cattle with bovine spastic paresis {cite:p}`Krull2025`
- GABAergic neurons rank as the most transcriptionally perturbed neuronal population in mutant SOD1 brainstem (1.77% of expressed genes differentially expressed), a single-cohort ranking with no independent reproduction published {cite:p}`Liu2020a`
- TDP-43 loss of function in medial prefrontal cortex identifies GABAergic neurons as selectively vulnerable {cite:p}`Thapa2025`
- TDP-43 overexpression accelerates age-dependent interneuron degeneration, with interneuron-derived ubiquitin aggregates {cite:p}`Tsuiji2017`
- a single-nucleus atlas of human antero-median thalamus in GRN-associated and sporadic TDP-43 FTD (331,065 nuclei from 92 individuals, a preprint) finds two inhibitory populations markedly depleted {cite:p}`Trujillo2026`

What this body of work does not contain is the obvious measurement. No quantification of SST interneuron density, morphology or transcriptional state in post-mortem human ALS or FTLD cortex appears to have been published, and the human cortical quantifications in these diseases measure parvalbumin. The contrast with the Alzheimer single-nucleus cohorts of {ref}`sec-human-evidence` is stark.

:::{admonition} Evidence Conflict
:class: warning
Whether reduced SST-immunoreactive counts after an insult mean interneuron death is directly contested. {cite:t}`Buckmaster1999` read the missing cells as selective death, reporting that interneuron loss in the epileptic hippocampus is remarkably specific, with 83% of the missing GAD-positive neurons somatostatin-immunoreactive; {cite:t}`Drake2024` fate-mapped the same population genetically in a Pten knockout epilepsy model and found density reduced by roughly 13–22% across subregions (hilar 4,395 ± 182 against 3,411 ± 322 cells/mm³, p = 0.0334) with no increase in oxidative-stress or apoptosis markers (3-nitrotyrosine-positive proportion 38.47% against 38.61%, p = 0.9684), retained SST phenotype among labelled cells (84.17% against 84.76%, p = 0.8212) and preserved axonal output density. The dimension of disagreement is what was counted — antibody-defined somata against genetically labelled cells with phenotype and output measured in parallel. Status: unresolved — the two studies examine different epileptogenic models, and no experiment applying both readouts to the same tissue was retrieved by these searches. The direction-of-change literature is unstable for the same reason: chronic pilocarpine epilepsy shows fewer SST- and NPY-immunoreactive hilar interneurons {cite:p}`Long2010`, whereas kindling and electrically induced status epilepticus show markedly increased SST and NPY immunoreactivity and mRNA in the same population {cite:p}`Vezzani1996` — partially resolved as a difference of timepoint and insult severity, which is precisely the condition under which peptide immunoreactivity fails as a surrogate for interneuron survival.
:::

(sec-07-tdp43-model)=

## The SST-driven disinhibition model and its single source

The mechanistic account that gives SST interneurons a leading role in ALS/FTD comes from one paper. {cite:t}`Zhang2016` recorded from a TDP-43 transgenic mouse motor cortex crossed to Sst-Cre and Pv-Cre reporter lines and found SST interneurons hyperactive, with significantly increased spontaneous but normal miniature inhibitory postsynaptic currents at three weeks, persisting into adulthood, while PV interneurons were hypoactive. On that basis the authors argued that SST-driven suppression of PV cells disinhibits layer 5 pyramidal neurons and contributes to excitotoxicity.

The recordings are from more than ten neurons in at least three mice per group, and the circuit logic depends on the SST→PV connection described in {ref}`sec-sst-identity`. This is the clearest case in this review of an influential mechanism carried by a single study: it stands unreplicated ten years after publication, with no independent laboratory reproduction reported. The alternative account in the wobbler mouse runs in the opposite direction, which is the section's mechanistic fork.

:::{admonition} Evidence Conflict
:class: warning
{cite:t}`Zhang2016` attribute layer 5 pyramidal hyperexcitability in TDP-43 mice to hyperactive SST interneurons suppressing PV cells, whereas {cite:t}`NietoGonzalez2010` attribute motor cortex hyperexcitability in the wobbler mouse to globally reduced GABAergic inhibition — the frequency of GABA-A-mediated spontaneous inhibitory postsynaptic currents in layer 5 pyramidal neurons was reduced by 72% — alongside decreased numbers of both PV- and SST-immunoreactive interneurons. The dimension of disagreement is whether SST interneurons are functionally gained or numerically lost, and whether disinhibition is a circuit-specific SST-to-PV effect or the consequence of overall interneuron depletion. Status: open. The models differ in construct and in what was counted, and the wobbler result is available here only at abstract level, so the comparison is between a cell-type-resolved optogenetic/electrophysiological dissection in one transgenic line and a mixed physiological and immunohistochemical account in another.
:::

:::{figure} ../figures/fig_sec7_pv_versus_sst_depletion_across_conditions.png
:name: fig-sec7-pv-versus-sst-depletion-across-conditions
:width: 100%
**Parvalbumin and somatostatin depletion across neurodegenerative and injury conditions, grouped by measured quantity.** Panels group entries by what was measured and where: panel A cortical PV+ cell-count/density reductions, panel B hippocampal PV+ cell-count reductions, panel C the two PV entries whose quantity differs in kind, panel D SST depletion, panel E a tau-pathology burden. No value was converted between quantity types and nothing is pooled. Values are not a single measurement type: bars for Lin 2021, White 2018, Magliozzi 2021, May 2024 and Mishra 2015 are percentage reductions in PV+ cell density or number; Falco 2014 is the percentage reduction in PV-immunoreactive cortical AREA, which conflates cell number with per-cell immunoreactivity; Merino-Serrais 2025 is an absolute density in neurons/mm². Panel A pools three species and three disease entities on one axis — TDP-43 Q331K knock-in mouse (ALS-FTD), human post-mortem progressive multiple sclerosis, and rat mild blast traumatic brain injury — and bar heights are not comparable across these systems. May 2024 is a rat model of mild blast traumatic brain injury. Panel B's axis is not one quantity: Mishra 2015's 39% is a loss relative to a separate control group, whereas Thielsen 2013's 42% and the 18% control bar are uncorrected within-group total reductions over the study interval, so the 42% must not be read as disease-attributable loss; Thielsen 2013's PV+ counts are reported for all areas of the hippocampal formation except the hilus, and the value plotted here is that study's total reduction rather than any single subfield. Regions are not matched: frontal cortex (Lin 2021's plotted value is the mouse frontal cortex, not the human post-mortem arm), motor cortex, cortical layer 5, dentate gyrus and hippocampus are each represented; Mishra 2015's loss is reported for the dentate gyrus, not the whole hippocampus, and Falco 2014's M1 cell-number reduction is reported for layers II and III. Lin 2021 and White 2018 report the same TDP-43 Q331K knock-in model and must not be read as independent replication. Magliozzi 2021's abstract reports 40 post-mortem progressive MS cases (with/without meningeal inflammation) and 10 control cases; whether that cohort is the same as the second, independent post-mortem group supplying the plotted 47.6% and 31.5% cannot be determined from the material available, and no MS-high / MS-low group size is stated anywhere. No bar in this figure carries a group size, and dispersion is plotted only for Merino-Serrais 2025, whose standard deviation exceeds its mean in both groups, so apparent rank order between bars is not statistically supported. The abstract of Magliozzi 2021 additionally reports a different figure (51.8) for PVALB+ cell density in cortical lesions in patients with high meningeal inflammation, which is not plotted. Mishra 2015's values are the vehicle (untreated) arm of a resveratrol intervention study. Merino-Serrais 2025's report describes the two densities as similar and quotes no statistical test, so the entry is not labelled "no significant difference"; the sentence reporting them names no region, and because that study's analysis covers the hippocampal formation and the entorhinal cortex the two bars are labelled "region not resolved in the available material". Panel D's axis carries the population qualifier because the quantity is not uniformly SST-specific: Levenga 2013's ~20% is reported jointly for PV and SST interneurons in CA1 and is labelled in-panel as such. Frankowski 2022's ~65% is the loss of Cre-dependent virally labelled (GFP+) hilar cells, and reduced labelling efficiency after injury cannot be separated from cell loss. Morrone 2022's value is the fraction of the SST hippocampal population at 15 months bearing dystrophic tau pathology, not SST cell loss, and sits on its own panel E axis; its denominator is itself depleted, since that study's abstract states that by 15 months the TgF344-AD rats had robust loss of excitatory and inhibitory neurons. In panel D, subfield is perfectly confounded with study, species, insult, timepoint and labelling method — one study per subfield (dentate gyrus, Mishra 2015; hilus, Frankowski 2022; CA1, Levenga 2013; hippocampus, Morrone 2022) — so no part of the spread can be attributed to subfield and no gradient across the bars may be inferred; the bars are therefore not ordered by subfield or by severity, and each carries its species, insult, region and counting method on its in-panel label. The injury descriptors that identify each model more precisely appear only in the papers' article text, not in the abstracts available for this figure, and are therefore not shown on the bars. No entry in panel D or E carries a stated group size, so no bar is better powered than another and no rank order between bars is statistically supported. Sources: {cite:p}`Lin2021, White2018, Magliozzi2021, May2024, Mishra2015, Thielsen2013, Falco2014, MerinoSerrais2025, Frankowski2022, Levenga2013, Morrone2022`.
:::

:::{dropdown} 📓 Figure code
```python
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

# ---



# ---

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

# ---

save_figure(fig, OUT)
print("saved", OUT)
```
:::

:::{figure} ../figures/fig_sec7_cortical_inhibition_across_als_cohorts.png
:name: fig-sec7-cortical-inhibition-across-als-cohorts
:width: 100%
**Transcranial magnetic stimulation measures of cortical inhibition in ALS, on separate axes.** Panel A plots the mean short-interval intracortical inhibition of one cohort by group, as reported in that study's abstract; panel B is a units-explicit table of three non-commensurable results, one row each, with no shared axis. Percent signs in this figure do not denote one quantity: Geevasinga 2015 reports mean SICI amplitude (%), whereas Pavey 2024 reports the proportion of a patient cohort in each excitability phenotype (%), which is why they are on separate panels and are not compared. Panel A's error bars are the standard deviations reported alongside those means in the study's abstract (1.8 / 1.2 / 1.8 / 1.0). The same paper's article text reports a different set of dispersion values for three of these groups — "patients with FALS, 1.2% [7.0%]; patients with SALS, 1.6% [10.3%]; control participants, 11.8% [8.6%]" — and which set is correct cannot be determined here, so the error bars are marked disputed and the separation between groups must not be read as tight. Higashihara 2024 is a standardised mean difference pooled over 25 studies and may already contain the Geevasinga 2015 cohort, so the two are not independent datapoints; its pooled comparator is not healthy-only, since of 1102 controls 907 are healthy and 195 have neuromuscular disease, and its n counts participants pooled across 25 studies rather than studies. McMackin 2026 measures GABA-B-mediated long-interval inhibition and reports its abstract's full-cohort null (Hedge's g ≤ 0.14, P ≥ 0.44), whereas all other entries measure GABA-A-mediated short-interval inhibition; the value shown is that full-cohort result, not the study's spinal-onset subgroup analysis. That protocol spans interstimulus intervals of 50, 100, 150 and 200 ms and, by the paper's own framing, intervals below 100 ms index spinal rather than cortical inhibition, so the null is not a pure cortical measure. Pavey 2024's proportions are a dichotomisation of mean SICI at a 5.5% threshold; in the cortically inexcitable 26.4%, SICI is undefined rather than reduced, so that subgroup is not evidence of reduced inhibition. All four entries are circuit-level physiological proxies and none measures somatostatin or parvalbumin interneurons directly. Group sizes are taken from each paper's abstract (Geevasinga 2015: 15 C9orf72 familial ALS, 11 asymptomatic carriers, 73 sporadic ALS, 74 controls; Higashihara 2024: 1530 ALS patients and 1102 controls across 25 studies; Pavey 2024: 417 patients; McMackin 2026: 30 ALS and 45 controls), and no weighting across panels is implied. The abstracts available for this figure name no recording muscle for Geevasinga 2015; McMackin 2026's abstract specifies stimulation of the precentral gyrus and names no muscle. Sources: {cite:p}`Geevasinga2015, Higashihara2024, Pavey2024, McMackin2026`.
:::

:::{dropdown} 📓 Figure code
```python
import sys, pathlib
sys.path.insert(0, str(pathlib.Path.cwd()))

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from shared_style import COLORS, apply_style, save_figure

apply_style()
OUT = "../fig_sec7_cortical_inhibition_across_als_cohorts.png"

# ---

# ---------------------------------------------------------------------------
# Every number below is verbatim from the source sentence recorded beside it.
# Nothing is converted, pooled or back-calculated; no ratio is computed.
# ---------------------------------------------------------------------------
PANEL_A_SRC = ("Results Mean (SD) short-interval intracortical inhibition was significantly "
               "reduced in patients with c9orf72 FALS (1.2% [1.8%]) and sporadic ALS "
               "(1.6% [1.2%]) compared with asymptomatic c9orf72 expansion carriers "
               "(10.2% [1.8%]; F = 16.1; P < .001) and healthy control participants "
               "(11.8% [1.0%]; F = 16.1; P < .001).")
PANEL_A = [
    dict(label="c9orf72 FALS\n(n = 15)",            value=1.2,  sd=1.8),
    dict(label="Sporadic ALS\n(n = 73)",            value=1.6,  sd=1.2),
    dict(label="Asymptomatic c9orf72\ncarriers (n = 11)", value=10.2, sd=1.8),
    dict(label="Healthy controls\n(n = 74)",        value=11.8, sd=1.0),
]
# The same paper's article text reports a different set of dispersion values for
# three of these groups; both sets are quoted, neither is adjudicated, and no
# ratio between them is computed.
DISPUTED_SD_SRC = ("The mean (SD) SICI, between ISI 1 and 7 milliseconds, was significantly "
                   "reduced in patients with FALS and ALS when compared with control "
                   "participants (patients with FALS, 1.2% [7.0%]; patients with SALS, "
                   "1.6% [10.3%]; control participants, 11.8% [8.6%]; F = 16.1, P < .0")

PANEL_B = [
    ["Higashihara 2024 —\nmeta-analysis of 25\nthreshold-tracking\nTMS studies",
     "Standardised mean\ndifference in mean SICI\n(GABA-A, short interval)",
     "SMD -0.99\n(95% CI -1.12 to -0.87);\nI2 = 40%",
     "1530 ALS patients;\n1102 controls (907 healthy,\n195 neuromuscular)"],
    ["Pavey 2024 — single\nclinic cohort,\nexcitability\nphenotyping",
     "Proportion of the cohort\nper phenotype (dichotomised\nat mean SICI 5.5%)",
     "Hyperexcitable 50.3%;\ncortically inexcitable 26.4%;\nnormal 23.3%",
     "417 classified patients"],
    ["McMackin 2026 —\npaired-pulse TMS,\nprecentral gyrus",
     "Long-interval intracortical\ninhibition (GABA-B);\nfull-cohort null",
     "Hedge's g <= 0.14,\nP >= 0.44",
     "30 ALS;\n45 healthy controls"],
]
PANEL_B_HEADERS = ["Study and design", "Measured quantity", "Reported value (own units)",
                   "Group sizes (abstract)"]

# ---

fig = plt.figure(figsize=(7.4, 7.4))
gs = GridSpec(2, 1, figure=fig, height_ratios=[1.0, 1.15], hspace=0.65,
              left=0.10, right=0.985, top=0.93, bottom=0.07)

# ---- Panel A --------------------------------------------------------------
axA = fig.add_subplot(gs[0, 0])
xs = list(range(len(PANEL_A)))
cols = [COLORS["decrease"], COLORS["decrease"], COLORS["no_change"], COLORS["neutral_gray"]]
bars = axA.bar(xs, [e["value"] for e in PANEL_A], yerr=[e["sd"] for e in PANEL_A],
               capsize=3, color=cols, edgecolor="black", linewidth=0.5, width=0.6,
               error_kw=dict(linewidth=0.9, ecolor=COLORS["conflict_marker"]))
for i, e in enumerate(PANEL_A):
    axA.text(i, e["value"] + e["sd"] + 0.35, f"{e['value']:g}", ha="center", fontsize=8)
axA.set_xticks(xs)
axA.set_xticklabels([e["label"] for e in PANEL_A], fontsize=7.6)
axA.set_ylabel("Mean short-interval intracortical\ninhibition (%), as reported in the\n"
               "study's abstract", fontsize=8.8)
axA.set_ylim(0, 15)
axA.set_title("A  Geevasinga 2015 — one cohort, four groups", loc="left",
              fontsize=11, fontweight="bold", pad=26)
axA.annotate("single cohort; error bars are SD and are marked DISPUTED (red) — the same paper's\n"
             "article text reports larger dispersion values for three of these groups",
             xy=(0.0, 1.015), xycoords="axes fraction", fontsize=7.8, style="italic",
             color=COLORS["neutral_gray"])
axA.annotate("a physiological proxy for inhibitory interneuron function;\n"
             "no interneuron is measured", xy=(0.03, 0.80), xycoords="axes fraction",
             fontsize=7.8, color=COLORS["neutral_gray"])

# ---- Panel B (annotated table, no shared axis) -----------------------------
axB = fig.add_subplot(gs[1, 0])
axB.set_xlim(0, 1)
axB.set_ylim(0, 1)
axB.axis("off")
axB.set_title("B  Three non-commensurable results, one row each — no shared axis",
              loc="left", fontsize=11, fontweight="bold", pad=14)
col_x = [0.0, 0.215, 0.495, 0.775]
row_y = [0.82, 0.54, 0.26]
for x, h in zip(col_x, PANEL_B_HEADERS):
    axB.text(x, 0.96, h, fontsize=8.0, fontweight="bold", va="top", ha="left",
             transform=axB.transAxes)
axB.plot([0, 1], [0.90, 0.90], color="black", linewidth=0.8, transform=axB.transAxes)
for y, row in zip(row_y, PANEL_B):
    for x, cell in zip(col_x, row):
        axB.text(x, y, cell, fontsize=7.3, va="top", ha="left", transform=axB.transAxes)
    axB.plot([0, 1], [y - 0.075, y - 0.075], color=COLORS["light_gray"],
             linewidth=0.6, transform=axB.transAxes)
axB.annotate("Percent signs in panels A and B do not denote one quantity, so the two panels are not compared. "
             "Higashihara 2024 may\nalready contain the Geevasinga 2015 cohort; the two are not independent "
             "datapoints. In the cortically inexcitable 26.4%,\nmean SICI is undefined rather than reduced. "
             "All four entries are circuit-level physiological proxies.",
             xy=(0.0, -0.02), xycoords="axes fraction", fontsize=7.6,
             color=COLORS["neutral_gray"])

# ---

save_figure(fig, OUT)
print("saved", OUT)
```
:::

(sec-07-markers-and-nets)=

## Prion disease, Down syndrome and traumatic injury: loss of cells, or loss of markers and nets

These literatures are included not because they are neurodegenerative in the same sense, but because each one ran, in a model system, the experiment the ALS and FTLD literature has not. Each measured a marker and something else in the same tissue, extending the insult-specific vulnerability pattern of {ref}`sec-selective-vulnerability`. No study in human FTLD, prion or trauma tissue appears to have performed that experiment.

In prion disease the two measurements disagree. Three reports describe loss of the PV-positive population:

- severe, early and selective loss of cortical PV-positive GABAergic neurons, with calbindin and calretinin subpopulations preserved, in scrapie and Creutzfeldt-Jakob disease (CJD) {cite:p}`Guentchev1998`
- alteration of the PV-positive population in sheep scrapie, in which the extracellular matrix was examined and found unchanged {cite:p}`Vidal2006`
- early destruction of the perineuronal net around PV interneurons in CJD, which that report interprets as a possible cause of the cells' loss {cite:p}`Belichenko1999`

But the cells themselves survive in other preparations. In ME7 prion-infected mice the perineuronal net is progressively lost in parallel with microglial activation while the PV interneurons persist through 20 weeks post-inoculation {cite:p}`Franklin2008`. Prion aggregates are under-represented in GABA-positive neurons and concentrated in excitatory ones (p < 0.01) {cite:p}`Erdenebat2024`. The prion protein gene is expressed roughly twofold higher in excitatory vGluT2+ neurons than in GABAergic cell types in a fatal familial insomnia model {cite:p}`Bauer2022b` — a single-model translatome result, unreplicated, whose direction nonetheless converges with the aggregate distribution reported by {cite:t}`Erdenebat2024`.

Both disagreements remain unresolved: reduced PV-immunoreactive density against the under-representation of prion aggregate in GABAergic neurons, and PV cell loss against perineuronal-net loss with intact counts. Both turn on species, stage and whether PV immunoreactivity falls before the cell dies. The one SST-resolved measurement in prion disease is transcriptional: translating-ribosome profiling in pre-symptomatic fatal familial insomnia and CJD models reports SST neurons as showing the most prominent gene expression changes of the profiled subtypes {cite:p}`Bauer2022a`, a preprint result awaiting replication.

Post-traumatic cortex produces the same dissociation with better controls. Controlled cortical impact depletes PV-immunoreactive interneurons in peri-injury cortex by 71% while leaving SST interneuron and excitatory neuron numbers intact {cite:p}`Nichols2018`. In the deafferentation undercut model, by contrast, PV and GABA immunoreactive cell counts are preserved (50.4 ± 2.7 against 50.1 ± 4.0 per section, p = 0.96) while the total NeuN cell count falls, perisomatic VGAT immunoreactivity drops by 46% and VGAT/synaptophysin by 67% {cite:p}`Gu2017`. That pair is partially resolved as a difference between injury models, but only if one accepts that counts and terminals can move independently.

{cite:t}`Folweiler2020` make the case for independence directly. After lateral fluid percussion injury, dentate PV interneurons fail to be recruited by feedforward excitation. Evoked action potential probability falls from 57.8 ± 6.3% to 12.0 ± 4.0% (p = 0.0008, Glass's d = 3.6) while the total dentate PV cell count is not significantly changed (p = 0.067). The only significant loss in that study sits in the hilus (p = 0.028). Blocking GABA-A receptors reverses the deficit — excessive inhibition of the interneurons, and not their loss.

On the SST side, surviving cells are demonstrably not quiescent. They:

- receive increased excitatory input after pilocarpine status epilepticus {cite:p}`Halabisky2010`
- are reported to sprout axons in an mTOR-dependent manner, although the recorded axon-crossing counts are indistinguishable between control, vehicle-treated and rapamycin-treated mice and are not normalised to the smaller surviving interneuron population {cite:p}`Buckmaster2011`
- acquire de novo excitatory input from granule and CA3 cells after controlled cortical impact and become hyperactive (43.33 ± 11.97% responding sites after CA3 photostimulation, p = 0.0033) {cite:p}`Butler2017`
- switch L-type calcium channel subunits from CaV1.2 to CaV1.3 contralateral to injury as early network hyperactivity resolves {cite:p}`Ihbe2021`
- reorganise their presynaptic inputs brain-wide {cite:p}`Frankowski2022` — an unreplicated tracing result

Their synaptic target makes this consequential: of the 42 symmetric synapses formed by one reconstructed hilar somatostatinergic axon segment, 67% were on granule cell spines that also receive an excitatory contact {cite:p}`Buckmaster2002` — a single reconstruction, not a population estimate.

Three results push back against these functional accounts:

- per-cell parvalbumin expression and gamma power fall six weeks after repetitive mild TBI {cite:p}`MacMullin2020`
- enhancing glutamate uptake preserves both intracortical inhibition and PV interneuron measures {cite:p}`Hameed2018`
- in human epileptogenic tuberous sclerosis cortex both SST and PV interneurons downregulate GABRA1, while only SST interneurons upregulate NKCC1 and lose maturation markers {cite:p}`Scheper2024`

One further result argues that none of this requires a proteinopathy at all. In the absence of amyloid, tau or alpha-synuclein pathology, midbrain dopamine depletion alone {cite:p}`Cauzzi2026`:

- breaks down perineuronal nets
- reduces inhibition
- causes progressive PV interneuron loss

It is a 2026 report with no replication yet.

Down syndrome contributes the cleanest marker-versus-function dissociation in the same animal. Anatomical and physiological work in Ts65Dn mice reports excess inhibition:

- increased dentate GABAergic innervation, attributed to a greater number of PV basket cells and normalised by removing the third App copy {cite:p}`Mojabi2016`
- increased interneuron subtype counts for calbindin, calretinin, NPY and VIP in CA1 and CA3, with PV unaffected {cite:p}`HernandezGonzalez2014`
- markedly raised evoked GABA release, normalised by environmental enrichment {cite:p}`Begenisic2011`

Optogenetic dissection of the same model disagrees. SST- and PV-evoked inhibition of granule cells is kinetically distinct and age-dependently reduced, which attributes the excess inhibition to neither class (SST-evoked IPSC decay 55.82 ± 2.66 ms in euploid against 62.62 ± 2.65 ms in trisomic mice) {cite:p}`Gutmann2026`. Anatomical terminal counts and functional synaptic measurements therefore stand in unresolved disagreement.

For SST specifically the trisomic literature is itself split. Reciprocal pyramidal-to-Martinotti connections are strengthened, with larger unitary EPSCs and increased release probability at dendritic inhibitory synapses {cite:p}`ZorrillaDeSanMartin2020` — a single-laboratory result unreplicated in six years. But triplicated miR155 suppresses SST+ interneuron production in human induced pluripotent stem cell organoids, and deleting the extra copy restores their number {cite:p}`Zhu2026`.

Gene-dosage mechanisms around the same cells have been mapped in three single studies, none of them independently reproduced:

- DSCAM dosage sets GABAergic bouton number {cite:p}`Liu2023`
- the DSCAM-PAK1 pathway impairs interneuron oxidative phosphorylation {cite:p}`Xu2022`
- patient-derived lines generate fewer calretinin interneurons {cite:p}`Huo2018`

Maternal choline supplementation restores parvalbumin neuron number in the basal forebrain (medial septum and vertical limb of the diagonal band) to near-euploid levels (a 1.5-fold increase, 2309.71 ± 157.62 against 1584.00 ± 196.58, p = 0.001) {cite:p}`Gautier2023`. Those are projection neurons, not the cortical and hippocampal interneurons counted elsewhere in this trisomic literature, so the result shows the deficit is modifiable without settling what it is.

(sec-07-multiple-sclerosis)=

## Multiple sclerosis: four modalities, four answers

In MS the direction of the inhibitory deficit depends entirely on which level of the GABAergic system is measured. Three measures of transmitter and protein point different ways:

- edited magnetic resonance spectroscopy finds lower GABA+ in posterior cingulate cortex (p = 0.036) and left hippocampus (p = 0.039) in relapsing-remitting patients, with no magnitude reported and a null in medial prefrontal cortex {cite:p}`Cao2017`
- 7T spectroscopy finds higher voxel GABA associated with smaller cortical lesion volume in the same voxel (−0.71 log(mm³) per unit GABA, 95% CI −1.24 to −0.18, p = 0.01), an association within patients and not a patient-versus-control contrast {cite:p}`Madsen2024`
- CSF parvalbumin at diagnosis is reported as higher in patients who are severely cognitively impaired four years later (p = 0.033), although the group means quoted in that report run in the opposite direction to the stated result and are therefore not used here {cite:p}`Ziccardi2024`

Against the transmitter-deficit reading, {cite:t}`Kang2020` measured cortical GABA-A receptor availability with [11C]flumazenil positron emission tomography and found global cortical binding higher in MS than in controls (5.72 ± 0.91 against 4.70 ± 0.41, p = 0.002). Receptor upregulation compensating for a reduced transmitter pool is as consistent with these data as a graded inhibitory failure. In that sense the conflict is partially resolved, because the two modalities index different levels and the opposition may be methodological instead of biological, so {numref}`fig-sec7-gabaergic-measures-in-ms-by-modality` arranges the four results by level without adjudicating between them.

The tissue literature adds a further split in the same disease. PV interneuron density falls in motor cortex {cite:p}`Magliozzi2021, Clements2008`, and total interneuron loss in temporal cortex is 43.4% greater in layer IV and 54.3% greater in layer VI beneath subpial lesions than in non-lesional cortex, without subtype resolution {cite:p}`Nicholas2015`. But demyelinated hippocampi show increased numbers of GAD67-positive neurons and elevated astrocytic GAD67 {cite:p}`Kiljan2019`, a contested result pointing the other way.

:::{figure} ../figures/fig_sec7_gabaergic_measures_in_ms_by_modality.png
:name: fig-sec7-gabaergic-measures-in-ms-by-modality
:width: 100%
**GABAergic measures in multiple sclerosis cortex, one column per modality.** The figure is a units-explicit table, not a grouped bar chart: there is no shared axis and no pooled summary. These four results cannot be expressed in common units — p-values from edited spectroscopy, a regression slope in log(mm³) per unit GABA, a unitless positron emission tomography binding potential, and a direction-and-significance statement for a cerebrospinal fluid protein — and no concentration column appears in the table. Direction is not shared: spectroscopy indicates lower GABA in multiple sclerosis while flumazenil positron emission tomography indicates HIGHER GABA-A receptor binding. Only the cerebrospinal fluid parvalbumin column is interneuron-specific; spectroscopy GABA is a bulk tissue metabolite pool and flumazenil binding measures postsynaptic receptor availability. Ziccardi 2024's report quotes group means whose assignment contradicts the direction stated in the same sentence and in that study's abstract; the contradiction cannot be resolved from the material available, so no concentration is tabulated and the column reports only the abstract-supported direction (higher cerebrospinal fluid parvalbumin at diagnosis in patients later severely cognitively impaired) with p = 0.033. Ziccardi 2024 includes no control group — all 72 participants are patients with multiple sclerosis and the contrast is between those later severely cognitively impaired and those later cognitively normal — so the direction-relative-to-controls cell is left blank for that column. Kang 2020 is a pilot study (sixteen patients and ten age-matched healthy controls) and its control binding potential differs between its article text (4.79) and its abstract (4.70), so the patient-versus-control gap depends on which anchor is used. Participant counts are printed as the papers state them: Cao 2017 twenty-eight relapsing-remitting patients and twenty-six healthy controls (enrolled; no post-exclusion analysed count is available here, so the analysed set may be smaller); Kang 2020 sixteen patients and ten age-matched healthy controls; Madsen 2024 forty-seven patients with multiple sclerosis (34 relapsing-remitting, 13 secondary progressive) and 23 healthy controls; Ziccardi 2024 72 patients. No summed participant total is printed. Madsen 2024's −0.71 log(mm³) coefficient is an association estimated in the patients only, so its denominator is the patient group as the abstract states it, not the whole sample, and the column is a within-patient association between voxel GABA and cortical lesion volume rather than a patient-versus-control difference. Cao 2017 contributes significance only (p = 0.036 posterior cingulate, p = 0.039 left hippocampus) with no GABA+ concentration and a null in medial prefrontal cortex, so no magnitude can be read from that column. Sources: {cite:p}`Cao2017, Madsen2024, Kang2020, Ziccardi2024`.
:::

:::{dropdown} 📓 Figure code
```python
import sys, pathlib, textwrap
sys.path.insert(0, str(pathlib.Path.cwd()))

import matplotlib.pyplot as plt
from shared_style import COLORS, apply_style, save_figure

apply_style()
OUT = "../fig_sec7_gabaergic_measures_in_ms_by_modality.png"

# ---

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

# ---

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

# ---

save_figure(fig, OUT)
print("saved", OUT)
```
:::

(sec-07-scope-discipline)=

## Scope discipline: what belongs in a somatostatin review

The breadth of this section should not be mistaken for breadth of SST evidence. Direct, cell-resolved SST measurements in the conditions covered here exist only in rodent models and one human stem-cell model:

- the TDP-43 cortical recordings {cite:p}`Zhang2016`
- the wobbler counts {cite:p}`NietoGonzalez2010`
- post-insult hippocampal counts and tracing {cite:p}`Mishra2015, Frankowski2022, Levenga2013, Drake2024`
- tau-bearing survivors in a transgenic rat {cite:p}`Morrone2022`
- trisomic Martinotti physiology {cite:p}`ZorrillaDeSanMartin2020`
- trisomic dentate SOM interneuron physiology {cite:p}`Gutmann2026`
- prion translatome profiling {cite:p}`Bauer2022a`
- SST+ interneuron production counted in human iPSC-derived cortical organoids {cite:p}`Zhu2026`

Beyond those, transcript and tissue work measures the population outside degenerating human cortex: downregulated somatostatin transcripts in bovine brainstem {cite:p}`Krull2025`, SST+ cell counts in human tuberous sclerosis surgical cortex {cite:p}`Scheper2024`, and a post-mortem human thalamic single-nucleus atlas quantifying the depletion of two inhibitory populations {cite:p}`Trujillo2026`.

Prion disease, MS and traumatic injury enter this review as controlled comparisons for the marker problem, not as established SST pathologies. Their human evidence is dominated by parvalbumin and perineuronal net markers, and SST interneurons appear never to have been quantified directly in human prion disease, MS cortical lesions or chronic traumatic encephalopathy. Chronic traumatic encephalopathy in particular is discussed here only through experimental traumatic brain injury models. No published study appears to pair it with somatostatin, parvalbumin or interneuron measurements, so the inhibitory-circuit evidence commonly attributed to that condition belongs to the injury models and not to the tissue. These absences mark the present limits of the published record and are not proof that the studies do not exist.

Four disease literatures have now produced the same four explanatory axes: what was measured, where, in which construct, and in which cohort. Those disagreements are inventoried in {ref}`sec-conflicts-limitations`. {ref}`sec-circuit-consequences` changes the level of description and asks what SST dysfunction does to circuits, which is where the apparently contradictory cellular findings here — hyperactive survivors, intact counts with degraded terminals, markers that fall before cells die — become reconcilable and not merely contradictory.

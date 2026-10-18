(sec-therapeutics)=

# Therapeutic Strategies: Somatostatin Receptor Agonists, Interneuron-Targeted Interventions, and Neuromodulation

Where {ref}`sec-human-evidence` left the somatostatin deficit established in human cortex but unaccompanied by any fluid measure that could grade it, therapy supplies the direct test: if the deficit is causal, correcting it should change the disease. No study retrieved by these searches has run that test on the SST class. The interventions assembled below are the closest approaches to it — receptor agonism, replacement of the cells, gene therapy addressed to inhibitory neurons, excitability-lowering drugs, and stimulation of the circuits those cells inhabit — and each of them either engages a different cell class, stops short of a disease model, or stops short of a controlled clinical endpoint. The pattern that organises the section is not disease biology but study design: across these literatures the reported magnitude of benefit falls as the design that produced it becomes more rigorous.

(sec-10-sstr-agonists)=

## Somatostatin receptor agonists: a clean rodent pathway and an unclosed translational chain

The most coherent pharmacological case for acting on the somatostatin axis comes from a single series of studies of the SSTR4-selective agonist NNC 26-9100, and its coherence is also its limitation. Delivered intracerebroventricularly at 0.2 µg in SAMP8 mice, the compound produced what its authors describe as an approximately 2-fold enhancement in recognition memory (P < 0.01) {cite:p}`Sandoval2012`; given chronically by the intraperitoneal route at 20 µg it lowered brain amyloid-β (Aβ) x-42, though the report gives a direction and P < 0.05 rather than a magnitude {cite:p}`Sandoval2011`; co-administration of the metalloproteinase inhibitor phosphoramidon at 10 mM left Aβ x-42 at levels the source describes as identical to vehicle and higher than with the agonist alone (P < 0.01 against agonist alone; no test is reported for the identity with vehicle), placing neprilysin causally downstream of the receptor {cite:p}`Sandoval2013`; and transcriptional profiling in 3xTg-AD mice found subcortical increases in *Nep1* (2.4-fold), *Ide* (4.4-fold) and *Sst* (4.4-fold) at 24 h that were not statistically significant {cite:p}`Sandoval2019`. Medicinal chemistry has continued to produce SSTR4-selective chemical series with Alzheimer's disease named as an intended indication {cite:p}`AbdelMagid2024`, and structural work on the receptor family places subtype discrimination largely in extracellular loop 2, consistent with the earlier mutagenesis that work reviews rather than repeats — a loop swap reported to reduce octreotide binding by ~40-fold, and a position-7 phenylalanine substitution reported to raise SSTR2 affinity ~6-fold with little effect on SSTR4 {cite:p}`Zhao2022`. Two limits bound the whole programme. All four efficacy entries test one compound from one closely related research programme, so their agreement is convergence within a programme and not independent replication; and the doses are not interchangeable, because 0.2 µg into the ventricle and 20 µg into the peritoneum are the blood–brain barrier problem written as a dose. No replicating study for the phosphoramidon result was retrieved by these searches, more than a decade after publication. It also establishes less than it is usually asked to: blocking the enzyme abolishes the amyloid effect, which shows the effect requires neprilysin activity, but no study directly measuring a rise in brain neprilysin activity under pharmacological SSTR agonism was retrieved by these searches, so the step most often quoted as the mechanism is inferred rather than observed.

{numref}`fig-sec10-sstr4-agonist-dose-route-mechanism` tabulates the four results rather than plotting them, because they do not share a measurement scale.

:::{figure} ../figures/fig_sec10_sstr4_agonist_dose_route_mechanism.png
:name: fig-sec10-sstr4-agonist-dose-route-mechanism
:width: 100%
**SSTR4 agonist: dose, route and endpoint.** Four reported results for the SSTR4-selective agonist NNC 26-9100, tabulated with their quoted values {cite:p}`Sandoval2012, Sandoval2011, Sandoval2013, Sandoval2019`. No shared numeric axis: the four results are a behavioural preference ratio, two Aβ x-42 protein measurements and a set of qPCR fold-changes. Route and dose differ: 0.2 µg intracerebroventricular versus 20 µg chronic intraperitoneal; the doses are not comparable. Two entries report only a direction of effect and a p value; no magnitude is shown for them. The Sandoval 2012 row quotes the published wording, "an approximately 2-fold enhancement in recognition memory". Sandoval 2019 was performed in 3xTg-AD mice, not SAMP8; the fold-changes shown are the non-significant subcortical values at 24 h ("no statistically significant differences were found between NNC 26-9100 and vehicle treatment"), and the same study's cortical counterparts at 24 h were larger, the abstract reporting the failure to reach statistical significance only for the subcortical tissue. No group size is shown for any row: none of the four reports states one in its abstract or in the sentence reporting the result. All entries test one compound from one research programme; this is convergence within a programme, not independent replication.
:::

:::{dropdown} 📓 Figure code
```python
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath("__file__")) if "__file__" not in globals() else os.path.dirname(os.path.abspath(__file__)))

import matplotlib.pyplot as plt
from shared_style import COLORS, apply_style, save_figure

apply_style()
OUTDIR = ".."   # notebooks live in figures/notebooks/; figures are written to figures/

# ---

# One row per study; cells quoted from each entry's value_source_sentence.
ROWS = [
    dict(study="Sandoval 2012",
         model="SAMP8 mouse, 12 months",
         route_dose="0.2 \u00b5g i.c.v.",
         endpoint="object-recognition memory",
         value='"an approximately 2-fold enhancement in recognition memory"',
         sig="P < 0.01"),
    dict(study="Sandoval 2011",
         model="SAMP8 mouse",
         route_dose="20 \u00b5g chronic i.p.",
         endpoint="brain A\u03b2 x-42",
         value='direction only: "a significant decrease"; no magnitude stated',
         sig="P < 0.05"),
    dict(study="Sandoval 2013",
         model="SAMP8 mouse; abstract also reports an APPswe Tg2576 cohort",
         route_dose="agonist + 10 mM phosphoramidon",
         endpoint="A\u03b2 x-42 under neprilysin blockade",
         value='direction only: "identical levels ... compared to vehicles", and increased versus agonist alone',
         sig="P < 0.01"),
    dict(study="Sandoval 2019",
         model="3xTg-AD mouse",
         route_dose="agonist vs vehicle, 24 h sampling",
         endpoint="subcortical transcript fold-change (qPCR)",
         value="Nep1 2.4-fold, Ide 4.4-fold, Sst 4.4-fold",
         sig="not significant"),
]

# (key, header, x0, column width) in figure-width fractions
COLS = [("study",      "Study",                   0.000, 0.105),
        ("model",      "Model",                   0.115, 0.140),
        ("route_dose", "Route and dose",          0.270, 0.130),
        ("endpoint",   "Endpoint class",          0.415, 0.130),
        ("value",      "Reported value (quoted)", 0.560, 0.280),
        ("sig",        "Significance",            0.855, 0.145)]

FS, FSH = 7.5, 8.0
FIGW = 7.08
LINE = FS * 1.35 / 72.0          # inches per wrapped text line
LINE_H = FSH * 1.35 / 72.0

# ---

fig = plt.figure(figsize=(FIGW, 4.0))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 1)
ax.axis("off")
fig.canvas.draw()
renderer = fig.canvas.get_renderer()


def text_width(s, fontsize, weight="normal"):
    """Width of a single-line string as a fraction of figure width."""
    t = ax.text(0, 0, s, fontsize=fontsize, fontweight=weight)
    w = t.get_window_extent(renderer=renderer).width
    t.remove()
    return w / (FIGW * fig.dpi)


def wrap_to_width(s, maxw, fontsize, weight="normal"):
    """Greedy word wrap so that no line exceeds maxw figure-width fractions."""
    lines, cur = [], ""
    for word in s.split():
        trial = word if not cur else cur + " " + word
        if text_width(trial, fontsize, weight) <= maxw or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return "\n".join(lines)


wrapped = []
for row in ROWS:
    cells = {k: wrap_to_width(row[k], w - 0.012, FS, "bold" if k == "study" else "normal")
             for k, _, _, w in COLS}
    wrapped.append((cells, max(c.count("\n") + 1 for c in cells.values())))

headers = {k: wrap_to_width(lab, w - 0.008, FSH, "bold") for k, lab, _, w in COLS}
head_lines = max(v.count("\n") + 1 for v in headers.values())

NOTES = [
    "No group size is shown for any row: none is stated in the quoted result sentence or in the abstract.",
    "Route and dose are not comparable: 0.2 \u00b5g intracerebroventricular versus 20 \u00b5g chronic intraperitoneal.",
    "All four rows test one compound (NNC 26-9100) from one closely related research programme.",
    "All values extracted from the source papers' full text.",
]

head_h = head_lines * LINE_H + 0.10
rows_h = sum(n * LINE + 0.12 for _, n in wrapped)
notes_h = 0.16 + LINE + 0.06 + len(NOTES) * LINE * 1.1 + 0.08
H = head_h + rows_h + notes_h

fig.set_size_inches(FIGW, H)
ax.set_ylim(0, H)

y = H - 0.06
for key, lab, x0, w in COLS:
    ax.text(x0, y, headers[key], fontsize=FSH, fontweight="bold", va="top", ha="left",
            linespacing=1.35)
y -= head_h - 0.04
ax.plot([0, 1], [y, y], color="#333333", lw=1.0)

for i, (cells, nlines) in enumerate(wrapped):
    h = nlines * LINE + 0.12
    if i % 2 == 0:
        ax.add_patch(plt.Rectangle((0, y - h), 1, h, facecolor="#F4F4F4",
                                   edgecolor="none", zorder=0))
    for key, lab, x0, w in COLS:
        ax.text(x0, y - h / 2.0, cells[key], fontsize=FS, va="center", ha="left",
                fontweight=("bold" if key == "study" else "normal"),
                color="#111111", zorder=2, linespacing=1.35)
    y -= h
    ax.plot([0, 1], [y, y], color="#CCCCCC", lw=0.6, zorder=1)

y -= 0.14
ax.text(0.0, y, "Heterogeneous comparison \u2014 values not pooled. "
                "No numeric axis: the four endpoint classes share no scale.",
        fontsize=FS, style="italic", color=COLORS["conflict_marker"], ha="left", va="top")
y -= LINE + 0.08
ax.text(0.0, y, "\n".join(NOTES), fontsize=FS, color="#333333", ha="left", va="top",
        linespacing=1.45)

# ---

save_figure(fig, os.path.join(OUTDIR, "fig_sec10_sstr4_agonist_dose_route_mechanism.png"))
```
:::

The clinically available short analogues cannot test this pathway. The octapeptide and hexapeptide analogues, which are the class the receptor-pharmacology record describes, bind well to only three of the five receptors — SSTR2, SSTR3 and SSTR5 — and therefore cannot engage the subtype the amyloid-clearance argument depends on {cite:p}`Patel1999`, while their formulation constraints are those of peptides: food reduces absorption of oral octreotide by about 90% {cite:p}`Periferakis2024`. Systemic octreotide nonetheless produces central effects in a rat model of post-traumatic stress, attenuating HPA-axis hyperactivity, neuroinflammation and oxidative stress, with the authors themselves noting that direct receptor-mediated mechanisms remain unconfirmed {cite:p}`Motamedy2026`. Related peptides of the same family act on tissue compartments that drug delivery must cross: loss of cortistatin dysregulates 613 genes in brain endothelium {cite:p}`CastilloGonzalez2023`, cortistatin supplementation shifts neuronal mitochondrial networks toward a tubular morphology (to 84% in wild-type and 40% in mutant neurons) {cite:p}`GonzalezGarcia2026`, and systemic cortistatin restores pole-test performance in MPTP-intoxicated mice {cite:p}`SerranoMartinez2024`. Barrier-opening technologies are advancing in parallel — focused ultrasound with microbubbles is reported practical, reversible and generally safe in selected Alzheimer's cohorts, though without conclusive evidence linking the opening to clinical benefit {cite:p}`Desale2026`, and ultrasound-assisted lipid nanoparticle delivery achieved gene editing comparable to the same group's earlier ultrasound-delivered viral system while raising the astrocyte-targeted expression fraction above that group's previously reported 12.9%, in a comparison against a published number rather than a controlled head-to-head, and in astrocytes rather than any interneuron population {cite:p}`Zheng2026`. Two absences matter more than any of this: no clinical trial of an SSTR-selective agonist in any neurodegenerative indication was retrieved by these searches, and no quantitative human CNS exposure data for the octreotide class surfaced, so proposals to repurpose existing analogues remain unanchored. The receptor pharmacology that would make such a trial interpretable is set out in {ref}`sec-sst-identity`.

(sec-10-neprilysin)=

## Raising neprilysin: downstream effector, or the wrong amyloid pool

The SSTR4 chain terminates in neprilysin, and the independent literature on raising neprilysin directly shows why terminating there is not the same as succeeding. Vector-delivered neprilysin is axonally transported to presynaptic terminals and abolished the rise in Aβ in the hippocampal formation of neprilysin-deficient mice, with reductions appearing contralateral to the injection {cite:p}`Iwata2004`. Against that, a synthesis of hAPP/NEP double-transgenic data reports that a 50% fall in soluble Aβ with prevention of plaque formation left oligomer reduction undemonstrated and behavioural outcome unassessed, attributing the dissociation to neprilysin's inability to cleave some naturally occurring oligomeric Aβ species {cite:p}`Grimm2013`. A review of neprilysin biology notes that the enzyme is promiscuous, metabolising enkephalins, substance P and bradykinin alongside Aβ, so raising its activity would not be a clean intervention {cite:p}`Saxena2024`; no primary measurement of off-target neuropeptide consequences under a neprilysin-raising therapy was retrieved by these searches. The human anchor for the whole chain remains correlational, and narrower than the chain it supports: somatostatin content is reduced by approximately 50% in the anterior olfactory nucleus in Alzheimer's disease, with most remaining somatostatin-expressing elements co-localising with Aβ (65.43%) {cite:p}`SaizSanchez2010` — one region, recorded at abstract level. The upstream step — that loss of somatostatin signalling is what lowers neprilysin in human disease — is contested where it is examined at all, and is treated in {ref}`sec-alzheimers`; its primary demonstration in human tissue was not retrieved here, which makes the therapeutic prior for SSTR agonism weaker than its frequent restatement in reviews implies.

:::{admonition} Evidence Conflict
:class: warning
**Which amyloid pool is therapeutically decisive for neprilysin-raising strategies?** Vector-delivered neprilysin abolishes the Aβ increase in neprilysin-deficient hippocampus and reduces it in young mutant APP mice {cite:p}`Iwata2004`, whereas the synthesis of hAPP/NEP double-transgenic data reports a 50% soluble-Aβ reduction and plaque prevention without a demonstrated fall in oligomers, on the stated grounds that neprilysin cannot cleave some naturally occurring oligomeric species {cite:p}`Grimm2013`. The disagreement is not about whether neprilysin degrades Aβ but about which pool matters; the two sides measure different pools, and the question is unresolved.
:::

(sec-10-gamma)=

## Gamma entrainment: what is stimulated, and what shrinks as rigor rises

Gamma sensory stimulation is the most publicised interneuron-targeted strategy in this field and the one whose mechanistic premise is least secure. Three claims must be separated: that 40 Hz stimulation entrains the endogenous oscillator, that it lowers amyloid, and that it improves cognition. The frequency choice has a biophysical rationale — human steady-state visual evoked potentials show resonance peaks near 10, 20, 40 and 80 Hz {cite:p}`Herrmann2001` — and the paradigm's originating report measured soluble amyloid one hour after a single hour of flicker, finding Aβ1-40 reduced by 57.96% and Aβ1-42 by 57.97% in visual cortex relative to dark controls {cite:p}`Iaccarino2016`. Direct multisite silicon-probe recording in APP/PS1 and 5xFAD mice, however, found that 40 Hz flicker did not engage native gamma oscillations in visual cortex, entorhinal cortex or hippocampus, with weak hippocampal spike responses {cite:p}`Soula2023`; no independent confirmation that 40 Hz sensory stimulation entrains native gamma in deep structures was retrieved by these searches. The amyloid endpoint, meanwhile, is intensity-dependent: in 3xTg-AD mice Aβ burden fell under high-intensity (1100–1500 lux) but not low-intensity (100–500 lux) 40 Hz stimulation {cite:p}`Gu2026`, an exposure variable that is unreported in much of the downstream work. The amyloid endpoint does replicate across sensory modality: four weeks of 40 Hz vibrotactile stimulation lowered cortical soluble Aβ40 and Aβ42 and hippocampal plaque burden {cite:p}`Nam2026`, as the intensity-controlled study does at high illumination {cite:p}`Gu2026`; both name the originating report among the work they replicate {cite:p}`Iaccarino2016`. Two further results are often enrolled in the same argument but measure something else. Intraoperative 40 Hz flicker preserved novel-object recognition memory after anaesthesia and surgery {cite:p}`Jiang2026`, an endpoint that is behavioural rather than molecular and a model that is perioperative rather than neurodegenerative, and the record for it is contested rather than replicated. The frequency control — 22 days of 80 Hz stimulation leaving V1 neuronal loss in P301S tau mice unchanged {cite:p}`Adaikkan2019` — was run on neuronal loss in a tauopathy, not on amyloid, and carries no replication here. Where optogenetic drive is reported to have restored gamma and spatial memory in amyloid models, the targeted cells were medial septal parvalbumin neurons, not SST cells — a result known here only through a survey of this literature, which attributes it to an earlier experiment whose primary report was not retrieved by these searches {cite:p}`Zhang2024a`. That is the central qualification for this review: the entrainment literature is built on fast-spiking parvalbumin circuitry, and no study retrieved here selectively drove SST interneurons in a neurodegeneration model and measured amyloid, tau or cognition. Whether 40 Hz stimulation engages the endogenous oscillator at all is examined in {ref}`sec-circuit-consequences`.

:::{admonition} Evidence Conflict
:class: warning
**Does 40 Hz flicker entrain native gamma, and does the amyloid effect generalise or translate?** Three recorded disagreements share one party: the originating report, which attributes a large reduction of soluble Aβ1-40 and Aβ1-42 in visual cortex to one hour of 40 Hz flicker {cite:p}`Iaccarino2016`. On mechanism, multisite silicon-probe recording in two amyloid models finds no engagement of native gamma in visual cortex, entorhinal cortex or hippocampus {cite:p}`Soula2023`, so the process the originating study proposes {cite:p}`Iaccarino2016` is not observed where it is looked for directly; the axis is recording method and the level at which entrainment is defined, and the disagreement is unresolved. On dose, an intensity-controlled study lowers Aβ burden only at high illumination {cite:p}`Gu2026`, which bounds rather than overturns the original {cite:p}`Iaccarino2016` and is partially resolved in favour of a threshold — stimulus intensity being an axis left unreported in much of the downstream literature. On translation, the individual trials tabulated in a synthesis of clinical gamma stimulation report no significant change in overall cognition tests under protocols of up to four weeks, although that synthesis also tabulates longer protocols with reported cognitive improvement and its authors' own conclusion is favourable to the technique {cite:p}`DePaolis2024`, which disagrees with the mouse molecular result {cite:p}`Iaccarino2016` along species and endpoint — amyloid load in mouse cortex against global cognition in patients, with delivery modality differing as well — and is also open.
:::

In patients, the effect sizes order themselves by design. A random-effects meta-analysis of randomized 40 Hz light stimulation trials — eleven studies, 341 participants — found no significant cognitive difference from control (standardised mean difference, SMD = 0.16, 95% CI −0.36 to 0.68, P = 0.55) alongside a significant difference in structural brain measures, and no significant increase in overall adverse events, although the risk of tinnitus was significantly raised {cite:p}`Ang2025`. A single session in 62 healthy adults improved psychomotor vigilance accuracy (Kruskal–Wallis χ²(2) = 7.98, p = 0.018) {cite:p}`Attokaren2026`, and a randomized sham-controlled trial of transcranial and intranasal photobiomodulation in post-COVID cognitive impairment — a near-infrared photobiomodulation trial rather than sensory gamma entrainment, its source stating no pulse rate — reported a significant difference of 0.059 (95% CI 0.007–0.111, p = 0.028, Cohen's d ≈ 0.44) in a prespecified exploratory subgroup under 45 years, while its primary outcome, 0.043 (95% CI −0.007 to 0.092), was not significant at p = 0.088 {cite:p}`Lim2026`. Feasibility and open-label work supplies the rest of the ladder: entrainment does not accumulate with chronic exposure, the number of entrained EEG channels being unchanged before versus after flicker exposure (all P > 0.11) {cite:p}`He2021`; a sham-controlled trial reported maintained daily-living function against a declining sham arm of eight participants {cite:p}`Cimenser2021`; long-term follow-up diverged by onset subtype, with the 40 Hz EEG response declining in early-onset and increasing in late-onset patients, who improved on MMSE, CDR and FAS against matched registry comparators {cite:p}`Chan2025`; and a single open-label record whose reported outcome could not be attributed to the work cited for it {cite:p}`Yamada2026` cannot be placed on the ladder at all. {numref}`fig-sec10-gamma-stimulation-evidence-ladder` sets these human results beside one another, each on the scale its own source reports. The two best-controlled results disagree outright, and ranking them does not settle it: population, outcome measure and exposure duration all differ between the pooled patient trials {cite:p}`Ang2025` and the single-session study in healthy adults {cite:p}`Attokaren2026`, so neither excludes the other and whether 40 Hz sensory stimulation produces measurable cognitive benefit remains open. New trials continue to register, extending the paradigm to post-illness cognitive impairment {cite:p}`Fu2026` and to home-based personalised transcranial alternating current stimulation (tACS) with an enrolment target of 40 participants {cite:p}`Brechet2026`. The strongest human claim is structural rather than cognitive: over six months of daily audiovisual stimulation, total cerebral white matter volume rose by 0.17 ± 1.08% in the active arm while falling by 2.54 ± 1.38% under sham (p < 0.038) {cite:p}`Da2024a`, and corpus callosum area changed by 0.20 ± 0.70% versus −2.08 ± 0.87% {cite:p}`Da2024b`. Both are analyses of one randomized cohort from a single device programme with overlapping, unequal subsets, which is the weakest form of convergence this review encounters, and no independent group's structural replication was retrieved.

:::{figure} ../figures/fig_sec10_gamma_stimulation_evidence_ladder.png
:name: fig-sec10-gamma-stimulation-evidence-ladder
:width: 100%
**Gamma stimulation in humans, ordered by design.** (A) Sham- or control-referenced interval estimates in patient populations {cite:p}`Ang2025, Lim2026`. (B) Acute single-session attention in healthy adults, shown as a test statistic with no magnitude axis {cite:p}`Attokaren2026`. (C) Percent change from baseline over 6 months, active versus sham, for two structural measures {cite:p}`Da2024a, Da2024b`. Ang 2025's SMD = 0.16 is a null finding (P = 0.55, 95% CI crossing zero), not a small benefit. Lim 2026's 0.059 is an exploratory <45-year subgroup estimate; the trial's primary outcome was 0.043, p = 0.088, non-significant, and the subgroup's own size is not reported, so that row carries no weight. The two panel-A rows are on different scales (a pooled standardized mean difference and a raw composite z-score difference), are not pooled, and their positions on the axis are not comparable with one another; each row prints its own metric. Attokaren 2026's value is a Kruskal–Wallis test statistic, not an effect size, and comes from healthy adults after a single 1-hour session; it is shown in a separate panel with no magnitude axis. Sensory gamma entrainment (40 Hz audiovisual flicker) and near-infrared photobiomodulation (Vielight Neuro RX Gamma device) are distinct interventions; the photobiomodulation pulse rate is not stated in its abstract. Only Ang 2025 studies a dementia population. Sample sizes are as stated in each paper's abstract (341 pooled participants; 43 randomized / 41 analysed; 62 healthy adults). "Whole brain" in the row annotations is a label, not an equivalence: Lim 2026 delivered light to default-mode-network targets, the other entries drove the whole brain through the senses. In panel C, both measurements come from the same trial cohort (OVERTURE, NCT03556280) with overlapping participants (white matter subset N = 38; corpus callosum subset N = 50, 33 active / 17 sham) — one trial reported twice, not independent replication; the corpus callosum is a component of the white matter compartment measured in the other entry, so the two percent changes are nested, not independent; one entry is a volume change, the other a cross-sectional area change, both expressed as percent of baseline; error terms are reproduced as published, the sources do not state whether they are SD or SEM, and for the corpus callosum sham arm the published ±0.87% cannot be distinguished from the ±0.87% the abstract attaches to the between-group difference; the corpus callosum analysis used Bayesian linear mixed-effects modelling, while the white matter analysis reports a significance test without naming its framework; rows are labelled by measured structure because both entries would otherwise appear as "Da 2024"; and the corpus callosum analysis describes its population as mild cognitive impairment or Alzheimer's disease, not mild-to-moderate Alzheimer's disease alone.
:::

:::{dropdown} 📓 Figure code
```python
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath("__file__")) if "__file__" not in globals() else os.path.dirname(os.path.abspath(__file__)))

import matplotlib.pyplot as plt
from shared_style import COLORS, apply_style, save_figure

apply_style()
OUTDIR = ".."   # notebooks live in figures/notebooks/; figures are written to figures/

# ---

# ---------------------------------------------------------------- panel A
# Interval estimates in patient populations. Scales are NOT comparable.
PANEL_A = [
    dict(label="Ang 2025",
         value=0.16, lo=-0.36, hi=0.68,
         metric="pooled standardized mean difference, cognition vs control "
                "(P = 0.55, null)",
         detail="meta-analysis of randomized 40 Hz light stimulation trials; "
                "11 studies, 341 participants; AD and MCI"),
    dict(label="Lim 2026",
         value=0.059, lo=0.007, hi=0.111,
         metric="composite cognitive z-score difference at Day 56, active - sham "
                "(p = 0.028)",
         detail="prespecified exploratory <45-year subgroup, subgroup size not reported; "
                "43 randomized / 41 analysed;\npost-COVID cognitive impairment; "
                "transcranial + intranasal photobiomodulation, 8 weeks"),
]

# ---------------------------------------------------------------- panel B
PANEL_B = dict(
    label="Attokaren 2026",
    stat="Kruskal-Wallis \u03c7\u00b2(2) = 7.98, p = 0.018",
    note="test statistic, not an effect size \u2014 no magnitude axis",
    detail="62 healthy adults; single 1-hour session of 40 Hz audiovisual flicker "
           "vs constant light vs random flicker; psychomotor vigilance accuracy",
)

# ---------------------------------------------------------------- panel C
# Percent change from baseline over 6 months, active vs sham (one trial).
PANEL_C = [
    dict(structure="Cerebral white matter volume\n(Da 2024; N = 38)",
         active=0.17, active_err=1.08, sham=-2.54, sham_err=1.38),
    dict(structure="Corpus callosum area\n(Da 2024; N = 50, 33 active / 17 sham)",
         active=0.20, active_err=0.70, sham=-2.08, sham_err=0.87),
]

# ---

fig = plt.figure(figsize=(7.08, 7.4))
gs = fig.add_gridspec(3, 1, height_ratios=[1.25, 0.50, 1.20], hspace=0.55,
                      left=0.11, right=0.985, top=0.955, bottom=0.085)

# ----- Panel A -----------------------------------------------------------
axA = fig.add_subplot(gs[0])
ys = [1.70, 0.0]
for y, e in zip(ys, PANEL_A):
    axA.plot([e["lo"], e["hi"]], [y, y], color=COLORS["SST"], lw=1.6,
             solid_capstyle="butt", zorder=3)
    axA.plot([e["lo"], e["lo"]], [y - 0.10, y + 0.10], color=COLORS["SST"], lw=1.6, zorder=3)
    axA.plot([e["hi"], e["hi"]], [y - 0.10, y + 0.10], color=COLORS["SST"], lw=1.6, zorder=3)
    axA.plot([e["value"]], [y], marker="s", ms=6, color=COLORS["SST"],
             markeredgecolor="black", markeredgewidth=0.6, zorder=4)
    axA.annotate("{:g}  [{:g}, {:g}]".format(e["value"], e["lo"], e["hi"]),
                 xy=(e["value"], y), xytext=(0, -13), textcoords="offset points",
                 ha="center", va="top", fontsize=7.5, color="#111111")
    axA.text(0.005, y + 0.62, e["metric"], transform=axA.get_yaxis_transform(),
             fontsize=7.5, va="bottom", ha="left", color="#333333")
    axA.text(0.005, y + 0.56, e["detail"], transform=axA.get_yaxis_transform(),
             fontsize=7, va="top", ha="left", color="#666666", linespacing=1.4)

axA.axvline(0, color="#444444", lw=0.8, ls="--", zorder=1)
axA.set_yticks(ys)
axA.set_yticklabels([e["label"] for e in PANEL_A], fontweight="bold", fontsize=8.5)
axA.set_ylim(-0.75, 2.85)
axA.set_xlim(-0.65, 0.95)
axA.set_xlabel("effect estimate (row-specific scale; positions not comparable between rows)")
axA.set_title("A   Interval estimates in patient populations", loc="left",
              fontsize=10, fontweight="bold")
axA.spines["left"].set_visible(False)
axA.tick_params(axis="y", length=0)

# ----- Panel B -----------------------------------------------------------
axB = fig.add_subplot(gs[1])
axB.axis("off")
axB.set_title("B   Acute single session in healthy adults", loc="left",
              fontsize=10, fontweight="bold")
axB.add_patch(plt.Rectangle((0.0, 0.05), 1.0, 0.82, transform=axB.transAxes,
                            facecolor="#F4F4F4", edgecolor="#CCCCCC", lw=0.6))
axB.text(0.02, 0.68, PANEL_B["label"], transform=axB.transAxes, fontsize=8.5,
         fontweight="bold", va="center")
axB.text(0.22, 0.68, PANEL_B["stat"], transform=axB.transAxes, fontsize=9, va="center",
         color=COLORS["SST"])
axB.text(0.22, 0.44, PANEL_B["note"], transform=axB.transAxes, fontsize=7.5,
         va="center", style="italic", color=COLORS["conflict_marker"])
axB.text(0.02, 0.19, PANEL_B["detail"], transform=axB.transAxes, fontsize=7,
         va="center", color="#666666")

# ----- Panel C -----------------------------------------------------------
axC = fig.add_subplot(gs[2])
xs = [0, 1]
wbar = 0.3
for i, e in enumerate(PANEL_C):
    for off, key, errkey, colour, arm in ((-wbar / 2 - 0.02, "active", "active_err",
                                           COLORS["active_arm"], "active"),
                                          (+wbar / 2 + 0.02, "sham", "sham_err",
                                           COLORS["sham_arm"], "sham")):
        x = xs[i] + off
        axC.bar(x, e[key], width=wbar, color=colour, edgecolor="black", lw=0.6,
                zorder=2, label=arm if i == 0 else None)
        bars = axC.errorbar(x, e[key], yerr=e[errkey], fmt="none", ecolor="#333333",
                            elinewidth=1.0, capsize=3, zorder=3)
        for b in bars[2]:
            b.set_linestyle("--")
        va = "bottom" if e[key] >= 0 else "top"
        dy = e[errkey] + 0.18 if e[key] >= 0 else -(e[errkey] + 0.18)
        axC.text(x, e[key] + dy, "{:+.2f}".format(e[key]), ha="center", va=va,
                 fontsize=7.5)

axC.axhline(0, color="#444444", lw=0.8)
axC.set_xticks(xs)
axC.set_xticklabels([e["structure"] for e in PANEL_C], fontsize=8)
axC.set_ylabel("change from baseline over 6 months\n(percent of baseline)")
axC.set_xlim(-0.6, 1.6)
axC.set_ylim(-4.4, 2.2)
axC.legend(frameon=False, fontsize=8, loc="upper right", ncol=2)
axC.set_title("C   Structural measures, active versus sham (one randomized cohort, OVERTURE NCT03556280)",
              loc="left", fontsize=9.5, fontweight="bold")
axC.text(0.0, -0.30, "Error bars dashed: dispersion type not stated in either source. "
                     "The two structures are nested (corpus callosum lies within the white matter\n"
                     "compartment) and come from overlapping, unequal subsets of one trial \u2014 "
                     "not independent replication.",
         transform=axC.transAxes, fontsize=7, color="#666666", va="top", ha="left")

fig.text(0.11, 0.018, "Heterogeneous comparison \u2014 values not pooled; no summary estimate is drawn. "
                      "All values extracted from the source papers' full text.",
         fontsize=7.5, style="italic", color=COLORS["conflict_marker"], ha="left")

# ---

save_figure(fig, os.path.join(OUTDIR, "fig_sec10_gamma_stimulation_evidence_ladder.png"))
```
:::

(sec-10-replacement)=

## Interneuron replacement and interneuron-directed gene therapy

Cell replacement is the only strategy in this section that puts new inhibitory neurons into a diseased network, and its quantitative strength is concentrated in epilepsy. Medial ganglionic eminence (MGE) progenitors grafted into the adult epileptic hippocampus reduced spontaneous electrographic seizure frequency by 92%, to a reported frequency of 0.17 ± 0.09 in eight animals, with graft-derived cells characterised by patch clamp {cite:p}`Hunt2013`; a clinical-grade human embryonic stem cell-derived MGE-type product suppressed mesiotemporal seizures after a single intrahippocampal dose, with most animals becoming seizure-free and surviving longer {cite:p}`Bershteyn2023`; and a synthesis of neural stem cell graft outcomes in status epilepticus models collects reports that grafting limits the structural reorganisation accompanying those seizures — a different graft class from the MGE-derived progenitors above, at review level rather than as a single primary experiment {cite:p}`Wang2025c`. {numref}`fig-sec10-cell-and-circuit-interventions` sets these graft and vector quantities side by side, each on its own axis. The cell source is tractable: human pluripotent stem cells can be directed to NKX2.1+ progenitors that yield parvalbumin- and somatostatin-expressing cortical interneurons with appropriate synaptic properties {cite:p}`Maroof2013`, although those cells need roughly 30 weeks post-differentiation to acquire mature firing, with 5 of 7 recorded neurons identified as SST-positive {cite:p}`Nicholas2013`. Two facts restrict what this means for neurodegeneration. First, the SST yield is a minority of the graft: transplanted MGE progenitors differentiated into 41.3 ± 2.8% parvalbumin-positive, 21.6 ± 1.2% somatostatin-positive and 7.7 ± 0.8% nNOS-positive cells {cite:p}`Wang2025a`, so a graft is an inhibitory-tone intervention rather than an SST-selective one. Second, the host models are mostly not Alzheimer models — Fragile X {cite:p}`Wang2025a`, status epilepticus {cite:p}`Wang2025c`, early-life stress {cite:p}`Lin2025` — and the one amyloid-model graft retrieved here is a single study, reported both as a preprint {cite:p}`Yokomizo2025b` and as a journal record carrying the quantitative result, in which transplanted progenitors integrated into APP/PS1 cortex and raised slow-oscillation power relative to vehicle-treated hosts {cite:p}`Yokomizo2025a`. The limitation is that it stands alone, not that it is unpublished.

:::{admonition} Evidence Conflict
:class: warning
**Do unmodified interneuron progenitors suffice in an amyloid host?** Transplantation into J20 hAPP mice reduced behavioural abnormalities only when the grafted MGE cells overexpressed Nav1.1; wild-type MGE grafts gave no benefit, which the authors read as a requirement for molecular optimisation in a hyperexcitable, amyloid-laden brain {cite:p}`MartinezLosa2018`. Transplantation of unmodified embryonic interneuron progenitors into the hippocampal hilus of aged apoE4 knock-in and amyloid-model mice, by contrast, is reported to have restored normal learning and memory {cite:p}`Tong2014`. Host model, graft site and amyloid burden all differ, so the disagreement is resolvable by method rather than by arbitration between results — and it is precisely the variable, model construct, that {ref}`sec-conflicts-limitations` identifies as the dominant predictor of reported interneuron phenotypes.
:::

Gene therapy addressed to interneurons has the better-characterised toolkit. An adeno-associated virus carrying the mDlx enhancer restricted expression almost exclusively to GABAergic cells, with ~95% of transgene-expressing cells co-expressing GAD67 {cite:p}`Dimidschstein2016`, while a panel of candidate enhancers ranged from over 90% to below 5% parvalbumin specificity depending on which enhancer was used {cite:p}`VormsteinSchneider2020` — a spread that has not been independently replicated and that makes vector choice, not the concept, the determinant of selectivity. Payloads now include endogenous-locus activation by dCas9, which restored interneuron firing and attenuated febrile seizures in a Dravet model {cite:p}`Colasante2020`, and antisense de-repression, where AAV9-AntagoNAT raised survival from 50% to 84% and cut febrile seizure susceptibility from 73% to 7.7% in *Scn1a*+/− mice {cite:p}`Diaz2026`. Timing may constrain both: AAV gene replacement that worked neonatally produced no survival benefit at postnatal day 10 {cite:p}`Chen2025b`, an unreplicated result whose authors note that the loss of benefit could equally reflect reduced viral coverage at the later age as a closing developmental window — on the first reading it sets an uncomfortable timing constraint for a late-onset disease, on the second it sets none. The chemogenetic approach that would most directly test SST causality carries a ligand confound: clozapine-N-oxide (CNO) itself impaired object-location memory encoding whereas Compound 21 did not, with neither ligand altering overall neuronal or parvalbumin interneuron activity across dorsal hippocampal subregions, a result reported in a preprint {cite:p}`Bunce2026`. What is missing is not replication of that confound but replication of the rescue experiments it threatens — no published SST-interneuron chemogenetic rescue effect has been re-run here with a non-CNO ligand or with CNO-only controls. The one chemogenetic manipulation of a somatostatin-family population retrieved here went the other way, with repeated inhibition of cortistatin-expressing prelimbic neurons accelerating seizure kindling in female mice {cite:p}`Salisbury2026`.

:::{figure} ../figures/fig_sec10_cell_and_circuit_interventions.png
:name: fig-sec10-cell-and-circuit-interventions
:width: 100%
**Cell and vector interventions: five quantities, five axes.** (A) Electrographic seizure frequency in grafted epileptic animals {cite:p}`Hunt2013`. (B) Cortical slow-oscillation measure, donor-transplanted versus vehicle APP/PS1 {cite:p}`Yokomizo2025a`. (C) SST+ fraction of transplanted MGE-derived cells {cite:p}`Wang2025a`. (D) GAD67+ fraction of vector-transduced cells {cite:p}`Dimidschstein2016`. (E) Survival of treated *Scn1a*+/− animals {cite:p}`Diaz2026`. The panels use independent axes and independent units; no shared scale is implied and the magnitudes are not comparable. Different host pathologies: epilepsy confirmed at the time of grafting versus APP/PS1 amyloid deposition; only the APP/PS1 entry is a neurodegeneration model. Different graft and recording territories (hippocampus versus cortex); in the epilepsy study the seizure effect was site-specific — amygdala grafts did not alter seizure activity. Group n is stated for the epilepsy entry (n = 8); the amyloid entry's source states none, in its result sentence or its abstract. The control seizure rate is not shown: the source states a 92% reduction and a grafted frequency of 0.17 ± 0.09, and does not report the pre-graft rate, which cannot be derived from those two values. Both axes in A and B are labelled "units as published": the seizure-frequency unit is not given in its source, and the oscillation quantity is published as "× 10⁻⁷ control", which may be a normalisation to control rather than an absolute power. The slow-oscillation measurements are reported by their source as obtained with in vivo multiphoton calcium imaging and voltage-sensitive dye imaging; the panel-B quantity is an imaging-derived, control-referenced measure, not an electrophysiological power spectrum. In C–E the three percentages have three different denominators — transplanted MGE-derived cells, animals, vector-transduced cells — and are not a common efficacy scale; each occupies a separate sub-panel whose axis label names its denominator, and no two bars share a baseline. The SST+ fraction and the GAD67+ fraction differ by a level of the marker hierarchy — a graft-composition subtype fraction versus a pan-interneuron vector-specificity fraction — and measure different things; they are shown in separate sub-panels so that their heights are not compared. Interventions differ in kind: MGE-derived GABAergic precursor grafting, AAV9 antisense gene therapy, and a viral targeting vector. None of the studies in C–E uses a neurodegeneration model; the models are Fragile X syndrome, Dravet syndrome and wild-type vector testing. No entry in C–E reports a group size in its source sentence and the abstracts supply none, so no bar is weighted. The neuronal-loss quantities available for these models come from a narrative review's account of another laboratory's primary data and are not plotted here.
:::

:::{dropdown} 📓 Figure code
```python
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath("__file__")) if "__file__" not in globals() else os.path.dirname(os.path.abspath(__file__)))

import matplotlib.pyplot as plt
from shared_style import COLORS, apply_style, save_figure

apply_style()
OUTDIR = ".."   # notebooks live in figures/notebooks/; figures are written to figures/

# ---

# A: seizure frequency after MGE graft in epileptic hippocampus (Hunt 2013)
HUNT = dict(value=0.17, err=0.09, n=8)
# B: cortical slow-oscillation measure, vehicle vs donor-transplanted (Yokomizo 2025)
YOKO = dict(vehicle=0.22, vehicle_err=0.10, donor=1.1, donor_err=0.47)
# C: SST+ fraction of transplanted MGE-derived cells (Wang 2025)
WANG = dict(value=21.6, err=1.2)
# D: GAD67+ fraction of vector-transduced cells (Dimidschstein 2016)
DIMI = dict(value=95.0)
# E: survival of treated Scn1a+/- animals (Diaz 2026)
DIAZ = dict(start=50.0, end=84.0)

# ---

fig = plt.figure(figsize=(7.08, 6.0))
gs_top = fig.add_gridspec(1, 2, wspace=0.60, left=0.105, right=0.985,
                          top=0.94, bottom=0.60)
gs_bot = fig.add_gridspec(1, 3, wspace=0.95, left=0.105, right=0.985,
                          top=0.47, bottom=0.215)

# ----- A -----------------------------------------------------------------
axA = fig.add_subplot(gs_top[0, 0])
axA.bar([0], [HUNT["value"]], width=0.45, color=COLORS["mixed_GABAergic"],
        edgecolor="black", lw=0.6, zorder=2)
axA.errorbar([0], [HUNT["value"]], yerr=[HUNT["err"]], fmt="none", ecolor="#333333",
             elinewidth=1.0, capsize=3, zorder=3)
axA.text(0, HUNT["value"] + HUNT["err"] + 0.012, "0.17 \u00b1 0.09", ha="center",
         va="bottom", fontsize=8)
axA.set_xticks([0])
axA.set_xticklabels(["MGE graft into\nepileptic hippocampus"], fontsize=8)
axA.set_xlim(-0.6, 0.6)
axA.set_ylim(0, 0.42)
axA.set_ylabel("seizure frequency after graft\n(units as published)")
axA.set_title("A   Hunt 2013 \u2014 epilepsy model", loc="left", fontsize=9.5,
              fontweight="bold")
axA.text(0.03, 0.97, 'reported as a "92% reduction"; the pre-graft\nrate is not reported by the source\nn = 8 grafted epileptic animals',
         transform=axA.transAxes, fontsize=8, va="top", ha="left", color="#333333")

# ----- B -----------------------------------------------------------------
axB = fig.add_subplot(gs_top[0, 1])
axB.bar([0, 1], [YOKO["vehicle"], YOKO["donor"]], width=0.45,
        color=[COLORS["neutral_gray"], COLORS["mixed_GABAergic"]],
        edgecolor="black", lw=0.6, zorder=2)
axB.errorbar([0, 1], [YOKO["vehicle"], YOKO["donor"]],
             yerr=[YOKO["vehicle_err"], YOKO["donor_err"]], fmt="none",
             ecolor="#333333", elinewidth=1.0, capsize=3, zorder=3)
for x, v, e in ((0, YOKO["vehicle"], YOKO["vehicle_err"]), (1, YOKO["donor"], YOKO["donor_err"])):
    axB.text(x, v + e + 0.05, "{:g} \u00b1 {:g}".format(v, e), ha="center", va="bottom",
             fontsize=8)
axB.set_xticks([0, 1])
axB.set_xticklabels(["vehicle", "donor-transplanted"], fontsize=8)
axB.set_xlim(-0.6, 1.6)
axB.set_ylim(0, 2.1)
axB.set_ylabel("cortical slow-oscillation measure\n(\u00d7 10$^{-7}$ control; units as published)")
axB.set_title("B   Yokomizo 2025 \u2014 APP/PS1 amyloid model", loc="left",
              fontsize=9.5, fontweight="bold")
axB.text(0.03, 0.97, "p = 0.0033; group size not reported\nimaging-derived, control-referenced",
         transform=axB.transAxes, fontsize=8, va="top", ha="left", color="#333333")

# ----- C, D, E: three denominators, three axes ---------------------------
axC = fig.add_subplot(gs_bot[0, 0])
axC.bar([0], [WANG["value"]], width=0.4, color=COLORS["SST"], edgecolor="black",
        lw=0.6, zorder=2)
bars = axC.errorbar([0], [WANG["value"]], yerr=[WANG["err"]], fmt="none",
                    ecolor="#333333", elinewidth=1.0, capsize=3, zorder=3)
for b in bars[2]:
    b.set_linestyle("--")
axC.text(0, WANG["value"] + WANG["err"] + 1.5, "21.6 \u00b1 1.2", ha="center",
         va="bottom", fontsize=8)
axC.set_xticks([0])
axC.set_xticklabels(["Fmr1-KO\nhippocampus"], fontsize=8)
axC.set_xlim(-0.6, 0.6)
axC.set_ylim(0, 100)
axC.set_ylabel("SST+ cells\n(% of transplanted MGE-derived cells)", fontsize=8.5)
axC.set_title("C   Wang 2025", loc="left", fontsize=9.5, fontweight="bold")
axC.text(0.5, 0.86, "dispersion type\nnot stated;\nno group size", transform=axC.transAxes,
         fontsize=8, va="top", ha="left", color="#333333")

axD = fig.add_subplot(gs_bot[0, 1])
axD.bar([0], [DIMI["value"]], width=0.4, color=COLORS["mixed_GABAergic"],
        edgecolor="black", lw=0.6, zorder=2)
axD.text(0, DIMI["value"] + 1.5, "~95", ha="center", va="bottom", fontsize=8)
axD.set_xticks([0])
axD.set_xticklabels(["mDlx-enhancer AAV,\nwild-type brain"], fontsize=8)
axD.set_xlim(-0.6, 0.6)
axD.set_ylim(0, 100)
axD.set_ylabel("GAD67+ cells\n(% of vector-transduced cells)", fontsize=8.5)
axD.set_title("D   Dimidschstein 2016", loc="left", fontsize=9.5, fontweight="bold")
axD.text(0.5, 0.86, "source's own\napproximation;\nno group size", transform=axD.transAxes,
         fontsize=8, va="top", ha="left", color="#333333")

axE = fig.add_subplot(gs_bot[0, 2])
axE.bar([0, 1.4], [DIAZ["start"], DIAZ["end"]], width=0.5,
        color=[COLORS["neutral_gray"], COLORS["primary_green"]],
        edgecolor="black", lw=0.6, zorder=2)
for x, v in ((0, DIAZ["start"]), (1.4, DIAZ["end"])):
    axE.text(x, v + 1.5, "{:g}".format(v), ha="center", va="bottom", fontsize=8)
axE.set_xticks([0, 1.4])
axE.set_xticklabels(["from", "to"], fontsize=8.5)
axE.set_xlim(-0.9, 2.3)
axE.set_ylim(0, 100)
axE.set_ylabel("animals surviving\n(% of Scn1a+/- animals)", fontsize=8.5)
axE.set_title("E   Diaz 2026", loc="left", fontsize=9.5, fontweight="bold")
axE.text(0.0, -0.13, 'quoted: survival "from 50% to 84%"\nin AAV9-AntagoNAT-treated mice;\nno group size reported',
         transform=axE.transAxes, fontsize=8, va="top", ha="left", color="#333333")

fig.text(0.105, 0.095,
         "Heterogeneous comparison \u2014 values not pooled. Five quantities, five axes: no magnitude is comparable across panels, and no two bars share a baseline.",
         fontsize=7.5, style="italic", color=COLORS["conflict_marker"], ha="left")
fig.text(0.105, 0.062,
         "Host models: confirmed epilepsy (A), APP/PS1 amyloid (B), Fragile X syndrome (C), wild-type vector characterisation (D), Scn1a+/- Dravet syndrome (E).",
         fontsize=7.5, color="#444444", ha="left")
fig.text(0.105, 0.029,
         "All values extracted from the source papers' full text. Units in A and B are not defined by their sources.",
         fontsize=7.5, color="#444444", ha="left")

# ---

save_figure(fig, os.path.join(OUTDIR, "fig_sec10_cell_and_circuit_interventions.png"))
```
:::

(sec-10-excitability)=

## Lowering network excitability pharmacologically

The excitability-lowering literature is the best-designed in this section and the clearest about what it has not achieved. Its clinical rationale is that patients with amnestic mild cognitive impairment (aMCI) or Alzheimer's disease (AD) who also have epilepsy or subclinical epileptiform activity decline earlier, cognitive decline beginning before 65 years in 50% of aMCI-epilepsy cases versus 21% without (P = .051) and in 51% versus 26% of AD cases (P = .002) {cite:p}`Vossel2013` — the AD comparison carries the weight, the aMCI one does not reach the conventional threshold. The target engagement result is the strongest of its kind: low-dose levetiracetam reduced hippocampal hyperactivity and improved the hyperactivity-sensitive pattern-separation task while leaving standard delayed-recall measures unchanged in the same 17 patients {cite:p}`Bakker2012` — a pre-specified direction with a reported null on the non-targeted measure. The drug's mechanism is presynaptic, acting through SV2A, since brain membranes from SV2A-null mice do not bind a tritiated levetiracetam derivative {cite:p}`Lynch2004`, with its in vivo anticonvulsant effect abolished by a benzodiazepine-site inverse agonist {cite:p}`Rigo2002`. Scaling up, the randomized crossover trial found no overall cognitive change (NIH-EXAMINER mean difference 0.07 points, 95% CI −0.18 to 0.32, P = .55) but a 7.4-point Stroop interference improvement (95% CI 0.2–14.7) confined to the prespecified epileptiform-activity subgroup {cite:p}`Vossel2021`; a synthesis of five clinical studies found cognitive change reported in four {cite:p}`Mohamadi2025`. Seizures themselves respond well — 72.7% of a 22-patient prodromal AD cohort achieved seizure freedom and 95.4% a ≥50% reduction {cite:p}`Cretin2026` — against responder rates of 30–50% in unselected epilepsy trials, where the companion benchmark, a 20–30% median reduction in seizure frequency, is a different quantity and shares no denominator with a proportion of patients {cite:p}`Loscher2021`. Which model is used matters: as reviewed in a case for screening antiseizure drugs across several Alzheimer models, kindling outcomes diverge between APP/PS1 and PSEN2-N141I lines, an account of other groups' experiments whose primary reports were not retrieved here {cite:p}`Barbour2025`. {numref}`fig-sec10-excitability-lowering-outcomes` places these three outcome types on three separate axes, which is the only honest way to show them together. The gap this leaves is the one that matters for the thesis: symptom control is demonstrated, disease modification is not.

:::{admonition} Evidence Conflict
:class: warning
**Does lowering excitability change the cognitive trajectory?** The randomized crossover trial reports no overall benefit on its primary composite {cite:p}`Vossel2021`, while a pharmacoepidemiologic analysis drawing on a database of more than 75 million adults aged 55 or older associates sodium-channel-blocking antiseizure medications with a 27% lower hazard of incident all-cause dementia (HR = 0.73, 95% CI 0.61–0.88) and a 34% lower hazard of Alzheimer's disease, relative to levetiracetam/brivaracetam {cite:p}`FerreiraAtuesta2026`. Drug class, design and outcome definition all differ — an SV2A ligand tested on short-term cognition against sodium channel blockers assessed on long-term incidence, with levetiracetam serving as index drug in one and reference drug in the other — so this is resolvable by method rather than a contradiction of results, and the observational estimate carries the confounding-by-indication that its design implies.
:::

:::{figure} ../figures/fig_sec10_excitability_lowering_outcomes.png
:name: fig-sec10-excitability-lowering-outcomes
:width: 100%
**Excitability-lowering drugs: three outcome types, three axes.** (A) Proportion of patients seizure-free in an epileptic prodromal-AD cohort {cite:p}`Cretin2026`. (B) NIH-EXAMINER composite, mean difference versus placebo {cite:p}`Vossel2021`. (C) Hazard ratio for incident all-cause dementia against an active comparator {cite:p}`FerreiraAtuesta2026`. The margin quotes a review-level benchmark {cite:p}`Loscher2021` that has no position on any axis. Panels use different outcome types and are not on a shared scale: a cognitive composite difference in points, a proportion of patients seizure-free, a hazard ratio (null = 1) and a median percent seizure-frequency reduction. The reported n of 75 million is the size of the source database of adults aged 55+, not the analysed cohort of patients with late-onset unexplained epilepsy, which the source does not state; the figure carries "analysed cohort not reported". The hazard ratio 0.73 is against an active comparator (levetiracetam/brivaracetam), not placebo; its own source notes that individual agents such as phenytoin, carbamazepine and lamotrigine showed divergent safety and efficacy profiles. The levetiracetam value of 0.07 points is a null primary outcome (P = .55); the trial's positive signals were restricted to the prespecified epileptiform-activity subgroup. The 72.7% seizure-freedom figure is a single-arm proportion in 22 patients (16 of 22) from a cohort its authors describe as exploratory and underpowered; in the abstract that caveat is attached to the cohort's cognitive-decline and medication comparisons rather than specifically to the seizure-freedom proportion. The 20–30% figure is a review-level generalization across epilepsy regulatory trials in unselected epilepsy patients, not a dementia population. It is a percent reduction in seizure frequency, not a percent of patients, so it shares no denominator with the 72.7% seizure-freedom proportion; it is quoted as text with no position on any axis and is not a comparable data point. The observation that individual agents showed divergent safety and efficacy profiles belongs to the hazard-ratio source, not to the review that supplies the 20–30% benchmark. Levetiracetam is the index drug in the cognitive panel and the reference drug in the dementia-incidence panel.
:::

:::{dropdown} 📓 Figure code
```python
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath("__file__")) if "__file__" not in globals() else os.path.dirname(os.path.abspath(__file__)))

import matplotlib.pyplot as plt
from shared_style import COLORS, apply_style, save_figure

apply_style()
OUTDIR = ".."   # notebooks live in figures/notebooks/; figures are written to figures/

# ---

CRETIN = dict(value=72.7, label="16 of 22 patients")
VOSSEL = dict(value=0.07, lo=-0.18, hi=0.32)
FERREIRA = dict(value=0.73, lo=0.61, hi=0.88)
LOSCHER_QUOTE = ('Loscher 2021 (benchmark, no axis position): "Most ASMs achieve 20-30% median '
                 'seizure frequency reduction over and above\nplacebo effect and a 30-50% responder rate." '
                 'Unselected epilepsy patients in regulatory trials - not a dementia population. '
                 'This is a percent\nreduction in seizure frequency, not a percent of patients, '
                 'so it shares no denominator with panel A and is not a comparable data point.')

# ---

fig = plt.figure(figsize=(7.08, 5.1))
gs = fig.add_gridspec(1, 3, wspace=0.80, left=0.095, right=0.985, top=0.93, bottom=0.50)

# ----- A: proportion seizure-free ---------------------------------------
axA = fig.add_subplot(gs[0, 0])
axA.bar([0], [CRETIN["value"]], width=0.42, color=COLORS["primary_green"],
        edgecolor="black", lw=0.6, zorder=2)
axA.text(0, CRETIN["value"] + 2, "72.7", ha="center", va="bottom", fontsize=8.5)
axA.set_xticks([0])
axA.set_xticklabels(["routine ASM,\nsingle arm"], fontsize=8)
axA.set_xlim(-0.6, 0.6)
axA.set_ylim(0, 100)
axA.set_ylabel("patients seizure-free\n(% of the 22-patient cohort)", fontsize=8.5)
axA.set_title("A   Cretin 2026\nseizure control", loc="left", fontsize=9, fontweight="bold")
axA.text(0.0, -0.22, "16 of 22 patients; no comparator;\nauthors describe the cohort as\nexploratory and underpowered",
         transform=axA.transAxes, fontsize=8, va="top", ha="left", color="#333333")

# ----- B: cognitive composite, mean difference vs placebo ----------------
axB = fig.add_subplot(gs[0, 1])
axB.axhline(0, color="#444444", lw=0.9, ls="--", zorder=1)
axB.plot([0, 0], [VOSSEL["lo"], VOSSEL["hi"]], color=COLORS["primary_purple"], lw=1.6, zorder=3)
for yv in (VOSSEL["lo"], VOSSEL["hi"]):
    axB.plot([-0.07, 0.07], [yv, yv], color=COLORS["primary_purple"], lw=1.6, zorder=3)
axB.plot([0], [VOSSEL["value"]], marker="s", ms=7, color=COLORS["primary_purple"],
         markeredgecolor="black", markeredgewidth=0.8, zorder=4)
axB.text(0.11, VOSSEL["value"], "0.07*\n[-0.18, 0.32]\nP = .55", fontsize=8, va="center",
         ha="left")
axB.set_xticks([0])
axB.set_xticklabels(["levetiracetam\nvs placebo"], fontsize=8)
axB.set_xlim(-0.45, 0.95)
axB.set_ylim(-0.45, 0.55)
axB.set_ylabel("NIH-EXAMINER composite,\nmean difference vs placebo (points)", fontsize=8.5)
axB.set_title("B   Vossel 2021\ncognition in AD", loc="left", fontsize=9, fontweight="bold")

# ----- C: hazard ratio for incident dementia -----------------------------
axC = fig.add_subplot(gs[0, 2])
axC.set_yscale("log")
axC.axhline(1.0, color="#444444", lw=0.9, ls="--", zorder=1)
axC.plot([0, 0], [FERREIRA["lo"], FERREIRA["hi"]], color=COLORS["primary_orange"],
         lw=1.6, zorder=3)
for yv in (FERREIRA["lo"], FERREIRA["hi"]):
    axC.plot([-0.07, 0.07], [yv, yv], color=COLORS["primary_orange"], lw=1.6, zorder=3)
axC.plot([0], [FERREIRA["value"]], marker="s", ms=7, color=COLORS["primary_orange"],
         markeredgecolor="black", markeredgewidth=0.8, zorder=4)
axC.text(0.11, FERREIRA["value"], "0.73*\n[0.61, 0.88]", fontsize=8, va="center", ha="left")
axC.set_xticks([0])
axC.set_xticklabels(["sodium channel blockers\nvs levetiracetam/brivaracetam"], fontsize=7.5)
axC.set_xlim(-0.45, 0.95)
axC.set_ylim(0.5, 1.6)
axC.set_yticks([0.5, 0.7, 1.0, 1.4])
axC.set_yticklabels(["0.5", "0.7", "1.0", "1.4"])
axC.minorticks_off()
axC.set_ylabel("hazard ratio for incident\nall-cause dementia (log scale)", fontsize=8.5)
axC.set_title("C   Ferreira-Atuesta 2026\nincident dementia", loc="left", fontsize=9,
              fontweight="bold")
axC.text(0.40, 0.98, "analysed cohort\nnot reported", transform=axC.transAxes,
         fontsize=8, va="top", ha="left", color="#333333")

# ----- margin: benchmark quoted as text, no axis position ----------------
fig.patches.append(plt.Rectangle((0.095, 0.145), 0.89, 0.150, transform=fig.transFigure,
                                 facecolor="#F4F4F4", edgecolor="#CCCCCC", lw=0.6,
                                 zorder=0))
fig.text(0.107, 0.283, LOSCHER_QUOTE, fontsize=7.5, va="top", ha="left", color="#333333",
         linespacing=1.45)

fig.text(0.095, 0.105, "Heterogeneous comparison \u2014 values not pooled; the three panels have three different null values "
                       "(a proportion, zero, and one) and no summary estimate is drawn.",
         fontsize=7.5, style="italic", color=COLORS["conflict_marker"], ha="left")
fig.text(0.095, 0.065, "* Value extracted from the abstract; full text was not accessible. "
                       "Panel A's value comes from the source's full text.",
         fontsize=7.5, color="#444444", ha="left")
fig.text(0.095, 0.025, "Levetiracetam is the index drug in panel B and the reference drug in panel C.",
         fontsize=7.5, color="#444444", ha="left")

# ---

save_figure(fig, os.path.join(OUTDIR, "fig_sec10_excitability_lowering_outcomes.png"))
```
:::

(sec-10-neuromodulation)=

## Neuromodulation of circuits: fornix stimulation as a cautionary case

Fornix deep brain stimulation shows the design gradient in a single programme. The open-label phase I study reported an early and striking reversal of temporal and parietal glucose hypometabolism maintained through 12 months of continuous stimulation, with possible slowing of decline in some patients {cite:p}`Laxton2010`. The randomized double-blind trial that followed found that the primary measures, ADAS-cog-13 and CDR-SB, did not differentiate active from sham after 12 months {cite:p}`Targum2021`. Chronic intracranial recordings then supplied a mechanism for the null: continuous stimulation overdrove fornix-to-hippocampus connectivity while attenuating hippocampal feedback, which the authors characterise as an electrical lesion {cite:p}`Stanslaski2026` — a single recent report with no replication. Interpreting volumetric endpoints in this programme requires the natural-history baseline, in which 67.5% of 40 comparison patients lost hippocampal volume over 12 months at a 3% threshold, 32.5% were unchanged and none gained {cite:p}`Germann2025`; the wider surgical literature reports both attenuation of decline and postoperative adverse effects {cite:p}`Swietlik2024`. Non-invasive stimulation faces the same gradient at smaller scale: two weeks of precuneus rTMS produced a domain-selective episodic memory improvement {cite:p}`Koch2018`, dual-target cerebellar TMS with striatal temporal-interference stimulation improved working-memory accuracy during distraction in mild cognitive impairment with Lewy bodies, but not under high load {cite:p}`Nencha2026`, and transcranial direct current stimulation has a measurable neurochemical footprint — anodal stimulation lowers local GABA, cathodal stimulation lowers glutamatergic activity {cite:p}`Stagg2009`, and baseline sensorimotor GABA concentration predicts motor performance (r = 0.64, p = 0.03, uncorrected) {cite:p}`Stagg2011` — though these two magnetic resonance spectroscopy reports share a senior author and are convergence within one programme rather than independent replication, the standard applied to the agonist series above. Yet current trials remain feasibility-scale, one powered at 36 participants {cite:p}`Kuo2026`. None of these methods reads out SST-cell function specifically, although paired-pulse TMS does index inhibitory circuit integrity in neurodegeneration: short-latency afferent inhibition is markedly weaker in Alzheimer's disease than in age-matched controls (responses reduced to 85.7 ± 15.8% of test size versus 45.3 ± 16.2%) {cite:p}`DiLazzaro2002`, and absent short-interval intracortical inhibition has 97% sensitivity for ALS {cite:p}`Vucic2012`.

:::{admonition} Evidence Conflict
:class: warning
**Does fornix stimulation activate or functionally lesion the hippocampal circuit?** Metabolic imaging in the uncontrolled phase I cohort was read as circuit activation {cite:p}`Laxton2010`; directed electrophysiological connectivity in chronically implanted patients indicates the opposite, that continuous stimulation disrupts bidirectional fornix–hippocampus communication {cite:p}`Stanslaski2026`. The dimension is inference from metabolism versus inference from directed connectivity, and the question is open; the randomized sham-controlled null {cite:p}`Targum2021` is consistent with either reading, which is why the mechanistic recordings matter more than the trial result.
:::

(sec-10-testable)=

## What would make an SST-targeted therapy testable

Three requirements follow from the preceding evidence, and each names an experiment that was not retrieved by these searches rather than one that failed. First, an SST-selective manipulation inside a disease model: the entrainment literature drives parvalbumin circuitry, as the survey that reports the medial-septal experiment describes {cite:p}`Zhang2024a`, grafts deliver mixed populations in which SST cells are a minority {cite:p}`Wang2025a`, and the chemogenetic tools that could isolate the class carry a ligand confound whose consequences for published rescue effects have not been tested with a non-CNO ligand here {cite:p}`Bunce2026`, so the "tractable target" framing is an extrapolation and should be read as one. Second, a brain-penetrant SSTR4 agonist with a pharmacodynamic marker: the existing in vivo results come from one compound and one programme {cite:p}`Sandoval2011, Sandoval2012, Sandoval2013, Sandoval2019`, the approved analogue class cannot reach the relevant subtype {cite:p}`Patel1999`, and the structural determinants of subtype selectivity are known well enough to design against {cite:p}`Zhao2022`. Brain entry of that compound has been measured directly (entry rate K(i) = 0.25 µl/g min, with about 93% associated with the parenchymal component) {cite:p}`Sandoval2011`, and an amyloid-model efficacy study exists within the same programme, with learning improved and soluble Aβ oligomers reduced in APPswe Tg2576 mice {cite:p}`Sandoval2013`; what is missing is a concentration-at-target measurement tied to efficacy, an independent programme, and any tau-model study. Third, an endpoint matched to the lesion: trials in this literature test global cognition, yet the circuit function attributable to SST cells ({ref}`sec-sst-identity`, {ref}`sec-circuit-consequences`) is dendritic inhibition and the coordination of non-rapid-eye-movement oscillations, which is where graft-mediated rescue of slow oscillations {cite:p}`Yokomizo2025b` and the subtype-divergent EEG entrainment response {cite:p}`Chan2025` point, and which {ref}`sec-human-evidence` identifies as lacking a biomarker-grade readout; {ref}`sec-conclusion` returns to these three requirements as the conditions under which the causal question could be answered. No head-to-head comparison of gamma entrainment, transplantation, antiseizure pharmacology and SSTR agonism on a common endpoint in a single model was retrieved either, so the apparent breadth of this field conceals an absence of comparative evidence.

Two features of the evidence behind this section limit how firmly any of it can be stated. Retrieval was dominated by one literature database with no citation chasing, so every statement above that an experiment was not found is a statement about these searches and not about the field; disconfirming-evidence searches were capped per query, so the reported nulls are a top-relevance sample rather than a census. Full text was available for 58 of the 86 records behind this section, with the shortfall concentrated in older closed-access material, and the replication ceiling here is low: most findings carry no identified replicating study, which is why no therapeutic claim in this section is called replicated unless the replicating work is named. The therapeutic failures catalogued here are not randomly distributed. They cluster exactly where the causal chain was extrapolated rather than demonstrated — from parvalbumin to SST, from epilepsy host to amyloid host, from rodent molecular endpoint to patient cognition, from a programme's internal convergence to independent replication. {ref}`sec-conflicts-limitations` anatomises those extrapolations across the whole review.

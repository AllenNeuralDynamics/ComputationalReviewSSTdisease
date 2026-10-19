(sec-circuit-consequences)=

# Circuit Consequences: Dendritic Inhibition, Oscillations, Sleep, and Memory

The cellular descriptions assembled in {ref}`sec-alzheimers` through {ref}`sec-als-ftd` — Alzheimer's disease, the Lewy body disorders, Huntington's disease and the ALS-FTD spectrum — do not agree about what happens to somatostatin-expressing interneurons in a degenerating brain. Interneurons are scored as hyperactive in one amyloid model and as hypoactive in another {cite:p}`MelgosaEcenarro2026, Meftah2026`. Somatostatin-immunoreactive density falls in ageing cortex, yet stereology finds no change in SST+ cell number in a transgenic model {cite:p}`Ouellet2014, Futacsi2025`.

Read as competing accounts of one cell, they cannot all be right. Read as inputs to a circuit, most of them converge. What propagates downstream is not how many somatostatin-immunoreactive somata a section contains, but how much inhibition reaches distal pyramidal dendrites and how precisely it is timed {cite:p}`Yao2025, Udakis2020`.

SST interneurons are described as roughly half of the GABAergic population and as primarily targeting dendritic compartments. In dentate gyrus their input to adult-born granule cells produces mixed inward and outward synaptic responses, which betray electrotonically distant release sites {cite:p}`Groisman2020`. Dendritic SST inhibition is routinely described as gating the integration of proximal and distal inputs, and thereby pyramidal gain {cite:p}`Taxidis2025`. Its primary demonstrations are cited secondhand instead of shown, so the formulation is treated here as a prevailing model to be tested and not as a settled result.

The dendritic targeting and the VIP-SST-PV motif established in {ref}`sec-sst-identity` are the mechanism. What follows is what measurably breaks when it weakens, and which cellular contradictions survive translation into a circuit prediction.

(sec-08-dendritic-signature)=

## The dendritic signature: what SST manipulation does that PV manipulation does not

The functional signature underwriting the circuit argument comes from three preparations measuring three different quantities. In one respect it is weaker than usually reported.

Sustained photoinhibition of SST+ interneurons reliably decreased cholinergically induced slow gamma power in ventral hippocampal CA3 ex vivo, to 0.69 ± 0.057 of the baseline period (t = 5.40, p < 0.001, one-sample t test) {cite:p}`Antonoudiou2020`. The same study reports that disrupting either PV+ or SST+ interneuron activity reduces slow gamma power, but the sentence carrying the measurement quantifies only the SST+ arm. The frequently repeated claim that SST silencing reduces gamma *more* than PV silencing is therefore weaker than its repetition suggests.

Where the two classes were measured against each other with the same readout, the perisomatic class won. In prefrontal cortex in vivo, wide-spiking units were suppressed with an index of 0.39 ± 0.02 on SST activation (n = 25 units) against 0.50 ± 0.01 on PV activation (n = 22 units; P < 0.0001, unpaired t test) {cite:p}`Liu2020b`. Peak suppression also arrived later for SST than for PV cells (9.92 ± 0.29 ms versus 6.73 ± 0.28 ms).

Chemogenetic inactivation in frontal cortex reproduces that asymmetry. PV+ inactivation changed peak membrane potential during hippocampal input by 4.19 ± 0.98 mV against -2.39 ± 1.23 mV in controls, whereas SOM+ inactivation produced 0.66 ± 0.94 mV {cite:p}`Zhang2024b`.

A null completes the dendritic reading. Potentiation of SST inhibitory synapses left action-potential generation from Schaffer-collateral stimulation essentially unchanged (0.53 ± 0.04 against 0.5 ± 0.08 after SST-iLTP, n = 8 cells, p > 0.05) {cite:p}`Udakis2020`. In addition, suppressing SST cells during the critical period raised inferred pyramidal spike rates without altering input tuning {cite:p}`Yaeger2019`.

Weaker, slower and invisible at the spike threshold is what dendritic targeting predicts, and not evidence that SST cells matter less. {numref}`fig-sec8-dendritic-versus-perisomatic-signature` sets the three quantities out panel by panel.

:::{figure} ../figures/fig_sec8_dendritic_versus_perisomatic_signature.png
:name: fig-sec8-dendritic-versus-perisomatic-signature
:width: 100%
**Three quantities, three preparations.** (A) Slow gamma power during SST+ interneuron photoinhibition, as a fraction of the baseline period: 0.69 ± 0.057 (t = 5.40, p < 0.001, one-sample t test) {cite:p}`Antonoudiou2020`. (B) Wide-spiking unit firing-suppression index on SST versus PV interneuron activation: 0.39 ± 0.02 (SST, n = 25) and 0.50 ± 0.01 (PV, n = 22); P < 0.0001, unpaired t test {cite:p}`Liu2020b`. (C) Spike probability from Schaffer-collateral stimulation before and after SST-iLTP: 0.53 ± 0.04 versus 0.5 ± 0.08 (n = 8, p > 0.05) {cite:p}`Udakis2020`. Caveats carried with this figure: {cite:t}`Antonoudiou2020` recorded cholinergically induced slow gamma in ventral hippocampal CA3 ex vivo. The three panels are three different quantities (fraction of baseline gamma power; dimensionless firing-suppression index; spike probability) plotted on separate axes and must not be read as a common scale. Index polarity is not shared: in panel A a smaller value means a larger effect of SST photoinhibition, whereas in panel B a larger suppression index means stronger suppression; panels A and B each carry an explicit direction-of-effect arrow, and panel C carries none because it is a null within-condition comparison for which no direction is claimed. Only panel B is a quantified SST-versus-PV contrast — {cite:t}`Antonoudiou2020`'s source sentence reports no number for the PV arm, so no PV value is plotted in panel A, and the absence of a PV bar must not be read as an absent PV effect, since that study reports that disrupting either PV+ or SST+ interneuron activity reduces slow gamma power. Panel C is a within-condition comparison in the same cells and is a null result, not an SST-versus-PV contrast. In panel C the measured unit is the postsynaptic CA1 pyramidal cell, not a property of the SST interneuron; in panel B the measured unit is likewise the wide-spiking unit rather than the SST or PV interneuron that is optogenetically activated, the interneuron being the manipulated population in both panels. Preparations differ: ventral hippocampal CA3 ex vivo (A), prefrontal cortex in vivo (B), CA1 slices (C) — two of three are ex vivo. The stimulation condition under which the suppression indices of panel B were obtained is not stated in the source sentence; that study's abstract reports frequency-specific optogenetic manipulations during social interaction, which does not establish the condition behind these indices. Sample sizes count different things: no sample size is stated in A, wide-spiking units per arm in B, and cells in C; each arm of panel B carries its own n.
:::

:::{dropdown} 📓 Figure code
```python
import sys, os

# Resolve paths so the notebook runs from either its own directory or the repo root.
HERE = os.path.abspath(".") if os.path.exists("shared_style.py") else os.path.abspath("figures/notebooks")
sys.path.insert(0, HERE)
OUTDIR = os.path.normpath(os.path.join(HERE, ".."))

import matplotlib.pyplot as plt
from shared_style import COLORS, apply_style, save_figure

apply_style()
plt.rcParams.update({"font.size": 10, "legend.fontsize": 9})  # figure authored at the 10 pt document size

# ---

# --- Values: every number below is verbatim in that entry's source sentence ---
# Antonoudiou et al. 2020 (10.1523/jneurosci.0261-20.2020) -> panel A
A = dict(value=0.69, err=0.057, stat="t = 5.40, p < 0.001 (one-sample t test)\nn not reported")
# Liu et al. 2020 (10.1126/sciadv.aay4073) -> panel B
B = dict(sst=0.39, sst_err=0.02, sst_n=25, pv=0.50, pv_err=0.01, pv_n=22,
         stat="P < 0.0001, unpaired t test")
# Udakis et al. 2020 (10.1038/s41467-020-18074-8) -> panel C
C = dict(base=0.53, base_err=0.04, post=0.5, post_err=0.08,
         stat="n = 8, p > 0.05\nwithin-condition null")

# ---

fig, axes = plt.subplots(1, 3, figsize=(7.1, 3.3))
fig.subplots_adjust(wspace=0.70, bottom=0.30)

# ---------------- Panel A: fraction of baseline gamma power -------------------
ax = axes[0]
ax.errorbar([0], [A["value"]], yerr=[A["err"]], fmt="o", ms=7,
            color=COLORS["sst"], ecolor=COLORS["sst"], elinewidth=1.2,
            capsize=4, linestyle="none")
ax.axhline(1.0, ls=":", lw=1.0, color=COLORS["neutral_gray"])
ax.text(0.62, 1.01, "baseline", fontsize=8, va="bottom", ha="right",
        color=COLORS["neutral_gray"])
ax.annotate("", xy=(0.55, 0.30), xytext=(0.55, 0.75),
            arrowprops=dict(arrowstyle="->", lw=1.1, color=COLORS["decrease"]))
ax.text(0.60, 0.52, "larger\neffect", fontsize=8, va="center", ha="left",
        color=COLORS["decrease"])
ax.text(0, A["value"] + A["err"] + 0.06, "0.69", fontsize=8, ha="center")
ax.set_xlabel(A["stat"], fontsize=8, labelpad=6)
ax.set_xlim(-0.6, 1.1); ax.set_ylim(0, 1.3)
ax.set_xticks([0]); ax.set_xticklabels(["SST+\nphotoinhibition"], fontsize=9)
ax.set_ylabel("Slow gamma power\n(fraction of baseline period)")
ax.set_title("A  Antonoudiou 2020", fontsize=11, fontweight="bold", loc="left")

# ---------------- Panel B: firing-suppression index ---------------------------
ax = axes[1]
ax.errorbar([0], [B["sst"]], yerr=[B["sst_err"]], fmt="o", ms=7, color=COLORS["sst"],
            ecolor=COLORS["sst"], elinewidth=1.2, capsize=4, linestyle="none")
ax.errorbar([1], [B["pv"]], yerr=[B["pv_err"]], fmt="s", ms=7, color=COLORS["pv"],
            ecolor=COLORS["pv"], elinewidth=1.2, capsize=4, linestyle="none")
ax.text(0, B["sst"] - B["sst_err"] - 0.03, "0.39\nn = 25", fontsize=8, ha="center", va="top")
ax.text(1, B["pv"] + B["pv_err"] + 0.03, "0.50\nn = 22", fontsize=8, ha="center", va="bottom")
ax.annotate("", xy=(1.62, 0.60), xytext=(1.62, 0.30),
            arrowprops=dict(arrowstyle="->", lw=1.1, color=COLORS["increase"]))
ax.text(1.57, 0.45, "stronger\nsuppression", fontsize=8, va="center", ha="right",
        color=COLORS["increase"])
ax.set_xlabel(B["stat"], fontsize=8, labelpad=6)
ax.set_xlim(-0.4, 1.75); ax.set_ylim(0, 0.72)
ax.set_xticks([0, 1]); ax.set_xticklabels(["SST\nactivation", "PV\nactivation"], fontsize=9)
ax.set_ylabel("Wide-spiking unit\nfiring-suppression index")
ax.set_title("B  Liu 2020", fontsize=11, fontweight="bold", loc="left")

# ---------------- Panel C: spike probability ----------------------------------
ax = axes[2]
ax.errorbar([0, 1], [C["base"], C["post"]], yerr=[C["base_err"], C["post_err"]],
            fmt="o", ms=7, color=COLORS["excitatory_pyramidal"],
            ecolor=COLORS["excitatory_pyramidal"], elinewidth=1.2, capsize=4,
            linestyle="-", lw=1.0)
ax.text(0, C["base"] + C["base_err"] + 0.05, "0.53", fontsize=8, ha="center")
ax.text(1, C["post"] + C["post_err"] + 0.05, "0.5", fontsize=8, ha="center")
ax.set_xlabel(C["stat"], fontsize=8, labelpad=6)
ax.set_xlim(-0.5, 1.5); ax.set_ylim(0, 0.95)
ax.set_xticks([0, 1]); ax.set_xticklabels(["baseline", "after\nSST-iLTP"], fontsize=9)
ax.set_ylabel("Spike probability\n(Schaffer-collateral stimulation)")
ax.set_title("C  Udakis 2020", fontsize=11, fontweight="bold", loc="left")

for ax in axes:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

fig.text(0.5, 0.005,
         "Heterogeneous comparison - values not pooled: three different quantities on three independent axes. "
         "Error bars are the source sentences' own +/- terms (dispersion type not stated).\n"
         "Preparations: ventral hippocampal CA3 ex vivo (A), prefrontal cortex in vivo (B), CA1 slices (C).",
         ha="center", va="bottom", fontsize=8, color=COLORS["neutral_gray"])

# ---

save_figure(fig, os.path.join(OUTDIR, "fig_sec8_dendritic_versus_perisomatic_signature.png"))
```
:::

Where and when these cells fire reinforces the compartment claim. SST cells are required for phase-locking to a context-dependent low-gamma rhythm that grows with stimulus size, peaking at 32 ± 1 Hz at 21 degrees across 32 mice {cite:p}`Veit2017`.

Their recruitment is also strongly brain-state dependent:

- during sleep, bistratified and PV+ basket cells fired 16.9 and 19.2 Hz faster than O-LM cells (t(10) = 2.35, p = 0.0407; t(10) = 2.75, p = 0.0204) {cite:p}`Katona2014`
- an identified O-LM-like neuron was recruited by sharp-wave ripples in quiet wakefulness but not in sleep ripples {cite:p}`Katona2017`
- a sparse long-range Sst population labelled in two intersectional lines was intensely active in slow-wave sleep and quiet wakefulness, and suppressed in movement and REM, in 95 of 111 superficial-layer cells {cite:p}`Ratliff2026`

Timing within the local circuit points the same way. In the dentate gyrus, putative SST cells fire last in the dentate spike sequence, at +1.5 ms after the peak against -1.5 ms for putative PV cells {cite:p}`Hainmueller2026` — the delayed-feedback position the dendritic account requires. In anterior cingulate cortex, 13 of 21 Som neurons were suppressed at reward-zone entry {cite:p}`Kvitsiani2013`. Superficial and deep CA1 pyramidal cells depolarise maximally at different theta phases (195 ± 32 against 222 ± 22 degrees), which implies that the dendritic inhibition they receive arrives at systematically different phases of the cycle {cite:p}`SanchezAguilera2021`.

Circuit models recover the same division of labour:

- reducing SST inhibition in a human L2/3 microcircuit raised baseline firing by 68% (0.72 ± 0.03 to 1.21 ± 0.03 Hz) while changing the stimulus-evoked response by 3% {cite:p}`Yao2025`
- feedback onto SOM cells allows gain and stability to move together instead of in opposition {cite:p}`Bos2025`
- two-interneuron networks occupy multistable oscillatory regimes whose beta/gamma structure depends quantitatively on inhibitory coupling strength {cite:p}`DeySarkar2026`
- a parkinsonian motor-cortex microcircuit reproduces beta-band burst structure from an isolated reduction of layer 5 pyramidal-tract neuron excitability in an otherwise unmodified network {cite:p}`Doherty2025`
- learning-related retuning can be reproduced by strengthening SST-to-PV connections {cite:p}`Wilmes2019`

The convergence is real, but it is a convergence of direction and compartment and not of magnitude. Almost no two of these studies measure the same quantity, and the closest pairs still differ in preparation or region.

(sec-08-oscillatory-phenotypes)=

## Oscillatory phenotypes in disease models are band- and parameter-specific

"Gamma deficit" is the phrase this literature uses, and it conflates amplitude with frequency.

In an amyloid model, slow (30-60 Hz) gamma power was reduced (F(1,56) = 9.89, p = 0.0027, n = 6) while fast (60-120 Hz) gamma was not (F(1,56) = 0.8096, p = 0.3721) {cite:p}`Etter2019`. Normalised hippocampal gamma power fell from a z-score of 5.1 in wild-type to 1.7 in mice combining amyloid with Nptx2 deletion, with amyloid alone at 3.9 (p = 0.0199, one-way ANOVA) {cite:p}`Xiao2017`. In a human-tau propagation model, by contrast, slow- and mid-gamma peak frequencies were indistinguishable between genotypes (28.7 ± 0.7 against 29.3 ± 1.2 Hz; 56.8 ± 0.8 against 59.3 ± 4.1 Hz). The authors report these as similar distributions, with no test statistic {cite:p}`Viney2022`.

Amyloid models also slow and desynchronise more broadly. Theta-band EEG coherence is reduced across vigilance states {cite:p}`Constantino2026`, and slow-wave power falls from three months of age while slow-wave frequency stays at 0.6 Hz {cite:p}`Lee2023a`. A tau model, by contrast, is reported to decrease beta power and raise markers of cortical excitability, with no effect size reported {cite:p}`Irmen2026`. In patients, resting theta elevation is topographically distinct between Alzheimer's disease and frontotemporal dementia {cite:p}`Cai2026`.

Interneuron classes are not interchangeable controllers of a single oscillatory variable either:

- PV-interneuron-restricted GluK1 ablation shifted hippocampal theta peak frequency from 8.78 ± 0.11 to 9.46 ± 0.12 Hz (p = 0.0007) without changing it in prefrontal cortex. Theta and gamma power were elevated in both hippocampus and prefrontal cortex in the same animals, so the frequency shift and not the phenotype is what is region-selective {cite:p}`Rhee2026`
- potentiation at pyramidal and PV synapses raised peak low-gamma power 2.5- to 3-fold in a CA3 network model {cite:p}`Hadler2024`
- deleting GAD67 from SOM cells left slow-oscillation up-state duration intact while shortening it in PV-GAD67 mice (p = 2.3 x 10-3, N = 5), a single study that remains unreplicated eleven years on {cite:p}`Kuki2015`
- driving O-LM alpha2 cells generated a theta2 peak near 7 Hz (n = 6, p < 0.0001) {cite:p}`Mikulovic2018`; that result, and the risk-taking association built on it, remain unreplicated eight years on
- impaired fast inhibition in a channelopathy model slowed ripples by about 21 Hz from a wild-type 235.69 ± 6.12 Hz instead of abolishing them {cite:p}`Lascorz2026`

Optogenetic suppression of lateral-septum SST neurons, the manipulation named in that study's title and abstract, changed dorsal hippocampal theta power by 14.8% (p = 8 x 10-7) along with ripple density {cite:p}`Espinosa2022`. But its individual results sentences attribute the theta increase to stimulation of these cells, and the fall in ripple density to silencing them.

Which parameter moves identifies which element failed, and pooling them loses exactly that information. {numref}`fig-sec8-oscillatory-phenotypes-and-manipulations` therefore keeps power, peak frequency and the parvalbumin-side manipulations on separate axes.

:::{figure} ../figures/fig_sec8_oscillatory_phenotypes_and_manipulations.png
:name: fig-sec8-oscillatory-phenotypes-and-manipulations
:width: 100%
**Power, frequency, and which element was manipulated.** (A) Normalised hippocampal gamma power (z-score) by genotype {cite:p}`Xiao2017`, with the slow- versus fast-gamma genotype statistics of {cite:t}`Etter2019` printed as a statistics row. (B) Slow- and mid-gamma peak frequency in a tauopathy model, plotted on band-local axes {cite:p}`Viney2022`. (C) Hippocampal theta peak frequency in control and PV-Grik1-/- mice {cite:p}`Rhee2026`. (D) Peak low-gamma power fold change, a model-condition output {cite:p}`Hadler2024`. Caveats carried with panels A and B: all four genotype groups of {cite:t}`Xiao2017` are shown because the gamma-power reduction is carried by the hAPP/Nptx2-/- double mutant (1.7), whereas amyloid alone (hAPP, 3.9) sits near the Nptx2-/- single mutant (3.8) and below wild-type (5.1), so the value is not attributable to amyloid alone. {cite:t}`Etter2019` contribute a genotype main effect only (F and p); no point estimate exists in the source, so this entry is drawn as a statistics row with no position on the power axis, not a bar. Recording-site grain is unresolved on one side only: {cite:t}`Xiao2017` recorded extracellular field potentials from stratum pyramidale of CA3, whereas the subfield and layer of {cite:t}`Etter2019`'s hippocampal recording are not stated in the source sentence or abstract supporting this value; gamma power is layer-dependent, so the two sites may not be read as equivalent. {cite:t}`Xiao2017` state no n in the source sentence or abstract, and their preparation is ex vivo, acute hippocampal slices from 3–4-month-old mice, while {cite:t}`Etter2019` state n = 6 without specifying whether this is per genotype; {cite:t}`Etter2019`'s study also applies optogenetic stimulation and the source sentence does not state the stimulation condition under which the genotype comparison was measured. {cite:t}`Xiao2017`'s model is hAPP crossed to Nptx2-/-, with the APP line named in that study's Methods as APPswe/PS1dE9; the line behind the other amyloid entry is not named in the source sentence or abstract supporting its value, so the two amyloid models are not established to be the same line. {cite:t}`Viney2022` report "similar distributions for both genotypes" and give no test statistic for the genotype comparison, so panel B is annotated with that wording and not as "n.s."; animal numbers differ per band (slow gamma, n = 6 non-transgenic and n = 5 transgenic; mid gamma, n = 5 and n = 4); this is a tauopathy model (THY-Tau22) whereas panel A shows amyloid models, so disease mechanism and time course differ; the behavioural state behind these values is unresolved because the study reports both head-fixed and freely moving recordings and the source sentence does not say which contributed them; the recording subfield is not named in the source sentence or abstract supporting this value; and peak frequency and power are independent properties of the gamma band, so panel B shares no axis with panel A. Caveats carried with panels C and D: neither entry manipulates somatostatin neurons — both act on parvalbumin-side elements (a PV-interneuron-restricted GluK1 ablation; combined pyramidal-cell plus PV-interneuron potentiation) — so this pair is the parvalbumin comparator, not an SST manipulation series. The two values are different oscillations and units (theta peak frequency in Hz; low-gamma power as a fold change) and are plotted on separate axes. {cite:t}`Hadler2024`'s 2.5-to-3-fold value is the output of a CA3 network-model condition, not a recorded measurement, and panel D is marked as simulated. {cite:t}`Rhee2026`'s theta peak-frequency difference is hippocampus-specific (no difference in mPFC, p = 0.264), but the same study reports elevated theta and gamma oscillation power in both hippocampus and mPFC, so panel C must not be read as showing a hippocampus-confined phenotype. The manipulations differ in kind (a PV-interneuron-restricted GluK1 ablation versus acute plasticity induction in a model); the source sentence and abstract supporting this value do not establish when the ablation takes effect, and lifelong developmental compensation is an inference drawn here rather than a finding reported by the study. Neither entry reports a sample size traceable to the sentence carrying its value, and the two "n not reported" cells are not equivalent: panel D is a model condition with no biological sample size, whereas panel C is a recording whose animal numbers are simply not stated. Error terms on the Xiao, Viney and Rhee points are the source sentences' own ± values; those sentences do not state whether they are SEM or SD, so they carry no dispersion claim.
:::

:::{dropdown} 📓 Figure code
```python
import sys, os

# Resolve paths so the notebook runs from either its own directory or the repo root.
HERE = os.path.abspath(".") if os.path.exists("shared_style.py") else os.path.abspath("figures/notebooks")
sys.path.insert(0, HERE)
OUTDIR = os.path.normpath(os.path.join(HERE, ".."))

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from shared_style import COLORS, apply_style, save_figure

apply_style()

# ---

# --- Values: every number below is verbatim in that entry's source sentence ---
# Xiao et al. 2017 (10.7554/elife.23798) -> panel A
XIAO = [("WT", 5.1, 0.73), ("Nptx2-/-", 3.8, 0.63), ("hAPP", 3.9, 0.79),
        ("hAPP/\nNptx2-/-", 1.7, 0.68)]
XIAO_STAT = "p = 0.0199, one-way ANOVA; n not stated"
# Etter et al. 2019 (10.1038/s41467-019-13260-9) -> statistics row in panel A
ETTER = ("Etter 2019 (statistic only, no point estimate, no axis position):\n"
         "slow (30-60 Hz) gamma F(1,56) = 9.89, p = 0.0027;\n"
         "fast (60-120 Hz) gamma F(1,56) = 0.8096, p = 0.3721; n = 6")
# Viney et al. 2022 (10.1016/j.celrep.2022.111646) -> panel B, band-local axes
VINEY = {"slow gamma (IMF4)": [("ntg", 28.7, 0.7, 6), ("tg", 29.3, 1.2, 5)],
         "mid gamma (IMF3)":  [("ntg", 56.8, 0.8, 5), ("tg", 59.3, 4.1, 4)]}
# Rhee et al. 2026 (10.1038/s41398-026-04060-z) -> panel C
RHEE = [("control", 8.78, 0.11), ("PV-Grik1-/-", 9.46, 0.12)]
# Hadler et al. 2024 (10.1126/sciadv.adj7427) -> panel D (model output)
HADLER = (2.5, 3.0)

# ---

fig = plt.figure(figsize=(7.1, 5.8))
gs = GridSpec(2, 4, figure=fig, hspace=1.05, wspace=1.00)

# ---------------- Panel A: gamma POWER in amyloid models ----------------------
axA = fig.add_subplot(gs[0, 0:2])
xs = range(len(XIAO))
axA.errorbar(list(xs), [v for _, v, _ in XIAO], yerr=[e for _, _, e in XIAO],
             fmt="o", ms=6, color=COLORS["mixed_gabaergic"],
             ecolor=COLORS["mixed_gabaergic"], elinewidth=1.2, capsize=4,
             linestyle="none")
for x, (lab, v, e) in zip(xs, XIAO):
    axA.text(x, v + e + 0.25, f"{v}", fontsize=8, ha="center")
axA.set_xticks(list(xs)); axA.set_xticklabels([lab for lab, _, _ in XIAO], fontsize=8)
axA.set_ylim(0, 7.0); axA.set_xlim(-0.5, 3.6)
axA.set_ylabel("Normalised hippocampal\ngamma power (z-score)")
axA.set_xlabel(XIAO_STAT, fontsize=8, labelpad=6)
axA.set_title("A  Gamma power (Xiao 2017)", fontsize=10,
              fontweight="bold", loc="left")
axA.text(0.0, -0.40, ETTER, fontsize=8, va="top", ha="left",
         transform=axA.transAxes, color=COLORS["neutral_gray"])

# ---------------- Panel B: gamma PEAK FREQUENCY, tauopathy model --------------
band_axes = [fig.add_subplot(gs[0, 2]), fig.add_subplot(gs[0, 3])]
for ax, (band, pts) in zip(band_axes, VINEY.items()):
    for x, (lab, v, e, n) in enumerate(pts):
        col = COLORS["neutral_gray"] if lab == "ntg" else COLORS["increase"]
        ax.errorbar([x], [v], yerr=[e], fmt="o", ms=6, color=col, ecolor=col,
                    elinewidth=1.2, capsize=4, linestyle="none")
        ax.text(x, v + e + 0.35, f"{v}\nn = {n}", fontsize=8, ha="center")
    ax.set_xticks([0, 1]); ax.set_xticklabels([lab for lab, _, _, _ in pts], fontsize=8)
    ax.set_xlim(-0.6, 1.6)
    lo = min(v - e for _, v, e, _ in pts) - 2.0
    hi = max(v + e for _, v, e, _ in pts) + 3.2
    ax.set_ylim(lo, hi)
    ax.set_title(band, fontsize=9, loc="left")
band_axes[0].set_ylabel("Gamma peak frequency (Hz)")
band_axes[0].text(-0.20, 1.34, "B  Gamma peak frequency (Viney 2022)",
                  fontsize=10, fontweight="bold", transform=band_axes[0].transAxes)
band_axes[1].set_xlabel('"similar distributions for\nboth genotypes";\nno test statistic reported',
                        fontsize=8, labelpad=6)

# ---------------- Panel C: theta peak frequency, PV-side manipulation ---------
axC = fig.add_subplot(gs[1, 0:2])
for x, (lab, v, e) in enumerate(RHEE):
    col = COLORS["neutral_gray"] if lab == "control" else COLORS["pv"]
    axC.errorbar([x], [v], yerr=[e], fmt="s", ms=6, color=col, ecolor=col,
                 elinewidth=1.2, capsize=4, linestyle="none")
    axC.text(x, v + e + 0.08, f"{v}", fontsize=8, ha="center")
axC.set_xticks([0, 1]); axC.set_xticklabels([lab for lab, _, _ in RHEE], fontsize=9)
axC.set_xlim(-0.6, 1.6); axC.set_ylim(8.3, 9.9)
axC.set_ylabel("Hippocampal theta\npeak frequency (Hz)")
axC.set_xlabel("p = 0.0007, unpaired t test; no difference in mPFC (p = 0.264);\n"
               "n not reported", fontsize=8, labelpad=6)
axC.set_title("C  Theta frequency (Rhee 2026)", fontsize=10,
              fontweight="bold", loc="left")

# ---------------- Panel D: simulated low-gamma power fold change --------------
axD = fig.add_subplot(gs[1, 2:4])
axD.bar([0], [HADLER[1] - HADLER[0]], bottom=[HADLER[0]], width=0.45,
        color="white", edgecolor=COLORS["simulated"], hatch="///", linewidth=1.0)
axD.axhline(1.0, ls=":", lw=1.0, color=COLORS["neutral_gray"])
axD.text(0.45, 1.02, "no change", fontsize=8, ha="right", va="bottom",
         color=COLORS["neutral_gray"])
axD.text(0, HADLER[1] + 0.15, "2.5 to 3", fontsize=8, ha="center")
axD.set_xticks([0]); axD.set_xticklabels(["PYR + PVI-LTP\n(model condition)"], fontsize=8)
axD.set_xlim(-0.6, 0.6); axD.set_ylim(0, 3.8)
axD.set_ylabel("Peak low-gamma power\n(fold change)")
axD.set_xlabel("model output (simulated); no biological sample size", fontsize=8, labelpad=6)
axD.set_title("D  Simulated gamma (Hadler 2024)", fontsize=10,
              fontweight="bold", loc="left")

for ax in [axA, axC, axD] + band_axes:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

fig.text(0.5, -0.04,
         "Heterogeneous comparison - values not pooled. Power (A), peak frequency (B), theta frequency (C) and a "
         "simulated fold change (D) occupy four independent axes.\nError bars are the source sentences' own +/- terms "
         "(dispersion type not stated). Panels C and D manipulate parvalbumin-side elements, not somatostatin neurons.",
         ha="center", va="top", fontsize=8, color=COLORS["neutral_gray"])

# ---

save_figure(fig, os.path.join(OUTDIR, "fig_sec8_oscillatory_phenotypes_and_manipulations.png"))
```
:::

:::{admonition} Evidence Conflict
:class: warning
Whether the SST pathway is functionally spared in amyloid-oligomer oscillopathy is unresolved, and the disagreement is probably about which synapse was measured. Optogenetic dissection of carbachol-induced CA1 gamma in oligomer-treated slices localised the damage to reciprocal pyramidal-cell-to-PV synapses and found pyramidal-to-SST synapses intact, with desynchronised spike phases relative to gamma {cite:p}`Park2020`. Recording in vivo from the same model, a second study found both theta (3-12 Hz) and gamma (30-60 Hz) power reduced in oligomer-injected SST-Cre mice, with increased initial GABA release probability at SST as well as PV output synapses {cite:p}`Chung2020`. The first interrogates the excitatory input to the interneuron, the second its inhibitory output onto pyramidal cells, so both can hold; the disagreement is reconciled by what each study measured rather than by data, and no experiment in the retrieved record tests input and output of the same SST population side by side. The claim that SST interneuron loss causes network hypersynchrony in Alzheimer's disease, repeated across secondary sources, has no primary demonstration in this record that isolates SST cells from PV dysfunction or general inhibitory failure — and one retrieved study localises amyloid-induced gamma failure to PV rather than SST synapses {cite:p}`Park2020`.
:::

The therapeutic corollary inherits two unresolved premises.

Driving fast-spiking PV interneurons at 40 Hz reduced CA1 amyloid-beta labelling intensity by 39.5% relative to controls {cite:p}`Iaccarino2016`. Chronic 40 Hz optogenetic stimulation of cortical GABAergic interneurons in APP mice restored slow-wave activity across the 24-hour period (6 mice per group), but did not alter plaque load or microglial number {cite:p}`Zhao2023`. The two differ in targeted population, region and stimulation duration, and the disagreement stands open.

Whether sensory flicker engages native gamma circuits at all is separately contested. 40 Hz visual stimulation increased 40 Hz spectral power in wake, N2, N3 and REM {cite:p}`Hainke2024`. But phase analysis in visual cortex showed phase angles exceeding one full cycle within the duration of the first gamma cycle (17.2 ms), so even stimulation at the oscillator's own frequency does not capture its dynamics {cite:p}`Duecker2021`.

The human data qualify the corollary twice more. A single session of 40 Hz audiovisual stimulation entrained scalp EEG without improving attention-network performance (alerting t(19) = -0.992, p = 0.334) {cite:p}`Wu2025`. Older adults lacked the theta-phase-to-gamma-amplitude nesting present in younger adults (z = -0.540, p = 0.286 against z = -2.724, p = 0.003), a deficit rhythmic transcranial stimulation is reported to restore, though no effect size for the restoration itself is reported {cite:p}`Reinhart2019`.

Replication of the amyloid-lowering effect by laboratories outside the originating group has not, as far as we can establish, appeared. So the mechanism handed forward to {ref}`sec-therapeutics` rests on two premises, each contradicted by at least one of the studies above.

(sec-08-sleep)=

## Sleep: slow oscillations, spindles, and the clearance link

The human sleep phenotype is the strongest bridge in this section and the one with the weakest cellular grounding.

Three observational results carry it:

- non-rapid-eye-movement (NREM) stage-2 spindle density improved prediction of CSF total tau by delta R-squared = 0.284 above age, sex and ApoE4 genotype (p = 0.001), and was the only sleep variable to do so. The variance statistic is itself unsigned, and the direction comes from the study's own report that N2 spindle density correlated negatively with CSF total tau {cite:p}`Kam2019`
- slow-wave activity supported memory specifically in amyloid-positive older adults, classified against a PiB global DVR cutoff of 1.065 {cite:p}`Zavecz2023`
- the overnight memory benefit of slow-wave count was fully mediated by travelling-slow-wave features (total effect beta = 0.48, 95% CI 0.103 to 0.850, p = 0.011) {cite:p}`Rouast2026`

Crucially these measures are modifiable:

- phase-locked acoustic stimulation increased slow-oscillation-coupled spindles by 24% in the intervention arm against 0% in controls (t = 2.81, P = 0.01; group difference t = -2.41, P = 0.02). The trial found no group difference in memory performance or plasma amyloid, and its reported benefits rest on within-group associations between response magnitude and later memory {cite:p}`Wunderlin2023`
- slow-wave-spindle coupling strength tracked overnight plasma amyloid-beta 42/40 change on the third experimental night (beta = 2.5, p = 0.006) {cite:p}`Wunderlin2026`
- anodal slow-oscillation tDCS raised spindle power by 24.1% in intermediate-to-evening chronotypes, a subgroup of 10 of 22 participants whose mean change carries an SD of 72.1% (pairwise p = 0.077; chronotype-by-stimulation interaction p = 0.068) {cite:p}`Dikici2026`

The model side adds three interventions of its own:

- zolpidem restored slow-oscillation and delta power in an amyloid model relative to each animal's own baseline {cite:p}`Yu2026`
- optogenetic drive of cortical interneurons restored slow-wave activity in the same disease class {cite:p}`Zhao2023`
- tau confined to dorsal raphe serotonin neurons reduced NREM percent delta composition (p = 0.0328) {cite:p}`Kolling2026` — a single study, with no independent replication known to us

{numref}`fig-sec8-sleep-oscillations-tau-and-memory` shows these observational and interventional results together.

:::{figure} ../figures/fig_sec8_sleep_oscillations_tau_and_memory.png
:name: fig-sec8-sleep-oscillations-tau-and-memory
:width: 100%
**Sleep oscillations, biomarkers, and interventions, never pooled.** (A) Two spindle studies side by side as a table: an observational association of N2 spindle density with CSF total tau (delta R-squared = 0.284, p = 0.001) {cite:p}`Kam2019` and a sham-controlled stimulation trial changing slow-oscillation-coupled spindle count (+24% against 0%, t = 2.81, P = 0.01) {cite:p}`Wunderlin2023`. (B) Direction-of-effect glyphs for two mouse studies {cite:p}`Yu2026, Kolling2026`. (C) Two human statistics, each in its own column {cite:p}`Wunderlin2026, Dikici2026`. Caveats carried with panel A: the two values are not the same kind of quantity — delta R-squared = 0.284 is incremental variance explained in CSF total tau and +24% is a relative change in slow-oscillation-coupled spindle count under acoustic stimulation; they are not comparable percentages and are never drawn as bars. The direction of inference differs, one entry treating spindle density as a predictor of an Alzheimer biomarker and the other treating acoustic stimulation as a predictor of spindle coupling, and delta R-squared is an unsigned variance statistic whose underlying association in {cite:t}`Kam2019` is negative, the opposite sign to the +24% increase in the other row. {cite:t}`Kam2019` is a cross-sectional association in cognitively normal older adults with CSF biomarkers; {cite:t}`Wunderlin2023` is a between-subject sham-controlled three-night trial (32 participants) that reported no group difference in plasma amyloid or memory, while reporting within the intervention group that the magnitude of the stimulation-induced response was associated with memory up to three months later and with beneficial plasma amyloid change. Outcome matrices differ (CSF total tau versus plasma amyloid) and no shared outcome links the two rows. Neither source reports the analysed sample size in the sentence carrying its value; only the trial total of 32 is available, from the abstract, and that figure belongs to the Wunderlin row alone, so the Kam row reads "not stated". {cite:t}`Wunderlin2023` and {cite:t}`Wunderlin2026` plausibly share participants and must not be read as independent replications. Caveats carried with panel B: both entries contribute a direction of effect only — no effect size is available from the cited sources — and are drawn as up/down glyphs with their p-values, never as bars with implied magnitude; mouse cortical EEG is not comparable in absolute terms with the human scalp-EEG entries of panel C; the two manipulations differ in kind (a systemic hypnotic drug in an amyloid model versus viral tau expression targeted to dorsal raphe serotonin neurons, recorded with longitudinal EEG); {cite:t}`Kolling2026` report the sleep effects as primarily sex-divergent, so the single glyph shown here is not a sex-resolved result and a pooled glyph averages over a declared sex interaction; the dependent variables differ (absolute slow-oscillation and delta power versus percent delta composition of nREM, a proportion rather than a power); group sizes are not stated in either source sentence; and the comparators differ, {cite:t}`Yu2026`'s direction being relative to the animals' own pre-injection baseline and {cite:t}`Kolling2026`'s relative to a control-virus group. Caveats carried with panel C: the two values are different statistics and each occupies its own labelled column — a regression interaction coefficient (beta = 2.5) whose units and scaling the source does not state, printed as a statistic with no axis position, and a percentage change in spindle power (+24.1%) on its own axis; no shared axis and no pooling. {cite:t}`Dikici2026`'s +24.1% is a subgroup mean (intermediate-to-evening chronotypes, n = 10 of 22) whose mean change is 24.1% with an SD of 72.1% as stated in the source sentence, and whose comparisons are printed on the face of the figure as the source's own statistics (pairwise p = 0.077; interaction p = 0.068) rather than as a significance mark. {cite:t}`Wunderlin2026`'s coupling-amyloid interaction is specific to the third experimental night and, per the source, benefited amyloid response exclusively in cognitively impaired individuals, so it is marked subgroup-restricted on the face of the figure; the interventions differ in modality (three-night phase-locked acoustic stimulation versus slow-oscillatory transcranial direct-current stimulation during naps); neither source sentence states the analysed sample size for its plotted statistic beyond {cite:t}`Dikici2026`'s chronotype subgroup (n = 10); and {cite:t}`Wunderlin2026` pooled and re-analysed data from three clinical trials, so the two Wunderlin entries must not be presented as independent replications.
:::

:::{dropdown} 📓 Figure code
```python
import sys, os

# Resolve paths so the notebook runs from either its own directory or the repo root.
HERE = os.path.abspath(".") if os.path.exists("shared_style.py") else os.path.abspath("figures/notebooks")
sys.path.insert(0, HERE)
OUTDIR = os.path.normpath(os.path.join(HERE, ".."))

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from shared_style import COLORS, apply_style, save_figure

apply_style()

# ---

# --- Values: every number below is verbatim in that entry's source sentence,
# --- except the two trial totals (32; 22), which come from the named abstracts.
# Panel A: table rows (Kam et al. 2019; Wunderlin et al. 2023)
TABLE_COLS = ["Design", "Spindle\nmeasure", "Outcome", "Statistic (type named)", "n"]
TABLE_ROWS = [
    ["Kam 2019\nobservational,\ncross-sectional",
     "N2 spindle\ndensity",
     "lower spindle density\nwith higher CSF tau\n(negative association)",
     "incremental variance\nexplained in CSF total tau:\ndelta R2 = 0.284 (p = 0.001)",
     "not\nstated"],
    ["Wunderlin 2023\nbetween-subject\nsham-controlled\n3-night trial",
     "SO-coupled\nspindle\ncount",
     "+24% (intervention)\nvs 0% (control)",
     "paired t statistic: t = 2.81,\nP = 0.01; group difference\nt = -2.41, P = 0.02",
     "32 total\n(abstract)"],
]
# Panel B: direction glyphs (Yu et al. 2026; Kolling et al. 2026)
GLYPHS = [
    dict(label="Yu 2026 (APP amyloid model)\nslow-oscillation (0.5-1 Hz) and\ndelta (1-4 Hz) power vs own baseline",
         direction="up", stat="significant increase; no effect size reported",
         method="chronic EEG"),
    dict(label="Kolling 2026 (tau in dorsal raphe\n5-HT neurons) nREM percent delta\ncomposition vs a control-virus group",
         direction="down", stat="virus effect p = 0.0328 (3-way ANOVA);\np = 0.0189 (2-way ANOVA)",
         method="longitudinal EEG"),
]
# Panel C: human statistics, one column each (Wunderlin et al. 2026; Dikici et al. 2026)
WUND26 = "beta = 2.5, p = 0.006\n(regression interaction,\nthird experimental night)"
DIKICI = dict(value=24.1, sd=72.1, n=10,
              stat="pairwise p = 0.077;\ninteraction p = 0.068")

# ---

fig = plt.figure(figsize=(7.1, 7.4))
gs = GridSpec(3, 2, figure=fig, height_ratios=[1.25, 0.85, 1.05], hspace=0.75, wspace=0.45)

# ---------------- Panel A: table-form figure ---------------------------------
axA = fig.add_subplot(gs[0, :]); axA.axis("off")
axA.set_title("A  Sleep spindles and Alzheimer biomarkers: one association, one trial",
              fontsize=10, fontweight="bold", loc="left", pad=10)
xpos = [0.00, 0.175, 0.305, 0.575, 0.925]
ytop = 0.88
for x, col in zip(xpos, TABLE_COLS):
    axA.text(x, ytop, col, fontsize=8.5, fontweight="bold", va="top", ha="left",
             transform=axA.transAxes)
axA.plot([0, 1], [ytop - 0.09] * 2, lw=0.8, color=COLORS["neutral_gray"],
         transform=axA.transAxes, clip_on=False)
for r, row in enumerate(TABLE_ROWS):
    y = ytop - 0.17 - r * 0.42
    for x, cell in zip(xpos, row):
        axA.text(x, y, cell, fontsize=8, va="top", ha="left", transform=axA.transAxes)
    if r == 0:
        axA.plot([0, 1], [y - 0.30] * 2, lw=0.5, color=COLORS["light_gray"],
                 transform=axA.transAxes, clip_on=False)
axA.text(0, -0.30, "Not comparable percentages: an unsigned variance statistic and a relative change; "
                   "never drawn as bars.", fontsize=8, va="top", ha="left",
         transform=axA.transAxes, color=COLORS["neutral_gray"])

# ---------------- Panel B: direction glyphs, mouse ---------------------------
axB = fig.add_subplot(gs[1, :]); axB.axis("off")
axB.set_title("B  Mouse NREM oscillation changes: direction of effect only",
              fontsize=10, fontweight="bold", loc="left", pad=10)
for i, g in enumerate(GLYPHS):
    y = 0.72 - i * 0.55
    col = COLORS["increase"] if g["direction"] == "up" else COLORS["decrease"]
    arrow = (0.055, y - 0.16, 0, 0.26) if g["direction"] == "up" else (0.055, y + 0.10, 0, -0.26)
    axB.arrow(arrow[0], arrow[1], arrow[2], arrow[3], width=0.012, head_width=0.045,
              head_length=0.09, color=col, transform=axB.transAxes,
              length_includes_head=True, clip_on=False)
    axB.text(0.12, y + 0.08, g["label"], fontsize=8, va="top", ha="left",
             transform=axB.transAxes)
    axB.text(0.58, y + 0.08, g["stat"] + "\n" + g["method"] + "; group sizes not stated",
             fontsize=8, va="top", ha="left", transform=axB.transAxes,
             color=COLORS["neutral_gray"])
axB.text(0, -0.28, "No magnitude axis: no effect size is available from either source. "
                   "Kolling et al. report the sleep effects as primarily sex-divergent.",
         fontsize=8, va="top", ha="left", transform=axB.transAxes,
         color=COLORS["neutral_gray"])

# ---------------- Panel C: human statistics, non-pooled -----------------------
axC1 = fig.add_subplot(gs[2, 0]); axC1.axis("off")
axC1.set_title("C  Wunderlin 2026 (statistic, no axis)", fontsize=9.5,
               fontweight="bold", loc="left", pad=8)
axC1.text(0.5, 0.60, WUND26, fontsize=9, ha="center", va="center",
          transform=axC1.transAxes)
axC1.text(0.5, 0.18, "subgroup-restricted: per the source, the\ncoupling-amyloid benefit applies to\n"
                     "cognitively impaired individuals.\nUnits and scaling of beta not stated.",
          fontsize=8, ha="center", va="center", transform=axC1.transAxes,
          color=COLORS["neutral_gray"])

axC2 = fig.add_subplot(gs[2, 1])
axC2.errorbar([0], [DIKICI["value"]], yerr=[DIKICI["sd"]], fmt="o", ms=7,
              color=COLORS["mixed_gabaergic"], ecolor=COLORS["mixed_gabaergic"],
              elinewidth=1.2, capsize=4, linestyle="none")
axC2.axhline(0, ls=":", lw=1.0, color=COLORS["neutral_gray"])
axC2.text(0.12, DIKICI["value"], "+24.1%\n(SD 72.1%)", fontsize=8, ha="left", va="center")
axC2.set_xticks([0])
axC2.set_xticklabels([f"anodal so-tDCS\nvs sham\n(n = {DIKICI['n']} of 22 [abstract],\nintermediate-to-evening\nchronotypes)"],
                     fontsize=8)
axC2.set_xlim(-0.5, 1.1); axC2.set_ylim(-60, 110)
axC2.set_ylabel("NREM spindle power\nchange (%)")
axC2.set_xlabel(DIKICI["stat"], fontsize=8, labelpad=6)
axC2.set_title("Dikici 2026", fontsize=9.5, fontweight="bold", loc="left", pad=8)
axC2.spines["top"].set_visible(False); axC2.spines["right"].set_visible(False)

fig.text(0.5, -0.085,
         "Heterogeneous comparison - values not pooled. Mouse cortical EEG (B) and human scalp EEG (A, C) are not "
         "comparable in absolute terms, and the\nhuman statistics in panel C share no axis. The two Wunderlin entries "
         "plausibly share participants and are not independent replications.",
         ha="center", va="top", fontsize=8, color=COLORS["neutral_gray"])

# ---

save_figure(fig, os.path.join(OUTDIR, "fig_sec8_sleep_oscillations_tau_and_memory.png"))
```
:::

The bridge lacks its middle term. No recording or manipulation of identified cortical SST interneurons during spindle events appears in the published record, and the work linking somatostatin interneurons to sleep addresses slow oscillations, sleep onset and sleep deprivation instead. So the human spindle biomarker currently has no cellular interpretation.

Nor is there an SST-selective sleep rescue. Interventional studies in disease models drive GABAergic interneurons broadly, with opsins or with zolpidem {cite:p}`Zhao2023, Yu2026`, and no study restoring slow-wave activity by SST-selective manipulation in a tau or amyloid model is known to us.

The indirect evidence that SST cells belong here is nonetheless substantial:

- brief activation of cortical Sst neurons in the ON state is described as inducing a long OFF state that silences broad cortical populations, with inhibition of those neurons reducing slow-wave activity. The claim is carried by a secondary source and not by its primary demonstration {cite:p}`Kobayashi2026`
- activity-tagged prefrontal Sst neurons were sufficient to initiate nesting and subsequent NREM sleep when reactivated (light against no light, P = 0.0046 at 5 Hz, P = 0.0498 at 10 Hz and P = 0.0202 at 20 Hz), a single study awaiting replication. The P = 0.0297 and P = 0.0043 values that study reports belong to light-evoked action-potential probability in slice recordings {cite:p}`Tossell2023`
- that same superficial-layer long-range Sst population is selectively active in slow-wave sleep {cite:p}`Ratliff2026`
- five hours of sleep deprivation raised hippocampal Sst and Npy transcripts two- to fourfold, against roughly 30% for Gad67 and Pvalb {cite:p}`Delorme2021`
- amyloid oligomers abolished the learning-induced increase in sharp-wave-ripple occurrence during post-encoding slow-wave sleep (t12 = 2.43, p = 0.032, n = 7) {cite:p}`Nicole2016`

{ref}`sec-human-evidence` assembles the human counterpart of these associations.

(sec-08-memory)=

## Memory: dendritic gating of plasticity and its disease relevance

If SST inhibition acts on dendrites and not on spike threshold, its behavioural signature should be control over what is learned instead of how much is fired. The plasticity data show that control.

O-LM interneurons control the dendritic calcium signalling and synaptic plasticity initiated by entorhinal input to CA1 pyramidal neurons, an effect reported qualitatively, with no effect size given {cite:p}`Udakis2025`. Their own activity was lower on the initial laps of a novel environment than on later laps of a familiar one (0.011 ± 0.005 against 0.093 ± 0.063 ΔF/F0) — the fall in dendritic inhibition that permits the plasticity new place fields require. The same inhibition terminates plateau potentials with a steep dependence on timing within the plateau (20 ± 6.7% termination at 10 ms against 62.7 ± 7.7% at 50 ms; n = 17, Friedman chi-square = 42.8, p < 10-8) {cite:p}`Vaasjo2026`.

The receptor-level mechanism offered for this gating is alpha5-subunit GABA-A-mediated control of synaptic NMDA-receptor activation. An alpha5-selective negative allosteric modulator reduced slow dendritic IPSCs by 29.4 ± 7.1%, from 138.8 ± 23.3 to 95.9 ± 14.6 pA (n = 6, P < 0.01) {cite:p}`Schulz2018` — a single study, unreplicated eight years on.

Three further results place the effect in the distal compartment:

- dendrite-targeting layer 1 interneurons strongly reduced apical dendritic calcium responses across 130 recorded dendrites, and themselves underwent learning-related potentiation {cite:p}`Abs2018`
- motor learning drove spine formation specifically in distal apical branches in layer 1 {cite:p}`Chen2015`
- systemic ketamine (10 mg/kg) reduced SST somatic calcium event rates by 13 ± 3% against a 13 ± 6% increase with saline, while dendritic spine event rates rose 43.42 ± 0.01% against 4.34 ± 0.01% {cite:p}`Ali2020`. These are co-observed changes under a drug with many other actions, and another single-laboratory demonstration

Behavioural manipulation of these cells has three reported outcomes:

- SST activation during the early delay of a working-memory task impaired performance strongly, as did PV activation, while VIP activation improved it {cite:p}`Kamigaki2017`
- prefrontal SST activation alone raised freezing above baseline in the absence of the conditioned stimulus, mimicking a conditioned response {cite:p}`Cummings2019`
- chemogenetic activation of dentate SST cells impaired object-location encoding (p = 0.0047) and retrieval (p = 0.046), but not consolidation (p = 0.8804) {cite:p}`Raven2026`

In an amyloid model, remote memory decline was accompanied by increased inhibitory input onto prefrontal engram cells without altered PV reactivation {cite:p}`VanAdrichem2025`. Driving O-LM alpha2 cells generated type 2 theta, which that same unreplicated study associates with increased risk-taking in response to predator odour {cite:p}`Mikulovic2018`.

Two gaps bound this account. The in vivo demonstrations are slice and head-fixed preparations, and not freely behaving animals. And no human tissue or in vivo human evidence for dendrite-targeted inhibitory gating of plasticity has been reported, as far as we can establish, so every statement here about human dendritic inhibition crosses species without a bridging measurement.

(sec-08-reconciliation)=

## Reconciling the cellular contradictions at circuit level

The cellular disagreements need not be settled for the circuit prediction to hold. This is both the strength and the limit of the account.

Whether SST cells in amyloid cortex are hyper- or hypoactive is open. Immediate-early-gene labelling found c-Fos elevated at both PV and SST neurons in App knock-in cortex relative to wild-type (two-way ANOVA, p < 0.001), with the increase reported as relatively greater at PV cells {cite:p}`MelgosaEcenarro2026`. Awake silicon-probe recording in young APP/PS1 mice, by contrast, found fast-spiking interneurons shifted towards low firing rates with pyramidal cells unchanged {cite:p}`Meftah2026`. Model construct, age and readout all differ. No study measures SST and PV firing with the same awake electrophysiological readout in both knock-in and transgenic models at matched ages, as far as we can establish.

Activity is in any case spatially graded and not uniform, SOM interneurons within 60 micrometres of plaques being more active than distant ones (Kruskal-Wallis H(2) = 18.41, p < 0.0001) {cite:p}`Algamal2022a`.

Whether the population is numerically reduced is equally open. Somatostatin-immunoreactive density in rat auditory cortex fell to 0.9 ± 0.3 cells per high-power field into old age, with a further ~20% rise in NPY immunostaining {cite:p}`Ouellet2014`. Unbiased stereology in young TgF344-AD rats, by contrast, could not observe any change in the numbers of PV+, calretinin+ or SST+ neurons {cite:p}`Futacsi2025`. The counting-method axis of the same disagreement is examined for the striatum in {ref}`sec-huntingtons` and for the cortex in {ref}`sec-alzheimers`. So driver, age, region and counting method are all confounded with the outcome, and head-to-head stereology across amyloid, tau and synucleinopathy models at matched ages does not appear to exist.

Each of these cellular states predicts the same circuit failure. Developmental ablation reducing CA1 SOM+ neurons by 46.41% {cite:p}`Subramanian2024` and inflammatory downregulation of Sst, Cort and Npy transcripts that BDNF infusion prevents {cite:p}`Rezaei2025` both reduce effective dendrite-targeted inhibition. Both therefore predict degraded low-gamma synchronisation and degraded NREM coordination, without requiring a single SST neuron to die.

Two neighbouring perturbations make that prediction less tidy instead of confirming it. Deleting the GABA-A gamma2 subunit from SST cells disinhibits those cells and increases their intrinsic excitability and spike output {cite:p}`Fuchs2016`, which moves dendrite-targeted inhibition in the opposite direction. What this family of manipulations predicts in common is therefore dysregulated, and not uniformly weakened, dendritic inhibition. The region-restricted interneuron loss recorded in Lewy body cingulate cortex but not inferior temporal gyrus is a parvalbumin-density measurement {cite:p}`Hawksworth2026`, taken from a perisomatic and not a dendrite-targeting population. It therefore speaks to where inhibition fails regionally, and not to whether the dendritic compartment is the one affected.

This is why a disease can present a severe somatostatin phenotype with the cells still present, and why the account is hard to falsify. What would distinguish these states is not a cell count but a compartment-resolved measurement: dendritic inhibitory conductance or plateau-potential termination probability, measured in the same preparation as low-gamma power and NREM slow-oscillation-spindle coupling, with SST cells identified independently of somatostatin expression.

Such an experiment must also resolve which SST cells it addresses:

- O-LM cells are a highly homogeneous transcriptomic population across Sst-Cre and Htr3a-Cre lines, the one Cre-line-dependent expression difference being attributed by that study to the BAC copy of Htr3b in the Htr3a-Cre line and not to a molecular split {cite:p}`Winterer2019`
- their overlap with the somatostatin population differs between subiculum and CA1 (59 ± 2% against 47 ± 3%; t(4010) = 7.2, p < 0.01) {cite:p}`Nichol2018`
- their septal input is graded along the dorsoventral axis (posterior probability 0.97) {cite:p}`Thulin2025`
- they integrate into cortical circuits late, only ~20% being visually responsive at P15 {cite:p}`Wang2025b`

Two further results warn that restoring cells is not the same as restoring the compartment. Transplanted medial ganglionic eminence progenitors mature into PV+ and SST+ cells in near-equal proportions (30.9 ± 8.9% against 27.2 ± 6.9%, p = 0.51) {cite:p}`Yokomizo2025a`. And dendritic SOM synapses can retain normal release properties while other inhibitory parameters shift (paired-pulse ratio 0.75 ± 0.02 against 0.75 ± 0.03, p = 0.18) {cite:p}`Gutmann2026`.

The decisive absence, carried into {ref}`sec-conflicts-limitations`, is an SST-selective gain- or loss-of-function experiment inside an amyloid or tau model with simultaneous gamma, theta and slow-oscillation measurement. No such study has been reported, as far as we can establish. The existing causal manipulations of disease oscillopathy target PV or broad GABAergic populations, and the SST contribution is inferred from circuit function in healthy animals plus marker loss in diseased tissue.

The evidence base is also uneven in depth. The circuit reports behind this section were examined in full, which is not true of the postmortem and fluid literatures they interpret, and the asymmetry should not be mistaken for equal evidential weight. The short-interval intracortical inhibition measures reinterpreted in {ref}`sec-als-ftd` are the closest human readout of a specific interneuron circuit currently available.

{ref}`sec-human-evidence` assembles the postmortem, single-nucleus and fluid evidence that can test these predictions, and places the strongest and the weakest claims of this review side by side.

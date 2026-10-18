"""Figure: inhibition received by striatal projection neurons in two HD models.

Two single-study genotype contrasts, each on its own axis. The readouts (percent
change in sIPSC frequency under interneuron silencing; mean sIPSC current in pA)
are not interconvertible and are never pooled or numerically compared. Values and
"+/-" terms are verbatim from each study's source sentence; neither source states
whether the dispersion is SD or SEM, so bars are dashed and labelled as such.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import matplotlib.pyplot as plt
from shared_style import COLORS, apply_style, save_figure

apply_style()
HERE = os.path.dirname(os.path.abspath(__file__))

# S06-C03R panel A: Holley 2019, Q175 knock-in, optogenetic eNpHR silencing of
# SOM-expressing interneurons; percent change in SPN sIPSC frequency.
PANEL_A = [("WT", 1.94, 2.7, "1.94 $\\pm$ 2.7%"), ("Q175", -15.14, 5.0, "-15.14 $\\pm$ 5.0%")]
# S06-C03R panel B: Spampanato 2008, BACHD; mean spontaneous IPSC current in
# striatal medium spiny neurons (Table 1 value in a cortex-focused paper).
PANEL_B = [("WT", 4.04, 1.27, "4.04 $\\pm$ 1.27 pA"), ("BACHD", 2.94, 1.07, "2.94 $\\pm$ 1.07 pA")]

fig, (axa, axb) = plt.subplots(1, 2, figsize=(7.2, 4.3))
fig.subplots_adjust(top=0.70, wspace=0.55, left=0.12, right=0.97, bottom=0.12)

for xi, (lab, v, e, disp) in enumerate(PANEL_A):
    axa.bar(xi, v, width=0.5, color=COLORS["sst"], edgecolor="black", linewidth=0.6)
    axa.plot([xi, xi], [v - e, v + e], color="black", lw=0.9, ls="--")
    for ye in (v - e, v + e):
        axa.plot([xi - 0.09, xi + 0.09], [ye, ye], color="black", lw=0.9)
    axa.text(xi, v + e + 1.6 if v > 0 else v - e - 1.6, disp, ha="center",
             va="bottom" if v > 0 else "top", fontsize=8)
axa.axhline(0, color="black", lw=0.8)
axa.set_xticks(range(len(PANEL_A)))
axa.set_xticklabels([b[0] for b in PANEL_A], fontsize=9)
axa.set_ylim(-26, 12)
axa.set_ylabel("% change in SPN sIPSC frequency during\noptogenetic silencing of SOM+ interneurons",
               fontsize=8.5)
axa.set_title("A   Holley 2019 — Q175 knock-in\nt(30) = 3.24, p = 0.003; all-cell analysis\n"
              "cell count behind the contrast not stated",
              fontsize=8.5, loc="left", pad=6)

for xi, (lab, v, e, disp) in enumerate(PANEL_B):
    axb.bar(xi, v, width=0.5, color=COLORS["mixed_gabaergic"], edgecolor="black", linewidth=0.6)
    axb.plot([xi, xi], [v - e, v + e], color="black", lw=0.9, ls="--")
    for ye in (v - e, v + e):
        axb.plot([xi - 0.09, xi + 0.09], [ye, ye], color="black", lw=0.9)
    axb.text(xi, v + e + 0.2, disp, ha="center", va="bottom", fontsize=8)
axb.set_xticks(range(len(PANEL_B)))
axb.set_xticklabels([b[0] for b in PANEL_B], fontsize=9)
axb.set_ylim(0, 6.6)
axb.set_ylabel("mean spontaneous IPSC current\nin striatal MSNs (pA)", fontsize=8.5)
axb.set_title("B   Spampanato 2008 — BACHD\nnot significant; striatal table value in a\n"
              "cortex-focused paper, recordings at 3 and 6 months",
              fontsize=8.5, loc="left", pad=6)
axb.text(0.5, 0.06, "not significant", transform=axb.transAxes, ha="center", fontsize=8.5,
         style="italic", color="#444444")

fig.text(0.12, 0.955, "Readouts are not interconvertible — separate axes, no pooling and no "
                      "numerical comparison between panels",
         fontsize=8.5, color=COLORS["conflict_marker"], ha="left")
fig.text(0.12, 0.925, "Error bars reproduce printed \"+/-\" values; dispersion type not stated in "
                      "either source (drawn dashed). Neither panel has a stated denominator.",
         fontsize=7.5, color="#444444", ha="left")
fig.text(0.12, 0.895, "Not shown: excitation-inhibition ratio values and compartment-resolved PV "
                      "terminal puncta counts — neither quantity was retrieved from a primary report "
                      "by these searches.",
         fontsize=7.5, color="#444444", ha="left")

save_figure(fig, os.path.join(HERE, "..", "fig_sec6_inhibition_onto_projection_neurons_hd.png"))

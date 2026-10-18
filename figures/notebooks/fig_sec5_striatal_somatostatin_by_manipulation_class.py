# Figure: striatal somatostatin by class of manipulation.
# Panel A: the two reported nulls after nigral lesion, rendered categorically
# (neither source states a number, so nothing is drawn at zero).
# Panel B: the manipulations that do move the peptide, as signed bars, with the
# two manipulation classes drawn as separated groups.
# Panel C: the one dopamine-agonist arm reporting no somatostatin magnitude.
import textwrap
import os
import sys

# Resolve the directory that holds shared_style.py so the notebook runs from the
# repository root or from figures/notebooks.
BASE = next(p for p in (".", "figures/notebooks", os.path.join(os.getcwd(), "figures", "notebooks"))
            if os.path.exists(os.path.join(p, "shared_style.py")))
sys.path.insert(0, BASE)
FIGDIR = os.path.normpath(os.path.join(BASE, ".."))
import matplotlib.pyplot as plt
from shared_style import COLORS, apply_style, save_figure

apply_style()

PANEL_A = [
    dict(entry_id="S05-C04a-E1", study="Salin 1990", outcome="unchanged",
         row="rat rostral striatum, unilateral 6-OHDA nigrostriatal lesion, 2-3 week survival",
         note="radioimmunoassay of striatal somatostatin concentration; the only row that is a\n"
              "dopamine-depletion manipulation on its own. No group size or dispersion reported.",
         source="In animals with similar 6-OHDA-induced lesions, no change in the striatal "
                "concentration of somatostatin measured by radioimmunoassay was observed.",
         condition_source="Such a distribution and number were not altered either by unilateral "
                          "6-hydroxydopamine (6-OHDA)-induced lesion of the nigrostriatal "
                          "dopaminergic neurons after 2- to 3-week survival periods, or by "
                          "alpha-methylparatyrosine-induced dopamine depletion."),
    dict(entry_id="S05-C04a-E2", study="Flint Beal 1983", outcome="unchanged",
         row="rat striatum, nigral 6-hydroxydopamine or ibotenic acid, together with\n"
             "pallidal hemisection, reported jointly in one sentence",
         note="radioimmunoassay of somatostatin-like immunoreactivity; only the 6-hydroxydopamine\n"
              "arm is a selective dopamine depletion and the arms are not separated in the source.",
         source="Lesions of the substantia nigra produced with either 6-hydroxydopamine or "
                "ibotenic acid and hemisections at the level of the globus pallidus (6.2 mm "
                "anterior) had no effect on striatal levels of somatostatin-like "
                "immunoreactivity (SLI)."),
]

PANEL_B = [
    dict(entry_id="S05-C04b-E1", study="Engber 1992", group="dopamine-receptor pharmacology",
         label="intermittent D1\nSKF 38393\n12.5 mg/kg/day",
         value=-61, display="down 61%", comparator="vs lesioned, vehicle-treated controls",
         source="In comparison to values from lesioned, vehicle-treated controls, intermittent "
                "administration of SKF 38393 reduced somatostatin and neuropeptide Y (down 61% "
                "and 57%, respectively)..."),
    dict(entry_id="S05-C04b-E2", study="Engber 1992", group="dopamine-receptor pharmacology",
         label="continuous D2\nquinpirole\n1 mg/kg/day",
         value=43, display="up 43%", comparator="vs lesioned, vehicle-treated controls",
         source="Continuous quinpirole elevated somatostatin and neuropeptide Y levels "
                "(up 43% and 33%, respectively)..."),
    dict(entry_id="S05-C04b-E3", study="Engber 1992", group="dopamine-receptor pharmacology",
         label="intermittent D2\nquinpirole\n1 mg/kg/day",
         value=-35, display="down 35%", comparator="vs lesioned, vehicle-treated controls",
         source="Conversely, intermittent quinpirole decreased somatostatin (down 35%) and "
                "neuropeptide Y (down 27%)..."),
    dict(entry_id="S05-C04b-E5", study="Flint Beal 1983", group="intrastriatal excitotoxic lesion",
         label="kainic acid\nipsilateral side",
         value=-60, display="60% depletion", comparator="comparator NOT STATED in the source",
         source="Kainic acid injected directly into the striatum at 2 dose levels resulted in a "
                "60% depletion of SLI on the ipsilateral side and a 25% reduction on the "
                "contralateral side."),
    dict(entry_id="S05-C04b-E6", study="Flint Beal 1983", group="intrastriatal excitotoxic lesion",
         label="kainic acid\ncontralateral side",
         value=-25, display="25% reduction", comparator="comparator NOT STATED in the source",
         source="Kainic acid injected directly into the striatum at 2 dose levels resulted in a "
                "60% depletion of SLI on the ipsilateral side and a 25% reduction on the "
                "contralateral side."),
]

DOSING_SOURCE = ("Rats with a unilateral 6-hydroxydopamine (6-OHDA) lesion of the nigrostriatal "
                 "pathway were treated for 7 days with either the D1 agonist SKF 38393 "
                 "(12.5 mg/kg/day) or the D2 agonist quinpirole (1 mg/kg/day).")

PANEL_C = [
    dict(entry_id="S05-C04b-E4", study="Engber 1992", outcome="unchanged",
         row="continuous D1 agonist SKF 38393, vs lesioned, vehicle-treated controls",
         note="the source states only that continuous SKF 38393 'did not alter levels of the other\n"
              "peptides' after naming the neuropeptide Y change, so no magnitude exists for somatostatin",
         source="...continuous SKF 38393 decreased neuropeptide Y by 39% but did not alter "
                "levels of the other peptides."),
]

fig, (axA, axB, axC) = plt.subplots(3, 1, figsize=(7.09, 8.4),
                                    gridspec_kw=dict(height_ratios=[1.05, 1.5, 0.5], hspace=0.85))


def categorical_panel(ax, rows, title):
    for i, e in enumerate(rows[::-1]):
        y = i
        ax.scatter([0.03], [y], s=180, marker="s", color=COLORS["no_change"],
                   edgecolors="black", linewidths=0.8, zorder=3, clip_on=False)
        ax.annotate(e["outcome"], (0.075, y), va="center", ha="left", fontsize=8.5,
                    fontweight="bold", color=COLORS["no_change"])
        ax.annotate(e["row"], (0.22, y), va="center", ha="left", fontsize=7.6)
        nlines = e["row"].count("\n") + 1
        ax.annotate(e["note"], (0.22, y), textcoords="offset points",
                    xytext=(0, -(5.0 * nlines + 8.0)), va="top", ha="left", fontsize=7.0,
                    color=COLORS["excitatory"])
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([e["study"] for e in rows[::-1]], fontsize=9)
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.95, len(rows) - 0.05)
    ax.set_xticks([])
    ax.spines["bottom"].set_visible(False)
    ax.set_title(title, fontsize=8.5, loc="left")


categorical_panel(axA, PANEL_A,
                  "A   Nigral lesion: two reported null results, rendered categorically.\n"
                  "     Neither source reports a numerical value, so nothing is plotted at zero "
                  "percent change")

# ---- Panel B: signed bars, two separated manipulation groups ---------------
positions, labels, colors, groups = [], [], [], []
x = 0
prev_group = None
for e in PANEL_B:
    if prev_group is not None and e["group"] != prev_group:
        x += 1.0                      # visible gap between manipulation classes
    positions.append(x)
    labels.append(e["label"])
    colors.append(COLORS["increase"] if e["value"] > 0 else COLORS["decrease"])
    groups.append(e["group"])
    prev_group = e["group"]
    x += 1

for pos, e, col in zip(positions, PANEL_B, colors):
    axB.bar(pos, e["value"], width=0.6, color=col, edgecolor="black", linewidth=0.8)
    off, va = (6, "bottom") if e["value"] > 0 else (-6, "top")
    axB.annotate(e["display"], (pos, e["value"]), textcoords="offset points", xytext=(0, off),
                 ha="center", va=va, fontsize=8.5, fontweight="bold", color=col)
axB.axhline(0, color="black", lw=0.8)
axB.axvline(2.5, color=COLORS["excitatory"], lw=1.0, ls=":")
axB.set_xticks(positions)
axB.set_xticklabels(labels, fontsize=7.2)
axB.set_ylim(-88, 98)
axB.set_xlim(-0.7, max(positions) + 0.7)
axB.set_ylabel("change in striatal somatostatin content,\nas reported (%)", fontsize=9)
axB.annotate("dopamine-receptor pharmacology on a\n6-hydroxydopamine-lesioned background;\n"
             "vs lesioned, vehicle-treated controls", (0.9, 95), ha="center", va="top",
             fontsize=7.4, color=COLORS["excitatory"])
axB.annotate("intrastriatal excitotoxic lesion;\ncomparator NOT STATED in the source",
             (3.5, 95), ha="center", va="top", fontsize=7.4, color=COLORS["excitatory"])
axB.set_title("B   Manipulations that do move striatal somatostatin. The two manipulation classes "
              "are\n     separated by the dotted rule and must not be read along one continuum; "
              "none of these\n     bars is an effect of dopamine depletion. No error bars: no "
              "entry reports n or dispersion",
              fontsize=8.5, loc="left")

categorical_panel(axC, PANEL_C,
                  "C   The one dopamine-agonist arm for which no somatostatin magnitude is "
                  "reported")

fig.text(0.5, 0.025, "heterogeneous comparison - values not pooled; all rows are rat striatal "
                     "peptide by radioimmunoassay, but Engber 1992 reports \"somatostatin\" "
                     "content\nwhile Flint Beal 1983 reports somatostatin-like immunoreactivity, "
                     "and neither is an interneuron-specific measure.",
         ha="center", fontsize=8, style="italic", color=COLORS["excitatory"])
fig.text(0.5, -0.02, "All values in this figure were extracted from the source abstracts; full "
                     "text was not accessible for either study.",
         ha="center", fontsize=7.5, color=COLORS["excitatory"])

save_figure(fig, os.path.join(FIGDIR, "fig_sec5_striatal_somatostatin_by_manipulation_class.png"))

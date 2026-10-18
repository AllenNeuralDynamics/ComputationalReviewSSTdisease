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

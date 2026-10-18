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
# Direction of effect is categorical. Every numeral quoted is verbatim from the
# source sentence; nothing is pooled, converted or averaged. Rows are ordered by
# the rigor of the design that produced the result, which is the figure's claim.
# ---------------------------------------------------------------------------
# (intervention, design, direction, marker, endpoint as reported)
pre = [
    ("MGE progenitor graft", "single study, amyloid host", "benefit", "D",
     "slow-oscillation power raised; graft matures into PV and SST cells\nin near-equal proportions"),
    ("SSTR4 agonist", "single programme, no independent\nreplication retrieved", "benefit", "o",
     "cortical Sstr4 4.9x, neprilysin 9.3x, IDE 14.8x, catalase 3.6x at 24 h\n(subcortical effects not significant)"),
    ("SSTR4 agonist", "single programme, no independent\nreplication retrieved", "benefit", "o",
     "learning improved; soluble A-beta42 oligomers lowered"),
    ("40 Hz stimulation", "single programme; independent\nreplications reported elsewhere", "benefit", "^",
     "amyloid and plaque load lowered in mouse cortex and hippocampus"),
]
hum = [
    ("Levetiracetam", "randomized, target-engagement\nendpoint", "mixed", "s",
     "n = 17: hyperactivity-sensitive task improved,\nstandard delayed recall unchanged"),
    ("Levetiracetam", "randomized crossover, halted\nbefore completion", "not established", "s",
     "8 of a planned 30 recruited: tolerability established, efficacy not"),
    ("Gamma stimulation", "synthesis across clinical trials", "no separation", "^",
     "no significant improvement in global cognition under protocols\nof up to four weeks"),
]
COL = {"benefit": COLORS["increase"], "mixed": COLORS["sst"],
       "no separation": COLORS["no_change"], "not established": COLORS["no_change"]}
XC = {"marker": 0.015, "interv": 0.055, "design": 0.235, "dirn": 0.50, "end": 0.63}

fig = plt.figure(figsize=(9.8, 5.4))
gs = GridSpec(2, 1, height_ratios=[1.12, 0.9], hspace=0.42, figure=fig)

for k, (dat, title) in enumerate([
        (pre, "(A) Preclinical entries - rodent models, on their own panel"),
        (hum, "(B) Human interventional entries")]):
    ax = fig.add_subplot(gs[k]); ax.axis("off")
    ax.set_title(title, fontsize=9.5, loc="left", fontweight="bold", pad=18)
    n = len(dat)
    step = 1.0 / (n + 0.6)
    for lbl, xc in [("intervention", "interv"), ("design", "design"),
                    ("direction", "dirn"), ("endpoint, as reported", "end")]:
        ax.text(XC[xc], 1.0, lbl, fontsize=7.8, fontweight="bold", va="center", transform=ax.transAxes)
    for i, (iv, dz, d, mk, endpoint) in enumerate(dat):
        y = 1.0 - (i + 1) * step
        ax.axhline(y - 0.5 * step, xmin=0.0, xmax=1.0, color=COLORS["light_gray"], lw=0.5)
        ax.plot(XC["marker"], y, marker=mk, ms=10, mfc=COL[d], mec="black", mew=0.8,
                transform=ax.transAxes, clip_on=False)
        ax.text(XC["interv"], y, iv, fontsize=7.6, va="center", transform=ax.transAxes)
        ax.text(XC["design"], y, dz, fontsize=7.2, va="center", transform=ax.transAxes)
        ax.text(XC["dirn"], y, d, fontsize=7.6, va="center", fontweight="bold",
                color=COL[d] if d in ("benefit", "mixed") else "black", transform=ax.transAxes)
        ax.text(XC["end"], y, endpoint, fontsize=7.0, va="center", transform=ax.transAxes)
    ax.annotate("", xy=(-0.012, 0.02), xytext=(-0.012, 0.93), xycoords=ax.transAxes,
                arrowprops=dict(arrowstyle="->", color=COLORS["neutral_gray"], lw=1.0))
    ax.text(-0.028, 0.5, "increasing design rigor", rotation=90, va="center", ha="center",
            fontsize=7.2, color=COLORS["neutral_gray"], transform=ax.transAxes)

fig.text(0.012, 0.012,
         "Heterogeneous comparison - values are not pooled and no summary estimate is shown. Direction of effect is categorical because the endpoints (transcript induction, amyloid\n"
         "load, oscillatory power, cognitive composites) are not commensurable; panels A and B share no scale. Marker shape: circle = somatostatin receptor agonist, triangle = 40 Hz\n"
         "stimulation, diamond = cell transplantation, square = antiseizure pharmacology. The human panel holds the three interventional entries this chapter cites.",
         fontsize=7.0, va="bottom")
fig.subplots_adjust(left=0.055, right=0.995, top=0.92, bottom=0.16)
save_figure(fig, os.path.join(FIGDIR, "fig_sec12_intervention_effect_versus_design_rigor.png"))
print("saved")

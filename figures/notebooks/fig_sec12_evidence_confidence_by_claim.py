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
# Tier placement is the replication status recorded for the specific studies
# each claim rests on, as stated in the cited sections. No counts are implied.
# ---------------------------------------------------------------------------
tiers = ["independently\nreplicated", "within-lab or\nsingle\nprogramme", "single\nstudy",
         "contested", "not tested in\nthe retrieved\nrecord"]

rows = [
    ("Reduction of the somatostatin signal\nin affected cortex", [0], [],
     "four decades, four non-interconvertible assay families"),
    ("Proportional depletion of somatostatin-\nannotated neurons in AD cortex", [0], [3],
     "annotation independent of peptide detection; a resilience\ncohort reads comparable data the other way"),
    ("Cell-intrinsic vulnerability of the\nSST class", [], [2],
     "sleep-disruption route shown outside amyloid pathology; the\nER-stress route rests on one small-sample study"),
    ("Somatostatin to neprilysin to amyloid-beta\nas a causal route", [], [1, 3],
     "protein engineering raises the enzyme in vivo; the one amyloid\nknock-in cross of the ligand knockout is negative on the enzyme"),
    ("Circuit consequences of reduced\nsomatostatin signalling", [0], [2],
     "dendritic and oscillatory signature replicated in healthy\nanimals; rescue inside a disease model is a single report"),
    ("CSF somatostatin as a diagnostic marker", [], [4],
     "group differences only; no sensitivity, specificity or AUC\nin the retrieved record"),
    ("Therapeutic benefit obtained by acting\non SST interneurons", [], [1, 3],
     "rodent pathway from one programme; human trials null,\nhalted or target-engagement only"),
]

fig = plt.figure(figsize=(9.6, 5.4))
ax = fig.add_subplot(111)
ny = len(rows)
for j in range(len(tiers)):
    ax.axvline(j, color=COLORS["light_gray"], lw=0.6, zorder=0)
for i, (lab, strong, weak, note) in enumerate(rows):
    y = ny - 1 - i
    ax.axhline(y, color=COLORS["light_gray"], lw=0.5, zorder=0)
    for j in strong:
        ax.plot(j, y, marker="s", ms=13, color=COLORS["sst"], zorder=3)
    for j in weak:
        ax.plot(j, y, marker="s", ms=13, mfc="white", mec=COLORS["increase"], mew=1.6, zorder=3)
    ax.text(len(tiers) - 0.55, y, note, fontsize=7.2, va="center", color="black")

ax.set_xticks(range(len(tiers))); ax.set_xticklabels(tiers, fontsize=8)
ax.set_yticks(range(ny)); ax.set_yticklabels([r[0] for r in rows][::-1], fontsize=8)
ax.set_xlim(-0.55, len(tiers) + 3.3)
ax.set_ylim(-0.7, ny - 0.3)
ax.xaxis.set_ticks_position("top"); ax.xaxis.set_label_position("top")
for sp in ["top", "right", "bottom", "left"]:
    ax.spines[sp].set_visible(False)
ax.tick_params(length=0)
ax.text(len(tiers) - 0.55, ny - 0.55, "evidence note", fontsize=8, fontweight="bold", va="center")
fig.text(0.015, 0.015,
         "Filled square = a status the claim rests on where the underlying studies are independently replicated; open square = a status recorded without replication, "
         "and a row may carry open\nsquares only. Placement is the status recorded for the named studies in the cited sections, not a count of findings. "
         "Rows are not comparable in sample size, species or measurement type.",
         fontsize=7.2, va="bottom")
fig.subplots_adjust(left=0.23, right=0.995, top=0.83, bottom=0.11)
save_figure(fig, os.path.join(FIGDIR, "fig_sec12_evidence_confidence_by_claim.png"))
print("saved")

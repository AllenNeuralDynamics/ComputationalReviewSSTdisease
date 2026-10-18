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

save_figure(fig, os.path.join(OUT_DIR, "fig_sec2_sst_connectivity_motif_disagreements.png"))
print("saved", os.path.join(OUT_DIR, "fig_sec2_sst_connectivity_motif_disagreements.png"))

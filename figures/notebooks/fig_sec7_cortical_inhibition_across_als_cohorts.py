import sys, pathlib
sys.path.insert(0, str(pathlib.Path.cwd()))

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from shared_style import COLORS, apply_style, save_figure

apply_style()
OUT = "../fig_sec7_cortical_inhibition_across_als_cohorts.png"

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

save_figure(fig, OUT)
print("saved", OUT)

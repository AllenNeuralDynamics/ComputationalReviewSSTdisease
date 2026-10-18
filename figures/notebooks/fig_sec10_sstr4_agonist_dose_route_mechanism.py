"""Figure: SSTR4 agonist dose, route and endpoint (section 10).

Table-form figure. No shared numeric axis and no bars: the four reported
results are a behavioural preference ratio, two Abeta x-42 protein
measurements and a set of qPCR fold-changes, which share no measurement
scale. Every cell is quoted from that entry's own source sentence, and no
row carries a group size because none is stated in the result sentence or
the abstract.
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath("__file__")) if "__file__" not in globals() else os.path.dirname(os.path.abspath(__file__)))

import matplotlib.pyplot as plt
from shared_style import COLORS, apply_style, save_figure

apply_style()
OUTDIR = ".."   # notebooks live in figures/notebooks/; figures are written to figures/

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

save_figure(fig, os.path.join(OUTDIR, "fig_sec10_sstr4_agonist_dose_route_mechanism.png"))

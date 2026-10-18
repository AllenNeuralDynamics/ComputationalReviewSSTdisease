"""Shared figure style for the review.

Every figure notebook imports COLORS, apply_style and save_figure from this module so
that the published figures share one palette, font, line weight and DPI. Palette keys
are additive: both case variants of the cell-type keys resolve to the same colour, so a
notebook written against either spelling renders identically.
"""

import matplotlib.pyplot as plt

COLORS = {
    'NPY_NOS': '#009E73',
    'PV': '#D55E00',
    'SST': '#0072B2',
    'VIP': '#CC79A7',
    'abstract_marker': '#FFB347',
    'active_arm': '#0072B2',
    'annotation': '#444444',
    'background': '#FFFFFF',
    'bracket': '#8C6D31',
    'conflict_marker': '#E41A1C',
    'decrease': '#2166AC',
    'excitatory': '#666666',
    'excitatory_pyramidal': '#666666',
    'fulltext_marker': '#4DAF4A',
    'highlight_orange': '#FF7F00',
    'increase': '#B2182B',
    'light_gray': '#CCCCCC',
    'mixed_GABAergic': '#56B4E9',
    'mixed_gabaergic': '#56B4E9',
    'neutral_gray': '#7F7F7F',
    'no_change': '#BBBBBB',
    'not_quantified': '#FFFFFF',
    'not_quantified_edge': '#7F7F7F',
    'not_quantified_face': '#FFFFFF',
    'npy_nos': '#009E73',
    'primary_blue': '#377EB8',
    'primary_brown': '#A65628',
    'primary_green': '#4DAF4A',
    'primary_orange': '#FF7F00',
    'primary_purple': '#984EA3',
    'primary_red': '#E41A1C',
    'pv': '#D55E00',
    'sham_arm': '#BBBBBB',
    'simulated': '#8C8C8C',
    'sst': '#0072B2',
    'vip': '#CC79A7',
}

def apply_style():
    """Set matplotlib rcParams to the document standard."""
    plt.rcParams.update({
        "font.family":      "DejaVu Sans",      # available in every matplotlib install
        "font.size":         9,
        "axes.labelsize":   10,
        "axes.titlesize":   11,
        "xtick.labelsize":   9,
        "ytick.labelsize":   9,
        "legend.fontsize":   8,
        "figure.titlesize": 12,
        "axes.linewidth":    0.8,
        "lines.linewidth":   1.2,
        "axes.spines.top":   False,
        "axes.spines.right": False,
        "savefig.dpi":      300,
        "savefig.facecolor": "white",
        "figure.facecolor":  "white",
        "axes.facecolor":    "white",
    })


def save_figure(fig, path):
    """Save a figure to disk at the document standard (300 DPI, white bg)."""
    fig.savefig(path, dpi=300, bbox_inches="tight", facecolor="white")

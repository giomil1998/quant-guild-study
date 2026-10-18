"""One plotting style for every notebook, so the portfolio looks consistent."""

import matplotlib.pyplot as plt
import seaborn as sns

PALETTE = ["#2a6fdb", "#e4572e", "#17a398", "#f3a712", "#6c4f8c", "#4d4d4d"]


def set_style() -> None:
    sns.set_theme(style="whitegrid", palette=PALETTE)
    plt.rcParams.update(
        {
            "figure.figsize": (11, 5),
            "figure.dpi": 110,
            "axes.titleweight": "bold",
            "axes.spines.top": False,
            "axes.spines.right": False,
            "legend.frameon": False,
        }
    )

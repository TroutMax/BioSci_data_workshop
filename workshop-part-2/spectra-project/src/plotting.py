"""Reusable plotting helpers for emission spectra.

Works on any CSV / XLSX / TSV whose FIRST column is wavelength (nm)
and SECOND column is intensity.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def wavelength_to_rgb(nm):
    """Approximate display colour of a visible wavelength (380-750 nm)."""
    if 380 <= nm < 440:
        r, g, b = -(nm - 440) / 60, 0.0, 1.0
    elif 440 <= nm < 490:
        r, g, b = 0.0, (nm - 440) / 50, 1.0
    elif 490 <= nm < 510:
        r, g, b = 0.0, 1.0, -(nm - 510) / 20
    elif 510 <= nm < 580:
        r, g, b = (nm - 510) / 70, 1.0, 0.0
    elif 580 <= nm < 645:
        r, g, b = 1.0, -(nm - 645) / 65, 0.0
    elif 645 <= nm <= 750:
        r, g, b = 1.0, 0.0, 0.0
    else:
        r, g, b = 0.4, 0.4, 0.4          # outside visible: grey
    return (r * 0.85, g * 0.85, b * 0.85)  # darken slightly for white backgrounds


def load_spectrum(path):
    """Read a spectrum file. Returns (DataFrame[wavelength, intensity], label)."""
    path = Path(path)
    if path.suffix == ".csv":
        df = pd.read_csv(path)
    elif path.suffix in (".xlsx", ".xls"):
        df = pd.read_excel(path)
    elif path.suffix in (".tsv", ".txt"):
        df = pd.read_csv(path, sep="\t")
    else:
        raise ValueError(f"Don't know how to read '{path.suffix}' files")
    df = df.iloc[:, :2].dropna()              # column POSITION, not name
    label = str(df.columns[1])
    df.columns = ["wavelength", "intensity"]
    return df, label


def plot_spectrum(path, ax=None, normalise=True, color=None, save_to=None):
    """Plot one emission spectrum in the house style. Returns the Axes."""
    df, label = load_spectrum(path)
    if normalise:
        df["intensity"] = df["intensity"] / df["intensity"].max()
    peak = df.loc[df["intensity"].idxmax(), "wavelength"]
    color = color or wavelength_to_rgb(peak)

    if ax is None:
        _, ax = plt.subplots(figsize=(7, 3.8))
    ax.plot(df["wavelength"], df["intensity"], color=color, lw=2, label=label)
    ax.fill_between(df["wavelength"], df["intensity"], color=color, alpha=0.18)
    ax.axvline(peak, color=color, ls=":", lw=1)
    ax.annotate(f"peak {peak:.0f} nm", (peak, df["intensity"].max()),
                xytext=(0, 6), textcoords="offset points", ha="center",
                color=color, fontsize=10)
    ax.margins(y=0.15)
    ax.set_xlabel("Wavelength (nm)")
    ax.set_ylabel("Normalised intensity" if normalise else "Intensity")
    ax.set_title(label)
    ax.spines[["top", "right"]].set_visible(False)

    if save_to:
        ax.figure.savefig(save_to, dpi=300, bbox_inches="tight")
    return ax

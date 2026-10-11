"""Plot every spectrum in data/raw/ into outputs/figures/.

Run from the project root:   python -m scripts.make_plots
"""
from pathlib import Path

import matplotlib.pyplot as plt

from src.plotting import plot_spectrum

OUT = Path("outputs/figures")
OUT.mkdir(parents=True, exist_ok=True)   # outputs/ is git-ignored, so create it here

for f in sorted(Path("data/raw").glob("*_em.*")):
    plot_spectrum(f, save_to=OUT / f"{f.stem}.png")
    plt.close("all")
    print("saved", f.stem)

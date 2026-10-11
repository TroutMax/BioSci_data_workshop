"""Download the two example spectra from FPbase (https://www.fpbase.org, CC BY-SA 4.0).

Run from the project root:   python scripts/download_data.py

If this fails (e.g. HTTP 403), open the URLs below in a browser, save the files into
data/raw/ with the names shown, and carry on.
"""
import urllib.request
from pathlib import Path

import pandas as pd

RAW = Path("data/raw")
RAW.mkdir(parents=True, exist_ok=True)


def fetch(url, dest):
    if dest.exists():
        print("already have", dest)
        return
    # FPbase returns 403 to Python's default User-Agent, so identify as a browser.
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (workshop script)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        dest.write_bytes(r.read())


fetch("https://www.fpbase.org/spectra_csv/?q=9077", RAW / "nanoluc_em.csv")   # save as nanoluc_em.csv

if not (RAW / "egfp_em.xlsx").exists():
    tmp = RAW / "_egfp_raw.csv"                                               # save as _egfp_raw.csv
    fetch("https://www.fpbase.org/spectra_csv/?q=17,18,173", tmp)
    pd.read_csv(tmp)[["wavelength", "EGFP em"]].dropna().to_excel(RAW / "egfp_em.xlsx", index=False)
    tmp.unlink()
print("Done:", sorted(p.name for p in RAW.iterdir()))

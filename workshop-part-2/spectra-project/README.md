# Spectra project

Part of the workshop repo, folder `part2/spectra-project`. Get it with **Code → Download ZIP** (then open that folder) or `git clone`.

Plot emission spectra (NanoLuc, EGFP) in one consistent style.

## Setup (PyCharm)
1. **File → Open** this folder. PyCharm offers to create a virtual environment; accept it
   (interpreter type *Virtualenv*, location `.venv`). If you skip it: *Settings → Project → Python Interpreter → Add Interpreter → Virtualenv*.
2. Open the **Terminal** tab. You should see `(.venv)` at the start of the prompt.
3. Install packages:
   ```bash
   pip install -r requirements.txt
   ```

### Setup (any terminal, no PyCharm)
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
Windows PowerShell blocks `activate`? Run once: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.

## Run
```bash
python scripts/download_data.py   # fetch data into data/raw/
python -m scripts.make_plots      # figures -> outputs/figures/
```
If the download fails (HTTP 403), save the two links in `scripts/download_data.py` from your browser into `data/raw/` as named in the comments.

## Layout
| Folder | Contains |
|---|---|
| `data/raw/` | Original data. **Never edit by hand.** |
| `src/` | Reusable code (`plotting.py`) |
| `scripts/` | Things you run |
| `notebooks/` | Exploration |
| `outputs/` | Generated figures (safe to delete, re-make any time) |

Data: [FPbase](https://www.fpbase.org), CC BY-SA 4.0.

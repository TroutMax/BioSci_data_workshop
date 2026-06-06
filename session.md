# Workshop Build Session — Summary
**Date:** 2026-05-24
**Project:** Introduction to Data Analysis with Python (45-min workshop)

---

## What was built

A complete, ready-to-deliver workshop for biomedical/biology grad students with no prior Python experience.

### Files

| File | Purpose |
|------|---------|
| `workshop_notebook.ipynb` | 56-cell Colab notebook — the main hands-on material |
| `slides_outline.md` | 16-slide presenter deck with speaker notes and timing guide |
| `resources.md` | Take-home guide: setup, tools, mini project, links |
| `requirements.txt` | `pandas matplotlib seaborn scipy requests feedparser` |
| `mini_project_news/news_scraper.py` | Post-workshop project: RSS feed → HTML webpage |
| `README.md` | GitHub repo landing page with Open-in-Colab badge |
| `.gitignore` | Excludes `.venv/`, `.idea/`, generated `news.html`, etc. |

---

## Key decisions made

### Dataset
**HDRUK/los_review** — COVID-19 hospital length of stay systematic review (Rees et al., 2020, *BMC Medicine*).

Chosen over other HDRUK repos because:
- Real published clinical data in CSV format, loadable directly from a GitHub URL
- Immediately relatable to biomedical students (patients, hospitals, COVID-19)
- 76 columns — messy enough to demonstrate cleaning, rich enough for meaningful analysis
- Mix of categorical (Country, severity, treatment) and numerical (age, LOS, sample size) variables

Key columns used: `Country`, `covid_severity`, `outcome`, `N`, `perc_male`, `age_med`, `LOS_med`, `LOS_ICU_med`

Filtering: rows where `Author` is NaN are sub-group rows — dropped with `df.dropna(subset=["Author"])`.

### Workshop approach
Application-first (not syntax-first): start with a real dataset and explain Python as it appears. Goal is inspiration and a working notebook students leave with, not comprehensive Python training.

### Excel comparison framing
The user's own repo ([Data Analysis Workflow – Plant Growth](https://github.com/forest929/Data_Analysis_workfow_plant_growth)) provided the framework — a 7-step research workflow (collect → organise → explore → clean → save → quick check → analyse). This became the backbone for the Excel vs Python comparison slides and the `groupby` = Pivot Table demonstration in the notebook.

---

## Notebook structure (56 cells)

1. **Title & overview**
2. **From Excel to Python map** — 9-row table linking Excel tools to pandas equivalents
3. **Setup** — library imports, `!pip install` cell for local use
4. **Section 1: Load** — `pd.read_csv()` from GitHub URL, `.shape`, `.columns`, `.head()`
5. **Section 2: Explore & clean** — column selection, `dropna`, missing values audit, `value_counts`, `describe`, `groupby` (Pivot Table equivalent)
6. **Section 3: Visualise** — bar chart (studies by country), histogram (LOS distribution), box plot (LOS by severity), scatter (sample size vs LOS coloured by China/Other), heatmap (median LOS by severity × outcome)
7. **Section 4: Statistics** — Mann-Whitney U test comparing China vs other countries; result visualised with annotated box plot
8. **Section 5: Your turn** — 3 exercises with commented-out hints
9. **Section 6: Resources** — links table including the plant growth repo

---

## Slides structure (16 slides)

| Slide | Content |
|-------|---------|
| 1 | Title |
| 2 | The Pain You Already Know (Excel problems) |
| 3 | What Python Can Do For Your Research |
| 4 | The 7-Step Research Workflow (from plant growth repo) |
| 5 | Excel vs Python: Same Task, Same Data (Pivot Table → groupby) |
| 6 | Today's Workshop |
| 7 | The Tools (Colab, VS Code, PyCharm, JupyterLab) |
| 8 | Where Code Lives: GitHub |
| 9 | The Dataset |
| 10–13 | Live coding slides (one per notebook section) |
| 14 | Your Turn |
| 15 | What's Next + resources |
| 16 | Q&A |

**Buffer strategy:** drop scatter plot if running long; dwell on Slide 5 (Excel vs Python) if running short.

---

## Mini project: news scraper

`mini_project_news/news_scraper.py` — fetches any RSS or Atom feed, generates a styled HTML page, opens it in the browser.

### Feed format support
Three formats encountered and handled:

| Format | Example | Structure |
|--------|---------|-----------|
| RSS 2.0 | BBC News | `<rss> → <channel> → <item>` |
| RSS 1.0 / RDF | Nature | `<RDF> → <item>` (items at root level, not inside channel) |
| Atom | Many modern feeds | `<feed> → <entry>` with `<link href="">` attribute |

### Issues resolved during session

**1. Nature feed (`https://www.nature.com/nature.rss`)**
- Error: `'NoneType' object has no attribute 'findtext'`
- Cause: RSS 1.0/RDF format — `<item>` elements are siblings of `<channel>` at root level, not children of it
- Fix: after `findall(channel, "item")` returns empty, fall back to `findall(root, "item")`

**2. PubMed feed (`https://pubmed.ncbi.nlm.nih.gov/rss/search/?term=CRISPR&format=rss`)**
- Error: `ParseError: mismatched tag`
- Cause: URL returns an HTML page (Content-Type: text/html) — PubMed RSS requires a session token generated from the website
- Fix: replaced with working science feeds (bioRxiv, Lancet, Science magazine); added a content-type pre-check that prints a clear error message if a URL returns HTML instead of XML

**3. Custom XML parser complexity**
- The hand-rolled namespace-stripping parser grew unwieldy across three feed formats
- Fix: replaced entirely with `feedparser` (6.0.12) — handles RSS 0.9/1.0/2.0, Atom, malformed XML, and encoding in one call; parsing section reduced from ~40 lines to ~10

### Working feed URLs

| Source | URL |
|--------|-----|
| BBC News | `https://feeds.bbci.co.uk/news/rss.xml` |
| Nature | `https://www.nature.com/nature.rss` |
| bioRxiv bioinformatics | `https://connect.biorxiv.org/biorxiv_xml.php?subject=bioinformatics` |
| The Lancet | `https://www.thelancet.com/rssfeed/lancet_online.xml` |
| Science magazine | `https://www.science.org/rss/news_current.xml` |
| Guardian Science | `https://www.theguardian.com/science/rss` |
| PubMed | Generate from website: search → "Create RSS" → copy URL |

---

## GitHub repo

**Repo:** `github.com/forest929/python-data-workshop`

- Initialised locally with `git init`, committed, pushed to GitHub
- README includes Open-in-Colab badge wired to the notebook
- `.gitignore` excludes `.venv/`, `.idea/`, `__pycache__/`, generated `news.html`
- Students share link: `github.com/forest929/python-data-workshop`
- Students open notebook: click badge in README → opens directly in Colab

### Sharing resources.md with students
Three options discussed:
1. Append content as final notebook cells (simplest)
2. GitHub repo link — GitHub renders `.md` files natively (recommended, already done)
3. In-Colab cell: `feedparser.parse` the raw GitHub URL and `display(Markdown(...))`

---

---

## Notebook improvements (second session)

### Flow and delivery
- Opening cell rewritten with a three-line research hook (*"100+ papers, one CSV, 45 minutes"*) to give students an immediate reason to engage
- Timing markers (`⏱ N min`) added to every section header
- Fixed misleading note about blank rows — clarified that subgroup rows (same Author, blank StudyNo) are valid cohorts; only truly empty rows are dropped
- 8 new interpretation/callout cells inserted after key outputs: missing-value table, value_counts, groupby severity, country bar chart, histogram, severity boxplot, scatter, and Mann-Whitney test
- Stat test section (Section 4) now includes explicit H₀/H₁ hypotheses and a "why Mann-Whitney?" rationale before the code
- Post-test callout explains that "not significant ≠ no difference" and flags the low statistical power problem
- Exercises renamed descriptively and each given an **Expected output** block so students can self-check
- Key Takeaways table added as a wrap-up cell before Resources

### Plot style
All plots updated to publication style:

| Setting | Value |
|---------|-------|
| Theme | `sns.set_theme(style="white", context="paper", font_scale=1.2)` per plot cell |
| Spines | `sns.despine(ax=ax)` on every plot |
| Figure size | `(7.2–7.5, 4.8)` consistently |
| Bar charts | `color="0.55"`, `edgecolor="black"`, `linewidth=0.8`, `width=0.7`, subtle y-gridlines |
| Histograms | Matching neutral grey, `edgecolor="black"`, subtle y-gridlines |
| Box plots | White fill (`facecolor="white"`), explicit `boxprops` / `whiskerprops` / `capprops` / `medianprops` / `flierprops`, grey jitter strip (`color="0.35"`, `jitter=0.18`) |
| Scatter | Small points (`s=32`) with thin black edges (`linewidths=0.4`), `frameon=False` legends |
| Heatmap | `cmap="YlOrRd"`, white grid lines, `mask` for empty cells, two-line annotation (value + n) |

### Heatmap replaced
Original heatmap (Country × Severity) was ~90% empty because only China has LOS data.  
Replaced with **Severity × Outcome → median LOS**:
- Both axes well-populated; meaningful for all category combinations
- Rows ordered clinically: Mild → Non-severe → Moderate → Severe → All
- Columns: Alive → All → Dead
- Each cell annotated with median value and sample size (`14.0\n(n=52)`)
- `mask=heatmap_data.isna()` hides empty cells cleanly

### Outreach email drafted
Short email to BioSci Toolkit team lead asking her to identify a co-designer volunteer, describing the 45-min practical workshop and the bonus news-scraper project.

---

## Remaining before delivery

- [ ] Push latest commits (`feedparser` fix) to GitHub: `git push`
- [ ] Upload `workshop_notebook.ipynb` to Google Colab, get shareable link, add to Slide 16
- [ ] Test the full notebook runs top-to-bottom in Colab without errors
- [ ] Replace Colab badge URL in README if repo name differs from `python-data-workshop`

---

---

## Workshop Notebook 4 (session 2026-05-25)

**File:** `workshop_notebook_4.ipynb`  
**Style reference:** Wang et al., *Journal of Bacteriology*, October 2024 ([PMID 39329528](https://pubmed.ncbi.nlm.nih.gov/39329528/)) — the user's own publication.  
**Dataset:** COVID-19 OWID — loaded directly via raw GitHub URL (`raw.githubusercontent.com/owid/covid-19-data/...`).  
**Output PDFs:** `fig4a_violin_continent.pdf`, `fig4b_grouped_bar.pdf`, `fig4c_composite.pdf`

---

### Notebook structure (final)

| # | Section | Content |
|---|---------|---------|
| 0 | Setup | `!pip install`, imports, publication `rcParams`, `sig_stars` + `draw_bracket` helpers |
| 1 | Load & prepare data | `pd.read_csv(URL)`, annual aggregation, GDP tertile income groups |
| 2 | Explore the data | `df.shape`, `df.columns`, `df.info()`, `df.head()`, `df.describe()`, `value_counts()` |
| 3a | Violin + box chart | Continent mortality 2021; `plot_3a(ax)` function defined |
| 3b | Grouped bar chart | Income × year; `plot_3b(ax)` function defined |
| 3c | Composite 2-panel | `plot_3a(axes[0])` + `plot_3b(axes[1])` — 9 lines total |

---

### Figures

| Figure | Type | Scientific question |
|--------|------|---------------------|
| 3a | Violin + box + mean ± SEM | Which continent had the highest COVID-19 mortality in 2021? |
| 3b | Grouped bar + SEM + significance brackets | Did the income–mortality gap narrow from 2021 to 2023? |
| 3c | Composite 2-panel (A/B) | Both stories in one publication-ready figure |

---

### Key design decisions

**EDA section added (Section 2)**  
Exploratory data section inserted between load/prep and figures. Covers `df.shape`, `df.columns`, `df.info()`, `df.head()`, `df.describe()`, `value_counts()`. Includes a callout on why `df.info()` matters — NaN counts per column before computing means or running stats.

**GitHub raw URL tip added (Section 1)**  
Callout explaining how to get a raw CSV URL from any GitHub repo: navigate to file → click Raw button → copy address bar URL.

**Function-based composite (Section 3c)**  
3a and 3b each wrap their plotting code in `def plot_3a(ax)` / `def plot_3b(ax)`. The standalone plots call the function then set a title. 3c becomes 9 lines — `plt.subplots(1,2)`, two function calls, two `set_title` calls, `suptitle`, save. Teaching point: functions make compositing trivial.

**Exercises removed**  
All 9 exercise cells dropped to keep the notebook focused and within 45-min delivery time.

**Histogram (old 3c) removed**  
Removed to streamline the narrative — 3a and 3b tell a coherent two-part story; histogram was a third independent question.

---

**Opening introduction updated**  
Title changed from "Workshop Notebook 4" to "Introduction to Data Analysis with Python" to match the official workshop style of `workshop_notebook.ipynb`. Added dataset source link, row-level description ("one country on one day"), and a clear goal statement. Removed all "Notebook 3" cross-references so the notebook stands alone.

---

### Technical fixes

- Seaborn `FutureWarning` fixed in both violin cells: added `hue="continent", legend=False` alongside `palette=` (required from seaborn ≥ 0.14)
- Notebook executed end-to-end locally via `jupyter nbconvert --execute` — all 9 code cells ran clean, no errors, no warnings

---

### Figure 3b refinements

**Scatter removed**  
Individual country dots removed from the grouped bar chart — cleaner for workshop delivery.

**Bracket heights fixed (per-year local tops)**  
Original code placed all three year-group brackets at `data_top + step*(1+i)` — stacking from the 2021 global peak, leaving 2022 and 2023 brackets floating 2.6 and 4.4 data units above their bars. Fixed by anchoring each bracket to its own year's local bar top (`yr_tops[yr]`) with a fixed gap of `data_top * 0.12` — giving identical 8.3% axis-height clearance above every year's bars.

**All pairwise comparisons added**  
Extended from Low vs High only to all three pairs: Low–Middle, Middle–High, Low–High. Brackets stacked at fixed multipliers above the year's local top:

| Pair | Multiplier | Rationale |
|------|-----------|-----------|
| Low – Middle | `gap × 1.0` | Lowest, innermost |
| Middle – High | `gap × 1.8` | Middle tier |
| Low – High | `gap × 2.8` | Highest, widest span |

Fixed multipliers guarantee distinct bracket heights regardless of which income group has the tallest bar in a given year (per-bar-top approach collapsed in 2021 because High ≈ Middle). `ylim` raised to `data_top × 1.60`.

# Workshop Slide Outline
## "Introduction to Data Analysis with Python"
**Audience:** Biomedical/biology grad students (no prior coding experience)
**Duration:** 45 min | **Format:** Live coding + slides

---

## Slide 1 — Title
**Introduction to Data Analysis with Python**
Health Data Research UK — COVID-19 Length of Stay Dataset

*Your name / affiliation / date*

---

## Slide 2 — The Pain You Already Know
**Why are we here?**

- You have 50 Excel sheets from your experiments
- Copy-paste errors crept in somewhere on row 847
- Your collaborator uses a Mac. Your pivot table looks wrong on their machine.
- You need to re-do the whole analysis because one sample was excluded

> *"Python doesn't get tired. It doesn't make copy-paste errors. And it remembers exactly what you did."*

**Speaker note:** Ask the room: who has >5 Excel files open right now? Who has ever re-done an analysis from scratch?

---

## Slide 3 — What Python Can Do For Your Research

| Task | Excel | Python |
|------|-------|--------|
| Analyse 10,000 rows | Slow | Instant |
| Reproduce your analysis in 6 months | Hope you remember | Run the script |
| Make publication-quality figures | Painful | `matplotlib` / `seaborn` |
| Run statistics | Limited | `scipy`, `statsmodels` |
| Machine learning | No | `scikit-learn` |

**Speaker note:** Emphasise reproducibility — journals increasingly require code + data submission.

---

## Slide 4 — The 7-Step Research Workflow

**A framework you can apply to any dataset**

*(Based on the [Data Analysis Workflow – Plant Growth](https://github.com/forest929/Data_Analysis_workfow_plant_growth) guide)*

| Step | What you do | Tool |
|------|-------------|------|
| 1. Collect | Design your data sheet, record measurements | Paper / Excel template |
| 2. Organise | Enter in tidy format (one row = one observation) | Excel |
| **3. Explore** | Understand what you have | **Excel Pivot Tables → Python** |
| **4. Clean** | Fix inconsistencies, missing values, date formats | **Find & Replace → Python** |
| 5. Save cleaned | Separate raw and cleaned files, version names | `plant_growth_2025-08-11_clean.csv` |
| **6. Quick check** | Visual sanity check before analysis | **Charts → Python plots** |
| **7. Analyse** | Stats, comparisons, publication figures | **=T.TEST() → `scipy`** |

> Today we cover **steps 3, 4, 6, and 7** — the parts where Python replaces
> the most painful parts of the Excel workflow.

**Speaker note:** This workflow is universal — plant phenology, clinical trials, gene expression, behavioural data. The tools change; the steps don't.

---

## Slide 5 — Excel vs Python: Same Task, Same Data

**The Pivot Table problem**

You want to know: *"What is the mean hospital stay for each severity group?"*

**In Excel:**
1. Select all data → Insert → PivotTable
2. Drag `covid_severity` to Rows
3. Drag `LOS_med` to Values → Change to Average
4. Format the output
5. *(Repeat every time the data changes)*

**In Python — one line:**
```python
df.groupby("covid_severity")["LOS_med"].mean().round(1)
```

---

**Other direct comparisons:**

| Task | Excel | Python |
|------|-------|--------|
| Clean text inconsistencies | Find & Replace (manual, error-prone) | `df["col"].str.strip().str.lower()` |
| Handle dates | Format cells → TEXT() formulas | `pd.to_datetime(df["date"])` |
| Spot outliers | Conditional formatting (visual only) | `df.describe()` + box plot |
| Share your analysis | Email the file | Share a GitHub link or Colab URL |
| Re-run after data update | Redo every step manually | Run the script — done |

**Speaker note:** Don't frame this as "Excel is bad." Frame it as: Python makes the *tedious, error-prone parts* reproducible and fast. Many researchers use both — Excel for initial entry, Python for analysis.

---

## Slide 6 — Today's Workshop

**What we will do (45 min):**

1. Load a real published dataset — no setup, straight from GitHub
2. Explore and clean it
3. Build 3 visualisations
4. Answer a statistical question
5. Try it yourself

**What we will NOT do today:**
- Learn all of Python (that takes months)
- Write complex programs

> Goal: see what's possible. Leave with a working notebook you can adapt.

---

## Slide 7 — The Tools

### Where you write Python

| Tool | Best for | Setup |
|------|----------|-------|
| **Google Colab** | Getting started fast, sharing | Zero — just a browser |
| **VS Code** | Day-to-day research coding | 5 min install |
| **PyCharm** | Larger projects, debugging | 10 min install |
| **JupyterLab** | Notebook-first workflow | Via Anaconda |

**Today we use Colab** — open the shared link, no installation needed.

**Speaker note:** Show Colab briefly — the interface, how cells work, how to run a cell (Shift+Enter). Mention that Colab notebooks save to Google Drive.

---

## Slide 8 — Where Code Lives: GitHub

**GitHub = Google Drive for code**

- Every change is tracked (who changed what, when, and why)
- You can go back to any previous version
- Collaborate with your team without emailing files
- The dataset we're using today comes from a published GitHub repository

```
https://github.com/HDRUK/los_review
```

**Key concepts:**
- **Repository (repo):** a project folder tracked by Git
- **Commit:** a saved snapshot of your changes
- **Clone:** download a repo to your computer

**Speaker note:** Show the HDRUK/los_review repo briefly — the README, the `data/` folder, the CSV file. Emphasise this is a peer-reviewed publication with open data.

---

## Slide 9 — The Dataset

**COVID-19 Hospital Length of Stay: A Systematic Review**
Rees et al. (2020), *BMC Medicine*

- Extracted data from **100+ published studies**
- Each row = one patient cohort reported in a paper
- Variables: country, severity, sample size, age, length of stay

**Why this dataset?**
- Real clinical research — not toy data
- Relatable: these are patients, hospitals, outcomes you understand
- Messy enough to teach cleaning, rich enough to be interesting

| Variable | Meaning |
|----------|---------|
| `Country` | Where the study was conducted |
| `covid_severity` | Mild / Moderate / Severe / All |
| `N` | Number of patients |
| `LOS_med` | Median hospital stay (days) |
| `LOS_ICU_med` | Median ICU stay (days) |
| `age_med` | Median patient age |

**Speaker note:** Briefly explain what a systematic review is — many grad students will recognise the concept.

---

## Slide 10 — Live Coding: Section 1
### Load the Data

*Switch to Colab notebook — Section 1*

**Key concepts introduced:**
- `import` — bringing in a library
- `pd.read_csv()` — loading data from a URL
- `.shape` — dimensions of the table
- **DataFrame** — pandas' name for a table

**Talking points while coding:**
- "Notice we loaded data directly from a GitHub URL — no download"
- "76 columns — that's daunting. Real data is like this."
- "`.head()` is the first thing I run on any new dataset"

---

## Slide 11 — Live Coding: Section 2
### Explore & Clean

*Switch to Colab notebook — Section 2*

**Key concepts introduced:**
- Column selection (`df[list_of_cols]`)
- `.dropna()` — removing rows with missing values
- `.isnull().sum()` — auditing missingness
- `.value_counts()` — frequency table for categories
- `.describe()` — summary statistics in one line
- `.groupby()` — Pivot Table equivalent

**Talking points:**
- "Missing data is not a problem to hide — it's information. Here, NaN in LOS_ICU_med means the study didn't report ICU patients."
- "`.describe()` in one line replaces a whole Excel summary table"
- Before groupby cell: *"This is the moment Excel users feel at home — this is your Pivot Table."*

---

## Slide 12 — Live Coding: Section 3
### Visualise

*Switch to Colab notebook — Section 3*

**Three plots:**
1. **Bar chart** — Studies by country *(who was studying this?)*
2. **Histogram** — Distribution of LOS *(what does the data look like?)*
3. **Box plot** — LOS by severity *(does severity matter?)*
4. **Scatter** — Sample size vs LOS, coloured by China/Other

**Talking points:**
- After histogram: "Mean vs median — which is more appropriate when the data is skewed?"
- After box plot: "Each dot is one published paper. This is what meta-analysis looks like."

---

## Slide 13 — Live Coding: Section 4
### Ask a Statistical Question

*Switch to Colab notebook — Section 4*

**Research question:** Did patients in China have a different length of stay?

**Why Mann-Whitney U (not a t-test)?**
- LOS is right-skewed → parametric tests are inappropriate
- We're comparing medians
- Small-to-moderate group sizes

```python
stat, p = stats.mannwhitneyu(china_los, other_los, alternative="two-sided")
```

**Talking points:**
- "Three lines of code. In Excel this would take 20 minutes."
- "Choosing the right test matters more than knowing how to code it."
- Discuss the result: what might explain the difference (or lack of one)?

---

## Slide 14 — Your Turn

*Switch to Colab notebook — Section 5*

**3 exercises (7 min):**

1. What is the median patient age in ICU vs non-ICU studies?
2. Bar chart: mean LOS by country (top 6)
3. **Challenge:** Is LOS significantly different between Severe and All-patient cohorts?

**Speaker note:** Walk the room. Let people struggle briefly before revealing hints. Normalise errors — "getting a red error box is completely normal, it tells you exactly what's wrong."

---

## Slide 15 — What's Next

**Your immediate next steps:**

1. **Save this notebook** to your Google Drive — it's yours now
2. **Try it on your own data** — replace the CSV URL with a path to your file
3. **Install locally:** [Anaconda](https://www.anaconda.com/download) → VS Code + Python extension

**Learning path:**
```
This workshop
    → Kaggle Learn: Pandas (free, 4h)
    → The Carpentries: Data Analysis with Python
    → Your own dataset
    → scikit-learn for machine learning
```

**Useful one-liners to remember:**
```python
pd.read_csv("file.csv")              # load data
df.head()                            # preview
df.describe()                        # summary stats
df["col"].value_counts()             # category frequencies
df.groupby("group")["val"].mean()    # Pivot Table equivalent
df["col"].str.strip().str.lower()    # clean text (Find & Replace equivalent)
pd.to_datetime(df["date"])           # parse dates
```

**Further reading:**
- [Data Analysis Workflow – Plant Growth](https://github.com/forest929/Data_Analysis_workfow_plant_growth) — full 7-step workflow with Excel and Python examples, written for experimental biology

---

## Slide 16 — Q&A

**Questions?**

Workshop notebook: *[share Colab link here]*
Source data: `github.com/HDRUK/los_review`
Workflow reference: `github.com/forest929/Data_Analysis_workfow_plant_growth`

---

## Speaker Notes: Timing Guide

| Slide | Section | Cumulative time |
|-------|---------|----------------|
| 1–3 | Intro & motivation | 3 min |
| 4 | 7-step workflow | 5 min |
| 5 | Excel vs Python | 7 min |
| 6 | Today's workshop | 8 min |
| 7–8 | Tools & GitHub | 12 min |
| 9 | Dataset | 14 min |
| 10 | Live code: Load | 22 min |
| 11 | Live code: Clean + groupby | 30 min |
| 12 | Live code: Visualise | 38 min |
| 13 | Live code: Stats | 42 min |
| 14 | Your turn | 43 min |
| 15–16 | Next steps + Q&A | 45 min |

**Buffer strategy:** If running long, cut the groupby second cell (two-variable) and skip the scatter plot (Slide 12, plot 4). If running short, pause on Slide 5 and ask the room for their own Excel horror stories.

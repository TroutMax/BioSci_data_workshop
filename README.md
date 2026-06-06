# Introduction to Data Analysis with Python
### A 45-minute hands-on workshop for biomedical & biology researchers

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/forest929/python-data-workshop/blob/main/workshop_notebook_4.ipynb)

---

## What this workshop covers

A practical introduction to Python for researchers who use Excel today and want to produce publication-quality figures. No prior programming experience required.

| # | Section | Time |
|---|---------|------|
| 0 | Setup | 2 min |
| 1 | Load & prepare data | 5 min |
| 2 | Explore the data | 5 min |
| 3a | Violin + box chart | 8 min |
| 3b | Grouped bar chart | 8 min |
| 3c | Composite 2-panel figure | 7 min |

**Dataset:** Our World in Data — COVID-19 daily pandemic statistics for 240+ countries, 2020–2024.
Variables: smoothed death rates, vaccination coverage, GDP per capita.
*Source: [owid/covid-19-data](https://github.com/owid/covid-19-data)*

**Today's goal:** Build figures that look like they belong in a journal article — applying design conventions from a real *Journal of Bacteriology* paper to answer real epidemiological questions.

---

## Quick start

### Option A — Google Colab (no installation)

Click the **Open in Colab** badge above. The notebook loads instantly in your browser.

### Option B — Run locally

```bash
git clone https://github.com/forest929/python-data-workshop.git
cd python-data-workshop
pip install -r requirements.txt
jupyter lab workshop_notebook_4.ipynb
```

---

## Repository contents

```
├── workshop_notebook_4.ipynb   Main hands-on notebook (open this in Colab)
├── resources.md                Take-home guide: setup, tools, mini project, links
├── requirements.txt            Python packages needed to run locally
└── mini_project_news/
    └── news_scraper.py         Standalone post-workshop project (RSS → HTML webpage)
```

---

## After the workshop

See **[resources.md](./resources.md)** for:
- How to install Python and VS Code / PyCharm locally
- How to install packages with `pip` and `conda`
- Markdown and HTML basics
- Using Claude AI to help you code
- Step-by-step mini project: build a live news webpage with Python

---

## Workflow reference

This workshop follows the 7-step data analysis workflow developed for plant growth experiments — applicable to any experimental dataset:

> [Data Analysis Workflow – Plant Growth Experiments](https://github.com/forest929/Data_Analysis_workfow_plant_growth)

---

## License

Workshop materials: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to reuse and adapt with attribution.
Dataset: © HDRUK / Rees et al. 2020, used under open access terms.

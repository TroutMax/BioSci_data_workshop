# Introduction to Data Analysis with Python
### A 45-minute hands-on workshop for biomedical & biology researchers

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/forest929/python-data-workshop/blob/main/workshop_notebook.ipynb)

---

## What this workshop covers

A practical introduction to Python for researchers who use Excel today and want a more reproducible, scalable workflow. No prior programming experience required.

| Section | What you do |
|---------|-------------|
| Load data | Pull a real published dataset directly from GitHub into Python |
| Explore & clean | Select columns, handle missing values, audit categories |
| GroupBy | Replicate an Excel Pivot Table in one line |
| Visualise | Histogram, box plot, bar chart, scatter plot |
| Statistics | Mann-Whitney U test — China vs other countries |
| Your turn | 3 exercises with hidden hints |

**Dataset:** COVID-19 hospital length of stay — extracted from 100+ peer-reviewed studies.
*Rees et al. (2020), BMC Medicine. Source: [HDRUK/los_review](https://github.com/HDRUK/los_review)*

---

## Quick start

### Option A — Google Colab (no installation)

Click the **Open in Colab** badge above. The notebook loads instantly in your browser.

### Option B — Run locally

```bash
git clone https://github.com/forest929/python-data-workshop.git
cd python-data-workshop
pip install -r requirements.txt
jupyter lab workshop_notebook.ipynb
```

---

## Repository contents

```
├── workshop_notebook.ipynb     Main hands-on notebook (open this in Colab)
├── resources.md                Take-home guide: setup, tools, mini project, links
├── slides_outline.md           16-slide presenter deck with speaker notes
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

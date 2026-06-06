# After the Workshop — Resources & Next Projects

A self-contained guide for biomedical researchers who want to keep going after today's session.

---

## 1. Get Python on Your Computer

You have two routes. Pick one.

### Option A — Anaconda

Anaconda bundles Python, 300+ scientific packages, and the conda package manager in one installer.

1. Go to **[anaconda.com/download](https://www.anaconda.com/download)**
2. Download the installer for your OS (Mac / Windows / Linux)
3. Run the installer — accept all defaults
4. Open **Anaconda Navigator** from your Applications / Start Menu
5. Click **Launch** next to JupyterLab to open a notebook interface in your browser

**Why choose this:** everything scientific is pre-bundled — nothing to install separately. Note: the installer is large (~3 GB) and includes many packages you may never use.

### Option B — Python from python.org (recommended)

1. Go to **[python.org/downloads](https://www.python.org/downloads/)**
2. Download the latest stable release (e.g. Python 3.12.x)
3. Run the installer — on Windows, tick **"Add Python to PATH"** before clicking Install
4. Open your terminal (Mac: `Terminal`; Windows: `Command Prompt` or `PowerShell`)
5. Confirm it worked: `python --version`
6. Install just the packages you need (see Section 3): `pip install pandas matplotlib seaborn scipy`

**Why choose this:** lightweight (~30 MB), installs in seconds, and you only add packages you actually use. Recommended for most researchers.

---

## 2. Code Editors

A code editor is where you write and run Python files. Think of it as Word, but for code.

### VS Code (recommended — free, works for everything)

**Download:** [code.visualstudio.com](https://code.visualstudio.com/)

**Setup (5 min):**
1. Download and install VS Code
2. Open VS Code → click the **Extensions** icon in the left sidebar (looks like four squares)
3. Search for **Python** → install the extension by Microsoft
4. Search for **Jupyter** → install the extension by Microsoft
5. Open a `.py` file or `.ipynb` notebook — VS Code handles both

**Running a Python file in VS Code:**
- Open a `.py` file
- Press `Ctrl+F5` (Windows) / `Cmd+Shift+P` → "Run Python File" (Mac)
- Or click the ▷ play button in the top-right corner

**Running a notebook in VS Code:**
- Open a `.ipynb` file
- Select your Python interpreter (click bottom-left where it says "Select Kernel")
- Run cells with `Shift+Enter`

---

### PyCharm (great for larger projects)

**Download Community Edition (free):** [jetbrains.com/pycharm/download](https://www.jetbrains.com/pycharm/download/)
Scroll down to **Community** — the Professional edition requires a license.

**Setup:**
1. Install PyCharm
2. Open it → **New Project**
3. Choose a location, select your Python interpreter (PyCharm can auto-detect Anaconda)
4. Click **Create**

**Installing packages in PyCharm:**
- `File` → `Settings` (Windows) / `PyCharm` → `Preferences` (Mac)
- Go to **Project → Python Interpreter**
- Click the `+` button → search for a package → **Install Package**

---

## 3. Installing Python Packages

Packages extend Python with new capabilities. You install them with `pip` (Python's package manager).

### In your terminal / command prompt

```bash
# Install one package
pip install pandas

# Install several at once
pip install pandas matplotlib seaborn scipy

# Install a specific version
pip install pandas==2.1.0

# Upgrade an existing package
pip install --upgrade pandas

# See what's installed
pip list
```

### In a Jupyter notebook / Google Colab

Prefix the command with `!` to run shell commands from inside a notebook:

```python
!pip install pandas matplotlib seaborn scipy
```

### With conda (if you installed Anaconda)

```bash
conda install pandas matplotlib seaborn scipy
```

conda is often better than pip for scientific packages — it handles system-level dependencies automatically.

### Keeping packages tidy: virtual environments

For serious projects, use a **virtual environment** — an isolated Python installation per project, so packages don't conflict.

```bash
# Create a new environment called "myproject"
python -m venv myproject

# Activate it (Mac/Linux)
source myproject/bin/activate

# Activate it (Windows)
myproject\Scripts\activate

# Install packages into this environment only
pip install pandas matplotlib

# Deactivate when done
deactivate
```

---

## 4. Markdown & HTML Basics

### Markdown

Markdown is the lightweight text format used in Jupyter notebooks, GitHub READMEs, and this file.
It converts plain text into formatted HTML.

**Cheat sheet:**

```markdown
# Heading 1
## Heading 2

**bold**   *italic*   `inline code`

- bullet item
- another item

1. numbered item
2. second item

[Link text](https://example.com)

| Column A | Column B |
|----------|----------|
| value 1  | value 2  |

```python
# code block (with syntax highlighting)
print("Hello")
` `` `
```

**Reference:** [markdownguide.org/cheat-sheet](https://www.markdownguide.org/cheat-sheet/)

---

### HTML basics

HTML is the language of web pages. Python can generate HTML files automatically (see Section 6).

```html
<!DOCTYPE html>
<html>
<head>
    <title>Page title</title>
</head>
<body>
    <h1>This is a heading</h1>
    <p>This is a paragraph.</p>
    <a href="https://example.com">This is a link</a>
</body>
</html>
```

Save this as `page.html` and open it in your browser — that is a webpage.

---

## 5. Using Claude to Learn and Build

[Claude](https://claude.ai) is Anthropic's AI assistant. It is genuinely useful for learning to code because it explains *why*, not just *what*.

### Prompts that work well for researchers

**Explain a concept:**
> "Explain what a pandas DataFrame is, using an analogy to an Excel spreadsheet. I am a biologist with no prior coding experience."

**Debug an error:**
> "I am getting this error in Python: [paste the full error message]. Here is my code: [paste code]. What is wrong and how do I fix it?"

**Adapt code to your data:**
> "Here is a Python script that analyses COVID hospital data [paste script]. I have a CSV file from my plant growth experiment with columns: Date, Treatment, Plant_ID, Height_cm, Biomass_g. Adapt the script to work with my data."

**Learn by doing:**
> "Give me a step-by-step exercise to practise using pandas groupby on a small sample dataset you create for me."

**Generate boilerplate:**
> "Write a Python script that reads a CSV file, removes rows with missing values, and saves the cleaned version. Add comments explaining each line."

### Tips
- Paste your actual error messages — Claude can fix them precisely
- Ask for explanations alongside code, not just the code itself
- If an answer is too advanced, say: "Explain this more simply, I am a beginner"
- Use [Claude Code](https://claude.ai/code) for longer projects — it can read and edit your files directly

---

## 6. Mini Project — News Update Webpage

Build a Python script that fetches the latest BBC News headlines from a public RSS feed, formats them into a webpage, and opens it in your browser. No API key needed.

**What you will learn:** installing packages, HTTP requests, parsing XML, generating HTML, running a local web server.

**Time:** ~20–30 minutes

---

### Step 1 — Set up your project folder

Open your terminal and run:

```bash
mkdir news_project
cd news_project
```

Or create a new folder called `news_project` anywhere on your computer, then open it in VS Code:
`File → Open Folder → select news_project`

---

### Step 2 — Install the required package

Only one external package is needed — `requests` for fetching data from the web:

```bash
pip install requests
```

---

### Step 3 — Create the script

Create a new file called `news_scraper.py` inside `news_project` and paste the following code.
Every line is commented so you can follow along.

```python
import requests                        # fetches pages from the internet
import xml.etree.ElementTree as ET    # parses XML (built-in, no install needed)
import webbrowser                      # opens a file in your browser (built-in)
import os                              # file path utilities (built-in)
from datetime import datetime          # current date/time (built-in)

# --- 1. Choose your news feed ---
# This is a public BBC News RSS feed — no account or API key required.
# You can swap this URL for any RSS feed (Reuters, Nature, PubMed, etc.)
RSS_URL = "https://feeds.bbci.co.uk/news/rss.xml"

# --- 2. Fetch the feed ---
print("Fetching news headlines...")
response = requests.get(RSS_URL, timeout=10)
response.raise_for_status()   # raises an error if the request failed

# --- 3. Parse the XML ---
# RSS feeds are XML files. We navigate the tree to find each <item>.
root = ET.fromstring(response.content)
channel = root.find("channel")

feed_title = channel.findtext("title", default="News Feed")
articles = []

for item in channel.findall("item"):
    articles.append({
        "title":       item.findtext("title", ""),
        "description": item.findtext("description", ""),
        "link":        item.findtext("link", "#"),
        "pub_date":    item.findtext("pubDate", ""),
    })

print(f"Found {len(articles)} articles from: {feed_title}")

# --- 4. Build the HTML page ---
def make_card(article):
    """Turn one article dict into an HTML card."""
    return f"""
    <div class="card">
        <h2><a href="{article['link']}" target="_blank">{article['title']}</a></h2>
        <p class="date">{article['pub_date']}</p>
        <p class="desc">{article['description']}</p>
    </div>
    """

cards_html = "\n".join(make_card(a) for a in articles)
generated_at = datetime.now().strftime("%Y-%m-%d %H:%M")

html_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{feed_title}</title>
    <style>
        body {{
            font-family: Georgia, serif;
            max-width: 800px;
            margin: 40px auto;
            padding: 0 20px;
            background: #f5f5f5;
            color: #222;
        }}
        h1 {{ border-bottom: 2px solid #333; padding-bottom: 10px; }}
        .meta {{ color: #888; font-size: 0.9em; margin-bottom: 30px; }}
        .card {{
            background: white;
            border-radius: 8px;
            padding: 20px 24px;
            margin-bottom: 18px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.08);
        }}
        .card h2 {{ margin: 0 0 6px; font-size: 1.05em; }}
        .card h2 a {{ color: #1a0dab; text-decoration: none; }}
        .card h2 a:hover {{ text-decoration: underline; }}
        .date {{ color: #888; font-size: 0.82em; margin: 0 0 8px; }}
        .desc {{ margin: 0; line-height: 1.55; }}
    </style>
</head>
<body>
    <h1>📰 {feed_title}</h1>
    <p class="meta">Last updated: {generated_at} &nbsp;·&nbsp; {len(articles)} articles</p>
    {cards_html}
</body>
</html>
"""

# --- 5. Save to a file ---
output_file = "news.html"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_page)
print(f"Saved → {output_file}")

# --- 6. Open in your browser ---
webbrowser.open("file://" + os.path.abspath(output_file))
print("Done! Your browser should open automatically.")
```

---

### Step 4 — Run the script

In your terminal (make sure you are inside the `news_project` folder):

```bash
python news_scraper.py
```

A file called `news.html` will be created and your browser will open it automatically.

---

### Step 5 (bonus) — Serve it on a local web server

Opening a file directly with `file://` works, but a real web server is closer to how actual websites work. Python has one built-in:

1. Open a second terminal window inside `news_project`
2. Run:

```bash
python -m http.server 8000
```

3. Open your browser and go to: **[http://localhost:8000/news.html](http://localhost:8000/news.html)**
4. Press `Ctrl+C` in the terminal to stop the server

---

### Step 6 — Customise it

Try these modifications once the basic version works:

**Change the news source** — swap `RSS_URL` for any of these:

| Source | RSS URL |
|--------|---------|
| Nature | `https://www.nature.com/nature.rss` |
| Science magazine | `https://www.science.org/rss/news_current.xml` |
| The Lancet | `https://www.thelancet.com/rssfeed/lancet_online.xml` |
| bioRxiv – bioinformatics | `https://connect.biorxiv.org/biorxiv_xml.php?subject=bioinformatics` |
| The Guardian Science | `https://www.theguardian.com/science/rss` |
| BBC News | `https://feeds.bbci.co.uk/news/rss.xml` |

> **PubMed note:** PubMed RSS feeds require a personal token — you can't construct the URL manually.
> To get one: go to [pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov) → run your search → click **Create RSS** below the search bar → copy the generated URL.

**Auto-refresh every hour** — add a `<meta>` refresh tag in the HTML `<head>`:

```html
<meta http-equiv="refresh" content="3600">
```

**Filter by keyword** — add this after the `for item in channel...` loop:

```python
KEYWORD = "cancer"   # change to any word
articles = [a for a in articles if KEYWORD.lower() in a["title"].lower()]
print(f"Filtered to {len(articles)} articles containing '{KEYWORD}'")
```

**Schedule it to run daily** — on Mac/Linux, add a cron job:

```bash
# Open crontab
crontab -e

# Add this line to run the script every day at 8am
0 8 * * * /usr/bin/python3 /full/path/to/news_project/news_scraper.py
```

---

## 7. What to Learn Next

| Goal | Resource | Time |
|------|----------|------|
| Python fundamentals | [Python for Everybody — Coursera](https://www.coursera.org/specializations/python) | Free to audit |
| Pandas & data analysis | [Kaggle Learn: Pandas](https://www.kaggle.com/learn/pandas) | ~4 hours |
| Data viz | [Kaggle Learn: Data Visualization](https://www.kaggle.com/learn/data-visualization) | ~4 hours |
| Research data workflows | [The Carpentries](https://datacarpentry.org/lessons/) | Self-paced workshops |
| Web scraping (more advanced) | [Beautiful Soup docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) | Reference |
| Statistics in Python | [statsmodels.org](https://www.statsmodels.org/) | Reference |
| Machine learning | [Kaggle Learn: Intro to ML](https://www.kaggle.com/learn/intro-to-machine-learning) | ~3 hours |
| Version control | [Git — the simple guide](https://rogerdudler.github.io/git-guide/) | 15 min |
| Full workflow example | [Data Analysis Workflow – Plant Growth](https://github.com/forest929/Data_Analysis_workfow_plant_growth) | Reference |

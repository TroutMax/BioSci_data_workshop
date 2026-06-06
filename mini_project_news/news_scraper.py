"""
News Update Webpage — Mini Project
===================================
Fetches headlines from any RSS or Atom feed, builds an HTML page,
and opens it in your browser.

Requirements: pip install requests feedparser
Run with:     python news_scraper.py
"""

import feedparser
import webbrowser
import os
from datetime import datetime

# ---------------------------------------------------------------------------
# CONFIGURATION — edit these to customise your feed
# ---------------------------------------------------------------------------

# Uncomment the feed you want (or paste in any RSS/Atom URL)
# RSS_URL = "https://feeds.bbci.co.uk/news/rss.xml"                          # BBC News
# RSS_URL = "https://www.nature.com/nature.rss"                               # Nature
# RSS_URL = "https://www.theguardian.com/science/rss"                         # Guardian Science
# RSS_URL = "https://www.science.org/rss/news_current.xml"                    # Science magazine
RSS_URL = "https://www.thelancet.com/rssfeed/lancet_online.xml"             # The Lancet
# RSS_URL = "https://connect.biorxiv.org/biorxiv_xml.php?subject=bioinformatics"  # bioRxiv

# Note on PubMed: PubMed RSS links require a session token generated from the website.
# To get one: go to pubmed.ncbi.nlm.nih.gov → run a search → click "Create RSS" → copy the URL.

# Optional: only keep articles whose title contains this word (leave "" for all)
KEYWORD_FILTER = ""

# Output filename
OUTPUT_FILE = "news.html"

# ---------------------------------------------------------------------------
# 1. Fetch and parse the feed
#    feedparser handles RSS 0.9/1.0/2.0, Atom, and malformed XML automatically
# ---------------------------------------------------------------------------

print(f"Fetching: {RSS_URL}")

# Quick pre-check: if the server returns HTML instead of XML the URL is wrong
import requests as _req
_r = _req.get(RSS_URL, timeout=10)
if "html" in _r.headers.get("Content-Type", "").lower() and _r.text.lstrip().startswith("<!"):
    print("Error: the URL returned an HTML page, not a feed.")
    print("Check that the URL points directly to an RSS/Atom feed (it should start with <?xml).")
    print("For PubMed: go to pubmed.ncbi.nlm.nih.gov → search → 'Create RSS' → copy that URL.")
    raise SystemExit(1)

feed = feedparser.parse(RSS_URL)

if feed.bozo and not feed.entries:
    print(f"Error reading feed: {feed.bozo_exception}")
    raise SystemExit(1)

feed_title = feed.feed.get("title", "News Feed")
articles = []

for entry in feed.entries:
    articles.append({
        "title":    entry.get("title", "(no title)"),
        "description": entry.get("summary", ""),
        "link":     entry.get("link", "#"),
        "pub_date": entry.get("published", entry.get("updated", "")),
    })

print(f"Found {len(articles)} articles from: {feed_title}")

# Optional keyword filter
if KEYWORD_FILTER:
    articles = [a for a in articles if KEYWORD_FILTER.lower() in a["title"].lower()]
    print(f"Filtered to {len(articles)} articles containing '{KEYWORD_FILTER}'")

# ---------------------------------------------------------------------------
# 2. Build the HTML page
# ---------------------------------------------------------------------------

def make_card(article):
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

# ---------------------------------------------------------------------------
# 3. Save and open
# ---------------------------------------------------------------------------

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html_page)

print(f"Saved → {OUTPUT_FILE}")
webbrowser.open("file://" + os.path.abspath(OUTPUT_FILE))
print("Done! Check your browser.")
print()
print("Tip: to serve on a local web server instead, run:")
print(f"  python -m http.server 8000")
print(f"  then open http://localhost:8000/{OUTPUT_FILE}")

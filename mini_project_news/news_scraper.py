"""
News Update Webpage — Mini Project
===================================
Fetches headlines from a public RSS feed, builds an HTML page,
and opens it in your browser.

Requirements: pip install requests
Run with:     python news_scraper.py
"""

import requests
import xml.etree.ElementTree as ET
import webbrowser
import os
from datetime import datetime

# ---------------------------------------------------------------------------
# CONFIGURATION — edit these to customise your feed
# ---------------------------------------------------------------------------

RSS_URL = "https://feeds.bbci.co.uk/news/rss.xml"

# Optional: only keep articles whose title contains this word (leave "" for all)
KEYWORD_FILTER = ""

# Output filename
OUTPUT_FILE = "news.html"

# ---------------------------------------------------------------------------
# 1. Fetch the RSS feed
# ---------------------------------------------------------------------------

print("Fetching news headlines...")
try:
    response = requests.get(RSS_URL, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching feed: {e}")
    raise SystemExit(1)

# ---------------------------------------------------------------------------
# 2. Parse the XML
# ---------------------------------------------------------------------------

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

# Optional keyword filter
if KEYWORD_FILTER:
    articles = [a for a in articles if KEYWORD_FILTER.lower() in a["title"].lower()]
    print(f"Filtered to {len(articles)} articles containing '{KEYWORD_FILTER}'")

# ---------------------------------------------------------------------------
# 3. Build the HTML page
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
# 4. Save and open
# ---------------------------------------------------------------------------

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html_page)

print(f"Saved → {OUTPUT_FILE}")
webbrowser.open("file://" + os.path.abspath(OUTPUT_FILE))
print("Done! Check your browser.")
print()
print("Tip: to serve this on a local web server instead, run:")
print(f"  python -m http.server 8000")
print(f"  then open http://localhost:8000/{OUTPUT_FILE}")

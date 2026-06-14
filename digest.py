import feedparser
import requests
import json
from datetime import datetime

# Config
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

# Function to get the RSS feed
RSS_FEEDS = [
    "https://huggingface.co/blog/feed.xml",
    "https://www.marktechpost.com/feed/",
    "https://towardsdatascience.com/feed",
]

ARXIV_URL = "http://export.arxiv.org/rss/cs.LG"


def load_sent():
    try:
        with open("sent.json", "r") as f:
            return set(json.load(f))
    except:
        return set()
    
    
def save_sent(sent):
    with open("sent.json", "w") as f:
        json.dump(list(sent), f)
        
        
        
def fetch_rss(url):
    feed = feedparser.parse(url)
    items = []

    for entry in feed.entries[:5]:
        items.append({
            "title": entry.title,
            "link": entry.link
        })

    return items



def fetch_arxiv():
    feed = feedparser.parse(ARXIV_URL)
    items = []

    for entry in feed.entries[:5]:
        items.append({
            "title": entry.title,
            "link": entry.link
        })

    return items



#llM
KEYWORDS = {
    "llm": 5,
    "agent": 5,
    "rag": 4,
    "reasoning": 5,
    "mlo ps": 4,
    "fine-tune": 3,
    "transformer": 4,
    "dataset": 2
}

def score(title):
    title = title.lower()
    s = 0
    for k, v in KEYWORDS.items():
        if k in title:
            s += v
    return s


# Build digest
def build_digest(items):
    items = sorted(items, key=lambda x: x["score"], reverse=True)[:5]

    text = "🤖 AI & Data Science Daily Digest\n\n"

    for i, item in enumerate(items, 1):
        text += f"{i}. {item['title']}\n{item['link']}\n\n"

    return text     


#Send to telegram
def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHANNEL_ID,
        "text": text
    }

    response = requests.post(url, json=payload)

    print("Telegram status:", response.status_code)
    print("Telegram response:", response.text)

    response.raise_for_status()
 
 
#Main flow
def main():
    sent = load_sent()
    all_items = []

    for feed in RSS_FEEDS:
        for item in fetch_rss(feed):
            if item["link"] not in sent:
                item["score"] = score(item["title"])
                all_items.append(item)
                sent.add(item["link"])

    for item in fetch_arxiv():
        if item["link"] not in sent:
            item["score"] = score(item["title"])
            all_items.append(item)
            sent.add(item["link"])

    if not all_items:
        print("No new items found")
        return

    digest = build_digest(all_items)
    
    print("TOTAL ITEMS FOUND:", len(all_items))

    for i, item in enumerate(all_items[:10]):
        print(i, item["title"])

    print("Digest:\n", digest)

    send_to_telegram(digest)
    save_sent(sent)

if __name__ == "__main__":
    main()           
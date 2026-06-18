# AI Daily Digest Bot

[![Telegram Channel](https://img.shields.io/badge/Telegram-Join%20Channel-blue?logo=telegram)](https://t.me/+dwaC5Bdkz9NmMWRk)

An simple automated AI, Machine Learning, Data Science, and Research Paper digest that delivers the most relevant updates directly to a Telegram channel every day.

# AI Daily Digest Bot

An automated AI, Machine Learning, Data Science, and Research Paper digest that delivers the most relevant updates directly to a Telegram channel every day.

## Overview

AI Daily Digest Bot collects content from leading AI and Data Science sources, filters and ranks articles based on relevance, and publishes a curated daily briefing to Telegram.

The goal is to reduce information overload by surfacing only the most important developments in:

* Artificial Intelligence
* Machine Learning
* Data Science
* MLOps
* AI Agents
* Research Papers (arXiv)

The workflow runs automatically using GitHub Actions and requires no server infrastructure.

---

## Features

* Daily automated execution
* RSS feed aggregation
* arXiv paper monitoring
* Keyword-based relevance scoring
* Duplicate prevention
* Telegram channel delivery
* GitHub Actions scheduling
* Zero-cost deployment

---

## Data Sources

### AI & Machine Learning News

* Hugging Face Blog
* MarkTechPost
* Towards Data Science
* **(More being added)**

### Research Papers

* arXiv (cs.LG)

Additional sources can be added by updating the `RSS_FEEDS` list.

---

## Architecture

```text
GitHub Actions
      ↓
Fetch RSS Feeds
      ↓
Fetch arXiv Papers
      ↓
Rank Content
      ↓
Generate Digest
      ↓
Telegram Bot
      ↓
Telegram Channel
```

---

## Example Digest

```text
🤖 AI & Data Science Daily Digest

1. Agentic Resource Discovery: Let agents search
https://...

2. OpenAI Deployment Simulation
https://...

3. New AI Agent Framework Released
https://...
```

---

## Project Structure

```text
.
├── digest.py
├── sent.json
├── requirements.txt
└── .github
    └── workflows
        └── daily.yml
```

### Files

| File             | Purpose                         |
| ---------------- | ------------------------------- |
| digest.py        | Main application                |
| sent.json        | Stores previously sent articles |
| requirements.txt | Python dependencies             |
| daily.yml        | GitHub Actions workflow         |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/ai-daily-digest.git
cd ai-daily-digest
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Telegram Setup

### Create a Bot

1. Open Telegram
2. Search for `@BotFather`
3. Run:

```text
/newbot
```

4. Copy the generated bot token

### Create a Channel

1. Create a Telegram channel
2. Add the bot as an administrator
3. Grant permission to post messages

### Get Channel ID

Use:

```text
https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates
```

Locate the channel ID:

```json
{
  "chat": {
    "id": -1001234567890
  }
}
```

---

## GitHub Secrets

Add the following repository secrets:

| Secret              | Description         |
| ------------------- | ------------------- |
| TELEGRAM_BOT_TOKEN  | Telegram bot token  |
| TELEGRAM_CHANNEL_ID | Telegram channel ID |

Repository Settings → Secrets and Variables → Actions

---

## GitHub Actions

The workflow runs daily at:

```text
20:00 EAT (17:00 UTC)
```

Manual execution is also supported via:

```text
Actions → Daily AI Digest → Run Workflow
```

---

## Customization

### Add New RSS Sources

Update:

```python
RSS_FEEDS = [
    "...",
]
```

### Modify Ranking Logic

Update:

```python
KEYWORDS = {
    "agent": 5,
    "llm": 5,
    "rag": 4
}
```

### Change Number of Articles

Modify:

```python
items[:5]
```

to the desired number.

---

## Future Enhancements

* LLM-powered article summarization
* arXiv paper explanations
* Embedding-based ranking
* Topic clustering
* Multi-agent research workflow
* WhatsApp delivery
* Email digest support
* MLOps and Azure AI sections

---

## Tech Stack

* Python
* GitHub Actions
* Telegram Bot API
* RSS Feeds
* arXiv
* Requests
* Feedparser

---

## License

MIT License

---

## Author

Christopher Toromo

Data Scientist | Machine Learning Engineer

Building practical AI systems that turn information into actionable insights.

---
id: reddit-post-scraping-tool
name: Reddit Post Scraping Tool
description: Use when you have a Reddit `username`, subreddit, or keyword and want to bulk-collect matching posts — returns exported post data (author, text, timestamps) for offline analysis.
url: https://github.com/rly0nheart/reddit-post-scraping-tool
category: social-networks
path:
- social-networks
bestFor: Bulk-scraping Reddit posts by keyword, subreddit, or user for offline review and archiving.
selectorsIn:
- username
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free, open-source Python script. Uses Reddit's API, so you supply free Reddit API credentials.
opsec: passive
opsecNote: Reads public Reddit content via the API; users are not notified. Your Reddit API credentials/IP are visible to Reddit. Keep the account read-only — never comment/vote from it — to stay passive, and store scraped data securely as it may contain third parties' personal details.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Small open-source project (rly0nheart); it only collects public Reddit data, and every extracted post is verifiable against the live thread.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
relatedTools:
- reddit-persona
- rug
- reddit-user-analyser
aliases:
- rly0nheart/reddit-post-scraping-tool
- rpst
tags:
- reddit
- scraping
- python
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Reddit Post Scraping Tool

> A simple open-source Python scraper that pulls Reddit posts by keyword, subreddit, or user into a structured export for offline analysis and preservation.

## When to use
You want more than a live browse of a subject's Reddit activity — you need to *collect and preserve* it: all posts by a `username`, everything in a subreddit, or every post matching a keyword. Useful for building a timeline, keyword-mining a community for mentions of a person/place, or capturing content before it can be deleted. The structured output makes it easy to search offline for identifying details (locations, names, dates) scattered across many posts.

## How to use it (`bestInteractionPattern`: cli)
1. Register a free Reddit "script" app (reddit.com/prefs/apps) for API credentials, then clone `https://github.com/rly0nheart/reddit-post-scraping-tool`.
2. Install dependencies (Python) and configure your Reddit API client id/secret.
3. Run the scraper targeting a username, subreddit, and/or keyword, and set the number of posts to collect.
4. Review the export (post text, author, subreddit, timestamps) offline — grep for locations, names, timezones, and cross-post patterns.
5. Pivot: reused `username` → username-search tools; location/timezone hints → geolocation; for a per-user persona summary use `[[reddit-persona]]`.

## Inputs → Outputs
- **In:** `username` (also subreddit or keyword)
- **Out:** structured post export — `social-profile` (activity/interests), `geolocation` hints (locations/timezone inferred from content and timestamps)
- **Empty/negative result looks like:** an empty/tiny export — the user/subreddit has little public content, the account is suspended/deleted, or the keyword doesn't appear. Sparse output means little public data, not a failed scrape.

## Gotchas & OpSec
- Reddit's API only returns a bounded window of recent history; very old posts may be unreachable — note the coverage limit when concluding "nothing found."
- Human-in-the-loop: you must supply your own Reddit API key; respect API rate limits to avoid throttling.
- OpSec: **passive** if the account stays read-only; scraped data can contain third parties' personal info — handle and store it responsibly.

## Overlaps ("do both")
- Pairs with `[[reddit-persona]]` (summarizes a user into a persona) and `[[reddit-user-analyser]]` — scrape for the raw corpus, then use those to summarize; cross-checking catches history one method windows out.

## Trust & verifiability
`trust: community` — a small open-source scraper that only surfaces public Reddit data; every collected post links back to a live thread you can verify directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reddit-post-scraping-tool |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |

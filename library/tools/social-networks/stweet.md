---
id: stweet
name: Stweet
description: Use when you have a `username`, hashtag, or keyword and want to bulk-scrape historical tweets without an API key — returns tweet `social-profile` data (text, dates, engagement).
url: https://github.com/markowanga/stweet
category: social-networks
path:
- social-networks
bestFor: Programmatic bulk scraping of tweets by user/hashtag/keyword from Python with no login or API key.
selectorsIn:
- username
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free, open-source (Python) on GitHub; no API key or paid tier.
opsec: passive
opsecNote: Passive toward the target — it reads Twitter/X's public web endpoints; it does not touch the user's account or notify them. It scrapes anonymously (no login), which is good for your footprint, but scraping may breach X's ToS and endpoints break often — run from research infrastructure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source library (markowanga, ~270+ stars); technique is sound but fragile against X's frequent API changes and only lightly maintained — verify it still runs before relying on it.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- stweet
tags:
- Social Media
- Twitter
- python
- scraper
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Stweet

> A Python library that scrapes tweets and users by handle, hashtag, or keyword — no login, no API key.

## When to use
You want to pull a subject's tweet history (or all tweets for a hashtag/keyword over a time window) programmatically, without a paid X API — e.g. to reconstruct a timeline, find location/time patterns, or archive posts before deletion. Best when you need volume or automation rather than a single manual look.

## How to use it (`bestInteractionPattern`: cli)
1. `pip install stweet` (Python 3.8+).
2. In a script, build a search runner: by username, by phrase/hashtag, or by tweet IDs. For date ranges, split into smaller windows (X blocks wide timestamp ranges).
3. Run it and collect the output (JSON/CSV) of tweets and user data.
4. Read the output: tweet text, timestamps, engagement, and user metadata. Pivot: extract mentioned handles, links, geo hints, and images for face/geolocation follow-up.

## Inputs → Outputs
- **In:** a `username`, hashtag, or keyword (+ optional date window)
- **Out:** tweets and user `social-profile` data (text, dates, counts, links)
- **Empty/negative result looks like:** empty results are often rate-limiting or a broken endpoint after an X change, not a truly empty account — retry with smaller windows / later; confirm the library version still works.

## Gotchas & OpSec
- **Fragile:** X frequently changes its unofficial API; expect breakage and check for a maintained fork if it fails.
- Scraping may violate X's ToS; use judiciously and from research infrastructure.
- Human-in-the-loop: none. OpSec: passive (anonymous scraping).

## Overlaps ("do both")
- Do both with a deleted-tweet/archive tool — stweet pulls what's live; archives recover what's gone. Together they rebuild a fuller timeline.

## Trust & verifiability
`trust: community` — well-used open-source tool, but unmaintained enough that you should confirm it runs today; every scraped tweet is checkable against the live/archived post.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | stweet |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |

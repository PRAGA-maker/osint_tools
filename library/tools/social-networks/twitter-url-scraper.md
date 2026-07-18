---
id: twitter-url-scraper
name: Twitter URL Scraper (Apify)
description: Use when you have a Twitter/X conversation or profile URL and want it captured as data — returns tweet text, usernames, profile pictures and replies, exported to CSV/JSON/XML.
url: https://apify.com/zuzka/twitter-url-scraper
category: social-networks
path:
- social-networks
bestFor: Capturing the text, authors and profile pictures of a Twitter/X thread or page as structured data.
selectorsIn:
- social-profile
- username
selectorsOut:
- username
- image
- social-profile
status: degraded
pricing: freemium
costNote: Runs on the Apify platform, which gives free monthly usage credits; heavy runs consume paid compute/proxy units. An Apify account is required.
opsec: passive
opsecNote: Scraping reads public tweets via the Apify cloud, not from your own IP, so the target is unlikely to see you. You must hold an Apify account — register it under a sock-puppet identity, not your real one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: api
trust: unverified
trustNote: A community-published Apify actor (not an official Apify or X product); Twitter/X's frequent anti-scraping changes mean any given actor can break, so verify it still runs before relying on it.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- twitter-scraper
- reddit-scraper
- instagram-scraper
- facebook-latest-posts-scraper
- youtube-scraper
aliases:
- Apify Twitter URL Scraper
- zuzka twitter-url-scraper
tags:
- Social Media
- Twitter
- apify
- scraper
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Twitter URL Scraper (Apify)

> An Apify actor that turns a Twitter/X thread or profile URL into structured data — tweet text, authors, profile pictures and replies — exportable to CSV/JSON/XML for offline analysis.

## When to use
You have a Twitter/X conversation or profile URL tied to a subject and want a durable, structured capture rather than fragile screenshots — the full text of a thread and its replies, the usernames involved, and their profile pictures (`image`). Useful for preserving a conversation before it's deleted and for turning replies into a list of `associate` handles to pivot on.

## How to use it (`bestInteractionPattern`: api)
1. Create an Apify account (sock puppet) and open the actor at https://apify.com/zuzka/twitter-url-scraper.
2. Provide the target Twitter/X URL(s) as input and run the actor from the console or via the Apify API.
3. Download the dataset (CSV/JSON/XML): tweet text, author usernames, profile-picture URLs, and reply threads.
4. Pivot: reply authors become new `username`/`social-profile` leads; profile-picture URLs feed reverse-image/face tools; the captured text preserves a timeline.

## Inputs → Outputs
- **In:** a Twitter/X conversation or profile `social-profile` URL (or `username`)
- **Out:** `username`s, tweet text, `image` (profile pictures), and reply `social-profile`s as structured data
- **Empty/negative result looks like:** an empty dataset or a run error — X's anti-scraping defenses or a login wall blocked it; a null run usually means the actor is broken/rate-limited, not that the page is empty.

## Gotchas & OpSec
- Human-in-the-loop: an Apify account/login is required; runs may need proxy configuration.
- **Status: degraded** — X's aggressive anti-scraping and API lockdown break community actors frequently; test a small run and, if it fails, switch to a maintained alternative like `[[twitter-scraper]]`.
- OpSec: the scrape runs from Apify's cloud, keeping your IP off X; still use a sock-puppet Apify account.

## Overlaps ("do both")
- Pairs with `[[twitter-scraper]]` and the other Apify social scrapers — if this URL-focused actor breaks, a broader maintained Twitter scraper may still pull the same thread; keep a fallback ready given X's volatility.

## Trust & verifiability
`trust: unverified` — a third-party community actor subject to X's changing defenses; confirm it still returns data on a known public thread before trusting a run, and spot-check the output against the live page while it still exists.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitter-url-scraper |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, username → username, image, social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | api |
| opsec | passive |
| human-in-loop | yes (account-login) |

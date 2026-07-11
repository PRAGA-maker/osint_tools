---
id: universal-reddit-scraper-urs
name: Universal Reddit Scraper (URS)
description: Use when you have a Reddit `username` (or subreddit) and want their full post/comment history exported for analysis — returns activity that leaks location, routine, and associates.
url: https://github.com/JosephLai241/URS
category: social-networks
path:
- social-networks
bestFor: Exporting a Reddit user's complete submission and comment history to mine for location, schedule, and relationship signals.
selectorsIn:
- username
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free and open-source (Python); requires your own free Reddit API credentials (PRAW client id/secret).
opsec: passive
opsecNote: Reads via Reddit's official API using your API key — it does not interact with the target (no votes, no messages) and the user is not notified. Your API app/IP is visible to Reddit, not to the subject. Use a dedicated Reddit API app for investigative work.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Well-known open-source Reddit scraper (JosephLai241/URS); code is inspectable and it uses the sanctioned API, so data fidelity is high subject to Reddit API limits.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
invitationOnly: false
deprecated: false
aliases:
- URS
tags:
- reddit
- scraper
- python
source: gh-topic-osint-resources
lastVerified: '2026-07-11'
enrichment: full
---

# Universal Reddit Scraper (URS)

> A Python CLI that pulls a Reddit user's (or subreddit's, or thread's) full history through the official API and writes it to JSON/CSV — so you can analyze months of posts for the details a person leaks without realizing.

## When to use
You have a Reddit `username` and want more than the last few posts the site shows — you want the whole corpus to comb for location tells ("my local X", weather, sports teams), daily rhythm (post timestamps → time zone / work schedule), interests, and the other users they interact with (`associate`s). Reddit histories are unusually revealing; exporting and analyzing them in bulk is far more productive than scrolling the profile. Reach for it when a subject has a substantive Reddit presence.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/JosephLai241/URS`, install dependencies, and create a Reddit API app to get a client id/secret (free).
2. Configure credentials, then run URS in redditor mode against the `username` (it also has subreddit and comments/submissions modes).
3. Choose the export (JSON/CSV) and depth.
4. Analyze the output: cluster post times for a time-zone estimate, grep for place/routine mentions, and list frequently-engaged users and subreddits.
5. Pivot: subreddits reveal communities (see `[[subreddits]]`); recurring co-posters are `associate` leads; location mentions feed geolocation.

## Inputs → Outputs
- **In:** `username` (also subreddit / thread targets)
- **Out:** `social-profile` (full activity export), `geolocation` (from post content/timing), plus interests and associates
- **Empty/negative result looks like:** an empty or tiny export — a new, deleted, suspended, or shadow-restricted account, or an API-limit truncation. Not proof of no history; confirm the account exists and re-run within rate limits.

## Gotchas & OpSec
- Human-in-the-loop: you must obtain and configure **Reddit API credentials** (api-key); setup is technical.
- Deleted/removed content won't be retrieved via the API — pair with Pushshift-style archives for gone content where available.
- OpSec: passive — official API reads only, target not notified; use a dedicated API app.

## Overlaps ("do both")
- Pairs with `[[subreddits]]` (which communities to look in) and Reddit archive/search tools — URS exports what's live; archives recover what was deleted. Analyze both together.

## Trust & verifiability
`trust: community` — a mature, inspectable open-source tool using Reddit's sanctioned API; data is faithful to what the API returns, bounded by rate limits and content deletion.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | universal-reddit-scraper-urs |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |

---
id: snscrape
name: SNScrape
description: Use when you have a `username`, hashtag, or keyword and want to bulk-collect a social account's public posts without an API key — returns post history and profile data (social-profile) as JSON/CSV.
url: https://github.com/JustAnotherArchivist/snscrape
category: social-networks
path:
- social-networks
bestFor: Scraping a public account's post history across Twitter/X, Telegram, Mastodon, VK, Reddit and more from the command line.
selectorsIn:
- username
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free and open-source (Python). No API keys or paid tier; you install it locally and run it yourself.
opsec: passive
opsecNote: snscrape fetches public pages/endpoints directly from the target platform, so those platforms see your requests (IP, rate pattern) — not the target user. Run behind a VPN and rate-limit to avoid IP blocks. No login is used, so no sock-puppet account is exposed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A well-known open-source scraper (JustAnotherArchivist) widely used in OSINT; output is raw platform data, but individual scrapers break as sites change their front-ends — verify a live sample.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- snscrape
- social network scraper
tags:
- Social Media
- Universal
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# SNScrape

> A command-line scraper for social networks — pull a public account's full post history (or a hashtag/keyword search) into JSON/CSV without touching any official API.

## When to use
You have a `username` (or a hashtag/keyword/search term) on a supported platform and want the account's complete public post history for timeline reconstruction, geolocation from post content, associate mapping, or pattern-of-life analysis. Because it bypasses API rate/pagination limits, snscrape can retrieve far more than a manual scroll — every public tweet/toot/message a profile has posted, exportable for analysis.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install snscrape` (Python 3.8+; use the dev build from GitHub for the latest fixes).
2. Scrape a user's posts, e.g. `snscrape --jsonl twitter-user TARGET > out.jsonl` or `snscrape telegram-channel NAME`. Supported modules include twitter, telegram, mastodon, vkontakte, reddit, and others.
3. Add `--max-results N` to cap volume, and `--jsonl` for structured output you can load into a script/spreadsheet.
4. Parse the output for timestamps, geotags, mentioned handles, and links.
5. Pivot: mentioned `username`s → cross-platform username tools; geotags/photos → geolocation and reverse-image tools; linked sites → domain tools.

## Inputs → Outputs
- **In:** `username`, hashtag, or keyword on a supported platform
- **Out:** the account's public posts and profile metadata (`social-profile`) as JSONL/CSV — text, timestamps, links, mentions, sometimes geotags
- **Empty/negative result looks like:** an error or zero rows — usually the platform's front-end changed and that specific scraper module broke, or the account is private/suspended. Update to the latest GitHub build and retry.

## Gotchas & OpSec
- **Twitter/X is unreliable:** after X's 2023 access clampdown the twitter module frequently breaks; treat it as degraded and verify on each run. Other modules (Telegram, Mastodon, VK, Reddit) are more dependable.
- Only public content is reachable — no logins, so private/protected accounts return nothing.
- Aggressive scraping gets your IP rate-limited or blocked; throttle and use a VPN.
- OpSec: **passive** toward the target (no interaction with the account), but the platform logs your scraping traffic.

## Overlaps ("do both")
- Complements manual profile review and platform-specific tools: use those to confirm the account, then snscrape to bulk-export its history for analysis.

## Trust & verifiability
`trust: community` — a respected open-source project returning raw platform data, so results are authentic when the scraper works; but modules degrade as sites change, so always sanity-check a few records against the live profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | snscrape |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |

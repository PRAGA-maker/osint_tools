---
id: twint
name: Twint
description: Use when you want historical Twitter/X data (tweets by handle, keyword, hashtag, date) without API keys — but note the tool is DEPRECATED and broken by X's changes; returns `social-profile` tweet collections when run against old data.
url: https://github.com/twintproject/twint
category: social-networks
path:
- social-networks
- twitter
- analytics
bestFor: Historically, bulk-scraping tweets and user metadata by handle/keyword/hashtag/date from the CLI with no API key — now largely non-functional after X locked down access.
selectorsIn:
- username
selectorsOut:
- social-profile
- metadata-exif
status: down
pricing: free
costNote: Free and open-source (Python CLI). Value today is minimal — the project is unmaintained and broken by X's anti-scraping and login-wall changes.
opsec: active
opsecNote: When it did work it scraped X directly from your IP, which X can detect and block. If you attempt it, run behind a VPN/puppet. The target account is not notified, but X sees the automated access.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: A once-popular open-source Twitter scraper (twintproject/twint), now archived/unmaintained and non-functional following Twitter/X's 2023 API and login-wall crackdown. Catalogued so agents don't waste time on it.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
deprecated: true
aliases:
- twintproject
- Twitter Intelligence Tool
tags:
- twitter
- x
- scraper
- deprecated
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Twint

> Once the go-to no-API Twitter scraper — now deprecated and broken by X's lockdown, catalogued mainly so you reach for a working alternative instead.

## When to use
Historically you'd use Twint to pull a user's full tweet history, or all tweets matching a keyword/hashtag/date range, from the command line without a Twitter API key. **Today, treat it as non-functional**: Twitter/X's 2023 API pricing changes and login wall broke the scraping paths Twint relied on, and the project is unmaintained. Reach for it only against previously-collected data, or skip straight to a current X-OSINT method.

## How to use it (`bestInteractionPattern`: cli)
1. (If attempting at all) `pip install twint` or install from the GitHub repo.
2. Run e.g. `twint -u <username>` (tweets by user), `twint -s "<keyword>"`, or with `--since/--until` for date ranges; export with `--csv/--json`.
3. Expect it to fail, return nothing, or error out on auth/rate-limit — that is the current normal state.
4. Do not burn time cycling flags; pivot to a maintained approach for live X data.
5. Pivot: for live X data use a puppet X account + native search, or archive tools (`[[sotwe-com]]`, Wayback Machine); for historical bulk data, other archives.

## Inputs → Outputs
- **In:** `username`, keyword, or hashtag (+ date filters)
- **Out:** `social-profile` (tweet collections), `metadata-exif` (timestamps, counts) — only if it runs, which it generally no longer does
- **Empty/negative result looks like:** immediate errors, empty output, or auth failures. This reflects X blocking the tool, not the absence of tweets — verify on X directly.

## Gotchas & OpSec
- **Deprecated:** the single most important fact — it's broken and unmaintained. Have a working alternative ready.
- Forks claiming to fix it are hit-or-miss and also fragile against X's changes.
- OpSec: **active** — direct scraping X sees and blocks; VPN/puppet if you try.

## Overlaps ("do both")
- Superseded in practice by puppet-account native X search, `[[sotwe-com]]`-style viewers, and web archives — use those for live/recent tweets.

## Trust & verifiability
`trust: unverified` — a legitimate but defunct tool; any data it returns comes from X and should be verified against the live platform. Mostly of historical interest now.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twint |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |

---
id: sotwe-com
name: Sotwe
description: Use when you have a Twitter/X `username` and want to read their tweets without an X login — returns `social-profile` timeline content, though access is frequently blocked.
url: https://www.sotwe.com/
category: social-networks
path:
- social-networks
bestFor: Viewing a public Twitter/X account's tweets and media without logging into X — a Nitter-style front-end/archive, when it isn't rate-limited or blocked.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free, no account. But it depends on scraping X, which X actively fights — availability is intermittent and it often shows CAPTCHAs, partial timelines, or blocks.
opsec: passive
opsecNote: You read via Sotwe's servers instead of your own X session, so you don't touch the target's account or reveal your identity to X. Sotwe (a third party) can log your queries — use a puppet IP for sensitive work.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party X viewer/archive whose data comes from scraping X. Coverage is partial and often stale or truncated because X throttles such tools; treat what you see as a possibly-incomplete snapshot.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- sotwe.com
- Nitter alternative
tags:
- xtwitter
- twitter
- social-networks
- alternative-frontend
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Sotwe

> A Nitter-style way to read a Twitter/X account without logging in — handy when it works, but X's crackdown makes it flaky and often incomplete.

## When to use
You have a Twitter/X `username` and want to view their public tweets/media **without** an X account (X now walls most content behind login). Reach for Sotwe as a no-login reading path — to browse a timeline, grab media, or check an account while staying logged out. Because X aggressively throttles scrapers, treat it as one of several fallbacks, not a reliable primary.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.sotwe.com/ and enter the `username` (or try `sotwe.com/<username>`).
2. If a CAPTCHA or block appears, solve it or retry later — availability is intermittent.
3. Read the rendered timeline: tweets, media, and profile info (`social-profile`), without an X login.
4. Cross-check completeness — the timeline may be truncated or stale versus the live account.
5. Pivot: media → reverse-image/EXIF; content → geolocation/timeline; reused handle → cross-platform enumeration.

## Inputs → Outputs
- **In:** `username` (X handle), or `name` to find one
- **Out:** `social-profile` (tweets, media, profile) — read-only, possibly partial
- **Empty/negative result looks like:** a CAPTCHA wall, an error, or a blank/partial timeline. This usually means X blocked the scrape, not that the account is empty — verify against the live X profile or another viewer.

## Gotchas & OpSec
- **Fragile by nature:** X fights scraping, so Sotwe (like all Nitter-style tools) breaks, throttles, and truncates unpredictably. Don't rely on a single check.
- Data may lag or omit recent tweets, replies, or protected content.
- OpSec: **passive** — you read via Sotwe, not your own X session; a third party sees your queries.

## Overlaps ("do both")
- Pairs with other X front-ends/archives (Nitter instances, `[[twitter-lolarchiver-com]]`-style archivers) and, for deleted content, the Wayback Machine — run several since each fails differently.

## Trust & verifiability
`trust: unverified` — a third-party scraper-based viewer with partial, sometimes stale coverage. Confirm anything important against the live X account (via a puppet login) or an independent archive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sotwe-com |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |

---
id: tgramsearch
name: TgramSearch
description: Use when you have a keyword, topic, or `username` and want to find related Telegram channels — returns a catalogue of channels with names, descriptions, and join links as social-profile leads.
url: https://tgramsearch.com/
category: messaging
path:
- messaging
bestFor: Searching a large indexed catalogue of public Telegram channels by keyword or category.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free; no account required.
opsec: passive
opsecNote: You search a third-party index of public channels, not Telegram itself, so no channel admin is notified of your search. The index operator sees your queries/IP; use a sock-puppet browser. Actually joining a discovered channel in Telegram is a separate, more active step done from an investigative account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent Telegram channel-directory (Russian-language interface) indexing 800k+ channels from open sources. Coverage is broad but incomplete and unranked by authority.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- telegago
- tgstat
aliases:
- Tgram Search
- tgramsearch.com
tags:
- telegram
- channel-search
source: awesome-osint
lastVerified: '2026-07-14'
enrichment: full
---

# TgramSearch

> A search engine over 800,000+ public Telegram channels: find channels by keyword, topic, or name that Telegram's own weak search misses.

## When to use
You need to discover public Telegram channels around a topic, place, event, or name — Telegram's native search is deliberately limited, so an external index surfaces far more. Useful for finding community/interest channels a subject may frequent, local or event channels tied to a `geolocation`, or channels matching a `username`/brand you're tracking.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tgramsearch.com/ (interface is in Russian; a browser translator helps).
2. Enter a 1–3 word query, or browse the 100+ categories.
3. Read results: channel name, description, subscriber hint, avatar, and join link.
4. Pivot: open a promising channel in Telegram from an investigative account to read/monitor it; cross-check with other Telegram indexes like `[[telegago]]` and `[[tgstat]]`, which surface different channels and add stats.

## Inputs → Outputs
- **In:** keyword/topic or `username`
- **Out:** `social-profile` (matching public Telegram channels + join links)
- **Empty/negative result looks like:** no results — the term isn't indexed, the channel is private/unlisted, or it's newer than the index; a miss here doesn't mean no such channel exists.

## Gotchas & OpSec
- Human-in-the-loop: none for searching; joining a channel is a separate active step.
- OpSec: **passive** — searching the index doesn't touch Telegram or notify admins; sock-puppet the index query anyway.
- Index is incomplete and not ranked by trust — corroborate any channel's relevance before acting.

## Overlaps ("do both")
- Pairs with `[[telegago]]` (Google-dork-based Telegram search) and `[[tgstat]]` (channel statistics) — run several, since each Telegram index has different coverage.

## Trust & verifiability
`trust: community` — an independent directory built from open sources. Results are real channels but the index is partial and unvetted; verify each channel directly in Telegram.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tgramsearch |
| category | messaging |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

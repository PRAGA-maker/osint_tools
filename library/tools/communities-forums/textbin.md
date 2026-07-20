---
id: textbin
name: TextBin
description: Use when you have a `username`, `email`, or leaked keyword and want to check a public pastebin for dumped text, credentials, or contact fragments — returns paste content that may contain `email`, `password`, `username`.
url: https://textbin.net/
category: communities-forums
path:
- communities-forums
bestFor: Checking a lightweight public pastebin for dumped text, credential lists, or contact fragments tied to a selector.
selectorsIn:
- username
- email
selectorsOut:
- email
- password
- username
status: degraded
pricing: free
costNote: Free to read and post pastes; no account required.
opsec: passive
opsecNote: Reading existing pastes is passive and leaks nothing. Never paste any of the subject's own data here — this is a public bin and anything you post becomes searchable and attributable. Use a sock puppet if you must interact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A small, community-run pastebin clone; content is user-submitted and unvetted, so any "hit" is a raw lead to corroborate, not a fact. Site returned intermittent 503s at last check.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- textbin.net
tags:
- pastebins
source: awesome-osint
lastVerified: '2026-07-20'
enrichment: full
---

# TextBin

> A small public pastebin — one of many bins to sweep when hunting for a subject's data in dumped/leaked text.

## When to use
You have a `username`, `email`, or a distinctive keyword and you're doing a pastebin sweep for leaked or dumped material — credential lists, doxes, contact fragments, or reused handles. TextBin is a minor Pastebin.com clone; it belongs in a *breadth* pass across many pastebins (via a paste-search aggregator) rather than as a standalone destination, because it has no strong native full-text search and its public feed is thin.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://textbin.net/ in a clean/sock-puppet browser (the site has been returning intermittent 503s — retry or treat as down if it doesn't load).
2. Browse the recent/public pastes list if one is exposed; there is no robust native search, so most discovery comes from indexed pastes.
3. Better: pivot to Google with `site:textbin.net "<selector>"` to full-text search this bin via the search engine's index.
4. Read any matching paste for `email`, `password`, `username`, phone fragments, or names.
5. Pivot: feed recovered credentials/handles into breach-check and username-enumeration tools; corroborate before trusting.

## Inputs → Outputs
- **In:** `username`, `email`, or keyword (via `site:` dork)
- **Out:** raw paste text possibly containing `email`, `password`, `username`, other contact fragments
- **Empty/negative result looks like:** no indexed paste matches, or the site 503s — absence here means nothing; the same data may sit on any of a dozen other bins.

## Gotchas & OpSec
- Site reliability is shaky (503s observed); do not treat unavailability as a cleared lead.
- No trustworthy native search — rely on `site:textbin.net` dorking.
- OpSec: reading is passive; **never** post the subject's data here. Anything you paste is public and attributable.

## Overlaps ("do both")
- Pairs with broader paste-search tools and other bins — run the same selector across many pastebins, since any single bin only holds a slice.

## Trust & verifiability
`trust: community` — user-submitted, unvetted content on a small third-party bin. Any hit is an unverified lead; corroborate identity and recency before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | textbin |
| category | communities-forums |
| selectorsIn → selectorsOut | username, email → email, password, username |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

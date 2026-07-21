---
id: dpaste
name: dpaste
description: Use when you have a `username`, `email`, `domain` or leak keyword and want to check a public pastebin for dumped credentials, contact lists or config that mention it — returns exposed text snippets and associated selectors.
url: https://dpaste.com
category: communities-forums
path:
- communities-forums
bestFor: Checking a public paste service for leaked data, dumps or shared snippets mentioning a target selector.
selectorsIn:
- username
- email
- domain
selectorsOut:
- email
- password
- ip-address
status: live
pricing: free
costNote: Free paste service with a public feed and API; no account required to read public pastes.
opsec: passive
opsecNote: Reading public pastes and the public feed is passive and invisible to any target. Do NOT paste your own investigative notes or target data into it — anything you submit becomes publicly retrievable. Treat found credentials as evidence to report, never to use.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: dpaste is a long-running open pastebin (Django-based); it hosts user-submitted content, so anything found is unvetted and possibly stale, spoofed, or planted.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- dpaste.com
- dpaste.org
tags:
- pastebins
- leaks
- breach-data
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# dpaste

> A public code/text pastebin — searchable in aggregate as one of the many paste sites where credential dumps, contact lists and leaked config get shared.

## When to use
You are hunting for leaked or shared data tied to a subject — a `username`, `email`, `domain`, or breach keyword — and want to check whether it appears in a public paste. Paste sites are a common drop point for credential dumps, doxes, database fragments, and shared contact lists, so a hit can surface passwords, secondary emails, IPs, or associates that no formal record holds.

## How to use it (`bestInteractionPattern`: web-manual)
1. Browse dpaste's public feed at https://dpaste.com/public/ to see recently shared items.
2. dpaste has no strong internal full-text search, so pivot through a search engine: `site:dpaste.com "<selector>"` (email, username, domain) on Google/Bing, and check paste-aggregators (e.g. a Pastebin-scraper index) that ingest dpaste.
3. Open any matching paste and read the raw content for exposed `email`, `password`, `ip-address`, or contact data.
4. Screenshot/preserve the paste (they expire or get deleted) and record its URL and timestamp.
5. Pivot: leaked credentials → confirm account existence elsewhere; leaked contacts/associates → people-search; leaked domains/IPs → infrastructure tools.

## Inputs → Outputs
- **In:** `username`, `email`, `domain`, or breach keyword
- **Out:** exposed `email`, `password`, `ip-address`, contact lists, associate names
- **Empty/negative result looks like:** no paste indexed for your term — absence is weak evidence; pastes expire and aren't fully indexed, so re-check aggregators and other paste sites before concluding nothing exists.

## Gotchas & OpSec
- No reliable native search: reach dpaste content via external search-engine dorks and paste-aggregators, not an on-site query.
- Pastes are ephemeral: they can be set to expire or be removed — capture evidence immediately.
- Content is unvetted: dumps can be fabricated, recycled from old breaches, or planted — corroborate before trusting.
- OpSec: reading is passive. Never submit your own target data to the site; anything pasted is public. Do not reuse found passwords — that crosses into unauthorized access.

## Overlaps ("do both")
- Pairs with other pastebin and breach-search tools — dpaste is one of many paste hosts, so run the same selector across a paste-aggregator and breach databases to catch dumps that landed elsewhere.

## Trust & verifiability
`trust: community` — an established but open, user-submitted paste service; treat any find as an unverified lead and confirm the data against an independent source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dpaste |
| category | communities-forums |
| selectorsIn → selectorsOut | username, email, domain → email, password, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

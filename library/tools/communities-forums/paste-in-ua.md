---
id: paste-in-ua
name: paste.in.ua
description: Use when you have a `username`, `email` or `domain` and want to check a Ukrainian/RU-language pastebin for dumped credentials, leaked lists or shared config mentioning it — returns exposed text snippets and associated selectors.
url: https://paste.in.ua/
category: communities-forums
path:
- communities-forums
bestFor: Checking a Ukrainian-region paste service for leaked data or dumps tied to a target selector.
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
costNote: Free public paste service; no account required to read public pastes.
opsec: passive
opsecNote: Reading public pastes is passive and invisible to any target. Never paste your own case notes or target data into it — submissions become public. Treat any found credentials as evidence, never for access.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An open, user-submitted pastebin in the Ukrainian/RU-language sphere; content is unvetted and may be stale, recycled, or fabricated.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- paste.in.ua
tags:
- pastebins
- leaks
- breach-data
- ukraine
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# paste.in.ua

> A Ukrainian-region public pastebin — one of the many paste hosts where credential dumps, leaked lists and shared config surface, of particular interest for EE/CIS-linked subjects.

## When to use
You are hunting for leaked or shared data tied to a subject — a `username`, `email`, or `domain` — and want to check a regional paste host that Western tools often miss. Paste sites are common drop points for dumps and doxes; a hit can expose passwords, secondary emails, IPs, or contacts. This one is worth including when the subject has a Ukrainian/Russian-language footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Browse the site's recent/public pastes at https://paste.in.ua/.
2. Because native full-text search is limited, pivot through a search engine: `site:paste.in.ua "<selector>"` (email, username, domain), and check paste-aggregators that ingest it.
3. Open any matching paste and read the raw content for exposed `email`, `password`, `ip-address`, or contact lists.
4. Preserve the paste immediately (URL, timestamp, screenshot) — pastes expire or get removed.
5. Pivot: leaked credentials → confirm account existence elsewhere; leaked contacts → people-search; domains/IPs → infrastructure tools.

## Inputs → Outputs
- **In:** `username`, `email`, or `domain`
- **Out:** exposed `email`, `password`, `ip-address`, contact/associate data
- **Empty/negative result looks like:** no indexed paste for your term — weak evidence, since pastes expire and aren't fully indexed; re-check aggregators and other paste sites.

## Gotchas & OpSec
- Regional/RU-language: best value for EE/CIS-linked subjects; content may be non-English.
- Ephemeral and unvetted: capture evidence at once, and corroborate before trusting — dumps can be fabricated or recycled from old breaches.
- OpSec: reading is passive; never submit target data. Do not reuse found passwords — that would be unauthorized access.

## Overlaps ("do both")
- Pairs with other pastebins ([[dpaste]]) and breach-search tools — run the same selector across multiple paste hosts and breach databases to catch dumps landing elsewhere.

## Trust & verifiability
`trust: community` — an open, user-submitted paste host; every find is an unverified lead, to be confirmed against an independent source before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | paste-in-ua |
| category | communities-forums |
| selectorsIn → selectorsOut | username, email, domain → email, password, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

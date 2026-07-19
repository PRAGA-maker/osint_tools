---
id: tutpaste
name: TutPaste
description: Use when you have a `username`/`email` and want to check a pastebin for leaked text, dumps or code tied to it — returns public paste content (`document-id`) that may expose credentials or contact data.
url: https://tutpaste.com/
category: communities-forums
path:
- communities-forums
bestFor: Checking whether a subject's data or handle appears in a public paste on this pastebin.
selectorsIn:
- username
- email
selectorsOut:
- document-id
- email
status: live
pricing: free
costNote: Free to read and to create pastes; no account required. Premium tiers add longer expiry but nothing needed for OSINT reading.
opsec: passive
opsecNote: Reading a public paste is passive and the poster is not notified. There is no site-wide full-text search, so you typically arrive via a Google dork or a direct paste URL — do that from a sock-puppet browser. Never re-paste sensitive victim data you find; treat leaked credentials as read-only evidence.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A generic public pastebin (text/code/images, custom expiry); content is user-submitted and unverified, so anything found needs independent corroboration.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- TutPaste pastebin
tags:
- pastebins
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# TutPaste

> A public pastebin for text, code and images — an OSINT surface where leaked dumps, credentials, and handle-tagged notes sometimes surface.

## When to use
You have a `username`, `email`, or `name` and want to see whether it appears in a public paste — credential dumps, config leaks, chat logs, or a subject's own posted snippets. Pastebins are a classic breach/leak surface; TutPaste is one more to sweep when running a paste-site search.

## How to use it (`bestInteractionPattern`: web-manual)
1. TutPaste has no reliable site-wide search box, so query it from a search engine: `site:tutpaste.com "<selector>"` (email, username, or a distinctive string).
2. Alternatively, if you already hold a paste URL (e.g. `tutpaste.com/NNNNN-title/`), open it directly.
3. Read the paste content; note the paste's age and any custom expiry (pastes can be set to expire from 10 minutes to a month, so time-sensitive dumps vanish).
4. Screenshot/preserve anything relevant via [[wayback-machine]] before it expires.
5. Pivot: exposed `email`, `password`, `phone`, or `crypto-wallet` strings feed breach-lookup and account-existence checks.

## Inputs → Outputs
- **In:** `username` / `email` / distinctive string (via search-engine dork)
- **Out:** public paste content — a `document-id` that may contain `email`, credentials, or contact data
- **Empty/negative result looks like:** no indexed pastes match — that's expected for most subjects; absence here says nothing, so sweep other pastebins too.

## Gotchas & OpSec
- No native search means Google/Bing coverage is your real index; freshly posted or noindex'd pastes won't show until crawled (or ever).
- Pastes expire — capture immediately; don't rely on the link persisting.
- OpSec: passive; the poster isn't alerted. Do not repost or redistribute leaked victim data — view it as evidence only, and mind the legal line on handling stolen credentials.

## Overlaps ("do both")
- Pairs with other pastebin sweeps and dedicated paste-monitoring/breach tools — run the same dork across multiple paste hosts, because any single pastebin indexes only its own content.

## Trust & verifiability
`trust: community` — user-submitted content on a generic pastebin; treat every find as an unverified lead and corroborate the underlying data before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tutpaste |
| category | communities-forums |
| selectorsIn → selectorsOut | username, email → document-id, email |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

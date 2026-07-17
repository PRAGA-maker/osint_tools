---
id: pastery
name: Pastery
description: Use when you have a Pastery paste URL/ID or are dorking for leaked text — returns the pasted content; a paste host where dumps and notes may be shared.
url: https://www.pastery.net/
category: communities-forums
path:
- communities-forums
bestFor: Reading a Pastery paste you've been pointed to, and treating it as a paste host where leaked data or notes may surface.
selectorsIn:
- username
selectorsOut:
- email
- password
status: live
pricing: free
costNote: Free pastebin with syntax highlighting, expiry options, and an API; no account needed to create or view a paste.
opsec: passive
opsecNote: Viewing a paste by its link is passive and anonymous; the poster isn't notified. No public paste index, so access is via a known URL or a search-engine hit. Don't paste your own case data into it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established small pastebin; content is arbitrary user-submitted text with no verification.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- pastebin
- katbin
aliases:
- pastery.net
tags:
- pastebins
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# Pastery

> A clean pastebin with syntax highlighting and an API — an OSINT-relevant paste host where leaked credentials, dox, or notes may appear (found via links or dorks, not an on-site search).

## When to use
You're pointed to a `pastery.net` paste, or you're sweeping paste sites for leaks tied to a subject (an `email`, `username`, or dump). Like most paste hosts, Pastery has no public browse/search — you reach a paste by its URL or via a search engine that indexed it. Use it to read a referenced paste and to include `pastery.net` in leak-hunting dorks.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open a known paste directly by its URL (e.g. `https://www.pastery.net/<id>/`).
2. To find relevant pastes, dork a search engine: `site:pastery.net "target@email.com"` or a username.
3. Read the content (code, logs, lists) — Pastery highlights 200+ formats, which helps parse structured dumps.
4. Extract selectors: emails, usernames, passwords, hosts.
5. Pivot: leaked `email`/`password` → breach-check/account tools; hosts/usernames → cross-platform search. Never reuse a credential.

## Inputs → Outputs
- **In:** a Pastery paste URL/ID, or a dork term (`username`, `email`)
- **Out:** raw pasted text → possible `email`/`password`/host leaks
- **Empty/negative result looks like:** no indexed pastes for your dork / an expired paste link — Pastery pastes can auto-expire and are mostly unlisted, so absence here is not meaningful.

## Gotchas & OpSec
- No native search/listing and pastes can expire — discoverability depends entirely on search-engine indexing.
- Content is unverified and may be fabricated or bait; corroborate before relying on it.
- Don't paste your own notes here; don't reuse leaked credentials.

## Overlaps ("do both")
- Pairs with `[[pastebin]]` and `[[katbin]]` — sweep the same leak dorks across several paste hosts, since posters pick whichever site they like.

## Trust & verifiability
`trust: community` — an unvetted paste host. Treat any find as unverified user-submitted text and confirm independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pastery |
| category | communities-forums |
| selectorsIn → selectorsOut | username → email, password |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: bpaste
name: bpaste
description: Use when you have a bpaste URL/ID or are dorking for leaked text — returns the pasted content; a paste host where dumps and notes may be shared.
url: https://bpa.st/
category: communities-forums
path:
- communities-forums
bestFor: Reading a bpaste paste you've been pointed to, and treating it as a paste host where leaked data may surface.
selectorsIn:
- username
selectorsOut:
- email
- password
status: live
pricing: free
costNote: Free open-source pastebin (the Python community's paste service); no account to create or view a paste.
opsec: passive
opsecNote: Viewing a paste by its link is passive and anonymous; the poster isn't notified. No public paste index, so access is via a known URL or a search-engine hit. Don't paste your own case data into it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running community paste service (bpa.st, associated with the Python community); content is arbitrary user-submitted text with no verification.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- pastebin
- katbin
- pastery
aliases:
- bpa.st
- bpaste.net
tags:
- pastebins
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# bpaste

> A long-running open-source pastebin (bpa.st) — an OSINT-relevant paste host where leaked credentials, code, or notes can surface, reached via links or search dorks rather than an on-site search.

## When to use
You're pointed to a `bpa.st` paste, or you're sweeping paste sites for leaks tied to a subject (an `email`, `username`, or dump). Like other paste hosts, bpaste has no public browse/search — you reach a paste by its URL or via a search engine that indexed it. Use it to read a referenced paste and to include `bpa.st`/`bpaste.net` in leak-hunting dorks.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open a known paste directly by URL (e.g. `https://bpa.st/<id>`).
2. To find relevant pastes, dork a search engine: `site:bpa.st "target@email.com"` or a username/handle.
3. Read the content (often code, logs, config, or leaked lists).
4. Extract selectors: emails, usernames, passwords, hosts.
5. Pivot: leaked `email`/`password` → breach-check/account tools; hosts/usernames → cross-platform search. Never reuse a credential.

## Inputs → Outputs
- **In:** a bpaste URL/ID, or a dork term (`username`, `email`)
- **Out:** raw pasted text → possible `email`/`password`/host leaks
- **Empty/negative result looks like:** no indexed pastes for your dork, or an expired/removed paste — most pastes are unlisted and many expire, so absence here means little.

## Gotchas & OpSec
- No native search/listing and pastes can expire — discoverability depends entirely on search-engine indexing.
- Content is unverified and may be fabricated or bait; corroborate before relying on it.
- Don't paste your own notes here; don't reuse leaked credentials.

## Overlaps ("do both")
- Pairs with `[[pastebin]]`, `[[katbin]]`, and `[[pastery]]` — sweep the same leak dorks across multiple paste hosts, since posters pick whichever site they prefer.

## Trust & verifiability
`trust: community` — an unvetted paste host. Treat any find as unverified user-submitted text and confirm independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bpaste |
| category | communities-forums |
| selectorsIn → selectorsOut | username → email, password |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

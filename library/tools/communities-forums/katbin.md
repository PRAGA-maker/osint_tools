---
id: katbin
name: Katbin
description: Use when you have a Katbin paste URL/ID or are dorking for leaked text — returns the pasted content; a place dumps and notes may be shared.
url: https://katb.in
category: communities-forums
path:
- communities-forums
bestFor: Reading a Katbin paste you've been pointed to, and recognizing it as a paste host where leaked data or notes may be posted.
selectorsIn:
- username
selectorsOut:
- email
- password
status: live
pricing: free
costNote: Free open-source pastebin (sphericalkat/katbin); no account needed to create or view a paste.
opsec: passive
opsecNote: Viewing a paste by its link is passive and anonymous — the poster isn't notified. There is no public index of pastes, so you access content only via a known URL or a search-engine hit; don't paste your own case data into it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Small open-source paste service; content is arbitrary user-submitted text with no verification — treat anything found as unverified.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- pastebin
- pastery
aliases:
- katb.in
tags:
- pastebins
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# Katbin

> A lightweight open-source pastebin — relevant to OSINT as one more host where leaked credentials, dox, or notes can surface (found via links or dorks, not a built-in search).

## When to use
Someone references a `katb.in` paste, or you're sweeping paste sites for leaked data tied to a subject (an `email`, a `username`, a breach dump). Katbin has no public directory of pastes, so you can't browse it — you reach a paste via a direct URL or by a search engine that indexed it. Use it to read a paste you've been pointed to, and include `katb.in` in Google dorks when hunting for leaks.

## How to use it (`bestInteractionPattern`: web-manual)
1. To read a known paste, open its URL directly (e.g. `https://katb.in/<id>`).
2. To hunt for relevant pastes, dork a search engine: `site:katb.in "target@email.com"` or a username/handle.
3. Read the content — often code, logs, config, or leaked lists.
4. Extract selectors: emails, usernames, passwords, hostnames.
5. Pivot: leaked `email`/`password` → breach-check and account tools; usernames/hosts → cross-platform search. Do NOT reuse any credential.

## Inputs → Outputs
- **In:** a Katbin paste URL/ID, or a dork term (`username`, `email`) to find one
- **Out:** raw pasted text → possible `email`/`password`/host leaks
- **Empty/negative result looks like:** no indexed pastes for your dork / a dead paste link — pastes can expire or be unlisted, and most are never indexed; absence here means little.

## Gotchas & OpSec
- No native search or public listing — Katbin is only as discoverable as search engines make it; most pastes stay private-by-link.
- Content is unverified and can be fabricated, stale, or bait — corroborate before acting.
- Don't paste your own investigation notes here; and never reuse leaked credentials (illegal and OpSec-poor).

## Overlaps ("do both")
- Pairs with `[[pastebin]]` and `[[pastery]]` — run the same leak dorks across multiple paste hosts, since data lands on whichever the poster chose.

## Trust & verifiability
`trust: community` — an open-source paste host with zero content vetting. Anything found is unverified user text; treat it as a lead and confirm independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | katbin |
| category | communities-forums |
| selectorsIn → selectorsOut | username → email, password |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

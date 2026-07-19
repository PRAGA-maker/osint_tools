---
id: cutapaste
name: Cutapaste
description: Use when you have a `username`/`email`/`domain` term and want to search for leaked or dumped text on a pastebin — returns pastes that may contain credentials, contact data or documents.
url: https://cutapaste.net/
category: communities-forums
path:
- communities-forums
bestFor: A public pastebin to search/monitor for dumped text (credential lists, contact data, leaks) referencing a selector.
selectorsIn:
- username
- email
- domain
selectorsOut:
- email
- password
- document-id
status: degraded
pricing: free
costNote: Free to read and create pastes; no account required to view public content.
opsec: passive
opsecNote: Reading public pastes is passive. Never enter live credentials you find, and don't create a paste containing case data. Use a search engine's site: operator against the domain so you don't tip a monitored paste. Handle any breach data ethically and lawfully.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A minor third-party pastebin listed in awesome-pastebins directories; uptime is inconsistent (observed intermittent 503s) and there is no guarantee of index completeness.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- cutapaste.net
tags:
- pastebins
- leaks
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# Cutapaste

> A public pastebin — of interest to OSINT as one more place leaked credentials, contact lists, or dumped documents referencing your selector may surface.

## When to use
You are hunting for exposed data — a `username`, `email`, `domain`, or company name that may appear in a dumped credential list, contact export, or leaked document. Pastebins like Cutapaste are common dumping grounds, so it's worth checking (and periodically re-checking) whether your selector shows up here alongside the mainstream paste sites.

## How to use it (`bestInteractionPattern`: web-manual)
1. Visit https://cutapaste.net/ (retry if you hit an intermittent 503 — uptime is inconsistent).
2. Cutapaste is primarily a create/share pastebin with limited on-site search, so the reliable route is a search engine: `site:cutapaste.net "<email-or-username-or-domain>"`.
3. Open any matching paste and scan for credentials, contact details, internal document references, or other identifiers.
4. Do NOT reuse or enter any live credential you find; record the finding and its context.
5. Pivot: leaked `email`/`password` pairs feed breach-analysis and account-existence checks; document references feed further record searches.

## Inputs → Outputs
- **In:** `username`, `email`, or `domain` search term
- **Out:** pastes possibly containing `email`s, `password`s/credentials, and `document-id` references
- **Empty/negative result looks like:** no indexed pastes match — meaning nothing is dumped *here* under that term. This is a niche site; absence says nothing about the mainstream paste ecosystem, so check the larger paste-aggregators too.

## Gotchas & OpSec
- Uptime is unreliable (intermittent 503s observed) — treat a failed load as transient, not proof it's dead, but don't depend on it.
- On-site search is weak; rely on `site:` engine queries.
- Legal/ethical: handle any breach/credential data responsibly and never authenticate with found credentials.

## Overlaps ("do both")
- Pairs with paste-aggregators and breach-search tools — a single small pastebin covers little, so cross-check the big aggregators and HIBP-style services for the same selector.

## Trust & verifiability
`trust: unverified` — a minor, inconsistently available pastebin; any hit is only as trustworthy as the paste's own content, which is anonymous and unvetted. Corroborate anything found here before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cutapaste |
| category | communities-forums |
| selectorsIn → selectorsOut | username, email, domain → email, password, document-id |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: onion-lookup
name: onion-lookup
description: Use when you have a Tor `.onion` address and want to confirm it exists and pull its metadata — returns onion domain details (titles, seen-dates, related indicators) from the AIL project.
url: https://onion.ail-project.org/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Checking whether a .onion hidden service exists and retrieving its indexed metadata.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
opsec: passive
opsecNote: You query the AIL project's index over the clearnet, not the hidden service itself — so you do NOT connect to the .onion (no Tor circuit to the target, no footprint on it). This is safer than visiting the onion directly. Data is whatever AIL has previously crawled, so absence means "not indexed," not "doesn't exist."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Part of the AIL Project by CIRCL (Luxembourg CERT), a reputable threat-intel org; open source (AGPLv3).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- onion-lookup
- AIL onion lookup
tags:
- dark-web
- onion-services
- threat-intelligence
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# onion-lookup

> A clearnet lookup for Tor hidden services — check whether a `.onion` address is known and pull its indexed metadata without ever connecting to the onion yourself.

## When to use
You've encountered a `.onion` address (in a paste, a chat, a breach, a scam) and want to verify it and learn about it before deciding whether to investigate further. onion-lookup, backed by CIRCL's AIL project, tells you if the service has been seen/indexed and returns associated metadata — a safe first step that avoids opening an unknown, potentially hostile hidden service in Tor.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://onion.ail-project.org/.
2. Enter the target `.onion` address.
3. Read the result: whether it's known/indexed and its associated metadata (titles, seen dates, related indicators) (`selectorsOut`).
4. Automate via the documented API (OpenAPI/Swagger) for bulk checks; pivot any related indicators into further dark-web/threat-intel research.

## Inputs → Outputs
- **In:** `domain` (a Tor `.onion` address)
- **Out:** `domain` existence + metadata (indexed details, related indicators)
- **Empty/negative result looks like:** not found / no metadata — the service isn't in AIL's index; it may be new, short-lived, or simply uncrawled, not necessarily nonexistent.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive and notably safer than direct access — you query AIL's clearnet index, so no Tor connection reaches the hidden service.
- Coverage is limited to what AIL has crawled; onion services churn fast, so treat a miss as inconclusive.

## Overlaps ("do both")
- Pairs with dark-web search engines (Ahmia, onion indexes) and paste/leak search — onion-lookup verifies and enriches a specific address safely, while search engines help you discover addresses in the first place.

## Trust & verifiability
`trust: trusted` — built by CIRCL (Luxembourg's CERT) as part of the open-source AIL project. The service and its data are reputable; because onion services are ephemeral, confirm current status carefully and treat an absence as "not indexed."

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onion-lookup |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

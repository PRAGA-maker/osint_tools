---
id: canadian-law-list-lawyer-search-engine-canada
name: Canadian Law List Lawyer Search Engine (Canada)
description: Use when you have a `name` or `address`/region and want to find a Canadian lawyer or law firm — returns contact details, firm, address and practice area.
url: http://www.canadianlawlist.com
category: search-engines
path:
- search-engines
bestFor: Locating a specific lawyer or law firm in Canada, or the counsel associated with a person or matter, by name, firm, location or practice area.
selectorsIn:
- name
- address
selectorsOut:
- name
- phone
- address
- employer-org
status: live
pricing: freemium
costNote: Free to search and view listings; lawyers/firms pay for enhanced listings and advertising, but public search is free with no account.
opsec: passive
opsecNote: A public professional directory; searching leaks nothing to the person you look up. Standard clean-browser hygiene is enough — no notifications are sent to listed lawyers.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running commercial legal directory (published by Thomson Reuters/Carswell lineage); listings are self- and firm-supplied, so treat contact details as current-but-unverified.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Canadian Law List
tags:
- toddington
- curated-directory
- legal
- specialty-search
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Canadian Law List Lawyer Search Engine (Canada)

> Canada's established lawyer/firm directory — search by name, firm, location or practice area to reach the counsel behind a person or matter.

## When to use
You have a `name` (of a lawyer, or a person whose lawyer you're trying to reach) or a `address`/region and practice area, and you need contact details for legal representation in Canada. In a missing-persons or locate context this helps you identify or reach the attorney tied to a subject — for estate, family, immigration or litigation matters — which can be a legitimate channel to pass a message or confirm representation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.canadianlawlist.com.
2. Search by lawyer name, firm name, practice area, and/or province/territory.
3. Open a listing to read firm affiliation, office `address`, `phone`, email, and areas of practice.
4. Pivot: a firm name feeds a corporate-records or website lookup; a confirmed lawyer of record is a lawful contact point for reaching a subject who does not want to be found directly.

## Inputs → Outputs
- **In:** `name` and/or `address`/region (+ practice area)
- **Out:** `name`, `employer-org` (firm), `address`, `phone`
- **Empty/negative result looks like:** no matching lawyer/firm returned — the person may not be a listed Canadian lawyer, or the listing lapsed; it is not proof they don't practise.

## Gotchas & OpSec
- Listings are firm-supplied and may be stale or upsell "enhanced" placements; verify contact details against the firm's own site or the provincial law society before relying on them.
- Coverage is Canada only; for other jurisdictions use the relevant national bar/law-society directory.
- OpSec: passive public-directory search; no alert reaches the person.

## Overlaps ("do both")
- Complements provincial law-society member directories — the law society is authoritative for licensing/standing, this list is better for firm contact and practice-area discovery.

## Trust & verifiability
`trust: community` — a reputable long-standing commercial directory, but entries are self-submitted; cross-check the licensing status with the person's provincial law society.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canadian-law-list-lawyer-search-engine-canada |
| category | search-engines |
| selectorsIn → selectorsOut | name, address → name, phone, address, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

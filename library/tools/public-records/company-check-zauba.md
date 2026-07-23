---
id: company-check-zauba
name: ZaubaCorp (Company Check)
description: Use when you have an Indian company or director `name` and want official corporate registry details — directors, CIN, registered `address`, filings — returns company and director records with cross-links.
url: https://www.zaubacorp.com
category: public-records
path:
- public-records
bestFor: Looking up Indian (MCA-registered) companies and directors — directorships, co-directors, registered address and status.
selectorsIn:
- employer-org
- name
selectorsOut:
- address
- name
- associate
status: live
pricing: freemium
costNote: Free to search and view core company/director details; full financial documents and some reports are paid.
opsec: passive
opsecNote: Passive — you query a public aggregation of India's MCA corporate registry; no target is contacted. Data is official filing data, but can lag the registry; confirm critical facts on the MCA portal.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A widely-used third-party mirror/aggregator of India's Ministry of Corporate Affairs data; reliable for leads, but the authoritative source is MCA itself.
missingPersonsRelevance: medium
coverage:
- in
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- ZaubaCorp
- Zauba Corp
- zaubacorp.com
tags:
- india
- corporate-registry
- directors
- company-search
source: metaosint
lastVerified: '2026-07-23'
enrichment: full
---

# ZaubaCorp (Company Check)

> A free front-end to India's corporate registry: search a company or director and get directors, CIN, registered address, incorporation date and status.

## When to use
You have an Indian company `name` (or a director's `name`) and want to map the corporate structure around it — who the directors are, what other companies they sit on, the registered `address`, and the company's status. Strong for linking a person to businesses and uncovering co-directors (`associate`s) in an Indian context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.zaubacorp.com and search the company or director `name`.
2. Open the company page: directors, CIN, registered `address`, incorporation date, authorized/paid-up capital, status.
3. Click a director to see their **other directorships** — this reveals linked companies and co-directors.
4. Build the network by hopping director → companies → co-directors.
5. Verify anything critical against the official MCA (Ministry of Corporate Affairs) portal, since aggregated data can lag.

## Inputs → Outputs
- **In:** Indian company `employer-org` or director `name`
- **Out:** directors (`name`s), co-directors (`associate`s), CIN, registered `address`, status, incorporation date
- **Empty/negative result looks like:** no match — the entity may be unregistered, a partnership/LLP filed differently, or spelled differently; try the MCA portal directly.

## Gotchas & OpSec
- Covers **India (MCA-registered)** entities only — not partnerships/proprietorships without MCA filings.
- Aggregated data can be stale; confirm current directors/status at MCA.
- Full financial statements are behind a paywall; the free view still gives structure and directors.

## Overlaps ("do both")
- Pairs with the official MCA portal and global company registries (OpenCorporates) — ZaubaCorp gives fast, linked director networks; MCA/OpenCorporates confirm and extend beyond India.

## Trust & verifiability
`trust: community` — a reliable third-party aggregator of official Indian registry data; treat as a strong lead and confirm at the MCA source for anything decisive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | company-check-zauba |

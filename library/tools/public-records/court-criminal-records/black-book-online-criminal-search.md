---
id: black-book-online-criminal-search
name: Black Book Online — Criminal Search
description: Use when you have a `name` + US location and want free links to official records — a portal routing you to state/county criminal, court, property and offender databases, returning `address`, court and `associate` data.
url: https://www.blackbookonline.info/
category: public-records
path:
- public-records
- court-criminal-records
bestFor: A free directory of official US public-records sources (criminal, court, property, offender) organised by state/county.
selectorsIn:
- name
- address
selectorsOut:
- address
- associate
status: live
pricing: free
costNote: The Black Book Online directory is free. It links to official sources, some of which charge for documents; it is not a background-check subscription itself.
opsec: passive
opsecNote: Using the directory is passive. Each linked official source has its own logging; most county/court searches are anonymous, but read each site's terms. Not FCRA-compliant — do not use for employment/tenant screening.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running, well-regarded free public-records portal (by Peter Weber/BRB Publications) that curates links to official government sources rather than reselling data.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- unicourt
- courtlistener
- arrest-warrants
- criminal-search-criminal-records-by-state-and
- free-aviation-records-black-book-online
- jail-records
- nationwide-county-court-records-by-state-and
- property-search-public-records-by-state
- sex-offender-search
aliases:
- Black Book Online
- blackbookonline.info
tags:
- public-records
- criminal-records
- court-records
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Black Book Online — Criminal Search

> A free, hand-curated gateway to official US public records — instead of selling you a report, it points you to the actual state/county criminal, court, property and offender databases.

## When to use
You have a `name` and a US location and want authoritative records rather than a paid data-broker summary. Black Book Online organises thousands of free public-records sources by state and county — criminal/inmate searches, court dockets, property records, sex-offender registries, professional licences — so you can go straight to the government source that holds the data. It's the "where do I actually look?" tool for US records work, and it keeps you on primary sources you can cite.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.blackbookonline.info/ and pick the record type (e.g. Criminal Records) and the state, then county.
2. Follow the curated link to the official database (state DOC inmate locator, county clerk of court, sheriff, assessor, etc.).
3. Search that official source by `name` (and location) per its own interface.
4. Read the record for court/case detail, `address`es, and named co-parties/relatives (`associate`s); note that most criminal data is county-level, so check every relevant county.
5. Pivot: court cases → `[[unicourt]]`/`[[courtlistener]]` for cross-jurisdiction litigation; addresses → people-search; property records → ownership/geolocation.

## Inputs → Outputs
- **In:** `name` (+ US state/county), sometimes `address`
- **Out:** links to official records yielding criminal/court history, `address`es, property ownership, `associate`s
- **Empty/negative result looks like:** the linked source returns no match — remember US criminal records are county-by-county, so a null in one county isn't a clean record overall. Check surrounding counties and statewide sources.

## Gotchas & OpSec
- It's a **directory of links**, not a single search box — expect to hop into each official site and learn its quirks (human-in-the-loop review of each source).
- **Not FCRA-compliant** — legally cannot be used for employment, tenant, or credit decisions.
- Coverage/quality varies wildly by county; some links may be stale — confirm you're on the current official site.
- US-only.

## Overlaps ("do both")
- Pairs with `[[unicourt]]` and `[[courtlistener]]` for litigation that spans jurisdictions, while Black Book gets you into the county-level criminal/property sources those may miss. Use it to find sources; use them to search broadly.

## Trust & verifiability
`trust: trusted` — a long-established, respected free portal (BRB Publications) that curates links to official government record sources rather than reselling scraped data, so what you ultimately read is primary-source. The directory itself is maintained by a third party, so verify each linked site is current.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | black-book-online-criminal-search |
| category | public-records |
| selectorsIn → selectorsOut | name, address → address, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |

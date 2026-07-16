---
id: court-locator-united-states-courts
name: Court Locator | United States Courts
description: Use when you have a location (`address`/state) and need to find the right US federal court and its records system — returns the court and a route to case records (`document-id` via PACER).
url: http://www.uscourts.gov/court-locator
category: public-records
path:
- public-records
bestFor: Identifying which US federal district/bankruptcy/appellate court serves a place, and linking to its website and PACER records.
selectorsIn:
- address
selectorsOut:
- document-id
- employer-org
status: live
pricing: free
costNote: The locator/directory itself is free (official uscourts.gov). Note it routes you to PACER for actual case documents, and PACER charges per page/search beyond a modest fee-waiver threshold.
opsec: passive
opsecNote: Passive — you are browsing an official court directory; no subject is involved. The onward PACER case search requires a registered PACER account (a trail), and querying a specific person's cases there is logged; use appropriate account hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official directory published by the Administrative Office of the U.S. Courts; authoritative for which federal court has jurisdiction and how to reach its records.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- US Courts Court Locator
- uscourts.gov court locator
tags:
- court
- inmate
- legal
- federal
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- court-electronic-records-pacer
- court-records-united-states-courts
- pacer-2
- pacer-case-locator
- public-access-to-court-electronic-records
---

# Court Locator | United States Courts

> The official "find a federal court" directory: given a place, it tells you which US district/bankruptcy/appellate court has jurisdiction and links you to its site and PACER records. A routing tool, not a case search itself.

## When to use
You know your subject's location or where an event occurred and need to identify the correct **federal** court to search — then get to its case records. It answers "which court, and where do I look?" so you don't waste time in the wrong jurisdiction. It's a navigation step ahead of an actual name-based case search (which happens in PACER/CM-ECF or the local court site).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.uscourts.gov/court-locator and enter a location (state/city/ZIP) and the court type (district, bankruptcy, appellate).
2. It returns the court(s) serving that area with links to each court's website and PACER/CM-ECF.
3. Follow the link into PACER (or the court site) and run the actual name search there for cases (`document-id`).
4. Note: PACER needs a registered account and charges beyond the fee-waiver threshold.
5. Pivot: a case number/`document-id` from PACER feeds document retrieval; state matters route to state tools like `[[iowa-courts-online-search]]`.

## Inputs → Outputs
- **In:** a location (`address`/state/ZIP) + desired court type
- **Out:** the responsible federal court (an `employer-org`/institution) and links to its records system, which is where `document-id` case records live — **the locator itself returns no person data**
- **Empty/negative result looks like:** it always returns a court for a valid US location; the "miss" is realizing your matter is a **state** case (not federal), so redirect to state court tools.

## Gotchas & OpSec
- Human-in-the-loop: none for the locator; PACER requires an account/payment for the actual search.
- OpSec: **passive** at the directory; the onward PACER query is logged and tied to your PACER account — use hygiene.
- Federal only. Most everyday criminal/civil matters are **state** cases — don't assume federal.

## Overlaps ("do both")
- Pairs with `[[iowa-courts-online-search]]` and other state-court tools — this routes federal matters to PACER; state tools cover the far more common state cases. Run the right one for the jurisdiction.

## Trust & verifiability
`trust: trusted` — first-party US Courts directory. Authoritative for jurisdiction/routing; the case facts themselves come from PACER/the court and should be read there.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | court-locator-united-states-courts |
| category | public-records |
| selectorsIn → selectorsOut | address → document-id, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

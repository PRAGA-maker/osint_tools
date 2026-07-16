---
id: free-public-records-directory-us
name: OnlineSearches (Free Public Records Directory, US)
description: Use when you have a name and a US state/county and want the right official record source — returns links to free state/county property, court, vital and voter record searches.
url: http://publicrecords.onlinesearches.com/
category: people-search
path:
- people-search
bestFor: Finding the correct free official US state/county public-records search portal for a given jurisdiction.
selectorsIn:
- name
- address
selectorsOut:
- address
- associate
- dob
- document-id
status: live
pricing: freemium
costNote: The directory and the official searches it links to are free; OnlineSearches is operated by Intelius and upsells paid people-search reports on the same pages. Stick to the outbound links to free official sources to avoid the paywall.
opsec: passive
opsecNote: Browsing the directory is passive and does not alert anyone. Each outbound official search runs on a government site with its own logging. Avoid running names through the Intelius-branded paid boxes on the page if you want to stay off a commercial broker's logs; use the free official links instead. VPN for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An aggregator/directory (Intelius-run) that links to authoritative government sources; the directory itself is a signpost, and it monetises via paid reports, so treat its own boxes with caution and trust the official sites it points to.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- OnlineSearches
- publicrecords.onlinesearches.com
- Free Public Records Directory
tags:
- people-search
- public-records-directory
- us
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
relatedTools:
- court-records-search-directory
- jail-and-inmate-records-search-directory
- laws-and-codes-search-directory-by-state
- marriage-records-search-directory
- os-birth-records
- os-death-records
- os-divorce-records
- permits-and-inspections-search-by-state
- public-records-directory
- sex-offender-us
- unclaimed-and-abandoned-property-search-directory
---

# OnlineSearches (Free Public Records Directory, US)

> A jurisdiction-by-jurisdiction signpost to the *official* free US public-records searches — the fast way to find which county/state site actually holds the record you need.

## When to use
You have a `name` and know (or suspect) a US `address`/county, and you want the authoritative government source rather than a broker's summary. Property deeds, court and warrant records, vital records (birth/death/marriage/divorce), sex-offender registries, voter and UCC filings all live on scattered state and county portals. OnlineSearches indexes those official portals by state → county → record type, so you jump straight to the right free search instead of guessing URLs.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://publicrecords.onlinesearches.com/ and drill down: pick the **state**, then the **county**, then the **record category** (property, court, vital, criminal, voter, licensing).
2. Follow the **outbound link to the official government search** — that is the value; run the actual name/address query there, not in the page's own Intelius boxes.
3. On the official portal, search your `name`/`address` and read the record.
4. Ignore/skip the "background report" upsell boxes (those are paid Intelius products, FCRA-restricted).
5. Pivot: a deed gives an `address` + co-owners (`associate`); court records give a `document-id` and `dob`; feed these to people-search and mapping tools.

## Inputs → Outputs
- **In:** `name` and a US `address`/county/state to pick the jurisdiction
- **Out:** links to official searches yielding `address`, co-parties/`associate`, `dob`, and case `document-id`s
- **Empty/negative result looks like:** the county has no online portal listed, or the linked official site itself returns nothing. A gap in the directory means "not online here," not "no record exists" — some counties are offline-only.

## Gotchas & OpSec
- OnlineSearches is run by **Intelius**; the page mixes free official links with paid people-search upsells — use the outbound official links, avoid the paid boxes.
- Explicitly **not for FCRA purposes** (employment, housing, credit) — this is investigative/locate use only.
- Coverage and record availability vary wildly by county; always confirm the record on the official site, and note the directory is a pointer, not the source of truth.
- Passive, but each official portal logs its own searches; VPN for sensitive names.

## Overlaps ("do both")
- Pairs with statewide court portals (e.g. `[[state-appellate-and-supreme-courts]]`) and county-specific tools — the directory finds them, those tools go deep.
- Complements broader US people-search aggregators to cross-check an address or relative surfaced from a deed/court record.

## Trust & verifiability
`trust: community` — the directory itself is a commercially-run aggregator (Intelius) and should not be treated as a source; its worth is that it routes you to authoritative government portals, which are where you verify every fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | free-public-records-directory-us |
| category | people-search |
| selectorsIn → selectorsOut | name, address → address, associate, dob, document-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

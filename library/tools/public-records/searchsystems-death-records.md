---
id: searchsystems-death-records
name: SearchSystems Death Records
description: Use when you have a `name` (and rough US location) and want to locate the official government database holding a death/mortality record — returns links to state/county source databases yielding dob, date of death, and associate (next-of-kin) links.
url: https://publicrecords.searchsystems.net/free_public_records_by_type_of_record/death_records
category: public-records
path:
- public-records
bestFor: Routing to the correct official US state/county death-record or vital-records database instead of guessing the agency.
selectorsIn:
- name
selectorsOut:
- dob
- associate
- name
status: live
pricing: free
costNote: The directory is entirely free ("no paywall, no email harvesting, no account"). Some linked government databases charge for certified copies.
opsec: passive
opsecNote: Browsing the directory is passive and anonymous. Actual searches run on the linked .gov/.us sites, which log queries per their own policies; use a sock-puppet browser. The subject here is deceased, but next-of-kin data may surface living relatives — handle sensitively.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running (since 1997) public-records directory linking only to official government (.gov/.us) sources, not data brokers. A navigation index, so quality depends on the destination agency.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- searchsystems-birth-records
- vitalchek
- county-clerks-recorded-doc-s-by-state
- court-records-directory
- property-records-public-records-by-state
- search-systems-criminal-records
- search-systems-public-records-us
- texas-public-records-search
aliases:
- Search Systems death records
- searchsystems.net
tags:
- genealogy
- family
- vital-records
- public-records
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# SearchSystems Death Records

> A free directory that routes you to the official US government database holding a death/mortality record — a map of where the record lives, not the record itself.

## When to use
You have a `name` and an approximate US state/county and need the authoritative source for a death record or obituary/mortality index — to confirm whether a missing person is deceased, establish a date of death, or pull next-of-kin (`associate`) links for a family tree. SearchSystems indexes official government death/vital databases by jurisdiction so you land on the real .gov source rather than a data-broker upsell.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the SearchSystems death-records page (it routes into the main `searchsystems.net/us` state index).
2. Drill to the subject's state → county → vital/death-records category.
3. Follow the link to the official database and search the name (rules and fees differ per agency).
4. Read the result — an index entry (name, date of death, county) is often free; certified copies usually cost and may be eligibility-gated.
5. Pivot: cross-check with `[[searchsystems-birth-records]]` for the birth side, and use `[[vitalchek]]` to order a certified copy where permitted.

## Inputs → Outputs
- **In:** `name` (+ US jurisdiction)
- **Out:** links to source databases yielding date of death / `dob`, `associate` (next of kin), confirmed `name`
- **Empty/negative result looks like:** no matching jurisdiction/database, or the destination returns no index hit — the death may be recent (not yet indexed), out of state, or pre-digitisation; absence is not proof the person is alive.

## Gotchas & OpSec
- Human-in-the-loop: **manual-review** — you must pick the right jurisdiction and interpret each agency's rules.
- OpSec: **passive** while browsing/searching indexes; ordering certified copies is attributable.
- US-only; openness varies sharply by state. Next-of-kin data can expose living relatives — handle with care.

## Overlaps ("do both")
- Pairs with `[[searchsystems-birth-records]]` (same directory, birth side) and `[[vitalchek]]` (ordering channel) — together they cover locate → read → obtain across the vital-records lifecycle.

## Trust & verifiability
`trust: trusted` — links exclusively to official government sources, so endpoints are authoritative; the directory's own risk is only a stale link, confirmable on arrival at the .gov site.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | searchsystems-death-records |
| category | public-records |
| selectorsIn → selectorsOut | name → dob, associate, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |

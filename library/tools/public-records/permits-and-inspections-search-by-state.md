---
id: permits-and-inspections-search-by-state
name: Permits and Inspections Search (by State) — OnlineSearches
description: Use when you have a property `address` or owner `name` and want building/permit records — returns a state-by-state directory of official permit and inspection lookups (document-id, address, owner links).
url: https://publicrecords.onlinesearches.com/permits-and-inspections.htm
category: public-records
path:
- public-records
bestFor: Finding the official city/county building-permit and inspection portals for a US location to tie a property to owners and dates.
selectorsIn:
- name
- address
selectorsOut:
- document-id
- address
- name
status: live
pricing: free
costNote: Free directory; it links out to official government portals, which are themselves free to search (some may charge for certified copies).
opsec: passive
opsecNote: OnlineSearches is a link directory and the government portals it points to are read-only public records — searching does not notify the property owner. Passive.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party public-records aggregator/directory; it does not hold data itself but curates links to official state/county sources.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- OnlineSearches permits and inspections
- publicrecords.onlinesearches.com
tags:
- court
- inmate
- property
- permits
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- court-records-search-directory
- free-public-records-directory-us
- jail-and-inmate-records-search-directory
- laws-and-codes-search-directory-by-state
- marriage-records-search-directory
- os-birth-records
- os-death-records
- os-divorce-records
- public-records-directory
- sex-offender-us
- unclaimed-and-abandoned-property-search-directory
---

# Permits and Inspections Search (by State) — OnlineSearches

> A curated directory that routes you to the *official* US city/county building-permit and inspection portals for a given location.

## When to use
You have a property `address` (or an owner `name`) in the US and want the paper trail a building generates: permits pulled, contractors named, inspection dates, and the applicant/owner on file. Permit records are an underused way to place a person at an address and time, or to surface a contractor/associate. OnlineSearches doesn't hold the data — it points you to the government portal that does, organized by state and county.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the OnlineSearches directory (https://publicrecords.onlinesearches.com/) and navigate to Permits & Inspections, or start from the target's state page. (If the exact deep link 404s, use the site's state/category navigation — the section is maintained even when individual URLs change.)
2. Drill to the relevant state → county/city; select the linked official permits or building-department portal.
3. On the official portal, search by `address` or owner `name` per that jurisdiction's form.
4. Read results: permit numbers (`document-id`), applicant/owner `name`, contractor, work description, and dates.
5. Pivot: the owner name feeds people search; the contractor is a possible `associate`; permit dates corroborate an occupancy timeline.

## Inputs → Outputs
- **In:** `address` (best) or owner `name`
- **Out:** permit/inspection `document-id`, associated `address`, applicant/owner `name`, contractor, dates
- **Empty/negative result looks like:** a state/county with no online permit portal listed (many rural jurisdictions are offline-only), or the official portal returning no permits for an address. Absence often means "not digitized," not "no permits."

## Gotchas & OpSec
- Two-hop tool: OnlineSearches is a *directory* — the real search happens on the government site it links to, and coverage/format vary by jurisdiction.
- Human-in-the-loop: you must pick the right jurisdiction and run each portal's own form; deep links on the aggregator go stale.
- FCRA: OnlineSearches states it is not a consumer-reporting agency — do not use for employment/housing/credit decisions.
- OpSec: **passive**; official record searches don't alert the owner.

## Overlaps ("do both")
- Pairs with county assessor/recorder and property-deed searches — permits show *work and occupants over time*, deeds show *ownership transfers*; together they build a full address history.

## Trust & verifiability
`trust: community` — the directory itself is third-party, but it routes to authoritative government portals, so verify and cite the underlying official record, not the aggregator.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | permits-and-inspections-search-by-state |
| category | public-records |
| selectorsIn → selectorsOut | name, address → document-id, address, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |

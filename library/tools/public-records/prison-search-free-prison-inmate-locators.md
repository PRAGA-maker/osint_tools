---
id: prison-search-free-prison-inmate-locators
name: Prison Search - Free Inmate Locators (AncestorHunt)
description: Use when you have a `name` and want to find the right official US inmate locator — a state-by-state directory of free federal, state, and county prisoner-search links.
url: http://www.ancestorhunt.com/prison_search.htm
category: public-records
path:
- public-records
bestFor: Quickly finding the correct official inmate/prisoner locator for a given US state, county, or the federal system.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- address
status: live
pricing: free
costNote: Free directory of links; the official locators it points to are also free to search.
opsec: passive
opsecNote: A link directory plus official government locators — searches are read-only public records and don't notify the inmate. Passive.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running genealogy site (AncestorHunt) that curates links to official federal/state/county inmate locators; it holds no data itself, so trust flows to the official sources it links.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- AncestorHunt Prison Search
- free inmate locators directory
tags:
- court
- inmate
- corrections
- directory
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Prison Search - Free Inmate Locators (AncestorHunt)

> A jump-table to the right official inmate locator: federal, state, and county prisoner searches, organized so you don't have to hunt for the correct portal.

## When to use
You have a `name` and suspect (or need to rule out) US incarceration, but you don't know which official locator to use for the relevant jurisdiction. This directory links to the federal BOP locator and each state's DOC search, plus county-jail search resources — the fast way to reach the authoritative source for wherever your subject might be held.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.ancestorhunt.com/prison_search.htm (and its County Jail Inmate Search companion page).
2. Pick the jurisdiction: federal (BOP), the relevant state DOC, or the county.
3. Follow the link to the official locator and search there by `name` (and any ID/DOB the portal asks for).
4. Read the official result: inmate `name`, ID/`document-id`, facility (`address`), and status.
5. Pivot: a facility and ID confirm custody and location; feed into `[[vinelink]]` for change notifications; a "released" status reframes the timeline toward court/booking records.

## Inputs → Outputs
- **In:** `name` (applied on the linked official locator)
- **Out:** via the official source — inmate `name`, `document-id`, facility `address`, custody status
- **Empty/negative result looks like:** a jurisdiction with no online locator listed, or the official portal returning no match. Coverage is uneven (many county jails lack online search), so a miss in one system doesn't rule out custody elsewhere — check federal, state, and county separately.

## Gotchas & OpSec
- Two-hop tool: this is a *directory* — the real search happens on the official locator it links to, and each has its own form and quirks.
- Link rot: a genealogy-maintained list can carry stale links; if one is dead, go straight to the BOP or the state DOC site.
- OpSec: **passive**; official inmate searches don't alert anyone.

## Overlaps ("do both")
- Pairs with `[[vinelink]]` and specific state searches like `[[maine]]` — this directory routes you to the right official locator, VINE aggregates and adds notifications, and the state DOC gives the authoritative detail.

## Trust & verifiability
`trust: community` — the directory is third-party, but it routes to authoritative government locators; verify and cite the official record, not the AncestorHunt page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | prison-search-free-prison-inmate-locators |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |

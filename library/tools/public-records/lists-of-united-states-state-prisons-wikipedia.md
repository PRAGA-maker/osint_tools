---
id: lists-of-united-states-state-prisons-wikipedia
name: Lists of United States state prisons - Wikipedia
description: Use when you have a state or a facility `name` and want the roster/location of that state's prisons — returns facility names and `address`/location context to route an inmate lookup.
url: https://en.wikipedia.org/wiki/Lists_of_United_States_state_prisons
category: public-records
path:
- public-records
bestFor: Enumerating a state's prisons and locating a named facility so you know which state DOC inmate-locator to query next.
selectorsIn: []
selectorsOut:
- address
status: live
pricing: free
costNote: Free Wikipedia reference; no account.
opsec: passive
opsecNote: Reading a public Wikipedia article leaks nothing about your subject and never contacts anyone. No sock puppet needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-maintained Wikipedia; facility rosters are broadly accurate but may lag closures/renamings — confirm against the state DOC site before relying on it.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- US state prisons list
- Wikipedia state prisons
tags:
- court
- inmate
- reference
source: metaosint
lastVerified: '2026-07-16'
enrichment: full
---

# Lists of United States state prisons - Wikipedia

> A directory page linking to per-state lists of U.S. state prisons — the fast way to enumerate a state's facilities and locate a named one before hitting the state inmate locator.

## When to use
You know (or suspect) a subject is incarcerated in a given U.S. state, or you have a facility `name` and need to place it — which state runs it, where it is, and what the other facilities in that state are. It is a routing/reference step: use it to pick the correct state Department of Corrections inmate-locator to search next.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://en.wikipedia.org/wiki/Lists_of_United_States_state_prisons.
2. Follow the link for the relevant state to see that state's prison roster (and links to individual facility articles with location/operator detail).
3. Confirm a facility's location/operator, or scan the roster to identify a facility from partial info.
4. Pivot: with the facility and state confirmed, run the subject through that state's DOC inmate locator (and federal BOP if needed) — this page does not itself return inmate records.

## Inputs → Outputs
- **In:** a U.S. state, or a partial/whole facility `name`
- **Out:** facility roster + per-facility `address`/location and operator; a jump-off to the right inmate locator
- **Empty/negative result looks like:** the facility is not listed — it may be a county jail, federal prison, or juvenile/private facility not covered here (the page explicitly excludes federal prisons and county jails); redirect to the appropriate list.

## Gotchas & OpSec
- It excludes federal prisons and county jails — a missing facility does not mean it doesn't exist, just that it's out of this page's scope.
- Data can lag real-world closures, transfers to private operators, or renamings; verify current status on the state DOC site.
- OpSec: fully passive — public reference reading, no subject contact.

## Overlaps ("do both")
- Pairs with state DOC inmate locators and the federal BOP locator — this page tells you *which* system to search; those return the actual inmate record.

## Trust & verifiability
`trust: community` — Wikipedia, actively maintained but community-sourced; treat the facility list as a reliable index and confirm any operational detail against the official corrections agency.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lists-of-united-states-state-prisons-wikipedia |
| category | public-records |
| selectorsIn → selectorsOut | (none) → address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

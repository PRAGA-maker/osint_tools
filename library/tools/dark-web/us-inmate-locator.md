---
id: us-inmate-locator
name: US Inmate Locator
description: Use when you have a `name` and think the person may be incarcerated — returns a directory of state/federal DOC search links leading to facility `address` and inmate `document-id`.
url: http://www.theinmatelocator.com/
category: dark-web
path:
- dark-web
bestFor: One hub linking to every US state and federal inmate-search system to check if a person is currently or recently in custody.
selectorsIn:
- name
selectorsOut:
- address
- document-id
status: live
pricing: free
costNote: Free directory; the linked DOC search systems are also free public-record lookups.
opsec: passive
opsecNote: You search public correctional records; the subject is not contacted. Some state systems log searches, but these are open records. Results are personal/sensitive — handle accordingly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party link directory (not an official source); it points to authoritative government DOC systems but does not itself guarantee accuracy.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- inmate-locator-us
aliases:
- The Inmate Locator
- theinmatelocator.com
tags:
- toddington
- curated-directory
- specialty-search
- incarceration
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# US Inmate Locator

> A directory that gathers links to every US state Department of Corrections inmate search plus the federal BOP locator — the fast way to check whether a person you're looking for is in custody.

## When to use
Someone is missing or unaccounted for and incarceration is a real possibility. Rather than hunting each state's DOC site individually, this hub links them all in one place so you can systematically check state prison systems (and, via the federal BOP locator, federal inmates). A hit places the person at a specific facility with a booking/inmate number — a strong, official location anchor. High value in missing-persons work because "in custody" is a common, checkable explanation for someone dropping off the grid.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.theinmatelocator.com/ and pick the relevant state (and/or the federal BOP link).
2. Follow the link to that jurisdiction's official inmate-search system.
3. Search by the subject's `name` (and DOB where the state allows) on the official site.
4. Read the record: current facility (`address`), inmate/booking `document-id`, status, and sometimes admission/release dates.
5. Pivot: county jail systems are separate — for very recent arrests also check the county sheriff/jail roster; use the confirmed facility for visitation/records follow-up.

## Inputs → Outputs
- **In:** `name` (plus DOB where required)
- **Out:** facility `address`, inmate `document-id` (booking/DOC number), custody status/dates
- **Empty/negative result looks like:** no match in a state's system — the person isn't in *that* state's prisons, but could be in another state, in a county jail (often a separate roster), federal custody, or released. Check multiple systems before concluding.

## Gotchas & OpSec
- OpSec: **passive** — public correctional records; nothing reaches the subject.
- This is a *directory*: accuracy lives on the official DOC systems it links to, and some links may be stale — navigate to the current official site if one is dead.
- State prison systems exclude county jails and immigration detention; absence here is not absence from all custody.

## Overlaps ("do both")
- Pairs with the federal BOP inmate locator and county sheriff/jail rosters — together they cover federal, state and local custody, which no single system does.

## Trust & verifiability
`trust: community` — the directory is unofficial, but it routes you to authoritative government inmate systems; treat the government result, not the directory, as the source of truth.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | us-inmate-locator |
| category | dark-web |
| selectorsIn → selectorsOut | name → address, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

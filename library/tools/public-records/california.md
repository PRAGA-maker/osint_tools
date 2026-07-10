---
id: california
name: California
description: Use when you have a `name` or CDCR number and want to locate a person in California state prison custody — returns current incarceration status, facility, age and CDCR ID.
url: https://inmatelocator.cdcr.ca.gov
category: public-records
path:
- public-records
bestFor: Confirming whether a named person is (or was) in California state prison and where they are held.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: free
costNote: Free official state service; no account or payment required.
opsec: passive
opsecNote: Read-only search of the state's public inmate database. You submit only a name/ID; the subject is not notified and CDCR does not tie the query to the searcher. Use a clean session for hygiene.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the California Department of Corrections and Rehabilitation (CDCR) — the authoritative source for California state-prison custody status.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- indiana-offender-database-search
- sex-offender-us
aliases:
- CDCR Inmate Locator
- California inmate locator
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# California

> The CDCR Inmate Locator — California's official public search for people held in state prison, an authoritative "is this person incarcerated?" check.

## When to use
You have a `name` (and ideally an approximate age) for someone who may be in California state custody, and you need to confirm incarceration status and location. Incarceration is a common, mundane explanation for someone dropping off the grid, so a custody hit can resolve a missing-persons lead quickly; it also gives a verified age/CDCR ID to anchor further identity work. Note: this covers **state prison only** — not county jail, federal (BOP), or ICE custody.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://inmatelocator.cdcr.ca.gov.
2. Search by `name` (last/first) or, if known, the CDCR number. Solve the CAPTCHA if prompted.
3. Read the result: matching records show name, age, CDCR identification number (`document-id`), and current housing facility.
4. Corroborate age/spelling against other records; a CDCR number is a strong unique anchor.
5. Pivot: for out-of-state or other-custody-type checks, use other corrections locators (e.g. `[[indiana-offender-database-search]]`) or the federal BOP locator; the person's confirmed identity feeds court-record and people-search tools.

## Inputs → Outputs
- **In:** `name` (or CDCR number)
- **Out:** `name`, age (`dob` proxy), CDCR `document-id`, current facility/location
- **Empty/negative result looks like:** no match — meaning the person is not in California *state* prison custody (they may be in jail, federal, or another state, or simply not incarcerated). Absence is not proof of anything beyond "not in CDCR state custody now."

## Gotchas & OpSec
- Human-in-the-loop: a **CAPTCHA** commonly appears; solve it manually.
- Scope is CDCR state prisons only — county jails and federal facilities have separate locators.
- Common names return many hits; use age/CDCR number to disambiguate.
- OpSec: **passive** — a public-records read; the subject is not alerted.

## Overlaps ("do both")
- Pairs with other custody locators like `[[indiana-offender-database-search]]`, the federal BOP locator, and `[[sex-offender-us]]` registries — each covers a different jurisdiction or offender category, so run the ones matching the subject's likely location and status.

## Trust & verifiability
`trust: trusted` — first-party CDCR data; authoritative for California state-prison custody status.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | california |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |

---
id: alaska-inmate-search
name: Alaska Inmate Search
description: Use when you have a `name` and want to locate someone in Alaska Department of Corrections custody — a guide/gateway to the official Alaska DOC / VINELink inmate lookup returning status, DOB and offender ID.
url: https://inmatesearchinfo.com/alaska-inmate-search-department-of-corrections-lookup
category: public-records
path:
- public-records
bestFor: Finding and using the official Alaska DOC inmate lookup to confirm state custody status.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: free
costNote: Free; the guide page is free and the official Alaska DOC / VINELink lookups it points to are free public services.
opsec: passive
opsecNote: Read-only inmate lookup; the subject is not notified. Prefer the official Alaska DOC / VINELink source over the third-party guide when running the actual search, and use a clean session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: The listed URL is a third-party guide (inmatesearchinfo.com), not the government source; treat it as a signpost to the authoritative Alaska DOC / VINELink lookup, which is where the real data lives.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- iowa-offender-search
- ohio
- california
aliases:
- Alaska DOC inmate lookup
- Alaska VINELink
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Alaska Inmate Search

> A signpost to Alaska's inmate lookup — use it to reach the official Alaska DOC / VINELink search and confirm whether a person is in Alaska state custody.

## When to use
You have a `name` for someone who may be in Alaska Department of Corrections custody and need to confirm status and location. As with any state offender search, a custody hit is a common, quick resolution to a "went unreachable" lead and yields a verified DOB and offender ID. The catalogued URL here is a **third-party guide**; the authoritative data is the official Alaska DOC inmate lookup / VINELink, which you should use for the actual search. Scope is **Alaska state custody** — not federal (BOP) or other states.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the guide at the listed URL to find the current official links, then go to the **official Alaska DOC / VINELink** inmate lookup.
2. Search by `name` (or offender number if known).
3. Read the result: `name`, DOB, offender ID (`document-id`), custody status, and facility.
4. Disambiguate namesakes with DOB; the offender number is a unique anchor.
5. Pivot: for other jurisdictions use `[[iowa-offender-search]]`, `[[ohio]]`, `[[california]]`, or the federal BOP locator; the confirmed identity feeds court-record and people-search tools.

## Inputs → Outputs
- **In:** `name` (or offender number)
- **Out:** `name`, `dob`, offender `document-id`, custody status, facility
- **Empty/negative result looks like:** no match — the person isn't in Alaska DOC custody (may be federal, another state, or not incarcerated). Absence only rules out current Alaska state custody.

## Gotchas & OpSec
- The listed page is a **third-party guide** — always confirm findings on the official Alaska DOC / VINELink source, which is authoritative.
- Scope is Alaska state custody only.
- OpSec: **passive** — a public-records read; the subject is not alerted.

## Overlaps ("do both")
- Pairs with other state and federal locators — `[[iowa-offender-search]]`, `[[ohio]]`, `[[california]]`, and the federal BOP locator each cover a different jurisdiction; run the ones matching the subject's likely location.

## Trust & verifiability
`trust: community` — the catalogued URL is an unofficial guide; rely on the official Alaska DOC / VINELink lookup it points to for authoritative custody data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | alaska-inmate-search |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

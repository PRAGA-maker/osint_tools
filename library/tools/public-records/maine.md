---
id: maine
name: Maine DOC Corrections Search
description: Use when you have a `name` of someone possibly in Maine's corrections system and want their custody info — returns the resident's name, MDOC identifier, and facility/supervision status.
url: https://www1.maine.gov/online/mdoc/search-and-deposit/index.htm
category: public-records
path:
- public-records
bestFor: Checking whether a person is an adult resident or community-corrections client of the Maine Department of Corrections and where.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- address
status: live
pricing: free
costNote: Free official Maine DOC service, available 24/7; no account required.
opsec: passive
opsecNote: Official government custody lookup; the search is anonymous and does not notify the individual. Passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Maine Department of Corrections. Note the site itself states results are NOT a complete criminal history — that requires a separate Public Criminal History Request.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Maine Department of Corrections search
- MDOC inmate search
tags:
- court
- inmate
- corrections
- maine
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Maine DOC Corrections Search

> Maine's official adult-corrections lookup: is this person in Maine DOC custody or community supervision, and where?

## When to use
You have a `name` and want to know whether the subject is an adult resident (incarcerated) or community-corrections client under the Maine Department of Corrections. For a missing-persons workflow this both locates a subject in Maine custody/supervision and rules it in or out — one state-specific piece of the nationwide custody picture that aggregators like `[[vinelink]]` may not fully cover.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Maine DOC search (the old `www1.maine.gov/online/mdoc/search-and-deposit/` link now redirects to the current `apps1.web.maine.gov/online/correctionssearch/` app).
2. Search by resident `name`.
3. Read the record: name, MDOC identifier (`document-id`), and facility/supervision status/location.
4. Pivot: an MDOC ID and facility (`address`) confirm custody and location; a "community corrections" status reframes where the person actually is; for a full record, file the separate Public Criminal History Request.

## Inputs → Outputs
- **In:** `name`
- **Out:** resident `name`, MDOC `document-id`, facility/supervision `address`/status
- **Empty/negative result looks like:** no match — the person is not a current Maine DOC adult resident/client under that spelling. Note the service explicitly is NOT a complete criminal history and covers current Maine DOC involvement only; absence here doesn't rule out past or out-of-state custody.

## Gotchas & OpSec
- Scope is current Maine DOC adults only — not juveniles, not county jails (check those separately), not a full criminal history.
- Disambiguate common names carefully before acting on a record.
- OpSec: **passive**, official, anonymous.

## Overlaps ("do both")
- Pairs with `[[vinelink]]` and Maine county jail rosters — VINE aggregates broadly but the state DOC search is the authoritative source for Maine state custody; run both when Maine is in play.

## Trust & verifiability
`trust: trusted` — a first-party state corrections service; a hit is authoritative for current Maine DOC status, though it is deliberately not a complete criminal history.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | maine |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

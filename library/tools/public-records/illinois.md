---
id: illinois
name: Illinois DOC Inmate Search
description: Use when you have a `name` (or IDOC number) and want to locate someone in Illinois state prison custody — returns custody status/facility plus dob, physical-description, and image (photo).
url: https://www2.illinois.gov/idoc/offender/pages/inmatesearch.aspx
category: public-records
path:
- public-records
bestFor: Locating and confirming a person in Illinois Department of Corrections custody by name or IDOC number.
selectorsIn:
- name
selectorsOut:
- name
- dob
- physical-description
- image
status: live
pricing: free
costNote: Free public record search operated by the Illinois Department of Corrections; no account or payment.
opsec: passive
opsecNote: A read-only query against a government public-records site; the subject is not notified and no login is required. Ordinary passive browsing hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Illinois Department of Corrections individual-in-custody database; authoritative for IL state-prison custody.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- georgia
- vinelink
- bop-inmate-locator
- illinois-inmate-search
aliases:
- Illinois Department of Corrections inmate search
- IDOC offender search
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# Illinois DOC Inmate Search

> The Illinois Department of Corrections' public individual-in-custody locator — the authoritative "is this person in Illinois state prison, and where" lookup.

## When to use
A missing or sought person may be incarcerated in Illinois state custody. You have a `name` (or an IDOC number) and want to confirm custody, find the current facility, and pull identifying details — DOB/age, physical description, and a photo. A hit locates the person, corroborates identity, and can explain a sudden disappearance from normal life.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the IDOC inmate search (current endpoint: https://idoc.illinois.gov/offender/inmatesearch.html; the legacy www2.illinois.gov/idoc path redirects there).
2. Search by `name` — or by IDOC number for an exact match. Narrow common names with birth year.
3. Read the record: custody status and facility, IDOC number, DOB/age, physical description, photo, and offense/sentence.
4. Empty result → not currently in IDOC state custody (could be in a county jail, federal custody, or another state).
5. Pivot: confirmed custody + DOB feeds identity confirmation; register for release alerts on `[[vinelink]]`.

## Inputs → Outputs
- **In:** `name` (or IDOC number)
- **Out:** `name`, `dob`, `physical-description`, `image` (photo), current facility & sentence status
- **Empty/negative result looks like:** "no records found" — means not in Illinois *state prison* custody; check county jails (e.g. Cook County) and the federal BOP separately.

## Gotchas & OpSec
- Scope is Illinois **state** prisons — county jail detainees (including large Cook County Jail) and federal inmates are elsewhere.
- Data reflects IDOC records; confirm before treating as fact for consequential decisions.
- Fully passive; no login or CAPTCHA in the normal flow.

## Overlaps ("do both")
- Pairs with `[[vinelink]]` (custody status + release/transfer alerts across states) and `[[bop-inmate-locator]]` (federal) — run these together to cover the custody blind spots this state-only tool leaves. Same pattern as `[[georgia]]` for GA.

## Trust & verifiability
`trust: trusted` — first-party state government database, authoritative for IL state custody. Confirm details for anything legally consequential.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | illinois |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, physical-description, image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

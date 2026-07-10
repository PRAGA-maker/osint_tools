---
id: kansas
name: Kansas (KASPER)
description: Use when you have a `name` and want to check whether a subject is in the Kansas Department of Corrections population — returns offense history, supervision status, digital image, and KDOC ID.
url: https://kdocrepository.doc.ks.gov/kasper
category: public-records
path:
- public-records
bestFor: Confirming Kansas DOC incarceration/supervision status and offense history for a named person.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
- image
- physical-description
status: live
pricing: free
costNote: Free official public records service operated by the Kansas Department of Corrections; no account or payment.
opsec: passive
opsecNote: Passive — you query a state public-records repository, not the subject. The offender is not notified. Standard official-site logging applies; use a clean browser if you want to avoid attributing the query to yourself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: KASPER is the official public offender repository of the Kansas Department of Corrections — authoritative for KDOC-supervised persons, though it warns it is not a complete criminal-history source (consult KBI for that).
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- KASPER
- Kansas Adult Supervised Population Electronic Repository
- Kansas Department of Corrections offender search
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Kansas (KASPER)

> KASPER — the Kansas Adult Supervised Population Electronic Repository — is the Kansas Department of Corrections' official public search for offenders in KDOC custody or supervision.

## When to use
You have a `name` and a Kansas nexus (last known in KS, arrested there, family there) and need an authoritative check on whether the subject is currently or was recently in Kansas DOC custody, on parole, or under community supervision. This is the source of truth to confirm a lead surfaced by a commercial aggregator like `[[state-and-county-jail-inmate-locators]]`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://kdocrepository.doc.ks.gov/kasper in a browser.
2. Search by `name` (and, if available, KDOC number as `document-id`). Narrow with any known `dob`.
3. Open a matching record to read: conviction/offense descriptions, supervision status, sentencing, a digital photo (`image` / `physical-description`), and the KDOC ID.
4. Match carefully on name + photo + `dob` — Kansas is small but common names still collide.
5. Pivot: the photo feeds face/reverse-image tools; the facility gives a physical location; supervision status tells you whether the person is reachable via a parole office.

## Inputs → Outputs
- **In:** `name` (optionally KDOC `document-id`, `dob`)
- **Out:** offense history, supervision status, sentencing, `image`, `physical-description`, KDOC ID
- **Empty/negative result looks like:** "no records found" — meaning not in the KDOC-supervised population. This is NOT a full criminal history; a clean KASPER result doesn't rule out county-jail time or out-of-state records. Community-corrections probation data also has a stated cutoff of 21 Apr 2021.

## Gotchas & OpSec
- KASPER explicitly warns it is not a complete criminal-history repository (the KBI holds that) and that offenders "shall not be arrested solely on the basis of" its data. Treat it as status/location intelligence, not a rap sheet.
- Data updates daily and can lag reality between updates — a just-released person may still show in custody.
- No login/captcha; fully passive and free.
- Scope is Kansas only — for other states use their equivalent DOC search (e.g. `[[oregon-offender-search]]`).

## Overlaps ("do both")
- Confirms hits from `[[state-and-county-jail-inmate-locators]]` (aggregator → authoritative source).
- Parallel to `[[oregon-offender-search]]` and `[[sex-offender-search]]` for other jurisdictions/registries.

## Trust & verifiability
`trust: trusted` — it is the Kansas DOC's own public repository, authoritative for who is in KDOC custody/supervision. Its one caveat is scope: it covers KDOC only and is not a complete criminal history, so absence here isn't proof of a clean record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kansas |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id, image, physical-description |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: indiana-offender-database-search
name: Indiana Offender Database Search
description: Use when you have a `name` (or DOC number) and want to check Indiana incarceration status — returns offender ID, DOB, offense, facility and custody/release status.
url: https://www.in.gov/apps/indcorrection/ofs/ofs
category: public-records
path:
- public-records
bestFor: Confirming whether a person is or was in Indiana state custody and pulling their offender record.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
- physical-description
status: live
pricing: free
costNote: Free official Indiana Department of Correction public database; no account or payment.
opsec: passive
opsecNote: An official government records search — you query the IDOC database, not the subject, so nobody is notified. The site carries a disclaimer that republishers are responsible for accuracy. Use a sock-puppet browser as routine hygiene; the search itself is unremarkable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Indiana Department of Correction — a first-party, authoritative source for state incarceration records (subject to update lag for newly sentenced individuals).
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- IDOC Offender Search
- Indiana Department of Correction offender locator
tags:
- court
- inmate
- corrections
- indiana
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Indiana Offender Database Search

> Indiana's official offender locator — is this person in Indiana state custody, and what's their record?

## When to use
You have a `name` (or an IDOC number) and need to establish whether a subject is incarcerated, on supervised release, or previously held in the Indiana state prison system. Incarceration is a common explanation for someone going "missing," and a custody record confirms a person is alive, located, and dates their whereabouts — a high-value resolution in a missing-person workflow.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.in.gov/apps/indcorrection/ofs/ofs (redirects to offenderlocator.idoc.in.gov).
2. Search by last name, or first + last name; if you already have the IDOC/DOC number, search by that for a direct hit.
3. Review the candidate list and open the matching record.
4. Read the record: full legal `name` (and aliases), `dob`, IDOC offender `document-id`, offense(s), holding facility, and custody/release status; a `physical-description` and photo are often included.
5. Pivot: confirmed custody dates a whereabouts and closes the "missing" question; aliases/DOB feed cross-state offender and court searches (`[[minnesota]]`-style locators, national inmate search).

## Inputs → Outputs
- **In:** `name` (last, or first+last) or IDOC number
- **Out:** `name`/aliases, `dob`, offender `document-id`, offense, facility, custody/release status, `physical-description`
- **Empty/negative result looks like:** "no records found" — means not in *Indiana state* custody. It does not rule out county jail, federal (BOP), or other-state custody; newly sentenced people also lag before appearing.

## Gotchas & OpSec
- Scope is **Indiana state DOC only** — county jails and federal inmates are elsewhere (VINELink, county sheriffs, BOP). A blank result is not "never incarcerated."
- Common surnames return many hits; corroborate with DOB/photo before asserting a match.
- OpSec: **passive**, first-party government source; nothing leaks to the subject.

## Overlaps ("do both")
- Pairs with `[[minnesota]]` and other state offender locators, VINELink, and the federal BOP inmate locator — coverage is per-jurisdiction, so run the relevant states plus federal when you don't yet know where a person might be held.

## Trust & verifiability
`trust: trusted` — the authoritative Indiana DOC system. Records are official; note the site's own disclaimer on accuracy and the update lag for recent sentences.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | indiana-offender-database-search |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id, physical-description |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

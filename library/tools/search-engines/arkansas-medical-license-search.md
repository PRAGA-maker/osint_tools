---
id: arkansas-medical-license-search
name: Arkansas Medical License Search
description: Use when you have a `name` and want to verify an Arkansas physician's license — returns license `document-id`, status and practice `address`.
url: http://www.armedicalboard.org/public/verify/default.aspx
category: search-engines
path:
- search-engines
bestFor: Verifying whether a person holds an Arkansas medical license and its current status.
selectorsIn:
- name
selectorsOut:
- document-id
- address
status: live
pricing: free
costNote: Free public license-verification service run by the Arkansas State Medical Board; no account.
opsec: passive
opsecNote: A public licensing-board record check; the subject is not contacted. Queries may be logged by the state site, but this is open public-record data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Arkansas State Medical Board — the authoritative primary source for physician licensure in that state.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Arkansas State Medical Board verify
- armedicalboard.org
tags:
- toddington
- curated-directory
- license-verification
- professional-records
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Arkansas Medical License Search

> The Arkansas State Medical Board's public license-lookup — confirm that a named individual is (or was) a licensed physician in Arkansas, with their license number, status and practice location.

## When to use
You have a `name` (or a claim that someone is a doctor in Arkansas) and want to confirm licensure. Professional-license records are strong identity and location anchors: they tie a real person to a license number, a status (active/expired/disciplined), a specialty, and often a city or practice `address`. Useful for verifying an occupation claim, disambiguating people, or finding a current place tied to a licensed professional in a missing-persons or due-diligence context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the verification page at armedicalboard.org and open the license search.
2. Search by the physician's last/first `name` (or by license number if known).
3. Read the record: license `document-id`, status, license type/specialty, and city/practice `address` where shown.
4. Note any disciplinary/board-action flags, which can open further public records.
5. Pivot: for other states use that state's medical board (or a multi-state aggregator like the FSMB DocInfo); for non-physician professions use the relevant Arkansas licensing board.

## Inputs → Outputs
- **In:** `name` (or license number)
- **Out:** license `document-id`, status, specialty, city/practice `address`
- **Empty/negative result looks like:** no record — the person isn't licensed as a physician in Arkansas (they may be licensed elsewhere, in a different profession, or unlicensed). Absence is state- and profession-specific.

## Gotchas & OpSec
- OpSec: **passive** — public licensing record; nothing reaches the subject.
- Arkansas physicians only; other states and other professions have separate boards.
- Common names can collide; confirm with a second data point (specialty, city, license number) before attributing.

## Overlaps ("do both")
- Pairs with FSMB DocInfo (multi-state physician lookup) and other state medical boards — this is the Arkansas-authoritative source; the aggregators give breadth across states.

## Trust & verifiability
`trust: trusted` — a first-party state medical board system; its licensure records are the authoritative source for Arkansas and are directly citable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | arkansas-medical-license-search |
| category | search-engines |
| selectorsIn → selectorsOut | name → document-id, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

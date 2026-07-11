---
id: tfl-gov-uk
name: tfl.gov.uk Licence Checker
description: Use when you have a London taxi/private-hire driver badge or a vehicle plate and want to confirm the licence is valid — returns licence status for TfL-licensed drivers and vehicles.
url: https://tph.tfl.gov.uk/home/services/licence-checker
category: public-records
path:
- public-records
bestFor: Verifying whether a London taxi/PHV driver badge or vehicle licence number is genuine and currently valid.
selectorsIn:
- document-id
- vehicle-plate
selectorsOut:
- document-id
- employer-org
status: live
pricing: free
costNote: Free official Transport for London service; no account.
opsec: passive
opsecNote: An official TfL verification page that checks a licence number you already have; it does not notify the driver and returns only licence-status data, not personal contact details. Standard clean-browser hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Transport for London (TfL) Taxi & Private Hire — the licensing authority itself, so licence-status results are authoritative.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
aliases:
- TfL licence checker
- Taxi and Private Hire licence checker
tags:
- professionlicensing
- Profession & Licensing Sites
- london
- taxi
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# tfl.gov.uk Licence Checker

> Transport for London's official licence-checker — confirm whether a London taxi (black cab) or private-hire (minicab/Uber-type) driver badge or vehicle licence is genuine and in-date.

## When to use
You have a TfL driver badge number, licence number, or a vehicle licence/plate for a London taxi or private-hire vehicle and want to verify it's legitimate and currently valid. Useful to confirm a subject's claimed occupation as a London cab/PHV driver, to validate a vehicle a person is associated with, or as a safety/vetting check. Reach for it whenever a London taxi/PHV licence is part of the picture.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tph.tfl.gov.uk/home/services/licence-checker.
2. Choose the check type (driver vs. vehicle) and enter the badge/licence number or vehicle licence detail.
3. Read the result: whether the licence is valid/current and its status.
4. Cross-check the confirmed status against the subject's claim (occupation, the specific vehicle).
5. Pivot: a valid driver licence corroborates `employer-org`/occupation; a vehicle result ties a plate to a licensed PHV operator context.

## Inputs → Outputs
- **In:** `document-id` (driver badge/licence number) or `vehicle-plate`/vehicle licence
- **Out:** `document-id` (licence validity/status), `employer-org` (licensed driver/operator context)
- **Empty/negative result looks like:** "not found" / not valid — the number is wrong, lapsed, or not a TfL licence. That confirms the credential isn't valid *in London*; drivers licensed by other UK councils won't appear here (check that council).

## Gotchas & OpSec
- Human-in-the-loop: none.
- Scope is **London TfL licensing only** — private-hire licences issued by other UK local authorities are checked on those councils' sites, not here.
- Returns licence *status*, not the driver's personal contact details.
- OpSec: passive; the driver is not notified.

## Overlaps ("do both")
- Pairs with other UK council private-hire licensing checkers and DVLA vehicle checks — TfL covers London; other councils and DVLA cover the rest of the driver/vehicle picture.

## Trust & verifiability
`trust: trusted` — the licensing authority's own checker; licence-status results are authoritative for London taxi/PHV.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tfl-gov-uk |
| category | public-records |
| selectorsIn → selectorsOut | document-id, vehicle-plate → document-id, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

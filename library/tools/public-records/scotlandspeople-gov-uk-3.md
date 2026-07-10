---
id: scotlandspeople-gov-uk-3
name: scotlandspeople.gov.uk
description: Use when you have a `name` and want official Scottish vital records — births, marriages, deaths, divorces, censuses — returns `dob`/life dates, `associate` (family) and place/`address`.
url: https://www.scotlandspeople.gov.uk/search-records/statutory-records/stat_divorces
category: public-records
path:
- public-records
bestFor: Official Scottish statutory and historical records (BMD, divorces, censuses, wills) for genealogy and identity confirmation.
selectorsIn:
- name
selectorsOut:
- name
- dob
- associate
status: live
pricing: freemium
costNote: Free to register and search the record indexes; viewing a record image or ordering a certificate is pay-per-view (credits) or a per-certificate fee.
opsec: passive
opsecNote: Passive — you search an official government archive; no living subject is notified, and recent statutory records are restricted by closure periods to protect the living. An account is required; register with a sock-puppet identity for sensitive work. Purchases leave a billing trail.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official National Records of Scotland genealogy service; record data is authoritative (transcribed from statutory registers and censuses).
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: true
aliases:
- ScotlandsPeople
- National Records of Scotland
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- scotland
- vital-records
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# scotlandspeople.gov.uk

> The official National Records of Scotland archive online: search authoritative Scottish births, marriages, deaths, divorces, censuses and wills by name.

## When to use
You have a `name` with a Scottish connection and need authoritative vital-records evidence: a confirmed `dob`/life dates, marriage and family links (`associate`), divorce records, or census placements that tie a person to a household and place/`address`. Unlike crowd-sourced genealogy, this is the primary source — ideal for confirming identity, disambiguating same-name people, or tracing surviving family in a missing-persons case. (The linked page is the divorces index; the site covers all statutory records.)

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free account at https://www.scotlandspeople.gov.uk/ (needed to search).
2. Choose a record set — statutory births/marriages/deaths/divorces, censuses, church registers, wills — and search the `name` (add year/place to narrow).
3. Read the free index result (names, dates, reference); recent records are withheld under closure periods.
4. To see the full record image or a certificate, spend credits / order a certificate (pay-per-view).
5. Pivot: a confirmed `dob` disambiguates other records; family links feed `[[geneanet-org]]`/`[[192-uk]]`; places narrow local searches.

## Inputs → Outputs
- **In:** `name` (+ optional year/place)
- **Out:** confirmed `name`/spelling variants, `dob`/marriage/death dates, `associate` (spouse, parents, household), place/`address` from censuses
- **Empty/negative result looks like:** no index hit, or hits blocked by closure periods (recent births/marriages/deaths are restricted) — the event isn't in Scottish records, predates coverage, or is too recent to be open. Not proof of absence.

## Gotchas & OpSec
- Human-in-the-loop: **account-login** required to search; record images/certificates are pay-per-view.
- OpSec: **passive** — official archive; register with a puppet account; closure periods protect the living.
- Scotland-only. It's the authoritative source, but transcription errors exist — check the image, not just the index.

## Overlaps ("do both")
- Pairs with `[[geneanet-org]]` (broader European trees) and `[[192-uk]]` (current UK household) — ScotlandsPeople is the authoritative Scottish vital-records layer; the others add breadth and present-day data.

## Trust & verifiability
`trust: trusted` — first-party National Records of Scotland data. Authoritative; still verify by viewing the actual record image rather than relying on the index transcription alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scotlandspeople-gov-uk-3 |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |

---
id: tellmescotland-gov-uk
name: tellmescotland.gov.uk
description: Use when you have a Scottish `address`/`geolocation` and want the statutory public notices (planning, licensing, roadworks) attached to it — returns `address` + `name` of applicants/parties tied to those notices.
url: https://tellmescotland.gov.uk/home/
category: public-records
path:
- public-records
bestFor: Finding official public/statutory notices — planning, licensing, roads — for any place in Scotland.
selectorsIn:
- address
- geolocation
selectorsOut:
- address
- name
- employer-org
status: live
pricing: free
costNote: Free national public service, no payment. Registration is optional and only needed to set up email/SMS alerts for an area — searching and reading notices is open.
opsec: passive
opsecNote: You are searching a public government notices portal, not contacting anyone. Nothing is disclosed to the subject of a notice. Registering for alerts creates an account tied to your email — use a sock-puppet address if you don't want that association.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Scotland's official national public-notice portal, endorsed by the Scottish Government and run by the Improvement Service — the notices are authoritative statutory records.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- scotland-peoplescotland-gov-uk
aliases:
- Tell Me Scotland
- tellmescotland
tags:
- propertysites
- Property Related Sites
- public-notices
- scotland
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# tellmescotland.gov.uk

> Scotland's single national portal for statutory public information notices — planning applications, licensing, road closures — searchable by area and map.

## When to use
You have a Scottish `address` or `geolocation` and want the official record of what is happening (or has happened) at or around it: planning/property developments, licence applications (which name applicants and premises), road closures and traffic restrictions. For a missing-person or subject workup this surfaces an `address`-linked `name` (e.g. a licence holder, a development applicant) and confirms activity/occupancy at a location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tellmescotland.gov.uk (the home page).
2. Search by area/`address` or use the map of Scotland to click into a local-authority area.
3. Filter by notice type (planning, licensing, roads, general) and read individual notices — each carries the issuing council, dates, the premises/`address`, and often the applicant's `name` or `employer-org`.
4. Optionally register to receive text/email alerts for a specific area if you're monitoring an address over time.
5. Pivot: an applicant `name` feeds Scottish person/records lookups (e.g. `[[scotland-peoplescotland-gov-uk]]`); a premises licence links a person to a specific business `address`.

## Inputs → Outputs
- **In:** `address` / `geolocation` (a Scottish location or council area)
- **Out:** statutory notices carrying `address`, applicant/holder `name`, sometimes `employer-org`, plus dates
- **Empty/negative result looks like:** no notices returned for the area/date range — normal for a location with no recent statutory activity; it is not evidence about any individual.

## Gotchas & OpSec
- Human-in-the-loop: none for searching; only alert sign-up needs an account.
- OpSec: **passive** — a public-records portal, nothing reaches the subject. Alert registration ties an email to the watched area, so use a throwaway address.
- Coverage is Scotland only. Notices are time-bounded; older items move to the searchable archive.

## Overlaps ("do both")
- Pairs with `[[scotland-peoplescotland-gov-uk]]` (ScotlandsPeople) — this gives current statutory *notices* tied to a place, while ScotlandsPeople covers historical civil/vital records for people; together they bracket a Scottish subject's paper trail.

## Trust & verifiability
`trust: trusted` — an official Scottish Government-endorsed portal operated by the Improvement Service; the notices are primary statutory records, not scraped or crowd-sourced data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tellmescotland-gov-uk |
| category | public-records |
| selectorsIn → selectorsOut | address, geolocation → address, name, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

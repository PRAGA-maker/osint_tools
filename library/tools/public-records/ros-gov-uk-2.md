---
id: ros-gov-uk-2
name: ros.gov.uk (ScotLIS — Scotland's Land Information Service)
description: Use when you have a Scottish property `address` (postcode) and want the owner and price history — returns owner name, address, and document-id of title deeds.
url: https://scotlis.ros.gov.uk/
category: public-records
path:
- public-records
bestFor: Finding who owns a Scottish property, its sale price history, and title documents via Registers of Scotland's official land service.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- address
- employer-org
- name
status: live
pricing: freemium
costNote: Free to search by postcode/title number and view basic property/ownership and price-history summaries; purchasing full title deeds/plans (title sheet documents) incurs a per-document fee.
opsec: passive
opsecNote: Official government land registry — searching does not notify the owner and reveals only your IP to Registers of Scotland. Buying a document requires payment (attributable). No sock-puppet needed for the free search; use payment hygiene if purchasing.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Scottish government body (Registers of Scotland); the authoritative record of land ownership in Scotland.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- gov-uk-14
- gov-uk-9
aliases:
- ScotLIS
- Registers of Scotland
- scotlis.ros.gov.uk
tags:
- propertysites
- Property Related Sites
- land-registry
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# ros.gov.uk (ScotLIS — Scotland's Land Information Service)

> Registers of Scotland's official portal for finding who owns a Scottish property, what it sold for, and its title documents — the Scottish counterpart to HM Land Registry.

## When to use
You have a Scottish property `address` (or postcode/title number) and need to establish ownership, sale history, or title details — for example placing a subject at an address, identifying a co-owner (`associate`), or confirming a corporate (`employer-org`) proprietor. Because Scotland has its own land registry separate from England & Wales, ScotLIS is the correct source north of the border.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://scotlis.ros.gov.uk/ and search by postcode, address, or title number (a map search is also available).
2. Select the specific property.
3. Read the free summary: whether it's on the Land Register, the current owner, and price/sale history.
4. If you need the authoritative detail, buy the title sheet/plan documents (per-document fee) — these carry the registered proprietor and deed references (`document-id`).
5. Pivot: an owner `name` feeds people-search; a sale date anchors a timeline; a corporate owner feeds Companies House.

## Inputs → Outputs
- **In:** property `address`/postcode or title number (or a `name`/`employer-org` to confirm against a property)
- **Out:** current owner `name`, registered `address`, price/sale history, title deed references (`document-id`), corporate proprietor (`employer-org`)
- **Empty/negative result looks like:** the property isn't yet on the Land Register (Scotland is mid-transition from the older Sasine register) or no match for the search — some properties won't show an owner online; that's a registration gap, not proof of no owner.

## Gotchas & OpSec
- **Scotland only** — use [[gov-uk-9]]/[[gov-uk-14]] (HM Land Registry) for England & Wales, and the separate NI registry for Northern Ireland.
- Coverage is incomplete during the ongoing migration from the Sasine register to the Land Register — an absent property may simply not be migrated yet.
- Human-in-the-loop: full deeds are behind a paid, per-document wall; the free tier gives ownership/price summaries.
- OpSec: passive — the owner isn't notified by a search.

## Overlaps ("do both")
- Pairs with [[gov-uk-9]] (current E&W register) and [[gov-uk-14]] (historical E&W editions) — ScotLIS is the Scottish equivalent; choose by jurisdiction.

## Trust & verifiability
`trust: trusted` — first-party Registers of Scotland data; the authoritative record of Scottish land ownership. Free summaries are reliable; purchased title sheets are the definitive legal record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ros-gov-uk-2 |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → address, employer-org, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |

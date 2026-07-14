---
id: usrealtyrecords-com
name: usrealtyrecords.com
description: Use when you have a US `address` (or owner `name`) and want property ownership, value, sale history and possible owner contact info — returns owner name, address history and associate leads.
url: https://usrealtyrecords.com/
category: public-records
path:
- public-records
bestFor: US property lookups — ownership, value, tax, and sale history for an address (118M+ properties).
selectorsIn:
- address
- name
selectorsOut:
- name
- address
- associate
status: live
pricing: freemium
costNote: Free search/teaser over 118M+ US properties; the full report (ownership records, contact info, tax and sale history) is a paid product. Treat detailed owner data as paywalled.
opsec: passive
opsecNote: The subject is not notified, but you are querying a commercial data broker that logs searches and upsells. Use a sock-puppet session; never enter your own details.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial property-data aggregator; ownership and contact fields are broker-sourced and can be stale or misattributed, so corroborate against the county assessor/recorder.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- US Realty Records
- usrealtyrecords.com
tags:
- propertysites
- Property Related Sites
- property-records
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# usrealtyrecords.com

> A US property-records aggregator: search an address (118M+ properties) for its value, tax, sale history, and current/past owners — with possible owner contact info in the paid report.

## When to use
You have a US `address` and want to know who owns it, its value and sale history, and prior owners — or you have an owner `name` and want to tie them to property. Strong for linking a person to a physical `address`, establishing an ownership timeline, and surfacing prior owners/occupants (`associate` leads) around a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://usrealtyrecords.com/ in a sock-puppet browser.
2. Search primarily by street address (city/state/ZIP); the interface is address-first.
3. Read the free teaser: property characteristics, value, and whether ownership/history data exists.
4. Treat the full report (current/past owners, contact info, tax and sale records) as a paid product — decide whether to pay or corroborate via the free county assessor/recorder.
5. Pivot: an owner `name` feeds people-search; prior owners are `associate` leads; the sale timeline anchors when a subject lived there.

## Inputs → Outputs
- **In:** US `address` (or owner `name`)
- **Out:** owner `name`, `address`/property history, prior owners (`associate`), value/tax/sale records
- **Empty/negative result looks like:** no property match, or only an upsell with no distinguishing teaser — meaning no record in this aggregator, not that the address doesn't exist; verify against the county.

## Gotchas & OpSec
- Paywall: meaningful owner/contact detail is a paid report.
- Broker-quality: ownership can lag deed transfers; the authoritative source is the county assessor/recorder — corroborate there for anything consequential.
- Not FCRA-permissible for tenant/employment/credit use.

## Overlaps ("do both")
- Pairs with `[[find-people-search-us]]`: property records tie a name to an address and prior owners, while people-search adds phones, relatives, and cross-state history.

## Trust & verifiability
`trust: unverified` — a commercial aggregator; every owner/contact field is a lead to confirm against the county's primary property records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | usrealtyrecords-com |
| category | public-records |
| selectorsIn → selectorsOut | address, name → name, address, associate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |

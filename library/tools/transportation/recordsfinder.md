---
id: recordsfinder
name: RecordsFinder
description: Use when you have a `name`, `phone`, `address`, `vehicle-plate` or `vin` and want a US public-records aggregate — returns names, addresses, contact info and vehicle links.
url: https://recordsfinder.com/
category: transportation
path:
- transportation
bestFor: US public-records aggregator spanning people, phone, address, and vehicle (plate/VIN) lookups in one search.
selectorsIn:
- vehicle-plate
- vin
- name
- phone
- address
selectorsOut:
- name
- address
- phone
- vehicle-plate
status: live
pricing: freemium
costNote: Free to start a search and see teaser hits; viewing a full report requires buying a report or a paid membership. Not FCRA-compliant — not for employment/tenant/credit decisions.
opsec: passive
opsecNote: Searches run against the broker's aggregated data, not against the subject, so the person is not notified. Use a sock-puppet email/payment if you register, since the account ties the searches to you.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial data broker; coverage and accuracy vary by jurisdiction and records are frequently stale or mismatched. Corroborate every hit against a primary source.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- recordsfinder-people-search-ca
tags:
- plate
- vin
- people-search
- records
source: inteltechniques-tools
lastVerified: '2026-07-19'
enrichment: full
---

# RecordsFinder

> A broad US data-broker aggregator that takes almost any selector — name, phone, address, license plate, or VIN — and returns a bundled report of associated people, addresses, contacts and vehicles.

## When to use
You have one identifier for a US subject and want a fast, wide net: current/past addresses, phone numbers, relatives, and — usefully for vehicle work — a plate-to-owner or VIN lookup. Best as an early-stage aggregator that suggests leads to verify, especially when you already have a `vehicle-plate` or `vin` and want to connect it to a `name` and `address`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://recordsfinder.com/ and choose the search type (People, Phone, Address, VIN, or License Plate).
2. Enter what you have — e.g. a plate + state, or first/last name + city/state.
3. Review the free teaser results (matched name, rough location, record categories present).
4. To see the full report you must buy a report or a membership; register with a sock-puppet identity and disposable payment if you proceed.
5. Read the report for addresses, phones, relatives/associates, and any vehicle links.
6. Pivot: treat each field as a lead — confirm addresses via county records, plates/VINs via a state DMV or dedicated vehicle tool, and relatives via a second people-search.

## Inputs → Outputs
- **In:** `name`, `phone`, `address`, `vehicle-plate`, or `vin`
- **Out:** `name`, `address`, `phone`, relatives/`associate`, and vehicle records where available
- **Empty/negative result looks like:** "no records found" or a report with sparse, generic entries. Broker data is patchy; an empty result here does not mean no public record exists — try another aggregator or the primary source.

## Gotchas & OpSec
- Paywall: the useful detail is behind a purchase; the free layer is a teaser. Budget for a report or use a fully-free source first.
- Accuracy is uneven — brokers mix records for people with similar names and carry stale addresses. Never treat a single RecordsFinder hit as confirmation.
- Legally NOT an FCRA consumer-reporting agency: do not use for hiring, tenant, credit, or insurance decisions.
- OpSec: passive toward the subject, but any account/payment you create is logged and tied to you.

## Overlaps ("do both")
- Pairs with `[[recordsfinder-people-search-ca]]` and other people-search aggregators — run the same selector through two brokers; where they agree, confidence rises; where they differ, you've found records to reconcile.

## Trust & verifiability
`trust: community` — a commercial aggregator with no editorial guarantee; use it to generate leads, then verify each against an authoritative primary record (county, court, DMV) before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | recordsfinder |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate, vin, name, phone, address → name, address, phone, vehicle-plate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |

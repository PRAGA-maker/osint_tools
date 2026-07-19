---
id: civil-aviation-authority-aircraft-register-united-kingdom
name: Civil Aviation Authority Aircraft Register (United Kingdom)
description: Use when you have a UK aircraft registration mark (`vehicle-plate`, e.g. G-ABCD) and want the registered owner — returns owner `name` and `address`.
url: https://www.caa.co.uk/aircraft-register/g-info/search-g-info/
category: transportation
path:
- transportation
bestFor: Turning a UK "G-" aircraft registration mark into the registered owner's name and address via the official CAA G-INFO register.
selectorsIn:
- vehicle-plate
selectorsOut:
- name
- address
status: live
pricing: free
costNote: Free public G-INFO search. Bulk data extracts / data queries are a paid CAA service, but single-mark lookups are free with no account.
opsec: passive
opsecNote: You query the CAA's own public register, not the owner; no one is notified. The register exists by law for public inspection, so use is legitimate and non-alerting.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official UK Civil Aviation Authority register, maintained by law. Owner details are as supplied to the CAA; note the register records the registered owner, not necessarily legal title.
missingPersonsRelevance: medium
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- G-INFO
- CAA aircraft register
- UK aircraft register
tags:
- toddington
- curated-directory
- specialty-search
- aircraft
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Civil Aviation Authority Aircraft Register (United Kingdom)

> The UK's official G-INFO register — one of the few vehicle registers that publishes owner name **and** address, searchable free by registration mark.

## When to use
You have a UK aircraft registration mark (the "G-" tail number, e.g. `G-ABCD`) from a photo, flight-tracking site, or document, and you want the registered owner. Unlike the UK car register, aircraft ownership is public by statute, so this can yield a real `name` and `address` — a strong pivot when a subject is linked to a private aircraft.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.caa.co.uk/aircraft-register/g-info/search-g-info/.
2. Enter the registration mark (with or without the `G-` prefix), or search by aircraft type/manufacturer if you only have that.
3. Open the matching record and read: registered owner `name`, owner `address`, aircraft type/serial, and registration dates.
4. Pivot: run the owner name/address through people-search and company records; if the owner is a trust or company, follow it into a corporate registry to reach the humans behind it.

## Inputs → Outputs
- **In:** `vehicle-plate` (UK aircraft registration mark)
- **Out:** owner `name` and `address`, plus aircraft make/model/serial and dates
- **Empty/negative result looks like:** "no results" — the mark is unassigned, cancelled, or you mistyped it; it may also be registered to a company/trust rather than a person (still useful as a corporate lead).

## Gotchas & OpSec
- The register shows the **registered owner**, which the CAA itself notes is not proof of legal ownership — ownership can be via a trust or leasing company.
- Marks get re-used over time; confirm the aircraft type matches your source before trusting an owner match.
- OpSec: fully passive; the register is a statutory public record.

## Overlaps ("do both")
- Pairs with flight-tracking (ADS-B) sites that give you the mark from a live/near-live flight, and with corporate-registry tools when the owner turns out to be a company or trust.

## Trust & verifiability
`trust: trusted` — an official government register maintained under statute. Data quality depends on owners keeping the CAA updated; corroborate the address against other records if it is action-critical.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | civil-aviation-authority-aircraft-register-united-kingdom |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate → name, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

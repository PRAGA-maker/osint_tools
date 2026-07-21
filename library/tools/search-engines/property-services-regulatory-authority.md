---
id: property-services-regulatory-authority
name: Property Services Regulatory Authority (Ireland)
description: Use when you have an Irish `name` or `address` and want the PSRA's public registers — returns licensed estate-agent/auctioneer details (`name`, licence, location) and residential property sale prices/dates by `address`.
url: https://www.psr.ie
category: search-engines
path:
- search-engines
bestFor: Ireland's official registers — licensed property-services providers plus the residential property price register (sale price/date by address).
selectorsIn:
- name
- address
selectorsOut:
- name
- address
status: live
pricing: free
costNote: Free public registers; no account or payment. Data is viewable online and downloadable (PDF/Excel).
opsec: passive
opsecNote: Official government registers queried directly; nothing is exposed to any individual and no login is used. Ordinary web access.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: PSRA is Ireland's statutory regulator for the property-services sector; the registers are official records sourced from licensing data and Revenue stamp-duty declarations.
missingPersonsRelevance: medium
coverage:
- ie
auth: none
api: false
localInstall: false
registration: false
aliases:
- PSRA
- psr.ie
- Residential Property Price Register
tags:
- toddington
- curated-directory
- specialty-search
- ireland
- property-records
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Property Services Regulatory Authority (Ireland)

> Ireland's property regulator publishes two OSINT-useful public registers: who is a licensed estate agent/auctioneer, and the price/date/address of every residential property sold since 2010.

## When to use
Your subject has an Irish property or property-industry connection. Use the **Register of Licensed Property Services Providers** to confirm whether a `name`/company is a licensed auctioneer, estate agent or letting agent (with licence number, type and location), and the **Residential Property Price Register** to look up an `address` and see the sale date and price of that property since 1 Jan 2010 — corroborating a property transaction, a timeline, or a claimed occupation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.psr.ie and go to "PSRA Registers."
2. For an agent/auctioneer: open the **Register of Licensed Property Services Providers**, search by name, licence number or location (updated weekly; downloadable as PDF/Excel).
3. For a property: open the **Residential Property Price Register**, filter by county/address/date, and read the sale date, price and address for each transaction (there's also a Commercial Lease Register).
4. Read the output: licensee records confirm professional status and location; price-register rows confirm a sale occurred at an address on a date.
5. Pivot: a confirmed sale date/price at an `address` anchors a timeline and can corroborate residency; a licensee record links a `name` to a firm and location for further people-search.

## Inputs → Outputs
- **In:** `name` (or company/licence number), or an `address`/county
- **Out:** licensed-provider `name` + licence/location, and residential sale `address` + date + price
- **Empty/negative result looks like:** no licensee match (the person isn't a PSRA-licensed provider) or no price-register row for an address (no residential sale there since 2010, or the address is formatted differently — try the street/area). The price register lists the *property and sale*, not the buyer's name.

## Gotchas & OpSec
- The **price register names the property, not the purchaser** — it confirms a sale, not who bought it; don't infer ownership identity from it alone.
- Address strings are as declared to Revenue and can be inconsistent; search broadly (street, area) before concluding "no record."
- OpSec: **passive** — official registers, nothing exposed to any person.

## Overlaps ("do both")
- Pairs with Irish land/property registry and general people-search tools — PSRA confirms the *sale event* and *agent licensing*; a land registry links the property to a named owner.

## Trust & verifiability
`trust: trusted` — the PSRA is Ireland's statutory property-services regulator and these are official registers (licensing data; Revenue stamp-duty declarations). Records are authoritative for what they cover, updated weekly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | property-services-regulatory-authority |
| category | search-engines |
| selectorsIn → selectorsOut | name, address → name, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

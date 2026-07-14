---
id: residential
name: VOA Council Tax Band Check
description: Use when you have a UK `address` (postcode) and want to confirm a dwelling exists and read its council tax band as a rough property-value / occupancy signal — returns address-level band data.
url: https://www.gov.uk/council-tax-bands
category: public-records
path:
- public-records
bestFor: Confirming a specific England/Wales dwelling exists at an address and reading its council tax band.
selectorsIn:
- address
selectorsOut:
- address
status: live
pricing: free
costNote: Free UK government service (Valuation Office Agency); no account or payment required.
opsec: passive
opsecNote: You query a government database of properties, not people. The lookup is anonymous, server-side, and never notifies any occupant. Standard clean-browser hygiene is enough; no sock puppet needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Valuation Office Agency (part of HMRC); this is the authoritative source of council tax bands for England and Wales.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Valuation Office Agency council tax band search
- VOA band check
- voa.gov.uk council tax
tags:
- propertysites
- Property Related Sites
- uk
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# VOA Council Tax Band Check

> The UK government's authoritative council tax band lookup: does a dwelling exist at this address, and what band (rough value tier) is it?

## When to use
You have a UK `address` or postcode (England or Wales) and want to (a) confirm that a distinct dwelling is registered at it, and (b) read its council tax band as a coarse proxy for property size/value. Useful for validating an address a subject supplied, spotting whether a "flat" is really a subdivided HMO (multiple bands at one postcode), or building a picture of a person's likely housing circumstances. Note: the legacy `voa.gov.uk/cti/InitS.asp` endpoint has been retired; the live service is the gov.uk council-tax-bands page.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.gov.uk/council-tax-bands and follow through to the "Check your Council Tax band" service (`tax.service.gov.uk/check-council-tax-band/search`).
2. Enter the target `address` or postcode.
3. Read the returned list of every property in that postcode, each with its band (A–H in England, A–I in Wales) and full address line.
4. Pivot: multiple sub-addresses at one postcode reveal flat/annex subdivisions; the band hints at property scale. Cross-reference occupant identity via `[[scotland-landlord-search]]` (Scotland) or electoral-roll / people-search tools.

## Inputs → Outputs
- **In:** `address` (postcode or full UK address, England & Wales only)
- **Out:** confirmed dwelling `address` lines plus council tax band per property
- **Empty/negative result looks like:** "We couldn't find that postcode" or no properties listed — the address may be in Scotland (use the SAA instead), be a new/unbanded build, or not exist.

## Gotchas & OpSec
- Coverage is England and Wales only. Scotland uses the separate Scottish Assessors Association (saa.gov.uk); Northern Ireland uses LPS.
- It returns bands and addresses, **not** occupant names — never treat a band lookup as identifying who lives there.
- OpSec: passive and anonymous; nothing is sent to the property or its occupants.

## Overlaps ("do both")
- Pairs with `[[scotland-landlord-search]]` — that covers Scottish rental ownership by postcode where VOA does not reach, and adds a landlord/contact name this service lacks.

## Trust & verifiability
`trust: trusted` — first-party HMRC/VOA data; it is the definitive council-tax-band register for England and Wales.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | residential |
| category | public-records |
| selectorsIn → selectorsOut | address → address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

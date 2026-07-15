---
id: gov-uk-15
name: GOV.UK Find an Energy Certificate
description: Use when you have a UK `address` (or postcode) and want to confirm a property exists, see its dwelling characteristics, and date when it was last sold/let/assessed — returns property `address` details and assessment dates.
url: https://www.gov.uk/find-energy-certificate
category: public-records
path:
- public-records
bestFor: Confirming a UK property at an address and dating when an EPC was lodged (a proxy for a recent sale/tenancy).
selectorsIn:
- address
selectorsOut:
- address
status: live
pricing: free
costNote: Free UK government register; no account or payment required.
opsec: passive
opsecNote: You query a public government register about a property, not about the target directly — nothing is sent to the subject. Ordinary web-logging by GOV.UK only; a sock-puppet browser/IP is prudent but not essential.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party UK government service (Department for Levelling Up / MHCLG), drawing on the official EPC register — authoritative, not a third-party scraper.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- EPC register
- Energy Performance Certificate search
- find-energy-certificate
tags:
- propertysites
- Property Related Sites
- uk
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# GOV.UK Find an Energy Certificate

> The official UK register of Energy Performance Certificates, usable to confirm a property at an address and to date when it was last sold, let, or assessed.

## When to use
You have a UK `address` or postcode tied to a subject and want to (a) confirm the property physically exists and normalise its exact address, and (b) read the lodged EPC — whose lodgement date is a proxy for a recent sale or new tenancy, and whose contents (property type, floor area, number of rooms/heated area) describe the dwelling. An EPC dated shortly before the subject appears at that address helps corroborate a move-in timeline.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.gov.uk/find-energy-certificate.
2. Choose "Domestic" (homes) or "Non-domestic" (business/public buildings) as appropriate.
3. Search by postcode, then pick the exact property from the list; or search by certificate number if you already have one.
4. Read the certificate: lodgement date and validity (EPCs last 10 years), property type, built form, total floor area, number of habitable rooms, and heating/energy details.
5. Pivot: the lodgement date narrows a sale/let window (cross-check with Land Registry / `[[gov-uk]]` property tools); the floor area and room count give a physical picture of the dwelling.

## Inputs → Outputs
- **In:** `address` (or postcode / certificate number)
- **Out:** confirmed/normalised `address`, EPC lodgement + expiry dates, dwelling characteristics (type, floor area, rooms)
- **Empty/negative result looks like:** "No results" for the postcode, or the specific property has no lodged certificate — this is common for homes not sold or let since ~2008, so absence is not proof the address is fake.

## Gotchas & OpSec
- Coverage is England, Wales and Northern Ireland only; **Scotland has a separate register** (Scottish EPC Register).
- No occupant names — EPCs describe the building, never who lives there. Do not infer identity from an EPC alone.
- OpSec: passive; you query a property register, not the subject, so there is no notification risk.

## Overlaps ("do both")
- Pairs with UK land/property lookups such as `[[gov-uk]]` and Land Registry price-paid data — the EPC dates and describes the dwelling while those confirm ownership and sale price.

## Trust & verifiability
`trust: trusted` — it is the UK government's own EPC register, so the property data is authoritative; the only limitation is coverage gaps for properties never sold or let recently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gov-uk-15 |
| category | public-records |
| selectorsIn → selectorsOut | address → address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
</invoke>

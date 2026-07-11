---
id: mycounciltax-org-uk
name: mycounciltax.org.uk
description: Use when you have a UK `address`/postcode and want the Council Tax band for properties there — returns the band per property (a proxy for property value/size) and street-level `address` context.
url: http://www.mycounciltax.org.uk/content/index
category: public-records
path:
- public-records
bestFor: Looking up Council Tax bands for UK addresses by postcode (a rough property-value proxy).
selectorsIn:
- address
selectorsOut:
- address
status: live
pricing: free
costNote: Free to search by postcode. No account or payment. (Underlying band data is the public VOA/Scottish Assessors valuation banding.)
opsec: passive
opsecNote: You look up public property banding by postcode; no person is queried and nothing reaches any occupant. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party front-end over the public Council Tax valuation bands. Band data itself is official; this site is a convenience layer, so confirm a specific band on the official VOA/Scottish Assessors site if it matters.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- gov-uk-council-tax-band
- companies-house
aliases:
- My Council Tax
- mycounciltax.org.uk
tags:
- propertysites
- Property Related Sites
- council-tax
- uk
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# mycounciltax.org.uk

> A postcode lookup for UK Council Tax bands — see the tax band (A–H, a proxy for a property's relative value) for the addresses on a street.

## When to use
You have a UK `address` or postcode tied to a subject and want quick context about the property: its Council Tax band, which reflects the property's assessed value bracket and, loosely, its size/type. Handy for gauging a subject's likely circumstances at an address, distinguishing properties on a street, and enriching a location — though it returns property banding, not the occupant's identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.mycounciltax.org.uk/content/index.
2. Enter the target's full `address`/postcode.
3. Read the returned Council Tax band(s) for the property/street, plus any band/discount/exemption context.
4. Treat the band as a value/size proxy; for the authoritative band, confirm on the official VOA (England & Wales) or Scottish Assessors service.
5. Pivot: property context supports an address workup; combine with Land Registry/company records (`[[companies-house]]`) to link the address to owners/entities (which this tool does not provide).

## Inputs → Outputs
- **In:** `address` / postcode (UK)
- **Out:** Council Tax band per property (a value/size proxy), street-level `address` context
- **Empty/negative result looks like:** no band returned — the postcode is mistyped, the property is new/unbanded, or not in the dataset. It tells you nothing about who lives there.

## Gotchas & OpSec
- Human-in-the-loop: none; a postcode lookup.
- OpSec: **passive** — public property data; no occupant is queried.
- It returns *banding only* — no owner or occupant identity. Bands are a coarse value proxy, not an exact valuation, and this is a third-party mirror, so verify important bands on the official service.

## Overlaps ("do both")
- Pairs with the official `[[gov-uk-council-tax-band]]` service (authoritative bands) and property/ownership sources like `[[companies-house]]` / Land Registry — this gives quick band context, the others give the authoritative band and the ownership link it lacks.

## Trust & verifiability
`trust: community` — a convenient front-end over official band data. The bands originate from the valuation authorities (reliable), but confirm a specific property's band on the official VOA/Scottish Assessors site before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mycounciltax-org-uk |
| category | public-records |
| selectorsIn → selectorsOut | address → address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

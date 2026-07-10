---
id: royalmail-com
name: royalmail.com
description: Use when you have a UK `address` fragment or postcode and want to resolve the full, canonical postal address (or the postcode for an address) — returns the authoritative PAF® `address`.
url: https://www.royalmail.com/postcode-finder
category: public-records
path:
- public-records
bestFor: Resolving/normalising a UK address against the official Postcode Address File (postcode ↔ full address).
selectorsIn:
- address
selectorsOut:
- address
status: live
pricing: free
costNote: Free public postcode/address lookup from Royal Mail; free tier is limited to a modest number of lookups before it prompts for a paid PAF® product.
opsec: passive
opsecNote: A directory read against Royal Mail's address file. You submit an address/postcode, not anything identifying about your subject beyond where they may live; Royal Mail cannot tie the query to a person. Use a clean session if doing many lookups.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Royal Mail using the official Postcode Address File (PAF®), regulated by Ofcom — the authoritative source of truth for UK postal addresses.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- zoopla-co-uk
aliases:
- Royal Mail Postcode Finder
- PAF lookup
tags:
- propertysites
- Property Related Sites
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# royalmail.com

> Royal Mail's official Postcode Finder — the authoritative way to normalise or complete a UK address against the Postcode Address File (PAF®).

## When to use
You have a partial UK `address` (a street + town, a building name, or just a postcode) and need the exact, canonical form: the full delivery address, the correct postcode, or the list of properties on a postcode. Use it to confirm an address a subject gave is real, to standardise an address before feeding it to property/people-search tools, or to enumerate the numbered/named properties at a postcode.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.royalmail.com/postcode-finder.
2. Type part of an `address` or a postcode to begin.
3. Read the result: the tool resolves bidirectionally — postcode → the addresses it covers, or address fragment → the matching full address(es), including alternate forms (e.g. a property with both a name and a number).
4. Pivot: a confirmed full address feeds property tools like `[[zoopla-co-uk]]`, electoral-roll / people-search, and mapping.

## Inputs → Outputs
- **In:** UK `address` fragment or postcode
- **Out:** canonical full `address`(es) and postcode from PAF®
- **Empty/negative result looks like:** "address not found" — usually a typo, or a newly built/converted property not yet in PAF. A non-match is not proof the address is fake; try alternate spellings or the street rather than the building name.

## Gotchas & OpSec
- Free tier caps the number of lookups before pushing a paid PAF® product; for bulk work you would need a licensed data product.
- Newly built or recently converted properties may lag the database.
- OpSec: **passive** — an address-directory read, not a query about a person.

## Overlaps ("do both")
- Pairs with `[[zoopla-co-uk]]` and other UK property sites — Royal Mail gives you the authoritative address string, property portals then attach sale history, valuation, and occupancy signals to it.

## Trust & verifiability
`trust: trusted` — first-party Royal Mail data drawn from the Ofcom-regulated PAF®; the canonical source for UK postal addressing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | royalmail-com |
| category | public-records |
| selectorsIn → selectorsOut | address → address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

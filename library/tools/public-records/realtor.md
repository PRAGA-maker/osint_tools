---
id: realtor
name: Realtor
description: Use when you have an `address` (or an agent `name`) and want property details, listing history, and the listing agent — returns `address`, `name`, `geolocation`.
url: https://www.realtor.com/
category: public-records
path:
- public-records
bestFor: Looking up a US property's listing/sale history, features, and associated agent from an address.
selectorsIn:
- address
- name
selectorsOut:
- address
- name
- geolocation
status: live
pricing: freemium
costNote: Free to browse listings, property pages, and agent profiles; no account required for the core lookups.
opsec: passive
opsecNote: Browsing listing pages is passive and reveals nothing to the property's occupant. Avoid using the "contact agent" / tour-request forms, which send your details to a real agent and create a record.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Move, Inc. (News Corp) and powered by MLS data; listing facts are authoritative, though owner identity is inferred, not stated.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- realtor-com-united-states
aliases:
- realtor.com
tags:
- real-estate
- property-records
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Realtor

> One of the major US real-estate portals, backed by MLS feeds — turn an `address` into a property's listing history, features, and the agent who represents it.

## When to use
You have an `address` associated with your subject and want to characterize the property: is it currently for sale or rent, what did it last sell for and when, how many beds/baths, and who is the listing agent. Or you have an agent `name` and want their active listings and contact area. In a missing-persons context this corroborates a residence, reveals whether the subject may be moving (an active listing), and produces agent leads who may know the occupants.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.realtor.com/.
2. Enter the target `address` in the search bar (or search an agent `name`).
3. Open the property page: read status (for-sale/off-market/sold), price and listing/sale history, photos, and the listed agent.
4. Read the output: an active listing plus agent contact; an off-market page still shows last-sale data and property `geolocation`.
5. Pivot: the map pin refines `geolocation`; the listing agent is a human lead; sale-history dates cross-check tenure. Feed the address into county assessor/deed records for the actual owner `name`.

## Inputs → Outputs
- **In:** `address` (or agent `name`)
- **Out:** property `address`/details, listing agent `name`, map `geolocation`
- **Empty/negative result looks like:** "we couldn't find that address" or an off-market page with only sparse public data — the property may never have been MLS-listed; not proof it doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: none for lookups; do not submit tour/contact forms, which alert a live agent and log your identity.
- OpSec: passive. Realtor.com does not publish the current owner's name — that comes from assessor/deed records, so don't overstate a "match."
- US-only coverage; listing photos can be years old.

## Overlaps ("do both")
- Pairs with county assessor/deed and Zillow-style tools — Realtor.com gives listing/agent context, while public land records give the legal owner `name`. Do both to move from "who's selling it" to "who owns it."

## Trust & verifiability
`trust: trusted` — a major portal fed by MLS data, so property facts are reliable; just remember it infers nothing about the current occupant's identity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | realtor |
| category | public-records |
| selectorsIn → selectorsOut | address, name → address, name, geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

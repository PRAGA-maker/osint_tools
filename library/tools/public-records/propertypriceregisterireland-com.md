---
id: propertypriceregisterireland-com
name: Property Price Register Ireland
description: Use when you have an Irish `address` (or area) and want to confirm a residential sale — date and price — at that property — returns address plus the transaction date and amount.
url: https://propertypriceregisterireland.com/
category: public-records
path:
- public-records
bestFor: Confirming when an Irish residential property sold and for how much, as a timeline/ownership-change signal.
selectorsIn:
- address
selectorsOut:
- address
status: live
pricing: free
costNote: Free to search; a cleaner front-end over the official Residential Property Price Register data (PSRA).
opsec: passive
opsecNote: Public transaction records; searching does not identify or notify anyone. Only your IP touches the site. Note the register lists no buyer/seller names — only address, date, and price.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party mirror/search UI over Ireland's official Residential Property Price Register (an authoritative government dataset); the underlying data is authoritative, the presentation is community-run.
missingPersonsRelevance: high
coverage:
- ie
auth: none
api: false
localInstall: false
registration: false
aliases:
- PPR Ireland
- Irish Property Price Register
- propertypriceregisterireland.com
tags:
- propertysites
- Property Related Sites
- ireland
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Property Price Register Ireland

> A searchable front-end over Ireland's official residential property sales register — confirms that a property changed hands, when, and for how much.

## When to use
You have an Irish residential `address` (or an area) and want to establish whether and when it was bought or sold, and at what price. Because the register records the sale date and amount, it is useful for building an occupancy/ownership-change timeline around a subject — e.g. corroborating that a person moved to or from an address around a certain date. It does **not** name buyers or sellers, so use it for the transaction fact, not to identify a person directly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://propertypriceregisterireland.com/.
2. Search by `address`/street/town, and optionally filter by county, date range, price range, and new-build vs. second-hand.
3. Read the matching record(s): full property `address`, the **sale date**, and the **price paid**.
4. Pivot: the sale date anchors a timeline; cross-reference the address with electoral roll, planning, and people-search sources to attach names (which the register itself omits).

## Inputs → Outputs
- **In:** `address` (or area, Ireland)
- **Out:** confirmed `address` with sale date and price paid
- **Empty/negative result looks like:** no rows for the address — the property may not have sold in the register's coverage window (the PPR starts in 2010), not that the address is wrong.

## Gotchas & OpSec
- **No names:** Ireland's PPR deliberately excludes buyer/seller identities — do not expect person names here.
- Coverage begins in 2010; older sales aren't listed.
- This is a third-party UI; for disputes verify against the official PSRA register directly.
- Passive: nothing is sent to any subject.

## Overlaps ("do both")
- Pairs with the Irish electoral roll and planning registers — PPR confirms the transaction (date/price), while those sources attach the names PPR omits.

## Trust & verifiability
`trust: community` — the data originates from Ireland's authoritative government Property Price Register; this site is a community-run search layer over it, so verify anything critical against the official source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | propertypriceregisterireland-com |
| category | public-records |
| selectorsIn → selectorsOut | address → address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

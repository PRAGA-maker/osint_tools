---
id: loopnet
name: LoopNet
description: Use when you have an `address` or `employer-org` and want commercial-property listings, locations and broker/owner contacts — returns `address`, `employer-org`, `associate`.
url: https://www.loopnet.com/
category: search-engines
path:
- search-engines
bestFor: Researching commercial real estate — a business's premises, a property's listing history, and the broker/agent tied to it.
selectorsIn:
- address
- employer-org
selectorsOut:
- address
- employer-org
- associate
status: live
pricing: freemium
costNote: Browsing listings and searching is free; a free account unlocks saved searches and some detail, and premium/CoStar data is paid.
opsec: passive
opsecNote: A public listings site; searching properties reveals nothing to any subject. A login isn't needed to browse — avoid registering with identifying details; use a sock-puppet account if you do.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A major, established US commercial-real-estate marketplace (CoStar-owned); listing data is broker-supplied and generally reliable, though listings can be dated or removed once let/sold.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- loopnet.com
- commercial real estate search
tags:
- search-engines
- real-estate
- commercial-property
- business-research
- toddington
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# LoopNet

> The big US commercial-real-estate marketplace — search it to place a business at an address, trace a property's listing history, or find the broker/agent connected to it.

## When to use
You have an `address` or a subject's `employer-org` and want commercial-property context: where a business is located (for-lease/for-sale premises), what a specific commercial address is or was listed as, and who the listing broker/agent or seller is. Useful for confirming a company's physical footprint, spotting a property a subject owns or operates, and pulling a broker/agent `associate` you can pivot on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.loopnet.com/.
2. Search by location/`address` or by keyword/company name; filter by property type (office, retail, industrial, etc.) and for-sale vs for-lease.
3. Open a listing: read the address, property details, asking price/rent, and the listing broker/agent and brokerage.
4. Note the broker/agent and brokerage (`associate`) and any named owner/seller — these are pivot points into business registries and people-search.
5. Pivot: take the address into county assessor/recorder records for the legal owner, and the broker's name into professional-licence and people tools.

## Inputs → Outputs
- **In:** `address` (or `employer-org` / keyword)
- **Out:** `address` (property location & details), `employer-org` (occupying/listing business, brokerage), `associate` (broker/agent, seller)
- **Empty/negative result looks like:** no active listing for the address/area — meaning nothing is *currently listed*, which says nothing about ownership; go to assessor records for that.

## Gotchas & OpSec
- Human-in-the-loop: none to browse; a free account adds features.
- OpSec: passive — a public marketplace.
- Listings reflect what's on the market, not ownership — a property not listed is simply not for sale/lease. Data is broker-supplied and can be stale or removed after a deal closes; confirm ownership and occupancy through official records.

## Overlaps ("do both")
- Pairs with county assessor/recorder and business-registry searches — LoopNet gives the marketing listing, broker and premises; the official records give the legal owner and filings behind the address.

## Trust & verifiability
`trust: community` — an established commercial marketplace with broker-supplied data; reliable for listings but not an ownership record, so corroborate ownership in official sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | loopnet |
| category | search-engines |
| selectorsIn → selectorsOut | address, employer-org → address, employer-org, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: worldchambersnetwork-directory-search
name: WorldChambersNetwork Directory Search
description: Use when you need to find a chamber of commerce by country or region — returns the chamber's employer-org details and address as a route into local business networks.
url: http://chamberdirectory.worldchambers.com/
category: search-engines
path:
- search-engines
bestFor: Locating national, regional, bilateral, and local chambers of commerce worldwide as a gateway to regional business contacts.
selectorsIn:
- employer-org
- geolocation
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free directory search; no account required.
opsec: passive
opsecNote: Public directory lookup; you search for organizations, not individuals, and nothing is notified. Standard web logging only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Directory operated within the World Chambers Network / ICC ecosystem; useful as an index, though individual listings vary in freshness.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- World Chambers Network directory
- WCN chamber directory
- worldchambers.com
tags:
- search-engines
- chambers-of-commerce
- business-directory
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# WorldChambersNetwork Directory Search

> A global index of chambers of commerce — find the chamber for a country, region, or city, which in turn is a gateway to local company listings and business contacts.

## When to use
You are researching a business or person in a region and want an entry point into the local commercial network. This directory locates the relevant chamber of commerce (national, regional, bilateral, or local) with its contact details and `address`. Chambers often publish member directories and events, so the chamber you find here becomes a lead to the specific `employer-org`s and people active in that area.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the chamber directory at chamberdirectory.worldchambers.com.
2. Use the keyword search (with optional filters for chamber type — transnational, national, regional, bilateral, local — and match mode: any/all/exact).
3. Open a matching chamber's entry: read its name, jurisdiction, and contact/address details, then follow through to the chamber's own site.
4. Pivot: the chamber's website and member directory expose local companies and officers; bilateral chambers are useful for tracing cross-border business ties.

## Inputs → Outputs
- **In:** `employer-org` (chamber name) or `geolocation` (country/region to cover)
- **Out:** `employer-org` (matching chamber), `address` (chamber contact/location)
- **Empty/negative result looks like:** no chamber matched — the term/region isn't indexed here; try a broader region or search the country's national chamber directly.

## Gotchas & OpSec
- Human-in-the-loop: none; straightforward directory search.
- OpSec: passive — you're looking up organizations, not people.
- Freshness varies: some listings are dated; confirm a chamber still exists and its contact details on its own current website before relying on them.

## Overlaps ("do both")
- Pairs with `[[uk-government-list-of-overseas-registries]]` and corporate registries — the chamber directory gives you the local business network entry point, while registries give the statutory company records.

## Trust & verifiability
`trust: community` — a serviceable global chamber index; verify any specific chamber and its details against the chamber's own official site.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | worldchambersnetwork-directory-search |
| category | search-engines |
| selectorsIn → selectorsOut | employer-org, geolocation → employer-org, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

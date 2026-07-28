---
id: naics-code-search
name: NAICS Code Search (US Census)
description: Use when you have an industry keyword or a business and want its NAICS industry code (or the reverse) — the code that unlocks industry-scoped searches in other business databases.
url: https://www.census.gov/naics/
category: public-records
path:
- public-records
bestFor: Translating between an industry/business description and its official NAICS code for use in other datasets.
selectorsIn:
- employer-org
selectorsOut: []
status: live
pricing: free
costNote: Free official US Census Bureau tool; no account.
opsec: passive
opsecNote: Passive lookup of a public code reference; you search an industry keyword or code, disclosing nothing about a subject. No sock puppet needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official US Census Bureau NAICS reference — the authoritative source for North American industry classification codes.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- us-census-bureau
aliases:
- NAICS lookup
- North American Industry Classification System
tags:
- corporate
- industry-codes
- census
source: metaosint
lastVerified: '2026-07-28'
enrichment: full
---

# NAICS Code Search (US Census)

> The official lookup for North American Industry Classification System codes — turn an industry keyword into a NAICS code (or decode a code you found), the key that many business and government datasets are indexed by.

## When to use
You're doing company/corporate research and hit a NAICS code in a filing, permit, contract or registry and need to know what industry it means — or you want the code for an industry so you can filter another dataset (procurement, SBA, D&B, state registries) to businesses of that type. NAICS codes are the connective tissue of US business data; this tool moves you between plain-language industry and the code. It classifies industries, not people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.census.gov/naics/.
2. Keyword search (e.g. "auto repair") to find matching NAICS codes, or enter a known code to read its industry definition.
3. Note the 2–6 digit code and its official description.
4. Take the code into other datasets to scope a search to that industry (procurement, licensing, business directories).
5. Pivot: combine an industry code + location to enumerate businesses of a type via a corporate-search tool or `[[us-census-bureau]]` data.

## Inputs → Outputs
- **In:** an industry keyword or a NAICS code (often tied to an `employer-org`)
- **Out:** the matching NAICS code(s) and official industry definition (no person-level `selectorsOut`)
- **Empty/negative result looks like:** no match for a keyword — try a broader/synonymous term; NAICS categories are sometimes worded differently than everyday language.

## Gotchas & OpSec
- OpSec: fully passive; a code reference, not a target query.
- Scope is North American (US/Canada/Mexico); for other regions use ISIC/NACE equivalents.
- A code describes an *industry*, not a specific company — it's a filter/key, not a business record itself.

## Overlaps ("do both")
- Do both with `[[us-census-bureau]]` and corporate registries via `[[catalogue-of-research-databases-occrp-id]]` — NAICS gives the industry key; those datasets use it to return the actual businesses and their filings.

## Trust & verifiability
`trust: trusted` — the authoritative US Census NAICS reference; codes and definitions are official.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | naics-code-search |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

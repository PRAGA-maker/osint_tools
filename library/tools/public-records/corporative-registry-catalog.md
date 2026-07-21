---
id: corporative-registry-catalog
name: Corporative Registry Catalog
description: Use when you have an `employer-org` or company lead in a specific country and want the link to that country's official business/company registry — returns direct links to 63 national corporate registries (a routing directory, no direct selector output).
url: https://cipher387.github.io/corporative_registry_worldwide_catalog/
category: public-records
path:
- public-records
bestFor: Quickly finding the official company-registration search site for a given country to then look up a business, its directors and filings.
selectorsIn:
- employer-org
selectorsOut: []
status: degraded
pricing: free
costNote: The catalog itself is free; individual national registries it links to may charge or require registration (marked $ / r in the list).
opsec: passive
opsecNote: Passive — a static list of links. The registry sites you land on may log searches; use a clean browser if you want to avoid a trail on a specific jurisdiction's registry.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Curated by researcher cipher387 (Cyb_Detective); the page itself carries a notice that it is no longer being updated and points to the newer Worldwide OSINT Tools Map, so treat the link list as a frozen-2020s snapshot.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Worldwide Corporate Registry Catalog
tags:
- Company information search
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Corporative Registry Catalog

> A one-page directory linking to the official company registries of 63 countries — the fast way to jump from "a company in country X" to that country's authoritative registry. Note: **frozen / no longer updated.**

## When to use
You have an `employer-org` (or a company mentioned in a case) tied to a particular country and need the *official* corporate registry to look it up — directors, incorporation date, registered address, filings. This catalog saves you guessing the right registry per jurisdiction across 63 countries.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the catalog and find the country of interest.
2. Note the flags: `$` marks registries that charge for searches, `r` marks those needing registration.
3. Follow the link to the national registry and search the company by name (or director/`name`).
4. Read the official record: officers, registered address, status, filing history.
5. Pivot: directors' names feed `associate`/`name` work; a registered address feeds address OSINT.

## Inputs → Outputs
- **In:** an `employer-org` + its country (used to pick the registry)
- **Out:** direct links to the relevant national registry (a routing step); the registry itself then yields directors, address, status
- **Empty/negative result looks like:** the country isn't among the 63 listed, or the linked registry has moved — use the newer Worldwide OSINT Tools Map or a dedicated company-search aggregator instead.

## Gotchas & OpSec
- **Frozen list**: the maintainer explicitly stopped updating it and recommends the successor OSINT Tools Map — some links may have rotted; treat as a starting index, not a live tool.
- It's a directory only — it never returns companies, just the registry to search.
- Some linked registries paywall or gate searches.
- OpSec: passive.

## Overlaps ("do both")
- Pairs with global company aggregators (e.g. OpenCorporates-style tools) — use this to find the *authoritative national* registry when an aggregator's data is thin or stale for that jurisdiction.

## Trust & verifiability
`trust: community` — a curated hobbyist index that points at first-party registries; the registries themselves are authoritative, but confirm each link still resolves since the catalog is no longer maintained.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | corporative-registry-catalog |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

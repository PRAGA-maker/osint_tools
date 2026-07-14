---
id: gijn-org-3
name: GIJN Guide — Land & Property Ownership Records
description: Use when you have an `address` or a person/`employer-org` and want a methodology and jurisdiction pointers for finding land/property ownership records worldwide — returns a research guide, not a search box.
url: https://gijn.org/resource/land-ownership-records-so-useful-but-challenging-to-find/
category: public-records
path:
- public-records
bestFor: Learning where and how to find land/property ownership records across jurisdictions when no single registry covers your target.
selectorsIn:
- address
- name
- employer-org
selectorsOut:
- address
- name
- employer-org
status: live
pricing: free
costNote: Free guide/resource article from GIJN; no account required. The registries it points to may have their own fees.
opsec: passive
opsecNote: Reading a guide is entirely passive. OpSec risk lives in the individual registries it directs you to, not in this page.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by the Global Investigative Journalism Network (GIJN), a well-regarded nonprofit resource for investigative methodology.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- GIJN land ownership records guide
tags:
- propertysites
- Property Related Sites
- guide
- methodology
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# GIJN Guide — Land & Property Ownership Records

> A GIJN methodology guide (not a searchable database) on locating land and property ownership records across jurisdictions where they are useful but hard to find.

## When to use
You need to establish who owns a property, or which properties a person/company owns, but you don't yet know which registry to use — because land records are fragmented, jurisdiction-specific, and often not online. This GIJN resource orients you: it explains why land-ownership records matter for investigations, the obstacles to finding them, and where to look by region. Reach for it as a *starting map* before diving into a specific national/regional land registry, rather than as a tool that returns records itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://gijn.org/resource/land-ownership-records-so-useful-but-challenging-to-find/ and read the guide.
2. Identify the jurisdiction of your target `address`/owner and note the registries, access routes, and workarounds the guide highlights for that region.
3. Follow the guide's pointers to the actual land/cadastral registry, then run your `address` or `name`/`employer-org` query there.
4. Pivot: ownership records surface owner `name`s, linked `address`es, and holding `employer-org`s that feed corporate-registry and people-search follow-up.

## Inputs → Outputs
- **In:** the *context* of an `address`, `name`, or `employer-org` you want to trace to property ownership
- **Out:** a research methodology and jurisdiction-by-jurisdiction pointers to the registries that actually return owner `name`s / `address`es / `employer-org`s
- **Empty/negative result looks like:** the guide has no direct pointer for your jurisdiction — you'll need to search for that country's cadastre/land registry separately; this is a guide, so it never "returns no results" in the search sense.

## Gotchas & OpSec
- This is a **guide, not a search tool** — it produces no records itself; the actual data lives in the registries it points to.
- Land-record access, cost, and coverage vary enormously by jurisdiction; the guide sets expectations rather than guaranteeing availability.
- OpSec: reading is passive; assess OpSec at each downstream registry.

## Overlaps ("do both")
- Use alongside specific land/property registries such as `[[residential]]` (VOA council tax bands, England & Wales) and national cadastres — this guide tells you *which* registry, those return the actual ownership data.

## Trust & verifiability
`trust: trusted` — GIJN is a reputable investigative-journalism nonprofit; the guidance is editorial methodology, so verify the current state of any registry it references before relying on access details.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gijn-org-3 |
| category | public-records |
| selectorsIn → selectorsOut | address, name, employer-org → address, name, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

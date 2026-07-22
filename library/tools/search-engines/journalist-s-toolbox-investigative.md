---
id: journalist-s-toolbox-investigative
name: Journalist's Toolbox — Investigative
description: Use when you need a vetted starting point for an investigation and want a curated directory of people-tracing, public-records, and verification tools — returns pointers to specialised lookup tools.
url: https://www.journaliststoolbox.org/category/investigative/
category: search-engines
path:
- search-engines
bestFor: A journalist-curated jump-off list of investigative, public-records, and people-search tools.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, ad-supported resource; no account required to browse.
opsec: passive
opsecNote: Browsing the directory reveals nothing about a target. The linked third-party tools each have their own OpSec profile — apply the appropriate caution when you follow a link and run an actual lookup.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running resource maintained by Mike Reilley, associated with the Society of Professional Journalists and used in journalism training.
missingPersonsRelevance: medium
coverage:
- global
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Journalists Toolbox
tags:
- tool-collection
- journalism
- public-records
source: ultimate-osint
lastVerified: '2026-07-22'
enrichment: full
---

# Journalist's Toolbox — Investigative

> Mike Reilley's SPJ-linked directory of investigative research tools — a curated menu of where to look, organised for reporters tracing people, records, and claims.

## When to use
You're at the start of an investigation and want a trustworthy, human-curated index of investigative tools — people finders, public-records portals, court/business records, verification and archiving utilities — rather than blindly searching. Especially handy when you're missing a specialised tool for a given selector and want a vetted candidate to try. US-weighted but with global resources.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.journaliststoolbox.org/category/investigative/.
2. Scan the Investigative category (and sibling categories like public records, people search, verification) for a tool matching the selector you hold.
3. Follow the link to the actual tool and run your lookup there.
4. Cross-reference: because it's curated by a journalist, entries lean toward reputable, court-admissible-quality sources — good for building a defensible research trail.
5. Pivot: use it iteratively — each finding surfaces a new selector, and you return here to find the next specialised tool.

## Inputs → Outputs
- **In:** none (a curated directory, not a selector-driven lookup)
- **Out:** categorised links to investigative / public-records / people-search / verification tools
- **Empty/negative result looks like:** no listed tool for your niche need — meaning you fall back to a broader OSINT tool directory.

## Gotchas & OpSec
- It's a link directory: individual entries can go stale or dead over time, and coverage skews US.
- The tools it points to vary in cost, jurisdiction, and OpSec — vet each on arrival rather than assuming inclusion means free/passive.
- OpSec: browsing is passive; the footprint is created only when you follow a link and query a target.

## Overlaps ("do both")
- Pairs with broader OSINT tool catalogues — this one is journalist-curated and records/verification-heavy, so it surfaces reputable public-records tools that generic hacker-oriented lists under-emphasise.

## Trust & verifiability
`trust: trusted` — maintained for years by a named journalism educator (Mike Reilley) in the SPJ orbit, so the curation is credible; judge each linked tool's data quality separately.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | journalist-s-toolbox-investigative |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

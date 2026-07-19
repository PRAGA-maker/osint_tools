---
id: justice-directory
name: Justice Directory (CopNet)
description: Use when you have a jurisdiction/region and want the official website of its law-enforcement or justice agency — returns links to police/justice agencies worldwide.
url: http://www.copnet.org/justice.html
category: search-engines
path:
- search-engines
bestFor: A worldwide directory of law-enforcement and justice-agency websites, organised by region, for reaching the right official body.
selectorsIn:
- address
selectorsOut:
- employer-org
status: degraded
pricing: free
costNote: Free static directory, no account. It's an aging link index (CopNet) — expect some dead/outdated links; verify each agency link resolves before relying on it.
opsec: passive
opsecNote: Browsing a public list of agency links reveals nothing about your subject and contacts no one — fully passive. (Actually contacting an agency you find is a separate, non-passive step handled outside this tool.)
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: CopNet is a long-standing but dated community police-resource portal. It's a link index, not an authority — always confirm you've reached the genuine official agency site.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- CopNet Justice Directory
- Agencies of the World
tags:
- toddington
- curated-directory
- specialty-search
- law-enforcement
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Justice Directory (CopNet)

> A worldwide, region-organised index of law-enforcement and justice-agency websites — a starting point for finding the right official body, though the link list is aging.

## When to use
You have a jurisdiction or `address`/region and need to reach the correct law-enforcement or justice agency — for filing or checking a missing-persons report, finding the responsible police force, or identifying the official body in an unfamiliar country. This directory groups agency links by continent/region so you can drill from "which country" down to a specific force's site.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.copnet.org/justice.html (and the sibling "Agencies of the World" index at copnet.org/local/).
2. Browse to your region (Africa, Asia, Europe, North/Central/South America, Middle East, Australia).
3. Follow the link for the relevant agency/jurisdiction.
4. Verify the destination: confirm the linked site is the genuine current official agency (CopNet links can be outdated) — check the domain and cross-reference.
5. Pivot: use the official site to find the correct reporting channel, records office, or contact for your case.

## Inputs → Outputs
- **In:** a region/jurisdiction (`address`-level) you need the agency for
- **Out:** link to the corresponding law-enforcement/justice `employer-org` (agency) site
- **Empty/negative result looks like:** no entry for a region, or a dead link — CopNet's coverage is uneven and aging; fall back to a direct search for "<jurisdiction> police official site" or an official government portal.

## Gotchas & OpSec
- Status is degraded: it's an old link index; expect dead links and superseded agency URLs — always confirm the current official site.
- Coverage is broad but shallow/uneven; not every jurisdiction is listed.
- OpSec: passive to browse; any actual contact with an agency is a separate, attributable action.

## Overlaps ("do both")
- Complements a direct search-engine query for the official agency — use the directory to orient, then confirm the live official site independently.

## Trust & verifiability
`trust: unverified` — a community-maintained, dated portal that merely points to agencies. It carries no authority itself; treat every link as a lead and verify you've landed on the genuine official site before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | justice-directory |
| category | search-engines |
| selectorsIn → selectorsOut | address → employer-org |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

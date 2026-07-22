---
id: mindmap-search-engine
name: Mindmap Search Engine
description: Use when you want an alternate scoped Google search to broaden a query — returns web `social-profile` / `domain` links (scope is opaque, test empirically).
url: https://cse.google.com/cse?cx=013991603413798772546:gj6rx9spox8
category: search-engines
path:
- search-engines
bestFor: A secondary, community-configured Google search to diversify results — value depends entirely on its (undisclosed) site scope.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- domain
status: degraded
pricing: free
costNote: Free Google Programmable Search Engine; no account needed.
opsec: passive
opsecNote: A scoped Google search; queries go to Google. Passive to any target, but assume Google logs the query — use a sock-puppet browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Anonymous community-built Google Custom/Programmable Search Engine — the sites it covers are not disclosed and it may have rotted; verify what it returns before relying on it.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- chrome-extension-archive-search-engine
aliases: []
tags:
- google-cse
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# Mindmap Search Engine

> A community-configured Google Programmable Search Engine of undisclosed scope — treat it as one more alternate index to try, and confirm empirically what it actually covers before trusting a result.

## When to use
You want a second, differently-scoped search pass on a `name` or `username` and are willing to test an opaque CSE to see whether it surfaces links your primary engine missed. Because the creator's site scope is not documented, its usefulness is unknown until you run a few controlled queries — use it as a supplementary engine, never a primary one.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE URL; it loads as a Google Programmable Search box.
2. First calibrate: run a query you already know the answer to, to infer what the engine is scoped to (general web vs. a niche set of sites).
3. Then enter your real selector — `name`, `"exact phrase"`, or `username`.
4. Pivot: feed any new `social-profile`/`domain` hit into the appropriate specialist tool; discard the engine if calibration shows it adds nothing.

## Inputs → Outputs
- **In:** `name` / `username` (free-text query)
- **Out:** ranked web links → `social-profile`, `domain`
- **Empty/negative result looks like:** no hits — for an opaque CSE this usually means your target sits outside its configured scope, so fall back to an unscoped engine rather than concluding nothing exists.

## Gotchas & OpSec
- **Opaque, possibly stale scope:** you cannot see which sites it searches, and CSEs silently degrade. Always calibrate before trusting, and never treat an empty result as authoritative.
- No login, passive; standard Google query hygiene applies.

## Overlaps ("do both")
- Pairs with `[[chrome-extension-archive-search-engine]]` and a plain unscoped search — CSEs are hit-or-miss, so run several and compare.

## Trust & verifiability
`trust: community` — an anonymous CSE of unknown scope; corroborate every hit against a first-party source and drop the tool if calibration shows no added coverage.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mindmap-search-engine |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

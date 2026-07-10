---
id: knowem-username-search
name: Knowem Username Search
description: Use when you have a `username` and want to see which of 500+ social networks (and domains) it's registered on — returns a grid of taken/available `social-profile`s to pivot into.
url: http://knowem.com
category: people-search
path:
- people-search
bestFor: One-shot username availability/presence check across 500+ social networks and 150+ domains.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free username-availability grid; Knowem also sells paid brand-protection registration services, but the checking tool is free and needs no account.
opsec: passive
opsecNote: Knowem checks availability from its own infrastructure, so requests to the 500+ sites don't come from your IP and no target is contacted. Standard sock-puppet browsing hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running brand/username checker; "taken" means the handle exists on that site, but it doesn't confirm the account is your subject — verify each hit by opening it.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- whatsmyname-web
- namechk-2
- namevine-user-name-search
aliases:
- KnowEm
- knowem.com
tags:
- toddington
- curated-directory
- username-check
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Knowem Username Search

> A one-shot username checker across 500+ social networks and 150+ domains — see instantly where a handle is registered, then open the hits to confirm they're your subject.

## When to use
You have a `username` and want a fast breadth-first map of where that handle exists. Knowem's grid shows taken vs available across hundreds of platforms, giving you a shortlist of `social-profile`s to investigate. It's a triage step at the start of a username-pivot, complementary to (and cross-checked against) other multi-site checkers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://knowem.com and enter the `username`.
2. Run the check across the social-network categories (and optionally the domain-availability check).
3. Read the grid: a "taken" tile means the handle is registered on that platform — a candidate account to inspect.
4. Open each promising hit and verify it's actually your subject (avatar, bio, activity), not a namesake or brand.
5. Pivot: confirmed profiles feed per-platform enrichment; cross-run the same handle on `[[whatsmyname-web]]` and `[[namechk-2]]` since site coverage differs.

## Inputs → Outputs
- **In:** `username`
- **Out:** a taken/available map of `social-profile`s across 500+ networks and domains
- **Empty/negative result looks like:** the handle shows available almost everywhere — either genuinely unused or your subject uses a different handle; try variants (via `[[bellingcat-name-variant-search]]`).

## Gotchas & OpSec
- "Taken" ≠ "your subject" — different people/brands share handles; always open and verify.
- Coverage and accuracy drift as sites change; a stale checker can false-negative — corroborate with another tool.
- OpSec: passive; checks run from Knowem's side, not yours.

## Overlaps ("do both")
- Overlaps with `[[whatsmyname-web]]`, `[[namechk-2]]`, and `[[namevine-user-name-search]]` — run several because each covers a different, overlapping site set; the union is the real map.

## Trust & verifiability
`trust: community` — a reliable, long-standing availability checker, but it reports handle existence, not identity. Confirm each actionable hit on the platform itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | knowem-username-search |
| category | people-search |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

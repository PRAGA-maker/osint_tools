---
id: sourcinglab-pinterest-search
name: SourcingLab Pinterest Search
description: Use when you have a `name` or `username` and want to find their Pinterest pins, boards and profile — returns social-profile.
url: https://sourcinglab.io/search/pinterest
category: social-networks
path:
- social-networks
bestFor: Targeted searching of Pinterest pins, boards and users without hand-crafting Google dorks.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free web search helper; no account required to run a query.
opsec: passive
opsecNote: The tool builds and runs the search for you (typically via search-engine queries), so you hit Pinterest indirectly rather than logging into it. Passive, but do it from a sock-puppet browser/VPN so a sensitive query isn't tied to your real IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party query-builder that wraps public search; not affiliated with Pinterest. Results depend on the underlying search engine's index, so completeness varies.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- SourcingLab Pinterest
tags:
- pinterest
- social-search
source: osintambition-social
lastVerified: '2026-07-28'
enrichment: full
---

# SourcingLab Pinterest Search

> A query-builder that turns a name or handle into a targeted Pinterest search for pins, boards and users.

## When to use
You have a `name` or `username` and suspect the subject uses Pinterest (crafts, home, travel, wedding, recipe boards often leak location, relationships and interests). Rather than hand-building `site:pinterest.com` dorks, SourcingLab assembles the query and runs it, surfacing matching pins/boards/profiles. Pinterest boards can be surprisingly revealing for lifestyle, location and associate context in a missing-person or background case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://sourcinglab.io/search/pinterest.
2. Enter the subject's `name` or `username` (and any extra keyword like a city or interest).
3. Run the search; it opens/returns matching Pinterest pins, boards and user profiles.
4. Read the output: a matching profile is a `social-profile` pivot; board titles and pins reveal interests, locations and linked accounts.
5. Pivot: open the Pinterest profile directly, note the username, and cross-search that username on other networks with a username-enumeration tool.

## Inputs → Outputs
- **In:** `name` or `username` (optionally + keyword)
- **Out:** `social-profile` (Pinterest profiles/boards/pins), plus interest/location context from board contents
- **Empty/negative result looks like:** no matching profiles — the subject may not use Pinterest, may use an unrelated handle, or the search index may not have surfaced it; try a different name variant or interest keyword.

## Gotchas & OpSec
- OpSec: passive; the tool queries search engines, so Pinterest itself isn't directly probed. Use a sock-puppet browser on sensitive work.
- Completeness depends on the underlying search index; a negative is not proof of absence.
- Common Pinterest names are noisy — pair the name with a distinguishing keyword (city, employer, interest).

## Overlaps ("do both")
- Pairs with other `social-networks` username tools — SourcingLab finds the Pinterest presence, then a cross-platform username search maps the same handle onto other sites.

## Trust & verifiability
`trust: unverified` — a third-party query wrapper, not a Pinterest-official source; verify hits by opening the actual Pinterest profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sourcinglab-pinterest-search |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

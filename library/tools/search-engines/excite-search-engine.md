---
id: excite-search-engine
name: Excite Search Engine
description: Use when you want a second-opinion web search plus classic White/Yellow Pages links from one legacy portal — returns aggregated web/news results and directory jump-offs for a `name`.
url: http://www.excite.com
category: search-engines
path:
- search-engines
bestFor: A legacy metasearch portal for second-opinion results and quick White/Yellow Pages access.
selectorsIn:
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free ad-supported portal; no account.
opsec: passive
opsecNote: A plain web search is passive and the subject isn't notified. Excite aggregates other engines' results and embeds third-party services (Yahoo, ESPN, White/Yellow Pages), so clicking through hands you off to those sites — normal browsing hygiene applies; use a clean profile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A surviving legacy web portal that now aggregates third-party search/content rather than running its own crawler; useful as a different result mix, not an authoritative index.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Excite
- excite.com
tags:
- toddington
- curated-directory
- search
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Excite Search Engine

> A surviving early-web portal — handy for a *different* set of web/news results and one-click access to White/Yellow Pages directories.

## When to use
You want a second-opinion search that isn't Google/Bing directly, or quick jump-offs to classic US directory services (White Pages, Yellow Pages) bundled into the portal. As a metasearch-style portal, Excite sometimes surfaces or orders results differently, which can shake loose a hit the majors buried.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.excite.com and use the search box (web/images/news/video tabs).
2. Run the subject's `name` (quote it; add a location or qualifier to disambiguate).
3. Use the portal's directory links (White Pages / Yellow Pages) to pivot a name into a phone/address directory lookup.
4. Compare the result mix against what Google/Bing returned.
5. Pivot: directory hits feed people-search; any profile/news link feeds the relevant platform tool.

## Inputs → Outputs
- **In:** `name` (or any keyword)
- **Out:** aggregated web/news results and directory jump-offs (potential `social-profile`/contact leads)
- **Empty/negative result looks like:** thin or generic results — since Excite aggregates rather than crawls, treat a blank as "these upstreams had nothing," not authoritative absence; use a primary engine to confirm.

## Gotchas & OpSec
- It's a portal aggregating third-party services, not a first-party crawler — result quality tracks whatever it's pulling from.
- The embedded White/Yellow Pages tools are US-centric.
- OpSec: passive; ordinary web browsing, no subject notification.

## Overlaps ("do both")
- Pairs with the major engines and dedicated people-directories — use Excite for a different result mix and its directory jump-offs, then confirm anything material in a primary source.

## Trust & verifiability
`trust: community` — a legacy aggregator portal; treat its results as leads and verify in a first-party engine or the underlying directory service.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | excite-search-engine |
| category | search-engines |
| selectorsIn → selectorsOut | name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

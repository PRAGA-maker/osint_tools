---
id: alleba-philippines
name: Alleba (Philippines)
description: Use when your subject or content is Philippine and you want a local search engine/directory that surfaces PH sites a global engine buries — returns domain, social-profile leads.
url: https://www.alleba.com
category: search-engines
path:
- search-engines
bestFor: Finding Philippine-specific websites, businesses, and local content via a national search directory.
selectorsIn:
- name
- employer-org
selectorsOut:
- domain
- social-profile
status: degraded
pricing: free
costNote: Free to use; no account.
opsec: passive
opsecNote: A normal public search query — passive and target-invisible. Standard search-engine logging of your own query/IP applies; use a clean profile for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing Philippine search engine/directory. Its index is smaller and less fresh than a global engine, and national directories decay over time — treat coverage as partial and dated.
missingPersonsRelevance: low
coverage:
- ph
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- google-advanced-search
tags:
- main-national-search-engines
- philippines
- regional-search
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Alleba (Philippines)

> A Philippine national search engine/directory — a regional lens that can surface local PH sites and businesses which a global search engine ranks out of sight.

## When to use
Your subject, business, or content is Philippine and a global engine isn't surfacing local results. A national directory can index small local sites, regional businesses, and community pages that Google buries. Use it as a *complement* to global search, not a replacement — its index is narrower.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to alleba.com.
2. Search for the `name`, `employer-org`, place, or Filipino-language term.
3. Review results for local sites/directories not prominent on global engines.
4. Because coverage is limited and possibly dated, always re-run the query on a global engine with `site:.ph` and Filipino-language terms.
5. Pivot: a local site → its content/contacts (`domain`, `social-profile`); a business listing → PH company registry (SEC).

## Inputs → Outputs
- **In:** `name`, `employer-org`, or keyword (ideally with local/Filipino terms)
- **Out:** `domain` (PH sites), `social-profile`/business leads
- **Empty/negative result looks like:** thin or no results — very possible given a small national index; treat as inconclusive and fall back to a global engine with country/language operators.

## Gotchas & OpSec
- **Small, possibly stale index:** don't rule anything out from an empty result here; national directories age. Marked `degraded` for that reason.
- Best paired with local-language search terms — English-only queries miss Filipino/Tagalog content.
- Passive; standard query logging.

## Overlaps ("do both")
- Pairs with `[[google-advanced-search]]` using `site:.ph` and Filipino-language terms — the global engine gives breadth, the national directory occasionally catches local sites it misses.

## Trust & verifiability
`trust: community` — a regional search index of unknown freshness. Useful as a supplementary local lens; verify any lead on the source site and via a comprehensive engine.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | alleba-philippines |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → domain, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

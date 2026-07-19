---
id: lilo
name: Lilo
description: Use when you want an alternate (French) search front-end to cross-check results outside your usual engine — returns general web results with a charitable/privacy angle.
url: https://www.lilo.org
category: search-engines
path:
- search-engines
bestFor: A free French charitable search front-end, useful as a second-opinion search and for French/European-flavored results.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free; funded by search-ad revenue that it directs to social/environmental projects. No account needed to search.
opsec: passive
opsecNote: A search front-end that markets itself as not profiling users; querying it doesn't touch any subject. As with any engine, queries are logged provider-side — use a clean session for sensitive lookups.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A real, operating French charitable search engine; results come from mainstream back-ends, so quality tracks those — the charity angle doesn't affect data.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- lilo.org
tags:
- toddington
- curated-directory
- search-engines
- metasearch
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Lilo

> A free French charitable search engine — practically, another search front-end to run a query through outside your usual Google session, with a mild French/European lean.

## When to use
Like other cause-branded engines, Lilo's OSINT value is modest: it's an alternate front-end you can use to run a `name`, `username` or dork without your personalized Google session, and it can lean slightly toward French-language results. Use it as a second-opinion pass, not a unique index — don't expect data other engines lack.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.lilo.org and run your query (name, handle, quoted phrase, or `site:` dork).
2. Read the results; compare against Google/Bing/DuckDuckGo and Yandex for coverage differences.
3. Lean on it when French/European-language coverage matters.
4. Pivot: any profile/page found → the usual follow-up (confirm, capture, enumerate).

## Inputs → Outputs
- **In:** `name`, `username`, keyword, or dork
- **Out:** general web results, including any `social-profile`/page matches
- **Empty/negative result looks like:** sparse results — mirrors what its back-end has; try other engines and language variants before concluding absence.

## Gotchas & OpSec
- Not a unique crawler — it adds a viewpoint and slight regional lean, not new data.
- The charitable framing is irrelevant to intelligence value; judge it as "another engine's results."
- OpSec: passive; queries are logged provider-side — use a clean/sock-puppet session for sensitive work.

## Overlaps ("do both")
- Cross-check with Google, Bing, DuckDuckGo, Yandex and `[[metager-meta-search-engine]]` — the point is running the same query across engines to catch what any one buries.

## Trust & verifiability
`trust: community` — a legitimate, operating search front-end; results inherit its back-end's reliability, with no special data-quality risk beyond that.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lilo |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

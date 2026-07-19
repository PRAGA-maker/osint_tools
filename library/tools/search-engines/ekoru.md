---
id: ekoru
name: Ekoru
description: Use when you want an alternative web search that doesn't track/profile you — a privacy-branded metasearch; query a `name`/`username`/`domain` to get web results without Google's personalization.
url: https://ekoru.org/
category: search-engines
path:
- search-engines
bestFor: A low-personalization alternative search engine to diversify results away from a Google/Bing bubble.
selectorsIn:
- name
- username
- domain
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free, ad-supported charitable search engine; no account.
opsec: passive
opsecNote: Passive toward the target — a normal web search touching no site of theirs. Ekoru markets not storing search/IP data, which reduces your own footprint versus mainstream engines, but treat privacy claims as unaudited; still use a clean/sock-puppet browser for sensitive queries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A small independent metasearch (results drawn from partner indexes) with an environmental/privacy mission; useful as a diversity lens, not a primary authoritative source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Ekoru Search
tags:
- toddington
- search-engines
- privacy-search
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Ekoru

> A privacy-branded, ocean-cleanup-funding metasearch engine — handy as a second search lens that isn't personalised to you.

## When to use
You want to check a `name`, `username`, or `domain` against a search index other than Google/Bing to escape personalization and surface different top results. Ekoru is a privacy-oriented metasearch; its value in OSINT is diversity of results, not unique coverage.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ekoru.org/.
2. Enter your query — a name in quotes, a handle, or a domain. Basic operators work.
3. Read the output: standard web results (drawn from partner search indexes). Compare against what Google/Yandex returned.
4. Pivot: follow any new links Ekoru surfaces that your primary engine buried; feed selectors onward.

## Inputs → Outputs
- **In:** `name` / `username` / `domain` query
- **Out:** web results — links to `social-profile`s, `domain`s, articles
- **Empty/negative result looks like:** thin or no results is common for niche queries since it relies on partner indexes — never treat an Ekoru blank as proof; corroborate with a primary engine.

## Gotchas & OpSec
- Result quality/coverage is weaker and less predictable than Google — use it to diversify, not as a sole source.
- Privacy claims are marketing, not audited; do not over-rely on them for opsec.
- Human-in-the-loop: none. OpSec: passive.

## Overlaps ("do both")
- Do both with Google/Yandex/Bing — Ekoru's job here is to be a different lens; run the same query across several engines and merge what's unique.

## Trust & verifiability
`trust: community` — an independent metasearch; verify every hit on its live source, and don't assume its index is comprehensive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ekoru |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, domain → social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

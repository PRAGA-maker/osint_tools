---
id: metager-meta-search-engine
name: MetaGer Meta Search Engine
description: Use when you have a `name`, `username` or keyword and want privacy-preserving results merged from multiple engines — returns web results Google may personalize away.
url: https://metager.de
category: search-engines
path:
- search-engines
bestFor: A privacy-focused metasearch that blends several engines' results, useful as an unpersonalized second pass and for German/European coverage.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to search (run by the non-profit SUMA-EV); an optional paid membership removes ads and adds features, but search itself is free.
opsec: passive
opsecNote: MetaGer is built for privacy — it proxies queries to underlying engines and offers an anonymizing "open anonymously" proxy for opening results, so your searches and clicks aren't tied to your identity the way a logged-in Google session is. Passive toward any subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by SUMA-EV, a German non-profit; a long-standing, reputable privacy metasearch.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- metager.de
- MetaGer
tags:
- toddington
- curated-directory
- meta-mega-search-tools
- metasearch
- privacy
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# MetaGer Meta Search Engine

> A German non-profit privacy metasearch that merges results from several engines — an unpersonalized second-opinion search with strong German/European coverage and a built-in result-anonymizing proxy.

## When to use
You've searched a `name`, `username`, or phrase on Google and want a different, unpersonalized view — MetaGer blends multiple back-end engines and doesn't tailor to your account, so it can surface pages your personalized Google buries. Two extra draws for OSINT: solid German/European-language coverage, and an "open anonymously" proxy that lets you click into a result without your IP/identity reaching the destination.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://metager.de and run your query (name, quoted phrase, handle, or `site:` dork).
2. Read the merged results, noting which back-end engine each came from.
3. Use "open anonymously" to visit a sensitive result through MetaGer's proxy instead of directly.
4. Compare against Google/Bing/DuckDuckGo — the point is coverage diversity and no personalization.
5. Pivot: any profile/page found → the normal follow-up (confirm, capture, enumerate); German-language hits → European registries and directories.

## Inputs → Outputs
- **In:** `name`, `username`, keyword, or dork
- **Out:** merged multi-engine web results, including `social-profile`/page matches; anonymized result-opening
- **Empty/negative result looks like:** sparse merged results — the term genuinely has little web presence, or the back-end engines are throttling; try Google/Yandex and language variants before concluding absence.

## Gotchas & OpSec
- It aggregates other engines, so it inherits their gaps; it adds diversity and privacy, not a unique index.
- Ranking/back-ends differ from Google — good for coverage, but verify a specific page by opening it.
- OpSec: strong — no personalization and an anonymizing open-proxy; a good default for sensitive searches.

## Overlaps ("do both")
- Cross-check with Google, Yandex and DuckDuckGo — MetaGer's value is an unpersonalized, privacy-preserving pass and European coverage that a logged-in Google session won't give you.

## Trust & verifiability
`trust: trusted` — a reputable non-profit metasearch; results are genuine engine output (verify individual pages), and its privacy posture is a real, documented feature.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | metager-meta-search-engine |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: dib-dab-doo-and-dilly-too-kids-search-engine
name: Dib Dab Doo and Dilly Too Kids Search Engine
description: Use when you want a kid-safe, human-filtered Google Custom Search view — a niche search front-end that restricts results to vetted child/teen-safe sites.
url: http://www.dibdabdoo.com
category: search-engines
path:
- search-engines
bestFor: Searching a curated, allow-listed slice of the web (child/teen-safe sites) as an alternative filtered view of Google results.
selectorsIn:
- name
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and ad-free; no account. It's a Google Custom Search front-end maintained by a private individual.
opsec: passive
opsecNote: A passive search front-end — queries go to Google's Custom Search backend, so treat it like any Google query for attribution (your IP/query are visible to Google). It offers no anonymity; use a sock-puppet/VPN setup if the query itself is sensitive. Nothing reaches a subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A hobbyist-run, ad-free kid-safe search site (a father maintaining a human-curated Google Custom Search allow-list); dependable for its stated purpose but a private project with narrow, opaque curation.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Dib Dab Doo
- dibdabdoo.com
tags:
- toddington
- curated-directory
- kid-friendly-educational-search-engines
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# Dib Dab Doo and Dilly Too Kids Search Engine

> A hobbyist kid-safe search front-end over Google Custom Search. Marginal OSINT value — occasionally useful as a curated, allow-listed alternate view of the web.

## When to use
Rarely for investigations. It's a Google Custom Search instance whose results are restricted to a human-reviewed allow-list of child/teen-safe sites. The only OSINT-adjacent uses are (1) a *pre-filtered* search that surfaces educational/reference domains without the usual noise, and (2) context research into child-safety search tooling itself. It returns web results (`domain`s), not personal data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.dibdabdoo.com.
2. Enter your query (`name`, topic, or keyword).
3. Results come from Google Custom Search, constrained to the site's vetted allow-list.
4. Read the returned pages/domains; expect far narrower coverage than a normal Google search.
5. For any real search need, run the query on a full search engine — use this only when the curated/filtered view is specifically what you want.

## Inputs → Outputs
- **In:** a search query (`name`/keyword)
- **Out:** `domain`s/web pages from the allow-listed, kid-safe subset
- **Empty/negative result looks like:** few or no results — the allow-list simply doesn't cover your topic; switch to a general search engine.

## Gotchas & OpSec
- It's Google underneath, so it offers no anonymity — treat attribution like any Google query.
- Curation is narrow and opaque (one maintainer); coverage is a small, deliberately limited slice of the web.
- Very low investigative value; don't rely on it as a primary search tool.

## Overlaps ("do both")
- Overlaps with general and custom search engines — this is just a heavily filtered Google Custom Search view; use a full engine for real coverage and this only for its specific safe/curated slice.

## Trust & verifiability
`trust: unverified` — a genuine, long-running hobbyist project that does what it claims, but it's privately maintained with opaque curation and thin coverage; fine for its niche, not for serious research.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dib-dab-doo-and-dilly-too-kids-search-engine |
| category | search-engines |
| selectorsIn → selectorsOut | name → domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

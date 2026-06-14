---
id: carrot2
name: Carrot2
description: Use when a name or keyword returns sprawling web results and you want them auto-clustered into themes to spot relevant sub-topics fast.
url: https://search.carrot2.org
category: image-video-face
path:
- image-video-face
bestFor: Clustering web/search results into thematic groups (foam-tree/folders) to triage a noisy name or keyword query.
selectorsIn:
- name
- username
selectorsOut:
- metadata
- social-profile
status: live
pricing: free
opsec: passive
opsecNote: Runs queries through search backends and clusters the results; the target is not contacted. Queries are processed by Carrot2's service/backends — use a clean session for sensitive names.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Carrot2 is a real, long-running open-source search-results clustering engine. It clusters text results, not images — the image-video category placement is a harvest artifact.
missingPersonsRelevance: medium
coverage: [global]
auth: none
api: true
localInstall: true
registration: false
aliases: []
tags:
- visual-search-and-clustering-search-engines
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Carrot2

> An open-source search-results clustering engine — it takes a noisy query and groups the hits into labeled themes so you can see the shape of what's out there.

## When to use
You search a common `name` or `username` and get hundreds of mixed results (a celebrity namesake, a business, the actual person). Carrot2 clusters those results into thematic folders ("athlete," "obituary," "arrest," a city, an employer), letting you jump straight to the cluster that matches your subject instead of paging through noise.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://search.carrot2.org.
2. Enter the name/keyword and pick a source (web search / your own documents).
3. Read the cluster tree or FoamTree visualization; click a cluster to see its grouped results.
4. Pivot: a revealing cluster label (an employer, a town, a forum) becomes your next targeted query; result links lead to `social-profile`/`metadata`.

## Inputs → Outputs
- **In:** `name` / `username` / keyword query
- **Out:** clustered web results → thematic labels, candidate `social-profile` links, contextual `metadata`
- **Empty/negative result looks like:** thin or generic clusters ("more," "other") when the query is too rare or too broad — refine terms.

## Gotchas & OpSec
- It clusters TEXT search results, not images, despite this entry's category — set expectations accordingly.
- Quality depends on the underlying search backend's results; clustering only reorganizes, it does not find new pages.
- Passive; can also be self-hosted (open source) and offers an API if you want it off third-party infrastructure.

## Overlaps ("do both")
- Pair with raw Google/Bing searches: run the query directly, then Carrot2 to triage; also good over your own collected documents.

## Trust & verifiability
`trust: community` — established open-source project with a public demo, API, and self-host option. The engine is reliable; clustered results are still third-party content to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | carrot2 |
| category | image-video-face |
| selectorsIn → selectorsOut | name, username → metadata, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

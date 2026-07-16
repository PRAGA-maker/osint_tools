---
id: yacy
name: YaCy
description: Use when you want to run web searches through a decentralized, self-hosted engine with no central logging — returns `domain`/page results from a peer-to-peer index.
url: https://yacy.net
category: search-engines
path:
- search-engines
bestFor: A self-hosted, peer-to-peer search engine you fully control — useful for private searching and for crawling/indexing a defined set of sites yourself.
selectorsIn:
- name
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open source (GPL). No account; you run the software yourself.
opsec: passive
opsecNote: When self-hosted, your queries run locally against a P2P index rather than a central provider that logs you — good for query privacy. Note that in P2P mode your node exchanges index data with peers; run in a controlled/"robinson" mode if you need full isolation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: docker
trust: community
trustNote: Long-standing open-source project; the code is auditable and results come from your own/peer crawls rather than a commercial black box.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- Yacy
- yacy.net
tags:
- toddington
- curated-directory
- search-engines
- decentralized
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
---

# YaCy

> A free, open-source, decentralized search engine you host yourself — search without a central provider logging your queries, and build your own topical index by crawling chosen sites.

## When to use
You want to search the web (or a curated set of sites) through an engine you control, without your queries going to a commercial search provider — either for query-privacy reasons or because you want to crawl and index a specific set of `domain`s yourself for repeatable OSINT searching. It complements, rather than replaces, mainstream engines.

## How to use it (`bestInteractionPattern`: docker)
1. Install YaCy from https://yacy.net — run the Java app directly or via the official Docker image on your own machine/server.
2. Open the local web UI (default `http://localhost:8090`).
3. Choose a mode: join the global peer-to-peer index, or run in isolated ("robinson") mode indexing only what you crawl.
4. Optionally start crawls of specific sites you want indexed (`domain`).
5. Search from the local UI; read the output: web page results (`domain`) from the P2P/your-own index. Pivot into those pages as you would any search hit.

## Inputs → Outputs
- **In:** a query — a `name`, keyword, or `domain` to crawl
- **Out:** `domain` (matching web pages from the decentralized/self-crawled index)
- **Empty/negative result looks like:** sparse or no results — the P2P index has far less coverage than Google, and a fresh self-hosted node knows only what it has crawled.

## Gotchas & OpSec
- Requires local install (Java/Docker) and some setup — it is not a hosted website you just visit.
- Index coverage is much smaller than mainstream engines; treat it as a privacy-preserving supplement, not a primary web search.
- OpSec: self-hosting keeps queries off commercial engines, but default P2P mode shares index data with peers — use isolated mode for full query isolation.

## Overlaps ("do both")
- Complements mainstream and privacy meta-search engines: use YaCy for controlled/self-indexed searching, and a broad engine for coverage; combine for both reach and privacy.

## Trust & verifiability
`trust: community` — a mature open-source project. Results are as trustworthy as the sites crawled; there is no opaque ranking vendor, but also no guarantee of comprehensive coverage.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yacy |
| category | search-engines |
| selectorsIn → selectorsOut | name, domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | docker |
| opsec | passive |
| human-in-loop | no |

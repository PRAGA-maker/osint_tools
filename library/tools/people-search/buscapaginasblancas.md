---
id: buscapaginasblancas
name: BuscaPaginasBlancas
description: Use when you have Spanish surnames and want listed name/phone/address records — a Python scraper of Spain's Páginas Blancas, now defunct because the source endpoint was permanently shut down.
url: https://github.com/GeiserX/BuscaPaginasBlancas
category: people-search
path:
- people-search
bestFor: Historically, bulk-scraping Spain's Páginas Blancas white-pages directory into a local database by surname.
selectorsIn:
- name
selectorsOut:
- name
- phone
- address
status: down
pricing: free
costNote: Free open-source (Python) on GitHub, but non-functional — the repository was archived in April 2026 after the Páginas Blancas endpoint it scraped was permanently shut down (GDPR/LOPDGDD enforcement).
opsec: active
opsecNote: When it worked, it scraped a live third-party directory directly from your IP (active, ToS-sensitive). Moot now that the endpoint is dead — but any successor tool scraping Spanish personal data raises the same GDPR/legal exposure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A small community Python project (single author), now archived and inoperable because its data source was taken offline.
missingPersonsRelevance: high
coverage:
- es
auth: none
api: false
localInstall: true
registration: false
aliases:
- GeiserX/BuscaPaginasBlancas
- Paginas Blancas scraper
tags:
- people-investigations
- spain
- white-pages
- scraper
source: awesome-osint
lastVerified: '2026-07-15'
enrichment: full
relatedTools:
- wayback-archive
- website-diff
---

# BuscaPaginasBlancas

> A Python CLI that once scraped Spain's Páginas Blancas white-pages directory into a local database — now defunct: its source endpoint was permanently shut down and the repo archived.

## When to use
Effectively **not anymore**. It was built to bulk-look-up Spanish residents by surname — returning listed name, phone, address, postcode and city into a local SQLite database. That capability is gone: the Páginas Blancas endpoint it depended on was taken offline (GDPR/LOPDGDD privacy enforcement) and the author archived the project in April 2026. Documented here so you recognize it as a dead end and reach for a live alternative instead of burning time on it.

## How to use it (`bestInteractionPattern`: cli)
1. (Historical) Clone `https://github.com/GeiserX/BuscaPaginasBlancas`, `pip install requests beautifulsoup4`.
2. (Historical) Run `python3 crawler.py` with a surname list; results deduplicated into `paginasblancas.db`.
3. **Today:** the crawler returns nothing — the upstream directory endpoint no longer responds. Don't rely on it; skip to a working Spanish people-search route.

## Inputs → Outputs
- **In:** `name` (surnames)
- **Out (historical):** `name`, `phone`, `address` from public white-pages listings
- **Empty/negative result looks like:** everything — the tool now returns no data because the source is dead. Treat any run as a null and move on.

## Gotchas & OpSec
- **Defunct:** the core dependency (Páginas Blancas endpoint) is permanently down; the code runs but harvests nothing.
- Scraping Spanish personal data was always GDPR-sensitive — the shutdown was a privacy-enforcement outcome; any replacement carries the same legal risk.
- Kept in the library as a signpost, not a working tool.

## Overlaps ("do both")
- Pairs with (i.e., is replaced by) live Spanish sources — the official electoral/census routes, Spanish company registries (Registro Mercantil), and general people-search engines that still cover Spain.

## Trust & verifiability
`trust: community` — a genuine but now-archived hobby scraper. Its historical output was as reliable as the public directory; today it produces nothing, so verify Spanish subjects through currently-operational sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | buscapaginasblancas |
| category | people-search |
| selectorsIn → selectorsOut | name → name, phone, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |

---
id: search-engines-index
name: Search Engines Index
description: Use when you have a subject tied to a specific country and want that country's local search engines to query — returns a directory of national/regional search engines by location.
url: https://www.searchenginesindex.com/
category: search-engines
path:
- search-engines
bestFor: Finding the right country-specific search engine before searching a subject in a non-English-speaking region.
selectorsIn:
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free directory; no account or payment.
opsec: passive
opsecNote: Browsing the directory is passive and reveals nothing about your target. OpSec depends on the downstream national engine you then use.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-maintained directory (same operator as newspaperindex.com); it catalogs other engines rather than holding data itself, and listings can go stale.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- searchenginesindex.com
- search engines by country
tags:
- curated-directory
- specialty-search
- country-search
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Search Engines Index

> A directory of search engines organised by country and region — the jumping-off point when a general web search under-covers a subject's local internet.

## When to use
Your subject is tied to a specific country and Google alone under-indexes that region's web. Search Engines Index lists national and regional search engines by location, so you can pick a local engine (which often indexes local-language sites, directories, and forums Google misses) before running your actual `name` search there. Especially useful for Asia, Africa, the Middle East, and Eastern Europe where local engines outperform global ones.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.searchenginesindex.com/.
2. Browse to the subject's continent/country to see the search engines catalogued for that location.
3. Open a listed national engine and run your real query (`name`, `username`) there, in the local language if possible.
4. Pivot: local-engine results (`social-profile`s, local directories, news) feed the rest of your workflow. Repeat with a second national engine for coverage.

## Inputs → Outputs
- **In:** a subject `name` plus a target country/region.
- **Out:** a list of country-specific search engines to use (the directory), which then yield local `social-profile`s and pages.
- **Empty/negative result looks like:** a country with few or dead listings — the directory is finite and some entries rot; fall back to Google with `site:` and local-language terms.

## Gotchas & OpSec
- It's a directory, not a search engine: expect a second hop to the actual national engine.
- Some listed engines may be defunct or rebranded — verify the target engine loads before relying on it.
- Passive at the directory level; assess OpSec per downstream engine.

## Overlaps ("do both")
- Similar in spirit to `[[klug-suchen]]` (Germany-specific) but global by country. Pair with general web search and country people-search tools.

## Trust & verifiability
`trust: community` — a curated third-party index of other engines. It routes you to sources; result trustworthiness depends on the national engine you land on, not on this directory.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-engines-index |
| category | search-engines |
| selectorsIn → selectorsOut | name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

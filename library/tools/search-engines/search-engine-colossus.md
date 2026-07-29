---
id: search-engine-colossus
name: Search Engine Colossus
description: Use when your subject has a foreign/regional nexus and you need that country's own search engines — returns a directory of search engines by country and specialty.
url: http://www.searchenginecolossus.com/
category: search-engines
path:
- search-engines
bestFor: Finding country-specific and specialized search engines to search a subject in their local web.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free directory; no account, no charge for listings. Long-running (since 1998).
opsec: passive
opsecNote: A static directory of links — you submit no subject data to it, so browsing is fully passive. The search engines it points you to are where any actual (still passive) querying happens.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A 25+-year-old hand-maintained directory (last refreshed 2023); a curated index of links, only as current as its last update.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Search Engine Colossus
- searchenginecolossus.com
tags:
- search-engines
- directory
- regional
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# Search Engine Colossus

> A long-standing directory of the world's search engines organized by country and specialty — the map you use to find the *right local* search engine before you search.

## When to use
Your subject has a foreign or regional footprint and Google/Bing under-cover that country's web. Search Engine Colossus lists search engines per country/territory (plus academic, news, video, and other specialty categories), so you can pick the domestic engine that actually indexes local sites, directories, and press. It's a meta/navigation tool — it doesn't search *for* you; it tells you *where* to search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.searchenginecolossus.com/.
2. Browse to the target country (or a specialty category).
3. Pick a listed local search engine and open it.
4. Run your subject selectors (`name`, `username`, etc.) there — often with better local coverage than global engines.
5. Repeat across a couple of local engines; regional coverage varies.

## Inputs → Outputs
- **In:** none (you browse by country/specialty)
- **Out:** links to country-specific and specialized search engines to use next
- **Empty/negative result looks like:** a listed engine is dead or now redirects (the directory is only refreshed periodically) — skip to another entry for that country.

## Gotchas & OpSec
- **A directory, not a search engine** — its value is pointing you to local engines; the real work happens on those.
- Hand-maintained and only periodically updated (last ~2023) — some links may be stale.
- OpSec: **passive** — no subject data touches this site; keep normal hygiene on the engines it sends you to.

## Overlaps ("do both")
- Complements your primary search engines — use Colossus to add local/regional engines to a subject sweep so you don't miss country-specific results mainstream engines bury.

## Trust & verifiability
`trust: community` — a real, durable, curated directory; trustworthy as a link index, but verify each destination engine is still live before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-engine-colossus |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: search-22
name: Search-22 FTP Search Tools
description: Use when you have a filename, document title or keyword and want to find it on public FTP/file-sharing servers — a one-page launcher for 10+ FTP/file search engines.
url: https://search-22.com/ftp-search-tools
category: search-engines
path:
- search-engines
bestFor: Hunting exposed files (documents, media, leaked material) across public FTP indexers from a single directory page.
selectorsIn: []
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free directory page linking to free FTP/file-search engines; no account needed.
opsec: passive
opsecNote: The page itself is just links — you don't reveal anything by loading it. Exposure begins when you query a destination FTP indexer, which sees your search term and IP. Use a sock-puppet browser/VPN for the actual file searches and never download unknown files onto your investigative machine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running curated directory (Search-22.com, active since 2002); it aggregates third-party FTP indexers whose coverage and freshness vary — verify any file you find directly.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Search 22
- Search-22
tags:
- Search engines
- Filesharing Search Engines
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Search-22 FTP Search Tools

> A single directory page that launches your query across 10+ FTP and file-sharing search engines (NAPALM FTP Indexer, Archie mirrors, shared-file indexers) — a jump-off point for finding exposed files.

## When to use
You're looking for a specific file, document, or media item — a filename, a report title, a leaked document, a photo set — and want to check whether it sits on a publicly-indexed FTP or file-sharing server. Rather than remembering each FTP indexer's URL, Search-22 collects them on one page so you can fan a filename/keyword across all of them.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://search-22.com/ftp-search-tools.
2. Pick an FTP search engine from the list (e.g. NAPALM FTP Indexer) and enter your filename or keyword there.
3. Repeat across the other listed indexers — coverage differs, so a file missing on one may appear on another.
4. Pivot: a hit gives you a hosting server/path (`document-id`-like locator); the containing directory often exposes related files and an owning host/domain to investigate further.

## Inputs → Outputs
- **In:** a filename, document title, or keyword (free text, not a strict selector)
- **Out:** links to files on public FTP/file servers (a locator you can treat as `document-id`); the host/domain is a further pivot
- **Empty/negative result looks like:** no indexer returns the file — it may not be on a public FTP, may have been removed, or the indexer's crawl is stale. Absence here is not proof the file doesn't exist elsewhere.

## Gotchas & OpSec
- It's a launcher, not an index — result quality and logging belong to each destination engine.
- FTP indexers are patchy and often out of date; try several before concluding a file isn't public.
- Treat any downloaded file as untrusted (malware risk) and don't open it on your main system.

## Overlaps ("do both")
- Complements general web/file search: use Search-22 for the FTP/file-sharing layer specifically, then a mainstream search engine for web-hosted copies of the same document.

## Trust & verifiability
`trust: community` — a durable curated directory. It vouches for nothing about the files themselves; always open and verify a hit at its source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-22 |
| category | search-engines |
| selectorsIn → selectorsOut |  → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

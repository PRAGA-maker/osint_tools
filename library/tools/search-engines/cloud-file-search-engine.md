---
id: cloud-file-search-engine
name: Cloud File Search Engine
description: Use when you have a `name`/keyword and want to find files publicly shared on cloud lockers (Mega, MediaFire, etc.) — returns links to matching hosted files.
url: http://filesearch.link
category: search-engines
path:
- search-engines
bestFor: Keyword search across many file-sharing/cloud-locker hosts at once to locate publicly shared documents, media or archives.
selectorsIn:
- name
selectorsOut:
- document-id
status: degraded
pricing: freemium
costNote: Free to search; monetised via ads/host referrals. No account required.
opsec: passive
opsecNote: You submit a search term to a third-party engine — keep queries generic and use a sock-puppet browser/IP; do not download unknown files on your real machine. Treat any hosted file as untrusted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Anonymous aggregator that indexes third-party file lockers; result quality and safety of linked files are unvetted, and the root has been observed returning 503 (bot-blocking / intermittent).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- filesearch.link
- Mega file search
tags:
- Search engines
- Filesharing Search Engines
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Cloud File Search Engine

> A keyword search across dozens of file-sharing hosts (Mega, MediaFire and similar) — for locating publicly shared files, not for looking up a person directly.

## When to use
You have a `name`, filename, or distinctive keyword and want to find files that have been publicly shared on cloud lockers — e.g. a leaked document, a shared media set, or an archive whose name matches your subject. It searches file hosts, not people, so relevance is indirect.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://filesearch.link (sock-puppet browser). If it returns a 503/blank, retry later or via the per-host paths like `filesearch.link/meganz/`.
2. Enter a filename or keyword and search; it fans the query across the indexed hosts (Mega, MediaFire, etc.).
3. Review the result list; each hit links out to the file on its host.
4. Do NOT open/download unknown files on your real system — inspect metadata first, download only in a sandbox if at all.

## Inputs → Outputs
- **In:** `name` / filename / keyword
- **Out:** links to hosted files (`document-id`-style references)
- **Empty/negative result looks like:** no hits, or dead links to files already removed from the host — common, since shared files are frequently taken down.

## Gotchas & OpSec
- Human-in-the-loop: none in the search, but expect broken links and mislabelled results.
- OpSec: passive but you disclose your query to an anonymous operator — keep terms generic, never search sensitive personal identifiers you would not want logged.
- Safety: indexed files are untrusted; malware risk is real — sandbox any download.

## Overlaps ("do both")
- Complements general search-engine dorking: this reaches file-locker content that Google often does not index, while broad web search covers everything else.

## Trust & verifiability
`trust: unverified` — an anonymous third-party aggregator with intermittent availability; treat both its results and any file it links to with caution and independent verification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cloud-file-search-engine |
| category | search-engines |
| selectorsIn → selectorsOut | name → document-id |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

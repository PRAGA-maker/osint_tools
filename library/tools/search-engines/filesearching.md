---
id: filesearching
name: Filesearching
description: Use when you have a filename, keyword, or `document-id` and want to locate it across public FTP servers worldwide, filtered by file type and top-level domain — returns direct file/host locations.
url: https://filesearching.com
category: search-engines
path:
- search-engines
bestFor: Finding specific files (documents, media, archives) exposed on public FTP servers, scoped by filetype and country TLD.
selectorsIn:
- document-id
selectorsOut:
- document-id
- domain
status: degraded
pricing: free
costNote: Free to search; no account required.
opsec: passive
opsecNote: You search Filesearching's own index of FTP servers, so the file's owner isn't notified by the search. Connecting to a discovered FTP host to download, however, reveals your IP to that server — use a VPN and a disposable client if you retrieve anything.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Long-standing Russian FTP search engine (aka FileSearch.ru); index age and coverage are uncertain and it intermittently blocks automated access, so treat results as leads to confirm by connecting to the host.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- FileSearch.ru
- filesearching.com
tags:
- ftp-search
- file-search
- documents
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Filesearching

> A search engine over public FTP servers — find a specific file by name and type across thousands of indexed hosts, filterable by top-level domain.

## When to use
You have a distinctive filename, a `document-id`, or a keyword and want to know if that file (or files like it) is sitting on a public FTP server somewhere. FTP indexes are an old but still-useful OSINT surface for exposed documents, media, backups, and archives that never made it onto the web. Reach for it when a leak or artifact might live on open FTP rather than HTTP, or when you want to scope a search to a particular country via TLD.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://filesearching.com.
2. Enter the filename or keyword; set the **file type** filter (document, video, music, archive, etc.) and optionally a **top-level domain** to scope by country.
3. Run the search and read the hits — each is a file on a specific FTP host (server + path).
4. Verify a promising hit by connecting to the FTP host directly (through a VPN) to confirm the file exists and is what it claims.
5. Pivot: the host `domain`/IP becomes an infrastructure lead; the file itself feeds document-metadata analysis.

## Inputs → Outputs
- **In:** `document-id` / filename / keyword (+ filetype and TLD filters)
- **Out:** `document-id` (located files) and the `domain`/host serving them
- **Empty/negative result looks like:** no hits — the file isn't in Filesearching's index (which is partial and can be stale), not proof it's absent from all FTP; try alternate filenames or another FTP search engine.

## Gotchas & OpSec
- Status is **degraded**: the front end intermittently returns 503 to automated clients — use a normal browser, and expect variable availability.
- Index freshness is uncertain; a listed file may already be gone. Confirm by connecting.
- OpSec: searching is passive, but *downloading* from a discovered FTP exposes your IP to that server — use a VPN.

## Overlaps ("do both")
- Complements web search dorks and other FTP/file search engines: HTTP dorks miss FTP-only exposures and vice versa — run both when hunting for a leaked or exposed file.

## Trust & verifiability
`trust: unverified` — a legacy third-party index of uncertain currency and reliability; every hit is a lead to verify by connecting to the actual host, not a confirmed live file.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | filesearching |
| category | search-engines |
| selectorsIn → selectorsOut | document-id → document-id, domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

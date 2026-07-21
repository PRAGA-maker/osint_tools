---
id: od-search-tool
name: OD Search Tool (Open Directories)
description: Use when you have a filename, `name` or keyword and want files sitting in exposed open web directories — returns direct links to publicly listed files (docs, media, backups) on unprotected servers.
url: https://open-directories.reecemercer.dev
category: search-engines
path:
- search-engines
bestFor: Searching indexed open directories for exposed files by keyword or filename.
selectorsIn:
- name
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free web tool; no account or payment required.
opsec: passive
opsecNote: Searching the index is passive, but DOWNLOADING a discovered file connects you directly to that (often unsecured, sometimes hostile) server, which logs your IP. Fetch discovered files through a VPN/sandbox, never from your real environment.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Independent hobby project (by Reece Mercer) that queries open-directory indexes; coverage depends on what has been crawled and the hosted app could disappear without notice.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- open-directories.reecemercer.dev
- Reece Mercer Open Directory
tags:
- toddington
- curated-directory
- specialty-search
- open-directories
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# OD Search Tool (Open Directories)

> A search box over exposed open web directories — find files people left publicly listable on unprotected servers, by filename or keyword.

## When to use
You're hunting for a specific file or for documents/media that mention a subject, and you suspect it's sitting in an "open directory" (a web server with directory listing enabled, indexing its files publicly). This tool queries open-directory crawls so you can find leaked documents, backups, photo dumps, spreadsheets, or media by keyword — content that ordinary search engines often don't surface. Useful for recovering a leaked file, or finding photos/documents tied to a `name`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://open-directories.reecemercer.dev.
2. Enter a filename, a person's `name`, or distinctive keywords.
3. Review the results — each hit is a direct link to a file (or listing) sitting in a publicly exposed directory, with its filename and host.
4. **Before opening anything**, route through a VPN/sandbox; then download and inspect the file. Documents and images may carry authoring metadata and EXIF revealing device, author, and location.
5. Pivot: a recovered image feeds reverse-image + EXIF (`metadata-exif`) analysis; a document's properties can leak an author `name`, `employer-org`, or creation `geolocation`.

## Inputs → Outputs
- **In:** filename / `name` / keyword
- **Out:** direct links to exposed files; opened files can yield `metadata-exif` (author, device, GPS) and document properties
- **Empty/negative result looks like:** no results — the file/term isn't in any crawled open directory (most content isn't). Absence here says nothing about whether a file exists elsewhere; try other open-directory engines.

## Gotchas & OpSec
- **Downloading is the risk, not searching:** exposed servers are frequently misconfigured and sometimes deliberately hostile — fetch discovered files only in a sandbox behind a VPN.
- Coverage is limited to what the underlying crawl has indexed and is heavily biased toward media/software dumps.
- The hosted app is a personal project and may go offline — have alternative open-directory search engines ready.

## Overlaps ("do both")
- Pairs with other open-directory search engines (ODCrawler, opendirsearch) for broader coverage, and with EXIF/metadata tools to squeeze intel out of any file you recover.

## Trust & verifiability
`trust: unverified` — an independent hobby tool over third-party crawls. Results are real file links but their provenance is unknown; verify what a file actually is (and scan it) before trusting or acting on its contents.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | od-search-tool |
| category | search-engines |
| selectorsIn → selectorsOut | name → metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

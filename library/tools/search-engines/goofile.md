---
id: goofile
name: Goofile
description: Use when you have a `domain` and want to find public files of a given type hosted on it — returns URLs of documents (pdf, docx, xls, etc.) that may carry `metadata-exif` and names.
url: https://www.kali.org/tools/goofile/
category: search-engines
path:
- search-engines
bestFor: Enumerating files of a specific extension on a target domain for document/metadata recon.
selectorsIn:
- domain
selectorsOut:
- document-id
- metadata-exif
status: live
pricing: free
costNote: Free, open-source CLI packaged in Kali Linux. Reliable use benefits from a (free-tier) Google Custom Search API key/CSE ID to avoid scraping blocks.
opsec: active
opsecNote: It runs search-engine queries (optionally via Google CSE) from your IP to enumerate a target's files — active reconnaissance against the domain owner's exposed documents. Use a sock-puppet IP/API key; downloading the found files is a further active step.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A long-standing recon utility maintained in the Kali repositories (v1.6, updated 2025); it depends on search-engine access, so results vary with engine cooperation and any API key you supply.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
invitationOnly: false
aliases:
- goofile kali
- goofile filetype search
tags:
- document-recon
- filetype-search
- kali
source: metaosint
lastVerified: '2026-07-17'
enrichment: full
relatedTools:
- kali-linux
- kali-linux-os
---

# Goofile

> A command-line filetype search: point it at a domain and an extension, and it enumerates public files of that type hosted there — the raw material for document and metadata recon.

## When to use
You have a `domain` linked to a subject or organisation and want the documents it has published — PDFs, Office files, spreadsheets — because those files frequently leak author names, usernames, software versions, and GPS/`metadata-exif`. Goofile automates the `site:domain filetype:ext` style search so you can pull a list of file URLs quickly, then download and inspect their metadata.

## How to use it (`bestInteractionPattern`: cli)
1. Install via Kali (`apt install goofile`) or from source; ensure Python 3 + `python3-requests`.
2. Run: `goofile -d targetdomain.com -f pdf` (swap `pdf` for docx, xls, etc.). Supply a Google CSE key/ID (`-k`/`-e`) for reliable results, since unauthenticated scraping is often blocked.
3. Read the output: a list of matching file URLs on the domain.
4. Download the files and run them through a metadata extractor (e.g. metagoofil/ExifTool) to pull authors, usernames, and GPS.
5. Pivot: leaked author names/usernames feed people/username OSINT; `metadata-exif` GPS feeds geolocation.

## Inputs → Outputs
- **In:** a `domain` + a file extension.
- **Out:** URLs of public files of that type (`document-id`), which then yield embedded `metadata-exif`.
- **Empty/negative result looks like:** no files returned — the domain hosts none of that type, they aren't indexed, or the engine blocked the query (supply an API key and retry).

## Gotchas & OpSec
- Search engines throttle unauthenticated scraping; without a Google CSE key results are often empty. This is a tool limitation, not proof of "no files."
- The real intelligence is in the files' metadata, not the URL list — always extract EXIF/document metadata after downloading.
- Active recon: queries and downloads touch third-party engines and the target's server; proxy and use a puppet key.

## Overlaps ("do both")
- Pairs with metagoofil (metadata extraction) and ExifTool — Goofile finds the files, those tools mine them. Combine with `site:`/`filetype:` manual dorking for coverage.

## Trust & verifiability
`trust: community` — a maintained Kali recon utility. The file list is only as complete as the search engine allows; verify each file exists and inspect its metadata directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | goofile |
| category | search-engines |
| selectorsIn → selectorsOut | domain → document-id, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |

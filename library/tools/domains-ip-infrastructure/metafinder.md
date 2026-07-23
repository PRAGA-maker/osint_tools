---
id: metafinder
name: MetaFinder
description: Use when you have a `domain` and want documents it has published plus their metadata — returns author `name`s, `username`s, software, and paths from file `metadata-exif`.
url: https://github.com/Josue87/MetaFinder
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Harvesting a domain's public documents via search engines (incl. Baidu) and extracting author/software metadata.
selectorsIn:
- domain
selectorsOut:
- name
- username
- metadata-exif
status: live
pricing: free
costNote: Free and open-source; run locally with Python.
opsec: passive
opsecNote: "MetaFinder finds documents through search engines (Google/Bing/DuckDuckGo/Baidu) and then downloads the files to read their metadata. The search phase is passive, but downloading the documents fetches them from wherever they're hosted (often the target's own site), which can appear in that server's logs — route it through a proxy/VPN and a sock-puppet identity."
humanInLoop: false
humanInLoopReason:
- captcha
bestInteractionPattern: cli
trust: community
trustNote: Open-source tool by Josue87 (author of other well-regarded recon tools); metadata it extracts is only as accurate as the documents' own embedded fields.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- analyticsrelationships
aliases:
- MetaFinder
- Josue87/MetaFinder
tags:
- Domain/IP/Links
- Website's files metadata analyze and files downloads
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# MetaFinder

> Finds the documents a domain has published (searching Google, Bing, DuckDuckGo — and notably Baidu) and pulls the author, software, and path metadata out of each file.

## When to use
You have a `domain` (a company, org, or a person's site) and want to discover the PDFs/Office/image files it has leaked onto the web, then mine their `metadata-exif` for internal `username`s, author `name`s, software versions, and local file paths — the classic "who inside this org made this document" pivot. Its Baidu coverage often surfaces files the Western engines miss. Infrastructure/org-recon, so low direct missing-persons relevance.

## How to use it (`bestInteractionPattern`: cli)
1. Install from https://github.com/Josue87/MetaFinder (clone + `pip install` its requirements).
2. Run against a domain: `metafinder -d target.com -l 50 -o output -go -bi -du -ba` (limit, output, and enable Google/Bing/DuckDuckGo/Baidu).
3. It searches for indexed documents, downloads them, and extracts embedded metadata.
4. Read the report: usernames, author names, creation software, and paths gathered across all files.
5. Pivot a discovered `username`/`name` into people/social search; feed the software/versions into other recon.

## Inputs → Outputs
- **In:** `domain`
- **Out:** author `name`s, `username`s, `metadata-exif` (software, paths, dates) from the domain's public documents
- **Empty/negative result looks like:** few/no documents found or metadata stripped — the org may publish little, or scrub metadata before upload; absence isn't proof no documents exist.

## Gotchas & OpSec
- Search engines throttle/CAPTCHA automated queries; expect to pace requests or rotate, and Baidu results can be noisy.
- Downloading the files hits their host directly — proxy it so the target's logs don't see you.
- Many modern workflows strip metadata; a clean file yields nothing, and old files are where the gold usually is.

## Overlaps ("do both")
- Pairs with [[analyticsrelationships]] and general metadata viewers — MetaFinder gathers the documents and bulk-extracts fields; a dedicated EXIF viewer confirms a single high-value file in detail.

## Trust & verifiability
`trust: community` — a transparent open-source tool from a known author; the metadata is extracted verbatim from the files, so it's authentic but only as complete as what the document creators left embedded.

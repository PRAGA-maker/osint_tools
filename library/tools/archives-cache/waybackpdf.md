---
id: waybackpdf
name: WaybackPDF
description: Use when you have a `domain` and want every PDF the Internet Archive holds for it — returns document-id files that often carry names and metadata.
url: https://github.com/Haax9/WaybackPDF
category: archives-cache
path:
- archives-cache
bestFor: Bulk-collecting all archived PDFs for a domain from the Wayback Machine — reports, filings and documents that may name people or carry revealing metadata.
selectorsIn:
- domain
selectorsOut:
- document-id
- metadata-exif
status: live
pricing: free
costNote: Free open-source script; no account or key required.
opsec: passive
opsecNote: It queries and downloads from the Internet Archive, not the live target site, so the domain owner is not contacted or alerted. Purely archive-side collection.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: A small single-author utility over the public Wayback CDX API; simple and inspectable, but coverage is bounded by what the Archive captured.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Haax9/WaybackPDF
tags:
- Archives
- Tools for working with web archives
- pdf
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# WaybackPDF

> A CLI that finds and downloads every PDF the Wayback Machine has archived for a domain — a fast way to harvest documents that name people or leak metadata.

## When to use
You're mining a `domain` tied to a subject (their org, a school, a small business) and want the documents it published over time: reports, newsletters, member lists, filings, resumes. WaybackPDF pulls the list of archived PDFs for the domain from the Internet Archive and downloads them into a folder, so you can grep them for names/emails and inspect PDF metadata (author, software, timestamps) — often the richest OSINT in an old document.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and install its (minimal) requirements per the README.
2. Run it against the target `domain`; it queries the Wayback CDX index for PDF URLs and downloads them to a local folder.
3. Review the harvested PDFs — full-text search for names/emails/phone numbers.
4. Inspect PDF metadata (`exiftool`/document properties) for author, organization, creation software and timestamps.
5. Pivot: names/emails found feed people- and email-OSINT; document authors and dates corroborate an identity or timeline.

## Inputs → Outputs
- **In:** a `domain`
- **Out:** downloaded archived PDFs (`document-id` files) plus their embedded `metadata-exif` (author, timestamps, software)
- **Empty/negative result looks like:** no PDFs found — the Archive captured none for that domain (small/rarely-crawled site), not that the site never hosted documents.

## Gotchas & OpSec
- Coverage is bounded by the **Internet Archive's crawl**; sparsely-archived domains yield little.
- Documents can be large/numerous — review responsibly and mind disk usage.
- A single-author script — read it before running and confirm findings against the archived original.

## Overlaps ("do both")
- Pairs with the Wayback Machine UI and `[[wayparam]]` — WaybackPDF grabs the documents in bulk, wayparam maps the domain's URL surface, and the Wayback UI serves individual archived pages.

## Trust & verifiability
`trust: unverified` — a small open-source utility over the public Wayback API; its output is archive-sourced and reproducible, so verifiable, but only as complete as the Archive's capture.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | waybackpdf |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → document-id, metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |

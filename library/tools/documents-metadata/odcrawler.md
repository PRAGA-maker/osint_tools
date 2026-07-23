---
id: odcrawler
name: ODCrawler
description: Use when you have a filename/keyword and want files exposed in open directories — returns links to matching files on indexed open web servers.
url: https://odcrawler.xyz/
category: documents-metadata
path:
- documents-metadata
bestFor: Searching across crawled "open directories" (unprotected web-server file listings) for documents, media, and archives by name.
selectorsIn:
- name
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free community search engine. No account.
opsec: passive
opsecNote: Searching ODCrawler's index is passive (you query their crawl, not the origin server). But CLICKING a result fetches the file directly from the hosting open directory — an active touch that server logs. Download through a proxy if the source matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-run open-directory search index (associated with the r/opendirectories community); crawl coverage is partial and volunteer-driven.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- ODCrawler
- odcrawler.xyz
- open directory search
tags:
- file-search
- open-directories
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# ODCrawler

> A search engine for "open directories" — the unprotected file listings servers accidentally expose — indexing tens of millions of files you can search by name.

## When to use
You're looking for a specific file, document, or media item that might be sitting in a misconfigured, publicly-listed web directory — leaked documents, a person's uploaded files, datasets, archives. ODCrawler crawls open directories and lets you search their contents by filename/keyword, returning direct links. It's a file-discovery tool; missing-persons relevance is low and indirect (surfacing documents or media tied to a subject that were left publicly listed).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://odcrawler.xyz/.
2. Search a filename, keyword, or extension (e.g. a `name`, a project title, `.pdf`, `.xlsx`).
3. Read results: each hit is a direct link to a file on some origin open directory, with size/type.
4. Assess and pivot: the containing directory path often reveals related files — browse up a level on the origin server. Feed found documents into metadata extraction (`[[pdfx]]`, ExifTool) for authorship/`metadata-exif` leads.

## Inputs → Outputs
- **In:** a filename/keyword (`name`, title, extension)
- **Out:** direct links to matching files (`document-id`-style items) on open web directories
- **Empty/negative result looks like:** no results — the file isn't in any directory ODCrawler has crawled; coverage is partial, so absence here doesn't mean the file isn't exposed somewhere (try other open-directory search engines / dorking).

## Gotchas & OpSec
- Coverage is partial and community-driven — it indexes only directories that have been submitted/crawled, not the whole web.
- **Clicking/downloading a result hits the origin server directly** (active), which logs your IP — proxy sensitive downloads.
- Open directories can host malware or illegal content; treat unknown files cautiously and never open executables casually.
- OpSec: searching is passive; retrieving files is active.

## Overlaps ("do both")
- Complements other open-directory search engines and Google dorking (`intitle:"index of"`) — run several, since each crawls a different slice. Found documents feed metadata tools like `[[pdfx]]`.

## Trust & verifiability
`trust: community` — a volunteer-run index; results are real links to real files, but coverage is incomplete and the hosting directories are unvetted, so verify and handle downloaded files with care.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | odcrawler |
| category | documents-metadata |
| selectorsIn → selectorsOut | name → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

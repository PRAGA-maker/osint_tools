---
id: filetype-search-tool
name: Filetype Search Tool (Aware Online)
description: Use when you have a `name`/keyword and want documents (PDF, DOC, XLS…) mentioning it — a helper that builds Google `filetype:` dorks for you — returns document leads.
url: https://www.aware-online.com/en/osint-tools/filetype-search-tool/
category: search-engines
path:
- search-engines
bestFor: Quickly building Google filetype: dorks to surface documents (PDFs, spreadsheets, docs) about a subject.
selectorsIn:
- name
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free browser helper from Aware Online; no account. It constructs the search query — Google runs it.
opsec: passive
opsecNote: The tool only assembles a query string locally; the actual search runs on Google from your browser, so Google (and any downloaded document's host) sees your activity. Use a sock-puppet browser/VPN, and open found documents cautiously — files can carry tracking or malware.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A free helper from Aware Online, a reputable OSINT training provider; it's a convenience wrapper around standard Google dorking, not a data source itself.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Aware Online filetype search
tags:
- google-dorking
- documents
- search
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Filetype Search Tool (Aware Online)

> A small form that builds Google `filetype:` dork queries — point a name or keyword at it and it constructs the search that surfaces PDFs, spreadsheets and documents mentioning your subject.

## When to use
You have a `name`, `employer-org` or keyword and want *documents* about it rather than web pages — CVs/résumés, reports, spreadsheets, slide decks, meeting minutes — which often carry contact details, associates, and rich EXIF/metadata. This helper assembles the `filetype:`/`ext:` Google dork so you don't hand-write the syntax, then runs it. It's a convenience wrapper around Google dorking; the results and their metadata are where the real intel is.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.aware-online.com/en/osint-tools/filetype-search-tool/.
2. Enter your `name`/keyword and pick the file type(s) (pdf, doc/docx, xls/xlsx, ppt…).
3. Let it build and launch the Google query (e.g. `"Jane Doe" filetype:pdf`).
4. Review the document hits; download the promising ones (cautiously).
5. Pivot: run downloaded files through an EXIF/metadata reader (`documents-metadata`) — author names, software, and GPS often leak more than the text.

## Inputs → Outputs
- **In:** `name`/keyword + target file type(s)
- **Out:** document hits (`document-id`-style file leads) that may contain contacts, associates and metadata
- **Empty/negative result looks like:** no documents of that type — try other extensions, name variants, or drop the quotes; absence just means nothing indexed matches.

## Gotchas & OpSec
- OpSec: passive query-building, but the search runs on Google and downloads hit the file's host — sock-puppet/VPN, and treat downloaded files as potentially tracked/malicious.
- It's a Google-dork helper: it only finds what Google has indexed, and Google rate-limits heavy dorking.
- The document text is half the value — always check the file's metadata too.

## Overlaps ("do both")
- Do both with EXIF/metadata readers in `documents-metadata` — this finds the files, those extract the author/software/GPS metadata inside them.

## Trust & verifiability
`trust: community` — a convenience wrapper from a reputable OSINT trainer; it faithfully builds standard dorks, so verifiability rests on Google's index and the documents themselves.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | filetype-search-tool |
| category | search-engines |
| selectorsIn → selectorsOut | name → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

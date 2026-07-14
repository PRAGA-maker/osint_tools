---
id: github-io-2
name: FilePhish (Greylens)
description: Use when you have a name, org or domain and want to surface publicly exposed documents (PDFs, spreadsheets, configs, backups) — returns document leads and their embedded metadata.
url: https://greylensresearch.github.io/filephish/
category: search-engines
path:
- search-engines
bestFor: Building filetype-targeted "dork" queries to hunt exposed documents across six search engines.
selectorsIn:
- name
- domain
selectorsOut:
- document-id
- metadata-exif
status: live
pricing: free
costNote: Free static web tool hosted on GitHub Pages; no account, no payment, no rate limit of its own (the underlying search engine's limits apply).
opsec: passive
opsecNote: FilePhish itself only assembles a query string in your browser — nothing is sent to the target. The actual search runs on Google/Bing/Yandex/etc., which log your IP and query. The document you eventually open, however, IS fetched from the host that published it, so open sensitive hits through a sock-puppet browser/VPN, not your attributable IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Built by Greylens Research and hosted on their GitHub Pages; it is a client-side query builder with no backend, so there is no data-collection risk, but it is a hobby project, not an audited service.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- FilePhish
- Greylens FilePhish
- filephish query builder
tags:
- searchengines
- Search Engines
- dorking
- document-discovery
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# FilePhish (Greylens)

> A client-side "dork" builder that turns a name, org or domain into filetype-targeted search queries for hunting publicly exposed documents.

## When to use
You have a `name`, `employer-org` or `domain` and want to find documents that person or organisation has published (or leaked) online — a résumé PDF, a membership spreadsheet, a scanned form, a config or backup file that named them. Instead of hand-writing `filetype:pdf "John Smith"` operators, FilePhish assembles the query for you and lets you fire it at six different engines, which surfaces files that plain web search buries.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://greylensresearch.github.io/filephish/ in a sock-puppet browser.
2. Type your subject term (a `name`, `domain`, or keyword) into the query box.
3. Pick a file category — documents (PDF/DOC), spreadsheets, presentations, archives, or the sensitive set (password files, configs, logs, databases, backups).
4. Choose a search engine (Google, Bing, Yandex, Baidu, Sogou, DuckDuckGo). Yandex and Baidu often index files the others miss.
5. Click to launch — the tool opens the constructed dork on that engine. Read the hits, then open promising files through your sock-puppet.
6. Pivot: any document you retrieve feeds a metadata extractor (`[[exif-data-viewer]]`) — author names, timestamps and GPS in the file's `metadata-exif` are often more revealing than the visible text.

## Inputs → Outputs
- **In:** `name`, `domain` (or a free-text keyword)
- **Out:** `document-id` (links to exposed files), `metadata-exif` (once you extract the file's embedded properties)
- **Empty/negative result looks like:** the engine returns zero file hits or only unrelated documents. Rotate the engine (try Yandex/Baidu) and loosen the filetype before concluding nothing is exposed.

## Gotchas & OpSec
- No human-in-the-loop on FilePhish, but the search engine you launch may throw a CAPTCHA after repeated dorks — solve it or switch engines.
- The tool is passive at the query-building stage; the moment you *open* a found file you fetch it from its host and may be logged there. Use a VPN/sock-puppet for anything sensitive.
- The "password/config/backup" categories can surface genuinely private data — stay within authorised-investigation scope and do not exfiltrate.

## Overlaps ("do both")
- Pairs with `[[exif-data-viewer]]` — FilePhish finds the document, the EXIF viewer pulls the author, software and GPS metadata out of it.
- Complements `[[google-com-77]]` and other raw search dorks — FilePhish just makes the filetype operators fast and multi-engine.

## Trust & verifiability
`trust: community` — a client-side, open GitHub Pages tool from Greylens Research with no backend, so it cannot harvest your queries, but treat it as a convenience wrapper around search operators rather than an authoritative data source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | github-io-2 |
| category | search-engines |
| selectorsIn → selectorsOut | name, domain → document-id, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

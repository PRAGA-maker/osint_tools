---
id: mamont
name: Mamont
description: Use when you have a filename, keyword, or `domain` and want to find files exposed on public FTP servers — returns file paths, hosting server addresses, and archived copies.
url: https://www.mmnt.ru/
category: search-engines
path:
- search-engines
bestFor: Searching ~20 years of indexed public FTP servers for files, documents, and media by name or keyword.
selectorsIn:
- domain
selectorsOut:
- domain
- document-id
status: live
pricing: free
costNote: Free public search engine; no account or payment required.
opsec: passive
opsecNote: Searching Mamont's index queries Mamont's servers, not the target FTP host. However, if you then open a returned ftp:// link you connect directly to that server, which logs your IP — use a VPN/sock-puppet before following file links.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running Russian FTP search engine (mmnt.ru); niche and community-known rather than institutional. Index is large but stale in places — verify a file still exists before relying on it.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- mmnt.ru
- Mamont FTP Search
tags:
- speciality-search-engines
- ftp
source: awesome-osint
lastVerified: '2026-07-18'
enrichment: full
---

# Mamont

> A specialized FTP search engine indexing roughly 3.7 billion files across thousands of public FTP servers — finds documents and media the general web search engines never touch.

## When to use
General web search covers HTTP; Mamont covers the FTP layer that Google largely ignores. Reach for it when you want a specific filename or a document leaked/mirrored on an open FTP server — corporate documents, media dumps, backups, or files tied to a target `domain`. Useful when a subject or organization once ran an FTP server, or when a document's filename is your only lead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.mmnt.ru/ (there is an English interface link; the default is Russian).
2. Enter a filename, keyword, or partial path into the search box and submit.
3. Read the results: each hit shows the file name, size, and the `ftp://` server address hosting it. Mamont also links archived copies via web.archive.org for files that have since vanished.
4. To retrieve a file, follow the `ftp://` link — but do this behind a VPN/sock-puppet (see OpSec).
5. Pivot: a hosting server's hostname/IP → WHOIS and infrastructure lookups; a document → its metadata (author, org) for further identity leads.

## Inputs → Outputs
- **In:** filename / keyword / `domain` fragment
- **Out:** file paths, hosting FTP server `domain`/address, archived copies, `document-id`-style file references
- **Empty/negative result looks like:** no rows returned — the file/keyword isn't in Mamont's FTP index; it does not mean the file never existed on the open web.

## Gotchas & OpSec
- The index spans ~20 years and is partly stale — a listed file may be gone; the archive.org fallback sometimes recovers it.
- Interface is Russian-first; use the English toggle or translate.
- Opening a returned `ftp://` link is an **active** step that connects you straight to the host and logs your IP — route through a VPN/sock-puppet.

## Overlaps ("do both")
- Complements general web and cache search: Mamont finds the FTP-hosted files those engines miss, so run it alongside your normal document search when a filename is the lead.

## Trust & verifiability
`trust: community` — a long-lived but niche third-party engine with no institutional backing; treat results as leads and confirm a file's continued existence and provenance before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mamont |
| category | search-engines |
| selectorsIn → selectorsOut | domain → domain, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

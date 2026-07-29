---
id: mamont-s-open-ftp-index
name: Mamont's Open FTP Index
description: Use when you have a filename/keyword and want files exposed on public FTP servers — returns FTP hosts and paths hosting matching files.
url: https://www.mmnt.net/
category: search-engines
path:
- search-engines
bestFor: Searching the contents of publicly accessible FTP servers for a filename or keyword.
selectorsIn:
- name
selectorsOut:
- domain
- ip-address
status: degraded
pricing: free
costNote: Free to search/browse; no account. A long-running but aging (copyright 2011) index, so coverage is dated.
opsec: passive
opsecNote: Searching the index queries mmnt.net, not the target. Actually connecting to a discovered FTP server to retrieve a file is a direct connection from your host to that server (logged there) — use a VPN/proxy if attribution matters, and only access data you are authorised to.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing independent FTP search engine ("Mamont", by Constantine Aygi). Genuine and historically useful, but the crawl is old — many indexed servers are gone, and results skew stale.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- napalm-ftp-indexer
- shodan
aliases:
- mmnt.net
- Mamont FTP search
tags:
- ftp-search
- file-search
- exposed-data
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Mamont's Open FTP Index

> A veteran search engine over publicly accessible FTP servers — type a filename or keyword and it points you to open FTP hosts serving matching files.

## When to use
When you're hunting for documents, media, or leaked files by name and want to check open FTP servers, which normal web search rarely indexes. Useful for finding a specific filename a subject may have exposed, or files hosted on misconfigured/public FTP tied to an organisation. A niche but occasionally decisive angle for document discovery.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.mmnt.net/.
2. Enter a filename or keyword in the search box (or browse the numbered index pages of known open FTP hosts).
3. Read results: matching files with their FTP host (`domain`/`ip-address`) and path.
4. To retrieve, open the FTP location in an FTP client/browser — but connect only to data you're authorised to access.
5. Pivot: an FTP host `domain`/`ip-address` feeds `[[shodan]]` and infrastructure lookups; the file itself feeds document/metadata analysis.

## Inputs → Outputs
- **In:** `name` (filename/keyword)
- **Out:** open FTP `domain`/`ip-address` hosts and file paths matching the query
- **Empty/negative result looks like:** no hits — the file isn't on an indexed open FTP, or (likely) the once-indexed server is long gone; corroborate with a live FTP indexer.

## Gotchas & OpSec
- The index is **old** (2011-era crawl) — expect dead hosts and stale listings. Treat hits as leads to verify live, not current facts.
- Connecting to a discovered FTP server is a direct, logged connection; use a proxy and stay within authorised scope.
- Public FTP contents can include sensitive/illegally-shared material; handle findings responsibly.

## Overlaps ("do both")
- Pairs with `[[napalm-ftp-indexer]]` — another FTP search engine with a different, sometimes fresher crawl. Do both, since each indexes a different slice of open FTP space. Use `[[shodan]]` to find currently-open FTP services directly.

## Trust & verifiability
`trust: community` — a real, long-lived tool but with a dated crawl (hence status: degraded). Verify each hit by attempting the live FTP location; the index only suggests where files once were.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mamont-s-open-ftp-index |

---
id: index-commoncrawl-org
name: index.commoncrawl.org
description: Use when you have a `domain` and want every URL Common Crawl captured for it — returns archived URLs (`document-id`s) with pointers to the stored page content.
url: https://index.commoncrawl.org/
category: archives-cache
path:
- archives-cache
bestFor: Querying Common Crawl's index to list all crawled URLs under a domain and fetch their archived content.
selectorsIn:
- domain
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free public dataset/index; no account or key. You can query the web UI or the CDX API programmatically.
opsec: passive
opsecNote: You query Common Crawl's own index/archive, not the target site — the target's server sees nothing. Fully passive; the only party seeing your query is Common Crawl.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Common Crawl is a well-established non-profit web-scale crawl; the index is authoritative for "what we crawled and when", though coverage of any given site is partial.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- common-crawl
- commoncrawl-org
- gau
aliases:
- Common Crawl Index
- CC index
- CDX API
tags:
- archive
- commoncrawl
- cdx
- urls
source: uk-osint
lastVerified: '2026-07-18'
enrichment: full
---

# index.commoncrawl.org

> The searchable front door to Common Crawl's petabyte web archive: ask "what URLs did you capture for this domain?" and get a list plus the offsets to pull the stored HTML.

## When to use
You have a `domain` and want an alternative/complement to the Wayback Machine for reconstructing its history — every path Common Crawl saw, including pages that may be gone from the live site and absent from other archives. Good for surfacing old profile URLs, uploaded files, and parameters, and for bulk analysis where you want the raw crawled content rather than a rendered snapshot.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://index.commoncrawl.org/ and pick a crawl (e.g. `CC-MAIN-2026-xx`) — each monthly crawl has its own index.
2. Query a domain with a wildcard, e.g. `*.example.com/*` (or `example.com/*`), via the collection's search box or the CDX API endpoint.
3. Read the JSON results: each row is a captured URL with timestamp, MIME type, HTTP status, and WARC file + offset/length.
4. To read a page: use the WARC pointers to fetch that record from the Common Crawl data (or feed the URL into another archive viewer).
5. Pivot: mine the URL list for usernames/emails/IDs in paths and query strings; cross-check gaps against [[gau]] and Wayback.

## Inputs → Outputs
- **In:** `domain` (with wildcards)
- **Out:** list of archived URLs (`document-id`s) with timestamps and WARC pointers to stored content
- **Empty/negative result looks like:** no rows for that domain in the chosen crawl — Common Crawl didn't capture it that month (try other crawls) or the site was never crawled; check a different archive before concluding it never existed.

## Gotchas & OpSec
- Human-in-the-loop: none; but you must query the **right crawl** — each monthly index is separate, so a domain absent from one crawl may appear in another.
- Coverage is broad but sampled, not exhaustive — Common Crawl doesn't capture every page of every site.
- Reading actual content means resolving WARC offsets (or using a helper), which is more technical than a Wayback snapshot.
- OpSec: fully passive; only Common Crawl sees your query.

## Overlaps ("do both")
- Pairs with [[gau]] (which aggregates this index plus Wayback/OTX/URLScan in one command) and [[commoncrawl-org]]; query here for precision, use gau to cast the widest net.

## Trust & verifiability
`trust: trusted` — Common Crawl is an established non-profit and its index is authoritative for what it crawled; just remember "not indexed" means "not captured in that crawl", not "never existed".

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | index-commoncrawl-org |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: gogetcrawl
name: GoGetCrawl
description: Use when you have a `domain` and want every URL/file it ever exposed from web archives — returns archived URLs and downloadable files from Wayback and Common Crawl.
url: https://github.com/karust/gogetcrawl
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Bulk-extracting a domain's historical URLs and files from the Wayback Machine and Common Crawl.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open source (Go, MIT). Usable as a CLI, a Go library, or via Docker. Queries public archives — no key.
opsec: passive
opsecNote: GoGetCrawl reads from the Wayback Machine and Common Crawl, not the target's live server, so the subject sees nothing — the archives already captured the pages. Only the archive services see your queries. This is a passive way to enumerate a site without touching it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A focused, maintained (2023) open-source archive-extraction tool. It's a client over reputable archives, so result quality is the archives' coverage; it fetches, it doesn't vouch.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- karust/gogetcrawl
- gau-like
tags:
- Domain/IP/Links
- web-archive
- url-extraction
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# GoGetCrawl

> A Go CLI/library that pulls a domain's entire archived history — every captured URL and downloadable file — out of the Wayback Machine and Common Crawl, without touching the live site.

## When to use
You have a target `domain` and want its *historical* footprint: URLs, paths, parameters, and files that existed at some point, including pages long since removed. This is a passive reconnaissance and evidence-recovery move — surface deleted content, old endpoints, exposed documents, or a site's structure as it was, all from archives.

## How to use it (`bestInteractionPattern`: cli)
1. Install the Go binary (or run the Docker image / import the Go package).
2. Query archived URLs for the domain, e.g. with a wildcard pattern and optional date range: it returns every capture Wayback/Common Crawl hold.
3. Filter — by file type, MIME, or status code — and use "collapse" to dedupe to unique URLs.
4. Download matching files directly to a directory with configurable concurrency when you need the actual content, not just the list.
5. Pivot: recovered URLs feed content review and endpoint discovery; downloaded documents feed metadata analysis (`[[single-file]]` for fresh captures, EXIF tools for media).

## Inputs → Outputs
- **In:** a `domain` (with optional URL pattern / date / type filters)
- **Out:** archived URLs for that `domain`, and optionally the downloaded files themselves
- **Empty/negative result looks like:** no results — the archives have no captures for that domain/pattern (obscure or never-archived sites), or your filters are too tight. Loosen filters or check the domain spelling.

## Gotchas & OpSec
- Coverage is the archives' coverage — Wayback/Common Crawl miss plenty; absence isn't proof a URL never existed.
- Large domains return huge lists; use collapse/filters and rate-awareness so you don't hammer the archive APIs.
- OpSec: **passive** — nothing touches the target's live server; only the archive services see your queries.

## Overlaps ("do both")
- Same niche as `gau`/`waybackurls` with a Go client and Common Crawl support — run more than one, since Wayback and Common Crawl each hold captures the other lacks. Combine with `[[subdomain-finder]]` for hosts.

## Trust & verifiability
`trust: community` — a maintained, single-purpose client over reputable public archives. Reliable at *retrieving* what the archives hold; the completeness and accuracy of results are bounded by the archives themselves.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gogetcrawl |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |

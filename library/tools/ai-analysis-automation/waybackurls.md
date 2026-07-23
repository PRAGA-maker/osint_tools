---
id: waybackurls
name: waybackurls
description: Use when you have a `domain` and want every URL the Wayback Machine has ever archived for it — returns historical `domain`/URL paths (old pages, parameters, exposed files) to mine.
url: https://github.com/tomnomnom/waybackurls
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Dumping all historically-archived URLs for a domain to find old/hidden pages and parameters.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source (tomnomnom); a single Go binary, no account or API key.
opsec: passive
opsecNote: Reads from the public Wayback Machine index rather than touching the target's live site, so it's low-footprint recon. The query goes to web.archive.org over your IP — route through a sock-puppet/VPN for sensitive targets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Widely-used, well-known recon utility from tomnomnom; the data is authoritative archive.org content, only as complete as what was crawled.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- tomnomnom/waybackurls
tags:
- other-tools
- recon
- wayback
- domain
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- gau
---

# waybackurls

> One-line recon: feed it a domain, get back every URL the Wayback Machine ever archived for it — including pages the live site no longer serves.

## When to use
You have a target `domain` and want its historical URL surface: old pages that were deleted, endpoints with revealing query parameters, documents and directories that were once linked, and subdomains. Because it pulls from web.archive.org rather than crawling the live site, it surfaces content the current site hides or has removed — useful for finding a person's or org's earlier web presence and forgotten exposures.

## How to use it (`bestInteractionPattern`: cli)
1. Install (Go): `go install github.com/tomnomnom/waybackurls@latest`.
2. Run against one domain: `echo example.com | waybackurls > urls.txt`, or pipe a list: `cat domains.txt | waybackurls`.
3. It prints every archived URL for `*.example.com`, one per line.
4. Triage: `grep` for interesting extensions (`.pdf`, `.xls`, `.bak`, `.sql`), parameters (`?id=`, `?email=`), or old subdomains.
5. Pivot: feed live-looking URLs into a fetcher/screenshotter; pull archived copies of removed pages from the Wayback Machine itself.

## Inputs → Outputs
- **In:** a `domain` (on stdin)
- **Out:** a line-delimited list of historically-archived URLs (`domain`/paths, parameters, files) for that domain and its subdomains
- **Empty/negative result looks like:** no output — archive.org never crawled the domain (young or obscure sites), not proof the site never existed; try Common Crawl / gau for wider coverage.

## Gotchas & OpSec
- Output includes long-dead URLs — many will 404 on the live site; that's expected (fetch the archived copy instead).
- Coverage depends entirely on what archive.org crawled; a quiet domain may have little history.
- OpSec: passive — you query the archive, not the target — but still use a sock-puppet IP for sensitive work.

## Overlaps ("do both")
- Pairs with `[[gau]]` (getallurls), which adds Common Crawl, URLScan and OTX sources — run both and merge for the widest historical URL set.

## Trust & verifiability
`trust: community` — a well-established open-source recon tool; the URLs are genuine archive.org records, so reliability equals the archive's crawl completeness.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | waybackurls |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |

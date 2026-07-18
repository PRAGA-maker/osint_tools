---
id: gau
name: GAU
description: Use when you have a `domain` and want every URL ever seen for it across web archives — returns a bulk list of historical URLs (`document-id`s) to mine.
url: https://github.com/lc/gau
category: archives-cache
path:
- archives-cache
bestFor: Bulk-harvesting all known/archived URLs for a domain from Wayback, OTX, Common Crawl, and URLScan in one command.
selectorsIn:
- domain
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free, open-source (MIT) Go binary; no account or key needed for the default sources.
opsec: passive
opsecNote: gau queries public archive/index services (Wayback, AlienVault OTX, Common Crawl, URLScan), NOT the target's live site — so the target's own server sees nothing. It does not hit the domain directly unless you pipe results into an active fetcher.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Widely used, well-maintained open-source recon tool by lc; results are only as complete/current as the upstream archives it aggregates.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- index-commoncrawl-org
- web-archive-org
aliases:
- getallurls
- lc/gau
tags:
- Archives
- recon
- wayback
- urls
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# GAU

> "Get All URLs": one command that pulls every URL known to Wayback, Common Crawl, AlienVault OTX, and URLScan for a domain — a fast map of a target site's history and hidden corners.

## When to use
You have a `domain` (a subject's personal site, a company, a forum they ran) and you want to see everything that's ever existed under it — deleted pages, old profile URLs, uploaded files, parameter-laden endpoints — without touching the live server. gau aggregates several archive/index sources at once, which is broader than querying the Wayback Machine alone.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `go install github.com/lc/gau/v2/cmd/gau@latest` (or grab a release binary).
2. Run: `gau example.com` — or feed many domains: `cat domains.txt | gau`.
3. Narrow as needed: `--subs` to include subdomains, `--providers wayback,commoncrawl,otx,urlscan`, `--from`/`--to` for date ranges, `--o out.txt` to save.
4. Read the output: a deduplicated list of historical URLs. Grep it for interesting patterns (`/profile`, `/user`, `.pdf`, `?email=`, upload paths).
5. Pivot: feed a promising archived URL into [[web-archive-org]] to view the saved page; mine query strings for usernames/emails/IDs.

## Inputs → Outputs
- **In:** `domain` (one or many)
- **Out:** bulk list of historical URLs (`document-id`s) across all providers
- **Empty/negative result looks like:** no URLs returned — the domain was never crawled/archived (very new, very obscure, or robots-blocked); absence isn't proof the site never existed.

## Gotchas & OpSec
- Human-in-the-loop: none; pure CLI. Some providers (e.g. URLScan) benefit from an API key for higher limits, but defaults work keyless.
- Output is raw and noisy — expect thousands of URLs on a large domain; filter aggressively.
- OpSec: **passive** by itself. Danger is downstream: if you then *fetch* those URLs against the live host you become active — throttle/proxy that step.
- Results only cover what the archives captured; recent or deliberately-excluded pages won't appear.

## Overlaps ("do both")
- Pairs with [[index-commoncrawl-org]] (query one index directly and precisely) and [[web-archive-org]] (view the actual saved snapshot); gau casts the widest net, the others let you drill in.

## Trust & verifiability
`trust: community` — a mature, widely-adopted open-source tool; the aggregation is reliable, but a URL appearing here only proves an archive saw it once, so confirm the content in the actual snapshot.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gau |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |

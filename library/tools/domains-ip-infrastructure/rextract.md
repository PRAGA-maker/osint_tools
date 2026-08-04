---
id: rextract
name: rextract
description: Use when you have a list of URLs/`domain`s and want to pull specific strings from their HTML — returns regex-matched values (emails, IDs, tokens) scraped across many pages at once.
url: https://github.com/iustin24/rextract
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Bulk-extracting regex matches (emails, UUIDs, titles, IDs) from the raw HTML of a list of URLs from the command line.
selectorsIn:
- domain
selectorsOut:
- email
- domain
status: live
pricing: free
costNote: Free and open-source (Rust); build with `cargo install --git https://github.com/iustin24/rextract`. Only the Rust toolchain is needed.
opsec: active
opsecNote: rextract fetches each URL directly, so every target host sees a request from your IP. When scraping a subject's own pages this is active reconnaissance — run it through a proxy/VPN and mind rate limits so a burst of requests isn't obviously you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Small open-source utility (iustin24) — auditable single-purpose code; it does exactly what your regex says, so reliability rests on the pattern you supply, not on any data source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- REXTRACT
tags:
- Domain/IP/Links
- Searchers, scrapers, extractors, parsers
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# rextract

> A tiny, fast CLI scraper: feed it a list of URLs and a regex, get back every match found in their HTML — the quick way to harvest emails, IDs, or tokens across many pages at once.

## When to use
You have a set of pages tied to a `domain` (a sitemap dump, a list of profile URLs, search results) and want to pull one specific kind of string from all of them — email addresses, phone patterns, UUIDs/user IDs, tracking codes, `<title>`s. Instead of curling each page and grepping by hand, rextract fetches the list and applies your regex in one pass.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `cargo install --git https://github.com/iustin24/rextract` (needs Rust/Cargo).
2. Prepare a list of URLs (one per line).
3. Pipe them in with a regex, e.g. `cat urls.txt | rextract '<regex>'` — extract emails, UUIDs, or titles via lookarounds.
4. Read the matched strings from stdout; redirect to a file to build a dataset.
5. Pivot: harvested `email`s feed email-OSINT; extracted user IDs/handles feed username enumeration; titles/paths help map a site.

## Inputs → Outputs
- **In:** a list of URLs (a `domain`'s pages) + a regex pattern
- **Out:** every string matching the regex across those pages — commonly `email`, IDs, or `domain`/URL fragments
- **Empty/negative result looks like:** no output — either the pattern matched nothing, the pages didn't return the expected HTML (JS-rendered content won't be present), or requests were blocked; verify against one page manually.

## Gotchas & OpSec
- **Active:** it hits every URL directly from your IP — proxy it and throttle to avoid an obvious scraping signature.
- It reads **raw HTML only** — content injected by JavaScript after load won't appear; use a headless browser for those.
- Output quality is entirely your regex's quality; over-broad patterns produce noise, over-narrow ones miss variants.

## Overlaps ("do both")
- Complements broader scraping/parsing tools — rextract is the fast single-pattern harvester; pair it with a crawler to first gather the URL list, then a validator to clean the harvested emails/IDs.

## Trust & verifiability
`trust: community` — a small, inspectable open-source utility; it introduces no data source of its own, so results are as trustworthy as the pages you point it at and the regex you write.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rextract |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → email, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |

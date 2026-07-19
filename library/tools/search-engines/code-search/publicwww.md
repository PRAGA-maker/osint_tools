---
id: publicwww
name: PublicWWW
description: Use when you have a unique code string tied to a `domain` — an analytics/AdSense ID, a tracking snippet, a wallet address, a shared template — and want every other site carrying it — returns the list of matching `domain`s.
url: https://publicwww.com/
category: search-engines
path:
- search-engines
- code-search
bestFor: Finding all websites that share a specific analytics ID, tracker, code snippet, or string — pivoting one site to an operator's whole network.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free searches return limited results (first page, capped) and rate-limit anonymous use. Paid subscriptions unlock full result sets, CSV export, and API access. The free tier is enough to confirm a link between sites.
opsec: passive
opsecNote: You query PublicWWW's own index of source code — you never touch the target's sites, so the operator isn't alerted. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known source-code search engine widely used in security/OSINT; results are only as fresh as its crawl, so verify a match by viewing the live site's source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- publicwww.com
- source code search engine
tags:
- code-search
- pivot
- infrastructure
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# PublicWWW

> A search engine over the *source code* of web pages — find every site sharing a tracking ID, snippet, or string to map an operator's network.

## When to use
You have one site tied to a subject (a personal blog, a scam page, a business front) and you want the *other* sites the same person runs. If the page carries a reusable fingerprint — a Google Analytics/AdSense ID (`UA-…`, `pub-…`, `G-…`), a Facebook Pixel, a unique CSS/JS snippet, a crypto-wallet address, a distinctive phrase — PublicWWW returns every indexed `domain` that also contains it, exposing the cluster.

## How to use it (`bestInteractionPattern`: web-manual)
1. From the target site, view source and pull a distinctive string: analytics/ad IDs are best (they're reused across an owner's properties), then unique code or text.
2. Open https://publicwww.com/ and search that exact string (quote it; supports regex and multi-term queries).
3. Read the list of matching sites. Shared analytics/pixel IDs are strong evidence of common ownership; shared boilerplate is weaker.
4. Confirm each match by opening the live site and re-checking its source (the index can lag).
5. Pivot: run the newly found `domain`s through WHOIS/history (`[[whoisology]]`-style) and content review to build out the network.

## Inputs → Outputs
- **In:** a code/string fingerprint (usually pulled from a known `domain`)
- **Out:** list of `domain`s whose source contains that string
- **Empty/negative result looks like:** no matches can mean the string is genuinely unique, or that the other sites haven't been crawled / are behind Cloudflare / are newer than the index — absence isn't proof they don't exist.

## Gotchas & OpSec
- Human-in-the-loop: free tier caps results and rate-limits; for a full network you'll hit the paywall (results/CSV/API are the paid unlock).
- Match quality varies: a shared **analytics/ad ID** is a strong ownership link; a shared library or common phrase is not — weight accordingly.
- The index is a snapshot; always re-verify a hit against the live page before asserting a connection.

## Overlaps ("do both")
- Pairs with `[[spyonweb]]` / analytics-ID pivots and with WHOIS-history tools — PublicWWW finds sites sharing a code fingerprint; WHOIS ties them by registrant, and the two together confirm common ownership.

## Trust & verifiability
`trust: community` — a widely-used source-code search engine; treat its index as a lead source, verifying every match against the live site's current source before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | publicwww |
| category | search-engines |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

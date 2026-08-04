---
id: source-code-search-engine-315-million-domains-indexed-search-by-title-metadata-javascript-files-server-name-locat
name: Source code search engine (315 million domains indexed). Search by title, metadata, javascript files, server name, locat
description: Use when you have a snippet, tracker ID, title, or server detail and want every `domain` whose source contains it — returns matching domains, subdomains, IPs and hostnames.
url: https://domaincodex.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Reverse-searching 300M+ domains by page title, HTML/JS source, metadata, server name, IP or location.
selectorsIn:
- domain
- ip-address
- geolocation
- device-id
selectorsOut:
- domain
- ip-address
- geolocation
status: live
pricing: freemium
costNote: A live web search is available to try for free; deeper/bulk querying and the API require a paid plan. Core keyword/domain lookups can be run without payment.
opsec: passive
opsecNote: You query Domain Codex's pre-crawled index, not the target sites, so pivoting across a subject's infrastructure never touches the subject — this is a passive alternative to fetching each site yourself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial domain-intelligence engine (Erie Data Systems, launched 2022) indexing 300M+ domains for security/brand-protection/OSINT; data is directly crawled, but as a vendor index, coverage and freshness vary.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- domain-codex
aliases:
- domaincodex
- domain codex
tags:
- Domain/IP/Links
- Domain/IP investigation
- source-code-search
- reverse-tracker
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Source code search engine (315 million domains indexed)

> Domain Codex: a reverse index of 300M+ domains you can search by page title, HTML/JavaScript source, metadata, server name, IP or location — to find every site sharing a fingerprint.

## When to use
You have a fingerprint from one site — an analytics/ad `device-id` in its JavaScript, a distinctive page title or meta tag, a server name, an `ip-address`, or a hosting `geolocation` — and want to find *all other* `domain`s that share it. This is the classic technique for linking a network of sites to one operator, or expanding from a single seed domain to its infrastructure siblings, without crawling the web yourself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://domaincodex.com and use the live search.
2. Pick the filter matching your seed: title/metadata text, a JavaScript snippet or tracker id, server name, IP, reverse-hostname, certificate info, or location.
3. Enter the value and run the search across active and inactive root domains.
4. Read the result set: matching `domain`s with their `ip-address`, hostname, certificate and status data.
5. Pivot: each returned domain feeds WHOIS/DNS tooling and the cookie/tracker checker (`[[determines-if-website-is-not-comply-with-eu-cookie-law-and-gives-you-insight-about-cookies-installed-from-website-before]]`); a shared ID confirms common ownership.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, `geolocation`, or a source fingerprint (title/metadata/JS/tracker `device-id`, server name)
- **Out:** matching `domain`s, `ip-address`es, hostnames, `geolocation`, certificate/status data
- **Empty/negative result looks like:** no domains match the fingerprint — either the value is unique to one site or falls outside the index's 300M-domain coverage; corroborate with another passive-DNS/source-search engine.

## Gotchas & OpSec
- Index coverage is large but not exhaustive; a blank result is not proof no other site uses the fingerprint.
- The deepest filters and bulk/API access are paywalled; the free live search still handles most single pivots.
- Passive: you never touch the target sites, which makes this safer than direct crawling for sensitive infrastructure work.

## Overlaps ("do both")
- Pairs with `[[domain-codex]]` (the sibling entry for the same provider) and with the cookie/tracker checker — use CookieMetrix to read one site's IDs, then Domain Codex to find every other site carrying them.

## Trust & verifiability
`trust: community` — a commercial crawler-built index; the matches are directly observed source data (verifiable by visiting the returned domains), but as a single vendor's crawl it should be cross-checked against another passive-DNS/source engine for completeness.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | source-code-search-engine-315-million-domains-indexed-search-by-title-metadata-javascript-files-server-name-locat |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address, geolocation, device-id → domain, ip-address, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

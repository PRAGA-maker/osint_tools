---
id: metager-privacy-protected-search
name: 'MetaGer: Privacy Protected Search'
description: Use when you have a `name`, `username`, or `email` and want web results from a privacy-preserving metasearch that blends several engines — returns web links without profiling you or tipping the query to Google.
url: https://metager.org/
category: search-engines
path:
- search-engines
bestFor: Running a name/handle/email search across multiple back-end engines from an anonymized position, so the query isn't tied to your identity.
selectorsIn:
- name
- username
- email
selectorsOut:
- social-profile
- domain
status: live
pricing: freemium
costNote: Free to search (funded by the non-profit SUMA-EV via ads/donations). A small membership removes ads and unlocks the anonymizing proxy and extra filters; core search is free.
opsec: passive
opsecNote: MetaGer is built for privacy — it proxies queries to back-end engines so your IP/identity isn't handed straight to Google/Bing, and offers an "open anonymously" proxy for opening results. Still use a sock-puppet browser; it's passive, but destination sites you click can log you unless you use the proxy.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by SUMA-EV, a German non-profit association; long-established, open about its methodology, and explicitly privacy-focused.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- MetaGer
- metager.org
- metager3.de
tags:
- privacy-search
- metasearch
- search-engines
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# MetaGer: Privacy Protected Search

> A German non-profit privacy metasearch engine — queries multiple back-end engines through a proxy so your search isn't profiled or tied to you.

## When to use
You want to search a `name`, `username`, or `email` but don't want the query logged against your Google/Bing identity, and you'd like results aggregated from several engines rather than one. Useful early in a case when you're casting a wide, low-attribution net, or to get a different result mix than a single mainstream engine returns.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://metager.org/ (English UI; the old metager3.de redirects here).
2. Enter the selector — a full name in quotes, a `username`, or an `email` — and search.
3. Use the left-hand filters to narrow by source engine, time, or to exclude domains.
4. Open sensitive results via MetaGer's "open anonymously" proxy link (membership feature) so the destination doesn't see your real IP/referrer.
5. Pivot: promising hits feed username-enumeration (`[[whatsmyname]]`-style), email tools, or social-profile lookups.

## Inputs → Outputs
- **In:** `name`, `username`, or `email` (any web query)
- **Out:** aggregated web links — candidate `social-profile`s, `domain`s, articles mentioning the selector
- **Empty/negative result looks like:** thinner coverage than Google for long-tail/very recent pages, and it will not surface content behind logins; a blank isn't proof of absence — cross-run on a mainstream engine.

## Gotchas & OpSec
- Human-in-the-loop: none, though occasional rate-limit challenges can appear under heavy use.
- Result depth is smaller than Google's index; treat it as a privacy-first *complement*, not a full replacement.
- The anonymizing proxy for opening results is a paid/membership feature; without it, clicking a result exposes your browser to that site as usual.

## Overlaps ("do both")
- Pairs with a mainstream engine and with `[[searx]]`-style metasearch — MetaGer gives privacy and a different engine blend; run the same selector on Google/Bing to catch what MetaGer's smaller index misses.

## Trust & verifiability
`trust: trusted` — run by SUMA-EV, an established German non-profit with a transparent privacy model; results are aggregated from named back-end engines you can filter, so provenance is visible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | metager-privacy-protected-search |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, email → social-profile, domain |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

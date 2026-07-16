---
id: marple
name: Marple
description: Use when you have a `username` or `name` and want search-engine results that contain it in profile URLs — returns candidate social profiles gathered from Google/DuckDuckGo.
url: https://github.com/soxoj/marple
category: username
path:
- username
bestFor: Quickly collecting likely profile links for a nickname/name by mining Google and DuckDuckGo results, ranked by relevance.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free and open-source (soxoj, author of Maigret); Python CLI, no account.
opsec: passive
opsecNote: It issues web searches from your machine to Google/DuckDuckGo, so those engines see your IP — but it does not touch the target's accounts. Use a VPN/sock-puppet context if attribution matters; heavy use may trigger search-engine CAPTCHAs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: By soxoj, a respected OSINT developer; a lightweight search-scraper — results are only as good as the search engines' indexes, so treat links as candidates to verify.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- whatsmyname-web
- go-sherlock
- 1c-database-converter
- awesome-osint-mcp-servers
- counter-osint-guide-for-russians
- fravia-soxoj
- gitcolombo
- maigret
- maigret-via-socid-extractor-soxoj-ecosystem
- mailto-analyzer
- osint-namecheckers-list
- socid-extractor
- username-generation-guide
aliases:
- soxoj/marple
tags:
- Nicknames
- username
- cli
- search-scraper
source: cyb-detective
lastVerified: '2026-07-10'
enrichment: full
---

# Marple

> A CLI that mines Google and DuckDuckGo for a nickname/name and collects the URLs that contain it — a fast, search-engine-driven complement to signature-based username enumerators.

## When to use
You have a `username` or `name` and want a quick set of candidate profile/mention links without waiting on a full site-by-site enumeration. Because Marple works off search-engine indexes rather than a fixed site list, it surfaces mentions on sites that enumerators like Sherlock/WhatsMyName don't check — blogs, forums, news, niche platforms — and ranks by relevance. Use it alongside a signature enumerator to widen coverage.

## How to use it (`bestInteractionPattern`: cli)
1. Install from https://github.com/soxoj/marple (Python).
2. Run `marple <username>` (or a name in quotes); it queries Google/DuckDuckGo and aggregates matching URLs.
3. Use flags to control result count and engines; review the ranked links.
4. Open and verify each candidate — a URL containing the handle isn't proof it's your subject.
5. Pivot: confirmed profiles feed enrichment; combine with `[[whatsmyname-web]]`/`[[go-sherlock]]` for signature-based coverage the search engines miss.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** candidate `social-profile`/mention URLs (with the `username` in them), relevance-ranked
- **Empty/negative result looks like:** few/no links, or CAPTCHA blocks from the search engines — meaning the handle isn't well-indexed or you got rate-limited; retry later/behind a proxy.

## Gotchas & OpSec
- Depends on **search-engine indexes** — misses unindexed profiles and can be throttled/CAPTCHA'd on heavy use.
- Search results include noise; verify each link belongs to your subject.
- OpSec: passive toward the target, but your searches hit Google/DDG from your IP — use a proxy for sensitive work.

## Overlaps ("do both")
- Complements signature enumerators `[[whatsmyname-web]]`/`[[go-sherlock]]` — Marple finds indexed *mentions* anywhere; they check a *fixed list* of sites directly. Run both to cover indexed and non-indexed presence.

## Trust & verifiability
`trust: community` — a reputable author's lightweight scraper; results are candidate leads bounded by search-engine coverage, so confirm each on the actual page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | marple |
| category | username |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
</content>

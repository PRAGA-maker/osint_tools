---
id: sourcewolf
name: SourceWolf
description: Use when you have a `domain`/URL and want hidden endpoints, subdomains and links mined from its JS and responses — returns URLs, endpoints and social links.
url: https://github.com/ksharinarayanan/SourceWolf
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Crawling a site's responses/JavaScript to surface hidden endpoints, URLs and embedded social links.
selectorsIn:
- domain
selectorsOut:
- domain
- social-profile
status: degraded
pricing: free
costNote: Free and open source (Python3). Last release 2021 — functional but unmaintained.
opsec: active
opsecNote: SourceWolf can send live requests to the target to crawl responses and brute-force URLs/subdomains — those hits come from your host and are logged there. It can also parse locally-saved response files (fully passive). Use the local-file mode, or a burner proxy/VPS, for anything you don't want tied to you; only actively crawl targets you're authorised to test.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A known recon utility, but unmaintained since 2021. Extraction is regex/crawl-based, so expect false positives and misses; verify discovered endpoints are live.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- ksharinarayanan/SourceWolf
tags:
- Domain/IP/Links
- Website analyze
- javascript-analysis
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# SourceWolf

> A fast CLI response-crawler: it digs through a site's HTTP responses and JavaScript to pull out hidden endpoints, URLs, subdomains, and embedded social-media links — and can brute-force URLs from a wordlist.

## When to use
You have a target `domain` and want the *hidden* surface: API endpoints and paths referenced only in JS, subdomains, and social-media links baked into the source. Useful for expanding a site's footprint and finding the social handles a developer left in the code — a pivot from infrastructure back to people.

## How to use it (`bestInteractionPattern`: cli)
1. `git clone` the repo and `pip3 install -r requirements.txt` (works on Linux/macOS/Windows/WSL).
2. Point it at a single URL (`-u`) or a list (`-l`); set an output dir (`-o`). For a passive run, feed it locally-saved response files instead of hitting the site live.
3. Let it crawl responses to extract endpoints, JS variables, URLs, and social links; optionally brute-force URLs/subdomains with a wordlist and check status codes.
4. Triage the output — regex extraction yields false positives; confirm endpoints resolve and are live.
5. Pivot: discovered `social-profile` links feed username/social OSINT; endpoints/subdomains feed further mapping (`[[subdomain-finder]]`).

## Inputs → Outputs
- **In:** a `domain`/URL (or a list, or saved response files)
- **Out:** hidden endpoints, URLs, subdomains (`domain`), and embedded `social-profile` links
- **Empty/negative result looks like:** little or nothing extracted — a small/static site, JS that loads content dynamically at runtime, or requests blocked. Try seeding more URLs or a live crawl before concluding.

## Gotchas & OpSec
- **Active** when it crawls/brute-forces live — requests originate from your host and are logged; use local-file mode or a burner proxy for sensitive targets, and only actively test authorised scope.
- Unmaintained since 2021; may struggle with modern SPA/JS-heavy sites.
- Regex extraction → false positives; verify each finding.

## Overlaps ("do both")
- Complements dedicated JS endpoint tools (LinkFinder, gau/hakrawler) and `[[subdomain-finder]]` — each parses/sources differently, so combine to widen coverage.

## Trust & verifiability
`trust: community` — a recognised but dormant recon tool. Reliable at *surfacing candidates* from source; every extracted endpoint/link needs live verification before you act on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sourcewolf |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |

---
id: hakrawler
name: Hakrawler
description: Use when you have a `domain` and want to crawl it fast for links, endpoints, JS files and in-scope assets — returns URLs and `domain`s (subdomains, endpoints) to widen your attack/recon surface.
url: https://github.com/hakluke/hakrawler
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Fast CLI crawling of a target site to enumerate URLs, endpoints, JS locations and subdomains.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open source (Go); install via `go install` or Docker, no account.
opsec: active
opsecNote: hakrawler makes direct HTTP requests to the target from your host — the site's logs/WAF will see your crawl. Route through a proxy/VPN, throttle threads, and don't crawl from an attributable IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source tool by a well-known researcher (hakluke), 5k+ GitHub stars; source is auditable. Last tagged release 2022 but the crawler remains functional.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- haklistgen
aliases:
- hakluke/hakrawler
tags:
- Domain/IP/Links
- Dorks/Pentest/Vulnerabilities
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Hakrawler

> A fast Go web crawler that takes a URL on stdin and spits out every link, endpoint, JS-file location and subdomain it finds — quick recon of a site's attack/footprint surface.

## When to use
You have a `domain` (a subject's website, a company portal, a suspicious host) and want to map what's actually there: hidden endpoints, API paths, JavaScript files that leak URLs and keys, linked subdomains. It's the "spider it and dump everything" step before you dig into specific findings — far faster than clicking through a site by hand.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `go install github.com/hakluke/hakrawler@latest` (or run the Docker image).
2. Feed it a URL on stdin: `echo https://example.com | hakrawler`.
3. Tune flags: `-d` crawl depth (default 2), `-t` threads (default 8), `-subs` to include subdomains, `-proxy` to route through Burp/VPN, `-h` for custom headers/cookies.
4. Read stdout — a stream of discovered URLs, endpoints and JS locations (pipe to a file or to `sort -u`).
5. Pivot: grab JS files for secret-scanning; feed discovered subdomains/endpoints into further probing; harvest linked external `domain`s for a relationship graph.

## Inputs → Outputs
- **In:** `domain` / seed URL (stdin)
- **Out:** discovered URLs, endpoints, JS file locations, and (with `-subs`) `domain` subdomains
- **Empty/negative result looks like:** little or no output — a heavily JS-rendered SPA, a WAF blocking the crawler, or a tiny static site. Try increasing depth, adding headers, or a headless-browser crawler instead.

## Gotchas & OpSec
- It crawls with direct requests — this is **active**; expect to appear in the target's logs and to trip aggressive WAFs. Throttle threads and proxy your traffic.
- It follows links it's given; it is not a full JS-execution browser, so client-rendered content can be under-discovered.
- OpSec: never crawl a sensitive target from an attributable IP; use a VPN/proxy and reasonable rate limits.

## Overlaps ("do both")
- Pairs with `[[haklistgen]]` and JS-secret scanners — hakrawler enumerates the URLs/JS, and downstream tools mine those artifacts for wordlists, secrets and further endpoints.

## Trust & verifiability
`trust: community` — widely-used open-source tool from a reputable researcher; you can read the Go source, and although releases are infrequent the crawler still works as documented.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hakrawler |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |

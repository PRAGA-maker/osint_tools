---
id: server-status-pwn
name: server-status_PWN
description: Use when you have a `domain`/host with an exposed Apache /server-status and want to harvest live request data — returns visited `domain`s, URLs and connecting `ip-address`es.
url: https://github.com/mazen160/server-status_PWN
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Continuously scraping a misconfigured public Apache mod_status page to collect live URLs and client IPs for reconnaissance.
selectorsIn:
- domain
- ip-address
selectorsOut:
- ip-address
- domain
status: live
pricing: free
costNote: Free and open source (MIT). A Python script; only dependencies are `requests` and `bs4`.
opsec: active
opsecNote: Actively polling a target's /server-status page repeatedly generates recurring requests from your IP in that server's own logs and can look like scraping/abuse. Only run against systems you are authorized to test; route through infrastructure you're willing to burn, and throttle politely. The data harvested (other users' URLs/IPs) is sensitive — handle it lawfully.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source tool by researcher Mazin Ahmed (mazen160), several hundred GitHub stars; narrow, well-understood infrastructure-recon utility with public source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- server-status PWN
- mod_status scraper
tags:
- apache
- recon
- infrastructure
source: gh-topic-intelligence-gathering
lastVerified: '2026-07-29'
enrichment: full
---

# server-status_PWN

> A small Python recon tool that scrapes a misconfigured, publicly exposed Apache `mod_status` (`/server-status`) page over time to harvest the URLs and client IPs passing through that server.

## When to use
You have found (or suspect) a target web server with its Apache **`/server-status`** page publicly reachable — a common misconfiguration that leaks every in-flight request: full URLs, virtual hosts, and connecting client IPs. This tool polls that page continuously and logs the unique observations, turning a momentary leak into a growing intel picture of who and what talks to the server. Strictly an infrastructure/authorized-pentest tool, not a people-finder.

## How to use it (`bestInteractionPattern`: cli)
1. Confirm the target exposes `http(s)://<host>/server-status` (returns an Apache status table). Only proceed on systems you're authorized to test.
2. Clone the repo and install deps: `pip install requests bs4`.
3. Run: `python server-status_PWN.py --url 'http://<host>/server-status'`.
4. Let it poll; it writes observations to a SQLite database and can dump unique URLs to a newline-delimited file.
5. Read the output: harvested URLs (`domain`/paths — sometimes with tokens in query strings) and connecting client `ip-address`es; pivot IPs into geolocation/ASN and URLs into further site mapping.

## Inputs → Outputs
- **In:** a `domain`/host URL pointing at an exposed `/server-status`
- **Out:** observed `domain`s/URLs and connecting `ip-address`es (accumulated in SQLite)
- **Empty/negative result looks like:** `/server-status` returns 403/404 or is restricted to localhost — nothing to harvest; the misconfiguration isn't present.

## Gotchas & OpSec
- **Active and noisy:** repeated polling shows up in the target's own logs from your IP. Authorization is mandatory; throttle and use disposable infrastructure.
- The leaked data belongs to third parties (other visitors' URLs and IPs) — treat it as sensitive and handle within legal bounds.
- Only works against Apache with `ExtendedStatus`/`mod_status` publicly exposed; most hardened servers block it.

## Overlaps ("do both")
- Pairs with passive-DNS, ASN/IP geolocation and site-crawling tools — this surfaces live URLs and client IPs, which those enrich into infrastructure and location context.

## Trust & verifiability
`trust: community` — a well-known open-source researcher tool with public, auditable source; it does exactly one narrow thing, so reliability is high, but findings depend entirely on the target's misconfiguration being real.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | server-status-pwn |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → ip-address, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |

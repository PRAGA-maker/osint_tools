---
id: zoomeye
name: ZoomEye
description: Use when you have a `domain`/`ip-address` and want exposed-host, service and banner intel — returns ip-address, domain and device-id.
url: https://www.zoomeye.ai/
category: search-engines
path:
- search-engines
bestFor: An internet-wide scanner search engine (Shodan/Censys-style) for finding hosts, open services, banners and devices tied to an IP or domain.
selectorsIn:
- domain
- ip-address
selectorsOut:
- ip-address
- domain
- device-id
status: live
pricing: freemium
costNote: Free tier (registration + monthly query quota) covers most lookups; higher volume and advanced filters need a paid plan.
opsec: passive
opsecNote: ZoomEye serves results from its own prior scans, so querying it does NOT touch the target's infrastructure — it is passive reconnaissance. Do not follow up by directly connecting to discovered hosts unless authorized, as that would be active. Use a sock-puppet account for registration.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: An established internet-wide scanning search engine (Knownsec); results are its own scan data — accurate at scan time but may be stale.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- ZoomEye
- zoomeye.ai
tags:
- attack-surface
- internet-scan
- infrastructure
source: awesome-osint
lastVerified: '2026-07-18'
enrichment: full
---

# ZoomEye

> A search engine over the internet's exposed hosts and services — the Shodan/Censys alternative for mapping the infrastructure behind a domain or IP.

## When to use
You have a `domain` or `ip-address` linked to a subject (a personal site, a business, a leaked server) and want to understand the infrastructure around it: what services and ports are open, software/banner versions, TLS certificates, hostnames sharing the host, and connected devices. Useful for confirming a person controls a piece of infrastructure, finding co-hosted assets, or profiling an organization's exposed footprint. ZoomEye has particularly strong coverage of hosts in Asia, complementing Shodan/Censys.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free account at https://www.zoomeye.ai/ (sock-puppet) to unlock the query quota.
2. Search by `ip:`, `hostname:`/domain, service, port, or banner keyword using ZoomEye's dork syntax.
3. Read results: open services/versions, certificates, geolocation, and other hostnames on the same host.
4. Use filters (country, service, app) to narrow, or the API for bulk/automated queries within quota.
5. Pivot: shared certs/hostnames → other `domain`s the subject controls; open services → the hosting provider and tech stack; device banners → `device-id`-style identification of exposed cameras/IoT.

## Inputs → Outputs
- **In:** `domain` or `ip-address` (or service/banner dork)
- **Out:** `ip-address` (hosts), `domain` (co-hosted hostnames/certs), `device-id` (exposed device/service fingerprints)
- **Empty/negative result looks like:** no indexed data for the target — the host may be behind Cloudflare/CDN (you see the CDN, not the origin), newly stood up, or simply not scanned; cross-check with Shodan/Censys.

## Gotchas & OpSec
- Data is **scan-time**, so it can be stale — a banner may reflect a past state; confirm currency before relying on it.
- CDNs/proxies (Cloudflare) mask the real origin — you'll see the front, not the backend.
- OpSec: passive (ZoomEye's own scans); registration ties queries to an account — use a sock-puppet, and never actively connect to found hosts without authorization.

## Overlaps ("do both")
- Pairs with Shodan and Censys — coverage and freshness differ by engine and region (ZoomEye is strong in Asia); run the same target through more than one to avoid a single scanner's blind spots.

## Trust & verifiability
`trust: community` — a reputable scanning engine; results are authentic scan data but time-bound, so treat findings as "true as of the last scan" and re-verify anything current-state-dependent.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | zoomeye |
| category | search-engines |
| selectorsIn → selectorsOut | domain, ip-address → ip-address, domain, device-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |

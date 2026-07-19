---
id: odin
name: ODIN
description: Use when you have an `ip-address` or `domain` and want its exposed hosts/services — returns open ports, services, banners, and certificate/host data.
url: https://search.odin.io/
category: search-engines
path:
- search-engines
bestFor: Internet-wide host scanning — enumerate a target's exposed ports, services, banners, and TLS certificates from an IP or domain.
selectorsIn:
- ip-address
- domain
selectorsOut:
- ip-address
- domain
- device-id
status: live
pricing: freemium
costNote: Free tier available after registration (search quota); higher volume and API access are paid. Built by Cyble.
opsec: passive
opsecNote: ODIN serves results from its OWN internet-wide scans, so querying it does NOT send packets to the target — the lookup is passive and the target is not touched. Do not confuse this with active scanning; here you are reading a pre-collected index.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial internet-scanning search engine (Cyble); data is as fresh as its last scan of a host, so treat exposed-service findings as point-in-time snapshots to re-verify if timing matters.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- ODIN search
- odin.io
- search.odin.io
tags:
- internet-scanning
- shodan-alternative
- infrastructure
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# ODIN

> An internet-wide scanning search engine (a Shodan/Censys-style tool by Cyble) — query an IP or domain and see the ports, services, banners, and certificates it exposes, without touching the target yourself.

## When to use
You have an `ip-address`, CIDR, or `domain` tied to a subject or org and want to map its externally-exposed infrastructure: which ports/services are open, software/versions from banners, TLS certificate details (which can reveal other hostnames and organizational identity), and device fingerprints. Because ODIN answers from its own scan index, you learn the exposure passively — useful for attribution and infrastructure pivoting.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free account at https://search.odin.io/.
2. Search by IP, CIDR, domain, or facet (service, certificate, product) using ODIN's query syntax.
3. Read results: open ports/services, banners/versions, TLS certs (SANs reveal sibling domains), and host fingerprints (`device-id`).
4. Pivot: certificate SANs and shared banners link additional `domain`s/`ip-address`es; exposed services inform risk/attribution; feed found hosts back in to expand the map.

## Inputs → Outputs
- **In:** `ip-address` / CIDR / `domain`
- **Out:** open ports/services, banners, TLS certs, host fingerprints (`ip-address`, `domain`, `device-id`)
- **Empty/negative result looks like:** no data for the host — it may not have been scanned recently, may be firewalled, or may be behind a CDN masking the origin; cross-check with another scanner.

## Gotchas & OpSec
- Results are point-in-time snapshots from ODIN's last scan; a service may have opened/closed since.
- CDN/proxy fronting (Cloudflare etc.) hides the true origin IP — the scan sees the edge, not the backend.
- Human-in-the-loop: a free account/login is required; passive toward the target regardless.

## Overlaps ("do both")
- Complements other internet scanners (Shodan, Censys, Netlas, ZoomEye) — each scans on its own cadence and sees different hosts/ports, so run more than one.

## Trust & verifiability
`trust: community` — a commercial scanner; the raw banner/cert data is factual as scanned, but always note the scan date and corroborate across engines before drawing attribution conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | odin |
| category | search-engines |
| selectorsIn → selectorsOut | ip-address, domain → ip-address, domain, device-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |

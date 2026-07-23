---
id: tenssens
name: Tenssens
description: Use when you have a `domain` or `ip-address` and want a quick multi-check recon pass — one Python CLI runs whois, DNS, subdomains, headers, geolocation, and port checks.
url: https://github.com/thenurhabib/tenssens
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: One-command footprinting of a domain/IP bundling whois, DNS, subdomains, headers, geoip, and port checks.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
- geolocation
status: live
pricing: free
opsec: active
opsecNote: Some modules query passive sources, but others (port scan, admin-panel finder, HTTP headers, robots.txt) reach out to the target directly from your host and are logged there. Treat a full run as active/intrusive; use it only on assets you're authorized to test and route through controlled infrastructure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: Small community Python framework (thenurhabib, AGPL-3.0); auditable but modest maintenance and it wraps other free services.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- tenssens
- thenurhabib/tenssens
tags:
- osint-framework
- footprinting
- recon
- tools-collection
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Tenssens

> A compact Python footprinting CLI — point it at a domain or IP and it fires off ten common recon checks (whois, DNS, subdomains, CMS, headers, geoip, ports, admin-finder, robots.txt, hash cracking) in one place.

## When to use
You have a `domain` or `ip-address` and want a fast, all-in-one first-pass recon without stringing together separate tools. Tenssens bundles the routine checks an investigator runs early — registrant/whois, DNS records, subdomains, technology/CMS, HTTP headers, IP geolocation, and a light port scan — into a single menu. Good for quick triage of infrastructure tied to a case; reach for specialized tools when you need depth.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/thenurhabib/tenssens, install Python 3 + `requirements.txt`.
2. Run `python3 tenssens.py` (the app uses a built-in default login prompt).
3. Choose a module and enter the target `domain`/`ip-address` (`selectorsIn`).
4. Read the module output — whois/registrant, DNS, subdomains, geoip, ports, headers (`selectorsOut`) — and pivot the findings into deeper, purpose-built tools.

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** `domain` (subdomains, DNS), `ip-address`, `geolocation` (geoip), plus whois/registrant, headers, ports, CMS
- **Empty/negative result looks like:** a module returns nothing or errors — the underlying free service may be down/rate-limited, or the target exposes little; try the dedicated tool for that check.

## Gotchas & OpSec
- Human-in-the-loop: none beyond the app's own prompt.
- OpSec: **active** for its scanning/probing modules — those hit the target and are logged; only use with authorization and via controlled infrastructure.
- It wraps third-party free services, so reliability and freshness vary; verify anything important with a first-party source.

## Overlaps ("do both")
- Overlaps with fuller frameworks [[sn0int]] and [[harpoon]] and with single-purpose tools ([[subfinder]] for subdomains, whois/DNS utilities) — use Tenssens for a quick sweep, then the specialists for depth and reliability.

## Trust & verifiability
`trust: unverified` — a small AGPL community project that aggregates other free tools; the code is auditable but lightly maintained, so treat outputs as convenience leads and confirm with authoritative sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tenssens |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |

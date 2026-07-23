---
id: ivre
name: IVRE
description: Use when you have `ip-address`/`domain` scan data and want to build and query your own recon database — returns hosts, open ports and services.
url: https://github.com/ivre/ivre
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Self-hosting a private, Shodan-like network-recon database from your own (or public) scan data.
selectorsIn:
- ip-address
- domain
selectorsOut:
- ip-address
- domain
status: live
pricing: free
costNote: Free and open source (GPL). Self-hosted — you provide the compute/storage; there's no paid tier.
opsec: active
opsecNote: IVRE is a framework, not a passive site. It ingests scan data — and if you point its active scanners (nmap/masdns/zmap wrappers) at a target, those packets come from your infrastructure and are logged there. Only run active scans against systems you're authorised to test; ingesting existing/third-party datasets is passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: docker
trust: trusted
trustNote: Mature, well-known open-source project used in security research; the code is auditable. Result quality depends entirely on the scan data you feed it — IVRE stores and correlates, it doesn't vouch for accuracy.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- Instrument de veille sur les réseaux extérieurs
- ivre/ivre
tags:
- Tools collections/toolkits
- network-recon
- self-hosted
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# IVRE

> A self-hosted network-reconnaissance framework — build your own Shodan/Censys-style searchable database from nmap, masscan, zmap, Zeek and other scan output, then query it for hosts, ports and services.

## When to use
You have (or intend to gather) network scan data and want to store, correlate, and search it yourself rather than relying on a third-party service — for infrastructure mapping around a target `domain`/`ip-address`, tracking how a host's services change over time, or analysing large scan datasets offline. It's for teams doing repeated, structured recon, not a one-off web lookup.

## How to use it (`bestInteractionPattern`: docker)
1. Deploy IVRE (the documented path is Docker/`docker-compose`, bringing up the web UI + database + agents), or install from source.
2. Feed it data: import existing nmap/masscan/zmap results and passive sources, or run its active-scan agents against authorised targets.
3. Query via the web interface or CLI — filter by IP range, open port, service/product, country, or hostname to find matching hosts.
4. Correlate over time: re-import scans to track service/port changes on a host of interest.
5. Pivot: discovered `ip-address`/`domain` and service banners feed vulnerability triage and infrastructure clustering; export results for reporting.

## Inputs → Outputs
- **In:** scan data keyed on `ip-address`/`domain` (nmap/masscan/zmap/Zeek output, or its own scans)
- **Out:** a searchable store of hosts, open ports, service/product banners, and their history
- **Empty/negative result looks like:** empty query results — you haven't ingested data covering that host yet. IVRE knows only what you've fed it; it is not a pre-populated internet index.

## Gotchas & OpSec
- Non-trivial to stand up (database + services); it's infrastructure, not a click-and-go site.
- **Active scanning is your legal responsibility** — only scan what you're authorised to; those probes originate from your hosts and are logged by targets.
- It's a store/correlator: garbage-in-garbage-out. Data quality is whatever your scans provide.

## Overlaps ("do both")
- Complements hosted indexes like Shodan/Censys — use those for instant, pre-scanned global data; use IVRE when you need your own data, private storage, or custom/repeated scanning under your control.

## Trust & verifiability
`trust: trusted` — an established, auditable open-source framework. The tool is reliable; the *findings* are only as trustworthy as the scan data you ingest, so validate sources and re-scan for freshness.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ivre |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | ip-address, domain → ip-address, domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | docker |
| opsec | active |
| human-in-loop | no |

---
id: seekolver
name: Seekolver
description: Use when you have a `domain` (or org name) and want its live web attack surface — a Python CLI that pulls subdomains from open sources, resolves them, and reports which host HTTP(S) services, returning `domain` and `ip-address`.
url: https://github.com/Krypteria/Seekolver
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Mapping a domain's subdomains from multiple OSINT APIs and resolving them to find the live HTTP/HTTPS hosts.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free, open-source Python tool (Krypteria/Seekolver); optional VirusTotal/SecurityTrails API keys unlock those premium sources.
opsec: active
opsecNote: Subdomain gathering from APIs (crt.sh, AlienVault, SpyOnWeb) is passive, but Seekolver then resolves and connects to each subdomain to check for live HTTP(S) services — those probes reach the target's hosts and can appear in their logs. Route the resolution/probe stage through a controlled egress when discretion matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Small but active open-source recon tool; it aggregates well-known sources, so accuracy tracks those and should be confirmed by re-resolving results.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- dome
aliases:
- Krypteria/Seekolver
tags:
- Domain/IP/Links
- Subdomains scan/brute
- attack-surface
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Seekolver

> A subdomain-to-live-service mapper: collect a domain's subdomains from open sources, resolve them, and flag which are actually serving HTTP(S), with status codes and redirects.

## When to use
You have a `domain` (or an organisation name) and want not just a list of subdomains but **which of them are alive and reachable** — the real web attack/collection surface. Seekolver merges several OSINT subdomain sources and then does the resolution/HTTP check for you, so you skip the dead entries and go straight to live hosts.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `git clone https://github.com/Krypteria/Seekolver && cd Seekolver && pip3 install bs4 requests`.
2. (Optional) create `apitokens.json` with VirusTotal / SecurityTrails keys to add those sources; crt.sh, AlienVault, and SpyOnWeb work without keys.
3. Run: `python3 seekolver.py -te www.corp.com -cn -p 80 443` (target endpoint, resolve, ports to check).
4. Read output: discovered subdomains with resolved `ip-address`, HTTP/HTTPS status codes, and redirect targets.
5. Pivot live hosts into deeper recon (screenshots, tech fingerprinting) and IPs into reverse-IP/hosting.

## Inputs → Outputs
- **In:** `domain` or organisation name (+ optional API keys)
- **Out:** `domain` (subdomains), `ip-address` (resolutions), live-service status
- **Empty/negative result looks like:** few subdomains or none live — small footprint, CDN-fronted, or (without keys) limited to the free sources; add API keys before concluding the surface is small.

## Gotchas & OpSec
- The **HTTP liveness check is active** — it connects to the target hosts; the subdomain-gathering stage is passive.
- Full coverage needs VirusTotal/SecurityTrails keys; without them you see only the free sources' results.
- Aggregated data can be stale — re-resolve before trusting a subdomain is live.

## Overlaps ("do both")
- Overlaps heavily with [[dome]] (both enumerate subdomains from ~similar sources) — run both and union the results, since each source list and each tool's parsing catches subdomains the other misses; Seekolver's edge is the built-in live-service check.

## Trust & verifiability
`trust: community` — an active open-source aggregator adding no data of its own; verify findings by re-resolving hostnames and checking the underlying sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | seekolver |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |

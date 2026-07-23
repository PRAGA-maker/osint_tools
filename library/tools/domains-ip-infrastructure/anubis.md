---
id: anubis
name: Anubis
description: Use when you have a `domain` and want subdomains aggregated from many sources at once — returns discovered sub`domain`s with optional resolved `ip-address`es and cert/host detail.
url: https://github.com/jonluca/Anubis
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-command subdomain enumeration that collates results from many OSINT sources.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open-source (MIT); `pip3 install anubis-netsec`. Some data sources it queries benefit from their own API keys.
opsec: passive
opsecNote: Mostly PASSIVE — it aggregates subdomains from third-party sources (crt.sh, DNSDumpster, VirusTotal, Shodan, NetCraft) rather than hammering the target. Optional resolution/port-scan steps are active and hit the target; skip those for a purely passive footprint.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source subdomain aggregator (jonluca); result completeness depends on the upstream sources and any API keys you supply.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- anubis-netsec
tags:
- domains-ip-infrastructure
- subdomains
- recon
- cli
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Anubis

> A subdomain-enumeration aggregator — one command pulls subdomains from crt.sh, DNSDumpster, VirusTotal, Shodan, NetCraft and more, then optionally resolves and enriches them.

## When to use
You have a `domain` and want a broad subdomain list fast, drawing on many OSINT sources at once rather than querying each by hand. Good as the passive first pass of infrastructure mapping — it leans on third-party datasets, so you can enumerate a target's attack surface with minimal direct contact.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip3 install anubis-netsec`.
2. Run: `anubis -t example.com` (add `-o out.txt` to save; flags enable IP resolution, SSL detail, and port scanning).
3. Read the collated sub`domain` list, with resolved `ip-address`es and host detail if enabled.
4. Pivot: feed subdomains/IPs into `[[dnsrecon]]`, cert-transparency, and service enumeration; unexpected hosts (dev/staging) are high-value leads.

## Inputs → Outputs
- **In:** `domain`
- **Out:** discovered sub`domain`s, optional resolved `ip-address`es, cert/host detail
- **Empty/negative result looks like:** a short/empty list — the domain has few subdomains, or the upstream sources returned little (add API keys for Shodan/VirusTotal to improve coverage).

## Gotchas & OpSec
- Aggregation is passive; the optional resolve/port-scan steps are active and hit the target — omit them for a zero-touch footprint.
- Coverage is only as good as the upstream sources and your API keys; cross-check with another enumerator.
- Third-party sources can rate-limit or return stale data.

## Overlaps ("do both")
- Overlaps with `[[dnsrecon]]` (active brute-force) and `[[google-s-certificate-transparency]]` (CT-only) — Anubis fuses many passive sources; combine with active DNS brute-forcing to catch what passive sources miss.

## Trust & verifiability
`trust: community` — a useful open-source aggregator; because it relays other datasets, verify individual subdomains by resolving them before relying on the list.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | anubis |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |

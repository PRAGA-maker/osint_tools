---
id: subfinder
name: Subfinder
description: Use when you have a `domain` and want its subdomains fast, passively — aggregates dozens of sources into a deduped list of subdomains, returning more domains to map.
url: https://github.com/projectdiscovery/subfinder
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- aws-enumeration
bestFor: Fast passive subdomain enumeration by aggregating many third-party sources into one list.
input: Domain name and optional API credentials for data sources
output: Resolved and unresolved subdomain candidates
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
opsec: passive
opsecNote: By default subfinder pulls from third-party passive sources (cert transparency, DNS aggregators, search APIs) and does NOT send traffic to the target, so the subject isn't alerted. It becomes active only if you pipe results into a resolver/prober. Some sources need your own API keys — isolate those keys from your identity.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: trusted
trustNote: Maintained by ProjectDiscovery, a well-regarded security-tooling team; widely used and open source.
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
- alertx
- cve-map
- dnsx
aliases:
- subfinder
- projectdiscovery/subfinder
tags:
- subdomain-enumeration
- passive-recon
- attack-surface
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Subfinder

> ProjectDiscovery's passive subdomain enumerator — feed it a domain and it queries dozens of sources at once, returning a deduped list of subdomains to expand your map of a target's web presence.

## When to use
You have a `domain` and need its subdomains to widen the attack/OSINT surface — dev/staging boxes, mail, VPN, regional sites, forgotten hosts. Subfinder is passive by default (it asks third-party data sources, not the target), making it a safe first sweep before any active probing. Each subdomain is a new pivot point for DNS, hosting, and content analysis.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest` (or via package manager/Docker).
2. Optionally add API keys for richer sources (Censys, SecurityTrails, VirusTotal, etc.) in the provider config.
3. Run: `subfinder -d example.com -all -o subs.txt`.
4. Read the subdomain list (`selectorsOut`); pipe into a resolver (dnsx) or HTTP prober only when you intend active follow-up, and feed hosts into Censys/Netcraft.

## Inputs → Outputs
- **In:** `domain` (+ optional source API keys)
- **Out:** `domain` — a list of discovered subdomains (resolved and unresolved candidates)
- **Empty/negative result looks like:** few or no subdomains — the domain may be flat, very new, or its subdomains not indexed by passive sources; add API-keyed sources or try active brute-forcing (a separate, noisier step).

## Gotchas & OpSec
- Human-in-the-loop: none to run, but full coverage needs your own source API keys (`api-key`).
- OpSec: passive by default — no packets to the target; it becomes active only when you resolve/probe the results.
- Passive sources have blind spots and stale entries; a subdomain listed may be dead, and one that's live may be missing — verify with resolution before relying on it.

## Overlaps ("do both")
- Pairs with [[dnsx]] (resolve/validate the output) and with Amass, assetfinder, and crt.sh — cross-run because each aggregates different sources; the union is always larger than any single tool's result.

## Trust & verifiability
`trust: trusted` — a flagship ProjectDiscovery tool, open source and widely audited. The tool is reliable; individual results inherit the freshness of their upstream source, so resolve candidates before treating a subdomain as live.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | subfinder |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |

---
id: finalrecon
name: FinalRecon
description: Use when you have a target `domain`/URL and want a one-command footprint — returns headers, WHOIS, DNS, subdomains, ports, directories and Wayback URLs.
url: https://github.com/thewhiteh4t/FinalRecon
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Fast all-in-one web reconnaissance of a domain from a single CLI command.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open-source (MIT); packaged in Kali and BlackArch. Self-hosted CLI, no account.
opsec: active
opsecNote: Several modules are ACTIVE — port scanning, directory brute-forcing and subdomain probing send traffic directly to the target and are logged. Only run against systems you are authorised to test; route through a VPN/Tor and prefer the passive-only modules for recon.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source recon tool (2.9k+ stars) by thewhiteh4t; results are only as current as the upstream data sources it queries.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- FinalRecon web recon
tags:
- domains-ip-infrastructure
- recon
- cli
- footprinting
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- nexfil
- seeker
---

# FinalRecon

> A CLI Swiss-army knife for web reconnaissance — headers, WHOIS, DNS, subdomains, ports, directories and Wayback URLs from one command.

## When to use
You have a `domain` or URL and want a quick, consolidated footprint without stringing together a dozen separate tools. FinalRecon bundles the common recon steps so you get security headers, SSL cert details, DNS records, discovered sub`domain`s, open ports (and their `ip-address`), directory hits and archived URLs in one report.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `git clone https://github.com/thewhiteh4t/FinalRecon && cd FinalRecon && pip3 install -r requirements.txt` (or use the Kali/BlackArch package).
2. Run modules selectively, e.g. `python3 finalrecon.py --headers --whois --dns --url https://example.com`, or `--full` for everything.
3. Read the consolidated output; export is supported.
4. Pivot: discovered subdomains/IPs feed infrastructure mapping; Wayback URLs feed content review; use passive modules first, active ones only when authorised.

## Inputs → Outputs
- **In:** `domain` / URL
- **Out:** headers, WHOIS, DNS, sub`domain`s, open ports + `ip-address`, directories, Wayback URLs
- **Empty/negative result looks like:** a module returning nothing (no subdomains found, all ports filtered, WHOIS privacy-protected) — expected for hardened or well-protected targets.

## Gotchas & OpSec
- `--full` includes ACTIVE scanning (ports, dirs, subdomain probing) that hits and is logged by the target — get authorisation.
- Directory/subdomain brute-forcing can be noisy and slow; scope it.
- Data quality depends on upstream sources (crt.sh, DNS, Wayback) which can lag.

## Overlaps ("do both")
- Overlaps with individual specialist tools (crt.sh for certs, dnsdumpster for DNS) — FinalRecon is the fast first pass; drop to the specialist tool when you need depth on one facet.

## Trust & verifiability
`trust: community` — a widely-used open-source tool; it aggregates other sources rather than producing original data, so verify key findings against the authoritative source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | finalrecon |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |

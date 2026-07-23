---
id: dome
name: DomE
description: Use when you have a `domain` and want to map its subdomains and open ports — a CLI that pulls subdomains from 21 OSINT sources (passive) or brute-forces and port-scans them (active), returning `domain` and `ip-address`.
url: https://github.com/v4d1/Dome
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Exhaustive subdomain enumeration for a domain — combining 21 passive OSINT sources with optional active brute force and port scanning.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free, open-source Python script (v4d1/Dome); some passive sources (VirusTotal, Shodan, SecurityTrails) need free API keys in config.api for full coverage.
opsec: active
opsecNote: Passive mode (`-m passive`) queries only third-party datasets and never touches the target — undetectable. Active mode brute-forces hostnames and port-scans, connecting directly to the target's DNS/hosts and appearing in their logs; use it only with authorization and a controlled egress.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular, actively used open-source recon tool (500+ GitHub stars); aggregates well-known sources, so verifiability rests on those and on re-resolving the results.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- orb
aliases:
- v4d1/Dome
tags:
- Domain/IP/Links
- Subdomains scan/brute
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# DomE

> A focused subdomain-enumeration workhorse: gather a domain's subdomains from 21 OSINT sources passively, then optionally brute-force more and port-scan the live ones.

## When to use
You have a `domain` and want its **attack/asset surface** — every subdomain (dev, staging, mail, vpn, admin panels) and which have open ports. Passive mode is a safe, undetectable first sweep; active mode digs out subdomains the datasets miss via brute force and confirms what's live. Useful for mapping an organisation's or subject's web footprint before targeted collection.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `git clone https://github.com/v4d1/Dome && cd Dome && pip install -r requirements.txt`.
2. (Optional) add API keys to `config.api` to enable VirusTotal / Shodan / SecurityTrails sources.
3. **Passive sweep (stealthy):** `python3 dome.py -m passive -d target.com` — pulls from AlienVault, crt.sh, RapidDNS, ThreatMiner, web.archive.org, and more.
4. **Active dig (authorized only):** `python3 dome.py -m active -d target.com -w wordlist.txt` — brute-forces hostnames, validates live ones, and can port-scan.
5. Export (txt/json/html) and pivot: resolve each subdomain to its `ip-address`, then reverse-IP/hosting to expand the picture.

## Inputs → Outputs
- **In:** `domain` (+ wordlist for active mode)
- **Out:** `domain` (subdomains), `ip-address` (resolutions), open ports
- **Empty/negative result looks like:** few or no subdomains — a small footprint, everything behind a CDN, or (passive) sources without records; run active mode or add API keys before concluding the surface is small.

## Gotchas & OpSec
- **Know your mode:** passive = undetectable, active = touches the target (brute force + scanning) and is logged; never run active against infrastructure you aren't cleared for.
- Full passive coverage needs API keys for the premium sources; without them you get the free subset only.
- Results are only as current as the sources — re-resolve subdomains to drop stale/dead entries.

## Overlaps ("do both")
- Pairs with [[orb]] — Dome is the specialist for deep subdomain enumeration, while orb gives a broader (WHOIS/DNS/ports) but shallower footprint. Run Dome to exhaust subdomains, orb for the surrounding context.

## Trust & verifiability
`trust: community` — a well-regarded open-source aggregator; it introduces no data of its own, so confirm findings by re-resolving hostnames and checking the underlying sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dome |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |

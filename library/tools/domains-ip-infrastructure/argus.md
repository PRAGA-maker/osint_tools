---
id: argus
name: Argus
description: Use when you have a `domain` or `ip-address` and want a broad infrastructure sweep — returns DNS, WHOIS, geo-IP, ports, subdomains, harvested emails, and threat-intel from 130+ modules in one run.
url: https://github.com/jasonxtn/Argus
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Running a broad battery of domain/network/threat-intel recon modules against a target from one CLI.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
- email
- geolocation
status: live
pricing: free
costNote: Free and open source (MIT). Some threat-intel modules (e.g. VirusTotal, Shodan) need your own free API keys to return data.
opsec: active
opsecNote: Many modules touch the target directly — DNS/WHOIS is passive, but port scans, directory discovery, and web crawling send traffic to the target's infrastructure and can be logged. Route active modules through a VPS/sock-puppet IP and avoid scanning hosts you are not authorised to test.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source aggregate recon toolkit (jasonxtn/Argus, ~4k stars); it orchestrates well-known techniques rather than providing its own data. Infrastructure-focused, limited direct person-finding value.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- jasonxtn/Argus
tags:
- recon-toolkit
- python
- network
- domain
source: gh-topic-reconnaissance
lastVerified: '2026-08-04'
enrichment: full
---

# Argus

> A Python "all-in-one" recon toolkit that bundles 130+ modules — network, web-app, and threat-intel — behind a single menu-driven CLI, so one target expands into a full infrastructure picture.

## When to use
You have a `domain` or `ip-address` tied to a subject (a personal site, a company, a server referenced in other findings) and want to enumerate everything around it — resolving records, ownership, hosting geography, open ports, subdomains, and any breach/threat-intel flags — without stringing together a dozen separate tools. It is infrastructure recon, so its person-finding value is indirect: it maps the digital footprint you then pivot from.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and install: `git clone https://github.com/jasonxtn/Argus && cd Argus && pip install -r requirements.txt`.
2. Run it: `python -m argus` (or `pip install argus-recon && argus`). A numbered menu of modules appears in three groups — Network & Infrastructure, Web Application Analysis, Security & Threat Intelligence.
3. Set your target, then run modules by number: e.g. WHOIS, DNS records, subdomain enumeration, geo-IP, port scan, email harvesting.
4. (Optional) Add your own free API keys (VirusTotal, Shodan, etc.) in the config to enable threat-intel modules.
5. Pivot: harvested emails feed email-OSINT tools; subdomains/IPs feed further infrastructure mapping; WHOIS/registrant details feed identity work.

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** `domain` (subdomains), `ip-address`, `email` (harvested), `geolocation` (host country/city), plus WHOIS/registrant, ports, and threat-intel flags
- **Empty/negative result looks like:** modules returning "no records"/timeouts — common for hardened hosts, keyless threat-intel modules, or domains behind privacy proxies; absence of data is not proof of a clean host.

## Gotchas & OpSec
- **Active by default:** port scanning and crawling hit the target directly and may be logged or blocked. Only scan infrastructure you are authorised to assess.
- Keyless threat-intel modules silently return nothing — supply free API keys to get value from them.
- It orchestrates public techniques; results are only as fresh as the upstream data sources.

## Overlaps ("do both")
- Complements focused infrastructure tools in this category — Argus is the wide first pass; use a dedicated WHOIS/DNS/subdomain tool to go deep on whatever Argus surfaces.

## Trust & verifiability
`trust: community` — a widely used open-source project; because it aggregates third-party lookups, verify any high-stakes finding against the underlying source (registrar WHOIS, authoritative DNS) directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | argus |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address, email, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |

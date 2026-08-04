---
id: ote-osint-template-engine
name: OTE (OSINT Template Engine)
description: Use when you have a `domain` and want a broad host/subdomain footprint from a GUI — returns subdomains, resolved `ip-address`es, and related infrastructure.
url: https://github.com/3nock/OTE
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: GUI-driven subdomain enumeration and infrastructure recon across many sources at once.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open source; a locally installed C++/Qt desktop application.
opsec: active
opsecNote: Some enumeration is passive (OSINT sources/passive DNS) but active modules (DNS brute-force, resolution, host probing) send traffic that a target's infrastructure can log. Configure it to prefer passive sources, and route active runs through a VPS/sock-puppet IP for hosts you don't control.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Open-source recon GUI by 3nock (~hundreds of stars), related to the sub3suite project; infrastructure-focused, so limited direct person-finding value.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- spidersuite
- sub3-suite
aliases:
- sub3suite
- 3nock/OTE
tags:
- subdomains
- recon-gui
- osint
source: gh-topic-footprinting
lastVerified: '2026-08-04'
enrichment: full
---

# OTE (OSINT Template Engine)

> A cross-platform Qt desktop GUI for subdomain enumeration and infrastructure recon — pulls hosts and IPs from many sources into one interface without scripting.

## When to use
You have a `domain` (a subject's personal or business site) and want its full host footprint — subdomains, resolved IPs, and related infrastructure — through a point-and-click GUI rather than chained CLI tools. It is infrastructure mapping; person-finding value is indirect (a forgotten subdomain or shared IP can be a pivot), so treat it as a recon-support tool.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download/build OTE from https://github.com/3nock/OTE (C++/Qt; prebuilt releases for major OSes where available).
2. Launch the app and enter the target `domain`.
3. Select enumeration sources/modules — prefer passive OSINT/passive-DNS sources first, then active brute-force/resolution if authorised.
4. Read the results: discovered subdomains, their resolved `ip-address`es, and related hosts.
5. Pivot: feed subdomains/IPs into further infrastructure lookups (WHOIS, certificate transparency, port data) and correlate shared hosting.

## Inputs → Outputs
- **In:** `domain` (or `ip-address` to reverse into hosts)
- **Out:** `domain` (subdomains), `ip-address` (resolutions), related infrastructure
- **Empty/negative result looks like:** few or no subdomains — meaning a small/hardened footprint or keyless/limited sources; absence is not proof the surface is minimal.

## Gotchas & OpSec
- **Active modules touch the target:** DNS brute-force and resolution are logged; only run them against infrastructure you are permitted to assess.
- Some sources need API keys; without them coverage drops silently.
- Desktop GUI — no headless/API automation; results are only as fresh as the upstream sources.

## Overlaps ("do both")
- Related to `[[sub3-suite]]` (same author) and complements web-recon tools like `[[spidersuite]]` — OTE enumerates the host surface; a crawler then explores what each host serves.

## Trust & verifiability
`trust: community` — an established open-source recon project; because it aggregates third-party sources, confirm any high-value host against authoritative DNS/certificate data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ote-osint-template-engine |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | no |

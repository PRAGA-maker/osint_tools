---
id: ghost-eye
name: Ghost Eye
description: Use when you have a `domain` or `ip-address` and want a menu-driven recon sweep — returns WHOIS, DNS, open ports, CMS, and `geolocation`.
url: https://github.com/BullsEye0/ghost_eye
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One local tool with a 14-option menu for WHOIS, DNS, Nmap, headers, CMS, and IP geolocation recon.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
- geolocation
status: live
pricing: free
costNote: Free and open-source (GPL-3.0). Runs locally; needs system tools (Nmap, dnsutils, EtherApe) installed separately.
opsec: active
opsecNote: Several menu options are active — Nmap port scans, traceroute, and header/clickjacking checks send packets directly to the target and are readily logged/IDS-flagged. WHOIS/DNS/cert-transparency options are passive. Only port-scan hosts you're authorised to test, and run from an attribution-safe box.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source recon wrapper by GitHub user BullsEye0; it orchestrates standard utilities (Nmap, whois, dig), so results are as trustworthy as those underlying tools.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- amass
- central-ops
- ip-investigation-toolbox
aliases:
- ghost_eye
tags:
- whois
- dns
- nmap
- recon
source: gh-topic-footprinting
lastVerified: '2026-07-28'
enrichment: full
---

# Ghost Eye

> A Python menu-driven footprinting tool that bundles WHOIS, DNS, Nmap, HTTP-header, CMS, IP-geolocation, traceroute, and certificate-transparency checks behind 14 numbered options.

## When to use
You have a `domain` or `ip-address` from a lead and want to run the common recon checks from one interactive menu instead of remembering each command. Ghost Eye is convenient when triaging a host: what does WHOIS say, what DNS/ports are open, what CMS/tech is it running, where is the IP. Infrastructure-first, so direct missing-person value is low — but WHOIS registrant details and CMS/blog fingerprints can surface a human-facing site to pivot from.

## How to use it (`bestInteractionPattern`: cli)
1. Clone: `git clone https://github.com/BullsEye0/ghost_eye && cd ghost_eye`.
2. Install deps: `pip3 install -r requirements.txt`, and separately install Nmap, dnsutils, EtherApe.
3. Run: `python3 ghost_eye.py`.
4. Choose from the menu (WHOIS, DNS, Nmap scan, HTTP headers, robots.txt, CMS detect, IP geolocation, traceroute, cert transparency, etc.) and enter the `domain`/`ip-address`.
5. Pivot: WHOIS registrant `name`/`address` feeds people-search; open services/CMS feed a browser look for human content; resolved `ip-address` feeds reverse-IP.

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** `domain` (WHOIS, DNS), `ip-address` (ports, hosting), `geolocation` (IP location), plus CMS/tech and cert data
- **Empty/negative result looks like:** privacy-redacted WHOIS, a filtered host returning no open ports, or a menu option erroring because its system tool isn't installed.

## Gotchas & OpSec
- OpSec: the Nmap/traceroute/header options are **active** and intrusive; do not scan systems you aren't authorised to test.
- Depends on external binaries; options fail quietly if Nmap/dnsutils/EtherApe aren't present.
- IP `geolocation` reflects the server's location, not the person's.

## Overlaps ("do both")
- Overlaps `[[central-ops]]` (same WHOIS/DNS data, web-based and passive) and `[[amass]]` (deeper subdomain enumeration); pairs with `[[ip-investigation-toolbox]]` for the IP-side lookups.

## Trust & verifiability
`trust: community` — a single-maintainer open-source wrapper; verify findings against the raw output of the tools it wraps rather than trusting its summary blindly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ghost-eye |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |

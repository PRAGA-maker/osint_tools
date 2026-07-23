---
id: online-port-scanner
name: Online Port Scanner
description: Use when you have an `ip-address` or `domain` and want to enumerate open ports and exposed services from a browser without installing Nmap — returns open ports, running services and banners.
url: https://portscanner.online/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- host-port-discovery
bestFor: Quick browser-based port/service discovery on a host when you can't run a local scanner.
selectorsIn:
- ip-address
- domain
selectorsOut:
- ip-address
status: live
pricing: freemium
costNote: Basic Nmap port scans are free to registered members; advanced techniques (TCP SYN, OS detection, malware/HTTP vuln checks) are gated behind paid membership.
opsec: active
opsecNote: This sends real scan traffic from the service's infrastructure to the target host, and the site keeps a PUBLIC scan history (target, method, ports, time) unless you mark a scan unlisted/private. Your target may see the scan in its logs. Do not scan hosts you are not authorized to probe; mark scans private and use a sock-puppet account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party web front-end wrapping Nmap; operator identity and data handling are not independently verified, and results appear in a public feed.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- port-scanner-online
aliases:
- portscanner.online
tags:
- port-scan
- infrastructure
- network
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Online Port Scanner

> A browser-based Nmap front-end that scans a host for open ports and services without any local install.

## When to use
You have an `ip-address` or `domain` tied to an investigation (a subject's home router, a self-hosted service, a suspicious host) and want to know which ports are open and what services answer — but you're on a locked-down machine where you can't run Nmap locally. Useful for corroborating that a host is live and for fingerprinting the services it exposes.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://portscanner.online/ and register a free account (basic scans require membership).
2. Enter the target hostname or `ip-address`.
3. Pick a scan method — start with the free basic port scan; SYN/OS-detection methods are paid.
4. Set the scan to unlisted/private so it does not appear in the public history feed.
5. Read the results: open/closed ports, detected services, optional banner and OS data, scan duration and geolocated country.
6. Pivot: an open web port feeds domain/infrastructure tools; a service banner can reveal software versions worth researching.

## Inputs → Outputs
- **In:** `ip-address` or `domain`
- **Out:** list of open ports, running services, banners; sometimes the resolved `ip-address` and host country
- **Empty/negative result looks like:** all ports reported closed/filtered — the host may be firewalled, offline, or the free method is too shallow; it does not prove nothing is running.

## Gotchas & OpSec
- **Active scan:** traffic originates from the service and hits the target; the target's logs may record it. Only scan authorized hosts.
- **Public feed:** the default scan history is public — always mark scans private.
- Free tier is intentionally limited to basic scans; deep enumeration needs a paid plan (prefer a local Nmap instead of paying).

## Overlaps ("do both")
- Pairs with `[[port-scanner-online]]` — run both when one front-end's free method is too shallow or rate-limited, since coverage of methods differs.

## Trust & verifiability
`trust: unverified` — an anonymous third-party wrapper around Nmap with a public results feed; treat findings as indicative and re-verify anything important with a scanner you control.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | online-port-scanner |

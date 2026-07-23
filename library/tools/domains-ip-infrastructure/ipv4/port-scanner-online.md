---
id: port-scanner-online
name: Port Scanner Online
description: Use when you have an `ip-address` or `domain` and want to know which ports/services are open without scanning from your own IP — returns open ports and detected services.
url: https://portscanner.online/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- ipv4
bestFor: Browser-based port/service discovery on a host, run from the service's IP rather than your own.
selectorsIn:
- ip-address
- domain
selectorsOut:
- ip-address
status: live
pricing: freemium
costNote: Free basic scans (common ports); advanced scan types, full port ranges, and saved results require registration or a paid plan.
opsec: active
opsecNote: This is ACTIVE reconnaissance — packets hit the target's ports and can trip its firewall/IDS. The scan originates from portscanner.online's servers (not your IP), which shields you somewhat, but the *target* is still probed. Only scan hosts you are authorised to test; unauthorised scanning may be illegal in some jurisdictions.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party online scanner wrapping Nmap/RustScan/Unicornscan; results are only as trustworthy as the service, and it sees which targets you scan.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- shodan
- nmap
- censys
- online-port-scanner
aliases:
- portscanner.online
- Online Port Scanner
tags:
- port-scan
- infrastructure
- recon
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Port Scanner Online

> A browser-based port scanner that probes a host from *its* servers, not yours — quick open-port/service discovery without exposing your own IP to the target.

## When to use
You have an `ip-address` or `domain` and want to see which ports are open and what services answer — to profile exposed infrastructure, confirm a service a subject runs, or check a host before deeper work — but don't want the scan to originate from your own IP. Port Scanner Online runs Nmap/RustScan-class scans from its backend and reports the results in the browser.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://portscanner.online/.
2. Enter the target host/`ip-address`; choose a scan type (common ports on the free tier; full ranges/advanced types are paid).
3. Run the scan and read the results: open/closed/filtered ports and any detected service/version banners.
4. Note the open services for follow-up (a web server → visit it; SSH/RDP → note exposure).
5. Pivot: corroborate passively with `[[shodan]]`/`[[censys]]` (historical, non-intrusive), or run a controlled `[[nmap]]` yourself if you have authorisation and want full control.

## Inputs → Outputs
- **In:** `ip-address` or `domain`
- **Out:** open ports and detected services/versions on the host
- **Empty/negative result looks like:** all ports closed/filtered — a firewall is dropping probes, the host is down, or it genuinely exposes nothing; cross-check with Shodan.

## Gotchas & OpSec
- **Active by design.** The target is probed and may log/alert on it. Only scan hosts you are authorised to test; unauthorised scanning can be unlawful.
- The scan comes from the service's IP, not yours — but the *service* still knows which targets you scanned. Don't use it for operations that must stay wholly private.
- Human-in-the-loop: the free tier caps ports/scan types; deeper scans are paywalled.

## Overlaps ("do both")
- Pairs with `[[shodan]]` and `[[censys]]` (passive, historical port/service data — no packets to the target) and `[[nmap]]` (full local control when you're cleared to scan). Prefer the passive tools first; use active scanning only with authorisation.

## Trust & verifiability
`trust: unverified` — a third-party scanner wrapping standard engines; results are generally reliable for basic ports, but the service observes your targets and the free tier is limited — verify anything critical with your own authorised scan.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | port-scanner-online |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → ip-address |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (payment-wall-partial) |

---
id: ip-dns-leak-detection
name: IP / DNS Leak Detection
description: Use when you want to verify your own VPN/anonymization before an operation — returns your visible IP, DNS resolvers, WebRTC leaks, and geolocation.
url: https://ipleak.net/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
- vpn-tests
bestFor: Confirming a VPN/proxy setup is not leaking your real IP, DNS, or location via WebRTC before touching a target.
selectorsIn:
- ip-address
selectorsOut:
- ip-address
- geolocation
status: live
pricing: free
costNote: Completely free; no account. Run by AirVPN but usable by anyone as a neutral leak-test page.
opsec: active
opsecNote: Connecting reveals your CURRENT IP/DNS to ipleak's servers — that is the entire point, so run it only through the exact tunnel you intend to operate behind, never from your real connection while thinking about a case.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by AirVPN; a long-standing, widely recommended leak-test tool. It reports observed connection facts, not third-party claims.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- user-agent-string-decoder
aliases:
- ipleak.net
- IP leak test
- DNS leak test
tags:
- opsec
- vpn
- leak-test
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# IP / DNS Leak Detection

> A one-page self-audit of your own anonymity: what IP, DNS resolvers, and location the internet actually sees when you connect.

## When to use
Before running any active OSINT step (logging into a sock puppet, hitting a target's site, querying an auth endpoint), verify that your VPN/proxy chain is not leaking your real identity. ipleak.net shows the IP the site sees, the DNS servers resolving your queries, any WebRTC leak that bypasses the tunnel, and your browser-reported geolocation. It is a defensive OpSec tool for the investigator, not a way to research a subject — though you can also paste an arbitrary `ip-address` into its lookup to get geolocation on it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Connect through the exact VPN/proxy you plan to operate behind.
2. Open https://ipleak.net/ and let it auto-run.
3. Check each panel: the shown IP should be your VPN exit (not your ISP); the DNS servers should belong to the VPN, not your ISP; the WebRTC section must NOT reveal a second, real IP.
4. If WebRTC exposes your real IP, disable WebRTC in the browser (or use a hardened profile) and re-test.
5. Optional: use its IP lookup box to geolocate a target `ip-address`. Only proceed to your operation once every panel shows the intended anonymized values.

## Inputs → Outputs
- **In:** your live connection (or an `ip-address` to look up)
- **Out:** visible `ip-address`, DNS resolver IPs, WebRTC-exposed IPs, and `geolocation` (country/region/city/ASN)
- **Empty/negative result looks like:** if the page shows your real ISP IP or hometown, your setup is LEAKING — that is a failure state to fix, not a benign empty result.

## Gotchas & OpSec
- This is an **active** self-test: you are handing ipleak your current IP/DNS by design — so only run it through the tunnel you'll actually use.
- WebRTC leaks are the classic trap: the main IP can look correct while WebRTC quietly reveals the real one. Always read that panel.
- Geolocation is MaxMind-based and may be cached/approximate — fine for a sanity check, not forensic.
- Re-test after any network/VPN change; a tunnel that was clean yesterday can leak after a reconnect.

## Overlaps ("do both")
- Pairs with `[[user-agent-string-decoder]]` — ipleak covers network-layer leaks (IP/DNS/WebRTC) while UA analysis covers the browser-fingerprint layer; check both before operating.

## Trust & verifiability
`trust: trusted` — a reputable, long-running leak tester (AirVPN); it reports directly observed connection facts, which are authoritative for the moment you test.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ip-dns-leak-detection |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | ip-address → ip-address, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |

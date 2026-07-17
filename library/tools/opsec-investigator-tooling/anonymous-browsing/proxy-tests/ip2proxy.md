---
id: ip2proxy
name: IP2Proxy
description: Use when you have an `ip-address` and want to know if it's a VPN/proxy/Tor/hosting IP — returns proxy-type classification, ISP and `geolocation` (also handy to test your own exit-node's exposure).
url: https://www.ip2proxy.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
- proxy-tests
bestFor: Classifying whether an IP is a VPN/proxy/Tor/data-center address, and vetting your own anonymization IPs before an operation.
selectorsIn:
- ip-address
selectorsOut:
- ip-address
- geolocation
status: live
pricing: freemium
costNote: Free web demo lookups and a limited free API tier; the full database, bulk queries, and high-volume API need a paid IP2Location plan.
opsec: passive
opsecNote: A passive database lookup — you query IP2Proxy's classification data, not the IP itself, so the address's owner isn't contacted. Its main OpSec use is defensive: check whether your VPN/proxy exit IP is already flagged as an anonymizer before you use it, since flagged IPs blow your cover.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial proxy-detection dataset by IP2Location. Classifications are heuristic (based on known ranges) and generally reliable but not infallible.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- ipqualityscore
- ipinfo-io
aliases:
- ip2proxy.com
- IP2Location Proxy Detection
tags:
- ip
- proxy-detection
- vpn
- opsec
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# IP2Proxy

> A proxy/VPN/Tor classifier for IP addresses — tells you whether an IP is an anonymizer or data-center address, both for vetting a subject's IP and for checking your own cover.

## When to use
Two cases. **Offensively:** you have an `ip-address` (from an email header, server log, or another tool) and want to know if the subject was hiding behind a VPN/proxy/Tor or connecting from a residential line — a flagged IP means their real location is masked. **Defensively (its listed purpose here):** before an operation, check whether *your* VPN/proxy exit IP is already known/flagged as an anonymizer, since a flagged exit node signals to targets that you're hiding and undermines a sock-puppet's credibility.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.ip2proxy.com/ and use the demo lookup (or the free API tier).
2. Enter the `ip-address`.
3. Read the classification: proxy type (VPN / Tor / public/web proxy / data-center-hosting / residential), plus ISP and country `geolocation`.
4. Interpret: "residential + matching country" is consistent with a real user; "VPN/hosting/Tor" means the IP is anonymized and its geolocation is not the person's true location.
5. Pivot: a residential classification makes IP-geolocation worth trusting for a subject; a flagged classification tells you to look for the real IP elsewhere, or (for your own IP) to switch exit nodes.

## Inputs → Outputs
- **In:** `ip-address`
- **Out:** proxy-type classification, ISP, and country-level `geolocation` for the `ip-address`
- **Empty/negative result looks like:** "not a proxy"/residential — the IP isn't in the proxy database. That doesn't guarantee it's a home user (new/obscure VPNs may be unlisted), just that it isn't a *known* anonymizer.

## Gotchas & OpSec
- Detection is heuristic and based on known ranges — fresh or private VPN endpoints can slip through as "residential."
- Free demo is rate-limited; heavy or automated use needs a paid IP2Location plan.
- OpSec: passive; the IP owner is not contacted. Its best use is pre-flight self-checking of your own anonymization IPs.

## Overlaps ("do both")
- Pairs with `[[ipqualityscore]]` (a second proxy/fraud-risk opinion — agreement raises confidence) and `[[ipinfo-io]]` (ASN/geolocation context) — cross-check classifications since no single proxy database is complete.

## Trust & verifiability
`trust: community` — a commercial IP2Location dataset. Classifications are reliable leads but heuristic; corroborate a critical "residential vs anonymizer" determination with a second detection source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ip2proxy |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | ip-address → ip-address, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

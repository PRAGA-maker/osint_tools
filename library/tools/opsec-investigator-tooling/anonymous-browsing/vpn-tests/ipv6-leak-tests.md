---
id: ipv6-leak-tests
name: IPv6 Leak Tests
description: Use when you are on a VPN and want to confirm your real IPv6 `ip-address` isn't leaking past it — returns your exposed IPv6 (or a clean pass).
url: https://ipv6leak.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
- vpn-tests
bestFor: Verifying an IPv4-only VPN isn't leaking your real IPv6 address on a dual-stack connection.
selectorsIn: []
selectorsOut:
- ip-address
status: live
pricing: free
costNote: Free public test run by Private Internet Access (PIA); no account or payment to run it.
opsec: active
opsecNote: The test deliberately probes your own connection and will surface your real IPv6 if it leaks — that's the point. Run it on YOUR machine before any collection, never as a step against a target. It is a PIA-branded page and pushes their VPN.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Operated by Private Internet Access, an established VPN vendor; the leak check is genuine but the page is also marketing for their product.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- useragentstring-com
aliases:
- ipv6leak.com
- IPv6 leak test
tags:
- opsec
- vpn
- ipv6
- leak-test
- anonymity
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# IPv6 Leak Tests

> A one-click check for the classic VPN failure: your IPv4 traffic is tunnelled but your IPv6 traffic slips out on your real address.

## When to use
Before you begin any active collection through a VPN, confirm the tunnel is actually covering you. Many VPNs only route IPv4; on a dual-stack ISP connection your IPv6 requests can bypass the tunnel entirely, revealing your true `ip-address` (and therefore your real location/ISP) to anything you contact. This is your own pre-flight OpSec check, not a lookup on a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Connect to your VPN as you would for the investigation.
2. Open https://ipv6leak.com/ and click **Start Test**.
3. Read the result:
   - **No IPv6 detected / not reachable** → good; IPv6 is disabled or tunnelled, no leak.
   - **An IPv6 address is shown** → LEAK. That address is your real one and is escaping the VPN.
4. If it leaks: disable IPv6 on the OS/adapter (or switch to a VPN that handles IPv6), then re-test until clean.
5. Pivot: pair with a DNS-leak test and a WebRTC test — IPv6 is only one of several ways a real IP escapes.

## Inputs → Outputs
- **In:** nothing to type — it probes your live connection automatically
- **Out:** your exposed IPv6 `ip-address` if leaking, or a "no leak" confirmation
- **Empty/negative result looks like:** "no IPv6" — meaning either your network is IPv4-only or the tunnel is holding; that's the pass state, not a failure.

## Gotchas & OpSec
- Human-in-the-loop: none beyond clicking Start.
- The page is PIA marketing; ignore the upsell — the test itself is legitimate.
- OpSec: labelled **active** because it intentionally elicits and displays *your own* real IPv6. Never run it while you believe you're anonymous and then assume the shown address is safe to ignore — a shown address is a failure you must fix.
- A "pass" only covers IPv6; it says nothing about DNS or WebRTC leaks.

## Overlaps ("do both")
- Pairs with [[useragentstring-com]] — this locks down what IP you leak, that locks down what your browser claims to be; a clean network fingerprint with a suspicious UA (or vice-versa) still stands out.

## Trust & verifiability
`trust: community` — run by an established VPN vendor (PIA); the mechanism is sound and reproducible, but treat the surrounding product claims as advertising, not neutral advice.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ipv6-leak-tests |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  → ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |

---
id: browser-leaks
name: BrowserLeaks
description: Use when you (the investigator) want to check your own OpSec before an operation — returns what your browser leaks (real IP, WebRTC, DNS, canvas/WebGL/font fingerprint) so you can plug the gaps.
url: https://browserleaks.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
bestFor: Auditing your own browser/VPN setup for IP and fingerprint leaks before doing active OSINT.
selectorsIn:
- ip-address
selectorsOut:
- ip-address
- device-id
status: live
pricing: free
costNote: Completely free; no account required.
opsec: active
opsecNote: This tests YOUR machine, not a target — run it on the sock-puppet browser you will investigate from. It reveals whether your real IP leaks past a VPN (WebRTC/DNS) and how identifiable your fingerprint is. Do not run it while logged into personal accounts; the point is to confirm your investigative profile is clean.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-established, widely-cited privacy-testing suite used across the security community; results reflect your own browser and are directly reproducible.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- webrtc-leak-test
- dnsleaktest
aliases:
- browserleaks.com
tags:
- opsec
- fingerprint
- webrtc
- privacy
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# BrowserLeaks

> A suite of browser privacy tests that shows exactly what your browser reveals — real IP, WebRTC/DNS leaks, and canvas/WebGL/font fingerprints — so you can harden the machine you investigate from.

## When to use
Before running any **active** OSINT (touching a target's infrastructure, logging into sock-puppet accounts, clicking links) you must know your investigative browser isn't leaking your true identity. BrowserLeaks is a self-check: run it from your sock-puppet/VPN setup to confirm your real `ip-address` doesn't leak via WebRTC or DNS behind the VPN, and to see how unique (trackable) your browser fingerprint is. It protects the investigator, not the subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. On the exact browser/VPN profile you'll investigate from, go to https://browserleaks.com/.
2. Run the **IP Address** test — confirm it shows the VPN's IP, and check the WebRTC and DNS sections for any leak of your real IP.
3. Run **WebRTC**, **DNS Leak**, **Canvas**, **WebGL**, and **Fonts** tests — note whether your fingerprint is distinctive.
4. If your real IP or ISP appears, fix it (disable WebRTC, use a leak-proof VPN/DNS) and re-test until clean.
5. Repeat whenever you change VPN, browser, or extensions — leaks reappear after config changes.

## Inputs → Outputs
- **In:** `ip-address` (your own, implicitly — the browser under test)
- **Out:** your visible `ip-address` (and any leaked real IP), `device-id` (fingerprint uniqueness), leak vectors (WebRTC/DNS/IPv6)
- **Empty/negative result looks like:** the "clean" state — only the VPN IP shows, no WebRTC/DNS leak of your real IP, and a common/blendable fingerprint. That's the pass condition, not a failure.

## Gotchas & OpSec
- This is an OpSec tool for YOU; it returns nothing about a target. Don't confuse it with a lookup tool.
- A common failure is WebRTC leaking the real IP even with a working VPN — check that section specifically.
- Fingerprint "uniqueness" is relative; the goal is to blend in, not to be perfectly blank (a too-empty fingerprint is itself distinctive).

## Overlaps ("do both")
- Pairs with `[[webrtc-leak-test]]` and `[[dnsleaktest]]` — dedicated single-vector testers that confirm BrowserLeaks' findings; run more than one before trusting your setup.

## Trust & verifiability
`trust: trusted` — a well-known, community-standard privacy-testing suite; every result reflects your own browser and can be re-run instantly to verify a fix.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | browser-leaks |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | ip-address → ip-address, device-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |

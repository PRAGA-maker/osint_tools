---
id: whatsmybrowser-org
name: WhatsMyBrowser.org
description: Use when hardening an investigator sock-puppet browser and you want to see the fingerprint it leaks — returns the device-id/fingerprint you expose.
url: https://www.whatsmybrowser.org/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
- browser-tests
bestFor: Checking what your browser reveals (user-agent, version, OS, IP, capabilities) to verify a sock-puppet setup looks plausible.
selectorsIn: []
selectorsOut:
- ip-address
- device-id
status: live
pricing: free
costNote: Free; no account. Generates a shareable link describing the visiting browser.
opsec: passive
opsecNote: This tests YOUR browser, not a target — but it profiles you: run it through the exact VPN/proxy + browser profile you will use for collection, and confirm the reported IP and user-agent match your cover, not your real setup.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running, well-known browser-diagnostics site used widely for support; reports the standard signals a browser exposes.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- whatsmybrowser.org
- What's My Browser
tags:
- browser-fingerprint
- opsec
- anonymous-browsing
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# WhatsMyBrowser.org

> A quick mirror that shows exactly what your browser tells every site it visits — a sanity check that your sock-puppet setup leaks what you intend, and nothing that unmasks you.

## When to use
Before doing active collection from a sock-puppet, you want to confirm the browser/VPN combination presents a consistent, unremarkable identity: the right `ip-address` (your cover VPN exit, not your home IP), a common user-agent/OS, and no obvious tells. Loading this page from your operational profile shows the exposed signals so you can catch leaks (real IP bleeding through, a WebRTC/DNS mismatch, an oddball user-agent that stands out) before a target's site logs them.

## How to use it (`bestInteractionPattern`: web-manual)
1. Spin up the **exact** operational setup — VPN/proxy on, the sock-puppet browser profile.
2. Visit https://www.whatsmybrowser.org/.
3. Read the report: user-agent, browser + version, OS, screen, and the detected public IP.
4. Verify against your cover story — IP geolocates to the intended region, user-agent matches a common device, nothing reveals your real OS/network.
5. Cross-check deeper fingerprint vectors (WebRTC leak, DNS, canvas/font entropy) with a dedicated fingerprint tester; this covers the basics.

## Inputs → Outputs
- **In:** (none — it inspects the visiting browser itself)
- **Out:** the `ip-address` and browser/OS `device-id`-style fingerprint you are exposing
- **Empty/negative result looks like:** the report shows your **real** IP or an inconsistent user-agent — a red flag that your anonymity setup is misconfigured; fix before proceeding.

## Gotchas & OpSec
- It only shows basic signals — it is **not** a full anti-fingerprinting audit (no canvas/WebRTC/audio entropy). Pair it with a dedicated fingerprint/leak tester.
- Always run it through the operational stack; testing your clean host tells you nothing about the puppet.
- OpSec: passive, but it profiles you — treat a leaked real IP here as a near-miss and remediate.

## Overlaps ("do both")
- Pair with a full fingerprint/leak suite (WebRTC leak test, canvas-entropy checkers) — this gives the fast headline check; those catch the advanced vectors that deanonymize a puppet.

## Trust & verifiability
`trust: trusted` — a well-established diagnostics site; the signals it reports are simply what your browser sends, so the readout is inherently accurate (it is reflecting your own request back to you).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whatsmybrowser-org |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | (none) → ip-address, device-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

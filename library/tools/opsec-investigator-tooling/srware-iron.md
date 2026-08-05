---
id: srware-iron
name: SRWare Iron
description: Use when you want a Chromium-based investigation browser with Google's phone-home telemetry stripped out — supports lower-noise sock-puppet browsing rather than returning selectors.
url: http://www.srware.net/en/software_srware_iron.php
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A de-Googled Chromium build for cleaner, lower-telemetry sock-puppet browsing.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free download for Windows/macOS/Linux/Android; open-source-derived (Chromium).
opsec: passive
opsecNote: This is opsec infrastructure, not a data source. Iron removes Chrome's built-in Google identifiers/telemetry (RLZ, install-id, background phone-home), reducing what leaks to Google — but it does NOT hide your IP. Pair it with a VPN/Tor and a dedicated profile per sock puppet. It is not high-assurance anonymity by itself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: A long-standing third-party Chromium fork by SRWare; its core is Chromium, though the specific privacy patches are the vendor's and are not independently audited each release.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Iron browser
- SRWare Iron browser
tags:
- browsers
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# SRWare Iron

> A Chromium fork that strips Google's telemetry/identifiers — a familiar-feeling but quieter browser for sock-puppet collection.

## When to use
Not a lookup tool — it produces no selectors. Reach for it when you want the Chrome experience (extensions, dev-tools) for **passive collection** but without Chrome's built-in Google phone-home. Useful as a dedicated investigation browser where you keep each sock-puppet identity in its own profile and don't want the browser itself leaking install IDs and usage telemetry to Google.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download Iron from http://www.srware.net for your OS and install it on a dedicated investigation machine/VM.
2. Create a **separate Iron profile per sock-puppet identity** so cookies/logins never cross investigations.
3. Turn on your IP-masking layer first (VPN/Tor) — Iron does not do this for you.
4. Browse target public content; load reverse-image/lookup tools inside it as needed.
5. Treat it purely as the container; the investigative payload is whatever you view/run in it.

## Inputs → Outputs
- **In:** none (it is a browser)
- **Out:** none (it renders pages; findings come from what you view)
- **Empty/negative result looks like:** N/A — success is "I browsed without Chrome's Google telemetry and without cross-contaminating identities."

## Gotchas & OpSec
- **It masks telemetry, not your IP.** Do not mistake "de-Googled" for "anonymous"; layer a VPN/Tor and a disposable OS for real anonymity.
- The privacy patches are vendor-specific and closed to per-release audit — trust it for telemetry reduction, not as a guaranteed hardened browser.
- Being Chromium-based, sites still fingerprint it much like Chrome; combine with anti-fingerprinting hygiene if that matters.

## Overlaps ("do both")
- Interchangeable with other privacy Chromium/Firefox forks used as sock-puppet browsers; the value is the container, so pick one and pair it with real IP masking and profile isolation.

## Trust & verifiability
`trust: community` — its engine is mainstream Chromium (trustworthy), but the telemetry-stripping claims are the vendor's own and unaudited, so verify behaviour with a network monitor if the threat model demands it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | srware-iron |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |

---
id: opera
name: Opera
description: Use when you need a low-cost opsec browser for passive collection — its built-in free VPN and per-window profile isolation help mask your IP and separate investigations — supports sock-puppet browsing rather than returning selectors.
url: https://www.opera.com
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A free browser with a built-in VPN and easy profile separation for sock-puppet, IP-masked collection.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free desktop/mobile browser; the built-in "free VPN" (a browser-scoped proxy) is included at no cost, with a paid Opera VPN Pro upsell you do not need for basic masking.
opsec: passive
opsecNote: This is opsec infrastructure, not a data source. The built-in VPN is a browser-scoped proxy, NOT a full-device VPN or Tor — it hides your IP from visited sites but is not high-assurance anonymity, is logged by Opera/its provider, and leaks outside the browser. Treat it as light IP masking; layer a real VPN + disposable OS for anything sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Mainstream commercial browser from Opera Software; legitimate and widely used, though the free VPN is a proxy service whose logging/ownership you should not treat as zero-knowledge.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- search-by-image
aliases:
- Opera Browser
- Opera VPN
tags:
- browsers
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# Opera

> A free mainstream browser whose built-in VPN/proxy and easy profile isolation make it a convenient sock-puppet collection tool — opsec infrastructure, not a data source.

## When to use
Not a lookup tool — it produces no selectors. Reach for it when you need a quick, disposable browsing environment for **passive collection**: viewing a target's public pages while masking your IP (built-in VPN) and keeping each investigation walled off in its own window/profile. Useful as a lightweight sock-puppet browser when you don't want your real IP hitting the pages you visit.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install Opera on a dedicated investigation machine/VM.
2. Enable the built-in VPN (Settings → Privacy → VPN), then toggle it on from the address-bar badge; pick a region.
3. Use a **separate Opera profile** (or private window) per sock-puppet identity so cookies/logins don't bleed across investigations.
4. Browse the target's public content as normal — the visited sites see the VPN's IP, not yours.
5. For images you encounter, hand off to a reverse-image workflow such as `[[search-by-image]]`.

## Inputs → Outputs
- **In:** none (it is a browser, not a query tool)
- **Out:** none (it renders pages; the investigative payload is whatever you view)
- **Empty/negative result looks like:** N/A — success is "I viewed the target's public pages without exposing my real IP or cross-contaminating identities."

## Gotchas & OpSec
- The "free VPN" is a **browser-scoped proxy**, not device-wide and not Tor. It masks your IP from visited sites but is logged and is not high-assurance anonymity. Do not rely on it for anything where exposure has real consequences.
- Traffic outside the browser (OS, other apps) is not covered.
- For strong anonymity, layer a real VPN and a disposable OS; use Opera's VPN only as convenient light masking.

## Overlaps ("do both")
- Pairs with any reverse-image or lookup tool you run inside it — e.g. `[[search-by-image]]` — since Opera is the safe container, and those tools do the actual finding.

## Trust & verifiability
`trust: trusted` — Opera is a legitimate, widely-used commercial browser. The caveat is not authenticity but the free VPN's real (limited) privacy properties, which you must not overestimate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | opera |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |

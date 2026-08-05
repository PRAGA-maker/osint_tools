---
id: tor-browser
name: Tor Browser
description: Use when you need to browse investigation targets without exposing your real IP, or to reach .onion dark-web sites — returns anonymized web access (investigator OpSec).
url: https://www.torproject.org/download/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Browsing targets and dark-web (.onion) sites with your origin IP hidden behind the Tor network.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source, published by the non-profit Tor Project.
opsec: passive
opsecNote: The core OpSec tool — it hides your real IP from sites you visit by routing through three Tor relays. But logging into any real/attributable account over Tor destroys that anonymity; keep sock-puppet identities strictly separate, and never resize the window or install plugins (both aid fingerprinting).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Built and maintained by the Tor Project non-profit; the reference implementation for anonymous browsing, open source and widely audited.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- exonerator
- exonerator-ip-address-checker
- tor-download
- tor-project
aliases:
- Tor
- torbrowser
tags:
- browsers
- anonymity
- dark-web
- opsec
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# Tor Browser

> The Tor Project's hardened browser: it routes your traffic through the Tor network so the sites you investigate see an exit-node IP, not yours — and it is the standard doorway to .onion dark-web resources.

## When to use
Any time visiting a target could burn you — checking a subject's own site or infrastructure, viewing content that might log and geolocate visitors, or reaching dark-web (.onion) marketplaces and forums during a case. Tor Browser hides your origin IP and ships pre-configured to resist tracking, so it is the default browsing surface for sensitive OSINT rather than a data source itself.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download **only** from https://www.torproject.org/download/ (avoid mirrors) and verify the signature; install on your investigation machine/VM.
2. Launch and connect to the Tor network (use a bridge if Tor is blocked on your network).
3. Browse targets or paste a `.onion` address. Keep the security level appropriate to the task (higher levels disable risky scripts).
4. Do **not** log into personal or attributable accounts; treat each Tor session as a clean, separate identity.
5. Pivot: use it as the safe carrier for other web-manual lookups whenever attribution risk is high.

## Inputs → Outputs
- **In:** a URL or `.onion` address to visit (no subject data typed into the tool itself)
- **Out:** the page, fetched with your real IP hidden behind a Tor exit node
- **Empty/negative result looks like:** a site blocks Tor exit nodes (CAPTCHA walls, 403s) — common on major platforms; switch circuits or fall back to a sock-puppet VPN for that specific site.

## Gotchas & OpSec
- Human-in-the-loop: none for setup, but discipline is everything — a single login to a real account over Tor links your identity to the session.
- OpSec: passive and protective. Fingerprinting risks remain: never maximise/resize the window, add extensions, or open downloaded files while online.
- Slower than normal browsing, and many mainstream sites throttle or block Tor — expect friction, not failure.

## Overlaps ("do both")
- Pairs with [[exonerator]] (checks whether an IP was a Tor exit node at a given time) and a sock-puppet VPN — Tor for anonymity, a VPN for sites that block Tor; do both to cover the full target set.

## Trust & verifiability
`trust: trusted` — the official Tor Project release, open source and heavily audited. Download and verify from torproject.org only; malicious repackaged "Tor" builds exist and are a known threat.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tor-browser |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |

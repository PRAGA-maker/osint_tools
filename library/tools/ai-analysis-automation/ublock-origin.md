---
id: ublock-origin
name: uBlock Origin
description: Use when you are browsing target sites and want to block ads, trackers, and beacons that could fingerprint your investigation browser — a content blocker for OpSec, not a selector tool.
url: https://github.com/gorhill/uBlock
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Hardening a sock-puppet investigation browser against trackers, ads, and fingerprinting scripts.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (GPL-3.0); available for Firefox and Chromium browsers.
opsec: passive
opsecNote: This is a defensive OpSec tool — it reduces what third-party trackers can learn about your browsing session. It does not anonymize you (use Tor/VPN + a burner profile for that); it just cuts tracker/ad noise and some fingerprinting.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: A flagship open-source content blocker by Raymond Hill (gorhill), widely audited and recommended; efficient and transparent.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools: []
aliases:
- uBO
- uBlock
tags:
- opsec
- privacy
- browser-extension
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# uBlock Origin

> A fast, open-source content blocker — part of the OpSec baseline for an investigation browser, cutting the ads, trackers, and beacons that would otherwise profile your session.

## When to use
You are setting up (or working in) a sock-puppet browser profile to visit a subject's sites and social pages. uBlock Origin blocks the ad networks, analytics, and tracking beacons those pages load, reducing the third-party data trail your investigative browsing leaves and stripping distracting/fingerprinting content. It produces no intelligence; it is protective infrastructure for how you browse.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install uBlock Origin from your browser's add-on store (Firefox) or a Chromium-compatible build; prefer it on a dedicated investigation profile.
2. Keep the default filter lists (they cover ads + major trackers); enable additional privacy/annoyance lists as needed.
3. Optionally use the element picker / logger to see and block specific trackers on a page.
4. Browse target sites with the noise and beacons suppressed.
5. Nothing to pivot to — this shapes the OpSec of every browsing-based tool you use.

## Inputs → Outputs
- **In:** none (runs passively in the browser)
- **Out:** a cleaner, less-tracked browsing session (no case selectors)
- **Empty/negative result looks like:** N/A — success is invisible; the logger shows what it blocked if you want confirmation.

## Gotchas & OpSec
- Human-in-the-loop: none beyond install/config.
- OpSec: it **reduces tracking**, it does **not** anonymize you — your IP and browser fingerprint still exist. Combine with Tor/VPN and a burner profile for real anonymity.
- Aggressive filtering can break some sites; whitelist per-site if a target page misbehaves.
- Install only the genuine gorhill build; many copycat "uBlock" extensions exist.

## Overlaps ("do both")
- Complements anonymity layers (Tor Browser, VPNs) and sock-puppet hygiene: uBlock cuts tracker noise, while those hide *who and where* you are. Use them together, not interchangeably.

## Trust & verifiability
`trust: trusted` — a widely audited, open-source flagship privacy tool from a reputable maintainer; behavior is transparent and its block logger lets you verify exactly what it stops.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ublock-origin |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |

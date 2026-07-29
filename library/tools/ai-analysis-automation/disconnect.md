---
id: disconnect
name: Disconnect
description: Use when you want to block trackers during investigative browsing or understand who tracks a site — returns a tracker-blocking layer and tracker classification data.
url: https://disconnect.me
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Reducing tracker/telemetry leakage in your investigative browser and seeing what trackers a page loads.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free consumer browser extensions/apps (its tracker list powers Firefox/Edge protection); enterprise and the Lightbox privacy-intelligence API are paid.
opsec: passive
opsecNote: This is defensive tooling for YOUR browser — it blocks third-party trackers so your investigative sessions leak less. It is not a lookup you point at a subject and does not anonymize you (no IP masking). Pair with a VPN/Tor when origin-hiding matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Disconnect is an established privacy company whose open tracker-protection lists are used by major browsers; reputable and widely vetted.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- ublock-origin
- waterfox
aliases:
- Disconnect.me
- Disconnect Privacy
tags:
- privacy
- tracker-blocking
- opsec
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Disconnect

> A tracker-blocking browser extension (and the open tracker list behind Firefox/Edge protection) — investigator hygiene that reduces how much your browsing leaks, and shows you what a page tries to track.

## When to use
Two uses, both defensive. (1) **Session hygiene:** install it in your investigative browser so third-party trackers can't build a profile of your OSINT activity across sites. (2) **Tracker recon:** its visualization shows which tracking companies a given page loads — occasionally useful when profiling a site's ad/analytics stack. It takes no subject selector and returns no personal data; it protects your side of the glass.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the Disconnect extension from https://disconnect.me for your browser (Chrome/Firefox/etc.), or rely on the built-in protection in Firefox/Edge that uses Disconnect's list.
2. Browse as normal; it blocks known third-party trackers automatically.
3. Open the extension popup on a page to see which trackers were blocked/categorized.
4. Combine with per-site container tabs (e.g. in `[[waterfox]]`) to keep sock-puppet identities isolated.
5. For network-level anonymity (IP), add a VPN/Tor — Disconnect does not hide your IP.

## Inputs → Outputs
- **In:** none (a browser layer, not a query tool)
- **Out:** blocked-tracker counts / classification for the current page; reduced tracking of your session
- **Empty/negative result looks like:** N/A — success is fewer trackers loaded; the popup simply shows what it caught.

## Gotchas & OpSec
- **Privacy ≠ anonymity:** it stops trackers, not IP-based identification. Combine with VPN/Tor when origin must be hidden.
- Aggressive blocking can break some site functionality; whitelist per-site if a target page won't render.
- OpSec: **passive/defensive** — your tooling, not aimed at a subject.

## Overlaps ("do both")
- Pairs with `[[ublock-origin]]` and `[[waterfox]]` — uBlock Origin is the heavier content/ad blocker, Waterfox the hardened browser; Disconnect adds its curated tracker list and per-page tracker visibility. Running a blocker plus a hardened browser is the standard hygiene stack.

## Trust & verifiability
`trust: trusted` — a long-standing privacy company whose open tracker lists are adopted by mainstream browsers; transparent and independently used.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | disconnect |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |

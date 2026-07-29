---
id: netsurf
name: NetSurf
description: Use when you want a lightweight, minimal-footprint web browser for a disposable/low-resource investigation VM — a small independent browser, not a data-returning tool.
url: http://www.netsurf-browser.org
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A tiny, fast, independent-engine browser for constrained or throwaway investigation environments.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source (GPLv2); no account.
opsec: passive
opsecNote: NetSurf's own layout engine gives it a browser fingerprint distinct from Chrome/Firefox — that is unusual and can itself make you stand out, and its limited support for modern JS/TLS may break sites or degrade sandboxing you rely on. Do not use it as your primary target-facing browser where blending in matters; a hardened mainstream browser or Tor Browser is safer for attributable work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Long-running open-source project (GPLv2) with its own C layout engine; last stable release 3.11 (Dec 2023). Community-maintained, not a security-hardened browser.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- netsurf-browser
tags:
- toddington
- curated-directory
- web-browsers
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# NetSurf

> A featherweight, independent-engine web browser — useful for spartan or throwaway investigation machines, not an OSINT data source in itself.

## When to use
You need a browser that runs on minimal hardware or in a stripped-down VM (old machine, low RAM, non-mainstream OS like RISC OS/AmigaOS, or a deliberately minimal analysis box). NetSurf loads fast and has a tiny footprint. It returns no selectors of its own — it is infrastructure for browsing, listed here as an opsec/tooling option, not a lookup service.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download the build for your platform (Linux/UNIX, macOS, RISC OS, AmigaOS) from netsurf-browser.org, or install from your distro's package manager.
2. Launch it as you would any browser and navigate to the sites you need.
3. Use it where its small footprint helps — a low-resource sandbox, an air-gapped review box, retro hardware.
4. Fall back to a mainstream/Tor browser for anything requiring modern JavaScript, WebGL, or strong anti-fingerprinting.

## Inputs → Outputs
- **In:** none (it is a browser, not a query tool)
- **Out:** none (renders web pages)
- **Empty/negative result looks like:** N/A — but note pages heavy on modern JS may render incompletely or not at all.

## Gotchas & OpSec
- **Distinct fingerprint:** its own engine means a rare User-Agent and JS surface; that makes you *more* identifiable, not less — the opposite of what you want when blending into normal traffic.
- Limited modern-web support (partial JS, older TLS/CSS) can break logins and dynamic sites.
- **Passive**: the browser itself leaks nothing beyond normal HTTP requests, but treat it as unhardened — no built-in tracker/ad blocking, no anti-fingerprinting.

## Overlaps ("do both")
- Sits alongside other browser/opsec tooling in this category; choose Tor Browser when anonymity matters and NetSurf only when a minimal footprint is the actual requirement.

## Trust & verifiability
`trust: community` — a mature, openly developed GPL project, safe to install, but community-maintained and not a security-focused browser; don't rely on it for anonymity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | netsurf |

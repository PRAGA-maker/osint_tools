---
id: centbrowser
name: Cent Browser
description: Use when you need a hardened, multi-identity browsing setup for sock-puppet research — a Chromium-based browser with proxy/isolation features; not a data source.
url: http://www.centbrowser.com
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A Chromium-based browser with per-session proxy and privacy controls for keeping investigator personas separate.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free to download and use; closed-source freeware built on Chromium.
opsec: passive
opsecNote: A browser is only as anonymous as how you run it. Cent Browser adds proxy/privacy controls but is CLOSED-SOURCE freeware based on an older Chromium — it may lag on security patches and its telemetry can't be audited. For real anonymity, run it through Tor/a trusted VPN and keep each persona in its own profile; for high-risk work prefer Tor Browser or a hardened open-source build.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: unverified
trustNote: Popular closed-source Chromium fork; convenient for compartmentalisation, but unaudited and historically slow to track upstream Chromium security releases.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- tor-browser
- mullvad-browser
- firefox-multi-account-containers
aliases:
- CentBrowser
- centbrowser.com
tags:
- browsers
- sock-puppet
- opsec
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Cent Browser

> A feature-rich Chromium fork some investigators use for compartmentalised, proxy-per-session sock-puppet browsing — handy for separation, but closed-source and not a substitute for a hardened anonymity browser.

## When to use
You want to keep research personas apart — separate profiles, per-session proxies, tab isolation, fine-grained privacy toggles — without wiring up a full separate machine. Cent Browser adds conveniences (proxy switching, mouse-gesture/tab management, disk-cache controls) on top of Chromium that make running multiple sock-puppet sessions less error-prone. It's tooling for *how* you browse, not a data source.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download Cent Browser from http://www.centbrowser.com and install it on an investigation machine/VM.
2. Create a **separate profile per persona** so cookies, logins, and history never cross-contaminate.
3. Configure a proxy (ideally a trusted VPN/Tor upstream) per profile/session; verify your exit IP and test for WebRTC/DNS leaks before browsing.
4. Use one profile per sock puppet consistently, and never log a persona in from a leaky/default session.
5. Pivot: for higher-risk targets, step up to `[[tor-browser]]` or `[[mullvad-browser]]`; use `[[firefox-multi-account-containers]]` if you prefer an audited open-source stack.

## Inputs → Outputs
- **In:** — (browsing infrastructure, not a selector)
- **Out:** compartmentalised browsing sessions/personas (no data selectors)
- **Empty/negative result looks like:** n/a — it's a browser; failure looks like an IP/WebRTC leak on a check, meaning your setup, not a query, is broken.

## Gotchas & OpSec
- Closed-source freeware on an often-older Chromium base: it can trail upstream security patches and its telemetry is unauditable — a real consideration for sensitive work.
- The browser doesn't anonymise you by itself; anonymity comes from the proxy/Tor/VPN you route it through plus strict profile discipline.
- One slip (wrong profile, default session, leaked WebRTC) can burn a persona — verify isolation every session.

## Overlaps ("do both")
- Contrast with `[[tor-browser]]` and `[[mullvad-browser]]` (audited, anonymity-first) and `[[firefox-multi-account-containers]]` (open-source compartmentalisation) — Cent Browser trades auditability for convenience; prefer the hardened options when stakes are high.

## Trust & verifiability
`trust: unverified` — a widely-used but closed-source Chromium fork; fine as a compartmentalisation convenience, but its code and telemetry can't be independently verified, so don't rely on it alone for anonymity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | centbrowser |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |

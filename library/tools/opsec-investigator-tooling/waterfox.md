---
id: waterfox
name: Waterfox
description: Use when you want a hardened, low-telemetry Firefox-based browser for investigative sessions — returns a privacy-focused browsing environment, not target data.
url: https://www.waterfox.net/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A daily-driver investigative browser with built-in blocking, encrypted DNS, and no telemetry.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source; desktop and Android. www.waterfox.net redirects to waterfox.com.
opsec: passive
opsecNote: This is defensive tooling for YOUR side, not something you point at a target. It reduces telemetry/tracking leakage during investigative browsing, but it is not anonymity — for that you still need Tor and a sock-puppet identity. Use per-site container tabs to keep sock-puppet logins isolated.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Long-running open-source Firefox fork; independently developed and reasonably reputable, though a small project relative to upstream Firefox.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- tor-browser
aliases:
- Waterfox
- waterfox.com
tags:
- browsers
- opsec
- privacy
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Waterfox

> A privacy-hardened, open-source Firefox fork — a low-telemetry browser to run your investigative sessions in, with built-in blocking and container tabs.

## When to use
This is **investigator hygiene**, not a lookup tool. Reach for Waterfox when you want a browser that reduces your own footprint during OSINT work: no telemetry, encrypted DNS by default, a built-in Rust ad/tracker-blocking engine, and private container tabs to keep multiple sock-puppet logins from cross-contaminating. It takes no subject selector and returns no target data — it's the environment other tools run inside.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download from https://www.waterfox.net/ (redirects to waterfox.com) for desktop, or the Play Store for Android.
2. Install and confirm telemetry is off and encrypted/oblivious DNS is enabled (defaults).
3. Create a separate **container tab** per sock-puppet identity so cookies/logins stay isolated.
4. Add uBlock Origin / your investigative extensions; browse as normal.
5. For anything requiring anonymity (not just privacy), switch to `[[tor-browser]]` — Waterfox still exposes your real IP.

## Inputs → Outputs
- **In:** none (it's a browser, not a query tool)
- **Out:** none (a hardened browsing environment)
- **Empty/negative result looks like:** N/A — success is simply a working, low-leakage browser; there is no query result to interpret.

## Gotchas & OpSec
- **Privacy ≠ anonymity:** Waterfox hides you from trackers/telemetry, not from a site logging your IP. Pair with a VPN/Tor when the target must not see your origin.
- As a smaller fork it can lag upstream Firefox on security patches — keep it updated.
- OpSec: **passive/defensive** — it's your tooling; using container tabs per persona is the key discipline.

## Overlaps ("do both")
- Pairs with `[[tor-browser]]` — Waterfox is your hardened *day-to-day* investigative browser; Tor Browser is what you switch to when a session needs network anonymity, not just anti-tracking.

## Trust & verifiability
`trust: community` — a reputable, long-lived open-source project, but small; verify downloads from the official domain and keep it patched rather than assuming parity with mainline Firefox.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | waterfox |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |

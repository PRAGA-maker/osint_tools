---
id: librewolf
name: LibreWolf
description: Use when you need a privacy-hardened, anti-fingerprinting browser for OSINT collection — a Firefox fork with telemetry stripped and tracking resistance built in.
url: https://librewolf.net
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A ready-hardened, no-telemetry Firefox fork for conducting OSINT with a smaller fingerprint.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (community-driven, source on Codeberg). No account.
opsec: passive
opsecNote: This is OpSec infrastructure — it reduces (does not eliminate) tracking/fingerprinting and removes telemetry, helping keep your collection non-attributable. It is not anonymity: pair with a VPN/Tor and sock-puppet accounts; RFP can also make you stand out on some sites.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Reputable, actively-maintained open-source Firefox fork built from the latest stable Firefox with privacy defaults; source is public and auditable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- LibreWolf browser
tags:
- opsec-investigator-tooling
- browser
- privacy
- anti-fingerprinting
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# LibreWolf

> A privacy-hardened Firefox fork — telemetry removed, tracking and fingerprinting resistance on by default, uBlock Origin bundled. The browser you run OSINT from, not a data source.

## When to use
You want a clean collection browser that leaks less about you than a stock browser: no telemetry, resistance to fingerprinting, private search defaults, and content blocking out of the box. Use it as the front end for OSINT work — especially alongside a VPN/Tor and separate sock-puppet profiles — to keep your investigation attribution low.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download LibreWolf for your OS from https://librewolf.net (verify the download).
2. Use separate profiles per persona/case; keep the privacy defaults (Resist Fingerprinting, no telemetry) unless a site breaks.
3. Route traffic through a VPN or Tor for network-level separation, and log into sock-puppet accounts, never personal ones.
4. Pivot: it's the environment for every web-manual tool in this library — the tools do the finding; LibreWolf keeps your side quiet.

## Inputs → Outputs
- **In:** none (it's a browser, not a lookup)
- **Out:** none as a selector — it's collection infrastructure
- **Empty/negative result looks like:** n/a — success is simply a browsing session with reduced tracking/telemetry.

## Gotchas & OpSec
- Hardening ≠ anonymity — LibreWolf reduces fingerprinting but doesn't hide your IP; you still need a VPN/Tor.
- Resist Fingerprinting and strict blocking can break some sites (letterboxing, timezone spoofing) and can itself be a distinguishing signal; keep per-case profiles.
- Not for logging into your real accounts — use dedicated personas.

## Overlaps ("do both")
- Pairs with VPN/Tor and container/multi-account extensions — LibreWolf hardens the browser layer; those handle network anonymity and identity separation.

## Trust & verifiability
`trust: trusted` — an actively-maintained, open-source, auditable Firefox fork with a good privacy reputation; verify installers from the official site.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | librewolf |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |

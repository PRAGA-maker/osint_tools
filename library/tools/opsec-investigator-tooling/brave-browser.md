---
id: brave-browser
name: Brave Browser
description: Use when you need a privacy-hardened browser for sock-puppet OSINT work — returns no selectors itself; it is the anonymised viewing surface for every web-manual tool.
url: https://brave.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A privacy-respecting Chromium browser (with Tor windows and fingerprint defence) for anonymous investigation sessions.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source; a paid Brave VPN/Firewall add-on exists but nothing in the browser's investigative use requires it.
opsec: passive
opsecNote: This is your OpSec layer, not a query tool — it leaks nothing to targets by itself. Use a dedicated puppet profile (or a private/Tor window) per case so cookies, logins and history never cross-contaminate identities. Brave's Tor windows route through Tor but are NOT a full Tails-grade anonymity guarantee; for high-risk work prefer a purpose-built VM.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Well-known open-source Chromium fork maintained by Brave Software; shipped and pre-configured (with the Forensic OSINT capture extension) in the Trace Labs OSINT VM.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- brave
aliases:
- Brave
- brave.com
tags:
- browser
- privacy
- chromium
- opsec
source: tracelabs-repos
lastVerified: '2026-07-22'
enrichment: full
---

# Brave Browser

> A privacy-hardened Chromium browser used as the anonymised viewing surface for web-manual OSINT — the thing you look at targets *through*, not a thing you query.

## When to use
Any time you will open a target's page, run a web-manual lookup, or log into a sock-puppet account and do not want the session to leak a real identity or fingerprint. It is the default browser in the Trace Labs VM; reach for it (or an equivalent hardened browser) before touching any live target infrastructure.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install from https://brave.com/ (or use the copy pre-installed in the Trace Labs VM, which force-installs the Forensic OSINT capture extension).
2. Create a **separate browser profile per investigation / per puppet identity** so cookies, logins and history never bleed between cases.
3. For a throwaway look, open a **Private window**; for network-level separation open a **New private window with Tor** — this routes that window through the Tor network and gives you a non-attributable exit IP.
4. Keep Shields **up** (the default) to block third-party trackers and reduce fingerprinting while browsing target sites.
5. Use it as the surface for every other web-manual tool in this library; capture evidence with the Forensic OSINT extension or your own screenshot workflow.

## Inputs → Outputs
- **In:** nothing — this is infrastructure, not a selector lookup.
- **Out:** nothing directly; it is the clean, low-attribution window through which other tools return their selectors.
- **Empty/negative result looks like:** N/A — success is simply a session that does not carry your real identity.

## Gotchas & OpSec
- Tor windows anonymise the network path, but a logged-in puppet account still identifies *that account* — never mix a real login into a Tor window.
- Brave's built-in Tor is convenient but weaker than Tails/Whonix; for high-risk targets escalate to a dedicated VM.
- Fingerprint randomisation reduces but does not eliminate correlation; keep puppet profiles consistent within a case and isolated between cases.

## Overlaps ("do both")
- Pairs with `[[brave]]` (Brave Search) — the same vendor's non-profiling search engine, a natural query tool to run *inside* this browser.

## Trust & verifiability
`trust: trusted` — open-source, widely audited Chromium fork from Brave Software; the download is first-party and it is the standard browser bundled in the Trace Labs OSINT VM.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | brave-browser |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |

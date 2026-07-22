---
id: tor-project
name: Tor Project
description: Use when you need to browse anonymously or reach `.onion` sites without exposing your IP — the free Tor Browser and anonymity network.
url: https://www.torproject.org
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Investigator OpSec — anonymising your browsing origin and accessing dark-web (.onion) resources during research.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source; run by a non-profit, funded by donations/grants.
opsec: passive
opsecNote: This is your-side anonymity tooling: it hides your IP/origin from the sites you visit by relaying traffic through three encrypted hops. It protects you, but is not magic — don't log into attributable accounts over it, beware exit-node snooping on non-HTTPS, and follow your org's rules on dark-web access.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Developed by the Tor Project, a well-established privacy non-profit; open-source and heavily audited. The network's anonymity properties are well-studied (and have known limits).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Tor Browser
- torproject.org
- Tor
tags:
- anonymity
- opsec
- dark-web
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# Tor Project

> The free Tor Browser and anonymity network — relays your traffic through three encrypted hops so the sites you visit don't see your real IP, and lets you reach `.onion` services.

## When to use
You need to separate your investigative browsing from your real identity/network, or you need to reach dark-web (`.onion`) resources as part of research. Tor is infrastructure/OpSec tooling: it doesn't find anything itself, it changes *how* you connect so your origin isn't exposed to the target site.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download Tor Browser from https://www.torproject.org (verify the signature) and install it.
2. Launch it and connect to the Tor network (use a bridge if Tor is blocked on your network).
3. Browse normally — your traffic exits via a Tor relay, hiding your IP from the destination; use `.onion` addresses to reach hidden services.
4. Keep OpSec discipline: no attributable logins, keep the security level high, don't resize/altered the window (fingerprinting), and prefer HTTPS.
5. Pair with a sock-puppet workflow and, for dark-web work, your organisation's legal/ethical clearance.

## Inputs → Outputs
- **In:** none (it's a browsing tool)
- **Out:** none (it produces no data; it anonymises your access)
- **Empty/negative result looks like:** not applicable — the "failure" mode is a connectivity block (censored network), solved with bridges.

## Gotchas & OpSec
- Not a cloak of invincibility: logging into a real account, browser fingerprinting, or malicious exit nodes on unencrypted traffic can deanonymise you.
- Dark-web access can carry legal/ethical constraints — clear it with your engagement first.
- Slower than normal browsing by design.

## Overlaps ("do both")
- Pairs with a reputable VPN (defence-in-depth), sock-puppet browser profiles, and browser-fingerprint checkers to validate your setup before use.

## Trust & verifiability
`trust: trusted` — a mature, audited open-source project from a respected non-profit; its anonymity guarantees are real but bounded, so follow best practice.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tor-project |

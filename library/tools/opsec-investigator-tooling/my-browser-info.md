---
id: my-browser-info
name: My Browser Info
description: Use when you want to check what your own browser leaks before touching a target — returns your `ip-address`, user-agent and basic fingerprint as a target would see it.
url: http://mybrowserinfo.com
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A quick self-check of the IP, user-agent and browser/OS details your current session is exposing, to validate a sock-puppet or proxy setup.
selectorsIn: []
selectorsOut:
- ip-address
status: live
pricing: free
costNote: Free; no account or registration.
opsec: passive
opsecNote: This is a self-directed check — you look at your own connection, not a target's. Run it to confirm your VPN/proxy is masking your real IP and that your user-agent looks plausible before doing any active work against a subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A simple long-standing "what am I leaking" page (Speednet Group); it reports your own request headers, which are self-evidently correct.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- mybrowserinfo.com
tags:
- opsec
- fingerprint
- browser-info
source: opsec
lastVerified: '2026-07-22'
enrichment: full
---

# My Browser Info

> A one-glance "what is my browser leaking" page — your public IP, user-agent and OS/browser as any site you visit would see them.

## When to use
Before you point a sock-puppet browser or proxied session at a subject, you want to confirm what that session exposes: is your real `ip-address` hidden behind the VPN/proxy? Does the user-agent match the persona (not, say, a corporate build that could deanonymise you)? My Browser Info shows the basics instantly so you can catch a leaking setup before it burns you.

## How to use it (`bestInteractionPattern`: web-manual)
1. In the exact browser profile / proxied session you plan to use, open http://mybrowserinfo.com.
2. Read the displayed IP address and country — confirm it is the proxy/VPN exit, not your real location.
3. Check the user-agent string and derived browser/OS details for anything that contradicts your cover.
4. Follow the "detailed information" link for a fuller breakdown if needed.
5. If anything reveals your real identity/location, fix the setup and re-check before proceeding.

## Inputs → Outputs
- **In:** none (it reads your own session)
- **Out:** your public `ip-address`, geolocation guess, user-agent, and browser/OS details
- **Empty/negative result looks like:** it shows your *real* IP/location when you expected the proxy's — that is a failure of your setup, and the signal to stop and fix it.

## Gotchas & OpSec
- It reports only basic headers/IP, not advanced fingerprinting (canvas, WebRTC leaks, fonts) — for a thorough check use a dedicated fingerprint/WebRTC-leak tester as well.
- This is about protecting *you*; it tells you nothing about a target.

## Overlaps ("do both")
- Pairs with `[[free-proxy-list]]` (verify the proxy you picked actually masks you) and with fuller browser-fingerprint/WebRTC-leak testers for a complete pre-operation OpSec check.

## Trust & verifiability
`trust: community` — a simple utility echoing your own request data back to you; there is no third-party dataset to distrust, though it only covers the basics.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | my-browser-info |

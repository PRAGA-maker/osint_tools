---
id: what-every-browser-knows-about-you
name: What Every Browser Knows About You (Webkay)
description: Use when you want to check what your own investigative browser leaks — returns the IP, coarse location, fingerprint, device and social-login signals any site can read.
url: https://webkay.robinlinus.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Self-auditing your investigator/sock-puppet browser to see what a visited site would learn about you.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open (by Robin Linus); no account required.
opsec: passive
opsecNote: This tests YOUR OWN browser, not a target — run it in the exact browser/VPN/container setup you use for an operation to confirm it isn't leaking your real IP, location, or that you're logged into personal accounts before you touch a target site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known open-source privacy-demonstration site; it reads only what any site can already read from your browser and doesn't retain it, so it's a safe self-check — its location/network guesses are approximate.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Webkay
- webkay.robinlinus.com
tags:
- Domain/IP/Links
- browser-fingerprint
- opsec-selfcheck
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# What Every Browser Knows About You (Webkay)

> A live demonstration of everything your browser silently exposes to any site — IP, approximate location, fingerprint, device, network and social-login state — used as an OpSec self-check before you visit a target.

## When to use
Before an operation, you need to confirm your investigative or sock-puppet browser isn't betraying you. Webkay shows exactly what a visited website can read without asking: your `ip-address` and Google-geolocation-estimated position, OS/browser/plugins fingerprint, hardware and network details, whether you're logged into Google/Facebook, even EXIF from a photo you drop in. Running it in your actual op setup catches leaks (real IP, personal logins, revealing fingerprint) before a target ever sees them.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://webkay.robinlinus.com in the *exact* browser profile, VPN and container you plan to use for the target.
2. Read each panel: does the location/IP match your intended cover (VPN exit), or your real one? Are you unexpectedly logged into personal accounts? Is the fingerprint distinctive?
3. Fix any leak — switch VPN, use a clean profile/container (`[[kasm]]`), log out of personal services, add anti-fingerprint measures — then re-run until it's clean.
4. Pivot: once verified clean, proceed to the target using that hardened setup.

## Inputs → Outputs
- **In:** none (it reads your current browser)
- **Out:** your exposed `ip-address`, coarse `geolocation`, fingerprint, device/network info, social-login detection
- **Empty/negative result looks like:** N/A — it always reports; the "bad" result is seeing your *real* IP/location or personal logins, meaning your op setup is leaking.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive and self-directed — it only surfaces what any site already can and doesn't store it; the value is doing this *before* touching a target, not after.
- Accuracy: location is an estimate (can be off by tens of km), but IP and login-state signals are exact and are the ones that matter for attribution.

## Overlaps ("do both")
- Pairs with `[[kasm]]` and VPN/Tor because those *create* the isolated, anonymised setup while Webkay *verifies* it isn't leaking before you rely on it.

## Trust & verifiability
`trust: community` — a reputable open-source demo; you can read its source, it reflects genuine browser exposure, and every value shown is one you can act on to harden your setup.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->

---
id: mullvad-browser
name: Mullvad Browser
description: Use when you need a hardened, anti-fingerprinting browser for investigative work without Tor — a privacy browser that makes your OSINT sessions blend into the crowd.
url: https://mullvad.net/en/browser
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Conducting attributable-risk OSINT from a hardened, fingerprint-resistant browser (paired with a VPN) instead of Tor.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: The browser is free and open source; the optional Mullvad VPN it pairs with is paid, but the browser works with any VPN or none.
opsec: passive
opsecNote: This is investigator opsec, not a target query. Mullvad Browser minimises your browser fingerprint so sock-puppet sessions look generic; run it behind a VPN, keep separate profiles per persona, and never log into your real accounts in it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Built by the Tor Project in collaboration with Mullvad VPN; open source and based on the hardened Tor Browser engine minus the Tor network.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Mullvad Browser
tags:
- browsers
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# Mullvad Browser

> The Tor Browser's anti-fingerprinting hardening without the Tor network — a privacy browser for running OSINT from behind a VPN while looking like everyone else.

## When to use
You're collecting on a subject and don't want your browser's fingerprint (fonts, canvas, screen, headers) to make you uniquely trackable across the sites you visit, but Tor's exit nodes are blocked or too slow for the target sites. Mullvad Browser gives you Tor-Browser-grade fingerprint resistance while you route traffic through an ordinary VPN, so your investigative sessions blend into a large anonymity set.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download Mullvad Browser for Windows/macOS/Linux from https://mullvad.net/en/browser (verify the signature).
2. Connect a VPN first (Mullvad or any provider), then launch the browser.
3. Keep default privacy settings — resist the urge to resize the window or install fingerprintable extensions, which defeats the crowd-blending.
4. Use one browser profile/persona per investigation; never sign into personal accounts.
5. Pair with disposable sock-puppet accounts for any site that requires login.

## Inputs → Outputs
- **In:** n/a — this is your collection environment, not a lookup taking a selector
- **Out:** a hardened, fingerprint-resistant browsing session
- **Empty/negative result looks like:** not applicable; success is that target sites can't fingerprint you distinctly and your VPN IP is what they log.

## Gotchas & OpSec
- It does not provide anonymity by itself — without a VPN, your real IP is exposed; the browser only handles fingerprinting.
- Customising the window size, adding extensions, or maximising can re-introduce a unique fingerprint — keep it stock.
- Logging into a personal account inside it links the persona to you instantly.

## Overlaps ("do both")
- Complements VPNs, containerised browser profiles, and Tor Browser — use Tor Browser when you need network anonymity, Mullvad Browser when you need fingerprint resistance over a normal (faster, less-blocked) VPN path.

## Trust & verifiability
`trust: trusted` — a joint Tor Project / Mullvad open-source project built on the audited Tor Browser codebase; its behaviour is inspectable and widely vetted.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mullvad-browser |

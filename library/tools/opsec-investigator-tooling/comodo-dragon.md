---
id: comodo-dragon
name: Comodo Dragon
description: Use when you want a hardened, separate Chromium-based browser as a sandboxed sock-puppet environment for investigation browsing — provides an isolated browser profile with privacy/DNS features (not an investigative lookup).
url: https://www.comodo.com/home/browsers-toolbars/browser.php
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A dedicated Chromium-based browser kept separate from your daily browser for sock-puppet/OSINT sessions.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: The browser is a free download (Windows); Comodo upsells a paid antivirus bundle ($29.99/yr) that is not required to use Dragon.
opsec: passive
opsecNote: Value is compartmentalization — running investigation sessions in a browser fully separate from your personal one so cookies/history don't cross-contaminate. It is closed-source and vendor-controlled with its own "Secure DNS", so do NOT assume it hides you: pair it with a VPN/Tor and treat Comodo's telemetry as untrusted. A hardened Firefox or a throwaway VM often serves the same purpose with more transparency.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: unverified
trustNote: Proprietary Chromium fork from Comodo; the browser is real and downloadable, but it is closed-source with bundled-AV upsell and unaudited telemetry, so its privacy claims can't be independently confirmed.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Comodo Dragon
- Dragon browser
tags:
- browser
- opsec
- chromium
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Comodo Dragon

> A proprietary Chromium-based browser marketed for privacy — useful mainly as a *separate* browser profile for compartmentalized investigation browsing.

## When to use
You want investigation/sock-puppet browsing to live in a browser that is completely separate from your everyday one, so sessions, cookies, autofill and history never bleed between your real identity and your OSINT persona. Comodo Dragon is one such standalone Chromium fork. This is an OpSec/environment choice, not a tool that finds or enriches anything about a subject.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download Comodo Dragon (Windows, 32/64-bit) from https://www.comodo.com/home/browsers-toolbars/browser.php.
2. Install it — decline the bundled antivirus upsell; it is not needed to run the browser.
3. Use this browser *only* for investigation personas; keep your personal browsing in a different application.
4. Layer real network anonymity underneath it: a VPN or Tor, since the browser alone does not hide your IP.
5. Clear the profile or use fresh profiles between unrelated cases to keep personas separated.

## Inputs → Outputs
- **In:** none (a browsing environment)
- **Out:** none (no selector output; it's where you *run* other lookups)
- **Empty/negative result looks like:** n/a — success is simply a clean, isolated browser session for your persona.

## Gotchas & OpSec
- **Closed-source + vendor telemetry:** you can't audit what it phones home; don't trust its "privacy" branding at face value.
- Its "Secure DNS" is Comodo's own resolver — Comodo sees your DNS. Use your own trusted resolver/VPN.
- A hardened Firefox profile or a disposable VM gives similar compartmentalization with more transparency — prefer those if you need assurance.

## Overlaps ("do both")
- Pairs with VPN/Tor and MAC-spoofing (`[[macchanger]]`) — Dragon isolates the browser layer while those cover network and link layers; compartmentalization only works when all layers are separated.

## Trust & verifiability
`trust: unverified` — a real, downloadable proprietary browser, but closed-source with unaudited telemetry and an AV upsell; its privacy assurances cannot be independently verified.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | comodo-dragon |

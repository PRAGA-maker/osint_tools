---
id: script-safe
name: Script Safe
description: Use when you want to harden the investigator's browser against scripts and fingerprinting while visiting hostile pages — provides granular script/element blocking and anti-fingerprinting.
url: https://chrome.google.com/webstore/detail/scriptsafe/oiigbmnaadbkfbmpbfijlflahbdbdgdf?hl=en
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A NoScript-style browser extension that blocks scripts/iframes and spoofs fingerprinting signals to protect the investigator when opening untrusted sites.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free Chrome/Chromium extension (donation-supported). No account. Note it was last updated in 2017 — stable but no longer actively developed.
opsec: passive
opsecNote: Protects YOUR side — blocks scripts, WebRTC leaks, canvas/audio/WebGL fingerprinting, and spoofs referrer/user-agent/timezone when you visit a hostile page. It does not anonymise your IP (pair with VPN/Tor) and, being unmaintained since 2017, may miss newer fingerprinting vectors.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A long-standing, popular privacy extension (tens of thousands of users); reputable but unmaintained since 2017 — treat as one layer, not complete protection.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- ScriptSafe
tags:
- privacy-and-encryption-tools
- browsing-hardening
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# Script Safe

> A NoScript-style browser extension that blocks scripts and anti-fingerprints — investigator-side browsing hardening when opening untrusted or hostile pages.

## When to use
You are about to open a page you do not trust (a suspect's site, a phishing lure, a tracker-heavy forum) and want to reduce what it can execute and learn about your browser. It hardens the investigator's session; it does not look up or return anything about a subject.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install ScriptSafe from the Chrome Web Store on a dedicated investigation browser profile.
2. Enable script/iframe/object blocking and the anti-fingerprinting options (canvas, audio, WebGL, WebRTC, referrer/UA/timezone spoofing).
3. Visit the untrusted page; whitelist only the specific elements you must load to see the content.
4. Pair with a VPN/Tor for IP anonymity — this extension does not hide your address.

## Inputs → Outputs
- **In:** none (a browsing-protection setting, not a selector)
- **Out:** a hardened browser session with scripts/fingerprinting suppressed
- **Empty/negative result looks like:** a page that breaks with everything blocked — selectively whitelist the minimum needed, or view it in a disposable VM instead.

## Gotchas & OpSec
- Human-in-the-loop: none, but aggressive blocking breaks many sites — expect to whitelist.
- OpSec: it protects the browser, **not your IP**; combine with VPN/Tor and a sock-puppet profile.
- Unmaintained since 2017 — reliable for classic vectors but may not cover the newest fingerprinting techniques.

## Overlaps ("do both")
- Overlaps with uBlock Origin / NoScript and a disposable-VM approach: use ScriptSafe (or an equivalent) for element/fingerprint control, and a VM + VPN for full isolation against genuinely hostile sites.

## Trust & verifiability
`trust: community` — a popular, long-standing privacy extension; a useful hardening layer, but unmaintained, so do not treat it as complete protection.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | script-safe |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |

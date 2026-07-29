---
id: sleipnir
name: Sleipnir
description: Use when you want an alternative Chromium-based browser on Windows/macOS for OSINT browsing — a tab-focused browser from Fenrir, useful as a compartmentalized profile.
url: http://www.fenrir-inc.com/jp/sleipnir
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A separate, non-default browser to keep investigative browsing compartmentalized from your everyday browser.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free to download and use. Windows 10/11 and macOS 10.13+ (note the macOS build is currently paused for the latest macOS version).
opsec: active
opsecNote: Like any browser, Sleipnir exposes your IP/User-Agent/fingerprint to every site you visit. Its value for OSINT is compartmentalization — use it as a dedicated investigation browser separate from your personal one, paired with a VPN/sock-puppet setup. It's built on Chromium (Blink) and can run Chrome extensions on Windows, but it's a smaller vendor product, so don't assume the privacy-hardening of a purpose-built OpSec browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Developed by Fenrir Inc. (Japan); an established, still-maintained consumer browser (Sleipnir 6) on the Chromium/Blink engine. Legitimate but niche and vendor-specific.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Sleipnir browser
- Fenrir Sleipnir
tags:
- browsers
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Sleipnir

> A Chromium-based desktop browser from Fenrir (Japan). Browser infrastructure, not an investigative tool — its OSINT use is as a separate, compartmentalized browsing profile.

## When to use
When you want a second browser dedicated to investigations, kept apart from your everyday one so cookies, logins, and history don't cross-contaminate. Sleipnir emphasizes tab management (thumbnail tabs, gestures) and runs on the Blink engine, so it renders modern sites and — on Windows — supports Chrome extensions. Choose it if you specifically want a non-mainstream browser for compartmentalization; it offers no investigative data by itself.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download Sleipnir 6 from Fenrir (fenrir-inc.com) for Windows or macOS (check macOS-version compatibility — the macOS build has been paused for the newest macOS).
2. Set it up as your **investigation-only** browser: no personal accounts, distinct from your daily driver.
3. Pair with a VPN/sock-puppet identity and, on Windows, add any Chrome OSINT extensions you rely on.
4. Browse targets from this profile so activity stays isolated from your personal browsing.
5. Treat it as compartmentalization, not anonymity — for strong anonymity use a purpose-built hardened setup.

## Inputs → Outputs
- **In:** none (a browser, not a selector lookup)
- **Out:** renders whatever you point it at — no direct subject `selectorsOut`
- **Empty/negative result looks like:** N/A — it's browsing infrastructure; the risk is identity leakage, not a failed query.

## Gotchas & OpSec
- **Active exposure:** every visit reveals your IP/fingerprint; compartmentalize and use a VPN/sock-puppet.
- A niche vendor browser — don't assume the anti-fingerprinting or privacy defaults of a dedicated OpSec browser; harden it yourself.
- macOS support currently lags the newest macOS version — check before relying on it there.

## Overlaps ("do both")
- Overlaps with `[[safari-for-macos]]` and other browsers as an OSINT browsing surface; complements dedicated OpSec browser-profile/VPN tooling that provides the actual anonymity layer.

## Trust & verifiability
`trust: community` — a legitimate, maintained product from an established vendor, but niche; it's a fine compartmentalized browser, not a vetted anonymity tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sleipnir |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | no |

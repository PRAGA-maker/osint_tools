---
id: maxthon
name: Maxthon
description: Use when you want an alternative Chromium browser with built-in VPN, ad-blocking, and media/screenshot capture for investigative browsing — returns a browsing environment, not target data.
url: https://www.maxthon.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A Chromium-based investigative browser with built-in VPN, ad-block, split-screen, and page/video capture.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free to download and use (built-in VPN via Bright Data, ad-block, incognito); a paid membership adds extras but isn't required.
opsec: passive
opsecNote: Defensive tooling for your side, not a target lookup. The built-in "free VPN" is third-party (Bright Data) — treat it as light IP obfuscation, not trustworthy anonymity, and don't route sensitive work through it. Maxthon historically syncs data to its cloud; disable cloud sync and don't store investigative accounts in it. For real anonymity use Tor.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: unverified
trustNote: A long-running commercial Chromium browser; functional, but closed-source with a history of cloud data-sync and a bundled third-party VPN — vet before trusting it with sensitive sessions.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- waterfox
- tor-browser
aliases:
- Maxthon
- maxthon.com
tags:
- browsers
- opsec
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Maxthon

> A Chromium-based browser bundling a free VPN, ad-blocking, split-screen, and built-in media/screenshot capture — an alternative investigative browsing environment, with caveats about its cloud/VPN.

## When to use
Investigator tooling, not a lookup. Consider Maxthon when you want a self-contained browser with capture and light IP-obfuscation baked in: its built-in VPN, screenshot/video-download tools, split-screen (compare two sources), and reading mode can be convenient for OSINT triage on one machine. It takes no subject selector and returns no personal data — it's the environment, and a middling-trust one, so use it deliberately.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download from https://www.maxthon.com/ (Windows/macOS/Android/iOS) and install.
2. **Turn off cloud sync** and avoid signing into a Maxthon account with anything real — keep the browser local.
3. Use the built-in ad-block and incognito for routine browsing; use split-screen to compare two pages.
4. Treat the bundled VPN as light obfuscation only; for sessions that must hide origin, use Tor via `[[tor-browser]]` instead.
5. Use its capture tools to save evidence screenshots/video from a page.

## Inputs → Outputs
- **In:** none (a browser, not a query tool)
- **Out:** none (a browsing/capture environment)
- **Empty/negative result looks like:** N/A — success is a working browser; there is no query result.

## Gotchas & OpSec
- **Closed-source with cloud sync history** and a third-party bundled VPN — don't route sensitive work through it or trust it for anonymity. Disable sync; keep it local.
- Its VPN is Bright Data–backed obfuscation, not audited anonymity.
- OpSec: **passive/defensive**, but lower-trust than open-source alternatives — prefer a hardened browser for serious opsec.

## Overlaps ("do both")
- Compare with `[[waterfox]]` (open-source, privacy-hardened) and `[[tor-browser]]` (anonymity) — for most investigators an open-source hardened browser plus Tor is a safer stack than Maxthon; use Maxthon only for its capture/split-screen convenience, not for trust-critical sessions.

## Trust & verifiability
`trust: unverified` — a real, long-lived product, but closed-source with a data-sync/VPN profile that warrants caution; verify your privacy settings rather than assuming safe defaults.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | maxthon |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |

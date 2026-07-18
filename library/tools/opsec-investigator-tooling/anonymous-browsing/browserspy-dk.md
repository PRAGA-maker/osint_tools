---
id: browserspy-dk
name: BrowserSpy.dk
description: Use when you want to audit what a website can see about your investigative browser — returns your fingerprint (fonts, plugins, screen, ip-address) so you can harden your OpSec.
url: https://browserspy.dk/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
bestFor: Self-auditing the fingerprint/identifying data your browser leaks to sites, to check that a sock-puppet setup isn't uniquely trackable.
input: No input required (automatic browser detection)
output: Comprehensive browser property list including plugins, fonts, screen data, and capabilities
selectorsIn: []
selectorsOut:
- ip-address
- metadata-exif
status: degraded
pricing: free
costNote: Free; no account. Long-running hobby site by Henrik Gemal.
opsec: active
opsecNote: This profiles YOUR browser, not a target's. Run it in the exact sock-puppet browser/VPN profile you use for investigations to see what leaks — but the site is old and shows ads/possibly stale links, so run it in a disposable session, not your real identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Independent hobby site (gemal.dk); still referenced as a fingerprint tester but the interface is dated and content is not actively curated — treat as a rough self-check, not an authority.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- BrowserSpy
- gemal.dk browserspy
- browserspy.dk
tags:
- opsec
- browser-fingerprint
- anonymous-browsing
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# BrowserSpy.dk

> A veteran "what does your browser reveal about you" tester — run it in your investigative browser to see the fingerprint sites can build, then fix the leaks before you touch a target.

## When to use
Before doing attributable-sensitive work, you want to confirm your sock-puppet browser/VPN profile isn't leaking your real identity or standing out as uniquely fingerprintable. BrowserSpy enumerates dozens of properties — plugins, fonts, screen, language, `ip-address`, capabilities, headers — so you can spot mismatches (e.g. a VPN in one country but a system locale/timezone in another) that would blow your cover. This is OpSec self-checking, not target research.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://browserspy.dk/ **in the exact browser profile + VPN you use for investigations** (a disposable session, never your personal one).
2. Click through the individual tests in the list (IP, fonts, plugins, screen, language, headers, etc.) — results load per-test rather than all at once.
3. Review for leaks and inconsistencies: does the reported IP/country match your VPN? Do timezone, locale, and fonts tell a consistent story? Are unique plugins/fonts making you stand out?
4. Harden accordingly (spoof/normalize timezone and locale, reduce font/plugin uniqueness) and re-run, ideally cross-checking with a modern tool.

## Inputs → Outputs
- **In:** none (it inspects your own browser automatically)
- **Out:** `ip-address` (as seen by the site) and `metadata-exif`-style browser/environment metadata (fonts, plugins, screen, headers, capabilities)
- **Empty/negative result looks like:** tests that fail to load or report obsolete items (ActiveX, old plugins) — the site is dated, so a blank/legacy test is the tool's age, not a clean fingerprint.

## Gotchas & OpSec
- Human-in-the-loop: none, but you must click each test individually.
- OpSec: it profiles **you** — only ever run it in a disposable investigative profile. The site is old and ad-laden; don't trust it with anything and prefer a modern tool for the authoritative read.
- Staleness: many checks target legacy tech and won't reflect modern fingerprinting vectors (canvas, WebGL, audio) — cover those elsewhere.

## Overlaps ("do both")
- Pairs with modern fingerprint testers (EFF's Cover Your Tracks, BrowserLeaks/BrowserScan) — use those for canvas/WebGL/current vectors and BrowserSpy only as a quick supplementary enumeration.

## Trust & verifiability
`trust: unverified` — it is an independent, aging hobby site; the readings are indicative but should be confirmed against a current, maintained fingerprint tool before you rely on your OpSec.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | browserspy-dk |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | — → ip-address, metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |

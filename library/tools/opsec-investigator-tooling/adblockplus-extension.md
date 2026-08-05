---
id: adblockplus-extension
name: Adblock Plus
description: Use when you want your investigation browser to block ads and third-party trackers so target pages load cleaner and leak less about you — returns ad/tracker blocking (investigator OpSec).
url: https://adblockplus.org
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Blocking ads and tracking scripts in the investigator's browser for cleaner, lower-exposure browsing.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source; note its default "Acceptable Ads" program allows some ads unless you disable it in settings.
opsec: passive
opsecNote: Defensive, for the investigator. It blocks many trackers, reducing cross-site profiling as you browse targets — but it is an ad blocker, not an anonymizer, and its default Acceptable Ads allowlist lets some ads/trackers through. Turn Acceptable Ads off, and pair with a real anonymity tool for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A mature, widely used open-source blocker; effective for ads/trackers, though privacy purists prefer uBlock Origin and object to the Acceptable Ads default.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- ABP
- adblockplus.org
tags:
- toddington
- curated-directory
- proxy-servers-online-privacy-security-tools
- anti-tracking
- browser-extension
source: toddington-resources
lastVerified: '2026-08-05'
enrichment: full
---

# Adblock Plus

> A mainstream ad/tracker blocker for the investigator's browser: it strips ads and many tracking scripts so target pages render cleaner and profile you less — one hygiene layer, not an anonymity tool.

## When to use
While browsing targets, ad and tracker scripts both clutter pages and quietly build a cross-site profile of your session. Adblock Plus blocks much of that, giving cleaner captures and less passive exposure. It protects the investigator's footprint; it returns no subject data. Reach for it as basic browser hygiene, alongside — not instead of — real anonymity tooling.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install Adblock Plus from https://adblockplus.org (Chrome/Firefox/Edge) in your investigation browser profile.
2. **Turn off "Acceptable Ads"** in settings — by default it allowlists some ads/trackers.
3. Optionally add privacy/tracking filter lists (e.g. EasyPrivacy) for stronger tracker blocking.
4. Browse: ads and many trackers are blocked; disable per-site if a target page breaks.
5. Pivot: cleaner pages make [[fireshot]] captures clearer and reduce noise when reading a target.

## Inputs → Outputs
- **In:** nothing about a subject — it filters your own browsing
- **Out:** ad/tracker blocking in the browser
- **Empty/negative result looks like:** a target page that breaks or hides content because a blocked script was load-bearing — allowlist that site temporarily to see the full page.

## Gotchas & OpSec
- Human-in-the-loop: none beyond install/config.
- OpSec: passive and defensive. It reduces tracking but is **not anonymity** — your IP and browser fingerprint are unchanged. The default Acceptable Ads allowlist weakens it until you disable it.
- Occasionally breaks site functionality; know how to allowlist per-site.

## Overlaps ("do both")
- Pairs with [[electronic-frontier-foundation-eff-tools]] (Privacy Badger) and [[tor-browser]] — ABP handles ads/trackers, Privacy Badger learns trackers heuristically, Tor provides actual anonymity; layer them by how sensitive the target is. uBlock Origin is a stronger single alternative to ABP.

## Trust & verifiability
`trust: community` — a long-established, open-source blocker that reliably does its job. Note the Acceptable Ads business model (disable it); for maximal blocking, privacy communities favour uBlock Origin.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | adblockplus-extension |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |

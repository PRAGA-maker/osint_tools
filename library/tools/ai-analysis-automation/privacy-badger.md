---
id: privacy-badger
name: Privacy Badger
description: Use when you want to block trackers in your investigator browser to reduce your footprint — returns automatic tracker/cookie blocking (a defensive opsec tool).
url: https://www.eff.org/privacybadger
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Automatically blocking cross-site trackers in the browser you investigate with.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source, built by the EFF (non-profit); no account.
opsec: passive
opsecNote: Passive and defensive — it reduces the trackers/cookies that could fingerprint or correlate your browsing during investigations. It does not anonymise your IP; pair it with a VPN/Tor and a sock-puppet profile for real cover.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Developed and maintained by the Electronic Frontier Foundation (EFF); open-source and widely trusted.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- coveryourtracks-eff-org
- electronic-frontier-foundation-eff-tools
- https-everywhere
- panopticlick
- surveilliance-self-defense
aliases:
- EFF Privacy Badger
tags:
- privacy-and-encryption-tools
- tracker-blocker
- opsec
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Privacy Badger

> The EFF's tracker-blocking browser extension — it learns and blocks cross-site trackers automatically to shrink your investigative footprint.

## When to use
You want your working/sock-puppet browser to leak less: fewer cross-site trackers, cookies and fingerprinting scripts following you as you visit a subject's sites and social profiles. Privacy Badger is a defensive opsec add-on that runs in the background; it is not a data source and produces no OSINT selectors.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install Privacy Badger from the EFF page for your browser (Chrome, Firefox, Edge, Opera).
2. Browse normally — it learns which third-party domains track you across sites and starts blocking them automatically.
3. Use its toolbar panel to see/adjust what's blocked on a given site if something breaks.
4. Combine with IP-level cover (VPN/Tor) and a dedicated research profile — Badger blocks trackers, not your IP.
5. Pivot: it's an always-on opsec layer beneath whatever collection you're doing.

## Inputs → Outputs
- **In:** none (runs passively in the browser) — no OSINT selector
- **Out:** blocked trackers/cookies — reduced fingerprinting, not intelligence
- **Empty/negative result looks like:** N/A — it's protective, not a lookup; occasionally a site feature breaks and you allow a domain in its panel.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: defensive only — it does not hide your IP or identity; it complements, not replaces, a VPN/Tor + sock-puppet setup.
- It learns over time and per-profile, so a fresh install/profile starts with less blocking.

## Overlaps ("do both")
- Pairs with EFF's `[[coveryourtracks-eff-org]]` (test your fingerprint) and `[[https-everywhere]]`/`[[surveilliance-self-defense]]` — Badger blocks trackers, those measure/round out your browser hardening.

## Trust & verifiability
`trust: trusted` — built and maintained by the EFF, open-source and widely audited; a dependable defensive tool, though its protection is limited to tracker/cookie blocking.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | privacy-badger |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |

---
id: panopticlick
name: Panopticlick / Cover Your Tracks
description: Use when you want to test your investigative browser's fingerprint and tracker-blocking before an op — returns a uniqueness score and detailed fingerprint components.
url: https://panopticlick.eff.org/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- privacy-clean-up
bestFor: Testing how identifiable/unique your browser fingerprint is and whether your tracker-blocking is effective (EFF's Cover Your Tracks, formerly Panopticlick).
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free EFF tool. panopticlick.eff.org now redirects to coveryourtracks.eff.org.
opsec: active
opsecNote: This is a self-test of YOUR investigative browser, not a lookup on a target. Run it on your sock-puppet/Tor/VPN browser to see how trackable it is before you touch a target — a unique fingerprint can deanonymize you across sites. Test the exact browser profile you'll use for the op.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built and maintained by the Electronic Frontier Foundation; a canonical, reputable browser-fingerprinting research tool.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- coveryourtracks-eff-org
- privacy-badger
- surveilliance-self-defense
- electronic-frontier-foundation-eff-tools
- https-everywhere
aliases:
- Cover Your Tracks
- EFF Panopticlick
tags:
- opsec
- browser-fingerprint
- privacy
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
---

# Panopticlick / Cover Your Tracks

> EFF's browser-fingerprinting test — point your investigative browser at it to learn how uniquely identifiable you are and whether your tracker-blocking actually works, before you go operational.

## When to use
This is defensive OpSec tooling, not a subject lookup. Before running an investigation from a sock-puppet browser (especially over Tor/VPN), test that browser profile here: a highly unique fingerprint can link your "anonymous" sessions to each other and to your real identity across sites. Run it whenever you set up or change an investigative browser to confirm your anonymization holds.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the tool in the exact browser/profile you'll investigate from (it redirects to coveryourtracks.eff.org).
2. Start the test — it needs no input; it analyzes your browser automatically.
3. Read the results: your fingerprint's uniqueness (bits of identifying info), whether trackers/ads are blocked, and each fingerprint component (canvas, fonts, headers, etc.).
4. Harden accordingly: adjust the browser, add anti-fingerprinting measures (Tor Browser standardizes fingerprints), and re-test.
5. Pivot: a hardened, low-uniqueness browser is the safe platform from which to run every other tool in your workflow.

## Inputs → Outputs
- **In:** none (tests the browser you visit with)
- **Out:** a fingerprint-uniqueness score, tracker-blocking assessment, and component breakdown
- **Empty/negative result looks like:** N/A — it always returns a result about your browser; a "bad" outcome is a highly-unique fingerprint that means you're trackable and should harden before operating.

## Gotchas & OpSec
- It measures the browser you use to visit — test the real op profile, not your daily browser.
- A single test is a snapshot; extensions/updates change your fingerprint, so re-test after changes.
- Low uniqueness ≠ perfect anonymity — combine with VPN/Tor and disciplined persona separation.

## Overlaps ("do both")
- Pairs with `[[privacy-badger]]` and Tor Browser — this diagnoses your exposure; those reduce it (block trackers, standardize the fingerprint).

## Trust & verifiability
`trust: trusted` — a canonical EFF research tool; the fingerprint analysis is authoritative and widely cited in privacy research.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | panopticlick |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |

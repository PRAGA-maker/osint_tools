---
id: coveryourtracks-eff-org
name: coveryourtracks.eff.org
description: Use when you want to test how identifiable and fingerprintable your investigation browser is before doing OSINT — returns your browser's uniqueness, tracker exposure, and installed-font/fingerprint surface.
url: https://coveryourtracks.eff.org
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Auditing your own OPSEC browser for fingerprinting uniqueness and tracker/ad-network exposure.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free EFF project; no account required.
opsec: passive
opsecNote: Point it at your OWN investigation browser, never a target. It profiles the browser making the request; run it from your sock-puppet/VM to see exactly how unique that identity looks before you use it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Run by the Electronic Frontier Foundation (EFF); the successor to Panopticlick and a well-regarded reference on browser fingerprinting.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Cover Your Tracks
- Panopticlick successor
tags:
- Browser analyze
- opsec
- fingerprinting
source: cyb-detective
lastVerified: '2026-07-23'
relatedTools:
- electronic-frontier-foundation-eff-tools
- https-everywhere
- panopticlick
- privacy-badger
- surveilliance-self-defense
---

# coveryourtracks.eff.org

> EFF's browser-fingerprinting tester (formerly Panopticlick): shows how trackers see your browser and how unique — and therefore trackable — your OPSEC identity really is.

## When to use
Before running OSINT from a sock-puppet browser or VM, use this to check that identity's exposure: how unique its fingerprint is among all browsers tested, whether it blocks tracking ads/invisible trackers, and what surface (user-agent, screen, installed fonts, canvas/WebGL) leaks. It is a self-audit tool for the investigator, not something you run against a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. From the exact browser/VM you use for investigations, open https://coveryourtracks.eff.org.
2. Click "Test Your Browser" (choose the standard or "trackers actively blocking" mode).
3. Read the report: whether you block tracking ads/invisibles, whether you thwart fingerprinting, and your fingerprint's "bits of identifying information" / one-in-N uniqueness — plus the specific attributes (fonts, canvas hash, headers) that make you stand out.
4. Act: reduce standout attributes (disable exotic fonts/plugins, use a common resolution/user-agent, add anti-fingerprinting) and re-test until the identity blends in.

## Inputs → Outputs
- **In:** none about a subject — it profiles the requesting browser
- **Out:** fingerprint uniqueness score, tracker-blocking verdict, and the list of identifying attributes (including installed fonts)
- **Empty/negative result looks like:** "your browser has a unique fingerprint" — a warning that this identity is easily re-identified across sites; treat that as a reason to harden before proceeding.

## Gotchas & OpSec
- A "protected" verdict measures resistance to *this* test, not perfect anonymity — a unique fingerprint here means a real risk of cross-site correlation of your sock puppet.
- Results depend on browser, extensions, and window size at test time; re-test after any change to the OPSEC setup.
- OpSec: **passive** and self-directed — point it only at your own tooling.

## Overlaps ("do both")
- Pairs with `[[privacy-badger]]`, anti-fingerprinting browser configs, and `[[surveilliance-self-defense]]` — Cover Your Tracks diagnoses the exposure; those reduce it.

## Trust & verifiability
`trust: trusted` — an EFF-operated, widely cited fingerprinting reference; the methodology is transparent and open.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | coveryourtracks-eff-org |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: electronic-frontier-foundation-eff-tools
name: EFF Tools (Privacy Badger, Cover Your Tracks, SSD)
description: Use when you want to harden an investigator browser against tracking/fingerprinting and learn OpSec tradecraft — returns privacy tooling and self-defense guidance (investigator OpSec).
url: https://www.eff.org/pages/tools
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Hardening your investigation browser against trackers/fingerprinting and grounding your OpSec in EFF's guidance.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source, published by the non-profit Electronic Frontier Foundation.
opsec: passive
opsecNote: These protect the investigator, not a subject. Privacy Badger blocks trackers; Cover Your Tracks shows how identifiable/fingerprintable your browser is; Surveillance Self-Defense teaches threat-modelling. Note HTTPS Everywhere is retired (its function is now built into major browsers), so rely on the browser's HTTPS-only mode instead.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Published by the EFF, a respected digital-rights non-profit; open source and well-audited privacy tooling and guidance.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- coveryourtracks-eff-org
- privacy-badger
- panopticlick
- surveilliance-self-defense
aliases:
- EFF
- Electronic Frontier Foundation tools
tags:
- toddington
- curated-directory
- proxy-servers-online-privacy-security-tools
- privacy
- anti-tracking
source: toddington-resources
lastVerified: '2026-08-05'
enrichment: full
---

# EFF Tools (Privacy Badger, Cover Your Tracks, SSD)

> The EFF's suite of free privacy tools and guidance — a tracker-blocking extension, a browser-fingerprint tester, and a self-defense knowledge base — for keeping the investigator's own footprint small.

## When to use
Before and during sensitive investigation browsing, when you need your working browser to leak as little as possible and want your OpSec grounded in credible guidance. Use **Privacy Badger** to block trackers, **Cover Your Tracks** to measure how unique/fingerprintable your browser looks, and **Surveillance Self-Defense (SSD)** to threat-model a case. These protect you; they return no subject data.

## How to use it (`bestInteractionPattern`: browser-extension)
1. From https://www.eff.org/pages/tools, install **Privacy Badger** in your investigation browser profile — it learns and blocks trackers as you browse.
2. Run **Cover Your Tracks** (coveryourtracks.eff.org) to see how identifiable your browser fingerprint is; adjust your setup (e.g. use Tor Browser) if it stands out.
3. Read relevant **Surveillance Self-Defense** guides to threat-model the investigation and choose appropriate precautions.
4. Note: **HTTPS Everywhere is retired** — enable your browser's built-in HTTPS-only mode instead.
5. Pivot: a hardened, low-fingerprint browser is the safe carrier for every other web-manual OSINT lookup.

## Inputs → Outputs
- **In:** nothing about a subject — you configure/measure your own browser
- **Out:** tracker blocking, a fingerprint-uniqueness report, and OpSec guidance
- **Empty/negative result looks like:** Cover Your Tracks reporting your browser is highly unique — that is a finding to act on (harden further), not a failure.

## Gotchas & OpSec
- Human-in-the-loop: none beyond installing/configuring.
- OpSec: passive and defensive — for the investigator only. Privacy Badger can occasionally break site functionality; disable per-site if a target page won't load.
- Keep the toolset current: HTTPS Everywhere is deprecated, and fingerprinting defenses evolve — Tor Browser remains the strongest single anti-fingerprinting option.

## Overlaps ("do both")
- Pairs with [[tor-browser]] — EFF's tools harden a normal browser and teach the threat model, Tor gives the strongest anonymity/anti-fingerprinting; do both, matching the level to the target's sensitivity.

## Trust & verifiability
`trust: trusted` — published by the EFF, a long-standing digital-rights non-profit, with open-source, audited tools. Guidance is current and reputable; just note which specific tools (e.g. HTTPS Everywhere) have been retired.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | electronic-frontier-foundation-eff-tools |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |

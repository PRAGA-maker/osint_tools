---
id: epic-online-guide-to-practical-privacy-tools
name: EPIC Online Guide to Practical Privacy Tools
description: Use when you're hardening your own investigator OpSec and want a vetted checklist — returns categorized privacy tools; it protects the analyst, not a subject.
url: https://epic.org/privacy/tools.html
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A reputable, categorized reference of practical privacy tools for hardening your own operational security.
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
costNote: Free public guide from a non-profit; the tools it lists are mostly free/open-source with some freemium options.
opsec: passive
opsecNote: A defensive reference for the investigator. Reading it reveals nothing about a subject. Use it to choose the browser/proxy/comms hardening you apply before touching targets — the tools it points to are what actually change your exposure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by the Electronic Privacy Information Center (EPIC), a long-established privacy non-profit; guidance is credible, though a directory like this can lag as tools change.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-analytics-opt-out-extension-chrome
- adblockplus-extension
aliases:
- EPIC Practical Privacy Tools
- epic.org privacy tools
tags:
- privacy
- opsec-hygiene
- reference
source: toddington-resources
lastVerified: '2026-08-05'
enrichment: full
---

# EPIC Online Guide to Practical Privacy Tools

> The Electronic Privacy Information Center's categorized guide to privacy tools — a credible checklist for hardening your own browser, comms, and identity before you start investigating.

## When to use
Before (and while) working cases, you want your own OpSec sound: which tools to use for anonymous browsing, encrypted messaging, tracker blocking, email privacy, and secure storage. EPIC's guide organizes practical privacy tools by purpose from a trusted non-profit, giving you a defensible starting checklist rather than random blog recommendations. It's investigator hygiene reference — no subject selector in, no data out; it points you to the tools that reduce *your* footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://epic.org/privacy/tools.html (if the exact page has moved, search epic.org for its current privacy-tools guide — the resource persists even if the URL shifts).
2. Read by category (browsing/anonymity, messaging, email, tracking protection, etc.) and pick tools that fit your threat model.
3. Verify each recommended tool is still current and reputable before adopting it — any curated list ages.
4. Apply the chosen tools to your investigation profile (VPN/Tor, tracker blockers, encrypted comms) and pair with specific add-ons like `[[google-analytics-opt-out-extension-chrome]]`.

## Inputs → Outputs
- **In:** none (a privacy reference for the analyst)
- **Out:** a categorized set of privacy tools to harden your own OpSec
- **Empty/negative result looks like:** a listed tool that's outdated or discontinued — treat the guide as direction, not a guarantee, and confirm each tool's current status.

## Gotchas & OpSec
- It's a reference, not a live audit — some entries may lag behind the current tool landscape; verify before relying.
- The URL may have been reorganized on epic.org; the *resource* is what matters, so search the site if the deep link 404s.
- Reading it is passive; the protection only materializes once you actually deploy the tools.

## Overlaps ("do both")
- Turn the guidance into practice with concrete add-ons — `[[google-analytics-opt-out-extension-chrome]]` and a tracker blocker like `[[adblockplus-extension]]` — layered with a VPN/Tor and a clean sock-puppet profile.

## Trust & verifiability
`trust: trusted` — EPIC is a credible, long-standing privacy organization, so its recommendations are sound in principle; still confirm each specific tool is current, since directories age faster than the advice behind them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | epic-online-guide-to-practical-privacy-tools |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

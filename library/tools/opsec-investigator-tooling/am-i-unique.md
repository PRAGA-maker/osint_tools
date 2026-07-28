---
id: am-i-unique
name: Am I unique?
description: Use when you want to test how identifiable your investigation browser is — returns your browser `device-id` fingerprint and how rare it is among all visitors.
url: https://amiunique.org
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Checking whether your OSINT browser leaves a rare, trackable fingerprint before you use it on targets.
selectorsIn: []
selectorsOut:
- device-id
status: live
pricing: free
costNote: Free research service run by Université de Lille / Inria.
opsec: passive
opsecNote: Investigator-side OpSec. You test your *own* browser, not a target. The site records your fingerprint and sets a cookie (≈4 months) for its research dataset — run it in the same puppet browser/profile you intend to harden, and clear the cookie afterward if you don't want to contribute.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Academic project (Université de Lille, Inria/Spirals team); results and methodology are published in peer-reviewed fingerprinting research.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- AmIUnique
- amiunique.org
tags:
- anonymity
- browser-fingerprinting
- opsec
source: metaosint
lastVerified: '2026-07-28'
enrichment: full
---

# Am I unique?

> An academic browser-fingerprinting tester — shows how uniquely identifiable your current browser is, so you can harden it before touching targets.

## When to use
Before running an investigation from a "clean" browser or puppet profile, you want to know whether that browser stands out — a rare fingerprint (unusual fonts, screen size, canvas, plugins) makes you trackable across sites even without cookies. Am I unique? scores your fingerprint's rarity against its dataset.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://amiunique.org in the exact browser/profile you plan to investigate from.
2. Click "View my browser fingerprint."
3. Read the verdict: whether your fingerprint appears unique among visitors, plus a per-attribute breakdown (user-agent, screen, timezone, fonts, canvas, WebGL, plugins) showing which attributes make you stand out.
4. Harden the outliers (spoof user-agent, disable/normalise WebGL & canvas, standardise window size, cut exotic fonts) and re-test until you blend in.

## Inputs → Outputs
- **In:** none (it reads your own browser)
- **Out:** a browser fingerprint (`device-id`) and its uniqueness ratio + attribute-level entropy
- **Empty/negative result looks like:** "Yes, you are unique" is the *bad* outcome (you're trackable); a common, non-unique fingerprint is the goal.

## Gotchas & OpSec
- It fingerprints whatever browser opens it — test the puppet browser, not your daily driver.
- The site adds you to its research dataset and drops a ~4-month cookie; clear it if you don't want to persist.
- A "not unique" result is only relative to *their* visitor pool; real-world trackers use larger datasets, so treat it as directional.
- Fingerprint surface shifts with every browser update — re-test periodically.

## Overlaps ("do both")
- Pairs with EFF's Cover Your Tracks and anti-fingerprinting browser hardening — Am I unique? tells you which attributes leak; those tools/settings help you flatten them.

## Trust & verifiability
`trust: trusted` — a peer-reviewed academic project (Université de Lille / Inria); the fingerprinting methodology is public and well-cited.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | am-i-unique |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  → device-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

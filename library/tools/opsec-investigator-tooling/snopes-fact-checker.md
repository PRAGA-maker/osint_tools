---
id: snopes-fact-checker
name: Snopes Fact Checker
description: Use when you have a viral claim, rumour, image or urban legend and want to know if it's true, false or mixed — returns a sourced fact-check verdict.
url: http://www.snopes.com
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Checking whether a rumour, viral claim, meme or "urban legend" has already been investigated and rated.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free to read (ad-supported); no account needed.
opsec: passive
opsecNote: Reading a fact-check is passive and reveals nothing about your subject. It's a verification aid — use it to avoid amplifying a false claim, not as a lookup on a person.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: One of the oldest and most established fact-checking outlets; rulings cite sources, though (like any single outlet) confirm high-stakes claims against additional references.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- snopes
aliases:
- Snopes
- snopes.com
tags:
- fact-checking
- verification
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Snopes Fact Checker

> The veteran fact-checking site (formerly the Urban Legends Reference Pages) — look up a viral claim, rumour or image and see whether it's been rated true, false or mixed, with sources.

## When to use
A claim, screenshot, meme, or "did you hear that…" rumour surfaces in your investigation or feed and you need to know if it's already been debunked or confirmed before you act on or repeat it. Snopes has decades of investigated claims; checking it first prevents you from building on misinformation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.snopes.com and search the claim in your own words (or key phrases from a viral post/caption).
2. Open the matching fact-check: read the **rating** (True / False / Mixture / Unproven, etc.) and the sourced explanation.
3. Follow the cited primary sources to verify the reasoning yourself.
4. If there's no Snopes article, don't treat that as confirmation either way — check other fact-checkers.
5. Pivot: use the verdict to weight a claim in your analysis and to avoid amplifying false information.

## Inputs → Outputs
- **In:** a claim/rumour/image described in words (not a personal selector)
- **Out:** a rated, sourced fact-check verdict
- **Empty/negative result looks like:** no article means Snopes hasn't covered that specific claim — absence is not a verdict; verify elsewhere.

## Gotchas & OpSec
- It's a fact-verification aid, not a database about individuals — don't use it to look up a person.
- A single outlet: corroborate consequential claims with other fact-checkers and the primary sources cited.
- OpSec: passive reading; no login, no target contact.

## Overlaps ("do both")
- Complements other fact-checkers (PolitiFact, AFP Fact Check, Full Fact) and reverse-image search — cross-check a viral image both by its claim (Snopes) and its origin (reverse image) to fully debunk or confirm it.

## Trust & verifiability
`trust: trusted` — a long-established, source-citing fact-checker; still follow its cited primary sources for anything you'll rely on evidentially.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | snopes-fact-checker |

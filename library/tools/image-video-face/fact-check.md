---
id: fact-check
name: FactCheck.org
description: Use when you have a claim, quote, or viral `image`/video attributed to a US public figure and want to know if it's already been verified or debunked — returns fact-check verdicts and sourced context (no direct selector output).
url: http://www.factcheck.org
category: image-video-face
path:
- image-video-face
bestFor: Checking whether a US political/public claim, quote, or manipulated media artifact has already been fact-checked, with a documented evidence trail.
selectorsIn:
- image
selectorsOut: []
status: live
pricing: free
costNote: Free, nonprofit (Annenberg Public Policy Center). No account.
opsec: passive
opsecNote: Passive — you read published fact-checks and search an archive; nothing is disclosed to any subject. Standard web-read hygiene only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Nonpartisan project of the Annenberg Public Policy Center (University of Pennsylvania), a long-established, well-regarded fact-checker with transparent sourcing.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- debunking-false-stories-archives
- scicheck
aliases:
- FactCheck.org
tags:
- fact-checking
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# FactCheck.org

> A veteran, nonpartisan US fact-checking archive — the place to see whether a political claim, quote, or viral image has already been examined and what the evidence actually says.

## When to use
You've been handed a claim, a quote attributed to a public figure, or a viral `image`/video (a doctored photo, a miscaptioned clip) touching US politics or public affairs, and you need to know if it's true, false, or missing context — with sourcing you can cite. Best for US political/public-affairs material; its SciCheck arm covers science/health claims.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.factcheck.org and search the claim, name, or a distinctive phrase (or `site:factcheck.org <terms>`).
2. Separately reverse-image-search a suspect image; then check FactCheck for an existing debunk of that image/claim.
3. Read the article for the verdict *and* its evidence chain — primary sources, dates, and what was actually said/shown.
4. Follow the cited primary sources to confirm independently.
5. Pivot: an established true/false verdict stops you chasing fabricated leads and anchors a timeline with dated sources.

## Inputs → Outputs
- **In:** a claim / quote / `image` or media artifact
- **Out:** fact-check verdict + sourced context and provenance (analysis, not a structured selector)
- **Empty/negative result looks like:** no matching article — it hasn't been fact-checked here (common outside US public affairs); fall back to reverse-image search and other fact-checkers.

## Gotchas & OpSec
- Scope skews **US politics/public affairs** (plus science via SciCheck) — thin on non-US or non-political material.
- It fact-checks *claims/media*, not people — it won't locate or profile an individual.
- OpSec: passive; safe to read freely.

## Overlaps ("do both")
- Pairs with `[[scicheck]]` (its science arm), `[[debunking-false-stories-archives]]`, and reverse-image/EXIF forensics — FactCheck tells you if a claim/image is already debunked; forensics tools let you originate your own provenance check.

## Trust & verifiability
`trust: trusted` — nonpartisan Annenberg (UPenn) project with two decades of transparent, sourced fact-checking; still follow its cited primary sources for high-stakes conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fact-check |
| category | image-video-face |
| selectorsIn → selectorsOut | image → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

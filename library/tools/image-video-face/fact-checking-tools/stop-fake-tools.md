---
id: stop-fake-tools
name: StopFake
description: Use when you have an `image`, claim, or narrative (especially Russia/Ukraine-related) and want to check whether it has already been debunked or contextualized — returns fact-check verdicts, source analysis and provenance context (no direct selector output).
url: http://www.stopfake.org/
category: image-video-face
path:
- image-video-face
- fact-checking-tools
bestFor: Verifying or debunking disinformation, staged media and false narratives, with a strong focus on the Russia/Ukraine information space.
selectorsIn:
- image
selectorsOut: []
status: live
pricing: free
costNote: Free to read and search; no account.
opsec: passive
opsecNote: Passive — you read published fact-checks and search an archive. Nothing is disclosed to any subject; requests originate from your IP like any web read.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established Ukrainian fact-checking project (originating at Kyiv-Mohyla journalism school); reputable within the anti-disinformation community, though it has an explicit editorial focus (counter-Russian-disinformation) to keep in mind.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
aliases:
- StopFake.org
tags:
- fact-checking
- disinformation
- verification
source: arf-seed
lastVerified: '2026-07-21'
enrichment: full
---

# StopFake

> A veteran fact-checking archive centered on the Russia/Ukraine information war — the place to check whether a viral image or claim you've been handed is already a documented fake.

## When to use
You've encountered an `image`, video still, or narrative — a "photo from the front," a screenshot, an atrocity claim, a quote attributed to an official — and need to know if it has been debunked, is staged/recycled, or is genuine. Most valuable when the material touches the Russia/Ukraine conflict, but its "How to Identify a Fake" methodology transfers to any suspected manipulated media.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.stopfake.org/ (English section available) and search the archive for the claim, event, or a distinctive phrase.
2. Reverse-image-search the suspect `image` separately; then check StopFake for whether that image/scene has an existing debunk.
3. Read the fact-check for the verdict *and* its evidence chain — original source, date, where the media actually came from.
4. Use their "How to Identify a Fake" guidance to run your own checks when there's no existing article.
5. Pivot: a confirmed original source/date can re-anchor a timeline; a debunk stops you chasing a fabricated lead.

## Inputs → Outputs
- **In:** an `image`/media artifact or a claim/narrative
- **Out:** fact-check verdict, provenance/source analysis, contextual debunk (analysis, not a structured selector)
- **Empty/negative result looks like:** no matching article — it hasn't been fact-checked here (common outside the Russia/Ukraine focus); fall back to reverse-image search and other fact-checkers.

## Gotchas & OpSec
- **Editorial focus**: the project explicitly counters Russian disinformation — excellent within that lane, but note the standpoint and corroborate with an independent fact-checker for balance.
- Coverage is thin outside its regional/topical focus.
- OpSec: passive; safe to read freely.

## Overlaps ("do both")
- Pairs with reverse-image search and image-forensics/EXIF tools — StopFake tells you *if a scene is already debunked*, while reverse-image and metadata tools let you originate your own provenance check on a fresh image.

## Trust & verifiability
`trust: community` — a reputable, long-running fact-checking outlet with a stated editorial mission; treat its evidence chain as the value and confirm high-stakes conclusions against a second independent source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | stop-fake-tools |
| category | image-video-face |
| selectorsIn → selectorsOut | image → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

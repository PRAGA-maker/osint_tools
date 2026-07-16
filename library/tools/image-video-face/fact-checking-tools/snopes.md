---
id: snopes
name: Snopes
description: Use when you have a viral claim, rumor, image or story (a `document-id`) and want to check whether it is true — returns a sourced verdict and citation trail.
url: https://www.snopes.com/
category: image-video-face
path:
- image-video-face
- fact-checking-tools
bestFor: Quickly checking whether a widely-circulated rumor, meme, image or story has already been investigated and rated true/false.
selectorsIn:
- document-id
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free to read all fact-checks; no account required.
opsec: passive
opsecNote: Searching a public fact-check archive reveals nothing about a subject; activity is limited to normal web-browsing telemetry. Passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: One of the oldest and most established fact-checking outlets; articles carry explicit verdicts and cited sourcing you can follow and verify.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- snopes-fact-checker
aliases:
- snopes.com
tags:
- fact-checking
- misinformation
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
---

# Snopes

> The veteran rumor-and-misinformation checker — search a viral claim, image or story and get a plainly-rated verdict with a citation trail.

## When to use
You have encountered a claim, meme, viral photo, or "news" story (a `document-id` — a headline, quote, or circulating item) tied to your investigation and need to know quickly whether it is true, false, mislabeled, or already debunked. Especially useful for sanity-checking a sensational lead — a fabricated missing-person alert, a recycled disaster image, a fake quote — before you act on it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.snopes.com/ .
2. Search for the claim, phrase, or the subject of a viral image/story.
3. Open the matching fact-check article.
4. Read the output: the rating (True / False / Mixture / Miscaptioned / Unproven, etc.), the investigative write-up, and the cited sources (`document-id`) supporting the verdict.
5. Pivot: follow the article's cited sources to the primary material; if Snopes hasn't covered it, move to reverse-image search or another fact-checker.

## Inputs → Outputs
- **In:** `document-id` (a claim, rumor, image caption, or story)
- **Out:** `document-id` (a rated fact-check article with sourcing)
- **Empty/negative result looks like:** no article matches — the claim may be too new or too niche; absence is not a verdict, so verify independently.

## Gotchas & OpSec
- It only covers claims someone has already investigated — recent or obscure rumors may not be there yet.
- Read the *rating* precisely: "Miscaptioned" or "Mixture" is not the same as "False" — a real image with a fake caption is common.
- OpSec: fully passive; searching reveals nothing about your subject.

## Overlaps ("do both")
- Pairs with `[[snopes-fact-checker]]` and reverse-image tools: Snopes rates the claim; reverse-image search independently traces a viral photo's true origin.

## Trust & verifiability
`trust: trusted` — a long-established fact-checking outlet with explicit verdicts and transparent sourcing you can follow to primary material and verify yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | snopes |
| category | image-video-face |
| selectorsIn → selectorsOut | document-id → document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

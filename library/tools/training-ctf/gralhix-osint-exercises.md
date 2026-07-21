---
id: gralhix-osint-exercises
name: Gralhix OSINT Exercises
description: Use when you want to build or sharpen practical `image`/`geolocation` verification skills — a free, graded library of hands-on OSINT exercises with full walkthroughs.
url: https://gralhix.com/list-of-osint-exercises
category: training-ctf
path:
- training-ctf
bestFor: Practising real-world geolocation, image verification, and disinformation-analysis techniques against graded exercises with answer keys.
selectorsIn:
- image
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Entirely free; all exercises and their walkthroughs are published openly with no account or paywall.
opsec: passive
opsecNote: This is a training resource, not a live investigation tool — you work against fixed practice material, so there is no live target to alert. Standard browsing hygiene is sufficient.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Authored by Sofia Santos (Gralhix), a well-known OSINT practitioner; each exercise ships a documented walkthrough, so methods are verifiable rather than asserted.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Gralhix
- Sofia Santos OSINT exercises
- list of OSINT exercises
tags:
- tl-discord
- strategy
- training
- geolocation
source: tl-discord
lastVerified: '2026-07-21'
enrichment: full
---

# Gralhix OSINT Exercises

> A free, growing library of hands-on OSINT exercises (30+) by Sofia Santos, each with a full walkthrough — the place to *learn the method* before you apply it to a real missing-persons case.

## When to use
Reach for this when the bottleneck is your (or an agent's) skill rather than a specific subject: you need to practise geolocating a photo from visible clues, verifying whether an image is authentic and when/where it was taken, or dissecting disinformation. Building these reflexes on graded exercises — with an answer key to check yourself against — directly improves the geolocation and image-verification steps that matter most in real missing-persons work, where a single background photo often has to yield a location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://gralhix.com/list-of-osint-exercises.
2. Pick an exercise by difficulty (rated separately for novice vs. expert) and topic (geolocation, verification, satellite imagery, social-media analysis, conflict zones).
3. Attempt the 1–4 tasks yourself first, using only the clues given — do not read ahead.
4. Compare your process and answer against the published walkthrough to see which techniques and tools you missed.
5. Pivot: carry the techniques (chronolocation, shadow analysis, reverse-image, map cross-referencing) into a live case, pairing them with the actual lookup tools in this library.

## Inputs → Outputs
- **In:** a practice `image`/scenario with embedded `geolocation` clues
- **Out:** the honed *skill* of deriving `geolocation` and verifying media, plus a documented method per exercise
- **Empty/negative result looks like:** not applicable — this is training material, not a query tool; the "failure" mode is simply an exercise you can't yet solve, which the walkthrough then teaches.

## Gotchas & OpSec
- Human-in-the-loop by design: you must actually work the exercises and review the walkthroughs — there is nothing to automate here.
- It teaches methods, not a database of people; value is indirect (better analysts → better casework).
- Content is periodically added; older exercises may reference tools that have since changed.

## Overlaps ("do both")
- Pairs with the live geolocation and reverse-image tools in this library — Gralhix builds the technique, those tools execute it on a real subject.

## Trust & verifiability
`trust: trusted` — a respected practitioner's openly documented exercises; every answer comes with a reproducible walkthrough, so the tradecraft is auditable rather than taken on faith.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gralhix-osint-exercises |
| category | training-ctf |
| selectorsIn → selectorsOut | image, geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |

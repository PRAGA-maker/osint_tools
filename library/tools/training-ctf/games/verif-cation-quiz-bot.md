---
id: verif-cation-quiz-bot
name: Quiztime (#quiztime)
description: Use when you want to build/verify geolocation and image-verification skills — returns community OSINT challenges with worked solutions, not subject data.
url: https://x.com/quiztime
category: training-ctf
path:
- training-ctf
bestFor: Practising and sharpening image verification and geolocation through the daily community
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free to follow and participate; only a (sock-puppet) X account is needed to post answers.
opsec: passive
opsecNote: This is a training community, not an investigation. Still, participate from a sock-puppet X account, not your real identity — your solving methods and interests are visible to others. Never post real casework here.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running, well-regarded verification/geolocation challenge community run by experienced practitioners; content is educational and peer-produced.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- gralhix-osint-exercises
- geoguesser
- help-x-com
- here-19
- here-20
- twitter-search
- twitter-x-advanced-search
- x-com-3
- x-com-4
- x-com-6
aliases:
- Quiztime
- quiztime
- Verification Quiz Bot
tags:
- training
- geolocation
- verification
- ctf
source: osint-training
lastVerified: '2026-08-05'
enrichment: full
---

# Quiztime (#quiztime)

> The daily #quiztime challenge community — image-verification and geolocation puzzles with crowd-sourced solutions, for building the muscle you'll use on real cases.

## When to use
You want to practise or level up the core verification skills — geolocating a photo, dating an image, spotting fakes, chaining reverse-image and map tools — in a low-stakes setting before applying them to a live missing-persons case. #quiztime posts regular puzzles; participants work them openly and share methods, so it doubles as a technique library. This is a *training* resource: it produces skills and worked examples, not data about any subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Follow the #quiztime hashtag and the quiztime account on X (from a sock-puppet account).
2. Pick an active challenge (usually a photo to geolocate or verify) and attempt it before reading answers.
3. Work it with real tools — reverse image search, mapping/street-level imagery, metadata — then compare against the community's posted solution and method.
4. Bank the techniques and tool combinations that solved it for reuse on actual cases; deepen with structured exercises in `[[gralhix-osint-exercises]]`.

## Inputs → Outputs
- **In:** none (a practice feed; you bring effort)
- **Out:** verification/geolocation skills + worked method write-ups (no subject selectors)
- **Empty/negative result looks like:** N/A — it's a learning resource. The "failure" mode is not attempting challenges yourself before reading solutions, which skips the actual skill-building.

## Gotchas & OpSec
- It's training, not casework — never post real investigation material or a real subject's images to the community.
- Participate under a sock-puppet identity; your answers and interests are public.
- Requires an X account to post (account-login); you can read many challenges without one.

## Overlaps ("do both")
- Pair with `[[gralhix-osint-exercises]]` for structured, self-paced geolocation drills and `[[geoguesser]]` to build fast visual-geography intuition; #quiztime adds the live, community-verified element.

## Trust & verifiability
`trust: community` — a respected, practitioner-run training community; treat posted solutions as peer-reviewed teaching examples, and always re-derive the method yourself so the skill transfers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | verif-cation-quiz-bot |
| category | training-ctf |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |

---
id: captin-fact
name: CaptainFact
description: Use when you have a video (YouTube) and want crowd-sourced fact-checks of statements in it — returns sourced verifications/refutations tied to timestamps.
url: https://captainfact.io/
category: image-video-face
path:
- image-video-face
bestFor: Checking whether specific claims in a (YouTube) video have been collaboratively fact-checked, with cited sources tied to timestamps.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and non-profit; all code is open-source. A free account is only needed to contribute votes/sources, not to read.
opsec: passive
opsecNote: Reading fact-checks is passive and touches no target. If you contribute (votes/sources), that activity is public under your account — use a sock puppet if you don't want it attributed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-run collaborative fact-checking (French-origin, non-profit, open source); each check is only as good as the sources its contributors attach — verify the cited sources yourself.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Captain Fact
tags:
- fact-checking
- video-verification
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# CaptainFact

> A collaborative, timestamp-level fact-checking layer for videos (primarily YouTube) — community members attach sourced confirmations, refutations, and context to specific statements.

## When to use
You are assessing the credibility of a video or a channel and want to know whether claims made in it have been challenged or corroborated with sources. Given a video (or a `social-profile`/channel), CaptainFact can show timestamp-anchored fact-checks with citations, helping you weigh whether a source in your investigation is reliable or is spreading disinformation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://captainfact.io/ and browse the Videos section, or search for a specific video/channel (e.g. a subject's YouTube channel).
2. Open a checked video: statements are listed with community votes and attached source links, tied to the moment they were made.
3. Follow the cited sources and read the confirm/refute votes to judge each claim.
4. Note there is a public API for programmatic access if you need to pull checks at scale.
5. Pivot: a channel's fact-check record feeds a source-credibility judgement; cited sources become new leads.

## Inputs → Outputs
- **In:** a video URL or channel `social-profile`
- **Out:** timestamped fact-checks with sourced confirmations/refutations and a channel's `social-profile` credibility signal
- **Empty/negative result looks like:** the video/channel has no checks — coverage is limited to what the volunteer community has reviewed (French-language and popular channels are best covered), so absence is common and not a verdict.

## Gotchas & OpSec
- Coverage is patchy and skews toward French-language and higher-profile content; most videos won't be checked.
- Quality depends on contributors' sources — always follow and evaluate the citations rather than trusting the vote count alone.
- OpSec: reading is passive; contributing is public under your account.

## Overlaps ("do both")
- Pairs with reverse-video/keyframe search and other verification tools — those establish where/when a video came from, while CaptainFact assesses the truth of what's said in it.

## Trust & verifiability
`trust: community` — a genuine non-profit, open-source project, but each fact-check is crowd-produced; verifiability rests on the attached sources, which you should read yourself before relying on a check.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | captin-fact |
| category | image-video-face |
| selectorsIn → selectorsOut | social-profile → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

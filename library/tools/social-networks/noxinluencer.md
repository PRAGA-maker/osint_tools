---
id: noxinluencer
name: Noxinluencer
description: Use when you have a YouTube channel (`social-profile`/`username`) and want its audience, growth and engagement analytics — returns channel activity metrics and rankings.
url: https://noxinfluencer.com/youtube/channel-compare
category: social-networks
path:
- social-networks
bestFor: Profiling a YouTube channel's subscriber growth, upload cadence and engagement, and comparing channels side by side.
selectorsIn:
- social-profile
- username
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free tier shows headline stats and live sub-count; deeper history, full reports and the 5-dimension comparison prompt a paid NoxInfluencer membership.
opsec: passive
opsecNote: You query a third-party analytics platform about a public channel, not the creator; nothing is disclosed to the subject. Use a research browser.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: Commercial influencer-marketing analytics; numbers are third-party estimates (NoxScore, projected earnings) — treat as indicative, not exact.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- NoxInfluencer
- noxinfluencer.com
tags:
- Social Media
- YouTube
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Noxinluencer

> A YouTube analytics platform that turns a channel into growth, engagement and ranking metrics — and compares channels head to head.

## When to use
Your subject runs or is tied to a YouTube channel and you want to characterise it: how fast it's growing, how often and when it uploads, engagement rates, estimated earnings, and how it ranks. Useful to gauge whether a channel is active/real, to establish an activity timeline, or to compare a suspected alias channel against a known one.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://noxinfluencer.com/ and search the channel name/handle (or use the channel-compare page for two channels).
2. Read the free profile: subscriber count and live count, recent upload frequency, average views, engagement, and NoxScore.
3. Use the comparison view to line up two channels across the 5 dimensions.
4. Note that full history and detailed reports are gated behind membership — stop at the free tier and pivot rather than paying.
5. Pivot: an upload cadence/first-video date anchors a timeline; a linked website/social handle in the channel feeds domain/username OSINT.

## Inputs → Outputs
- **In:** YouTube channel (`social-profile` URL or `username`/handle)
- **Out:** `social-profile` analytics — subscribers, growth, upload cadence, engagement, ranking, estimated value
- **Empty/negative result looks like:** channel not indexed or too small — meaning no analytics history, not that the channel doesn't exist.

## Gotchas & OpSec
- Metrics like earnings and NoxScore are **estimates**, not disclosed figures.
- Deep data is paywalled (`payment-wall-partial`); don't over-rely on the free snapshot.
- It profiles the channel, not the person — a channel operator may be a team or a pseudonym.

## Overlaps ("do both")
- Pairs with YouTube-metadata tools (channel creation date, video upload times) — Nox gives the analytics arc, those give the forensic timestamps.

## Trust & verifiability
`trust: unverified` — a commercial analytics estimator; use its trend/activity signals and confirm hard numbers against the channel's own public stats.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | noxinluencer |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, username → social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |

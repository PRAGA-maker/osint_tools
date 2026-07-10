---
id: audiense
name: Audiense
description: Use when you have a Twitter/X `username` or audience and want deep audience-segmentation intelligence — returns audience segments, influencers and shared-interest associates.
url: https://www.audiense.com
category: social-networks
path:
- social-networks
bestFor: Profiling a Twitter/X account's audience into behavioral segments and surfacing the influencers and overlapping communities around it.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
status: live
pricing: freemium
costNote: Effectively a paid enterprise platform — access is via a free trial/limited free report, but full audience intelligence requires a paid subscription. Treat as gated.
opsec: passive
opsecNote: Analyzes public social data; the subject/audience is not notified. You must register an account, so activity ties to you — use a research identity, and note results are aggregated marketing analytics, not raw evidence.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Established commercial audience-intelligence vendor (now bundling Elevar and Buxton). Reliable analytics, but it is a marketing product — segments are inferred, not ground truth.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- followerwonk
aliases:
- Audiense Insights
tags:
- real-time-search-social-media-search-and-general-social-media-tools
- twitter
- audience-intelligence
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Audiense

> An enterprise audience-intelligence platform: break a Twitter/X account's followers into behavioral segments and reveal the influencers and communities they cluster around.

## When to use
You have a subject's Twitter/X `username` (or the audience around a topic/brand tied to them) and want structured *audience* intelligence rather than a list of tweets: how their followers segment by interests, affinities and behavior, which accounts are influential within each segment, and which communities overlap. Useful for mapping the social milieu around a person — the `associate` accounts and interest groups that surround them — when a simple follower list isn't enough.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.audiense.com and register (free trial / limited report; full features need a paid plan).
2. Create an audience report from a Twitter/X `username`, a follower base, or a keyword/topic.
3. Let it build segments: the platform clusters the audience by behavior, interests and cultural affinities.
4. Read output: audience segments, top influencers per segment, shared-interest communities, and demographic/affinity summaries.
5. Pivot: influential/overlapping `social-profile`s become new `associate` leads; interest clusters hint at where else the subject or their circle is active.

## Inputs → Outputs
- **In:** `username` (or audience/topic)
- **Out:** `social-profile` segments, `associate` (influencers and overlapping community accounts)
- **Empty/negative result looks like:** a thin or single-segment report. Small or low-activity accounts don't segment meaningfully, and X's API limits can cap the audience it can pull — sparse output reflects data limits, not necessarily a small network.

## Gotchas & OpSec
- **Paywall:** the substantive intelligence sits behind a paid subscription; the free path is a trial/limited report.
- Segments are *inferred* marketing analytics — treat "communities" and "affinities" as hypotheses to confirm, not facts.
- Depends on X API access, which has tightened since 2023.
- OpSec: passive; analyzes public data but requires a logged-in account.

## Overlaps ("do both")
- Pairs with `[[followerwonk]]` — Followerwonk gives raw follower analytics and account-overlap comparison for free-ish; Audiense adds deeper behavioral segmentation. Use Followerwonk first, Audiense when you need the richer segmentation.

## Trust & verifiability
`trust: community` — a mature commercial vendor with dependable analytics, but it is a marketing-intelligence product: its segments and affinities are inferred from public data, so verify any specific person-to-person link directly on-platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | audiense |
</content>

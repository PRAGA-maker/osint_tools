---
id: analyze-words-twitter
name: AnalyzeWords (Twitter)
description: Use when you have an X/Twitter `username` and want a quick psycholinguistic read of their tweets — returns an emotional/social/thinking-style profile (`social-profile` context), not identifying data.
url: http://analyzewords.com/
category: social-networks
path:
- social-networks
bestFor: A fast, low-effort personality/tone sketch of a Twitter account from its recent language patterns.
selectorsIn:
- username
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free; no account. Runs on LIWC-style text analysis (now hosted under liwc.net) by Pennebaker's group.
opsec: passive
opsecNote: You submit a handle to the analyzer; the target is not notified. It reads public tweets only. Because it relies on Twitter/X API access, results may be empty or stale.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Built on legitimate LIWC psycholinguistics (Pennebaker Conglomerates), but the output is a coarse, inferential personality sketch — not evidence and not identity data.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- analyzewords.com
- LIWC AnalyzeWords
tags:
- toddington
- curated-directory
- social-media
- text-analysis
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# AnalyzeWords (Twitter)

> A psycholinguistic toy-grade profiler: feed it a Twitter handle and it scores the account's emotional, social, and thinking styles from word usage — context, not identification.

## When to use
You have an X/Twitter `username` and want a rapid, impressionistic sense of the account's tone and disposition (upbeat vs. worried/angry, personable vs. detached, analytic vs. in-the-moment) before reading the timeline. It is corroborating colour for an assessment — never treat its scores as fact or as anything that identifies a person. Because it depends on Twitter/X API access, which is now heavily restricted, expect frequent empty results (`status: degraded`).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://analyzewords.com/ (redirects to the LIWC-hosted version).
2. Enter the target `username` and run the analysis.
3. Read the dimension scores (emotional style, social style, thinking style) as a rough sketch.
4. Sanity-check against the actual timeline — the model is coarse and context-blind (sarcasm, quotes, retweets skew it).
5. Pivot: use it only to prioritise/frame; do real content review with a timeline reader for substance.

## Inputs → Outputs
- **In:** `username` (Twitter/X handle)
- **Out:** a psycholinguistic `social-profile` sketch (style scores) — NOT names, locations, or identifiers
- **Empty/negative result looks like:** no data / error — most likely API access failure now, or too few tweets to score.

## Gotchas & OpSec
- Inferential and low-precision: retweets, sarcasm, and topic shifts distort scores badly.
- API-dependent; often non-functional post-2023 X API changes — confirm before citing.
- Never present its output as evidence or attribute it to a real personality assessment.

## Overlaps ("do both")
- Pairs with `[[tweet-topic-explorer]]` — that maps *topics and mentioned associates*, this scores *style*; together they sketch what an account talks about and how.

## Trust & verifiability
`trust: unverified` — grounded in real LIWC research but delivered as a coarse consumer sketch; treat results as soft context to verify against the timeline, not as findings.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | analyze-words-twitter |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

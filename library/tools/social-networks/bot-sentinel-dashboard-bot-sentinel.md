---
id: bot-sentinel-dashboard-bot-sentinel
name: Bot Sentinel
description: Use when you have an X/Twitter `username` and want a data-driven rating of how likely the account engages in inauthentic/trollbot behavior — returns a 0–100% problematic-behavior score.
url: https://botsentinel.com
category: social-networks
path:
- social-networks
bestFor: Scoring an X (Twitter) account for inauthentic, troll, or coordinated-harassment behavior.
selectorsIn:
- username
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free to look up an account's rating. Note the service has been in transition (Twitter/X revoked its API access in 2022; it announced an AI-powered relaunch in 2026), so coverage and availability are uneven.
opsec: passive
opsecNote: Passive — you query Bot Sentinel's own analysis, not the target account, and the subject is not notified. Ratings are behavioral estimates from its model, not proof; use as one signal, not a verdict.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known independent disinformation/bot tracker (founded 2018); its scoring is proprietary and its data pipeline has been disrupted by X API changes, so treat scores as indicative.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Bot Sentinel
- botsentinel.com
tags:
- twitter
- x
- bot-detection
- disinformation
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Bot Sentinel

> An independent tracker that rates X (Twitter) accounts 0–100% on how likely they are engaging in inauthentic, troll, or harassment behavior.

## When to use
You have an X/Twitter `username` and want a second opinion on whether the account behaves authentically — useful when assessing the credibility of a source, spotting coordinated harassment, or judging whether an account amplifying a narrative is likely a troll/bot. It rates *behavior patterns*, complementing follower-quality tools that rate the audience.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://botsentinel.com (the service has been relaunching; if a lookup is unavailable, its rating may not be current).
2. Search the target `username`.
3. Read the score: 0–100%, where higher means more likely engaged in problematic/inauthentic activity, plus the account's rating category.
4. Treat the score as one behavioral signal — corroborate with the account's actual content and posting patterns.
5. Pivot: a high score flags an account worth manual scrutiny; combine with follower-audit tools for a fuller picture.

## Inputs → Outputs
- **In:** X/Twitter `username`
- **Out:** a 0–100% problematic-behavior score and rating category for the `social-profile`
- **Empty/negative result looks like:** "not rated"/no data — the account may be outside its database or the pipeline is disrupted by X API limits; absence of a rating is not a clean bill.

## Gotchas & OpSec
- **Data disruption:** X revoked its API access in 2022 and the service has been mid-relaunch — scores can be stale or unavailable; verify recency.
- Scoring is proprietary and probabilistic — never present a score as definitive proof of a bot.
- Applies to X/Twitter only.

## Overlaps ("do both")
- Pairs with follower-quality auditors (e.g. `[[followeraudit]]`) — Bot Sentinel rates the account's own behavior while those rate the authenticity of its followers; do both for a full authenticity read.

## Trust & verifiability
`trust: community` — a reputable independent tracker with opaque, disruption-affected scoring; use its rating as a lead and confirm by examining the account's actual activity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bot-sentinel-dashboard-bot-sentinel |

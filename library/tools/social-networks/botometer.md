---
id: botometer
name: Botometer
description: Use when you have a Twitter/X `username` and want a bot-likelihood score for the account — returns a bot/human probability and behavioural sub-scores, from pre-June-2023 archival data.
url: https://botometer.osome.iu.edu/
category: social-networks
path:
- social-networks
bestFor: Assessing whether a Twitter/X account is automated/inauthentic when weighing how much to trust a "sighting" or lead posted by that account.
selectorsIn:
- username
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free to query. The public web form is limited; programmatic scoring requires a RapidAPI key (free tier) plus Twitter/X API credentials, which are now costly — hence the tool's archival-only state.
opsec: passive
opsecNote: You look up a public account's bot score; the target is not notified. Scoring is passive. Do not read the score as proof of identity or intent — it is a probabilistic signal only.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built and published by Indiana University's Observatory on Social Media (OSoMe); peer-reviewed methodology. The limitation is data freshness, not credibility.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Botometer X
- BotometerLite
- OSoMe Botometer
tags:
- twitter
- bot-detection
source: metaosint
lastVerified: '2026-07-19'
enrichment: full
relatedTools:
- botometer-by-osome
- botslayer
- covaxxy
- network-tool
- osome-iu-edu
- trends-tool
---

# Botometer

> Indiana University's machine-learning bot-likelihood scorer for Twitter/X accounts — now running in archival mode on pre-June-2023 data.

## When to use
You have a Twitter/X `username` that posted a lead — a claimed sighting, a "found them" reply, an account amplifying a missing-person appeal — and you need to judge whether it is a real person or an automated/inauthentic account before you act on it. A high bot score is a reason to discount or corroborate a lead more carefully; a low score doesn't prove authenticity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://botometer.osome.iu.edu/ (this is "Botometer X", the successor to the retired botometer.iuni.iu.edu / botometer.osome.iu.edu classic).
2. Enter the target `@handle`.
3. Read the overall bot score plus the sub-scores (e.g. astroturf, spammer, self-declared, fake-follower) and the language-independent BotometerLite score.
4. Treat the number as a probability, not a verdict — combine with a manual look at the account's age, posting cadence, and content.
5. Pivot: for network-level manipulation around a hashtag/appeal, move to OSoMe's `[[network-tool]]` / `[[trends-tool]]`; for a live stream of suspicious accounts use `[[botslayer]]`.

## Inputs → Outputs
- **In:** `username` (Twitter/X handle)
- **Out:** bot-likelihood score + behavioural sub-scores attached to that `social-profile`
- **Empty/negative result looks like:** for any account created after 31 May 2023, or with no cached history, Botometer X has **no record** and returns nothing usable — absence of a score is not a "human" verdict.

## Gotchas & OpSec
- Human-in-the-loop: the reliable path now needs an `api-key` (RapidAPI free tier + Twitter/X API credentials); the free web form is best-effort and often can't fetch fresh timelines.
- **Archival only:** scores derive from data collected before June 2023; they do not reflect recent behaviour and, per OSoMe, cannot catch modern AI-driven bots. State this caveat whenever you cite a score.
- Passive, but the score is probabilistic — never present it as identification of a specific human.

## Overlaps ("do both")
- Pairs with `[[botslayer]]` (real-time coordinated-behaviour detection) and `[[network-tool]]` — Botometer scores one account, those map the network amplifying a topic.

## Trust & verifiability
`trust: trusted` — OSoMe is an academic lab with published, peer-reviewed methodology. The rating reflects credible science; the operational caveat is that the underlying data is frozen pre-June-2023, so freshness, not trustworthiness, is the risk.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | botometer |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (api-key) |

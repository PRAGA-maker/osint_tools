---
id: botometer-by-osome
name: Botometer by OSoMe
description: Use when you have a Twitter/X `username` and want a bot-likelihood score — now archival ("Botometer X"), returns a pre-June-2023 automation score for accounts that existed then.
url: https://botometer.osome.iu.edu/
category: social-networks
path:
- social-networks
bestFor: Estimating how bot-like a Twitter/X account is, from historical (pre-June-2023) behavioural scores.
selectorsIn:
- username
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free to query. The interactive, real-time version ended when X cut off free API access; the current "Botometer X" serves pre-calculated historical scores only.
opsec: passive
opsecNote: You look up a cached score by handle — no interaction with the account and no notification to the user. Only the analysed account's public behaviour informs the score.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built by Indiana University's Observatory on Social Media (OSoMe), a reputable academic bot-detection research group; the model is peer-reviewed, but coverage is now frozen.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Botometer X
- OSoMe Botometer
tags:
- twitter
- bot-detection
- account-analysis
source: osint4all
lastVerified: '2026-07-23'
relatedTools:
- botometer
- botslayer
- covaxxy
- network-tool
- osome-iu-edu
- trends-tool
---

# Botometer by OSoMe

> An academic bot-likelihood scorer for Twitter/X accounts — after X ended free API access it was rebranded "Botometer X" and now returns pre-calculated historical scores rather than live analysis.

## When to use
You have a Twitter/X `username` and want to gauge whether it behaves like an automated/bot account when assessing the credibility of a lead, a tip, or an account interacting with your subject. Because the tool is now archival, it's only useful for accounts that existed and were active before June 2023 — treat it as a historical check, not a live one.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://botometer.osome.iu.edu/ (Botometer X).
2. Enter the Twitter/X handle.
3. Read the returned score: higher = more bot-like, based on the account's pre-June-2023 behaviour (posting patterns, network, content signals).
4. Interpret: a high score suggests automation; a low score suggests a human-driven account — for the historical period only.
5. Pivot: a likely-bot account interacting with your subject is probably noise; a human account is worth deeper profiling.

## Inputs → Outputs
- **In:** `username` (Twitter/X handle)
- **Out:** a bot-likelihood score / `social-profile` assessment (historical)
- **Empty/negative result looks like:** "no record" — the account was created after May 31, 2023 (post-cutoff) or wasn't in the archive; absence is a coverage gap, not a verdict.

## Gotchas & OpSec
- Archival only (`status: degraded`): no data for accounts created after May 2023, and no reflection of behaviour since then — a formerly-human account could have been sold/automated since, and the score won't know.
- A score is a probability, not proof; corroborate with manual review of the account's activity.
- OpSec: **passive** — a cached lookup, invisible to the account.

## Overlaps ("do both")
- Pairs with manual account review and other bot/coordination tools (`[[botslayer]]`) — Botometer scores an individual account historically; manual review and network tools assess current, coordinated behaviour.

## Trust & verifiability
`trust: trusted` — a peer-reviewed academic tool from OSoMe; the limitation is coverage (frozen pre-June-2023), not methodology.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | botometer-by-osome |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: twitter-audit
name: TwitterAudit
description: Use when you have an X (Twitter) `username` and want a rough estimate of how many of its followers look fake vs real — returns a real/fake follower score for the account.
url: https://www.twitteraudit.com
category: social-networks
path:
- social-networks
bestFor: Estimating the proportion of fake/bot followers on a Twitter/X account.
selectorsIn:
- username
selectorsOut:
- social-profile
status: degraded
pricing: freemium
costNote: A basic audit of your own or a public account is free; larger/repeat audits and full follower breakdowns are paid.
opsec: passive
opsecNote: The audited account is not notified. Historically it required authorising the app against a Twitter account for deeper audits — avoid connecting your real account; use a sock puppet, and prefer the anonymous public-account audit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party estimator using a sampled heuristic (not ground truth). Since X's API lockdown its ability to audit arbitrary/newer accounts is unreliable — treat any score as a rough indicator only.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Twitter Audit
- twitteraudit.com
tags:
- twitter
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# TwitterAudit

> A follower-authenticity estimator for X (Twitter) accounts — samples an account's followers and scores what fraction look like bots/fakes.

## When to use
You have an X `username` and want a quick read on whether its follower base is largely genuine or inflated with bots — e.g. assessing whether an account is an authentic person or an amplified/purchased persona. This is a credibility-signal tool, not a person-locator; its missing-person value is marginal (judging whether a lead account is real).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.twitteraudit.com and enter the target `username`.
2. Request the audit; it samples the account's followers and returns a real-vs-fake percentage score.
3. Read the score as a rough proportion — a high "fake" share suggests bought/bot followers; a high "real" share suggests an organically grown account.
4. Treat the number sceptically: sampling plus post-API-change data access make it approximate at best.
5. Pivot: use the credibility read to decide how much weight to give an account when it's a lead in `[[twitter-search]]`.

## Inputs → Outputs
- **In:** `username` (X/Twitter handle)
- **Out:** a real/fake follower score for that `social-profile`
- **Empty/negative result looks like:** an audit that won't run, errors, or an obviously stale/implausible score — increasingly common since X restricted API access; don't rely on it as ground truth.

## Gotchas & OpSec
- Degraded: X's API lockdown has undermined tools like this; newer or protected accounts may not audit at all.
- Heuristic, not truth: the score is a sampled estimate, easily wrong for accounts with unusual follower patterns.
- OpSec: prefer the anonymous public-account audit; never authorise it against your real X account.

## Overlaps ("do both")
- Pairs with `[[twitter-search]]` — search finds and profiles the account, TwitterAudit adds a (rough) authenticity signal to judge whether the account is worth pursuing.

## Trust & verifiability
`trust: unverified` — a third-party heuristic estimator whose accuracy and continued function are both uncertain post-API changes; use only as a soft indicator.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitter-audit |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

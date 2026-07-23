---
id: followeraudit
name: FollowerAudit
description: Use when you have an X/Twitter `username` and want to assess how many of its followers are fake/bot/inactive — returns an authenticity score and follower-quality breakdown.
url: https://www.followeraudit.com/
category: social-networks
path:
- social-networks
bestFor: Judging whether an X (Twitter) account's follower base is genuine, and spotting bot/inactive followers.
selectorsIn:
- username
selectorsOut:
- associate
status: live
pricing: freemium
costNote: Auditing your own connected account is free; auditing arbitrary third-party accounts and larger/export reports are on paid plans.
opsec: active
opsecNote: Requires signing in with an X (Twitter) account via OAuth, so use a sock-puppet X account you control — never your real identity. Auditing another user's public account does not notify them, but the OAuth session ties the audit to whatever account you authorize.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Established follower-analytics vendor; its bot heuristics are proprietary and approximate, so treat the score as an estimate rather than ground truth.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- FollowerAudit
- followeraudit.com
tags:
- twitter
- x
- bot-detection
- follower-analysis
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# FollowerAudit

> A follower-quality auditor for X (Twitter) that scores an account's followers as real, fake, bot, or inactive.

## When to use
You have an X/Twitter `username` and want to gauge whether its audience is organic — for example to judge if an influencer, campaign, or suspicious account has been artificially inflated, or to profile the account's genuine `associate` network by filtering out bots. It answers "is this following real?", not "who exactly follows this person".

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.followeraudit.com/ and sign in with a sock-puppet X account via OAuth.
2. Enter the target public `username` to audit (your own connected account audits free; third-party audits may need a paid plan).
3. Start the audit and wait for it to process the follower list.
4. Read the report: FA authenticity score, and counts of real vs. fake/bot/inactive followers, plus quality metrics.
5. Pivot: a high fake-follower ratio flags manufactured influence; the genuine-follower subset narrows down real `associate` connections for further profiling.

## Inputs → Outputs
- **In:** X/Twitter `username`
- **Out:** authenticity (FA) score, fake/bot/inactive breakdown, follower-quality analytics; genuine followers as candidate `associate`s
- **Empty/negative result looks like:** audit fails or returns "account private/too large for free tier" — a protected or very large account can't be fully audited without a paid plan.

## Gotchas & OpSec
- **Login required:** always authorize with a throwaway X account, never your real one.
- Bot detection is heuristic and proprietary — the numbers are estimates; don't state them as fact.
- Free access is limited to your connected account and small reports; broad third-party auditing is paywalled.

## Overlaps ("do both")
- Pairs with general X/Twitter profile and follower-mapping tools — FollowerAudit judges follower *quality* while those enumerate follower *identity*; do both to separate the real network from the noise.

## Trust & verifiability
`trust: community` — a known analytics vendor with opaque scoring; reproduce spot-checks by manually sampling flagged accounts to confirm they look like bots.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | followeraudit |

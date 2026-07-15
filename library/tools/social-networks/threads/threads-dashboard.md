---
id: threads-dashboard
name: Threads Dashboard
description: Use when you control (or can log into) a Meta Threads account and want its analytics — returns follower trends, engagement, posting cadence and audience demographics for that connected `social-profile`.
url: https://www.threadsdashboard.com/
category: social-networks
path:
- social-networks
- threads
bestFor: Analytics on a Threads account you can authenticate as — follower growth, engagement, posting times, audience demographics.
selectorsIn:
- social-profile
- username
selectorsOut:
- social-profile
- metadata-exif
status: live
pricing: freemium
costNote: Perpetual free tier gives basic metrics and current-week data; Pro (~$5.99/mo, or ~$4.99/mo annual) unlocks 6–12 months of history, advanced charts, and follower demographics.
opsec: passive
opsecNote: Data is pulled through Meta's official Threads API via one-click Meta login — so you can only analyse an account you can authenticate as (your own or a sock puppet you control), NOT an arbitrary target. It does not touch or notify third-party accounts. Passive, but it requires connecting a Meta account, which ties the activity to that login.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party analytics SaaS built on Meta's Threads API. It surfaces official Meta metrics for a connected account; reliability depends on Meta's API, and the service is a small commercial operator with no independent track record.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- Threads Dashboard
- threadsdashboard.com
tags:
- threads
- meta-threads
- social-analytics
source: arf-seed
lastVerified: '2026-07-15'
enrichment: full
---

# Threads Dashboard

> Meta Threads analytics for an account you can log into — growth, engagement, posting times, and audience breakdown, drawn from Meta's official API.

## When to use
You have access to a Threads account relevant to a case — a sock-puppet you use for monitoring, an organisation account you manage, or (with authority/consent) the subject's own account — and you want structured analytics: when it posts, how engagement moves, and who the audience is. Because it authenticates via Meta login, it analyses accounts you can sign into, not arbitrary strangers' profiles.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.threadsdashboard.com/.
2. Click the one-click **Log in with Meta** — you authenticate as the Threads account you want analysed (no passwords stored by the site; it uses Meta OAuth).
3. Let it sync. Review the free-tier basics: follower count, post impressions, engagement, current-week activity.
4. For deeper timelines (posting-time heatmaps, months of history, audience demographics) upgrade to a paid tier.
5. Pivot: use the posting-time pattern to predict when the account is active; feed audience/engagement leads into wider social mapping.

## Inputs → Outputs
- **In:** a connected Threads `social-profile` / `username` you can authenticate as
- **Out:** follower trend, engagement rates, posting cadence and optimal-time heatmap, audience demographics (paid), historical activity (paid) — a bundle of `metadata-exif`-style behavioural signals
- **Empty/negative result looks like:** you cannot analyse an account you can't log into — there is no "enter any username" mode. A brand-new account shows near-empty analytics.

## Gotchas & OpSec
- **Not a target-lookup tool.** It requires Meta OAuth for the account being analysed, so it is for accounts you legitimately control or are authorised to access — using it on someone else's account requires their login, which you should not obtain covertly.
- Everything depends on Meta's Threads API; if Meta changes/limits the API, metrics degrade.
- OpSec: **passive** toward third parties, but you are connecting a Meta identity — do it from the sock-puppet account, not a personal one.

## Overlaps ("do both")
- Complements native Threads/Instagram viewing and any username-enumeration tool: this gives *behavioural* analytics (cadence, audience) for an account you hold, while public-profile tools give surface content for accounts you don't.

## Trust & verifiability
`trust: unverified` — a small third-party analytics service. The numbers originate from Meta's official API (so the underlying data is authoritative), but the operator has no independent reputation and the scope is limited to accounts you can authenticate as.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | threads-dashboard |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, username → social-profile, metadata-exif |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |

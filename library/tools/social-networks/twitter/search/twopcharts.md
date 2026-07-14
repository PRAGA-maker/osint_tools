---
id: twopcharts
name: Twopcharts
description: Use when you have an X/Twitter `username` and want account metadata and history (creation date, name-change history, activity stats) — returns account-lifecycle data, though coverage is degraded post-API-lockdown.
url: https://twopcharts.com/
category: social-networks
path:
- social-networks
- twitter
- search
bestFor: Checking an X account's age, name/handle history, and activity metrics — where data is still available.
selectorsIn:
- username
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free, no account. Much of the functionality relied on Twitter's open API and has broken or gone stale since X restricted access.
opsec: passive
opsecNote: You query a third-party analytics site, not X, so the target is not notified. Twopcharts logs your queries/IP; use a sock-puppet browser. Treat outputs as historical indicators, not real-time truth.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running independent Twitter analytics site. Reliable historically, but X's API lockdown means many metrics are frozen or unavailable — verify freshness before relying.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- xcancel-nitter-mirror
- truthnest
aliases:
- Twopcharts
- twopcharts.com
tags:
- twitter
- x
- account-history
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# Twopcharts

> An independent X/Twitter analytics site for account-lifecycle data — creation date, handle-change history, activity — with the caveat that much of it is degraded since X locked down its API.

## When to use
You have an X/Twitter `username` and want account context rather than the timeline: how old the account is, whether the handle/display name changed over time, follower/activity trends, and rankings. Useful for judging whether an account is established or newly-minted, and for spotting rename history that links a current handle to a former one. Because X restricted API access, expect partial or stale results — cross-check anything important.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://twopcharts.com/ in a sock-puppet browser.
2. Enter the target handle into the relevant account-lookup tool (account age, name history, activity).
3. Read what's returned, noting the "as-of" date — several modules are frozen at their last successful pull.
4. Pivot: read the live timeline via `[[xcancel-nitter-mirror]]`; for deeper behavioural analytics (where accessible) use `[[truthnest]]`.

## Inputs → Outputs
- **In:** `username` (X handle)
- **Out:** `social-profile` — account creation date, handle/name-change history, activity metrics/rankings
- **Empty/negative result looks like:** a module returns nothing or clearly stale figures — a symptom of X's API restrictions, not necessarily an inactive account.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — the target isn't alerted; the site sees your query, so sock-puppet it.
- **Degraded:** the single most important caveat — verify data freshness; treat metrics as historical indicators.

## Overlaps ("do both")
- Pairs with `[[xcancel-nitter-mirror]]` (live timeline) and `[[truthnest]]` (behavioural analytics) — Twopcharts adds the account-history/age angle those don't emphasise.

## Trust & verifiability
`trust: community` — a reputable long-running analytics site now hampered by X's API changes. Confirm any account-age/rename claim against a second source before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twopcharts |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

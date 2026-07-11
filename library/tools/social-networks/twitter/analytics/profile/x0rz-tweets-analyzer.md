---
id: x0rz-tweets-analyzer
name: X0rz Tweets_analyzer
description: Use when you have a Twitter/X `username` and want a behavioral/temporal profile — activity by hour/day, timezone, sources, top hashtags — returns social-profile and associate patterns.
url: https://github.com/x0rz/tweets_analyzer
category: social-networks
path:
- social-networks
- twitter
- analytics
- profile
bestFor: Building a behavioral fingerprint of a Twitter/X account — posting rhythm, likely timezone/hours, client apps, and most-interacted accounts.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
status: degraded
pricing: free
costNote: Free and open source, but depends on the Twitter/X API — which now requires a paid developer tier for the timeline endpoints this tool uses. In practice it needs current API credentials/budget to run at all.
opsec: active
opsecNote: Collection runs through the Twitter/X API using your developer credentials — the API account/app is attributable and your usage pattern is visible to X. Use a dedicated sock-puppet developer account, never one linked to your identity. Reading a public timeline does not notify the target, but the API app is logged.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source tool by researcher x0rz (~3k stars), but built for the older Twitter API v1.1; its viability now hinges on X's current (paid, restrictive) API, so treat it as degraded.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
relatedTools:
- twint
- tinfoleak
aliases:
- tweets_analyzer
- x0rz tweets analyzer
tags:
- twitter
- analytics
- behavioral-profiling
- cli
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# X0rz Tweets_analyzer

> An open-source CLI that profiles a Twitter/X account's *behavior* — when it posts, likely timezone, which apps it uses, and who it interacts with — rather than just its content.

## When to use
You have a Twitter/X `username` and want a behavioral, not content, read: average activity by hour and weekday (which suggests the subject's real timezone and daily routine), device/app sources, most-used hashtags, and most-retweeted/mentioned accounts (`associate` leads). This is classic pattern-of-life analysis useful for narrowing location and identifying a subject's close network. **Caveat:** it was built for the Twitter API v1.1 and now depends on X's paid API, so expect it to need current credentials/budget and possibly fail on restricted endpoints.

## How to use it (`bestInteractionPattern`: cli)
1. Clone: `git clone https://github.com/x0rz/tweets_analyzer` and install dependencies (tweepy, numpy, tqdm; historically Python 2.7+).
2. Obtain Twitter/X API credentials on a **sock-puppet** developer account and put them in `secrets.py`.
3. Run: `python tweets_analyzer.py -n <target_username>` (add flags for friend/timezone analysis).
4. Read the output charts: activity by hour/day (timezone inference), language, app sources, top hashtags, and most-interacted accounts.
5. Pivot: inferred timezone/active-hours narrows geolocation; frequently-mentioned accounts are `associate` leads to profile next.

## Inputs → Outputs
- **In:** Twitter/X `username` (+ your API credentials)
- **Out:** `social-profile` behavioral summary (activity heatmap, timezone/language, app sources, top hashtags), `associate` patterns (most-retweeted/mentioned users)
- **Empty/negative result looks like:** API auth error, rate-limit, or "user not found / protected" — with X's API changes this is now common; a failure is often an API-tier limitation, not a real negative about the account.

## Gotchas & OpSec
- **API dependency is the main risk:** the tool targets the deprecated v1.1 API; on X's current paid API it may need a funded tier or may not run — verify before relying on it.
- Behavioral inferences (timezone from posting hours) are probabilistic — scheduled tweets and travel skew them; corroborate before treating as location fact.
- Human-in-the-loop: requires API keys; keep them on a burner developer account.
- OpSec: **active** — collection is attributable to your API app.

## Overlaps ("do both")
- Pairs with content/collection tools like [[twint]] (scrape-based, no-API history — itself fragile under X changes) and [[tinfoleak]] (broader Twitter intel incl. geodata) — combine behavioral timing here with content/geo from those.

## Trust & verifiability
`trust: community` — a well-regarded open-source researcher tool, but aging against X's API changes (hence `status: degraded`). Its raw inputs (tweets) are authoritative when the API returns them; the behavioral *inferences* are analytic estimates to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | x0rz-tweets-analyzer |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key) |

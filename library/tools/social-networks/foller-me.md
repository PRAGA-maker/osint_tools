---
id: foller-me
name: Foller.me
description: Use when you have a Twitter/X `username` and want a quick public-profile analytics snapshot — returns metadata, topics/hashtags, and activity patterns (a social-profile behavioural picture).
url: http://foller.me
category: social-networks
path:
- social-networks
bestFor: A fast public analytics snapshot of a Twitter/X account — topics, mentions, and posting rhythm.
selectorsIn:
- username
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free, no account. Coverage is constrained by X's API restrictions since 2023, so results can be partial or fail on some accounts.
opsec: passive
opsecNote: Foller.me queries public profile data server-side; the account owner is not notified and nothing comes from your IP. Only public accounts are analysable. Avoid pasting handles you don't want logged by a third-party service.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running (since 2009) third-party Twitter analytics site. Reputable and durable, but subject to X API limits; treat derived figures as indicative, not exact.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Foller
tags:
- twitter
- x
- profile-analytics
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- foller-me-analytics
---

# Foller.me

> A free, long-running Twitter/X profile analyzer: paste a handle and get topics, hashtags, mentions, and posting-pattern analytics.

## When to use
You have a Twitter/X `username` and want a fast behavioural read on the account without scrolling the timeline yourself: what it talks about (word cloud, top hashtags/mentions), when it posts (activity by hour/day — useful for inferring timezone or spotting automation), and basic profile metadata. Good for characterising an account and finding pivot handles it frequently mentions.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to foller.me and enter the target `username` (no @ needed).
2. Read the generated report: profile/`metadata` (join date, timezone, follower/following ratio), a topics word cloud, top hashtags and @-mentions, a tweet-type breakdown, and activity-time charts.
3. Note the most-mentioned handles and hashtags — these are your pivots.
4. Pivot: frequently-mentioned @handles are `associate`/alt-account leads; posting-hour peaks suggest a timezone (`geolocation` hint); hashtags map interests/communities.

## Inputs → Outputs
- **In:** `username` (Twitter/X handle)
- **Out:** profile `metadata`, topics/hashtags/mentions, activity-time patterns — a behavioural `social-profile`
- **Empty/negative result looks like:** an error or empty report — the account is private, suspended, renamed, or blocked by X's API limits. A blank result is not evidence the account is inactive.

## Gotchas & OpSec
- X API restrictions since 2023 hobble many third-party analytics tools; expect partial data or occasional failures (hence `status: degraded`).
- Analytics are computed from a recent sample of public tweets, not the full history — treat counts as indicative.
- OpSec: passive; server-side query, no notification to the owner. Public accounts only.

## Overlaps ("do both")
- Pairs with other X-profile tools and username-search — Foller.me characterises behaviour and surfaces mentioned handles; a username tool resolves those handles across other platforms, and an archive tool preserves the actual posts.

## Trust & verifiability
`trust: community` — an established third-party analyzer, not an X endpoint. Its numbers are best-effort given API limits; corroborate anything important by viewing the profile directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | foller-me |
| category | social-networks |
| selectorsIn → selectorsOut | username → metadata, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

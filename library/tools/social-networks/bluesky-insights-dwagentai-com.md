---
id: bluesky-insights-dwagentai-com
name: Bluesky Insights
description: Use when you have a Bluesky `username`/handle and want follower-growth analytics and similar-account discovery — returns social-profile metrics and related accounts.
url: https://bluesky-insights.dwagentai.com/
category: social-networks
path:
- social-networks
bestFor: Quick, no-login analytics on a Bluesky handle — follower trends, growth velocity, and discovery of similar profiles.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- associate
- name
status: live
pricing: free
costNote: Free; no signup and the site states it stores no user data.
opsec: passive
opsecNote: It reads public Bluesky (AT Protocol) data and requires no login, so the subject is not notified. You do route the handle through a third-party host (dwagentai.com) that could log your queries — use a sock-puppet browser if the subject is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: An independent third-party analytics front-end over public Bluesky data; ownership is unverified, but the underlying data is Bluesky's open, public firehose.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- clearsky-app
- bsky-app
aliases:
- Bluesky Insights
- bsky insights
tags:
- bluesky
- BlueSky / BSky Related Sites
- analytics
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Bluesky Insights

> A no-login analytics window on a Bluesky account: follower trends, growth velocity, and a "similar accounts" panel for pivoting to associates.

## When to use
You have a subject's Bluesky handle and want a fast read on the account beyond its raw profile — how its following is trending, and which other accounts are similar/related (a lead toward `associate`s and community). Useful for sizing up a Bluesky presence and finding adjacent accounts to investigate.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://bluesky-insights.dwagentai.com/.
2. Enter the subject's Bluesky `username` (the handle, without the `.bsky.social` suffix).
3. Read the generated report: follower count and growth over time, growth velocity/trends, milestone progress, and a "similar accounts" / discovery panel.
4. Note the similar profiles surfaced — these are candidate `associate`s or same-community accounts to pivot into.
5. Pivot: confirmed handles feed `[[clearsky-app]]` (block/relationship data) and direct viewing on `[[bsky-app]]`; the display `name`/bio feeds cross-platform username searches.

## Inputs → Outputs
- **In:** `username` (Bluesky handle).
- **Out:** `social-profile` metrics (followers, growth trend, velocity) and a list of similar/related accounts (`associate` leads) plus display `name`.
- **Empty/negative result looks like:** no report or an error — the handle is mistyped, the account is brand-new (no trend data), or the account doesn't exist. Thin metrics on a new account are not the same as an inactive person.

## Gotchas & OpSec
- The tool is growth/marketing-oriented (it even tracks "revenue" goals), so treat the follower-analytics framing loosely — for investigations the useful outputs are the profile confirmation and similar-account discovery.
- It relies on public AT Protocol data; private/limited signals aren't available, and Bluesky handles can change (the underlying DID is the stable identifier).
- Third-party host may log your lookups; use a sock puppet for sensitive targets.

## Overlaps ("do both")
- Pairs with `[[clearsky-app]]` — ClearSky exposes block lists and relationship data on Bluesky that pure analytics tools don't; run both to combine growth/discovery signals with relationship mapping. View the account itself on `[[bsky-app]]`.

## Trust & verifiability
`trust: unverified` — an independent front-end of unknown ownership over Bluesky's public data. The numbers derive from public AT Protocol records, so they're checkable, but corroborate the account and any "similar accounts" directly on Bluesky before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bluesky-insights-dwagentai-com |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, associate, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

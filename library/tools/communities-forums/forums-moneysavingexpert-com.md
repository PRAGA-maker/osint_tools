---
id: forums-moneysavingexpert-com
name: forums.moneysavingexpert.com
description: Use when you have a `username` and want to check whether it maps to a member on Britain's largest consumer-finance forum — returns a `social-profile` plus posting history.
url: https://forums.moneysavingexpert.com/
category: communities-forums
path:
- communities-forums
bestFor: Pivoting a UK-flavoured handle to a public forum profile and its self-disclosed post history on money and life topics.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free to read and search; a free account is only needed to post, not to view profiles or posts.
opsec: passive
opsecNote: Browsing public profiles and posts is read-only and does not notify the member. Do NOT register or send a private message from a real account — use a sock puppet if you must log in. Members frequently disclose location, employer, debts and family events in posts, so treat the content as sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large, long-running UK consumer forum (part of MoneySavingExpert / Moneysupermarket). Content is user-generated and unverified, but profiles and post timestamps are authentic.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- MoneySavingExpert forum
- MSE forum
tags:
- forums
- Forums
- uk
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# forums.moneysavingexpert.com

> The discussion board of MoneySavingExpert — one of the UK's busiest consumer forums — usable as a username-to-profile oracle with a rich, self-disclosed post trail.

## When to use
You have a `username` (or a distinctive handle a UK subject reuses) and want to confirm a `social-profile` on a mainstream British forum and read what they have posted. MSE members discuss debt, benefits, house moves, jobs, relationships and family circumstances in candid detail, so a matched profile can corroborate location, employment and life-event timelines that matter in a missing-persons or background context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://forums.moneysavingexpert.com/ in a clean/sock-puppet browser.
2. Try the direct profile path `https://forums.moneysavingexpert.com/profile/<username>`, or use the forum search box for the handle plus any distinctive phrases.
3. If a profile loads, read the "About", join date, post count and the visible post/comment history.
4. Confirm identity from self-disclosed details (region, occupation, other handles) rather than the name alone — handles are not unique across the internet.
5. Pivot: reused handles feed [[whatsmyname-app]] / other username sweeps; disclosed facts feed name and location searches.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` (forum profile URL), `username` corroboration, self-disclosed biographical detail in posts
- **Empty/negative result looks like:** the profile URL 404s or search returns no posts by that handle — the handle is not used here, which is not evidence about any other site.

## Gotchas & OpSec
- Human-in-the-loop: none for reading; posting or messaging requires a free account (do not use a real one).
- OpSec: **passive** for read-only browsing — it leaks nothing to the member. Registering or PM-ing would expose you; avoid it.
- Members can hide some profile fields; a thin profile does not disprove a match.

## Overlaps ("do both")
- Pairs with [[whatsmyname-app]] because a hit here confirms a handle you can then sweep across hundreds of other sites.

## Trust & verifiability
`trust: community` — a large, reputable UK forum; the platform is genuine but individual posts are unverified user claims, so treat disclosed facts as leads to corroborate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | forums-moneysavingexpert-com |
| category | communities-forums |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

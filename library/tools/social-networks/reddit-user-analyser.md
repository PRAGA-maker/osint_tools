---
id: reddit-user-analyser
name: Reddit User Analyser
description: Use when you have a Reddit `username` and want a fast behavioural profile — returns activity stats, top subreddits, posting-time patterns and controversiality (`social-profile` enrichment).
url: https://atomiks.github.io/reddit-user-analyser/
category: social-networks
path:
- social-networks
bestFor: One-click behavioural and interest profile of a Reddit account from its public history.
selectorsIn:
- username
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free, open-source, browser-based. No account or API key needed; it reads Reddit's public JSON API client-side.
opsec: passive
opsecNote: The lookup runs in your browser against Reddit's public API for the target's account — it does not notify the user, follow, or message them. No Reddit login is used. Standard passive recon; the target sees nothing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source project by developer "atomiks" (source on GitHub). It only reformats data Reddit already exposes publicly, so results are as accurate as the account's public history.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- redective
- reddit-com
aliases:
- reddit user analyzer
- reddit-user-analyser.netlify.app
tags:
- reddit
- behavioral-analysis
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Reddit User Analyser

> Paste a Reddit username and get an instant dashboard of that account's activity, favourite subreddits, and daily/weekly posting rhythm — all from public data.

## When to use
You have a Reddit `username` (from a breach, a cross-platform username match, or a lead) and want to understand the person behind it without reading thousands of comments by hand. The subreddit breakdown reveals interests, locale (city/regional subs), employer or hobby communities, and life circumstances; the posting-time histogram hints at time zone and daily routine — both useful for corroborating identity or narrowing location in a missing-person workup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://atomiks.github.io/reddit-user-analyser/ (mirror: reddit-user-analyser.netlify.app).
2. Type the target `username` (no `u/` prefix) and submit.
3. Read the output: total post/comment karma, account age, most-active subreddits, top posts/comments, controversiality, and a chart of activity by hour/day.
4. Note the local subreddits and the posting-time distribution — cluster them for a likely time zone and area of interest.
5. Pivot: local-subreddit + time-zone estimate feeds `geolocation` reasoning; interest subs feed identity corroboration; run the same `username` through other username tools and `[[redective]]`.

## Inputs → Outputs
- **In:** `username` (a Reddit account name)
- **Out:** `social-profile` enrichment — karma, account age, subreddit distribution, top content, controversiality, posting-time pattern (a weak `geolocation`/time-zone signal)
- **Empty/negative result looks like:** an error or empty dashboard — the account is suspended, deleted, shadowbanned, private, or the username is wrong/typo'd. It does not mean the person is inactive elsewhere.

## Gotchas & OpSec
- Human-in-the-loop: none; fully automated in the browser.
- OpSec: **passive** — no login, no interaction with the target's account, nothing logged to them. It only sees the public window Reddit's API exposes (recent items, typically last ~1000), so heavy accounts are truncated.
- Posting-time → time-zone inference assumes the user posts on their local schedule; treat it as a lead, not proof.

## Overlaps ("do both")
- Pairs with `[[redective]]` and `[[reddit-com]]` native search — the analyser is fastest for the aggregate behavioural picture, while Redective/native search let you pull specific comments and full text the analyser summarises away.

## Trust & verifiability
`trust: community` — an open-source hobby tool that only reshapes Reddit's own public API output. Reliable as a summariser; always spot-check the underlying posts before treating a subreddit or time pattern as identifying.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reddit-user-analyser |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

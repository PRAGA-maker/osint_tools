---
id: socialgrep
name: SocialGrep
description: Use when you have a `username`, keyword, or subreddit and want to find and export a subject's Reddit posts/comments across 2010–present — returns matching posts, comment history, and links to `social-profile`s.
url: https://www.socialgrep.com/search
category: social-networks
path:
- social-networks
bestFor: Historical, filterable Reddit search — surfacing a person's Reddit activity by author, keyword, or subreddit and exporting it.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: freemium
costNote: Free search with a limited sample and a free export sample (no card). Full exports/alerts/API are paid, roughly $9–$49/month depending on volume.
opsec: passive
opsecNote: You query SocialGrep's own aggregated index, not Reddit directly, so the subject gets no notification and your Reddit account is not exposed. Searching is passive; only creating an account for exports leaves a trace with SocialGrep.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial product by Lexyr Inc. that indexes Reddit's public firehose; data is real Reddit content, but coverage/recency depend on their crawl and paid tier.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
aliases:
- SocialGrep Reddit search
- Lexyr SocialGrep
tags:
- reddit
- social-media-search
- Social Media
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# SocialGrep

> Advanced, historical Reddit search: find a person's posts and comments by author, keyword, or subreddit going back to 2010 — and export the matches.

## When to use
You have a Reddit `username` (or a distinctive phrase, handle, or subreddit a subject frequents) and want their full public Reddit footprint in one place. Reddit's own search is shallow and can't pull a complete author history; SocialGrep indexes the firehose and lets you filter by author, keyword, subreddit, date, score, and linked domains — ideal for reconstructing what someone posted, when, and where, or for finding fresh accounts that reuse a known username.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.socialgrep.com/search.
2. Enter the target Reddit `username` in the author filter, or a keyword/phrase in the query box; narrow with subreddit, date range, minimum score, or domain filters.
3. Read the results feed — matching posts/comments with permalinks. Click through to the live Reddit thread to confirm the content still exists.
4. To pull the whole set, use SocialGrep Exports (Excel/JSON) — a free sample is available; large exports require a paid tier. SocialGrep Alerts can email/Slack you on new matches for ongoing monitoring.
5. Pivot: a confirmed profile feeds username-reuse checks across other platforms and cross-references linked domains/handles.

## Inputs → Outputs
- **In:** `username` (author), or a keyword/subreddit selector.
- **Out:** Reddit posts/comments (permalinks), an author's activity timeline, `social-profile` links, reused `username`s.
- **Empty/negative result looks like:** no posts for the author (deleted/shadowbanned account or a name that was never on Reddit) — absence here is not proof the person never used Reddit.

## Gotchas & OpSec
- Deleted/removed content: SocialGrep may retain items Reddit has since removed, but the reverse also happens — always click through to verify current state.
- The free tier caps results and export size; treat the sample as a lead, not a complete history, unless you pay for a full export.
- Passive: you are not touching the subject's account and Reddit is not queried under your identity.

## Overlaps ("do both")
- Complements direct Reddit username lookups — SocialGrep adds historical depth and structured export that Reddit's native search lacks.
- Feed confirmed handles into cross-platform username tools to find matching accounts elsewhere.

## Trust & verifiability
`trust: community` — a commercial aggregator (Lexyr Inc.) over genuine public Reddit data. The content is real; completeness depends on their crawl coverage and your subscription tier, so verify key items against live Reddit.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | socialgrep |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

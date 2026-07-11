---
id: universal-scammer-list
name: Universal Scammer List (USL)
description: Use when you have a Reddit `username` and want to check whether it appears on the community-maintained cross-subreddit scammer/banned list — returns a reputation flag and associated report context.
url: https://universalscammerlist.com/
category: social-networks
path:
- social-networks
bestFor: Checking a Reddit username against a community-compiled list of known scammers across trading/marketplace subreddits.
selectorsIn:
- username
selectorsOut:
- username
- social-profile
status: live
pricing: free
costNote: Free community tool; no account needed to search.
opsec: passive
opsecNote: Searching the list is passive and does not notify the user — you are querying a public database, not contacting the subject. No login to search.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-maintained aggregation of scammer tags from participating trading/marketplace subreddits; entries are moderator-submitted, so a listing is a strong community signal but not a legal or verified finding.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- USL
- universalscammerlist.com
tags:
- reddit
- reputation
- scammer-list
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Universal Scammer List (USL)

> A searchable, community-compiled blacklist of Reddit scammers — enter a username to see whether it's been tagged as a scammer across participating trading and marketplace subreddits.

## When to use
You have a Reddit `username` and want a fast reputation/trust check: has this account been flagged for scamming in the Reddit trading community? Useful for due diligence on a Reddit counterparty and for adding adverse-reputation context to a subject who is active in Reddit marketplaces.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://universalscammerlist.com/ (let the database load).
2. Enter the target Reddit username in the search box.
3. Read the result: whether the username is listed, and — where shown — the tag/reason and which participating subreddits flagged it.
4. Pivot: a listing is a lead to the originating report thread; confirm the underlying evidence there. Combine with the account's public Reddit history and cross-platform username checks.

## Inputs → Outputs
- **In:** Reddit `username`
- **Out:** listed/not-listed reputation flag, tag/report context, and the `social-profile` (Reddit account) it refers to
- **Empty/negative result looks like:** "not found" — the username isn't on the list, which is NOT proof of trustworthiness (new or renamed scammers won't be listed). A listing, conversely, is a community allegation, not a verified conviction.

## Gotchas & OpSec
- **Community allegations, not verdicts:** entries are moderator-submitted from participating subreddits — treat a hit as a strong lead to investigate, not proof, and a non-hit as unknown, not clean.
- Scope is Reddit trading/marketplace communities; it says nothing about behavior off Reddit.
- Usernames are cheap to change — a clean result on a fresh handle means little.
- OpSec: passive; no contact with the subject.

## Overlaps ("do both")
- Pairs with the subject's raw Reddit history (`[[reddit-search-tool]]`-style) and cross-platform username enumeration (`[[aliens-eye]]`) — USL gives the reputation flag; those give the behavior and footprint behind it.

## Trust & verifiability
`trust: community` — a legitimate, well-known community resource. Its signal is real but non-authoritative; always follow a listing back to its source report thread before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | universal-scammer-list |
| category | social-networks |
| selectorsIn → selectorsOut | username → username, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

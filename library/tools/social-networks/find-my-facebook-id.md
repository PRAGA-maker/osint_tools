---
id: find-my-facebook-id
name: Find my Facebook ID
description: Use when you have a Facebook profile/page/group URL or vanity `username` and want its stable numeric ID — returns the numeric Facebook ID that powers graph-search pivots.
url: https://randomtools.io
category: social-networks
path:
- social-networks
bestFor: Converting a Facebook vanity URL/username into the persistent numeric user/page/group ID.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free with no usage limits; no account required. Works across profiles, pages, and groups.
opsec: passive
opsecNote: The tool resolves a public URL to its numeric ID via Facebook's own metadata — you do not interact with the subject or their account, and no notification is sent. Do the resolution from a clean session; the ID itself is public.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A free third-party utility; it performs a mechanical lookup of the numeric ID, which is verifiable, but the site itself is a general "random tools" host.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Facebook ID finder
- lookup-id
- randomtools.io Facebook ID
tags:
- facebook
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- reddit-comment-lookup
---

# Find my Facebook ID

> Turns a Facebook vanity URL or username into its numeric ID — the stable key that unlocks graph-search and survives username changes.

## When to use
You have a Facebook profile, page, or group `URL`/vanity `username` and need its numeric ID. The numeric ID is what Facebook graph-search tools and many OSINT techniques actually require, and — crucially — it stays constant even if the subject changes their vanity name, so capturing it early anchors the account. Essential prep before running graph-based Facebook queries.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://randomtools.io and open the "Find your Facebook ID" tool.
2. Paste the Facebook `URL` (profile, page, or group — vanity or numeric form).
3. Read the returned numeric ID (`social-profile` identifier).
4. Record the numeric ID alongside the vanity handle so the account remains trackable if the handle changes.
5. Pivot: feed the numeric ID into `[[graph-tips]]`/graph-search URLs to enumerate photos, likes, friends signals, and tagged content.

## Inputs → Outputs
- **In:** Facebook profile/page/group `URL` or vanity `username`
- **Out:** the numeric Facebook ID (a persistent `social-profile` identifier)
- **Empty/negative result looks like:** no ID returned — usually a malformed URL, a deleted/renamed account, or a profile whose privacy prevents resolution. A failure here means the account can't be resolved, not that graph pivots are impossible via other means.

## Gotchas & OpSec
- Facebook has curtailed much of graph search over the years; the numeric ID is still useful but some downstream graph queries no longer work as they once did.
- If one resolver fails, try alternate Facebook-ID finders — they use similar public-metadata methods with varying reliability.
- The ID is public; capturing it is passive and safe.

## Overlaps ("do both")
- Pairs with `[[graph-tips]]` and other Facebook graph-search tools — this supplies the numeric ID they need, and they turn it into enumerable photos/connections/tags.

## Trust & verifiability
`trust: community` — a mechanical, verifiable lookup (you can confirm the ID resolves back to the same profile); the hosting site is a general utilities page, so use it just for this conversion.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | find-my-facebook-id |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

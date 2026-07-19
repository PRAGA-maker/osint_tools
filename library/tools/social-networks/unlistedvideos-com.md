---
id: unlistedvideos-com
name: Unlistedvideos.com
description: Use when you want to discover unlisted YouTube videos (not shown in search or on a channel) — returns a crowd-submitted, searchable index of otherwise-hidden public videos.
url: https://unlistedvideos.com/
category: social-networks
path:
- social-networks
bestFor: Finding "unlisted" YouTube videos — publicly viewable but hidden from search/channel listings — via a crowdsourced, no-login index.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free, no registration required to browse, search, or submit.
opsec: passive
opsecNote: Browsing is passive and touches only this third-party index, not YouTube's account systems — the video owner gets no signal. Watching the underlying YouTube video does count a view but doesn't identify you. Use a sock-puppet browser for separation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A small crowdsourced directory; it only contains videos users have submitted, so coverage is partial and it excludes content unlisted for privacy — treat it as a lucky-dip supplement, not a comprehensive index.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Unlisted Videos
tags:
- youtube
- unlisted-content
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# Unlistedvideos.com

> A crowdsourced, no-login index of *unlisted* YouTube videos — content that's publicly viewable via direct link but hidden from YouTube search and channel pages.

## When to use
You're investigating a subject's or organisation's YouTube presence and suspect there's content beyond what their channel shows publicly. Unlisted videos don't appear in YouTube search or on the channel listing, so this crowd-submitted index is one way to stumble onto unlisted uploads (tutorials, event recordings, drafts left public-by-link) that others have found and submitted.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://unlistedvideos.com/ and use its search, or browse "all"/"random".
2. Search by keyword, channel name, or `username` if the index supports it; also try a search engine `site:unlistedvideos.com "<term>"`.
3. Open matching entries and view the underlying YouTube video for content, captions, and description leads.
4. Because the index is partial, treat a miss as "not submitted here", not "doesn't exist".
5. Pivot: an unlisted video's uploader/channel is a `social-profile` lead; on-screen content and metadata feed `geolocation` and timeline analysis.

## Inputs → Outputs
- **In:** `username`/channel or keyword tied to a `social-profile`
- **Out:** links to unlisted YouTube videos → uploader `social-profile`, and any `geolocation`/context visible in the footage
- **Empty/negative result looks like:** no matching submissions — the crowdsourced index simply hasn't captured content for your subject (the common case). It is not a complete unlisted-video database.

## Gotchas & OpSec
- Coverage is thin and submission-dependent; it deliberately excludes videos unlisted for privacy reasons.
- Viewing the YouTube video registers a view but does not reveal your identity to the owner.
- OpSec: passive; use a sock-puppet browser/YouTube session for separation.

## Overlaps ("do both")
- Pairs with direct YouTube channel analysis and video-metadata tools — this surfaces hidden uploads, while those extract upload dates, geotags, and comment networks from whatever videos you find.

## Trust & verifiability
`trust: unverified` — a small community index with no completeness guarantee; anything found is real YouTube content (verifiable by opening it), but absence proves nothing about what a subject has unlisted.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | unlistedvideos-com |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → social-profile, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

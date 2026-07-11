---
id: commentpicker-com
name: Comment Picker
description: Use when you have an Instagram/Facebook/TikTok/YouTube `username` or post and want the account's stable numeric ID or the list of commenters — returns the numeric profile ID and commenter/liker handles.
url: https://commentpicker.com/instagram-username.php
category: social-networks
path:
- social-networks
bestFor: Resolving a social handle to its permanent numeric ID, and pulling the commenters under a public post as an associate list.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
- associate
- username
status: live
pricing: freemium
costNote: The ID-finder and giveaway/comment tools are free with no registration; an optional Premium ($9.99/mo) removes ads. The free tier is enough for OSINT lookups.
opsec: passive
opsecNote: Comment Picker's servers query the public APIs, so the lookups run from their infrastructure, not your IP, and leave no trace on the subject. It does see the handles/URLs you submit — use a clean session and avoid pasting sensitive targets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An established (since 2015) commercial giveaway-tools site; the ID-finder relies on platform APIs that change, so treat results as convenience lookups to confirm at source.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- commentpicker.com
- Instagram User ID Finder
tags:
- instagram
- Instagram Related Sites
- id-finder
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Comment Picker

> A free toolbox best known for giveaways, but quietly useful in OSINT for two things: turning a handle into its permanent numeric ID, and listing everyone who commented on a public post.

## When to use
Two cases. (1) You have a `username` on Instagram/Facebook/TikTok/YouTube and want its numeric account ID — the stable identifier that survives username changes and anchors the account across tools. (2) You have a public post and want the commenters as an `associate` list (Comment Picker was built to scrape post comments for prize draws). Reach for it to de-alias a handle or to enumerate who engaged with a post.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to commentpicker.com and pick the tool: Instagram User ID Finder / Facebook ID Finder / TikTok / YouTube Channel ID Finder, or a comment-picker for a platform.
2. For an ID lookup, enter the `username`; it returns the numeric profile/channel ID.
3. For commenters, paste the public post URL and run the picker; export the list of commenter handles.
4. Cross-check a sample against the live post/profile to confirm the API result is current.
5. Pivot: the numeric ID feeds `[[toutatis]]` and other ID-keyed tools; the commenter list feeds associate mapping in `[[maltego]]`.

## Inputs → Outputs
- **In:** `username` / a public post `social-profile` URL
- **Out:** numeric account/channel ID (`social-profile`), commenter/liker `username`/`associate` lists
- **Empty/negative result looks like:** ID lookup returns nothing (handle misspelled, account private/deleted, or the platform API changed), or the comment tool returns an empty set (comments disabled/removed or the post is private).

## Gotchas & OpSec
- API drift: these tools ride platform APIs that break periodically — a failure may be the tool, not a missing account.
- Public only: comment scraping covers public posts; it is not an access bypass.
- OpSec: passive — Comment Picker fetches on your behalf.

## Overlaps ("do both")
- Pairs with `[[toutatis]]` — Comment Picker gives the numeric Instagram ID; Toutatis uses it to extract hidden contact data.
- Pairs with `[[facebook-latest-comments-scraper]]` — different engines for the same "who commented" question; cross-check coverage.

## Trust & verifiability
`trust: community` — a legitimate commercial tool; results are convenience lookups against platform APIs, so confirm any critical ID/handle against the live profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | commentpicker-com |

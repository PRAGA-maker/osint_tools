---
id: facebook-watch
name: Facebook Watch
description: Use when you have a `name`/`username` or page and want to find video content that person or page has posted or appears in on Facebook — returns social-profile video content.
url: https://www.facebook.com/watch/
category: social-networks
path:
- social-networks
bestFor: Surfacing a subject's or page's Facebook video uploads and shows, and video mentions, via Facebook's video hub.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- image
status: live
pricing: free
costNote: Free. Browsing/searching video increasingly requires a logged-in Facebook account; without login you hit walls quickly.
opsec: active
opsecNote: Practical use needs a Facebook login, so use a well-worn sock account, never your own. Views themselves aren't shown to the target, but likes/comments/follows from your session are. Stay read-only.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Facebook surface; the content is genuine platform data. Reliability of discovery depends on Facebook's search, which is inconsistent.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- facebook-directory-users-by-name
aliases:
- fb watch
- facebook.com/watch
tags:
- toddington
- curated-directory
- social-media
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# Facebook Watch

> Facebook's video hub — a way to find the video a subject or page has posted or been tagged in, complementing text/profile search.

## When to use
You have a subject's `name`, `username`, or Facebook page and want their **video** footprint specifically: uploads, live streams, and shows, plus videos that mention or tag them. Video often reveals what a static profile hides — locations, associates, vehicles, physical description, and dates in the background — so Watch is a strong step once you've confirmed a Facebook identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a **sock** Facebook account and open https://www.facebook.com/watch/.
2. Use the search field for the subject's name/handle, or open their profile/page and go to its Videos tab.
3. Filter/scan results for videos posted by or featuring the subject; open each and note background detail (location, people, timestamps).
4. Read the output: a set of videos (`social-profile` content) with thumbnails (`image`) you can frame-grab for further analysis.
5. Pivot: faces/vehicles/locations in frames feed reverse-image, geolocation, and vehicle tools; tagged accounts feed `associate` mapping.

## Inputs → Outputs
- **In:** `name` or `username`/page
- **Out:** `social-profile` (video posts, live streams), `image` (thumbnails/frames)
- **Empty/negative result looks like:** no videos surface — either the subject posts no video, their content is friends-only, or Facebook's search simply isn't returning it. Absence isn't conclusive.

## Gotchas & OpSec
- Human-in-the-loop: a Facebook login is effectively required; logged-out browsing is heavily walled.
- Facebook's video search is unreliable — cross-check by going through the profile's Videos tab directly.
- OpSec: **active** and account-bound — keep the sock session read-only; any reaction/comment is attributable.

## Overlaps ("do both")
- Pairs with [[facebook-directory-users-by-name]] — the directory finds the profile, Watch mines that profile's video output. Run both to cover text and video footprints.

## Trust & verifiability
`trust: trusted` — first-party Facebook content, so what you see is genuine. The caveat is discovery completeness (Facebook's search), not authenticity; confirm by opening the source profile/page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-watch |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |

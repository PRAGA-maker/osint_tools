---
id: search-fotki-com
name: Fotki Profile Search
description: Use when you have a `username` or `name` and want to find a profile on Fotki, a long-running photo-sharing community — returns social-profile, photos, and name.
url: http://search.fotki.com/?search_type=profiles
category: image-video-face
path:
- image-video-face
bestFor: Searching the veteran Fotki photo-sharing community for a member's profile and their uploaded photo albums.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
- name
status: degraded
pricing: free
costNote: Free to search and view public Fotki profiles/albums. Fotki has been running since 1998 and skews toward RU/US photo hobbyists; the search now sits behind an anti-bot interstitial, so a real browser is needed.
opsec: passive
opsecNote: Browsing public profiles and albums is passive and does not notify the member. The anti-bot layer means you should use a normal browser (not a scraper); use a sock-puppet browser/IP if you don't want the session tied to you.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: unverified
trustNote: Fotki is a genuine, long-established photo-sharing site, but a niche one; account data is user-generated and the profile-search feature is gated behind anti-bot checks. Verify any identity match against the actual albums.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- flickr-com
aliases:
- fotki.com
- Fotki profile search
tags:
- flickr
- Flickr & Similar Linked Sites
- photo-sharing
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Fotki Profile Search

> A search into Fotki — a photo-sharing community that predates Instagram (since 1998, big with RU/US hobbyists) — where an older subject may have albums that reveal faces, places and dates.

## When to use
You have a `username` or `name` and suspect the subject is a photo hobbyist, or you're doing exhaustive coverage of an older online footprint. Fotki members maintain public albums, so a hit can yield the person's photos (`image`s of them and their surroundings), a real `name`, and a durable `social-profile` from the pre-Instagram era.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://search.fotki.com/?search_type=profiles in a real (sock-puppet) browser — a scripted fetch hits an anti-bot wall.
2. Clear the anti-bot interstitial if shown, then search by username or name.
3. Open matching profiles and browse their public albums.
4. Read albums for faces, locations (backgrounds, captions) and dates.
5. Pivot: a reused username feeds cross-platform enumeration; a face in an album feeds reverse-image/face search.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile` (Fotki profile), `image` (album photos), `name`
- **Empty/negative result looks like:** no profile match, or being stuck at the anti-bot page — retry in a genuine browser before concluding the person isn't there; Fotki is niche, so absence is weak evidence.

## Gotchas & OpSec
- Human-in-the-loop: the search sits behind an anti-bot interstitial — use a real browser, not automation.
- Niche and older platform; strongest for RU/US hobbyist photographers, thin elsewhere.
- OpSec: passive; the member isn't notified of profile/album views.

## Overlaps ("do both")
- Pairs with Flickr and other photo-community searches — coverage differs, so an absent Flickr subject may surface on Fotki.
- Feed any album photo into reverse-image/face tools to connect the same person across sites.

## Trust & verifiability
`trust: unverified` — a real but niche community with user-generated content behind anti-bot gating; treat a match as a lead and confirm via the actual albums.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-fotki-com |
| category | image-video-face |
| selectorsIn → selectorsOut | username, name → social-profile, image, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |

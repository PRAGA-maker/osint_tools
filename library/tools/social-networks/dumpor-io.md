---
id: dumpor-io
name: dumpor.io
description: Use when you have an Instagram `username` and want to view/download that public profile's posts, stories, reels and follower lists without logging in — returns social-profile content, images and associate links.
url: https://dumpor.io/
category: social-networks
path:
- social-networks
bestFor: Anonymously browsing and downloading a public Instagram target's stories, reels, tagged posts and follower/following lists.
selectorsIn:
- username
selectorsOut:
- social-profile
- image
- associate
status: live
pricing: free
costNote: Fully free, no account or payment; supported by ads. Only works on public Instagram accounts.
opsec: passive
opsecNote: You never log in and Dumpor routes requests through its own proxies, so Instagram sees Dumpor's IP, not yours, and the target gets no story-view notification. Dumpor itself is a third party that logs which usernames you look up, so use it from a sock-puppet browser and assume it can see your queries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Anonymous third-party Instagram scraper of unknown ownership; treat what it shows as an unauthenticated mirror of public IG data, not an authoritative source, and re-confirm anything critical against Instagram directly.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- otzberg-net-find-your-instagram-user-id
aliases:
- Dumpor
- Instagram anonymous viewer
tags:
- instagram
- Instagram Related Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# dumpor.io

> Anonymous, no-login viewer/downloader for public Instagram profiles, stories, reels, highlights, tagged posts and follower lists.

## When to use
You have a target's Instagram `username` (or found it via another pivot) and want to review and archive what they post — including ephemeral stories that vanish in 24h — without following them, logging in, or tripping a "seen by" notification. Especially useful for capturing stories/highlights before they expire and for reading follower/following lists to map `associate` relationships.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://dumpor.io/ in a clean/sock-puppet browser.
2. Type the target's exact Instagram `username` into the search box (no `@`) and submit.
3. Pick a lens from the tabs — Profile, Stories, Story Downloader, Reels, Highlights, Tagged, or Followers/Following.
4. Read/download the output: HD story downloads, watermark-free reels, permanent highlight archives, tagged photos, and follower ratios. Screenshot or download anything time-sensitive immediately.
5. Pivot: follower/following names feed `associate` mapping; a profile photo feeds reverse-image search; the numeric account confirmation pairs with `[[otzberg-net-find-your-instagram-user-id]]`.

## Inputs → Outputs
- **In:** `username` (public Instagram account)
- **Out:** `social-profile` content (posts, stories, reels, highlights, bio), `image` downloads, `associate` links (followers/following)
- **Empty/negative result looks like:** "This account is private" or no content loads — Dumpor cannot see private accounts, and a missing profile may mean the username was renamed/deleted rather than that no such person exists.

## Gotchas & OpSec
- Only public accounts. Private profiles return nothing regardless.
- Third-party scrapers like this break often and lag behind Instagram; if it fails, retry later or fall back to a different viewer.
- OpSec: **passive** for you (proxied, no login), but Dumpor logs your lookups — never enter your own credentials, and prefer a throwaway browser session.

## Overlaps ("do both")
- Pairs with `[[otzberg-net-find-your-instagram-user-id]]` — that resolves a username to the stable numeric user ID (which survives handle changes), while Dumpor gives you the actual content and connections behind the handle.

## Trust & verifiability
`trust: unverified` — anonymous Instagram mirror with no accountable operator. The underlying data is real public Instagram content, but treat Dumpor as a convenience layer and corroborate key findings against Instagram itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dumpor-io |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, image, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

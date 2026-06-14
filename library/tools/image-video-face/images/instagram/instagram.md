---
id: instagram
name: Instagram
description: Use when you have a username, name, hashtag, or location and want photos, captions, location tags, and social connections — returns profiles, posts, and network/location context.
url: https://www.instagram.com/
category: image-video-face
path:
- image-video-face
- images
- instagram
bestFor: Profiling a subject through their (or associates') public photos, captions, tagged locations, and follower/following network.
input: Username, real name, hashtag, or location/place
output: Profile, public posts, tagged people/places, follower-following network
selectorsIn:
- username
- name
- geolocation
selectorsOut:
- image
- face
- social-profile
- associate
- geolocation
- employer-org
status: live
pricing: freemium
costNote: Free to use; a (free) account is required to view most profiles beyond a teaser, and to see followers/following.
opsec: active
opsecNote: Viewing logged-in is tied to your account and can trigger "viewed your story"/follow-suggestion leakage; the subject may be notified of follow/DM/story-view. Always use a hardened sock-puppet account, never your own.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: web-manual
trust: trusted
trustNote: Instagram is a mainstream Meta platform; the data is first-party but user-supplied and may be staged or stale.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags:
- social-media
- photos
source: arf-seed
lastVerified: ''
enrichment: full
---

# Instagram

> The dominant photo-sharing network — a primary source of a subject's recent images, captions, tagged locations, and social circle.

## When to use
You have a `username`, real `name`, a place, or a hashtag and want the subject's photos, who they associate with, where they check in, and timeline cues. Critical in missing-person work for: recent appearance, last-seen clothing/`physical-description`, frequented `geolocation`s, romantic/peer `associate`s, and `employer-org` from bio/tags.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a sock-puppet account (never personal). Search the `username` or `name`; also try the name in the search bar and via Google `site:instagram.com "<name>"`.
2. On the profile, read bio (links, `employer-org`, location), then posts: captions, location tags, tagged accounts, and comments.
3. Inspect followers/following and tagged-in photos for `associate`s; click through to their profiles for more context.
4. Pivot: tagged places feed your geolocation timeline; associates feed further social lookups; a profile image feeds reverse-face search like `[[in20years-co]]`-style tools and PimEyes-class engines.

## Inputs → Outputs
- **In:** `username`, `name`, `geolocation` (place), hashtag
- **Out:** `social-profile`, `image`/`face`, `associate`, `geolocation`, `employer-org`
- **Empty/negative result looks like:** private account (only bio + count visible), no results for the handle, or a dormant profile — none of which confirm absence; try name variants and tagged photos on associates' public accounts.

## Gotchas & OpSec
- Active-risk platform: stories show viewers, follows/DMs notify the subject, and Meta's "people you may know" can expose your sock puppet. Use a well-aged puppet, disable contact syncing, and avoid story views on the target.
- Aggressive rate-limiting and login walls; scraping triggers checkpoints/bans.
- Content is user-curated — assume images/locations can be staged, geotag-spoofed, or old.

## Overlaps ("do both")
- Pairs with cross-platform username search and reverse-image/face engines because the same photos and handle often surface other accounts and the original source.

## Trust & verifiability
`trust: trusted` (platform is first-party) but treat individual posts as unverified self-published claims; corroborate locations/timelines with metadata and other sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | instagram |
| category | image-video-face |
| selectorsIn → selectorsOut | username, name, geolocation → image, face, social-profile, associate, geolocation, employer-org |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login, rate-limit) |

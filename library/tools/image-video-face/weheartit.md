---
id: weheartit
name: We Heart It
description: Use when you have a `username` or `image` and want a subject's curated image collections and tastes on this Tumblr-style gallery site — returns social-profile and image leads.
url: http://weheartit.com
category: image-video-face
path:
- image-video-face
bestFor: Recovering a subject's saved-image collections, interests, and self-uploaded photos on the We Heart It gallery network (largely archival since 2023).
selectorsIn:
- username
- image
selectorsOut:
- social-profile
- image
status: degraded
pricing: free
costNote: Free to browse; note the platform removed new uploads in 2023 and now mainly serves browsing/downloading of existing collections, so content is increasingly historical.
opsec: passive
opsecNote: Browsing public collections sends nothing to the subject. Following/hearting from an account would be active — view logged-out or from a sock puppet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A once-large teen image-sharing network now in decline; profiles and collections are user-generated, so treat identities as self-asserted.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- WeHeartIt
- weheartit.com
tags:
- toddington
- curated-directory
- image-video-multimedia-search
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# We Heart It

> A Tumblr-style image-collection network — useful for recovering a subject's curated galleries, aesthetic interests, and older self-uploaded photos.

## When to use
You have a `username` (often reused from Tumblr/Instagram) or an `image` and want a subject's saved-image collections and self-posts on We Heart It. The value is behavioural/interest intelligence and reused handles — a person's "hearts" reveal tastes, fandoms, and sometimes personal photos. Skews to accounts from its 2012–2020 heyday, since new uploads were removed in 2023.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open weheartit.com and search the `username`, or browse image tags/collections.
2. Open the profile: their collections ("canvases"), hearted images, and any bio links.
3. Download images of interest for further analysis.
4. Pivot: a reused `username` feeds cross-platform enumeration; a self-uploaded photo feeds reverse-image/face search; bio links feed direct social-profile enrichment.

## Inputs → Outputs
- **In:** `username` or `image`
- **Out:** `social-profile` (collections, hearts, bio links), `image` (saved/uploaded photos)
- **Empty/negative result looks like:** no such user, or an empty/archived profile — expected, since the network has shrunk and uploads are frozen. Absence is uninformative.

## Gotchas & OpSec
- Platform is degraded: no new uploads since 2023, many accounts dormant or lost — treat everything as historical.
- Most images are curated/reposted, not personal — distinguish self-uploads from saved third-party images before drawing conclusions.
- OpSec: passive when browsing logged-out.

## Overlaps ("do both")
- Pairs with Tumblr/Pinterest profile search and reverse-image tools — the same handle and saved images often recur across these gallery platforms.

## Trust & verifiability
`trust: unverified` — user-generated content on a declining network; confirm any identity link (handle, photo) against a live platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | weheartit |
| category | image-video-face |
| selectorsIn → selectorsOut | username, image → social-profile, image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

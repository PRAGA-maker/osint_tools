---
id: bskyviewer-github-io
name: Bluesky Viewer
description: Use when you have a Bluesky `username`/handle and want to view a profile, posts, and threads without an account — returns social-profile content and post history.
url: https://bskyviewer.github.io/
category: social-networks
path:
- social-networks
bestFor: Reading a Bluesky profile and its posts anonymously, with no login and no footprint on the target.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
- image
status: live
pricing: free
costNote: Free, open-source, client-side viewer hosted on GitHub Pages. No account required.
opsec: passive
opsecNote: A browser-side viewer that reads Bluesky's public AT Protocol data — you never log in, never follow, and leave no trace on the target's account. Ideal when you want to read a Bluesky profile without your own (even sock-puppet) account appearing in their notifications.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-built front-end over Bluesky's public API; it only renders data Bluesky already exposes publicly, so accuracy tracks the platform.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- Bluesky Viewer
- bskyviewer.github.io
tags:
- bluesky
- BlueSky / BSky Related Sites
- no-login-viewer
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Bluesky Viewer

> Read any public Bluesky profile and its threads without logging in — a zero-footprint window onto the network.

## When to use
You have a Bluesky `username`/handle (or a display `name` to search) and want to read the profile, posts, replies, and threads **without** an account of your own showing up — even a sock puppet. Because it renders Bluesky's public AT Protocol data client-side, it's the safe way to review a subject's Bluesky activity when you want no interaction footprint at all.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open `https://bskyviewer.github.io/`.
2. Enter the target's handle (e.g. `alice.bsky.social` or a custom-domain handle) or search by name.
3. Browse the rendered profile: bio, avatar/banner (`image`), post and reply history, and thread context.
4. Read posts for content, timing, and location/context clues; note the handle's domain (a custom domain ties to a `domain` you can WHOIS).
5. Pivot: the avatar → reverse-image (`[[yandex-images]]`); the handle → cross-platform username search; the full graph → the main `[[bluesky]]` entry / public API.

## Inputs → Outputs
- **In:** `username`/handle, `name`
- **Out:** `social-profile`, `name`, `image`, post/thread content
- **Empty/negative result looks like:** the handle doesn't resolve, or a profile with no posts — no usable presence (or a renamed/squatted handle). Verify by content, since handles are mutable.

## Gotchas & OpSec
- It only shows what Bluesky already makes public — no private or deleted content.
- Handles change; the stable identifier is the account DID. Record it when identity matters.
- OpSec: **passive/zero-footprint** — no login, nothing sent to the subject; the safest way to read a Bluesky profile.

## Overlaps ("do both")
- Pairs with the main `[[bluesky]]` entry — this viewer is the anonymous read path; the public AT Protocol API behind Bluesky is the route for bulk graph/timeline extraction.

## Trust & verifiability
`trust: community` — a thin client-side renderer of Bluesky's own public data; it adds no data of its own, so accuracy simply mirrors the platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bskyviewer-github-io |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

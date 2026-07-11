---
id: bitchute-com
name: bitchute.com
description: Use when you have a `username` or `name` and want to find a subject's video presence on the alt-tech platform BitChute — returns channels, videos, and profile context.
url: https://www.bitchute.com/
category: social-networks
path:
- social-networks
bestFor: Locating a subject's channel and video activity on BitChute, an alt-tech video-sharing platform.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free to browse and search public channels/videos; an optional free account is needed only to comment or subscribe.
opsec: passive
opsecNote: Browsing and searching public channels does not notify the target. Creating an account or subscribing ties activity to you — use a sock-puppet if you need to interact. Content skews to fringe/extremist material; handle exposure and download of media carefully.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Genuine, well-known alt-tech video platform; profiles are self-authored so identity attribution needs corroboration, and much content is unmoderated.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
aliases:
- BitChute
tags:
- rightwingsocialmediasites
- Right Wing Social Media Sites
- video
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# bitchute.com

> A video-sharing platform popular in alt-tech / fringe communities — use it to check whether a subject who is absent from mainstream sites maintains a channel and video presence here.

## When to use
You have a `username` or `name` and reason to think a subject posts video content outside mainstream platforms (YouTube-banned creators, fringe-community members, conspiracy/extremist circles often mirror or migrate here). A BitChute channel yields self-published videos, a bio, links to other platforms, and a posting timeline — strong leads for identity, associates, and recent activity when the usual channels are silent.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.bitchute.com/ and use the search box for the subject's `username` or `name` (try known handles reused from other platforms first).
2. Scan channel and video results; open the candidate channel.
3. Read the channel: bio, external links, video list and dates, and comment activity. Note handles/links that cross to other platforms.
4. Pivot: reuse the handle in cross-platform username tools; run video thumbnails/stills through reverse-image/face tools; follow linked accounts.

## Inputs → Outputs
- **In:** `username` / `name`
- **Out:** `social-profile` (channel), `name`, plus videos, bio, external links, timeline
- **Empty/negative result looks like:** no channel or only unrelated videos — the subject may use a different handle or not be here; try handle variants and other alt-tech platforms before concluding absence.

## Gotchas & OpSec
- Human-in-the-loop: none to search; an account (sock puppet) is only needed to comment/subscribe.
- Content is largely **unmoderated and often extremist** — exercise care viewing/downloading, and keep clear investigative justification.
- Self-authored profiles: confirm identity with corroborating signals, not the display name alone.
- OpSec: passive when browsing; interaction ties activity to your account, so use a sock puppet.

## Overlaps ("do both")
- Pairs with cross-platform username tools and other alt-tech video/social sites — subjects deplatformed elsewhere often reuse the same handle here, so match handles across platforms.

## Trust & verifiability
`trust: community` — a real, established platform, but profiles are user-generated and unmoderated; use content as leads and verify identity independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bitchute-com |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

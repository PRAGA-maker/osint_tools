---
id: twitch-tv
name: Twitch
description: Use when you have a `username` and want a person's live-streaming presence — returns their channel, VODs/clips, chat activity and voice/face/location leaks from streams.
url: https://www.twitch.tv/
category: image-video-face
path:
- image-video-face
bestFor: Checking a handle on Twitch for a streaming profile, past broadcasts and clips that can leak face, voice, room/location and routine.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
- geolocation
status: live
pricing: free
costNote: Free to view channels, VODs and clips; an account is only needed to chat/follow, not to watch public content.
opsec: passive
opsecNote: Browsing a channel/VODs logged-out is passive. Don't follow, chat, or view while logged into an attributable account — that notifies the streamer and ties activity to you. Some streamers see viewer counts but not identities of logged-out viewers.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Twitch is a legitimate mainstream platform; content is authentic first-party streaming, though a handle matching your target must still be verified.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- whatsmyname-web
- google-reverse-image-search
aliases:
- twitch.tv
tags:
- toddington
- streaming
- gaming
- social-media
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Twitch

> A live-streaming platform (gaming and IRL) — a subject's channel and archived broadcasts can leak far more than social media: their face, voice, room interior, schedule, and offhand location mentions.

## When to use
You have a `username` (gaming handles often carry across platforms) or a `name`, and want to check for a Twitch presence. Streamers reveal a lot on camera and in chat over hours of unscripted content — appearance, voice, home interior, daily routine, local references, and links to other socials in the channel's "About" panel. VODs and clips are searchable archives of this. It's a high-value source when your subject is a gamer or IRL streamer.

## How to use it (`bestInteractionPattern`: web-manual)
1. Try the handle directly: `https://www.twitch.tv/<username>`; also search Twitch and Google `site:twitch.tv "<name>"`.
2. If a channel resolves, read the **About** panel for linked socials, then review **Videos** (VODs), **Clips**, and past titles.
3. Watch/skim clips for face, voice, room details and any spoken location/schedule leaks; note stream times (timezone hint).
4. Check chat/mod lists for `associate`s and community.
5. Pivot: linked socials and the same handle → `[[whatsmyname-web]]`; capture a stream still for `[[google-reverse-image-search]]`; room/window views → geolocation.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile` (channel + linked accounts), `image`/video (face, room), and `geolocation` leaks from stream content/mentions
- **Empty/negative result looks like:** no channel, or an empty/inactive channel with no VODs — the handle may differ here or the person doesn't stream; absence isn't proof.

## Gotchas & OpSec
- A matching handle isn't proof of identity — verify via linked accounts, face/voice, and content.
- VODs may be auto-deleted after a period; clips persist longer — grab evidence promptly.
- OpSec: watch **logged-out**; following/chatting notifies the streamer and attributes you.

## Overlaps ("do both")
- Pairs with `[[whatsmyname-web]]` (find the handle elsewhere) and `[[google-reverse-image-search]]` (reverse a captured face/still) — Twitch supplies rich A/V; those confirm identity and spread.

## Trust & verifiability
`trust: community` — authentic first-party content, but confirm the channel is your subject (handle collisions happen) before attributing anything from a stream.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitch-tv |
| category | image-video-face |
| selectorsIn → selectorsOut | username, name → social-profile, image, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>

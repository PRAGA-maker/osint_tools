---
id: vaughnlivetv
name: VaughnLive TV
description: Use when you have a `username`/handle or need to browse live IRL/streaming video and want to find a person's live channel and on-camera appearance — returns social-profile and image/video of the streamer.
url: http://vaughnlive.tv
category: image-video-face
path:
- image-video-face
bestFor: Finding a subject's live-streaming channel (IRL/gaming/webcam) and observing them on camera in real time.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
- geolocation
status: live
pricing: free
costNote: Free to browse and watch; account only needed to broadcast, chat, or follow.
opsec: passive
opsecNote: Watching a public stream is passive and anonymous. But entering chat, following, or interacting reveals your account to the streamer and viewers — lurk read-only unless you deliberately want to engage from a sock puppet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running independent live-streaming platform (now at vaughn.live); legitimate service, but content is user-generated and unmoderated in places, so any identifying detail is claimed, not verified.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Vaughn Live
- vaughnlive.tv
- vaughn.live
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- livestreaming
source: toddington-resources
lastVerified: '2026-07-15'
enrichment: full
---

# VaughnLive TV

> An independent live-streaming platform (IRL, gaming, webcam, city cams): search a handle to find someone's live channel and watch them on camera in real time.

## When to use
You have a `username`/handle (or a display `name`) you believe belongs to a live-streamer, and you want to locate their channel, confirm identity by observing them on camera, and pick up incidental clues — visible surroundings (`geolocation`), on-screen chat handles, stream schedule. Useful in a missing-person context when a subject is known to stream, because a live feed places them at a moment in time.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the site — https://vaughnlive.tv redirects to https://vaughn.live/. No login is required to browse or watch.
2. Use the "Type a name to search" box to look up the `username`/handle, or browse category rows (IRL/Lifestyles, Gaming, News & Tech, City Cameras, Nature).
3. Open a matching channel: watch the live/archived video for on-camera identification, read the profile blurb, and note the chat for other handles the subject interacts with.
4. Watch the background of IRL/webcam streams for `geolocation` cues (signage, landmarks, room details) — but do not over-read; a stream location can be spoofed or old.
5. Pivot: the confirmed handle feeds cross-platform username search; on-camera appearance feeds face/image comparison via `[[pimeyes-com]]`-style tools; background clues feed geolocation workflows.

## Inputs → Outputs
- **In:** `username` / `name`
- **Out:** `social-profile` (channel), `image`/live video of the person, incidental `geolocation`
- **Empty/negative result looks like:** the search returns no channel, or only inactive/never-live channels — a registered handle with zero broadcasts tells you the account exists but places the person nowhere.

## Gotchas & OpSec
- Human-in-the-loop: none to watch; only broadcasting/chatting needs an account.
- OpSec: read-only watching is passive and anonymous. Following, chatting, or reacting exposes your account — use a sock puppet if you must interact.
- Content is user-generated: display names and bios are self-asserted, and background/location can be staged. Corroborate identity, don't assume it.

## Overlaps ("do both")
- Pairs with `[[livestream-aka-vimeo]]` and other livestreaming directories — coverage differs by platform, and a subject may stream on more than one, so check both.

## Trust & verifiability
`trust: community` — the platform itself is a real, established service, but everything on a given channel is user-submitted, so treat identities and locations as leads to verify rather than confirmed facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vaughnlivetv |
| category | image-video-face |
| selectorsIn → selectorsOut | username, name → social-profile, image, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

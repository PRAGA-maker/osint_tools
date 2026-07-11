---
id: snapchat-com
name: snapchat.com
description: Use when you have a Snapchat `username` and want the public profile behind it — returns the public profile page, Bitmoji/avatar and public Story/Spotlight content (`social-profile`/`image`), plus Snap Map `geolocation` context.
url: https://snapchat.com/add/
category: image-video-face
path:
- image-video-face
bestFor: Viewing a Snapchat user's public profile, avatar, and public snaps from the web.
selectorsIn:
- username
selectorsOut:
- social-profile
- image
- geolocation
status: live
pricing: free
costNote: Free. Public profile pages (snapchat.com/add/<username>) and Snap Map are viewable in a browser without an account.
opsec: passive
opsecNote: Viewing a public web profile or the Snap Map is passive and does NOT notify the user. This changes the instant you use the app to add/message someone or view their Story while logged in — that can be visible to them. For public recon stay on the web profile; if you must use the app, use a sock-puppet account and device.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Snapchat platform. The public web profile is genuine platform data; how much is exposed depends entirely on the user's privacy settings (many profiles show little publicly).
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- snap-map
- gsmarena-com
aliases:
- Snapchat
- snapchat.com/add
tags:
- profileimages
- Profile Images
- snapchat
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# snapchat.com

> Snapchat's public web layer — view a user's public profile, Bitmoji, and public Story/Spotlight snaps by handle, and read location from the Snap Map, all without the app.

## When to use
You have a Snapchat `username` (often reused from other platforms) and want what the platform exposes publicly: the profile page and Bitmoji avatar (`image`), any public Story or Spotlight content, and — via the Snap Map — a possible `geolocation` if the person shares their location or posts to public map Stories. Useful for confirming a handle belongs to your subject, pulling an avatar/photo to reverse-search, and picking up location signals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open `https://www.snapchat.com/add/<username>` in a browser to load the public profile (avatar, display name, Bitmoji, any public snaps).
2. Check the Bitmoji/avatar and any public Story/Spotlight content; capture the avatar `image` for reverse-image search.
3. Open the **Snap Map** (map.snapchat.com) and search the area for public map Stories that could place the subject or corroborate a location.
4. Note the display name and linked handles for cross-platform pivots.
5. Pivot: the avatar `image` feeds reverse-image/face search; public map Stories feed `geolocation`; the handle feeds username enumeration elsewhere.

## Inputs → Outputs
- **In:** `username` (Snapchat handle)
- **Out:** `social-profile` (public profile, display name), `image` (Bitmoji/avatar, public snaps), Snap Map `geolocation` context
- **Empty/negative result looks like:** a bare profile with no public snaps, or the handle doesn't resolve — most users keep everything private, so a thin profile is normal and not proof of inactivity.

## Gotchas & OpSec
- Human-in-the-loop: none for the public web profile; interacting in-app is where risk starts.
- OpSec: **passive** on the web profile/Snap Map (no notification). Adding/messaging or viewing a Story while logged in can expose you — do that only from a sock-puppet account, never your real one.
- Snapchat is privacy-heavy: the public surface is deliberately small. Snap Map only helps if the subject or bystanders share location publicly.

## Overlaps ("do both")
- Pairs with the `[[snap-map]]` for geolocation and with reverse-image/face tools for the captured avatar — the profile confirms the account, the map adds location, reverse-image links the avatar elsewhere. Combine with cross-platform username search.

## Trust & verifiability
`trust: trusted` — genuine first-party data, but limited by user privacy settings. Treat a matched handle plus avatar as a lead to confirm via reverse-image and cross-platform checks, since Snapchat exposes little to authenticate identity on its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | snapchat-com |
| category | image-video-face |
| selectorsIn → selectorsOut | username → social-profile, image, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

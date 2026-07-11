---
id: bandcamp
name: Bandcamp
description: Use when you have a `username`/`name` of a musician or music fan and want their public profile — returns social-profile, image, and often a stated location (geolocation).
url: https://bandcamp.com
category: image-video-face
path:
- image-video-face
bestFor: Finding a subject's music-artist or fan profile — bio, location, linked accounts, and profile image.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
- geolocation
status: live
pricing: free
costNote: Free to browse public artist and fan profiles; no account needed to view.
opsec: passive
opsecNote: Viewing public profiles is passive and doesn't notify the user. Following/messaging or buying music from a logged-in account would expose you — stay logged out for reconnaissance, or use a sock puppet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A major, legitimate music platform. Profile fields (bio, location, links) are self-declared by users, so treat them as claims to corroborate, not verified facts.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- bandcamp.com
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- music
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# Bandcamp

> A music platform where artists and fans keep public profiles — useful when your subject makes or collects music.

## When to use
Your subject is (or may be) a musician, label, or active music fan. A Bandcamp artist page carries a bio, a stated location, external links (website/socials), release history, and images; a fan account reveals a collection/wishlist that maps taste and, via followed artists, an `associate` network. Reach for it when a `username`/`name` from another platform might carry over to Bandcamp.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to bandcamp.com and search the `name`/`username`, or try bandcamp.com/<username> directly if you have a handle.
2. Open the artist or fan profile.
3. Read: bio, stated location (`geolocation`), linked website/socials, profile/banner `image`, releases or collection.
4. Pivot: reverse-image the profile picture; follow external links to other platforms; a fan's followed artists/collection reveal interests and connections.

## Inputs → Outputs
- **In:** `username` or `name` (artist/label/fan)
- **Out:** `social-profile` (bio, links, releases/collection), profile `image`, self-declared `geolocation`
- **Empty/negative result looks like:** no profile or an unrelated namesake — the subject isn't on Bandcamp under that handle. Common handles collide; confirm via linked socials or profile image before attributing.

## Gotchas & OpSec
- Self-declared fields: location and bio are user-supplied and may be fictional or promotional — corroborate.
- Handle collisions: many "johnsmith"s; verify identity via cross-links, not name alone.
- OpSec: passive when logged out; don't follow/buy from an attributable account.

## Overlaps ("do both")
- Pairs with username-search tools (to find the Bandcamp handle from another platform) and reverse-image search (on the profile picture) — Bandcamp adds a music-scene angle and often a fresh set of external links other platforms miss.

## Trust & verifiability
`trust: community` — a legitimate platform, but profile content is self-published. The account existing is solid; the biographical/location claims on it need a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bandcamp |
| category | image-video-face |
| selectorsIn → selectorsOut | username, name → social-profile, image, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

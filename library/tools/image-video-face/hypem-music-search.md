---
id: hypem-music-search
name: Hypem Music Search
description: Use when you have an artist/DJ `name` or `username` and want to find their tracks, blog write-ups and linked profiles across music blogs — returns social-profile links and web mentions.
url: http://hypem.com
category: image-video-face
path:
- image-video-face
bestFor: Surfacing music-blog coverage, track uploads and linked accounts for a subject who is a musician, DJ or producer.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to search and browse; a free account is optional (only needed to save favourites). No paywall for lookups.
opsec: passive
opsecNote: Passive third-party browsing — you query Hype Machine's index, not the subject. Searches are not visible to the subject. Standard sock-puppet browser hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running (since 2005) music-blog aggregator; reputable within music discovery, but it indexes third-party blogs so attribution quality varies. Not a first-party identity source.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Hype Machine
- hypem.com
tags:
- toddington
- curated-directory
- image-video-multimedia-search
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# Hypem Music Search

> Hype Machine — a music-blog aggregator; useful in OSINT only when the subject is a musician/DJ, to find their tracks and the blogs and profiles that link to them.

## When to use
Reach for this in the narrow case where your subject is a music artist, producer or DJ and you have their `name` or a stage/handle `username`. Hype Machine indexes what thousands of music blogs post, so it can surface an artist's tracks, the blogs writing about them, and outbound links (SoundCloud, Bandcamp, socials) you can pivot on. It is **not** a face/image search or a general people-finder despite its directory category — skip it for non-musician subjects.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://hypem.com and use the search box for the artist/track `name` (or the handle you suspect they use).
2. Open a matching artist/track result; note the source blog posts and any outbound links to streaming or social profiles.
3. Read the output: track listings, blog write-ups, and linked profiles (`social-profile`). Follow the blog links off-site for more context (locations, collaborators).
4. Pivot: linked SoundCloud/Bandcamp/social handles feed username enumeration; collaborator names feed `associate` mapping.

## Inputs → Outputs
- **In:** `name` or `username` (artist/DJ/producer)
- **Out:** `social-profile` (linked streaming/social accounts via indexed blog posts), web mentions
- **Empty/negative result looks like:** no matching artist/track — meaning the subject either isn't a covered artist or the name doesn't match anything the blogs posted. Do not treat absence as identity confirmation.

## Gotchas & OpSec
- Very narrow scope: only relevant for music-scene subjects. The stub's `image`/`face` selectors were mis-harvested — it does no image or face matching.
- OpSec: passive; the subject is not notified. Ordinary browser hygiene suffices.
- Attribution comes from third-party blogs, so treat a linked profile as a lead to verify, not a confirmed identity.

## Overlaps ("do both")
- Pairs with dedicated username-enumeration tools once Hype Machine hands you a stage handle — this finds the artist's music footprint, those tools spread the handle across the wider web.

## Trust & verifiability
`trust: community` — an established music-discovery aggregator, but it reflects what independent blogs publish, so its links are leads to corroborate rather than authoritative identity records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hypem-music-search |
| category | image-video-face |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

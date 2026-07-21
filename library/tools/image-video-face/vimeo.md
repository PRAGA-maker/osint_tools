---
id: vimeo
name: Vimeo
description: Use when you have a `name`, `username` or topic and want video content and creator profiles on Vimeo — returns `social-profile`s, videos and the descriptions/locations/links attached to them.
url: https://vimeo.com
category: image-video-face
path:
- image-video-face
bestFor: Searching Vimeo for a subject's videos and creator profile, and mining video pages for links, locations and collaborators.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free to search, watch and view public profiles; uploading/hosting has free and paid tiers, but consumption for OSINT is free.
opsec: passive
opsecNote: Browsing public videos and profiles is passive; the creator isn't notified. Logging in, liking, following or commenting reveals an identity — do that only from a sock-puppet account, never your real one.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Vimeo is the first-party platform; profiles and videos are authentic user content (though bios/links are self-declared).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- vimeo.com
tags:
- video-search-and-other-video-tools
- video-platform
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# Vimeo

> The creative-professional video platform — a quieter, higher-production corner than YouTube where filmmakers, artists and businesses post work, often with rich bios, portfolio links and location tags.

## When to use
Your subject is a creative professional (filmmaker, videographer, artist, agency) or you're chasing a specific video. Vimeo often carries content and profiles that never appear on YouTube, and its creators tend to link portfolios, websites and other socials from their bios. Search a `name`/`username` to find a subject's profile and uploads, or a topic/place to find footage of an event or location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://vimeo.com and search by `name`, `username`, keyword, or place.
2. Open matching profiles: read the bio for a real name, location, website and linked socials; browse their video library.
3. Open individual videos for descriptions, tags, credited collaborators, on-screen locations, and links in the description.
4. Note geolocation clues in footage (signage, landmarks) for visual geolocation.
5. Pivot: bio links feed domain/social OSINT; credited collaborators surface `associate`s; a matched profile confirms a `social-profile` and often a real name.

## Inputs → Outputs
- **In:** `name`, `username`, or topic/place
- **Out:** `social-profile`s (creator pages), videos, and their descriptions, links, collaborators and location cues
- **Empty/negative result looks like:** no matching profile/video — the subject isn't on Vimeo (it's far smaller than YouTube), or their content is private/password-protected. Check YouTube and other platforms before concluding no video footprint.

## Gotchas & OpSec
- Much smaller user base than YouTube — a blank here doesn't mean no video presence elsewhere.
- Some videos are private or password-protected and won't surface in search.
- OpSec: **passive** to watch/browse; **active** the moment you log in, follow or comment — use a sock-puppet.

## Overlaps ("do both")
- Pairs with YouTube and TikTok search plus reverse-image/video tools — run the subject across all video platforms, and analyze downloaded frames for location and identity cues.

## Trust & verifiability
`trust: trusted` — first-party platform content is authentic, but bios and links are self-declared, so verify claimed identities/locations against independent sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vimeo |
| category | image-video-face |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

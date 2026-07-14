---
id: podbean
name: Podbean
description: Use when you have a subject's `name` or `username` and suspect they host a podcast — returns their public podcast `social-profile`, episode metadata, and linked contact/social details.
url: http://www.podbean.com
category: image-video-face
path:
- image-video-face
bestFor: Finding a subject's podcast, its episode history, and the show notes / linked accounts they publish alongside it.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
status: live
pricing: freemium
costNote: Free to browse the public Discover directory and podcast/episode pages; hosting a podcast has free and paid tiers, but searching is free and needs no account.
opsec: passive
opsecNote: Browsing public podcast and episode pages is passive and unauthenticated. Do not subscribe/comment from an attributable account if you want to stay unseen.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Podbean is a large, established podcast-hosting platform; the content is first-party creator publishing, though creator-supplied bio/links are self-asserted.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Podbean podcasts
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- podcast
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# Podbean

> A major podcast-hosting platform (600k+ shows) with a public Discover directory — use it to find a subject's podcast and mine the show notes, episode history, and linked accounts for leads.

## When to use
You have a `name` or `username` and reason to think the subject podcasts, or you have a known podcast and want its metadata. Podbean's public pages expose the creator/show name, category, episode titles and dates, show notes, a custom show website, and often links to the creator's other social accounts and contact info — all rich pivot material and, in audio, the subject's own voice and disclosures.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to Podbean's Discover/search and query the subject's `name`, `username`, or a likely show title.
2. Open the show page: note the creator name, custom site URL, category, and any linked socials/contact details.
3. Scan episode titles, dates, and show notes for names, places, events, and associates.
4. Sample episodes — audio often reveals location, routine, and relationships not written anywhere.
5. Pivot: linked socials → cross-platform username checks; the custom show domain → WHOIS; transcribe key episodes with `[[huggingface-co-4]]`.

## Inputs → Outputs
- **In:** `name` or `username` (or a known show title)
- **Out:** `social-profile` (podcast page, custom site, linked accounts), confirmed `name`, episode metadata and show notes
- **Empty/negative result looks like:** no matching show, or a dormant/abandoned show with generic notes — Podbean also syndicates to Apple/Spotify, so check those directories before concluding absence.

## Gotchas & OpSec
- Creator bios and links are self-asserted — verify, don't assume.
- Discovery leans on content categories, not people; a subject's show may be findable only via a linked social account or the exact title.
- Some shows are private/unlisted and won't appear in Discover.

## Overlaps ("do both")
- Pairs with Apple Podcasts/Spotify directory search (same shows, different index) and `[[huggingface-co-4]]` for transcribing episodes into searchable, citable text.

## Trust & verifiability
`trust: trusted` — a large first-party hosting platform, so the show/episode data is genuine; treat creator-supplied bios and links as leads to corroborate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | podbean |
| category | image-video-face |
| selectorsIn → selectorsOut | name, username → social-profile, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: discover-podcasts-here
name: PodSearch
description: Use when you have a `name` and want to find a subject's own podcast or guest appearances — returns social-profile, associate.
url: https://podsearch.com/
category: image-video-face
path:
- image-video-face
bestFor: Discovering podcasts and episodes tied to a person — their own show or guest spots — as a route to voice, bio and network.
selectorsIn:
- name
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free to search and browse the podcast directory; listeners sign up at no cost for extra features, and listing a podcast is free.
opsec: passive
opsecNote: Searching a public podcast directory is passive and not visible to any subject. Listening to episodes leaks nothing about you; use a clean session by habit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party podcast discovery directory; listings are self-submitted and platform-aggregated, so treat identity links as leads.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- podsearch.com
- Discover Podcasts Here
tags:
- podcast
- audio-search
source: osint4all
lastVerified: '2026-07-16'
enrichment: full
---

# PodSearch

> A podcast discovery directory — a route to a subject's own show or guest appearances, and the bio, voice and contacts those expose.

## When to use
You have a `name` and want to check whether the subject hosts a podcast or has appeared as a guest. Podcasts are a rich, under-searched OSINT source: an episode page often carries a bio, social links (`social-profile`), a personal website, contact details, and co-hosts/guests (`associate`) — and the audio itself confirms voice and volunteers biographical detail people rarely put in writing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open `podsearch.com` and use the search / browse feature.
2. Search the subject's `name`, their known handle, or a niche topic they are associated with.
3. Read the results:
   - A matching show or episode gives the podcast's page, host/guest names (`associate`), and linked profiles/website (`social-profile`).
   - Note the hosting platform (Apple/Spotify/etc.) and jump there for full episode notes and links.
4. Pivot: episode show-notes links feed username-enumeration and website research; named co-hosts/guests become new targets; listen for self-disclosed location, employer or timeline details.

## Inputs → Outputs
- **In:** `name` (or handle / topic)
- **Out:** `social-profile` (podcast page, linked accounts, site), `associate` (co-hosts, guests)
- **Empty/negative result looks like:** no matching show/episode — meaning the person likely has no indexed podcast presence here; try the topic angle and the native Apple/Spotify search before concluding absence.

## Gotchas & OpSec
- Directory search leans toward show/episode *titles and metadata*; it does not transcribe audio, so a passing mention inside an episode won't surface by keyword. Cross-check with a transcript-search tool where one exists.
- Listings are self-submitted; verify the person is actually the host/guest, not just name-dropped.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with native Apple Podcasts / Spotify search and any podcast-transcript search tool — this finds the show, transcript search finds spoken mentions the directory can't index.

## Trust & verifiability
`trust: community` — a third-party discovery directory aggregating public podcast feeds; confirm host/guest identity on the podcast's own platform page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | discover-podcasts-here |
| category | image-video-face |
| selectorsIn → selectorsOut | name → social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

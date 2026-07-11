---
id: buzzsprout
name: Buzzsprout
description: Use when you have a `name` or `username` and want to find a subject's podcast presence — returns social-profile, audio/show-notes content, and employer-org / contact leads from their podcast site.
url: https://www.buzzsprout.com
category: image-video-face
path:
- image-video-face
bestFor: Locating a subject's podcast (hosted on Buzzsprout) and mining its episodes, show notes, and site for identifying details.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- employer-org
status: live
pricing: freemium
costNote: Free tier for creators; listening/browsing hosted shows is free and needs no account. Podcaster tools (upload, analytics) are paid — irrelevant for research use.
opsec: passive
opsecNote: Browsing a public podcast page and playing episodes is passive and anonymous; you are viewing published content, not contacting the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial podcast-hosting platform (est. 2009), not an investigative tool; useful only as a content source for shows it hosts.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Buzzsprout podcast
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- podcast
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# Buzzsprout

> A major podcast-hosting platform — not a search engine, but where a subject's podcast (and its revealing show notes, voice, and contact links) may live.

## When to use
You have a `name` or `username` and suspect the subject hosts or appears on a podcast. Podcasts leak identifying detail generously: a real voice (`physical-description`/voiceprint context), guest and co-host `associate` links, employer or project mentions (`employer-org`), locations, and often a contact email in the show notes. Buzzsprout hosts a large share of independent shows, and each show gets a public site with episodes and notes.

## How to use it (`bestInteractionPattern`: web-manual)
1. Note that Buzzsprout is a *host*, not a directory — you don't browse all shows from a search box. Find the specific show first: search the wider web (Google `site:buzzsprout.com <name>`, or the subject's name + "podcast") to land on their Buzzsprout-hosted page.
2. Open the show's Buzzsprout site: read the show description, host bio, and per-episode show notes.
3. Play/scan episodes for names, places, employers, and dates dropped in conversation; note any contact email or linked `social-profile`.
4. Pivot: an email feeds email-OSINT; a co-host/guest feeds `associate` mapping; the audio itself confirms a voice/identity.

## Inputs → Outputs
- **In:** `name` / `username` (resolved to a specific show via web search first)
- **Out:** `social-profile` (the show site + linked accounts), `employer-org`/project mentions, contact email, `associate` links
- **Empty/negative result looks like:** no Buzzsprout-hosted show for the subject. Many podcasters use other hosts (Anchor/Spotify, Libsyn, etc.), so absence here does not mean the subject has no podcast.

## Gotchas & OpSec
- Buzzsprout does not have a public search directory — you must locate the show through an external search engine, then read it here.
- This file lives under image-video-face for harvesting reasons, but the payload is audio + text, not faces; set expectations accordingly.
- OpSec: **passive** — playing a public episode is anonymous.

## Overlaps ("do both")
- Pairs with podcast search indexes (Listen Notes, Apple/Spotify search) — those find the show across all hosts, while Buzzsprout is where you then read the full notes and site once the show is Buzzsprout-hosted.

## Trust & verifiability
`trust: community` — a commercial hosting service; the content is self-published by the creator, so treat claims within episodes as the subject's own assertions, corroborated by the audio itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | buzzsprout |
| category | image-video-face |
| selectorsIn → selectorsOut | name, username → social-profile, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

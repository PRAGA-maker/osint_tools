---
id: podcast-alley
name: Podcast Alley (Podcast Machine)
description: Use when you have a `name`/`username` and want to check whether a subject self-hosts a podcast here — returns a show page with bio, photo and audio (a niche host, not a search directory).
url: https://podcastmachine.com
category: image-video-face
path:
- image-video-face
bestFor: Confirming and pulling a subject's self-hosted podcast (bio, cover image, voice) if they publish on Podcast Machine.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- image
- name
status: live
pricing: freemium
costNote: Free tier (1 GB storage) up to a $39/month plan; viewing a public show page needs no account or payment — the paid tiers are for creators hosting content, not for searchers.
opsec: passive
opsecNote: Browsing a public show page is an anonymous pageview and does not notify the podcaster. Registering as a creator is unnecessary for OSINT; if you do sign up, use a sock-puppet identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party podcast hosting/publishing platform, not a curated OSINT source; it was harvested into a directory under a mislabeled name ("Podcast Alley"). Any hosted content is self-published by the show owner.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Podcast Machine
- podcastmachine.com
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- podcast
source: toddington-resources
lastVerified: '2026-07-15'
enrichment: full
---

# Podcast Alley (Podcast Machine)

> Despite the "Podcast Alley" label, this URL is Podcast Machine — a podcast hosting/publishing platform. Its OSINT value is narrow: confirming and pulling a subject's *self-hosted* show, not searching podcasts at large.

## When to use
You have a `name` or `username` and a reason to think the subject produces a podcast, and you want to check whether they host it on Podcast Machine. A hit gives you a show page — bio, cover art / profile `image`, episode audio (their voice), and often external links — which corroborates identity and yields fresh pivots. This is a *destination check*, not a broad discovery engine; for finding any podcast by topic, use a real podcast search index instead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://podcastmachine.com and use its browse/search to look for the subject's name, handle, or show title.
2. If direct search is thin, run a Google dork: `site:podcastmachine.com "Name or handle"`.
3. Open any matching show page: read the bio, save the cover/profile `image`, note linked social profiles and website.
4. Pivot: the cover image feeds reverse-image/face tools; linked socials feed username/social searches; the audio itself is a voice sample.

## Inputs → Outputs
- **In:** `name` / `username` (or show title)
- **Out:** `social-profile` (show page + linked accounts), `image` (cover/profile art), confirmed `name`/bio
- **Empty/negative result looks like:** no matching show, or only the generic Podcast Machine marketing pages. Absence is weak evidence — most podcasters host on Spotify/Apple/Libsyn, not here, so a miss does not mean the subject has no podcast.

## Gotchas & OpSec
- Directory mislabel: the harvested name is "Podcast Alley," but the live site is **Podcast Machine** — do not conflate it with the defunct PodcastAlley.com directory.
- It is a *host*, not an aggregator: it only indexes shows published on its own platform, so coverage is small.
- OpSec: passive; browsing does not alert the show owner.

## Overlaps ("do both")
- Pairs with mainstream podcast search (Apple/Spotify/Listen Notes) and reverse-image tools — those cover the podcasts this host doesn't, and turn any cover art or voice clip you find here into further leads.

## Trust & verifiability
`trust: unverified` — a commercial hosting platform surfaced through a third-party directory, not a vetted investigative source. Treat show content as self-published and confirm identity against an independent channel.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | podcast-alley |
| category | image-video-face |
| selectorsIn → selectorsOut | name, username → social-profile, image, name |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

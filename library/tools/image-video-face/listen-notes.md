---
id: listen-notes
name: Listen Notes
description: Use when you want to find a person, name or topic mentioned across podcasts — returns matching podcast episodes with show, date and audio.
url: https://www.listennotes.com/
category: image-video-face
path:
- image-video-face
bestFor: Full-text search engine across podcasts/episodes — surface where a name or topic is discussed in audio.
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
- associate
- metadata-exif
status: live
pricing: freemium
costNote: Free web search; an API and premium features (e.g. full listening, larger result limits) are paid.
opsec: passive
opsecNote: Read-only keyword search over indexed public podcasts; no target data uploaded. Searches run against Listen Notes' servers.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Listen Notes is a well-established, widely-used podcast search engine with a documented API. Reliable as a search index; relevance to a given case depends on whether the subject appears in podcast audio.
missingPersonsRelevance: medium
coverage: [global]
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases: []
tags:
- podcast-search
source: osint4all
lastVerified: ''
enrichment: full
---

# Listen Notes

> A large podcast search engine — search millions of episodes by keyword, name or topic and get episode pages with show, date and audio.

## When to use
You have a `name` or `employer-org` and suspect the subject (or someone connected to them) has appeared on or been discussed in a podcast — interviews, local community shows, hobby/niche programmes. Useful for building context, finding associates and confirming voice/identity, especially for people with a public-facing role or interest community.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.listennotes.com/.
2. Search the name/term (`selectorsIn`: name, employer-org); use filters (date, language, genre) to narrow.
3. Open matching episodes; note the show, host, publish date, description and any guest/associate mentions (`selectorsOut`: associate links, social-profile links in show notes, episode `metadata-exif`/dates).
4. Pivot: a guest appearance leads to the show's other platforms, the host, and linked social profiles; for automation use the Listen Notes API.

## Inputs → Outputs
- **In:** `name`, `employer-org` (keyword)
- **Out:** episode pages with `associate`/`social-profile` references in show notes and episode `metadata-exif` (dates, durations)
- **Empty/negative result looks like:** no episodes match — common for private individuals with no media presence.

## Gotchas & OpSec
- Indexes public podcast feeds only; absence of a hit says nothing about whereabouts.
- Full listening / large-scale querying needs the paid API or premium.
- OpSec: passive — read-only public search; no target data is uploaded.

## Overlaps ("do both")
- Pair with general web/news search and social enumeration; podcast show notes often link the exact profiles those tools then expand.

## Trust & verifiability
`trust: community` — established, well-documented search index; reliable as a tool, with case relevance depending on the subject's media footprint.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | listen-notes |
| category | image-video-face |
| selectorsIn → selectorsOut | name, employer-org → social-profile, associate, metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

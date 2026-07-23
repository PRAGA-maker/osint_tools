---
id: overcast-podcast-app-mobile-ios
name: Overcast Podcast App (Mobile – iOS)
description: Use when you need to listen to and search a subject's podcast output on iOS — a free podcast player, useful for consuming audio evidence, not a data-source that resolves selectors.
url: https://itunes.apple.com/ca/app/overcast-podcast-player/id888422857?mt=8
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Playing, chapter-scrubbing and re-listening to podcast episodes a subject appears in or produces, on an iOS device.
selectorsIn:
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free on the iOS App Store (optional paid tier removes nothing essential for listening).
opsec: passive
opsecNote: Playback is passive — subscribing to or streaming a public podcast does not notify the creator. Do it on a sock-puppet device/Apple ID if you want no linkage; avoid interacting (ratings, reviews) which are attributable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: mobile-app
trust: trusted
trustNote: Well-known independent iOS podcast client by Marco Arment; the app itself is reputable, though the intelligence value is only in the public podcast content you play through it.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Overcast
- Overcast podcast player
tags:
- opsec-investigator-tooling
- mobile-app
- podcast
- toddington
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# Overcast Podcast App (Mobile – iOS)

> A free, reputable iOS podcast player — investigator plumbing for listening to and re-scrubbing a subject's audio output, not a lookup that returns intelligence on its own.

## When to use
Your subject hosts, guests on, or is discussed in podcasts and you need to actually listen — for names, places, admissions, or corroborating detail dropped in audio. Overcast is a convenient consumption tool (variable speed, chapters, per-episode search of your library) for working through that audio on iOS.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install Overcast from the iOS App Store (use a sock-puppet Apple ID/device for clean OpSec).
2. Search for the show or paste an episode/RSS URL you found via other OSINT, and add it.
3. Play with speed control and chapter navigation; re-listen to key segments and note timestamps.
4. Pivot: names/places/handles mentioned in audio feed people-search, geolocation, and social-profile enumeration. The show's own page/RSS often lists a `social-profile` or website for the subject.

## Inputs → Outputs
- **In:** `name` / show identifier you already have
- **Out:** the audio content itself, plus any `social-profile`/website linked from the show — no automated selector extraction
- **Empty/negative result looks like:** the show/episode isn't in Apple's podcast index — try the podcast's direct RSS feed or another directory.

## Gotchas & OpSec
- It is a *player*, not a discovery or transcription engine — you find the podcast elsewhere and use this to consume it.
- Do not rate, review, or comment from an attributable account.
- iOS-only; on Android or desktop use another player or a transcript tool instead.

## Overlaps ("do both")
- Pairs with podcast/transcript search tools — use those to *find and text-search* episodes, then Overcast to listen closely to the segments that matter.

## Trust & verifiability
`trust: trusted` — a mature, well-regarded app; reliability of any lead comes from the public podcast content, which you must corroborate independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | overcast-podcast-app-mobile-ios |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | name → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | mobile-app |
| opsec | passive |
| human-in-loop | no |

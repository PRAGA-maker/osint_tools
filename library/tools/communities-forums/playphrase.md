---
id: playphrase
name: PlayPhrase
description: Use when you have a spoken phrase (from a clip whose film/show you're trying to identify) and want to find where it's said on screen — returns movie/TV fragments containing that phrase.
url: https://playphrase.me/
category: communities-forums
path:
- communities-forums
bestFor: Identifying which film/show a line of dialogue comes from by searching millions of movie phrase clips.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free searching with limits; a paid subscription removes caps/ads.
opsec: passive
opsecNote: You search a media index — nothing concerns any individual. Fully passive; no subject is touched.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A novelty "cinema archaeology" search over movie subtitles/clips; useful for media identification, not an investigative data source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- PlayPhrase
- playphrase.me
tags:
- Movies
- media-identification
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# PlayPhrase

> A search engine over movie dialogue: type a phrase and watch the film/TV clips where it's spoken — a media-identification aid, not a people tool.

## When to use
A narrow media-verification use: you're geolocating or contextualising a video and someone quotes or plays a line of film/TV dialogue, and you need to identify the source title (which can date a clip, explain a reference, or debunk a "candid" recording that's actually a movie quote). PlayPhrase indexes millions of phrases to on-screen fragments. It identifies media, never a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://playphrase.me/.
2. Type the spoken phrase as accurately as you can transcribe it.
3. Browse the returned clips; match the scene/voice to your source to identify the film/show.
4. Pivot: the identified title dates and contextualises the clip; combine with other verification cues.

## Inputs → Outputs
- **In:** a text phrase of dialogue (not an OSINT selector)
- **Out:** movie/TV clips containing that phrase (identifying the source title)
- **Empty/negative result looks like:** no clips — the phrase is too generic, mis-transcribed, or from media not in the index (foreign/obscure/new); a miss doesn't mean it's not a quote.

## Gotchas & OpSec
- Index is large but far from complete (English-dominant); absence isn't proof.
- Requires an accurate transcription — mis-heard words kill the search.
- Free tier is capped; that's usually enough for one-off identification.

## Overlaps ("do both")
- Complements subtitle-search sites (e.g. OpenSubtitles) — PlayPhrase gives you the *clip*, subtitle databases give you the surrounding script and exact source for confirmation.

## Trust & verifiability
`trust: unverified` — a novelty media index; reliable enough for identifying a well-known quote, but verify the match against the actual film/subtitles before asserting a source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | playphrase |
| category | communities-forums |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

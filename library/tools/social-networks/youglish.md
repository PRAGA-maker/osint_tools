---
id: youglish
name: YouGlish
description: Use when you have a `name` or phrase and want YouTube clips where it is actually spoken — returns video segments (with jump-to timing) that pronounce/say the term.
url: https://youglish.com/
category: social-networks
path:
- social-networks
bestFor: Finding real YouTube clips where a specific word, name, or phrase is spoken aloud.
selectorsIn:
- name
selectorsOut:
- social-profile
- name
status: live
pricing: freemium
costNote: Free to search and watch clips (daily search limit for anonymous users); a free account or premium raises limits. Built for language learners, repurposable for OSINT.
opsec: passive
opsecNote: You search YouGlish's caption index, not YouTube directly, so no channel owner is notified. Opening a clip is a normal (logged-out) YouTube view. Passive; use a clean session for sensitive terms.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A language-learning tool indexing YouTube captions; results are real caption matches you can verify by watching the clip, but coverage is skewed to well-captioned content.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- filmot
- youtube-comment-downloader
aliases:
- youglish.com
tags:
- youtube
- pronunciation
- caption-search
- video
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# YouGlish

> Built to teach pronunciation, repurposable for OSINT: search a word, name, or phrase and get the exact YouTube moments where it's spoken aloud.

## When to use
YouGlish indexes YouTube captions to show real clips of a term being said. For OSINT it's a secondary caption-search: enter a subject's `name` or a distinctive phrase and jump to the video moments where it's spoken, e.g. to hear a name pronounced, find a person being referenced on video, or locate a spoken quote. It's narrower and more language-learning-oriented than a dedicated caption search, so treat it as a supplementary way to surface spoken mentions.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://youglish.com/.
2. Enter the `name`/phrase and pick a language/accent filter if useful.
3. It plays a YouTube clip cued to the moment the term is spoken, with the caption line shown; step through further examples.
4. Note the source video and channel for any clip that's actually about your subject.
5. Pivot: a relevant video's channel is a `social-profile` lead; for exhaustive spoken-content search use `[[filmot]]`, which is purpose-built for OSINT caption search.

## Inputs → Outputs
- **In:** `name` or phrase
- **Out:** YouTube clips where the term is spoken (source video/channel = `social-profile`), `name` mentions in speech
- **Empty/negative result looks like:** "no results" — the term isn't in captioned videos YouGlish indexes, or only appears in un-captioned content. Absence isn't proof it's never said on video.

## Gotchas & OpSec
- Optimised for common words/pronunciation, not rare proper nouns — a specific personal name may return little; `[[filmot]]` is better for names/phrases.
- Anonymous searches are daily-limited.
- OpSec: passive; searching doesn't touch any channel owner.

## Overlaps ("do both")
- Pairs with `[[filmot]]` — Filmot is the deeper, OSINT-focused YouTube caption search; use YouGlish as a quick alternate lens (and for hearing pronunciation), Filmot for comprehensive spoken-mention hunting.

## Trust & verifiability
`trust: community` — a language-learning caption index. Each clip is verifiable by watching it, so matches are trustworthy; the limitation is coverage (well-captioned videos) and a bias toward common vocabulary over proper nouns.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youglish |
| category | social-networks |
| selectorsIn → selectorsOut | name → social-profile, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

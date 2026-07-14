---
id: you-tldr-com
name: YouTLDR
description: Use when you have a subject's YouTube video/channel (`social-profile`) and want its transcript and a summary without watching — returns `name`s and `associate`s mentioned plus searchable transcript text.
url: https://you-tldr.com/
category: image-video-face
path:
- image-video-face
bestFor: Pulling a full transcript/summary of a target's YouTube video to mine spoken names, places, and associates.
selectorsIn:
- social-profile
selectorsOut:
- name
- associate
status: live
pricing: freemium
costNote: Free tools include YouTube-to-transcript/blog and chapters; some conversions and higher limits sit behind a paid tier.
opsec: passive
opsecNote: YouTLDR fetches the video's captions server-side, so the target's channel does not see a view from you. Paste only public video URLs; do not upload private/unlisted links you were not meant to have.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party summarizer built on YouTube captions; transcript accuracy depends on YouTube's captions and any AI summary may paraphrase — verify quotes against the source video.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- you-tldr
- YouTube TLDR
tags:
- youtube
- YouTube Related Sites
- transcript
- video-analysis
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# YouTLDR

> A YouTube transcript-and-summary tool: turn a subject's video into searchable text so you can mine what they say — names, places, associates — without watching the whole thing.

## When to use
You have a subject's YouTube video or channel (a `social-profile`) and need the *content*, not just the metadata: what they said, who they named, where they mention being. YouTLDR extracts the transcript and produces a summary/searchable text, letting you scan hours of video for `name`s, `associate`s, locations, and admissions in minutes.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://you-tldr.com/ and paste the target's YouTube video URL.
2. Generate the transcript and TLDR summary; use the transcript search to jump to keywords (a name, a place, "my/our", dates).
3. Read the passages in full context — do not trust the summary's paraphrase for anything you will act on.
4. Repeat across the channel's key videos to build a picture.
5. Pivot: names/associates → people-search and social lookups; mentioned places → geolocation; confirm every claim against the actual video.

## Inputs → Outputs
- **In:** `social-profile` (a YouTube video/channel URL)
- **Out:** `name`s and `associate`s spoken in the video, searchable transcript, topic summary
- **Empty/negative result looks like:** no captions available (auto-captions off / non-speech video) → thin or empty transcript; the video may still hold visual intel to review manually.

## Gotchas & OpSec
- Transcript quality = YouTube caption quality; auto-captions mangle names and places — verify spellings.
- AI summaries can hallucinate or omit; treat the raw transcript as the source of truth.
- Only for public videos; do not process links you are not entitled to.

## Overlaps ("do both")
- Pairs with `[[huggingface-co-4]]` (Whisper word-level timestamps) for videos lacking captions, and with direct channel review for on-screen/visual details a transcript misses.

## Trust & verifiability
`trust: unverified` — a third-party convenience layer over YouTube captions; useful for triage, but confirm any actionable quote or name in the original video.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | you-tldr-com |
| category | image-video-face |
| selectorsIn → selectorsOut | social-profile → name, associate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

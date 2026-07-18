---
id: youtube-word-search
name: YouTube Word Search
description: Use when you have a YouTube video and a keyword/`name` and want to know exactly when it is spoken — jumps to the timestamp(s) where the word appears in the captions.
url: https://chromewebstore.google.com/detail/youtube-word-searcher/jichoejagacnbcinlgncghhdegdlhbcj
category: social-networks
path:
- social-networks
bestFor: Finding the exact second a word or phrase is spoken in a YouTube video via its captions, with optional watch-list auto-alerting.
selectorsIn:
- name
selectorsOut: []
status: live
pricing: free
costNote: Free Chrome extension, no account.
opsec: passive
opsecNote: Works on captions already delivered with the video in your browser — no extra request to the uploader or any target, so nothing is leaked to them. Watch the video logged out / in a sock-puppet browser if the collection is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Independent third-party browser extension; it relies on the video having captions (manual or auto-generated), so accuracy depends on caption quality.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- YouTube Word Searcher
- YWS
tags:
- YouTube
- transcript-search
- browser-extension
- Social Media
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# YouTube Word Search

> Ctrl-F for spoken words in a YouTube video — find and jump to the exact second a name, place, or phrase is said, instead of scrubbing a long recording.

## When to use
You have a long YouTube video (an interview, livestream, press conference, testimony) and need to know whether — and when — a specific `name`, place, or keyword is spoken. Manually watching hours of footage is impractical; this searches the captions and seeks straight to each hit. It can also auto-watch for a loaded list of words across videos, flagging when any appears. Ideal for scanning content for mentions of a subject.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the "YouTube Word Searcher" extension in Chrome/Chromium on your investigation profile.
2. Open the target video (it must have captions — manual or auto-generated).
3. Click the extension's button above the player, type the word/phrase, and jump to each timestamp where it occurs.
4. Optionally load a list of watch-words; the button turns green when one is detected on a page.
5. Pivot: confirmed mentions (and their timestamps) become citable evidence; the spoken context can surface new names/places to investigate.

## Inputs → Outputs
- **In:** a YouTube video + a keyword/`name` (or a watch-list of words)
- **Out:** the timestamp(s) where the term is spoken (seeks the player there); no personal selectors returned
- **Empty/negative result looks like:** no matches — the word isn't in the captions, OR the video has no/poor captions (auto-captions mis-transcribe names). A miss can be a caption gap, not proof the word was never said.

## Gotchas & OpSec
- Caption-dependent: no captions = nothing to search; auto-generated captions mangle proper nouns, so try spelling variants.
- Client-side utility — it searches text already in the page; it does not transcribe audio itself.
- Passive; the uploader is never notified.

## Overlaps ("do both")
- Pairs with [[youtube-comment-finder]] and transcript-download tools — this searches the spoken audio via captions, those search the written comments and full transcript.

## Trust & verifiability
`trust: community` — an independent extension operating on YouTube's own captions. Timestamps are reliable when captions are accurate; verify any name hit by listening to the clip, since auto-captions err on proper nouns.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youtube-word-search |
| category | social-networks |
| selectorsIn → selectorsOut | name → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |

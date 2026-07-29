---
id: sympsons-screencaps-search
name: Frinkiac (Simpsons Screencap Search)
description: Use when you have a quote or a suspected Simpsons `image`/meme and want to source the exact frame — returns the matching screenshot, episode, and caption. Narrow provenance/meme-origin tool.
url: https://frinkiac.com/
category: communities-forums
path:
- communities-forums
bestFor: Finding the episode and frame behind a Simpsons quote or screenshot/meme.
selectorsIn: []
selectorsOut:
- image
status: live
pricing: free
costNote: Free, no account; you can search frames and generate captioned images/GIFs at no cost.
opsec: passive
opsecNote: Searches a public Simpsons screenshot index; you type a quote, not anything about a target, so it leaks nothing. Standard web-request hygiene (sock-puppet browser) is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known fan-built search engine indexing The Simpsons frame-by-frame; accurate for what it covers (the show), maintained independently.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- Frinkiac
- Simpsons screencaps search
tags:
- Movies
- meme-origin
- image-provenance
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Frinkiac (Simpsons Screencap Search)

> A frame-by-frame search engine for The Simpsons: type a line and it finds the exact screenshot, episode, and caption — a niche tool for sourcing a meme or verifying an image's origin.

## When to use
Very narrow: a piece of media in an investigation is (or is claimed to be) a Simpsons frame or meme, and you want to establish its true origin — which episode, which line — rather than treat it as an original photo. Frinkiac lets you type the quote and land on the exact frame, confirming that an `image` is a rendered cartoon still, not evidence. It has no bearing on person-selectors and is included only for image-provenance edge cases.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://frinkiac.com/.
2. Type the remembered/visible quote (subtitle text) into the search box.
3. Read the results grid of matching frames; click one to see the full screenshot, the surrounding captions, and the episode it comes from.
4. Optionally generate a captioned still or GIF to document the match.
5. Pivot: confirming an image is a Simpsons frame closes off a false lead; the episode/air-date context can also date when a meme could first have circulated.

## Inputs → Outputs
- **In:** a text quote or subtitle line (no case selectors)
- **Out:** the matching Simpsons frame `image`, its caption, and episode identifier
- **Empty/negative result looks like:** no frames match the quote — the line is misremembered, paraphrased, or simply not from The Simpsons (Frinkiac only indexes that show).

## Gotchas & OpSec
- Human-in-the-loop: none automated — you read and judge the frame matches yourself.
- OpSec: passive; you search cartoon captions, nothing about a subject leaves your browser about the target.
- Scope is *only* The Simpsons (sibling sites cover Futurama, etc.). For arbitrary video/meme provenance, use general reverse-image search instead.
- Zero value for person-finding; use it purely to rule an image in or out as a known cartoon frame.

## Overlaps ("do both")
- Complements general reverse-image search: if a reverse-image lookup hints an `image` is a Simpsons still, Frinkiac pins the exact episode and line to confirm it, whereas reverse-image search alone may only return other meme copies.

## Trust & verifiability
`trust: community` — a long-standing, well-regarded fan project; within its single-show scope its frame matches are precise and directly verifiable against the episode.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sympsons-screencaps-search |
| category | communities-forums |
| selectorsIn → selectorsOut |  → image |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

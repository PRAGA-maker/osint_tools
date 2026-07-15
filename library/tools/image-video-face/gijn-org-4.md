---
id: gijn-org-4
name: "GIJN Guide to Detecting AI-Generated Content"
description: Use when you have an `image`/video and need a methodology to judge whether it is AI-generated or manipulated — returns verification techniques and tool pointers, not a verdict.
url: https://gijn.org/resource/guide-detecting-ai-generated-content
category: image-video-face
path:
- image-video-face
bestFor: A reputable, up-to-date methodology for spotting AI-generated/deepfake images, video and audio.
selectorsIn:
- image
selectorsOut:
- face
- metadata-exif
status: live
pricing: free
costNote: Free guide published by GIJN (Global Investigative Journalism Network); no account or payment.
opsec: passive
opsecNote: Reading the guide is fully passive. The verification steps it recommends (reverse image search, metadata checks, detector tools) each have their own OpSec — run those in a clean session and avoid uploading sensitive originals to third-party detectors.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by the Global Investigative Journalism Network, a respected non-profit supporting investigative journalists worldwide; a curated, sourced methodology rather than a black-box tool.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- thehackernews-com
aliases:
- GIJN AI content guide
- detecting AI-generated content
tags:
- reverseimagesearching
- Reverse Image Searching
- deepfake
- verification
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# GIJN Guide to Detecting AI-Generated Content

> A trusted, regularly-updated methodology from the Global Investigative Journalism Network for judging whether an image, video, or audio clip is AI-generated or manipulated — the framework you apply before trusting any media in a case.

## When to use
You have an `image` (or video/audio) that could be pivotal — a purported photo of a missing person, a "sighting," a profile picture — and you need to assess authenticity before acting on it. Generative AI makes fabricated media cheap, so a structured verification pass matters. This is a reference/methodology entry: it teaches the checks and points to detector tools; it does not return a verdict itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the GIJN guide at the URL and read the current techniques (it's updated as the field moves).
2. Apply the recommended checks to your media: look for AI artifacts (hands, teeth, text, reflections, background warping), run reverse image search for the original, inspect metadata, and try named detector tools with appropriate skepticism.
3. Weigh signals together — no single detector is reliable; converging evidence is the standard.
4. Document what you checked and your confidence level.
5. Pivot: a confirmed-real photo feeds reverse-image/face/geolocation analysis; a likely-fake one redirects your investigation and flags the source.

## Inputs → Outputs
- **In:** `image`/video/audio to assess
- **Out:** a verification methodology and tool pointers → a reasoned authenticity judgement (with `face`/`metadata-exif` signals as inputs to that judgement)
- **Empty/negative result looks like:** the guide always renders; the real hard case is inconclusive media — AI detectors frequently return low-confidence or contradictory results, and that ambiguity is itself the finding, not a failure.

## Gotchas & OpSec
- Human-in-the-loop by design: this is judgement work, not a one-click verdict. Detector scores are indicative, not proof.
- The field moves fast — rely on the guide's current version, not remembered techniques; yesterday's tells (e.g. bad hands) get fixed in newer models.
- Don't upload sensitive originals to random online "AI detectors"; prefer local checks and reputable services.

## Overlaps ("do both")
- Pairs with reverse-image search, EXIF/metadata tools, and depixelization references like `[[thehackernews-com]]` — this guide is the framework that tells you which of those to run and how to weigh them.

## Trust & verifiability
`trust: trusted` — authored by a respected investigative-journalism non-profit and openly sourced; the methodology is reliable, but its output is a probabilistic judgement you must document and, where possible, corroborate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gijn-org-4 |
| category | image-video-face |
| selectorsIn → selectorsOut | image → face, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |

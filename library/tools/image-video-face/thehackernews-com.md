---
id: thehackernews-com
name: "Unredacter / Depix depixelization (The Hacker News writeup)"
description: Use when you have an `image` containing pixelated/blurred redacted text and want to attempt reconstruction — points to the Unredacter/Depix technique that returns recovered `document-id`/text.
url: https://thehackernews.com/2022/02/this-new-tool-can-retrieve-pixelated.html
category: image-video-face
path:
- image-video-face
bestFor: Understanding and locating the tooling to reverse pixelated (not black-bar) redactions in images.
selectorsIn:
- image
selectorsOut:
- document-id
- metadata-exif
status: live
pricing: free
costNote: The article is free to read; the underlying tools (Depix, Unredacter) are free open-source projects on GitHub. No cost, but they require local setup.
opsec: passive
opsecNote: Reading the article and running the open-source tools locally on an image you already hold is passive — nothing is sent to the target or a third party. Do the reconstruction offline on your own machine; do not upload sensitive source images to any web service.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: The Hacker News is an established infosec news outlet; this is a reference article, not a hosted tool. The tools it describes (Depix by spipm, Unredacter by Bishop Fox) are real open-source projects you run yourself.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- Unredacter
- Depix
- depixelize
tags:
- photosites
- Photo Related Sites
- redaction
- forensics
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Unredacter / Depix depixelization (The Hacker News writeup)

> A reference article documenting how pixelated redactions can be algorithmically reversed — and where to get the tools (Depix, Unredacter) to try it.

## When to use
You are holding an `image` — a screenshot, leaked document, or social post — where sensitive text (a name, address, `document-id`, account number) was hidden with pixelation, blurring, or mosaic rather than a solid black bar. This page explains the attack and names the tools; the reconstruction itself is done with the open-source software, not on this page. Note this is a knowledge/reference entry, not an interactive service.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read the article at the URL to understand the threat model: pixelation is reversible when the same font/size appears unredacted elsewhere in the image.
2. Obtain the actual tool — **Depix** (`github.com/spipm/depix`) for linear-box pixelation, or **Unredacter** (Bishop Fox) for a more robust approach.
3. Install/run it locally on the pixelated crop, supplying the pixel-block search space (Depix uses a De Bruijn sequence reference image).
4. Manually review candidate reconstructions — output is a best-guess, not a certainty.
5. Pivot: a recovered name/number feeds people-search, document, or account-lookup tools.

## Inputs → Outputs
- **In:** `image` with pixelated/blurred redacted text
- **Out:** a reconstructed string (candidate `document-id`, name, or other redacted text)
- **Empty/negative result looks like:** the tools fail on true black-bar redactions, on blur without a recoverable pattern, or when there's no matching unredacted reference font — you get noise, not text. Treat all output as a hypothesis to verify.

## Gotchas & OpSec
- Human-in-the-loop: results require manual judgement; false reconstructions look plausible.
- Only works against pixelation/mosaic/blur — a solid black bar carries no information and cannot be reversed.
- Run everything locally; never upload a sensitive source image to an online "unblur" site.

## Overlaps ("do both")
- Pairs with EXIF/metadata extraction on the same image — a redacted document may still leak the same fact in its metadata that pixelation tried to hide in the pixels.

## Trust & verifiability
`trust: community` — the article is from a reputable infosec outlet and the tools are well-known open-source projects, but this library entry is a pointer to a technique; verify any recovered text against an independent source before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | thehackernews-com |
| category | image-video-face |
| selectorsIn → selectorsOut | image → document-id, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |

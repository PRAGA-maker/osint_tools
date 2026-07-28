---
id: steganography-online-codec
name: Steganography Online Codec
description: Use when you have an `image` you suspect hides a message (or want to embed one) and need to encode/decode LSB steganography with AES-256 — returns hidden text or a carrier image.
url: https://www.pelock.com/products/steganography-online-codec
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Encoding or extracting an AES-256-encrypted hidden message in the least-significant bits of an image.
selectorsIn:
- image
- password
selectorsOut:
- image
- metadata-exif
status: live
pricing: free
costNote: Free browser tool; encoding/decoding runs client-side, no account.
opsec: passive
opsecNote: PELock states passwords, images, and messages are not logged server-side, and the LSB math runs in-browser — but you are still loading a target's image into a third-party page. For sensitive evidence, prefer an offline stego tool. Only lossless formats (PNG) survive; re-saving as JPG or posting to platforms that recompress destroys the payload.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: Made by PELock (a known software-protection vendor); functional and free, but a single-vendor web tool, so verify any recovered message with a second stego tool.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- PELock Steganography Online Codec
- online steganography codec
tags:
- other-resources
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Steganography Online Codec

> A free in-browser tool that hides (or recovers) an AES-256-encrypted message inside the least-significant bits of an image's pixels.

## When to use
Two cases. (1) You have an `image` — from a suspicious profile, a shared file, or a device dump — and suspect it conceals a hidden message; you have (or can guess) the `password`. (2) You need to embed a covert message in an image for a controlled test or exercise. Steganalysis is a niche step in a media investigation, so relevance to a typical missing-persons case is low.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.pelock.com/products/steganography-online-codec.
2. **To decode:** choose "Decode", upload the carrier `image` (must be lossless — PNG/BMP/GIF), enter the `password`, and read the recovered text.
3. **To encode:** choose "Encode", upload a cover image, type the secret message and password; download the resulting PNG (do not re-save as JPG or the payload is lost).
4. Manually judge the result: correct password → clean plaintext; wrong password or no payload → garbage/empty.
5. Pivot: a recovered message may contain new selectors (names, coordinates, credentials) to chase.

## Inputs → Outputs
- **In:** `image` (carrier) + `password`
- **Out:** hidden text (on decode) or a carrier `image` (on encode); inspecting the file also touches its `metadata-exif`
- **Empty/negative result looks like:** decoding returns nonsense or nothing — either the wrong password, no hidden payload, or the image was recompressed (JPG/social-media) and the LSBs were destroyed. Absence is not proof there was never a message.

## Gotchas & OpSec
- **Format-fragile:** only lossless images carry the payload; any JPG conversion or platform recompression wipes it. An image downloaded from Facebook/Instagram has already been recompressed.
- Human-in-the-loop: you must supply/guess the password and judge whether output is real plaintext.
- OpSec: passive and client-side per the vendor, but for evidentiary work use an offline tool so the image never leaves your machine.

## Overlaps ("do both")
- Pairs with offline steganalysis suites (e.g. StegOnline, zsteg, steghide) — cross-check any hit, since different tools use different LSB schemes and one may decode what another misses.

## Trust & verifiability
`trust: community` — a free single-vendor web tool from PELock; the AES/LSB approach is sound, but confirm any recovered message and, for sensitive material, reproduce the result with an independent offline tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | steganography-online-codec |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | image, password → image, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |

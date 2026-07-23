---
id: steganography-online
name: Steganography Online
description: Use when you have a PNG image and want to hide or recover a hidden text message in it, entirely in-browser — returns extracted hidden text (or a stego image), a client-side forensics aid.
url: https://stylesuxx.github.io/steganography/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Quick, browser-based encode/decode of text hidden in PNG images (LSB steganography), no install.
selectorsIn:
- image
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (GitHub Pages); runs entirely client-side, no account.
opsec: passive
opsecNote: Processing is client-side in your browser, so the image never leaves your machine — passive and safe for sensitive files. (Still, prefer offline tools for highly sensitive evidence.)
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A simple open-source client-side tool; it implements standard LSB steganography and is auditable on GitHub.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- steghide
aliases:
- stylesuxx steganography
tags:
- steganography
- forensics
- ctf
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Steganography Online

> A zero-install, browser-based LSB steganography tool — hide text in a PNG, or try to pull hidden text back out, all client-side.

## When to use
You have a PNG `image` from a subject and want to quickly test whether a text message is hidden in its least-significant bits, or you need to embed a marker in your own image. It's the fast, no-install option for LSB steganography — a niche forensics aid, not a person-finding tool. For JPEG/audio or passphrase-protected payloads, use a dedicated tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://stylesuxx.github.io/steganography/.
2. To **decode**: upload the suspect PNG under "Decode" and read any recovered hidden text.
3. To **encode**: upload a cover PNG, type your message, and download the resulting stego image.
4. Everything runs in-browser — nothing uploads to a server.
5. Pivot: recovered hidden text (a `metadata-exif`-style note, coordinates, a `document-id`) feeds the rest of your analysis; if nothing surfaces, try [[steghide]] or `zsteg`/`binwalk`.

## Inputs → Outputs
- **In:** a PNG `image` (to decode) or a cover PNG + message (to encode).
- **Out:** extracted hidden text, or a downloadable stego image.
- **Empty/negative result looks like:** decode returns nothing/garbage — either no LSB payload exists, or it was hidden with a different tool/algorithm/format; not proof the image is clean.

## Gotchas & OpSec
- Handles LSB in PNG-style images only; JPEG-embedded or passphrase-protected payloads won't decode here.
- Re-saving/compressing a PNG can destroy an LSB payload — work from the original file.
- A negative decode is weak evidence of "nothing hidden" — cross-check with other steg tools before concluding.

## Overlaps ("do both")
- Pairs with [[steghide]] and `zsteg`/`binwalk`: this covers quick in-browser LSB text, those cover other formats, passphrases, and appended data.

## Trust & verifiability
`trust: community` — a small open-source client-side tool; the code is on GitHub and any extraction is reproducible locally.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | steganography-online |

---
id: scphillips-morse-code-translator
name: SCPhillips Morse Code Translator
description: Use when you have Morse code (or text) and want it converted the other way — returns decoded text or encoded Morse, with audio/light/vibration playback.
url: https://morsecode.world/international/translator.html
category: translation-language
path:
- translation-language
bestFor: Bidirectional Morse↔text translation with playback (sound, flashing light, vibration).
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free web tool (the former morsecode.scphillips.com now redirects here); optional shop is unrelated to the translator.
opsec: passive
opsecNote: Runs in-browser and you paste your own content; nothing is sent to a target. Avoid pasting genuinely sensitive material into any third-party web tool as a habit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known long-running Morse resource (Stephen C. Phillips' tool, now at morsecode.world). Deterministic conversion — output is verifiable by hand against a Morse chart.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- morsecode.world translator
- Stephen Phillips Morse translator
tags:
- toddington
- curated-directory
- language-translation-tools
source: toddington-resources
lastVerified: '2026-07-28'
enrichment: full
---

# SCPhillips Morse Code Translator

> A free, bidirectional Morse-code translator with sound/light/vibration playback — decode intercepted Morse or encode a message, and hear it.

## When to use
You have a string of dots and dashes (from an image caption, an audio recording, a coded note) and want plain text — or the reverse. Also useful to *play* a decoded message as audio or flashing light to sanity-check a rhythm against a recording. Niche and low missing-persons relevance, but the go-to when Morse turns up in evidence.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://morsecode.world/international/translator.html.
2. To decode: type/paste the Morse (dots `.`, dashes `-`, spaces between letters, `/` or larger gaps between words) into the Morse box; the text appears in the other box.
3. To encode: type text and read the generated Morse.
4. Use the playback controls to hear the sound, see a flashing light, or vibrate the phone; adjust speed/pitch/volume to match a source recording.

## Inputs → Outputs
- **In:** Morse code string, or plain text
- **Out:** the converted text or Morse (no OSINT selectors)
- **Empty/negative result looks like:** garbled output when the input spacing is wrong — Morse depends on inter-letter vs inter-word gaps; if decoding is nonsense, re-check where the spaces fall.

## Gotchas & OpSec
- Human-in-the-loop: none beyond typing.
- OpSec: **passive**, entirely client-side; safe. As general hygiene, don't paste sensitive case material into any web utility.
- Conversion is deterministic — if in doubt, verify a short segment by hand against a standard Morse chart.

## Overlaps ("do both")
- Standalone converter; pair with any cipher/encoding identifier if you aren't sure the signal is Morse at all.

## Trust & verifiability
`trust: community` — a stable, long-lived hobbyist tool; its output is a mechanical transformation you can independently verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scphillips-morse-code-translator |
| category | translation-language |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: free-translation
name: Free Translation
description: Use when you have foreign-language text from a profile, message, or document and want it in your language — returns translated text so you can read and pivot on non-English content.
url: https://translation2.paralink.com/
category: translation-language
path:
- translation-language
- text
bestFor: Fast, no-login browser translation of pasted text across many language pairs.
input: Text
output: Translated text
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free web translator (Paralink); no account required.
opsec: active
opsecNote: Pasted text is sent to Paralink's backend translation providers — do NOT paste sensitive case content, credentials, or PII you must protect. For confidential material use offline translation. No target is contacted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing free online translator; adequate for gisting, but machine translation is imperfect — verify critical wording with a second engine and a human speaker.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- paralink-translation-tool
aliases:
- Paralink translation
- translation2.paralink.com
tags:
- translation
- language
- text
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Free Translation

> A no-login browser translator (Paralink) for quickly gisting foreign-language text you've pulled from a profile, message, or document.

## When to use
Your investigation surfaces text in a language you don't read — a bio, a comment thread, a classified ad, a scanned letter (after OCR). Paste it here for a fast translation so you can understand it and decide what to pivot on. Use it to gist and triage; for anything you'll quote or act on, confirm with a stronger engine and, ideally, a native speaker.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://translation2.paralink.com/.
2. Paste the source text, choose source→target languages (or auto-detect), and translate.
3. Read the output for meaning; watch for names, places, dates, and slang that machine translation may mangle or leave untranslated.
4. Pivot: extract the entities revealed (a `name`, city, org) into your searches. Cross-check the translation on another engine (DeepL/Google) when wording matters.

## Inputs → Outputs
- **In:** foreign-language text (paste)
- **Out:** translated text (gist)
- **Empty/negative result looks like:** garbled or near-identical output — unsupported language, mixed scripts, heavy slang, or transliteration the engine can't parse; try a different engine or transliterate first.

## Gotchas & OpSec
- Human-in-the-loop: none, but treat output as a draft, not an authority.
- OpSec: **active/cloud** — text goes to third-party translation backends. Never paste sensitive/confidential material; use offline translation for that. No subject is contacted.
- Accuracy: names and idioms are frequently wrong; verify proper nouns and any decision-critical phrasing with a second source.

## Overlaps ("do both")
- Pairs with `[[paralink-translation-tool]]` and mainstream engines (Google Translate, DeepL) and with OCR tools like `[[online-ocr-sodapdf]]` — OCR turns a scan into text, this translates it, and a second engine cross-checks the wording.

## Trust & verifiability
`trust: community` — a serviceable free translator for gisting; machine output is imperfect, so corroborate important wording with another engine or a human translator.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | free-translation |
| category | translation-language |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |

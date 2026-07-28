---
id: apertium-org
name: Apertium
description: Use when you have foreign-language text (a `name`, post, or document) and want a free, private machine translation — returns readable translated text, strong on lesser-served language pairs.
url: https://www.apertium.org/index.eng.html
category: translation-language
path:
- translation-language
bestFor: Free open-source machine translation, especially for related/minority language pairs big engines cover poorly.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source; a public web demo plus a self-hostable engine and API.
opsec: passive
opsecNote: The public demo sends your text to apertium.org for translation. Because it's open-source you can self-host the engine to keep sensitive text entirely local — do that for confidential case material rather than pasting it into any hosted translator.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established open-source MT project (rule-based); high quality on its supported pairs, but machine translation of names/idioms can mislead — verify critical strings.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- apertium.org
- apertium machine translation
tags:
- translation
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Apertium

> A free, open-source machine-translation platform with a public web demo — notably good on related and minority language pairs (e.g. Iberian, Nordic, Turkic) that the big engines handle poorly.

## When to use
You've hit foreign-language content during an investigation — a social post, a document, a `name` or place transliteration — and need it in a language you read. Apertium is especially valuable when the source is a smaller/regional language where Google Translate is weak, and when you want an option you can self-host to keep sensitive text off third-party servers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.apertium.org/index.eng.html.
2. Pick the source→target language pair from the dropdowns.
3. Paste the text (or a URL for webpage translation) and read the translated output.
4. For confidential material, install the open-source engine locally (or use the API) so the text never leaves your machine.
5. Pivot: translated content may reveal new selectors (names, locations, handles) — chase those; cross-check any critical phrase with a second translator.

## Inputs → Outputs
- **In:** foreign-language text (no structured selector)
- **Out:** translated text (no structured selector)
- **Empty/negative result looks like:** a garbled or barely-changed output usually means the language pair isn't supported or the input language was misidentified — pick the correct pair or fall back to another engine.

## Gotchas & OpSec
- Rule-based MT is strong on supported pairs but weaker on idioms, slang, and proper nouns — never rely on a machine translation of a name or a legally sensitive phrase without human verification.
- The public demo sends text to apertium.org; self-host for confidential content.
- Language coverage is uneven — great for its supported pairs, absent for others.

## Overlaps ("do both")
- Pairs with Google/DeepL translators — do both on important passages, since each engine handles idioms and rare languages differently and disagreements flag phrases needing a human translator.

## Trust & verifiability
`trust: community` — a mature open-source MT project; reliable within its supported pairs, but as with all machine translation, corroborate any critical string and prefer the self-hosted engine for sensitive text.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | apertium-org |
| category | translation-language |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

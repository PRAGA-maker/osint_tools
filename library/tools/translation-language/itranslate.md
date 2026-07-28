---
id: itranslate
name: iTranslate
description: Use when you have foreign-language text, speech, or an image tied to a subject and need a quick translation — returns translated text/voice across ~100 languages.
url: http://www.itranslateapp.com
category: translation-language
path:
- translation-language
bestFor: Fast text, voice, and camera translation across ~100 languages via web and mobile/desktop apps.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Basic text translation is free; voice, offline, camera/photo and conversation modes are largely behind iTranslate Pro (subscription).
opsec: passive
opsecNote: Pasted or spoken text is sent to iTranslate's servers for translation — do not submit confidential case material, PII, or credentials. Camera/voice modes send images/audio too; for sensitive documents prefer a local/offline translator.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: mobile-app
trust: unverified
trustNote: Established commercial consumer translation app; convenient and broad, but machine output — treat as gist and verify anything decisive.
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
- iTranslate
- itranslateapp.com
tags:
- translation
source: metaosint
lastVerified: '2026-07-28'
enrichment: full
---

# iTranslate

> A consumer translation app (web, mobile, desktop) doing text, voice, and camera translation across ~100 languages — a quick gist tool for foreign-language material in a case.

## When to use
Low-relevance, language-support only. Reach for it when a subject's post, message, document, sign, or spoken clip is in a language you don't read and you need a fast translation — text you paste, a photo of text (camera mode), or audio (voice mode). It returns translated text/voice, not any intelligence about a person. For anything you'll cite, verify with a second engine or a human translator.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Use the web translator at the iTranslate site, or install the mobile/desktop app.
2. Pick source/target languages (auto-detect for source usually works).
3. Enter text, or use camera mode on an image of foreign text, or voice mode for speech (voice/camera/offline are Pro features).
4. Read the translation for gist; switch languages or re-run to sanity-check odd output.
5. Pivot: use the gist to triage, then route anything decisive through a stronger translation or a qualified human.

## Inputs → Outputs
- **In:** foreign-language text, image of text, or speech (not a personal selector)
- **Out:** translated text/voice (no personal selectors)
- **Empty/negative result looks like:** a Pro-only feature is gated behind a subscription prompt, or a low-quality/garbled translation for a hard language pair — fall back to another engine.

## Gotchas & OpSec
- Free tier is text-focused; voice, camera, offline and conversation modes typically require the paid subscription.
- Machine translation — treat every output as gist; confirm anything evidentiary with a second source or human translator.
- Don't submit confidential case text/PII; camera and voice modes also upload images/audio to the service.

## Overlaps ("do both")
- Cross-check with another machine-translation engine — running a doubtful passage through a second translator catches meaning-changing errors, which matters when the text drives a decision.

## Trust & verifiability
`trust: unverified` — an established commercial consumer translation app. Convenient and broad in language coverage, but the output is machine translation; verify anything you'll rely on.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | itranslate |
| category | translation-language |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | mobile-app |
| opsec | passive |
| human-in-loop | no |

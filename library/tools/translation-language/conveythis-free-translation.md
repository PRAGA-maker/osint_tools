---
id: conveythis-free-translation
name: ConveyThis Free Translation
description: Use when you have a foreign-language website and want it rendered in your language — returns an auto-translated view of the site across 200+ languages.
url: https://www.conveythis.com
category: translation-language
path:
- translation-language
bestFor: Auto-translating an entire foreign-language website into a language you read.
selectorsIn:
- domain
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier translates a site into one language up to a word limit; more languages/words and advanced features (SEO, human editing) are paid. Primarily aimed at site owners, but the translation engine is usable for reading.
opsec: passive
opsecNote: If you paste a target URL into ConveyThis' translator, its servers fetch and process that page — so the fetch comes from ConveyThis, not you, but you disclose the URL of interest to a third party. For quick reads, a general machine translator (Google/DeepL) is lower-footprint.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: ConveyThis is an established commercial website-localization service using machine translation (with optional human review); reliable engine, but a vendor product built for site owners rather than investigators.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ConveyThis
- conveythis translation
tags:
- toddington
- language-translation-tools
- website-translation
source: toddington-resources
lastVerified: '2026-08-04'
enrichment: full
---

# ConveyThis Free Translation

> A website-translation service (200+ languages) you can use to read a foreign-language site in your own language when a single-string translator isn't enough.

## When to use
Your subject or lead lives on a foreign-language website — a regional forum, a local business site, a non-English social page — and you need to read it in full, in context, rather than pasting fragments into a translator. ConveyThis machine-translates whole sites across 200+ languages, which is useful for working through a foreign-language source end-to-end. (Its core product is for site owners localizing their own sites, but the engine reads for translation too.)

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.conveythis.com and use its translation/demo entry (or the free plan) to point at the target site.
2. Select the source and your target language (200+ supported).
3. Read the translated rendering; use it to understand the page's content, names, places and claims.
4. For a specific passage, copy the original text into a fragment translator to double-check the machine rendering.
5. Pivot: names/places recovered from the translated page feed person/location searches in the original language.

## Inputs → Outputs
- **In:** a foreign-language site `domain`/URL (or text)
- **Out:** a machine-translated rendering — comprehension, not new person data
- **Empty/negative result looks like:** garbled or partial translation on JS-heavy or login-walled pages, or a hit against the free word limit; fall back to Google Translate/DeepL for the passage.

## Gotchas & OpSec
- Built for site owners, not investigators — for a quick read a general translator (Google/DeepL) is faster and leaks less.
- Machine translation errs on names, idioms and legalese; verify critical strings against the original.
- Submitting a target URL discloses your interest to ConveyThis; weigh that before use.

## Overlaps ("do both")
- Complements general machine translators and `[[synonyms-net]]` — use ConveyThis for whole-site reading, a fragment translator for precision, and a thesaurus to expand keywords across languages.

## Trust & verifiability
`trust: community` — a reputable commercial translation vendor; the engine is dependable for gist, but treat machine output as a reading aid and confirm names/facts against the source text.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | conveythis-free-translation |
| category | translation-language |
| selectorsIn → selectorsOut | domain → (translated content) |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

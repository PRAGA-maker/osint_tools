---
id: linguee-english-french-dictionary
name: Linguee Dictionary
description: Use when you have foreign-language text (a `name`, post, or document snippet) and want an accurate translation shown with real bilingual example sentences — aids interpretation of other selectors.
url: https://www.linguee.com
category: translation-language
path:
- translation-language
bestFor: Translating words and phrases with authentic, in-context bilingual example sentences drawn from real documents.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free web dictionary (owned by DeepL); no account or payment needed.
opsec: passive
opsecNote: You paste text into a third-party service (Linguee/DeepL), which logs queries — don't paste sensitive or uniquely identifying case text; translate the minimum needed and vary phrasing if it matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Reputable bilingual dictionary, now part of DeepL; strong for European-language nuance because it shows how phrases were actually translated in real bilingual sources.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Linguee
- linguee.com
tags:
- toddington
- curated-directory
- language-translation-tools
- translation
- dictionary
source: toddington-resources
lastVerified: '2026-07-28'
enrichment: full
---

# Linguee Dictionary

> A bilingual dictionary that shows not just a word's translation but how it was actually rendered across thousands of real translated documents — the context a plain translator misses.

## When to use
You're working foreign-language material — a subject's social posts, a name/nickname, a document, a place description — and a machine translation is too flat to trust. Linguee shows a word or short phrase alongside authentic example sentences from real bilingual corpora (EU texts, company sites, etc.), which helps you judge idiom, slang, and register that affect how you interpret a lead. It's an interpretation aid rather than a selector-pivot tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.linguee.com and pick the language pair (despite the legacy "English-French" name, Linguee covers many pairs — German, Spanish, Portuguese, Dutch, and more).
2. Type the word or short phrase you need to understand.
3. Read the dictionary entry plus the two-column **example sentences** showing source and translation in real context.
4. For long passages, use it to disambiguate specific terms after a bulk machine translation elsewhere; Linguee is best at word/phrase level, not whole documents.
5. Pivot: a correctly interpreted nickname, place name, or idiom feeds back into your name/geolocation searches with the right spelling and meaning.

## Inputs → Outputs
- **In:** a word or short phrase in a source language
- **Out:** translations with in-context bilingual example sentences (interpretation, not a new selector)
- **Empty/negative result looks like:** "no results" for very rare terms, proper nouns, or slang not in the corpus — fall back to a full-text machine translator or a native-speaker check.

## Gotchas & OpSec
- Best for words/phrases, not paragraph translation — pair it with a full-text translator for long text.
- OpSec: passive but you're feeding text to DeepL/Linguee; keep case-identifying strings out of it where possible.
- Example sentences come from third-party documents and can carry their own errors — weigh several examples, not one.

## Overlaps ("do both")
- Pair with a full-text machine translator: translate the whole passage there, then use Linguee to nail the specific terms that machine output got wrong or ambiguous.

## Trust & verifiability
`trust: community` — a well-regarded dictionary backed by DeepL; its strength (real-corpus examples) is also its caveat, since those source translations are third-party and occasionally imperfect.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | linguee-english-french-dictionary |
| category | translation-language |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

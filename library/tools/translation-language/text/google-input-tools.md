---
id: google-input-tools
name: Google Input Tools
description: Use when a lead is in a non-Latin script and you need to TYPE it accurately (queries, names, addresses) — an input helper, not a subject lookup (no selectors out).
url: https://www.google.com/inputtools/
category: translation-language
path:
- translation-language
- text
bestFor: Typing names, addresses, and search terms in non-Latin scripts (Arabic, Cyrillic, Devanagari, CJK, etc.) via on-screen keyboards and transliteration so your queries match local-language sources.
selectorsIn:
- name
selectorsOut: []
status: live
pricing: free
costNote: Free Google service; the Chrome extension and on-page tool need no account.
opsec: passive
opsecNote: A client-side typing aid — it does not query any target. As with any Google tool, what you type may be processed by Google; don't paste truly sensitive case data, and note keystrokes for transliteration are sent to Google's service.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Google product; it only produces text, so there is no third-party data-quality risk.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Google Input Tools
- Google transliteration
tags: []
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Google Input Tools

> Google's free on-screen keyboards and transliteration engine — a support tool that lets you type accurate non-Latin queries so foreign-language searches actually hit.

## When to use
Not a lookup — an enabler. When a subject's name, an address, or a place is in a script you can't type (Arabic, Cyrillic, Devanagari, Thai, Chinese, Korean…), use this to produce the correct native-script text, then paste it into search engines, maps, or registries. Searching a Russian name in Cyrillic or an Arabic name in Arabic script surfaces local sources that a transliterated Latin spelling misses entirely.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.google.com/inputtools/try/ (or install the Chrome extension for typing anywhere).
2. Pick the target language/script.
3. Type phonetically (transliteration mode) or tap the on-screen keyboard to compose the native text; the tool converts as you go.
4. Copy the resulting native-script string into your actual search/map/registry query.
5. Pivot: run the native-script name/term through search engines, social platforms, and local directories that index that language.

## Inputs → Outputs
- **In:** `name` / place / term (your intended text)
- **Out:** none about a subject — it returns the same text rendered in the target script for you to reuse.
- **Empty/negative result looks like:** wrong transliteration produces a nonsensical native string — verify by back-translating or checking the rendered word against a known reference before searching.

## Gotchas & OpSec
- Transliteration is phonetic and approximate; proper nouns can have multiple valid spellings — try variants.
- OpSec: passive on the target's side. Keystrokes for transliteration are sent to Google's servers, so avoid typing genuinely sensitive identifiers you wouldn't want logged; it's a convenience tool, not a secure one.

## Overlaps ("do both")
- Use alongside any translation tool: translate to understand meaning, use Input Tools to correctly TYPE the native-script query — different jobs, both needed for foreign-language OSINT.

## Trust & verifiability
`trust: trusted` — a first-party Google utility that only generates text; there is no data source to be wrong, only your transliteration choices to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-input-tools |
| category | translation-language |
| selectorsIn → selectorsOut | name → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

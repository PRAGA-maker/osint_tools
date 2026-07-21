---
id: awesome-translations-list
name: Awesome Translations list
description: Use when you have foreign-language `name`, `address` or document text and want a curated menu of translation/transliteration tools to render it into a searchable form — returns tool links, not translations.
url: https://github.com/mbiesiad/awesome-translations#tools
category: translation-language
path:
- translation-language
bestFor: Picking the right translation/transliteration/dictionary tool when a lead is in a language or script you can't search directly.
selectorsIn:
- name
- address
selectorsOut:
- name
- address
status: live
pricing: free
costNote: The list is a free open-source GitHub "awesome" page; the tools it links to are mostly free (a few freemium).
opsec: passive
opsecNote: Reading a GitHub list leaks nothing. When you later paste target text into a downstream machine-translation service, remember that service now holds that text — for sensitive names/documents prefer offline or self-hosted translators the list also catalogues.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community "awesome-*" list maintained by mbiesiad on GitHub; a curated index, quality of linked tools varies.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- awesome-translations
- mbiesiad awesome translations
tags:
- language-tools
- tool-collection
- transliteration
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# Awesome Translations list

> A curated GitHub index of translation, transliteration and dictionary tools — the reference you open when a lead is in a script or language you can't yet search.

## When to use
A key selector — a `name`, `address`, ID document, or social post — is in a language or writing system (Cyrillic, Arabic, CJK, etc.) you can't query effectively. Before you can pivot, you need to translate it or transliterate it into a Latin-script variant to run in Western tools. This list points you to the appropriate translator, transliterator, or bilingual dictionary rather than defaulting to one generic engine.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/mbiesiad/awesome-translations#tools.
2. Scan the "Tools" section for the category you need (machine translation, transliteration, OCR-to-translate, dictionaries).
3. Pick a tool suited to your language pair and privacy needs (offline vs. cloud).
4. Run your source text through it to get a Latin-script or English rendering.
5. Pivot: feed the transliterated `name`/`address` into people-search, social, or public-records tools that only index Latin script.

## Inputs → Outputs
- **In:** foreign-language `name`, `address`, or free text
- **Out:** links to tools that yield translated/transliterated `name` / `address` variants to search on
- **Empty/negative result looks like:** the list has no tool for your exact language pair — fall back to a major multilingual engine, and cross-check the transliteration (multiple romanization schemes exist for the same name).

## Gotchas & OpSec
- This is a directory, not a translator — it produces no translations itself.
- Transliteration is lossy: one foreign name can romanize several ways (e.g. Yury / Yuri / Iurii). Generate variants and search all of them.
- OpSec: reading the list is passive; the privacy exposure comes from whatever cloud translator you later feed target text into — for sensitive material prefer the offline options catalogued here.

## Overlaps ("do both")
- Pairs with name-variant/alias generators — this gets you across the language barrier, and a name-permutation tool then expands the romanized result into searchable spelling variants.

## Trust & verifiability
`trust: community` — an open-source "awesome" list on GitHub curated by mbiesiad; the index is trustworthy as a menu, but vet each linked tool individually since maintenance and quality vary.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | awesome-translations-list |
| category | translation-language |
| selectorsIn → selectorsOut | name, address → name, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

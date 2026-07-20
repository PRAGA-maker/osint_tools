---
id: translate-shell
name: Translate Shell
description: Use when you have foreign-language text (a post, `name`, bio, or document) and want fast terminal translation/transliteration — returns readable English (or any target) plus language detection.
url: https://github.com/soimort/translate-shell
category: translation-language
path:
- translation-language
bestFor: Quickly translating, detecting, or transliterating foreign-language content from the command line while processing OSINT collection.
selectorsIn:
- name
- username
selectorsOut:
- name
status: live
pricing: free
costNote: Free and open-source (Unlicense); no API key needed for default web-engine backends.
opsec: passive
opsecNote: It sends the text you translate to the chosen web engine (Google/Bing/Yandex, etc.), so do NOT paste sensitive investigative notes verbatim. Translation queries can be logged by that engine; translate only the target's public text, and consider self-hosted engines for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: A popular, long-maintained open-source project (soimort/translate-shell); shipped in the Trace Labs OSINT VM and packaged in major Linux distros.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- trans
- translate-shell
tags:
- translation
- cli
- language
source: tracelabs-repos
lastVerified: '2026-07-20'
relatedTools:
- you-get
---

# Translate Shell

> A command-line translator (`trans`) over Google/Bing/Yandex and more — for fast, scriptable translation, language detection, and transliteration during OSINT collection.

## When to use
You're processing foreign-language material — a subject's social post, bio, `username`, place name, or a scraped document — and want it readable without leaving the terminal or opening a browser tab per snippet. Translate Shell detects the source language, translates to your target, and can transliterate non-Latin scripts (useful for turning a name into a searchable Latin form, or vice-versa). Because it's CLI, it scripts cleanly over batches of collected text.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `apt install translate-shell` (or `brew install translate-shell`); the command is `trans`.
2. Translate: `trans :en "متن فارسی"` → English; auto-detect source with `trans -b :en "text"` for brief output.
3. Detect language: `trans -id "text"`; transliterate: `trans -t :en -show-original y "текст"` (or use the translation's phonetic line).
4. Batch it: pipe or loop over collected strings for bulk translation of scraped content.
5. Pivot: transliterated `name`/`username` forms feed searches on the original-language platforms and search engines.

## Inputs → Outputs
- **In:** foreign-language text — a `name`, `username`, bio, or document snippet
- **Out:** translated/transliterated text (a searchable `name` form), detected source language
- **Empty/negative result looks like:** garbled or empty output usually means a network/engine error or an unsupported language pair — switch engine (`-e bing`/`-e yandex`) and retry.

## Gotchas & OpSec
- It calls external web engines — your text is sent to Google/Bing/Yandex and may be logged; never paste sensitive case notes, only the target's public text.
- Machine translation mangles idiom, slang, and names — treat output as a gist, and verify critical terms with a human or second engine.
- Transliteration schemes vary; try multiple romanizations of a name when searching.

## Overlaps ("do both")
- Pairs with scraping/download tools like `[[you-get]]` — grab the foreign-language content, then run it through `trans` to make it searchable and readable.

## Trust & verifiability
`trust: trusted` — a widely used, well-maintained open-source tool; reliability of the *translation* depends on the backend engine, so corroborate important phrases across engines.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | translate-shell |
| category | translation-language |
| selectorsIn → selectorsOut | name, username → name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |

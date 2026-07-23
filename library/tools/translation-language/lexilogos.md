---
id: lexilogos
name: Lexilogos
description: Use when you have a `name` or text in a foreign language/script and want dictionaries, transliteration keyboards, and etymology tools to read or romanize it — supports cross-script `name` work.
url: https://www.lexilogos.com
category: translation-language
path:
- translation-language
bestFor: A portal of 400+ language dictionaries plus on-screen keyboards for typing and transliterating non-Latin scripts.
selectorsIn:
- name
selectorsOut:
- name
status: live
pricing: free
costNote: Free to use, supported by donations; no account or payment required.
opsec: passive
opsecNote: A reference site — you look up words and type characters locally. No selector about the subject is sent anywhere identifying; treat it as a passive language aid.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Long-running independent scholarly portal (Xavier Nègre, 2002–present); it links out to many third-party dictionaries whose quality varies.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- lexilogos.com
tags:
- translation
- transliteration
- dictionaries
source: metaosint
lastVerified: '2026-07-23'
relatedTools:
- lexilogos-com
---

# Lexilogos

> A vast multilingual reference hub — dictionaries, maps, and on-screen keyboards for 400+ languages — most useful in OSINT for reading and romanizing names in unfamiliar scripts.

## When to use
You have a `name`, place, or short text in a language or script you can't read — Cyrillic, Arabic, Greek, Han, Devanagari, Georgian, etc. — and need to transliterate it into Latin characters (or type it correctly into another tool) and understand what it means. Lexilogos gives you the keyboard to enter the script and the dictionaries to decode it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.lexilogos.com and pick the target language.
2. For entry: use the language's on-screen keyboard to type names/words in the native script, then copy them into your search or translation tool.
3. For decoding: follow the language page's linked dictionaries, transliteration guides, and name/etymology resources.
4. Pivot: a correctly romanized `name` feeds username/social searches and people-search engines that would otherwise fail on the original script.

## Inputs → Outputs
- **In:** `name` or foreign-language text/script
- **Out:** transliterated/romanized `name`, definitions, script-entry keyboard output
- **Empty/negative result looks like:** a language or dialect Lexilogos doesn't cover, or a linked external dictionary that is offline — fall back to a dedicated transliteration/translation service.

## Gotchas & OpSec
- It is a portal, not a single translation engine — much of its value is links out to third-party dictionaries of varying quality and uptime.
- Transliteration schemes differ (e.g. multiple romanizations of the same Cyrillic name); generate several variants and search all of them.
- OpSec: **passive** — a reference/typing aid, nothing about the subject is disclosed.

## Overlaps ("do both")
- Pairs with machine-translation tools and transliteration utilities — Lexilogos helps you *enter and understand* a foreign script, while a translator renders full sentences.

## Trust & verifiability
`trust: unverified` — a respected, long-lived scholarly portal, but it aggregates external resources; verify a specific romanization against a second source before treating it as canonical.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lexilogos |
| category | translation-language |
| selectorsIn → selectorsOut | name → name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

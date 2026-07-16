---
id: cambridge-dictionary
name: Cambridge Dictionary
description: Use when you have a foreign-language word/phrase from a subject's posts or documents and want an authoritative definition and bilingual translation — returns meanings, pronunciation, and equivalents.
url: https://dictionary.cambridge.org/
category: translation-language
path:
- translation-language
- text
bestFor: Authoritative word-level definitions and bilingual dictionary/translation lookups.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free to use; no account required.
opsec: passive
opsecNote: A plain dictionary query to Cambridge University Press — nothing about your subject is submitted beyond the word you look up, and no target is contacted. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by Cambridge University Press; an authoritative reference dictionary. Definitions and translations are editorially curated, not machine-scraped.
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
- Cambridge English Dictionary
- dictionary.cambridge.org
tags:
- translation
- dictionary
- language
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
---

# Cambridge Dictionary

> An authoritative free dictionary and bilingual translator — for pinning down the exact meaning of a word or phrase from a subject's foreign-language content.

## When to use
You've hit an unfamiliar word, slang term, or short phrase in a subject's posts, messages, or documents and need a precise, trustworthy meaning or a translation into/out of English. Cambridge gives editorially curated definitions, pronunciations (IPA + audio), example usage, and bilingual equivalents across many language pairs — better for careful word-level accuracy than a raw machine translator when a single term is load-bearing. A supporting language aid; low direct missing-persons relevance but useful when working across languages.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://dictionary.cambridge.org/.
2. (Optional) pick the dictionary/translation pair (e.g. English, English–Spanish, English–Chinese).
3. Enter the word or short phrase.
4. Read the definition(s), part of speech, pronunciation, examples, and translated equivalent.
5. Pivot: use the confirmed meaning to interpret a message correctly, or feed a translated term into further searches; for full sentences use a dedicated MT engine instead.

## Inputs → Outputs
- **In:** a word or short phrase (text) — not a person-selector
- **Out:** definitions, part of speech, pronunciation (IPA + audio), examples, and bilingual translations
- **Empty/negative result looks like:** "No results" for very rare slang, proper nouns, or misspellings — try a corrected spelling, the root form, or a slang-specific resource.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: fully passive — a standard dictionary lookup; nothing about your investigation is revealed and no subject is contacted.
- It's word/phrase-level, not a sentence/document translator; for running text pair it with a full machine-translation tool.

## Overlaps ("do both")
- Complements full-text machine translators — use the MT engine for whole passages and Cambridge to verify the precise sense of any critical term the MT gets ambiguous.

## Trust & verifiability
`trust: trusted` — an authoritative reference from Cambridge University Press with editorially maintained content; definitions and translations are reliable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cambridge-dictionary |
| category | translation-language |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: wiktionary
name: Wiktionary
description: Use when you hit an unfamiliar word, slang, or foreign term in evidence and want its meaning, etymology, and translations — returns definitions, pronunciations, and cross-language equivalents.
url: https://en.wiktionary.org/
category: translation-language
path:
- translation-language
- text
bestFor: Decoding slang, jargon, dialect, or foreign words encountered in a subject's content.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, non-profit (Wikimedia). No account needed to read.
opsec: passive
opsecNote: A public dictionary lookup; the target is never involved and reading is unattributed. Editing is public and attributable — never edit during an investigation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Crowdsourced Wikimedia project; broadly reliable for common terms, but entries vary in quality and individual definitions can be incomplete — corroborate niche slang against usage in context.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- en.wiktionary.org
- Wiktionary dictionary
tags:
- translation
- dictionary
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Wiktionary

> The crowdsourced multilingual dictionary — a fast way to decode slang, jargon, dialect, and foreign words that appear in a subject's posts, messages, or documents.

## When to use
You've hit a word you don't understand while reading evidence: internet slang, a regional dialect term, a foreign word, an abbreviation, a piece of subculture jargon. Wiktionary gives the definition, pronunciation, etymology, and — usefully — translation sections linking the term across languages. In OSINT it's a supporting comprehension aid, not a source of intelligence about a person, so relevance is low; but understanding what a subject actually wrote (including which language/region a term signals) can be a small pivot in itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://en.wiktionary.org/ and search the word or phrase.
2. Read the definition(s), noting the language section — the same spelling may have entries under several languages, hinting at the writer's origin.
3. Check **Etymology** and **Translations** to see origin and cross-language equivalents; use other-language editions (e.g. de.wiktionary.org) for local slang the English edition lacks.
4. For a term still opaque, note it as untranslatable-here and try a slang-specific resource or the term in context.
5. Pivot: a term that pins a dialect/region can narrow a subject's geography; a translated term feeds broader searches.

## Inputs → Outputs
- **In:** a word or phrase
- **Out:** definitions, pronunciation, etymology, and translation equivalents
- **Empty/negative result looks like:** no entry — the term is too new, too niche, a proper noun, or misspelled. Try the language-specific Wiktionary edition or a dedicated slang dictionary.

## Gotchas & OpSec
- Crowdsourced coverage is uneven: excellent for established words, thin or absent for fresh slang and hyper-local dialect.
- A dictionary definition may miss the connotation a term carries in a specific community; weigh it against how the subject actually used it.
- OpSec: **passive** reading. Editing is public and attributable — don't.

## Overlaps ("do both")
- Pairs with full-sentence machine translation (e.g. a translate tool) — Wiktionary explains a single hard word; a translator handles whole passages.

## Trust & verifiability
`trust: trusted` — a reputable Wikimedia project, reliable as a dictionary for common terms; treat individual crowdsourced entries as good-but-verifiable, and confirm niche slang against real usage.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wiktionary |
| category | translation-language |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

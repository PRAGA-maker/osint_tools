---
id: word-reference
name: Word Reference
description: Use when you have foreign-language text (a bio, message, or listing) and want an accurate word-level translation with conjugations and idiom notes — returns translations, definitions and usage examples.
url: https://www.wordreference.com/
category: translation-language
path:
- translation-language
- text
bestFor: Precise word- and phrase-level translation with conjugation tables and native-speaker forum discussion of idioms.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free to use in the browser; ad-supported, no account required. Mobile apps are free too.
opsec: passive
opsecNote: Dictionary lookups go only to WordReference and never touch the target or their content host, so the subject learns nothing. Do not paste sensitive raw case text into any third-party site out of habit — translate only the fragment you need.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-established (since 1999) reference dictionary with human-curated bilingual dictionaries and heavily moderated language forums; not a data broker.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- wordreference-translator
aliases:
- WordReference
- wordreference.com
tags:
- translation
- dictionary
- language
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# Word Reference

> A high-quality bilingual dictionary and language-forum site, best when you need to understand a specific foreign word, idiom, or verb form rather than machine-translate a whole page.

## When to use
You have a short piece of foreign-language text — a social-media bio, a classified-ad description, a chat message, a place name modifier — and machine translation (Google/DeepL) is giving you a garbled or ambiguous result. WordReference is where you check what a single word or idiom actually means, resolve slang, and confirm a verb tense so you interpret a lead correctly rather than acting on a mistranslation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.wordreference.com/ and pick the language pair from the top menu (e.g. Spanish→English, French→English, Italian, German, Portuguese, and more).
2. Type the word or short phrase into the search box and submit.
3. Read the dictionary entry: primary and secondary senses, part of speech, register (formal/slang), and example sentences with translations.
4. For verbs, click the conjugation link to get the full tense table — useful for identifying who did what and when in a foreign message.
5. Scroll to the linked forum threads where native speakers debate tricky idioms and regional usage; this often resolves slang that no dictionary captures.
6. Pivot: use the confirmed meaning to re-read the source document, or feed a corrected place/name spelling into a geolocation or people-search tool.

## Inputs → Outputs
- **In:** foreign-language word or short phrase (free text — no OSINT selector)
- **Out:** translations, definitions, conjugation tables, idiom/usage notes, forum discussion
- **Empty/negative result looks like:** "No results found" with spelling suggestions — the word may be a proper noun, a typo, or slang too new/regional for the dictionary; check the forums or fall back to a full-text translator.

## Gotchas & OpSec
- Not a document translator: it works word/phrase by phrase, not on whole pages. For bulk text, machine-translate first, then use WordReference to disambiguate the words that don't make sense.
- Coverage is deepest for European languages plus Chinese, Japanese, Korean, Arabic and a few others; some pairs only route through English.
- OpSec: fully passive — pasting a foreign word here does not signal anything to the subject. Still, don't paste identifying case details you don't need translated.

## Overlaps ("do both")
- Pairs with `[[wordreference-translator]]` — use a general machine translator for the gist of a long passage, then WordReference to nail the specific words and idioms that determine meaning.

## Trust & verifiability
`trust: trusted` — a two-decade-old, human-curated dictionary and moderated forum resource, not a scraper or broker; treat its dictionary content as reliable and its forum threads as informed opinion.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | word-reference |
| category | translation-language |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

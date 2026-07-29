---
id: definitions-net
name: Definitions.net
description: Use when you have a foreign or unfamiliar term from collected material and want a definition plus translation in 40+ languages — returns plain-language meaning and cross-language equivalents.
url: http://www.definitions.net
category: translation-language
path:
- translation-language
bestFor: Quickly defining and translating unfamiliar words/terms encountered during OSINT review.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, ad-supported (part of the STANDS4 network); optional ad-free premium. A developer API exists.
opsec: passive
opsecNote: Passive — you are looking up dictionary terms, not touching a subject. Avoid pasting sensitive, unique target phrases you don't want logged by a third-party site; look up individual words instead.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community/crowd-sourced reference (STANDS4 network) aggregating WordNet, Wiktionary, Webster and user contributions; quality varies with the source entry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- definitions.net
- STANDS4 Definitions
tags:
- toddington
- curated-directory
- language-translation-tools
- dictionary
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# Definitions.net

> A free multilingual dictionary that defines a term from multiple reference sources and offers translations in 40+ languages.

## When to use
While reviewing collected material you hit a word, slang term, acronym or foreign phrase you don't understand and need a fast definition plus a rough translation. It aggregates several dictionaries (WordNet, Wiktionary, Webster and others) and adds pronunciation, etymology and usage examples — a support/analysis utility, not a source of OSINT selectors.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.definitions.net.
2. Type the word or term into the search box.
3. Read the aggregated definitions (each labelled by source), plus pronunciation, examples and etymology.
4. For a different language, use the translation panel to see equivalents in 40+ languages.
5. Pivot: a correctly understood term/name can change how you interpret and re-query the underlying material.

## Inputs → Outputs
- **In:** a word or term (no OSINT selector)
- **Out:** definition(s), usage examples, translations — contextual understanding, not selectors
- **Empty/negative result looks like:** "no definition found" for very niche slang, misspellings, or proper nouns — try a general search engine or a slang-specific resource instead.

## Gotchas & OpSec
- Human-in-the-loop: none; plain lookup.
- OpSec: passive; still, don't paste unique sensitive strings you'd rather not log on a third-party site — look up single words.
- Some entries are user-contributed and may be low quality; prefer the entries attributed to established dictionaries.

## Overlaps ("do both")
- Complements dedicated translation tools like `[[lexicool-translation]]` — use Definitions.net when you need the *meaning* of a term, a translation aggregator when you need to convert whole passages.

## Trust & verifiability
`trust: community` — a crowd-sourced aggregator; cross-check any critical definition against the named upstream dictionary rather than relying on user-submitted entries.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | definitions-net |
| category | translation-language |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

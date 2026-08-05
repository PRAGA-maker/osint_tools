---
id: one-look-reverse-dictionary
name: OneLook Reverse Dictionary
description: Use when you half-remember a word/term or need the right keyword for a search — describe the concept and get candidate words back to feed into other OSINT searches.
url: https://www.onelook.com/reverse-dictionary.shtml
category: search-engines
path:
- search-engines
bestFor: Turning a vague description ("word for someone who makes barrels") or a wildcard pattern into concrete search terms and keywords.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free to use; no account required.
opsec: passive
opsecNote: You query a generic dictionary service with concepts, not target identifiers — no OSINT subject data is exposed as long as you enter descriptions rather than case-specific PII. Nothing links the query to your investigation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running, well-known word-lookup service (OneLook) drawing on Wiktionary/Wikipedia and many dictionaries; a research aid, not a source of OSINT records.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- OneLook
- Reverse Dictionary
tags:
- keywords-discovery-and-research
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# OneLook Reverse Dictionary

> A concept-to-word lookup: describe what you mean in plain language (or a letter pattern) and get candidate words and terms back — a keyword-discovery aid for building better searches.

## When to use
You're stuck on the right term to search for — a profession, jargon word, slang, an object, or a half-remembered word — and you want the precise keyword before running a name/username/topic search elsewhere. Also handy for wildcard/pattern recovery (you know some letters of a term seen in a document). This produces search vocabulary, not OSINT records.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.onelook.com/reverse-dictionary.shtml.
2. Type a description ("urge to travel"), a "type of..." query, or a wildcard pattern (`b*ll`, `??ret`).
3. Read the ranked candidate words; reorder by relevance, length, or popularity to narrow down.
4. Pivot: take the recovered term into a search engine, a niche-community search, or a social-media keyword search to find the subject's content.

## Inputs → Outputs
- **In:** a concept/description or letter pattern (not an OSINT selector)
- **Out:** candidate words/terms (search keywords; no structured selectors)
- **Empty/negative result looks like:** no relevant candidates — the description is too abstract or the term is a proper noun/brand the dictionary doesn't cover; rephrase or try a general web search.

## Gotchas & OpSec
- It's a linguistic aid, not an investigative data source — outputs are vocabulary, never records about a person.
- Proper nouns, brand names and very recent slang may be missing.
- No login and no target PII involved, so OpSec exposure is negligible.

## Overlaps ("do both")
- Feeds any keyword-driven search tool — use it upstream to get the exact term, then run that term through a search engine or social-media search.

## Trust & verifiability
`trust: community` — a reputable, long-established word service. It never claims to be an OSINT record source; treat its output purely as candidate keywords to verify in the real search.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | one-look-reverse-dictionary |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

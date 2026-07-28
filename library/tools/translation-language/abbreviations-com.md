---
id: abbreviations-com
name: Abbreviations.com
description: Use when you have an unknown acronym or abbreviation from a document/chat/handle and want its expansions — returns candidate meanings to decode jargon, org names, and codes.
url: http://www.abbreviations.com
category: translation-language
path:
- translation-language
bestFor: Decoding an acronym or abbreviation into its possible full meanings across many domains.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free to search (part of the STANDS4 reference network); no account.
opsec: passive
opsecNote: You're looking up a generic abbreviation in a public dictionary — no target is involved and nothing sensitive is exposed. Passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large community/crowd-contributed acronym dictionary (STANDS4); comprehensive but crowd-sourced, so expansions are candidates to judge in context, not authoritative.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- abbreviations.com
- STANDS4 abbreviations
tags:
- translation
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Abbreviations.com

> A large crowd-sourced dictionary of acronyms and abbreviations — paste an unknown short code and get its candidate expansions across business, government, military, tech, medical, and slang domains.

## When to use
You've hit an unfamiliar acronym or abbreviation in a document, chat log, username, or record — an org code, a jargon term, a military/agency abbreviation, an internet shorthand — and need to know what it could stand for so the surrounding content makes sense. A small supporting/decoding tool, not a person-finder.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.abbreviations.com.
2. Enter the acronym/abbreviation and search.
3. Review the ranked list of expansions, each tagged by category/domain (business, governmental, medical, slang, etc.).
4. Pick the expansion that fits the **context** of your source material — several meanings usually exist.
5. Pivot: a decoded org/agency name or jargon term can open a new search thread (e.g. an unfamiliar abbreviation resolving to a company or unit).

## Inputs → Outputs
- **In:** an acronym/abbreviation (no structured selector)
- **Out:** candidate expansions/meanings (no structured selector)
- **Empty/negative result looks like:** no listed expansions — the abbreviation isn't in the crowd database (very niche, misspelled, or invented); try context clues or a domain-specific glossary.

## Gotchas & OpSec
- **Many expansions per acronym** — the tool can't tell you which is right; context decides. Don't over-trust the top result.
- Crowd-sourced, so obscure/domain-specific abbreviations may be missing or wrong.
- Passive; nothing about your case is disclosed.

## Overlaps ("do both")
- Pairs with domain-specific glossaries (military, medical, government) and a plain web search of the acronym plus a context word — do both when the generic dictionary returns too many candidates to disambiguate.

## Trust & verifiability
`trust: community` — a comprehensive but crowd-contributed reference; treat expansions as candidates to confirm against the context they appeared in, not as authoritative definitions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | abbreviations-com |
| category | translation-language |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

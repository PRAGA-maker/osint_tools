---
id: termwiki
name: TermWiki
description: Use when you have a specialised or foreign-language term and want its meaning/translation — returns multilingual definitions and the contributor behind an entry.
url: http://www.termwiki.com
category: search-engines
path:
- search-engines
bestFor: Looking up and translating industry/technical terminology across many languages.
selectorsIn:
- name
selectorsOut:
- name
status: live
pricing: free
costNote: Free to search and read; contributing/editing requires a free account.
opsec: passive
opsecNote: Passive reference lookup; searching a term is not a per-person query. Ordinary browsing, nothing sensitive leaked. Only creating a contributor account leaves a footprint.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowdsourced multilingual terminology wiki (operated by CSOFT); entries are community-contributed, so quality varies by term and language.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- TermWiki
- termwiki.com
tags:
- toddington
- curated-directory
- specialty-search
- terminology
- translation
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# TermWiki

> A crowdsourced multilingual glossary — useful for decoding industry jargon or foreign-language terms that surface in documents, chats, or listings during an investigation.

## When to use
You hit a specialised term, acronym, brand word, or foreign-language phrase in evidence (a forum post, a leaked document, a marketplace listing) and need its meaning or an English equivalent. TermWiki holds community-contributed definitions across many industries and languages, which helps you interpret context and generate better search terms. It is a language/reference aid, not a people-finder — its OSINT value is comprehension and query-building.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.termwiki.com and search the term.
2. Read the definition, industry tag, and translations into other languages.
3. Use the translated or clarified term to build sharper searches in the relevant language on other tools.
4. If an entry names its contributor, that handle is a minor `name`/`social-profile` lead within TermWiki.
5. Pivot: a decoded term feeds keyword searches on marketplaces, forums, and search engines in the right language.

## Inputs → Outputs
- **In:** a term / acronym / foreign phrase
- **Out:** multilingual definitions and translations; occasionally a contributor `name`/handle
- **Empty/negative result looks like:** no entry for the term — it may be too new, misspelled, or non-standard. Fall back to a general search or a domain-specific glossary.

## Gotchas & OpSec
- Entries are user-contributed and uneven; treat a definition as a lead, and confirm critical translations with a second source.
- It is a terminology reference, not an entity database — do not expect to find specific people here.

## Overlaps ("do both")
- Pairs with general dictionaries/translation tools and Wikipedia — TermWiki leans into niche industry jargon those may lack, while they give broader, better-vetted coverage of common terms.

## Trust & verifiability
`trust: community` — a crowdsourced glossary; useful for orientation and translation but community-edited, so verify any definition you rely on against an authoritative source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | termwiki |
| category | search-engines |
| selectorsIn → selectorsOut | name → name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

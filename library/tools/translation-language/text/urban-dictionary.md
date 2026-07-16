---
id: urban-dictionary
name: Urban Dictionary
description: Use when you have slang, a nickname, or a coded term from a subject's posts and want its meaning — returns crowd-sourced definitions that can decode a `username` or in-group language.
url: https://www.urbandictionary.com/
category: translation-language
path:
- translation-language
- text
bestFor: Decoding slang, memes, nicknames and subculture jargon that appear in a subject's messages, usernames or posts.
selectorsIn:
- username
selectorsOut:
- username
status: live
pricing: free
costNote: Free to search and read; no account required.
opsec: passive
opsecNote: Looking up a term reveals nothing about your subject and contacts no one. Passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Entirely crowd-sourced and unmoderated; definitions range from accurate to joke/offensive, so treat them as leads to a meaning, not authority.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- urbandictionary-com
aliases:
- UrbanDictionary
- urbandictionary.com
tags:
- slang
- language
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
---

# Urban Dictionary

> The crowd-sourced dictionary of slang and internet culture — for decoding the jargon, nicknames and coded terms that show up in a subject's own words.

## When to use
You have encountered slang, an abbreviation, a meme reference, a coded drug/subculture term, or a `username`/handle whose meaning is opaque, and you want a quick read on what it likely signifies in online/youth culture. Understanding a subject's language helps interpret their posts, identify in-groups, and spot risk indicators.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.urbandictionary.com/ .
2. Search the term, phrase, or handle component.
3. Read the top community definitions, ranked by up/down votes, with usage examples.
4. Weigh multiple definitions — pick the reading that fits the context you saw it in.
5. Pivot: use the decoded meaning to interpret the source message; if a handle decodes to a subculture/interest, pursue that community on the relevant platform.

## Inputs → Outputs
- **In:** `username` / a slang term or phrase
- **Out:** community definitions and examples that interpret the term (feeding back into understanding a `username` or message)
- **Empty/negative result looks like:** no entry, or only joke/vandal definitions — the term may be too new, too local, or not slang at all; corroborate elsewhere.

## Gotchas & OpSec
- Unmoderated and crowd-sourced: definitions can be wrong, outdated, deliberately fake, or offensive — never treat a single entry as authoritative.
- Meaning is context-dependent; the same term can be innocuous or coded depending on the community.
- OpSec: passive; a lookup signals nothing about your subject.

## Overlaps ("do both")
- Pairs with `[[urbandictionary-com]]` (same resource) and general search: cross-check a coded term with a web search and community context before acting on the interpretation.

## Trust & verifiability
`trust: unverified` — a fully crowd-sourced glossary. Useful for orientation on slang, but each definition is unverified opinion; corroborate any meaning you rely on.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | urban-dictionary |
| category | translation-language |
| selectorsIn → selectorsOut | username → username |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

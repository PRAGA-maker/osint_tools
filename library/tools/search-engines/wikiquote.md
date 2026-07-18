---
id: wikiquote
name: Wikiquote
description: Use when you have a `name` of a notable person and want sourced quotations that corroborate identity and surface associates — returns name and associate.
url: https://en.wikiquote.org
category: search-engines
path:
- search-engines
bestFor: Looking up a notable person's attributed, sourced quotations and the works/people cited alongside them.
selectorsIn:
- name
selectorsOut:
- name
- associate
status: live
pricing: free
costNote: Free, non-profit (Wikimedia Foundation); no account required to read.
opsec: passive
opsecNote: Reading a public wiki is invisible to any subject. No sock puppet needed for reading.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Wikimedia sister project; crowd-edited but each quote is supposed to carry a citation — verify against the cited primary source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- en.wikiquote.org
tags:
- specialty-search
- curated-directory
- toddington
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Wikiquote

> A Wikimedia compendium of sourced quotations — a niche corroboration source for notable people, presenting them through their own documented words and the company they keep.

## When to use
The subject is a public/notable figure (author, politician, academic, entertainer, activist) and you want quick, citation-backed confirmation of who they are and what they have said publicly. A person's page collects attributed quotes with sources, and the "About"/"Quotes about" sections and interwiki links often name `associate`s (people who quoted or were quoted alongside them) and point to the fuller Wikipedia biography. For non-notable subjects there is no page — skip.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://en.wikiquote.org and search the subject's `name` (or browse the "People" portal).
2. On the person's page, read the sourced quotes and note the citations (book, speech, interview, date).
3. Check "Quotes about <person>" and the sidebar links — these name associates and jump to Wikipedia for biography.
4. Pivot: cited sources → primary documents; interwiki link → `[[wikipedia]]`-style biographical detail; named people → `associate` mapping.

## Inputs → Outputs
- **In:** `name`
- **Out:** `name` (confirmed formal name/aliases), `associate` (people quoted with/about them), plus links to fuller biography
- **Empty/negative result looks like:** "no page" / no search match — meaning the subject is not notable enough to have a Wikiquote entry (the common case); not evidence of anything about the person.

## Gotchas & OpSec
- Coverage is limited to notable figures — the overwhelming majority of missing-person subjects will have no page.
- Crowd-edited: treat any quote as a lead until you check the cited source; misattributions happen.
- OpSec: passive read; safe.

## Overlaps ("do both")
- Pairs naturally with Wikipedia and general web search — use Wikiquote for the sourced-words angle and the biography link, then corroborate identity facts on the primary sources it cites.

## Trust & verifiability
`trust: community` — Wikimedia crowd-sourced content; reliable only to the extent each quote carries a verifiable citation, which you should follow before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikiquote |
| category | search-engines |
| selectorsIn → selectorsOut | name → name, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

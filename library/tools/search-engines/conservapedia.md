---
id: conservapedia
name: Conservapedia
description: Use when you have a `name` of a public/political figure and want a biographical article from a US-conservative viewpoint — returns background and `associate` links.
url: http://www.conservapedia.com
category: search-engines
path:
- search-engines
bestFor: Reading a conservative-Christian-POV encyclopedia entry on a notable political, religious or public figure to surface claimed affiliations and framing.
selectorsIn:
- name
selectorsOut:
- associate
status: live
pricing: free
costNote: Free to read and search; editing requires an account but reading does not.
opsec: passive
opsecNote: Reading and searching are anonymous and leak nothing to any subject. Safe to use directly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: An openly partisan wiki (self-described American conservative / fundamentalist Christian viewpoint) widely criticised for factual inaccuracy and bias — treat every claim as opinion to verify elsewhere.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- conservapedia.com
tags:
- toddington
- curated-directory
- specialty-search
- wiki
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Conservapedia

> An active but openly partisan online encyclopedia; useful only for its framing of notable political/religious public figures, never as a neutral fact source.

## When to use
Your subject is a **notable public figure** — a politician, activist, commentator or religious figure — and you want to see how the American-conservative movement characterises them, or to pick up claimed `associate`/affiliation leads that a mainstream encyclopedia omits or frames differently. It has ~59k articles and covers essentially no private individuals, so it is irrelevant for ordinary missing-persons subjects; reach for it only when the target is prominent and the *framing* itself is the intelligence.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.conservapedia.com and use its search box, or Google `site:conservapedia.com "<name>"`.
2. Open the subject's article, if one exists.
3. Read for claimed affiliations, organisations, associates and events — noting these are asserted from a strong ideological angle.
4. Pivot: take any specific name/org/date and verify it against neutral sources (mainstream encyclopedia, primary records) before using it.

## Inputs → Outputs
- **In:** `name` (a notable public figure)
- **Out:** `associate`/affiliation leads and biographical claims (heavily editorialised)
- **Empty/negative result looks like:** no article — the overwhelmingly common case, since coverage is limited to figures the community found ideologically relevant. Absence means nothing about the person.

## Gotchas & OpSec
- **Strong bias and documented inaccuracy.** Nothing here is authoritative; use it to understand a narrative, not to establish facts.
- Coverage is tiny and skewed toward US politics/religion; not a general people-search resource.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with a neutral reference like Wikipedia and with primary-record sources — read Conservapedia only for the partisan framing, and confirm every concrete claim independently.

## Trust & verifiability
`trust: unverified` — an avowedly partisan, error-prone wiki. Treat all content as opinion; every factual-sounding claim must be corroborated from an independent source before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | conservapedia |
| category | search-engines |
| selectorsIn → selectorsOut | name → associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

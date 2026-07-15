---
id: searchenginejournal-com
name: "Google Search Operators cheat sheet (Search Engine Journal)"
description: Use when you have a `name`/handle/domain and want the full syntax of Google advanced operators to build a precise dork — returns a reference for constructing queries that surface `social-profile`/`name` hits.
url: https://www.searchenginejournal.com/google-search-operators-commands/215331/
category: search-engines
path:
- search-engines
bestFor: A maintained reference list of working Google search operators for building OSINT dorks.
selectorsIn:
- name
selectorsOut:
- name
- social-profile
status: live
pricing: free
costNote: Free article; no account or payment. It documents Google operators — Google search itself is also free.
opsec: passive
opsecNote: Reading the cheat sheet is passive. The dorks you build from it run against Google — do those from a sock-puppet browser/IP, and remember advanced operators can trip Google's bot detection (CAPTCHA) after volume.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Search Engine Journal is an established SEO industry publication; the operator list is well-maintained and flags which operators still work vs. deprecated ones.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- google-com-86
aliases:
- Google advanced operators
- Google dork reference
tags:
- searchengines
- Search Engines
- google-dorking
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Google Search Operators cheat sheet (Search Engine Journal)

> A reference page listing Google's advanced search operators (`site:`, `intitle:`, `inurl:`, `filetype:`, `"…"`, `AROUND(n)`, etc.) and which ones still work — the raw material for building OSINT dorks.

## When to use
You are about to search Google for a person and want to narrow it precisely — restrict to a domain, a filetype, a title phrase, or a proximity match. This is a reference/knowledge entry, not an interactive tool: you read it to learn the syntax, then apply the operators in a normal Google search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the URL and skim the operator table; note the section separating operators that still function from deprecated ones.
2. Pick the operators that fit your goal — e.g. `site:linkedin.com/in "Jane Doe"`, `filetype:pdf "Jane Doe" resume`, `intext:"07123" site:facebook.com`.
3. Combine with Boolean logic (`AND`, `OR`, `-`, quotes) to constrain results.
4. Run the query in Google (ideally with search settings/region matched to the target).
5. Pivot: hits feed people-search, social-profile, and document tools.

## Inputs → Outputs
- **In:** `name` (plus any known selector to constrain the dork)
- **Out:** the operator syntax to produce targeted `name`/`social-profile`/document hits
- **Empty/negative result looks like:** an operator that returns nothing may be deprecated (Google has quietly killed several) — cross-check against the article's "still works" notes rather than assuming the subject is absent.

## Gotchas & OpSec
- Google deprecates operators over time; rely on this page's currency notes, not memory.
- Heavy dorking triggers CAPTCHAs and temporary blocks — pace queries and use a clean session.
- This is documentation, not a database; it holds no personal data itself.

## Overlaps ("do both")
- Pairs with `[[google-com-86]]` — that entry is a specific pre-built dork; this one teaches you to write your own for any target/platform.

## Trust & verifiability
`trust: community` — a reputable industry publication maintaining the list; verify each operator's current behavior by testing it, since search-engine syntax changes without notice.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | searchenginejournal-com |
| category | search-engines |
| selectorsIn → selectorsOut | name → name, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

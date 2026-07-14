---
id: google-com-81
name: Google Advanced Search Operators (reference)
description: Use when you have a `name` (or any selector) and want to construct precise Google dorks to surface a person's footprint — returns refined paths to `name` and `social-profile` hits.
url: https://support.google.com/websearch/answer/35890
category: search-engines
path:
- search-engines
bestFor: Learning and applying Google search operators (site:, intext:, filetype:, quotes, OR, minus) to sharpen OSINT queries.
selectorsIn:
- name
selectorsOut:
- name
- social-profile
status: live
pricing: free
costNote: Free — Google's own help documentation, and the operators it teaches cost nothing to use.
opsec: passive
opsecNote: Reading the docs is passive. The searches you build run against Google's index, not the subject, so the target is not alerted. For sensitive work, search logged-out from a sock-puppet browser so queries aren't tied to your Google account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Google documentation of its own search operators — authoritative for the syntax, though which operators still work changes over time.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Google search operators
- Google dorks reference
- Refine web searches
tags:
- searchengines
- Search Engines
- google-dork
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Google Advanced Search Operators (reference)

> Google's own guide to search operators — the syntax reference behind every effective "Google dork," turning a vague name search into a precise footprint hunt.

## When to use
You have a `name`, `username`, `email`, phone, or any string and Google's default results are too noisy. This reference teaches the operators that scope a query to exactly what you want — a specific site, file type, phrase, or exclusion — which is the backbone of nearly every web-search OSINT step. Reach for it to sharpen a search before assuming a subject isn't findable.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read the operator reference at the URL for current, supported syntax.
2. Build a targeted query from your selector, combining operators:
   - `"First Last"` — exact phrase, avoids scattered word matches.
   - `site:example.com "First Last"` — scope to one platform (repeat per site).
   - `intext:"555-123-4567"` / `intext:"email@domain"` — find pages mentioning a phone/email.
   - `filetype:pdf "First Last"` — surface documents (rosters, resumes, court PDFs).
   - `"First Last" (Denver OR Colorado) -linkedin` — disambiguate and exclude noise.
3. Run it logged-out; read hits for `name` confirmations and `social-profile` links.
4. Iterate: tighten with more operators, or broaden by dropping a qualifier.
5. Pivot: a discovered profile/site feeds platform-specific tools; a filetype hit may carry EXIF, addresses, or associates.

## Inputs → Outputs
- **In:** `name` (or any selector string) shaped into an operator query
- **Out:** targeted `name` mentions, `social-profile` links, documents and pages tied to the subject
- **Empty/negative result looks like:** zero results even after loosening operators — meaning the subject's footprint isn't in Google's index under those terms. Try alternate name forms, other engines (Bing/Yandex/DuckDuckGo), and archives before concluding nothing exists.

## Gotchas & OpSec
- Not all operators documented historically still work; Google deprecates some — test and adapt.
- Over-narrow queries return zero; loosen one qualifier at a time rather than assuming absence.
- OpSec: passive against the target. Search logged-out / sock-puppet so queries aren't tied to your Google identity, and vary engines to cover different indexes.

## Overlaps ("do both")
- Pairs with every site-specific dork card (e.g. `[[google-com-90]]`) and with other engines — operators are the method; the site cards are pre-built applications of them. Run the same query on Bing and Yandex, which index pages Google misses.

## Trust & verifiability
`trust: trusted` — it is Google's authoritative documentation of its own operators. The *syntax* is reliable; the *results* are only as complete as Google's index, so corroborate findings across engines and archives.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-com-81 |
| category | search-engines |
| selectorsIn → selectorsOut | name → name, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

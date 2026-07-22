---
id: najdsi-slovenia
name: Najdi.si (Slovenia)
description: Use when you have a `name`, `username`, or `domain` tied to Slovenia and want localized web/news results a global engine misses — returns `social-profile`, news, and `domain` leads.
url: https://www.najdi.si
category: search-engines
path:
- search-engines
bestFor: Slovenia-focused web, news, and business-directory search from a name or keyword.
selectorsIn:
- name
- username
- domain
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free Slovenian web portal; no account needed for search.
opsec: passive
opsecNote: Standard search-engine queries. Use a sock-puppet/clean browser if the subject is sensitive; the portal logs queries like any search engine, but nothing reaches the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing Slovenian web portal (Najdi.si); results are indexed content plus linked directories (Bizi, 1188, iTIS), not a verified dataset.
missingPersonsRelevance: medium
coverage:
- si
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- najdi-slovenia
aliases:
- najdi.si
- Najdsi
tags:
- search
- international
- slovenia
source: metaosint
lastVerified: '2026-07-22'
enrichment: full
---

# Najdi.si (Slovenia)

> Slovenia's home-grown search portal — the local index for names, news, and businesses that Google under-covers in the Slovenian web.

## When to use
Your subject has a Slovenian connection (nationality, residence, employer, or a `.si` `domain`) and you want localized results: Slovenian-language pages, local news, and the linked business directories (Bizi, 1188, iTIS). Reach for it as a country-specific complement when a global engine returns thin results for a Slovenian `name` or `username`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.najdi.si.
2. Enter the `name`, `username`, or keyword; use the News, Maps, and directory tabs for targeted results.
3. For a person, try name variants (Slovenian diacritics: č, š, ž) — spelling with/without accents changes results.
4. Follow into the linked directories (Bizi/1188) for business and phone-book style listings.
5. Pivot: profiles/domains found here feed username-search, social, and WHOIS tools; news hits build a timeline.

## Inputs → Outputs
- **In:** `name` / `username` / `domain` / keyword
- **Out:** `social-profile` and web pages, Slovenian news items, business-directory listings, `domain` leads
- **Empty/negative result looks like:** no Slovenian-web matches for the query — common for people with no local footprint. Absence here doesn't rule out presence on global platforms.

## Gotchas & OpSec
- Diacritics matter; run accented and unaccented variants of Slovenian names.
- Results are Slovenia-weighted — not a substitute for global search, but a complement.
- OpSec: passive; ordinary search queries, none of which reach the subject.

## Overlaps ("do both")
- Pairs with `[[najdi-slovenia]]` and global search engines: run both, since Najdi.si surfaces local-language pages that Google ranks poorly.

## Trust & verifiability
`trust: community` — a legitimate regional portal indexing third-party content; treat results as leads to verify, not authoritative records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | najdsi-slovenia |
| category | search-engines |

---
id: vinden-meta-search-netherlands
name: Vinden Meta Search (Netherlands)
description: Use when you have a `name` or keyword tied to the Netherlands and want a Dutch-oriented search/portal view — returns web results and links to Dutch services that can surface a `social-profile` or address lead.
url: https://www.vinden.nl
category: search-engines
path:
- search-engines
bestFor: A Netherlands-focused search portal for surfacing Dutch web results and directory links.
selectorsIn:
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to use; ad-supported Dutch portal, no account required.
opsec: passive
opsecNote: A standard web search/portal — passive, but it is a Dutch commercial site that sets cookies and may pass queries to underlying search partners. Use a clean browser session for sensitive lookups.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Dutch commercial search portal/directory; useful mainly for its Dutch-language bias and curated NL service links, not for unique data of its own.
missingPersonsRelevance: medium
coverage:
- nl
auth: none
api: false
localInstall: false
registration: false
aliases:
- vinden.nl
tags:
- toddington
- curated-directory
- meta-mega-search-tools
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Vinden Meta Search (Netherlands)

> A Dutch-language search portal and web directory — worth a pass when a subject is Dutch and you want NL-biased results plus quick links to Dutch services.

## When to use
Your subject has a Netherlands connection (Dutch `name`, NL address, `.nl` domain) and you want search results and directory links skewed toward Dutch sources instead of the US-centric default of Google. Vinden combines a search box with a curated portal of major Dutch websites (news, business, phone/address directories), which can point you toward the right NL-specific lookup for a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.vinden.nl.
2. Enter the subject's `name` or keyword in the search box for Dutch-oriented web results.
3. Alternatively, browse the portal's category links to jump into Dutch directories and services (news, telephone/address guides, business registers).
4. Read results with a Dutch-language eye — a Dutch subject's footprint (news mentions, forum posts, business listings) often surfaces here better than in English-first engines.
5. Pivot: a promising hit (a Dutch profile, a business listing, a phone/address directory) feeds NL-specific people-search and public-records tools.

## Inputs → Outputs
- **In:** `name` or keyword (Netherlands context)
- **Out:** Dutch web results and directory links that can lead to a `social-profile`, business listing, or address/phone directory entry
- **Empty/negative result looks like:** generic or empty results — Vinden is a portal over general web search, so a name with no Dutch footprint returns little of unique value.

## Gotchas & OpSec
- Vinden holds **no proprietary data** — it's a portal/meta layer, so its value is the Dutch-language bias and curated links, not exclusive records.
- The interface and much of the content are in Dutch; use translation if needed.
- OpSec: **passive** — ordinary web search; use a clean session and accept minimal cookies for sensitive work.

## Overlaps ("do both")
- Pairs with dedicated Netherlands public-records and people-search tools — Vinden helps you *find the right Dutch source*, those sources hold the actual person data.

## Trust & verifiability
`trust: unverified` — a Dutch commercial portal with no independent verification of data quality. Treat it as a routing/discovery layer and confirm any lead in the authoritative Dutch source it points you to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vinden-meta-search-netherlands |
| category | search-engines |
| selectorsIn → selectorsOut | name → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: seznam-czech-republic
name: Seznam (Czech Republic)
description: Use when you have a `name`, `username` or Czech `address`/business term and want results a global engine misses — returns Czech-language web, maps, business and news hits.
url: https://seznam.cz
category: search-engines
path:
- search-engines
bestFor: Searching the Czech-language web (people, businesses, local content) via the dominant domestic engine that indexes .cz sources Google under-covers.
selectorsIn:
- name
- username
- address
selectorsOut:
- social-profile
- address
- employer-org
status: live
pricing: free
costNote: Free to search; no account needed. An account is only required for Seznam's email/other services, not for search.
opsec: passive
opsecNote: A normal search query against a third-party engine — the subject is not notified. Seznam is a Czech company subject to Czech/EU law and logs queries against your IP; use a research browser and a neutral session for sensitive queries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Seznam.cz is the long-established, dominant Czech search portal and a real company; results are genuine index hits, not a scraper or aggregator.
missingPersonsRelevance: low
coverage:
- cz
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- seznam-cz
- google-search
aliases:
- Seznam.cz
- Seznam search
tags:
- main-national-search-engines
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Seznam (Czech Republic)

> The Czech Republic's dominant home-grown search portal — the go-to engine when your subject, business or event is Czech and Google's .cz coverage is thin.

## When to use
Your investigation touches the Czech Republic — a Czech `name`, a `.cz` business, a local `address`, a Czech-language forum handle — and Google is returning weak or Anglocentric results. Seznam indexes the Czech web, maps (Mapy.cz), business listings (Firmy.cz), goods and news more deeply than global engines, so it surfaces domestic pages, company records and local content the others miss.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://seznam.cz.
2. Enter the query in the search box. Put multi-word names/phrases in quotes; combine with a city or `.cz` to localise.
3. Read the tabbed results — web, Obrázky (images), Videa, Zboží (shopping), plus inline Mapy (maps) and Firmy (business directory) panels.
4. For a business or address, open the **Firmy.cz** / **Mapy.cz** panels directly — they carry registered company names, contacts and locations.
5. Pivot: Czech-language hits feed translation tools; a business hit feeds Czech corporate-registry lookups; a profile/handle feeds username OSINT.

## Inputs → Outputs
- **In:** `name`, `username`, or a Czech `address`/business term
- **Out:** Czech-language web pages, `social-profile` links, business `employer-org` records, local `address` data
- **Empty/negative result looks like:** few or only global-brand hits usually means the subject has little Czech-web footprint — retry with Czech spelling/diacritics or the Firmy.cz directory before concluding nothing exists.

## Gotchas & OpSec
- Best results come from Czech spelling **with diacritics** (Nováková, not Novakova); try both.
- The interface is Czech — pair with a translator, and note that Zboží/Firmy/Mapy are distinct verticals worth querying separately.
- Passive; the subject is not alerted, but Seznam logs your queries — use a neutral research session.

## Overlaps ("do both")
- Pairs with `[[google-search]]` — Seznam wins on domestic .cz depth, Google on international and recency; run both for any Czech subject.
- The Firmy.cz business hits feed Czech company-registry tools for registration details.

## Trust & verifiability
`trust: trusted` — Seznam is the established, first-party Czech search engine and a real operating company; results are authentic index hits. As with any search engine, corroborate the underlying pages themselves.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | seznam-czech-republic |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, address → social-profile, address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

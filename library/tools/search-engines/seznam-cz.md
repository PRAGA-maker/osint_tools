---
id: seznam-cz
name: seznam.cz
description: Use when you have a `name`/handle for a Czech subject and want Czech-web results Google under-indexes — returns `name`, `social-profile`, and Czech-language page leads.
url: https://www.seznam.cz/
category: search-engines
path:
- search-engines
bestFor: Searching the Czech-language web via the leading domestic search engine and portal.
selectorsIn:
- name
selectorsOut:
- name
- social-profile
status: live
pricing: free
costNote: Free to search; no account needed for search (a Seznam account is only needed for its email/other services).
opsec: passive
opsecNote: Running searches is passive and does not touch the subject. As with any search engine, your queries are logged by the provider; use a clean/sock-puppet browser session if your query pattern is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Seznam is the major established Czech search engine and web portal; results are its own index, strongest on Czech-language and .cz content.
missingPersonsRelevance: high
coverage:
- cz
auth: none
api: false
localInstall: false
registration: false
aliases:
- Seznam
- seznam.cz
tags:
- searchengines
- Search Engines
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- seznam-czech-republic
---

# seznam.cz

> Czechia's homegrown search engine and portal — the regional alternative to Google for surfacing Czech-language pages, directories, and profiles.

## When to use
Your subject is Czech or active on the Czech-language web and Google results feel thin. Seznam's own index and its portal services (Mapy.cz maps, Firmy.cz business directory, news) often surface `.cz` pages, local businesses, and profiles that international engines rank poorly or miss. Use it as a parallel search engine whenever the trail runs through Czechia.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.seznam.cz/ and use the search box (Czech interface; use browser translation).
2. Query the subject's `name`, handle, phone, or employer in Czech word order; try diacritics and non-diacritic variants.
3. Compare results against Google — note Czech pages, Firmy.cz business listings, and forum/social hits that Google didn't rank.
4. Use the portal's Mapy.cz for Czech addresses/street view and Firmy.cz for business/person-at-company leads.
5. Pivot: profile hits feed username/social OSINT; business listings feed the Czech company registry (justice.cz / ARES).

## Inputs → Outputs
- **In:** `name` / handle / keyword (Czech-language)
- **Out:** `name` and `social-profile` leads, Czech-language pages, directory/business listings
- **Empty/negative result looks like:** no distinctive Czech hits — for a non-Czech subject Seznam adds little over Google. As a general engine it returns pages, not verified identity; corroborate any profile hit.

## Gotchas & OpSec
- Czech-language interface and results; use translation and try diacritic variants (e.g. Novák vs Novak).
- Strength is regional — outside Czech content it rarely beats Google/Bing, so use it as a supplement, not a replacement.
- The Seznam account/login is only for email and portal services, not for search.

## Overlaps ("do both")
- Pairs with `[[google-com]]` and `[[yandex]]` — different indexes rank Czech content differently, so run the same query on all three; Seznam and Mapy.cz/Firmy.cz catch local results the global engines miss.

## Trust & verifiability
`trust: trusted` — an established, reputable national search engine; it indexes the open web, so weigh each result on its own source, not the engine.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | seznam-cz |
| category | search-engines |
| selectorsIn → selectorsOut | name → name, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: itar-tass
name: TASS (ITAR-TASS)
description: Use when you have a `name`, `employer-org`, or event and want how Russia's state news agency reported it — returns Russian-state-media coverage, named officials, and dates.
url: http://www.itar-tass.com
category: search-engines
path:
- search-engines
bestFor: Searching Russian state news agency coverage (English and Russian) for people, organisations, and events.
selectorsIn:
- name
- employer-org
selectorsOut:
- associate
- address
status: live
pricing: free
costNote: Free to read and search; no account required for the public news site.
opsec: passive
opsecNote: Passive reading of a public news site. Note it is Russian state infrastructure — assume requests are logged; use a clean browser/VPN for sensitive research. No contact with any subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: TASS is the official Russian state news agency; authoritative for what the Russian government says, but state-controlled — treat its framing as an official narrative, not neutral fact.
missingPersonsRelevance: low
coverage:
- ru
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-news
aliases:
- ITAR-TASS
- Itar-Tass
- TASS
- itar-tass.com
tags:
- news
- russia
- state-media
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# TASS (ITAR-TASS)

> Russia's official state news agency — the authoritative source for the Russian government's public narrative on a person, body, or event (the legacy itar-tass.com now resolves to tass.com/tass.ru).

## When to use
You are researching a subject with a Russian/CIS connection — an official, a company, a diplomat, a sanctioned entity, or an event inside Russia — and want to know how the Russian state reported it, who it named, and when. TASS coverage often supplies official titles, affiliations, quoted associates, and dated statements you won't find in Western outlets.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tass.com (English) or https://tass.ru (Russian, fuller coverage) — itar-tass.com redirects here.
2. Use the site search for the subject `name`, `employer-org`, or event keyword (search Russian-language terms/transliterations on tass.ru for more hits).
3. Read the articles for named officials, titles/affiliations (`employer-org`), quoted associates, locations, and dates.
4. Cross-reference the same event in independent outlets to separate fact from state framing.
5. Pivot: named officials/associates feed people-search; stated affiliations feed corporate-registry lookups.

## Inputs → Outputs
- **In:** `name`, `employer-org`, or event keyword
- **Out:** state-media coverage, named officials/`associate`s, titles/affiliations, locations (`address`), dates
- **Empty/negative result looks like:** no articles for the query — the subject may be below TASS's coverage threshold or reported only under a Russian-language spelling; retry on tass.ru.

## Gotchas & OpSec
- State-controlled: TASS reflects an official narrative. Use it for *what the Russian state asserts*, always corroborated independently.
- The Russian-language tass.ru carries far more than the English tass.com — transliterate names and search both.
- OpSec: passive, but it is Russian state infrastructure; use a clean browser/VPN for sensitive queries.

## Overlaps ("do both")
- Pairs with `[[google-news]]` — Google News aggregates independent and Western coverage of the same event, letting you triangulate TASS's framing against other sources.

## Trust & verifiability
`trust: community` — authoritative as the Russian government's own outlet, but state-controlled; treat its claims as an official position to be verified, not as neutral reporting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | itar-tass |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → associate, address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

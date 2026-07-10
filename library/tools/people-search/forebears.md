---
id: forebears
name: Forebears
description: Use when you have a surname/given `name` and want its geographic distribution and origin — returns where the name is common (`geolocation`) and ethnic/family origin clues (`associate`), NOT personal contact data.
url: http://forebears.io
category: people-search
path:
- people-search
bestFor: Surname and given-name analytics — incidence maps, country/region distribution, and origin/meaning of a name, to infer likely nationality/ethnicity of a subject.
selectorsIn:
- name
selectorsOut:
- geolocation
- associate
status: live
pricing: free
costNote: Free to search name statistics and distribution maps. It is a names/demographics resource, not a paid people-search — no personal records behind a paywall here.
opsec: passive
opsecNote: You query aggregate name statistics, not an individual — nothing identifies or notifies any specific person. Fully passive; no OpSec risk beyond normal web browsing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large, well-known names database (30M+ given names, 31M+ surnames) built from public census/registry statistics. Distribution figures are estimates aggregated from national data, so treat them as indicative, not exact.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- forebears.io
- surname distribution
tags:
- people-search
- genealogy
- surname
- demographics
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Forebears

> A names atlas: type a surname and see where in the world it's concentrated and where it likely originates — a way to narrow a subject's nationality/ethnicity from their name alone.

## When to use
You have a `name` — especially a surname — and little geographic anchor, and you want to infer likely origin. Forebears maps how common a name is per country/region and describes its origin and meaning. In a missing-person or identity case where you only have a name, this narrows *which country's* records and platforms to search (e.g. a surname 90% concentrated in the Philippines redirects your whole search). It does **not** return an individual's address, phone, or profiles — it's population statistics, not a people-lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open forebears.io and search the surname (or given name).
2. Read the distribution: incidence and rank by country, plus a heat map of where the name is most common.
3. Read the origin/meaning notes and any linked demographics (region, sometimes religion) for cultural context.
4. Use the top countries/regions to **direct** the rest of your investigation — pick the right national registries, languages, and platforms.
5. Pivot: dominant country → that country's public records/social platforms; name origin → transliteration variants to search; rare-surname clusters → tighter geographic focus.

## Inputs → Outputs
- **In:** `name` (surname or given name)
- **Out:** `geolocation` (country/region distribution, incidence), `associate` (ethnic/linguistic origin clues) — no personal contact data
- **Empty/negative result looks like:** very low incidence everywhere or "not enough data" — a rare/novel name, a misspelling, or a name below the statistical threshold. That still tells you the name is uncommon, which is itself useful.

## Gotchas & OpSec
- **Not a people-search:** despite the category, it won't find a specific person's address/phone/profiles — it profiles the *name*. The seed's contact-data selectors were wrong.
- Figures are statistical estimates from census/registry data of varying age and quality — indicative, not precise.
- OpSec: fully **passive** — aggregate data only.

## Overlaps ("do both")
- Use it as a *targeting* step feeding actual people-search and national registries (e.g. `[[swedish-name-register]]`-type national tools) once it points you to a country.
- Pairs with genealogy platforms (FamilySearch) for surname history.

## Trust & verifiability
`trust: community` — a reputable, widely cited names database drawn from public statistics. Its distributions are aggregate estimates; use them to steer, and confirm any individual conclusion with primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | forebears |
| category | people-search |
| selectorsIn → selectorsOut | name → geolocation, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

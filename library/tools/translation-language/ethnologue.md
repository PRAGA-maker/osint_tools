---
id: ethnologue
name: Ethnologue
description: Use when you have a language name, code, or region and want to know where a language is spoken and by whom — returns speaker geography, population, and dialects to geolocate/attribute a subject by language.
url: https://www.ethnologue.com
category: translation-language
path:
- translation-language
bestFor: The authoritative reference on the world's living languages — mapping a language or dialect to the countries/regions and communities where it's spoken.
selectorsIn: []
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: A limited number of page views are free; full/unrestricted access to language pages, maps and data requires a paid subscription. Basic language-location facts are reachable on the free tier.
opsec: passive
opsecNote: A reference database — you look up languages, not people. Nothing about any subject is disclosed; only your own browsing is seen by the site.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by SIL International since 1951; the standard scholarly catalogue of world languages and the source of ISO 639-3 codes. Authoritative for language facts, though speaker counts are estimates.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: true
relatedTools:
- glottolog
- language-identification-tools
aliases:
- Ethnologue Languages of the World
- SIL Ethnologue
tags:
- translation
- language-reference
- geolocation-aid
source: metaosint
lastVerified: '2026-07-29'
enrichment: full
---

# Ethnologue

> SIL International's catalogue of the world's living languages — the reference for turning "what language is this?" into "where and by whom is it spoken?"

## When to use
You have a language or dialect (identified from a subject's speech, writing, a document, or a caption) and you want to narrow down geography and community: which countries and regions speak it, roughly how many people, what the related dialects are, and its ISO 639-3 code. In a missing-persons or attribution context, a distinctive language or minority dialect can meaningfully shrink the map of where someone is from or currently located.

## How to use it (`bestInteractionPattern`: web-manual)
1. First identify the language (e.g. via a language-detection tool); then open https://www.ethnologue.com.
2. Search by language name or ISO 639-3 code, or browse by country.
3. Read the language page: primary countries, regions, speaker population estimates, dialect clusters, language status, and (on paid tiers) distribution maps.
4. Use minority/regional languages as a strong geolocation narrower — a small-population language points to a specific area far better than a world language.
5. Pivot: combine with `[[glottolog]]` for genealogical/linguistic detail and with your geolocation workflow to overlay language regions on candidate locations.

## Inputs → Outputs
- **In:** a language name / ISO code / country (a reference lookup, not a personal selector).
- **Out:** `geolocation` context — countries/regions of use, speaker populations, dialects.
- **Empty/negative result looks like:** a language not catalogued or a page gated behind the paywall — for the latter, note the partial paywall; for genuinely missing entries, check `[[glottolog]]`.

## Gotchas & OpSec
- Human-in-the-loop: a **partial paywall** — free views are capped; deeper data needs a subscription.
- OpSec: **passive** — a reference site; you disclose nothing about a subject.
- Speaker counts are estimates and can lag reality; treat population figures as orders of magnitude, not precise numbers.
- It classifies *languages*, not individuals — knowing a language's region narrows, but never proves, a person's location.

## Overlaps ("do both")
- Pairs with `[[glottolog]]` — Glottolog gives rigorous language genealogy and bibliographic detail (and is fully free); Ethnologue leads on speaker geography and population. Use both to triangulate a language's footprint.

## Trust & verifiability
`trust: trusted` — the standard scholarly reference (SIL International, source of ISO 639-3). Language facts are authoritative; speaker-population numbers are documented estimates, so cite them as such.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ethnologue |
| category | translation-language |
| selectorsIn → selectorsOut | — → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |

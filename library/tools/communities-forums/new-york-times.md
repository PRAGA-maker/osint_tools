---
id: new-york-times
name: New York Times
description: Use when you have a `name` and want news coverage, obituaries, or event reporting mentioning a subject — returns articles yielding `associate`, `geolocation`, and `employer-org` context.
url: http://www.nytimes.com
category: communities-forums
path:
- communities-forums
bestFor: Searching a major newspaper's archive for coverage, obituaries, and event reporting that names a person and their connections.
selectorsIn:
- name
selectorsOut:
- associate
- geolocation
- employer-org
status: live
pricing: freemium
costNote: Article search and headlines/snippets are free; reading full articles beyond a monthly limit requires a subscription. Obituary and archive access may need a subscription, but snippets and search are free and often enough to confirm a lead.
opsec: passive
opsecNote: Reading a public news site is passive. A search-engine site: query keeps you off the outlet's logs entirely and sidesteps the metered paywall for snippets.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: The New York Times is a major, professionally edited newspaper of record; its reporting and obituaries are high-reliability sources, though coverage of any given individual is not guaranteed.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- the-guantanamo-docket
aliases:
- NYT
- nytimes.com
tags:
- toddington
- curated-directory
- news-journalism
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# New York Times

> A newspaper of record with a deep, searchable archive — a strong source for coverage, obituaries, and event reporting that names a subject and reveals their associates, locations, and affiliations.

## When to use
You have a `name` and want to find whether the subject (or their family/associates) has appeared in the news — a story, an obituary, a wedding/court/business item, or event coverage. NYT reporting can supply corroborated `associate`s, `geolocation` (where the person lived/worked/was reported), `employer-org`, and dates, which are especially valuable in missing-persons and background work when a person has any public footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.nytimes.com and use its search, or run `site:nytimes.com "<name>"` in a search engine (usually more thorough and shows snippets past the paywall).
2. Try name variants and add a city, employer, or year to disambiguate.
3. Open articles/obituaries and extract named `associate`s, `geolocation`, `employer-org`, and event dates.
4. Check the obituaries and archive sections specifically for family/relationship detail.
5. Pivot: obituaries are rich for family/`associate` mapping; named organisations and places feed further record searches.

## Inputs → Outputs
- **In:** `name` (with disambiguating city/employer/year)
- **Out:** articles yielding `associate`, `geolocation`, `employer-org`, and dated events
- **Empty/negative result looks like:** no coverage mentions the name — the norm for most private individuals; absence is expected and not meaningful. Check local newspapers, which cover ordinary people far more.

## Gotchas & OpSec
- Metered paywall: search and snippets are free, full text may need a subscription — a `site:` query surfaces enough to triage.
- National coverage skews to newsworthy people; use local outlets for ordinary individuals.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with local-newspaper archives and obituary aggregators — the NYT gives authoritative national coverage, while local papers and obituary sites catch the everyday individuals it won't.

## Trust & verifiability
`trust: trusted` — professionally edited journalism of record; individual articles are citable, reliable sources, while remembering that whether a specific person is covered at all is hit-or-miss.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | new-york-times |
| category | communities-forums |
| selectorsIn → selectorsOut | name → associate, geolocation, employer-org |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |

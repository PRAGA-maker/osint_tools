---
id: leit-search-engine-iceland
name: Leit Search Engine (Iceland)
description: Use when you have a `name` and want Icelandic web, phone-directory, and business results — returns phone, address, and social-profile leads for people and businesses in Iceland.
url: http://leit.is
category: search-engines
path:
- search-engines
bestFor: Regional Iceland lookups — surfacing local web pages, phone/business directory entries, and news for an Icelandic name or company.
selectorsIn:
- name
- employer-org
selectorsOut:
- phone
- address
- social-profile
status: live
pricing: free
costNote: Free keyword search and directory; no account required.
opsec: passive
opsecNote: Ordinary search-engine queries against an Icelandic index; the subject is not contacted. Queries are logged by leit.is like any search engine — use a VPN if you want to keep your research IP out of their logs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running Icelandic search engine (DCG ehf, launched 1999); a legitimate regional index, but a third-party aggregator rather than an authoritative registry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- leit.is
tags:
- toddington
- curated-directory
- search-engines
- regional-search
- iceland
source: toddington-resources
lastVerified: '2026-07-20'
enrichment: full
---

# Leit Search Engine (Iceland)

> Iceland's home-grown search engine (since 1999), bundling web results with a phone directory, business listings, events, and news.

## When to use
Your subject has an Icelandic connection — a name, business, or address in Iceland — and mainstream global search engines under-index local content. Leit.is skews toward Icelandic-language pages and includes directory features (telephone, business listings) that turn a name into a phone number or address inside Iceland.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://leit.is.
2. Enter the target `name` or `employer-org`. Icelandic naming (patronymics, þ/ð/æ characters) matters — try the correct spelling and diacritics.
3. Scan web results plus the directory/business tabs for a matching person or company.
4. Read out `phone`, `address`, and links to social/professional `social-profile` pages.
5. Pivot: an Icelandic phone/address feeds local registry and people-search tools; a business name feeds company-registry lookups.

## Inputs → Outputs
- **In:** `name` or `employer-org` (Icelandic context)
- **Out:** `phone`, `address`, `social-profile` leads
- **Empty/negative result looks like:** few or no Icelandic-language hits — likely the subject has no Icelandic footprint, or the name is spelled/transliterated differently. Retry with native diacritics.

## Gotchas & OpSec
- Best value is strictly regional; for non-Iceland subjects a global engine will outperform it.
- Icelandic character encoding and patronymic naming cause misses — get the spelling right.
- OpSec: passive; standard search-engine logging applies to you, not the target.

## Overlaps ("do both")
- Complements global engines and national people-search: use Leit for the local Icelandic layer those miss, then pivot the phone/address into broader tools.

## Trust & verifiability
`trust: community` — an established regional search engine, useful as a discovery layer, but treat directory hits as leads to confirm against Iceland's official registries.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | leit-search-engine-iceland |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → phone, address, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

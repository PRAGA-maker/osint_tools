---
id: dpa-international
name: DPA International
description: Use when you have a `name` or `employer-org` and want English-language wire coverage of them — returns news mentions surfacing `associate` and `employer-org` context.
url: https://www.dpa-international.com
category: search-engines
path:
- search-engines
bestFor: English-language newswire coverage from Germany's national press agency for context on a person, org, or event.
selectorsIn:
- name
- employer-org
selectorsOut:
- associate
- employer-org
status: live
pricing: free
costNote: Free to read the public newswire; no account or subscription needed for the articles shown.
opsec: passive
opsecNote: Reading a public news site leaks nothing about the target; your request goes only to dpa's servers. No sock puppet required, though normal browser hygiene is sensible.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Deutsche Presse-Agentur (dpa), Germany's national news agency and an established primary wire service.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-news
- bing-news
- euronews
- abyznewslinks
aliases:
- Deutsche Presse-Agentur International
- dpa International
tags:
- news
- newswire
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# DPA International

> The English-language international feed of Deutsche Presse-Agentur — a national wire service, useful when you need agency-grade coverage of a person or event beyond the Anglophone press.

## When to use
You have a `name`, `employer-org`, or event and want reporting from a major European wire agency — especially for Germany, the EU, and stories the US/UK press under-covers. Wire coverage often names the people, companies, and places around a subject, which helps corroborate an `employer-org`, surface an `associate`, or fix a date/place to a story.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.dpa-international.com and browse the sections (Politics, Economics, Sports, General News, Culture & Science, Trends).
2. For a targeted lookup, use a site-scoped search engine query instead of the on-site nav, e.g. `site:dpa-international.com "Full Name"` in `[[google-news]]` or a general engine — dpa's own search is limited.
3. Read matching articles for named associates, employers, locations, and dates tied to your subject.
4. Pivot: corroborate any new `associate`/`employer-org`/`geolocation` against a second source, and widen with `[[google-news]]` / `[[bing-news]]` for other outlets.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** `associate`, `employer-org` (plus dates/places named in the coverage)
- **Empty/negative result looks like:** no articles mention your subject. For an ordinary private individual that is the normal result — a wire agency covers newsworthy people and events, not the general public.

## Gotchas & OpSec
- This is a live news homepage, not a searchable person-archive; rely on site-scoped search-engine queries for a specific name.
- Coverage is agency/wire-level — good for public figures, officials, companies, and events; near-useless for a private missing person unless their case was reported.
- OpSec: passive. Reading the site tells the target nothing.

## Overlaps ("do both")
- Pairs with `[[google-news]]` and `[[bing-news]]` to see who else ran the story, and with `[[abyznewslinks]]` to find additional local outlets for the same region.

## Trust & verifiability
`trust: trusted` — dpa is Germany's principal national news agency; treat its wire copy as reliable primary reporting, while still corroborating specific claims across outlets.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dpa-international |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → associate, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

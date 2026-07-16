---
id: ecured-cuba
name: EcuRed (Cuba)
description: Use when you have a Cuban `name`/place/`employer-org` and want a Spanish-language encyclopedic profile — returns biographical, organizational, and place details from Cuba's wiki.
url: http://www.ecured.cu/index.php/P%C3%A1gina_Principal
category: search-engines
path:
- search-engines
bestFor: Looking up Cuban people, places, institutions, and events in EcuRed, Cuba's state-run crowdsourced encyclopedia.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free public wiki; no account needed to read.
opsec: passive
opsecNote: Reading a public encyclopedia is passive. Note EcuRed is a Cuban state-run site — your IP hits a Cuban government server; use a VPN if that matters to you, but nothing about the subject is disclosed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A crowdsourced, state-affiliated Cuban encyclopedia; broad local coverage but with a Cuban-government editorial perspective — treat politically sensitive entries as slanted.
missingPersonsRelevance: low
coverage:
- cu
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- EcuRed
tags:
- toddington
- curated-directory
- specialty-search
- encyclopedia
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
---

# EcuRed (Cuba)

> Cuba's own crowdsourced encyclopedia — a Spanish-language reference that often covers Cuban people, institutions, and places that Wikipedia barely touches.

## When to use
Your subject or their context is Cuban — a person, a town, an institution, a company, or an event with a Cuban connection — and you want an encyclopedic profile. EcuRed frequently has entries on local Cuban figures, organizations, and geography absent from English sources, making it a useful specialty reference for Cuba-linked investigations. Low general relevance; high value only when Cuba is in scope.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open EcuRed (Spanish interface) and search the subject `name`, place, or `employer-org`.
2. Read the entry: biography, affiliations, roles, dates, and links to related people/organizations (`associate`s).
3. Translate as needed; note the entry's framing on political topics.
4. Corroborate any politically-charged claim against independent sources.
5. Pivot: named affiliations and related figures feed link analysis; place/institution details feed geolocation and org research.

## Inputs → Outputs
- **In:** a Cuban-linked `name`, place, or `employer-org`
- **Out:** encyclopedic profile with `employer-org` affiliations and related people (`associate`s)
- **Empty/negative result looks like:** no article — the subject isn't notable enough for EcuRed, or isn't Cuba-linked; a null result here says nothing about non-Cuban subjects.

## Gotchas & OpSec
- Cuba-focused and Spanish-language — irrelevant outside that context.
- State-affiliated editorial line — politically sensitive entries are slanted; corroborate.
- Coverage skews to notable figures/places, not private individuals.
- OpSec: passive read of a Cuban-government-hosted site; VPN optional.

## Overlaps ("do both")
- Pairs with Wikipedia and Spanish-language news archives — EcuRed fills Cuban gaps Wikipedia lacks; cross-check for balance on contested claims.

## Trust & verifiability
`trust: community` — a crowdsourced, state-affiliated wiki; useful for local coverage, but verify sensitive facts against independent sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ecured-cuba |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

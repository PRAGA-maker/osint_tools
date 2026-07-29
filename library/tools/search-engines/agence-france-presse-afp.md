---
id: agence-france-presse-afp
name: Agence France-Presse (AFP)
description: Use when you have a `name`, event, or place and want reporting/imagery from a major global news wire — AFP's site and fact-check arm return articles, photos, and debunks.
url: http://www.afp.com
category: search-engines
path:
- search-engines
bestFor: Sourcing news reporting, wire photography, and fact-checks from a major international news agency.
selectorsIn:
- name
- geolocation
selectorsOut:
- name
- image
status: live
pricing: freemium
costNote: Reading AFP's public news site and its AFP Fact Check content is free; licensing the wire feed, archive, and photo library for reuse is a paid B2B service.
opsec: passive
opsecNote: You browse a public news site; nothing about a target is transmitted. Standard sock-puppet browser hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: One of the world's three major news wire agencies with rigorous editorial standards and a dedicated fact-checking operation; a high-credibility reporting source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- AFP
- AFP Fact Check
tags:
- news
- media-source
- fact-check
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Agence France-Presse (AFP)

> A major global news wire and fact-checking operation — search AFP for reporting, wire photography, and debunks tied to a person, event, or place.

## When to use
You have a `name`, an event, or a `geolocation` and want credible journalism about it: contemporaneous reporting that dates and contextualizes events, wire photos that may show a subject, or an AFP Fact Check debunking a viral claim/image you are assessing. AFP is a primary-tier source, useful both for leads (who/where/when) and for verifying or debunking media in circulation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to afp.com (choose your language edition) or directly to AFP Fact Check (factcheck.afp.com).
2. Search or browse for the `name`, event, or place.
3. Read the reporting for named people, dates, locations, and quoted sources; inspect wire photos for identifiable faces/scenes.
4. For a suspicious image/claim, check AFP Fact Check to see if it has already been verified or debunked.
5. Pivot: named people/orgs in an article feed further person/entity OSINT; a wire photo can be reverse-image-searched; a fact-check gives you a sourced verdict to cite.

## Inputs → Outputs
- **In:** a `name`, event, or `geolocation`
- **Out:** news articles (with `name`s, dates, places), wire `image`s, and fact-check verdicts
- **Empty/negative result looks like:** no AFP coverage — the subject/event was not internationally newsworthy or not covered by AFP; try local/regional outlets and news aggregators.

## Gotchas & OpSec
- Human-in-the-loop: none; open reading.
- OpSec: passive; a public news site.
- Reuse of AFP text/photos is licensed and paid — reading is free, but republishing wire content in a report requires rights. Cite and link rather than copy.
- Coverage skews to internationally significant news; for ordinary individuals, expect little to nothing.

## Overlaps ("do both")
- Complements other major wires (Reuters, AP) and general news search: run several agencies to corroborate an event, and use AFP Fact Check alongside reverse-image tools when verifying a specific photo or claim.

## Trust & verifiability
`trust: trusted` — a top-tier international news agency with formal editorial standards and a dedicated fact-checking unit; reporting is attributable and, for fact-checks, explicitly sourced.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | agence-france-presse-afp |
| category | search-engines |
| selectorsIn → selectorsOut | name, geolocation → name, image |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

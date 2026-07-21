---
id: familypedia
name: Familypedia
description: Use when you have a `name` (especially with an ancestor/surname angle) and want crowdsourced genealogy — family trees, relatives, dates — returns `associate` (kin), `dob`, and locality from a semantic genealogy wiki.
url: https://familypedia.fandom.com
category: search-engines
path:
- search-engines
bestFor: Crowdsourced genealogy lookups — connecting a person to relatives, ancestors, surnames, dates and places via a semantic family-history wiki.
selectorsIn:
- name
selectorsOut:
- associate
- dob
- name
status: live
pricing: free
costNote: Free, community-run wiki on Fandom. No account needed to read.
opsec: passive
opsecNote: Passive — reading public wiki articles. Editing (which needs a Fandom account) is unnecessary for research; if you do edit, use a sock-puppet account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-edited semantic wiki (100,000+ articles) hosted on Fandom; contributor-supplied genealogy is often unsourced, so treat entries as leads to verify against primary records.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- itlaw
- lotrowikia
- memory-alpha-star-trek-universe-wiki
- religion-wiki
- thefaceoff-ice-hockey-wiki
- wikiawikis
- wikirecipes
aliases:
- Familypedia
- Family History and Genealogy Wiki
tags:
- toddington
- curated-directory
- specialty-search
- genealogy
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Familypedia

> The largest semantic genealogy wiki (100k+ articles on Fandom) — a crowdsourced way to place a person within a family tree of relatives, surnames, dates and locations.

## When to use
You have a `name` and a genealogical angle — a surname to trace, an ancestor to connect, or relatives to enumerate. Familypedia can link an individual to parents, spouses, children and wider kin, with dates and places, which helps build the family network around a missing or unidentified person (and can surface living relatives worth contacting).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://familypedia.fandom.com and search the person's `name` (or surname).
2. Because it uses Semantic MediaWiki, open a person's article to see structured links to relatives, birth/death dates and locations.
3. Follow relative links outward to map the family tree; note surnames and place articles.
4. Cross-check any date/relationship against a primary source (vital records, obituaries) before relying on it.
5. Pivot: relatives' names feed people-search and social lookups; dates feed obituary/records searches.

## Inputs → Outputs
- **In:** `name` / surname
- **Out:** `associate` (relatives/kin), `dob` (and death dates), locality, related surnames
- **Empty/negative result looks like:** no article or a stub with no relations — meaning no contributor has documented this family here (common for ordinary/living people); fall back to dedicated genealogy databases.

## Gotchas & OpSec
- **Crowdsourced & often unsourced** — coverage is uneven and accuracy varies; verify before acting.
- Skews toward historical/deceased individuals; living people are sparsely covered (and sometimes deliberately omitted).
- OpSec: passive reading; no need to log in.

## Overlaps ("do both")
- Pairs with mainstream genealogy databases and obituary/newspaper searches — Familypedia sketches the family network; primary records confirm the dates and relationships.

## Trust & verifiability
`trust: community` — an open, community-edited wiki; entries are leads, not proof. Chase the citations (where present) to primary genealogical records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | familypedia |
| category | search-engines |
| selectorsIn → selectorsOut | name → associate, dob, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

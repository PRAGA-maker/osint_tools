---
id: booleanstringbank
name: BooleanStringBank
description: Use when you have a name, role, or employer and want a ready-made, crowdsourced Boolean search string to find profiles fast instead of writing one yourself — returns query strings that surface social-profile/name results.
url: https://www.scoperac.com/booleanstringbank/
category: search-engines
path:
- search-engines
bestFor: Finding ready-to-use crowdsourced Boolean search strings for people/profile sourcing.
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
- name
status: live
pricing: freemium
costNote: Free tier gives search/contribution access; a Workspace upgrade (~$2.99/month) adds workflow integration. You don't need to pay to copy strings.
opsec: passive
opsecNote: You're browsing a library of query strings — nothing about a target is disclosed here. Running a copied string in Google/LinkedIn is passive against those engines (the target isn't contacted); log in to LinkedIn only via a sock-puppet account to avoid viewer traces.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A crowdsourced platform contributed by many sourcers; string quality varies with the contributor, so treat each as a starting template to adapt.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- bool
aliases:
- Boolean String Bank
tags:
- Search engines
- boolean-search
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# BooleanStringBank

> A crowdsourced library of ready-made Boolean search strings — copy a proven query for your role/industry instead of building the operators from scratch.

## When to use
When you have a `name`, job title/role, or `employer-org` and want to find someone's profiles/mentions with a precise search but don't want to author the Boolean logic yourself. BooleanStringBank indexes hundreds of community-contributed strings by topic/industry that you can copy, tweak with your target's specifics, and run in Google/LinkedIn X-ray. It's a query library, not a data source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.scoperac.com/booleanstringbank/.
2. Search the bank by topic/industry/role for a relevant string.
3. Copy a string and substitute your target's specifics (name, company, location).
4. Run it in Google or as a LinkedIn X-ray (`site:linkedin.com/in ...`) from a sock-puppet browser.
5. Pivot: results surface `social-profile`s and corroborating `name`/employer details; refine the string and repeat.

## Inputs → Outputs
- **In:** `name`, role, or `employer-org` (to pick and fill a string)
- **Out:** a query that surfaces `social-profile` / `name` results in a search engine
- **Empty/negative result looks like:** the filled string returns nothing — usually over-constrained; loosen terms or add OR synonyms.

## Gotchas & OpSec
- It provides **strings, not results** — value depends on the engine you run them in.
- Contributor quality varies; treat each string as a template to adapt, not a finished query.
- Some features/workspace are paid, but copying strings is free.

## Overlaps ("do both")
- Complements `[[bool]]` (interactive query builder): the bank gives proven starting strings, Bool helps you assemble/adjust the operators.

## Trust & verifiability
`trust: community` — crowdsourced query templates with no data of their own, so no accuracy risk in the strings themselves; the results you get are ordinary search hits to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | booleanstringbank |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → social-profile, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

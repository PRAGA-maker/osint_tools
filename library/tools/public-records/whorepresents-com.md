---
id: whorepresents-com
name: whorepresents.com
description: Use when you have a celebrity/public-figure `name` and want to find who represents them — returns the agency/publicist (`employer-org`) and a professional contact route.
url: http://www.whorepresents.com/
category: public-records
path:
- public-records
bestFor: Finding the agent, manager, or PR firm that represents a celebrity or public figure.
selectorsIn:
- name
selectorsOut:
- employer-org
- associate
status: degraded
pricing: freemium
costNote: A long-standing entertainment-industry contact database; basic lookups may be free but full contact detail and bulk access are subscription-gated. Coverage/uptime have become inconsistent over the years.
opsec: passive
opsecNote: Looking up a public figure's representation is passive and does not contact the person. If you then approach the agency, that is an active outreach step — plan pretext and attribution accordingly.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: An established industry directory of talent representation; useful but can be dated, and its free tier and reliability vary — corroborate a listed agency against the person's official/agency site.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- apollo-io
- contactout
aliases:
- WhoRepresents
- whorepresents.com
tags:
- professionlicensing
- Profession & Licensing Sites
- entertainment
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# whorepresents.com

> An entertainment-industry directory that maps a celebrity or public figure to their agent, manager, or PR firm — the route to a professional contact rather than the person directly.

## When to use
Your subject is a celebrity, actor, athlete, author, or other public figure, and you need the professional gatekeeper: the agency, management, or publicist that represents them. That representation is both a legitimate contact channel (for an official approach) and a network node (`associate`/`employer-org`) linking the figure to industry entities. Low direct missing-persons value unless the subject is a public figure.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.whorepresents.com/ and search the public figure's `name`.
2. Read the listed representation: agency/management/PR firm and any contact route (some detail is subscription-gated).
3. Corroborate the listing against the person's official site or the agency's own roster — industry representation changes often.
4. For an official approach, contact the listed representative rather than the individual.
5. Pivot: the agency (`employer-org`) links to other clients and staff; cross-check with `[[imdbpro]]` for entertainment figures.

## Inputs → Outputs
- **In:** public-figure `name`
- **Out:** representing agency/publicist (`employer-org`), professional contact leads (`associate`)
- **Empty/negative result looks like:** no listing — the person may be unrepresented, newly signed elsewhere, or not a covered public figure; the database also ages, so absence isn't conclusive.

## Gotchas & OpSec
- Status **degraded**: coverage, the free tier, and uptime have been inconsistent — verify any result against a second source (official site, agency roster, IMDbPro).
- Representation changes frequently; a listing can be out of date.
- Only useful for public figures — irrelevant for private individuals.
- OpSec: passive to look up; any subsequent outreach to the agency is active.

## Overlaps ("do both")
- Pairs with `[[imdbpro]]` (entertainment representation/credits) and `[[apollo-io]]` (business contact enrichment) — cross-check the representing entity and find the right individual contact.

## Trust & verifiability
`trust: community` — an established but aging industry directory. Treat a listing as a lead and confirm current representation against the person's or agency's official channels.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whorepresents-com |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |

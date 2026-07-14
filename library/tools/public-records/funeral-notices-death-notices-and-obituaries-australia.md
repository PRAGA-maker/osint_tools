---
id: funeral-notices-death-notices-and-obituaries-australia
name: Funeral Notices Death Notices and Obituaries (Australia)
description: Use when you have a `name` and want Australian death/funeral notices — returns family-member associate names, funeral location/date and death-date leads.
url: http://www.obits.com.au
category: public-records
path:
- public-records
bestFor: Searching Australian death, funeral, and obituary notices by name.
selectorsIn:
- name
selectorsOut:
- associate
- dob
- address
status: live
pricing: free
costNote: Free to search funeral/death notices; publishing a notice is a paid service, but searching/reading is free.
opsec: passive
opsecNote: Reading published notices is passive and leaks nothing about the subject. Notices are public death announcements placed by families/funeral homes.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An Australian funeral-industry notices aggregator; content is publisher/family-submitted, so details are as reliable as the placed notice.
missingPersonsRelevance: high
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
aliases:
- obits.com.au
- Australian death notices
tags:
- toddington
- curated-directory
- specialty-search
- obituary
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# Funeral Notices Death Notices and Obituaries (Australia)

> A searchable index of Australian death and funeral notices — the fastest way to confirm a death and harvest the family names an obituary lists.

## When to use
You have a `name` and need to confirm whether an Australian subject has died, or you want the rich relational data a death/funeral notice carries: surviving and predeceased family members (`associate`), the death/funeral date (`dob`-adjacent timeline anchor), and the funeral home/location (`address`/geolocation). Obituaries are one of the highest-yield sources for family-graph and confirmation-of-death questions in missing-persons work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.obits.com.au.
2. Enter the subject's `name` in the search box; filter by Australian state/territory to narrow.
3. Read the notice: deceased's name, death/funeral dates, listed family members, and funeral service location.
4. Cross-check dates and locations against other records to confirm it's your subject (common names produce false matches).
5. Pivot: family names (`associate`) feed people-search and genealogy; the funeral location/date anchors geography and timeline; a confirmed death redirects the whole investigation.

## Inputs → Outputs
- **In:** `name` (+ AU state to disambiguate)
- **Out:** family-member `associate` names, death/funeral date (`dob`/timeline), funeral `address`/location
- **Empty/negative result looks like:** no matching notice — meaning no notice was placed here (many deaths aren't publicly announced, or appear in local papers not indexed), not proof the person is alive.

## Gotchas & OpSec
- Coverage is partial: not every Australian death gets a notice, and some run only in local outlets — absence is weak evidence.
- Family-submitted content: names/relationships are as accurate as the notice; verify before building a family tree on it.

## Overlaps ("do both")
- Pairs with people-search and genealogy tools: the obituary supplies the family-name graph, which those tools expand into living relatives and addresses.

## Trust & verifiability
`trust: community` — a funeral-industry notices aggregator of family-submitted content; confirm identity and relationships against independent records before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | funeral-notices-death-notices-and-obituaries-australia |
| category | public-records |
| selectorsIn → selectorsOut | name → associate, dob, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

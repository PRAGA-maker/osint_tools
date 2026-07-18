---
id: nitv-television-australia
name: NITV (National Indigenous Television, Australia)
description: Use when you have a `name` linked to Aboriginal/Torres Strait Islander communities or events and want news coverage — returns social-profile and associate.
url: http://www.sbs.com.au/nitv
category: communities-forums
path:
- communities-forums
bestFor: Searching Australia's Indigenous public-broadcaster news/coverage for a subject, community or event.
selectorsIn:
- name
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free public-broadcaster content (part of SBS Australia); no account required.
opsec: passive
opsecNote: Reading published broadcaster content is invisible to any subject. Standard browsing hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Australia's national Indigenous public broadcaster (SBS); edited, attributable journalism.
missingPersonsRelevance: medium
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- NITV
- National Indigenous Television
- sbs.com.au/nitv
tags:
- news-journalism
- curated-directory
- australia
- toddington
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# NITV (National Indigenous Television, Australia)

> Australia's Indigenous public broadcaster — a targeted news source when a subject, family, or missing-person case is connected to Aboriginal or Torres Strait Islander communities.

## When to use
The case has an Australian Indigenous dimension — the subject, their family, or a related event is tied to Aboriginal/Torres Strait Islander communities. NITV covers stories, appeals, and community events that mainstream outlets often miss, including missing-person appeals and community-organised searches. A hit ties a `name` to coverage (`social-profile`) and to community members or organisers named alongside them (`associate`).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to www.sbs.com.au/nitv and use SBS site search, or run `site:sbs.com.au/nitv "Jane Doe"`.
2. Read matching articles/segments for the subject, community, or event.
3. Note dates, locations, community organisations, and people named.
4. Pivot: named community members/organisers → `associate`; local organisations → `employer-org`/community-group leads; event locations → `geolocation`.

## Inputs → Outputs
- **In:** `name` (or community/place term)
- **Out:** `social-profile` (coverage/mentions), `associate` (people named in the story)
- **Empty/negative result looks like:** no coverage matches — expected unless there is an Indigenous-community connection; means no NITV footprint, not a dead end for the wider case.

## Gotchas & OpSec
- Regional/community scope — high value for the specific Australian Indigenous angle, low relevance otherwise.
- Search the broader SBS domain too, since NITV content sits within sbs.com.au.
- OpSec: passive read; safe.

## Overlaps ("do both")
- Pair with mainstream Australian outlets and community Facebook groups — NITV catches community-specific coverage those miss, while broader outlets and social groups add reach and real-time appeals.

## Trust & verifiability
`trust: trusted` — an edited national public broadcaster; coverage is attributable and citable, though specifics (dates, names) should be corroborated against primary sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nitv-television-australia |
| category | communities-forums |
| selectorsIn → selectorsOut | name → social-profile, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

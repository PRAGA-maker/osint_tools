---
id: cnn-news-united-states
name: CNN (United States)
description: Use when you have a `name` and want major US/global news coverage mentioning a subject — returns `social-profile`/byline, event dates and named `associate` context.
url: http://www.cnn.com
category: communities-forums
path:
- communities-forums
bestFor: Searching a major global news archive for a person named, quoted, or reported on.
selectorsIn:
- name
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free to read and search most articles; ad-supported with some metered/premium content.
opsec: passive
opsecNote: Reading and dorking a public news site is passive and invisible to any subject; only CNN/its ad partners log the visit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A major international news organisation with editorial standards; well-sourced, but still secondary journalism (interpretation), not primary record.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- CNN
- cnn.com
tags:
- news-media
- archive
- global
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
relatedTools:
- cnn
---

# CNN (United States)

> A major global news archive — searchable coverage that can place a subject in a reported event, quote, byline or obituary with a firm date and location.

## When to use
You have a `name` and want to know whether the person appears in major US/international news: as the subject of reporting (crime, disaster, missing-person case, court proceeding), a quoted source or interviewee, a bylined journalist, or a tribute/obituary. News hits give a date-stamped event, a location, named associates/relatives, and quotes that establish role, presence or last-known status — often an anchor point for a timeline.

## How to use it (`bestInteractionPattern`: web-manual)
1. Use CNN's on-site search, or Google-dork it: `site:cnn.com "<full name>"` (add a city/event term to cut noise).
2. Open matching articles and read for the exact connection — subject, source, or byline — plus date, location and named associates.
3. Note the reporter and any CNN-affiliate/local tie-in for follow-up on a specific incident.
4. Pivot: named `associate`/relatives feed relationship mapping; an event date/location anchors a timeline; a byline feeds journalist enumeration.

## Inputs → Outputs
- **In:** `name`
- **Out:** `social-profile`/byline, named `associate`/relatives, event date, location and quoted context
- **Empty/negative result looks like:** no articles for the name — the person hasn't featured in CNN's coverage (common; try local outlets and other nationals), or same-name collisions you must disambiguate by context.

## Gotchas & OpSec
- National/global outlet: most ordinary people never appear — pair with local news for everyday subjects.
- Same-name collisions are frequent; confirm identity from article detail before linking.
- Journalism is interpretation — treat reported facts as leads, corroborate with primary records.

## Overlaps ("do both")
- Pairs with `[[nbc-united-states]]`, local-news search, Google News and obituary/court-record tools — nationals catch high-profile events, locals catch everyday ones; together they build the fullest media picture.

## Trust & verifiability
`trust: trusted` — a major professional news organisation; reporting is editorially sourced but is still secondary journalism, so anchor to primary records where possible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cnn-news-united-states |
| category | communities-forums |
| selectorsIn → selectorsOut | name → social-profile, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

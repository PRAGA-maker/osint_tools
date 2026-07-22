---
id: nbc-united-states
name: NBC News (United States)
description: Use when you have a `name` and want US news coverage mentioning a subject — returns `social-profile`/byline attribution, event dates and corroborating context.
url: https://www.nbcnews.com
category: communities-forums
path:
- communities-forums
bestFor: Searching a major US national news archive for a person named, quoted, or reported on.
selectorsIn:
- name
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free to read and search; ad-supported, no paywall for most articles.
opsec: passive
opsecNote: Reading and dorking a public news site is passive and invisible to any subject. Only NBC/its ad partners log your visit; nothing ties the search to your investigation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A major US national news organisation with editorial standards; reporting is professionally sourced, though still journalism (interpretation), not primary record.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- NBC News
- nbcnews.com
tags:
- news-media
- archive
- united-states
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# NBC News (United States)

> A major US national news archive — searchable coverage that can place a subject in a reported event, quote, byline or obituary with a firm date.

## When to use
You have a `name` and want to know whether the person appears in national US news: as a subject of reporting (crime, accident, missing-person appeal, court case), a quoted source, an interviewee, a bylined journalist, or in an obituary/tribute. News hits are valuable for a date-stamped event, a location, named associates/relatives, and quotes that establish presence, role or last-known status — often the anchor point for a timeline.

## How to use it (`bestInteractionPattern`: web-manual)
1. Use NBC's on-site search, or Google-dork it: `site:nbcnews.com "<full name>"` (add a city/event term to cut noise).
2. Open matching articles and read for the exact connection — subject, source, byline or mention — plus date, location and named associates.
3. For a missing-person or incident, note the reporter and any linked local NBC affiliate for follow-up.
4. Pivot: named `associate`/relatives feed relationship mapping; an event date/location anchors a timeline; a byline feeds journalist enumeration.

## Inputs → Outputs
- **In:** `name`
- **Out:** `social-profile`/byline, named `associate`/relatives, event date, location and quoted context
- **Empty/negative result looks like:** no articles for the name — the person hasn't featured in NBC's national coverage (common; try local outlets and other nationals), or same-name collisions you must disambiguate by context.

## Gotchas & OpSec
- National outlet: most people never appear — pair with local/regional news for ordinary subjects.
- Same-name collisions are frequent; confirm identity from article detail before linking.
- Journalism is interpretation — treat facts as reported, corroborate with primary records.

## Overlaps ("do both")
- Pairs with local-news search, Google News and obituary/court-record tools — nationals catch high-profile events, locals catch everyday ones; together they build the fullest media picture.

## Trust & verifiability
`trust: trusted` — a major professional news organisation; reporting is editorially sourced but is still secondary journalism, so anchor to primary records where possible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nbc-united-states |
| category | communities-forums |
| selectorsIn → selectorsOut | name → social-profile, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

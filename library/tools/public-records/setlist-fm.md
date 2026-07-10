---
id: setlist-fm
name: setlist.fm
description: Use when you have a performer/band `name` and want their concert history — dates, venues and cities — returns geolocation and address of gigs plus a timeline.
url: https://www.setlist.fm/
category: public-records
path:
- public-records
bestFor: Tracing a musician's or band's tour history — where and when they performed (venues, cities, dates) via crowd-sourced setlists.
selectorsIn:
- name
selectorsOut:
- geolocation
- address
- name
status: live
pricing: free
costNote: Free crowd-sourced database; no account needed to browse.
opsec: passive
opsecNote: Browsing public setlists is passive toward the subject. Standard web-server logging by setlist.fm applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Large, long-running crowd-sourced concert database (owned by Live Nation); data is fan-submitted, so dates/venues are usually accurate for notable acts but can be incomplete or wrong for obscure ones.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- setlist.fm
- setlistfm
tags:
- music
- concerts
- tour-history
- timeline
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# setlist.fm

> A crowd-sourced database of concert setlists — turn a performer's name into a dated map of where they've played, useful for placing a musician at specific venues and times.

## When to use
Your subject is a musician, DJ, band member or performer, and you want their movement/timeline: which venues and cities they played, on what dates. Setlist.fm's per-artist gig history is effectively a travel log — invaluable for building a timeline, confirming someone was in a city on a date, or finding the venues (and thus locations) a performer frequents. Start from an artist `name`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to setlist.fm and search the artist/band `name`.
2. Open the artist page and browse the chronological list of concerts — each entry shows date, venue and city.
3. Note the venues (`address`) and cities (`geolocation`) and build a timeline of appearances.
4. Drill into individual gigs for the setlist, sometimes with notes/photos that add context.
5. Pivot: venues/cities feed geolocation and local-source work; tour dates anchor a timeline; support acts and collaborators become `associate` leads.

## Inputs → Outputs
- **In:** performer/band `name`
- **Out:** `geolocation` (cities of performances), `address` (venues), `name` (confirmed artist + collaborators)
- **Empty/negative result looks like:** no artist page or a sparse history — meaning the act isn't covered or fans haven't submitted setlists; obscure or non-touring performers may be absent, so absence isn't conclusive.

## Gotchas & OpSec
- **Crowd-sourced:** coverage and accuracy vary — great for touring acts, thin for obscure/local ones; verify key dates against other sources (venue listings, news).
- It's a *performance* log, not a residence or contact source — it places someone at gigs, not at home.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with social-media event posts and venue/ticketing listings — cross-check a setlist.fm date against the artist's own posts or ticket archives to confirm the appearance and enrich the timeline.

## Trust & verifiability
`trust: community` — a large, generally reliable crowd-sourced database; confirm any critical date/venue against an independent source, since entries are fan-submitted.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | setlist-fm |
| category | public-records |
| selectorsIn → selectorsOut | name → geolocation, address, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

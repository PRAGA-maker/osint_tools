---
id: find-who-events
name: Find Who Events
description: Use when you have a location and keywords and want to find public events (Facebook, Eventbrite, etc.) tied to that place — a pre-built Google Custom Search Engine — returns event pages and geolocation/social-profile leads.
url: https://cse.google.com/cse?cx=017922636351918147428:v7m0tfgk6uj
category: search-engines
path:
- search-engines
bestFor: Searching public event listings across event platforms by location and keyword via a Google CSE.
selectorsIn:
- geolocation
- name
selectorsOut:
- geolocation
- social-profile
status: live
pricing: free
costNote: Free Google Custom Search Engine; no account required to run a query.
opsec: passive
opsecNote: It's a Google search over public event sites — you query Google, not the event organiser or attendees, so it's passive. Google logs the query to your session; use a clean/sock-puppet browser. Note a CSE is owned by a third party and can be edited or removed without notice.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-built Google CSE that restricts search to event platforms; results are Google's (authoritative), but the site scope is the curator's choice and may drift.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- events Google CSE
- find events by location
tags:
- meta-search
- events
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Find Who Events

> A pre-scoped Google Custom Search Engine that searches public event platforms (Facebook Events, Eventbrite, and similar) by location and keyword.

## When to use
When you want to find public events tied to a place or a name and don't want general web noise. This CSE limits Google to event-listing sites, so a `geolocation` + keyword (or a person/organisation `name`) query surfaces relevant events — useful for placing a subject at a gathering, finding organisers/attendee-facing pages, or mapping activity around a location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE at https://cse.google.com/cse?cx=017922636351918147428:v7m0tfgk6uj in a sock-puppet browser.
2. Enter a query combining location + keywords (e.g. a city plus a topic, or a person/org name).
3. Read the results — event pages on Facebook/Eventbrite/etc.
4. Open promising events for dates, venues, organisers, and attendee-facing details.
5. Pivot: an event page → the organiser's `social-profile`, the `geolocation`/date, and named attendees to run through people/username tools.

## Inputs → Outputs
- **In:** `geolocation` + keyword, or a `name`
- **Out:** public event pages revealing `geolocation`, dates, and `social-profile` leads
- **Empty/negative result looks like:** no events returned — the term is sparse, the event is private/unindexed, or the CSE's site scope doesn't cover the relevant platform; broaden terms or search each platform natively.

## Gotchas & OpSec
- **CSE fragility:** it's owned by a third party and can be edited or deleted, and its site list may be dated — cross-check by searching event platforms directly.
- Only *public* events are indexed; private events won't appear.
- Passive, but Google logs your query — use a clean browser.

## Overlaps ("do both")
- Complements native Facebook Events / Eventbrite search and general dorking; the CSE is a fast first pass, the platforms give depth.

## Trust & verifiability
`trust: community` — the engine is Google (authoritative results) but the *scope* is a community curator's choice that may drift; treat coverage as partial and verify important hits on the source platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | find-who-events |
| category | search-engines |
| selectorsIn → selectorsOut | geolocation, name → geolocation, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

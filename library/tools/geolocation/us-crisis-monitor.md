---
id: us-crisis-monitor
name: US Crisis Monitor
description: Use when you have a `geolocation` or `address` in the US and want to know what protests, political violence, or armed-group activity was recorded there and when — returns dated, mapped `geolocation` events.
url: https://acleddata.com/special-projects/us-crisis-monitor/
category: geolocation
path:
- geolocation
bestFor: Establishing whether civil unrest or political violence occurred at a US location on or around a given date.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: The interactive map and headline curation are free to browse; the full underlying event dataset (Data Export Tool / API) requires a free registered ACLED account, and some deeper analysis pages sit behind an access level.
opsec: passive
opsecNote: You are reading ACLED's published data, not querying anything about your subject, so there is no target-side footprint. Register the export account under a research identity if you prefer not to tie downloads to your real name.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Run by ACLED (Armed Conflict Location & Event Data Project) with the Bridging Divides Initiative; a peer-recognised academic conflict-event dataset with published sourcing and coding methodology.
missingPersonsRelevance: medium
coverage:
- us
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- acled-data-crisis-map
- global-conflict-tracker
- acled-armed-conflict-location-and-event-data-project
aliases:
- ACLED US Monitor
- US Crisis Monitor ACLED
tags:
- conflict-events
- protests
- situational-context
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# US Crisis Monitor

> ACLED's US-focused conflict-event tracker: a dated, geocoded map of protests, riots, and political violence across the United States.

## When to use
You have a US `geolocation` or `address` and a rough date, and you want the situational backdrop: was there a protest, riot, armed-group mobilisation, or targeted political violence at or near that place around that time? This is context, not a person-locator — useful when someone was last seen near an event, when you need to gauge whether an area was volatile on a given day, or when you are corroborating a subject's claim that they were "at the protest downtown."

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://acleddata.com/special-projects/us-crisis-monitor/ and load the interactive map.
2. Zoom to the city/region of interest and set the date window; each plotted dot is a coded event (type, actors, date, location, a source-linked summary).
3. Click an event to read its curated description and follow the cited source links back to the original reporting.
4. For systematic work, register a free ACLED account and use the Data Export Tool / API to pull the raw events as CSV filtered by state, date, and event type.
5. Pivot: an event's source links feed local-news OSINT; a confirmed unrest window at a `geolocation` feeds your timeline and other geolocation tools like `[[acled-data-crisis-map]]`.

## Inputs → Outputs
- **In:** `geolocation` / `address` (a US place + date window)
- **Out:** `geolocation` — dated, mapped events with type, actors, and cited-source summaries
- **Empty/negative result looks like:** no dots in the map area/date range means ACLED coded no qualifying event there — absence of a recorded protest, not proof nothing happened (small or unreported incidents may be below their sourcing threshold).

## Gotchas & OpSec
- Human-in-the-loop: browsing the map is open; the full dataset export needs a (free) account login.
- Scope is the United States only, and events, not people — it will never return a name or a person's location, only what happened at a place.
- Coding lag: recent days may be under-populated until ACLED's weekly update ingests them.
- OpSec: fully passive; you query ACLED, never your subject.

## Overlaps ("do both")
- Pairs with `[[acled-data-crisis-map]]` and `[[global-conflict-tracker]]` — the crisis map gives the global ACLED picture while this special project curates and contextualises the US subset with richer editorial coverage.

## Trust & verifiability
`trust: trusted` — ACLED is an established, methodologically transparent academic event dataset; every event links to its source, so you can verify each dot rather than take it on faith.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | us-crisis-monitor |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |

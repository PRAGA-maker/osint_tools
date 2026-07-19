---
id: tripit
name: TripIt
description: Use when you have a `name` or `username` and want to check for a public TripIt travel profile — returns social-profile and, rarely, trip/travel context.
url: https://www.tripit.com
category: communities-forums
path:
- communities-forums
bestFor: Checking whether a subject maintains a public TripIt profile and whether any itineraries are shared publicly.
selectorsIn:
- name
- username
- email
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free tier organizes itineraries from forwarded confirmation emails; TripIt Pro is a paid upgrade but irrelevant to OSINT lookups.
opsec: passive
opsecNote: The public surface is thin — TripIt itineraries are private by default and are only visible if the user deliberately shares a trip via a public link or a synced calendar. Viewing a shared public link is passive; do not attempt to log in as or contact the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: First-party travel app (Concur/SAP owned), but as an OSINT source it is low-yield: the platform has no public people-search and profiles are private unless explicitly shared.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- tripit.com
tags:
- toddington
- curated-directory
- online-communities-blogs
- travel
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# TripIt

> A travel-itinerary organizer with almost no public search surface — relevant to OSINT only when a subject has deliberately shared a trip via a public link or synced calendar.

## When to use
Reach for this only as a completeness check. TripIt has **no public people-search**; itineraries are private by default. It becomes an OSINT source in two narrow cases: (1) the subject published a shared-trip link (indexable by search engines, exposing dates, destinations, flights, hotels), or (2) they exposed a TripIt calendar (.ics) feed. If you have a `name`/`email`/`username`, use it to hunt for those leaked artifacts elsewhere, not to search TripIt directly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Do NOT expect an on-site people search — there isn't one. Instead, pivot to a search engine.
2. Run a dork: `site:tripit.com <name>` or `site:tripit.com/trips` combined with a username/handle, to surface any publicly shared itinerary pages.
3. Search for exposed calendar feeds: the subject's email/username plus `tripit ics` or `webcal`.
4. If a shared trip page appears, read the itinerary — travel dates, cities, airlines, hotels — as pattern-of-life data.
5. Pivot: destinations/dates feed timeline building and cross-reference with geotagged social posts.

## Inputs → Outputs
- **In:** `name`, `username`, or `email` (used against search engines, not TripIt's own search)
- **Out:** a public `social-profile`/shared-trip page if one exists; travel dates and destinations when a trip is publicly shared
- **Empty/negative result looks like:** no indexed tripit.com results — the expected case, since sharing is off by default. Absence tells you nothing about whether the person uses TripIt.

## Gotchas & OpSec
- Low yield by design: most users never make anything public.
- Do not create an account to "find" someone — TripIt has no friend/search graph to exploit, so it wastes time and adds an account footprint.
- OpSec: passive — only ever view already-public shared links; never attempt access to a private itinerary.

## Overlaps ("do both")
- Combine with geotagged social-media OSINT — a shared TripIt itinerary corroborates (or contradicts) location claims in posts.

## Trust & verifiability
`trust: unverified` — the app itself is legitimate (Concur/SAP), but as an intelligence source it is thin and opportunistic; anything found is genuinely the subject's shared content, so it is high-confidence when it exists but rarely exists.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tripit |
| category | communities-forums |
| selectorsIn → selectorsOut | name, username, email → social-profile, username |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

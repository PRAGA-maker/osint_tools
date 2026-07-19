---
id: wikitravel
name: Wikitravel
description: Use when you have a `geolocation` (a place name in a case) and want crowdsourced local knowledge — neighborhoods, transport, landmarks, "get in/get around" logistics — returns background context to interpret a location, not personal data.
url: https://wikitravel.org
category: search-engines
path:
- search-engines
bestFor: Getting a fast human-written orientation to an unfamiliar destination (layout, transport hubs, districts, common tourist routes) referenced in an investigation.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: degraded
pricing: free
costNote: Free, ad-supported community wiki. No account needed to read.
opsec: passive
opsecNote: Reading a public travel wiki reveals nothing about your subject and touches no target infrastructure. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowdsourced and community-edited; largely frozen since most contributors forked to Wikivoyage (2012), so entries can be dated and some pages carry spam. Corroborate specifics.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- wikitravel.org
tags:
- toddington
- curated-directory
- specialty-search
- travel
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
relatedTools:
- wikitravel-org
---

# Wikitravel

> A crowdsourced travel guide — human-written local orientation for a place named in a case (transport, districts, landmarks), not a people-lookup.

## When to use
A `geolocation` appears in your investigation — a city, town, or region a subject travelled to, mentioned, or was last seen near — and you need quick local context to interpret it: how you get in and around, which districts/neighbourhoods exist, major transport hubs, well-trodden tourist routes, and notable landmarks. That context helps you read a photo background, judge whether a stated itinerary is plausible, or scope where to look next. It will not tell you anything about a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://wikitravel.org and search the destination (city or region).
2. Read the "Get in", "Get around", "Districts", "See", and "Sleep" sections for transport, layout, and landmark orientation.
3. Cross-check anything you'll rely on — Wikitravel is dated; confirm current transport/place details against a live map or `[[wikivoyage]]`-style current source.
4. Use district/landmark names as search terms elsewhere (maps, social geotags) to narrow a location.
5. Pivot: feed identified place names into a mapping tool or geolocation workflow; for the successor/fresher content, prefer Wikivoyage.

## Inputs → Outputs
- **In:** `geolocation` (place name)
- **Out:** `geolocation` context — districts, transport, landmarks, logistics for that place
- **Empty/negative result looks like:** thin or missing pages for small/less-touristed places, or a page dominated by dated/spam edits — treat sparse coverage as "check a current source," not as authoritative.

## Gotchas & OpSec
- Human-in-the-loop: none.
- **Stale content risk:** the active community migrated to Wikivoyage years ago, so opening hours, prices, and transport details may be years out of date. Use it for orientation, verify specifics elsewhere.
- Anyone can edit — corroborate any claim you'd act on.

## Overlaps ("do both")
- Pairs with `[[wikitravel-org]]` (its phone-number reference page) and with a current travel wiki (Wikivoyage) — Wikitravel gives quick orientation; a live source confirms today's details.

## Trust & verifiability
`trust: community` — an open, crowdsourced wiki that is largely frozen since the Wikivoyage fork; reliable as rough orientation but not as current fact, so verify anything specific against an up-to-date source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikitravel |
| category | search-engines |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

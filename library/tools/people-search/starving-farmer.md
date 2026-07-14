---
id: starving-farmer
name: Starving Farmer
description: Use when you have a `name` you believe belongs to a US farmer and want to place them in a state/county — returns name, address (county/state). Niche directory, browse by state.
url: https://www.starvingfarmer.com
category: people-search
path:
- people-search
bestFor: Locating a named US farmer within a state/county via a browsable agricultural directory.
selectorsIn:
- name
- geolocation
selectorsOut:
- name
- address
status: live
pricing: free
costNote: Free to browse; a static directory site with no account or payment.
opsec: passive
opsecNote: Read-only browse of a static public directory; nothing is sent to the subject. No login, so no attribution beyond ordinary web-server logs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A self-published "Directory of American Farmers" (2015 base data) with no cited sourcing or verification process; useful as a corroborating lead, not authoritative.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Directory of American Farmers
tags:
- people-search
- directory
- agriculture
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# Starving Farmer

> A niche, browsable US farmer directory (name + county + state) — narrow, dated, but occasionally the one place a specific agricultural subject is listed.

## When to use
You have a `name` that plausibly belongs to a US farmer/agricultural worker and want to tie them to a state and county — or you want to enumerate listed farmers in a given `geolocation`. This is a specialist directory, not a general people-search: reach for it only when the subject has a farming connection, as a corroborating data point.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.starvingfarmer.com.
2. Select a US state to drill into that state's farmer listings.
3. Narrow by county and scan for the subject `name`; open the individual listing.
4. Read the entry: farmer name, county, and state (e.g. "Larry Pierce, Clark County, Iowa").
5. Pivot: take the confirmed name + county into a full people-search or county property/voter records to get current `address`/`phone`.

## Inputs → Outputs
- **In:** `name` and/or `geolocation` (US state)
- **Out:** `name`, `address` (county + state granularity only)
- **Empty/negative result looks like:** the state page lists no matching name — meaning they aren't in this directory, which covers only a slice of US farmers as of its ~2015 base data.

## Gotchas & OpSec
- Base data dates to ~2015; treat placements as historical leads, not current addresses.
- Coverage is partial and self-reported — absence proves nothing.
- Address granularity is county-level, not a street address; you must pivot elsewhere to localise.
- OpSec: fully passive, static-site browse.

## Overlaps ("do both")
- Pairs with county assessor/property and voter-record searches that turn a county-level farmer hit into a precise `address`.

## Trust & verifiability
`trust: unverified` — a self-published static directory with no sourcing or update guarantee; use a hit only to seed and corroborate, never as a standalone fact.

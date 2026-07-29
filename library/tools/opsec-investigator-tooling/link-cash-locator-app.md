---
id: link-cash-locator-app
name: LINK Cash Locator App
description: Use when you have a `geolocation`/`address` in the UK or Crown Dependencies and want the nearest cash machines — returns ATM `address`es and map `geolocation`s from the LINK network.
url: https://play.google.com/store/apps/details?id=com.linkschemeltd.atmlocator&hl=en_CA
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Mapping ATMs near a point in the UK, Jersey, Guernsey, Gibraltar or the Isle of Man.
selectorsIn:
- geolocation
- address
selectorsOut:
- address
- geolocation
status: live
pricing: free
costNote: Free Android app published by LINK Scheme Ltd; no account required.
opsec: passive
opsecNote: Queries run against LINK's public ATM directory, not against any person, so it leaks nothing about a target. It does request your location/map data through the app — run it on a clean device if that matters.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: trusted
trustNote: Published by LINK Scheme Ltd, the operator of the UK's national ATM network; the underlying data is authoritative first-party ATM location data.
missingPersonsRelevance: low
coverage:
- uk
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools: []
aliases:
- LINK ATM Locator
- Cash Locator
tags:
- toddington
- add-ons-apps-extensions
- geolocation
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# LINK Cash Locator App

> The official app of the UK's LINK ATM network: given a place, it lists the cash machines around it — a small geolocation reference for UK and Crown Dependency work.

## When to use
You are working a UK-area case and need to know where a subject could have withdrawn cash near a known `address` or `geolocation` — corroborating a route, narrowing a CCTV canvas, or checking what ATMs sit by a last-known location. It returns ATM points, not personal data, so it is a supporting geospatial reference rather than a lead generator.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install the LINK Cash Locator app from Google Play on an Android device (or use the LINK website's ATM locator for a desktop equivalent).
2. Enter a location — a postcode, `address`, or drop a pin at a `geolocation`; or let it use current GPS.
3. Read the map/list of nearby ATMs, each with an `address` and coordinates, plus attributes (free-to-use vs. fee, wheelchair access, deposit).
4. Note the specific machines within your radius of interest.
5. Pivot: an ATM location feeds a physical canvas — nearby CCTV, businesses, and transport — and can be cross-referenced with any transaction/time information you already hold (which the app itself does not provide).

## Inputs → Outputs
- **In:** a UK-area `geolocation`, postcode, or `address`
- **Out:** nearby ATM `address`es and map `geolocation`s with fee/access attributes
- **Empty/negative result looks like:** no machines returned for a point — either you are outside LINK's coverage (UK, Jersey, Guernsey, Gibraltar, Isle of Man) or genuinely in an ATM desert; it is not a data error to escalate.

## Gotchas & OpSec
- Human-in-the-loop: it is a phone app you drive by hand; nothing is scriptable.
- OpSec: passive with respect to the target — you query a public ATM directory, not a person. The app does want device location, so use a clean/investigation device if you care about that.
- Coverage is UK and Crown Dependencies only; it is useless outside that footprint.

## Overlaps ("do both")
- Pair with general mapping (Google/Apple Maps, OpenStreetMap) for the surrounding physical context; LINK's advantage is an authoritative, ATM-complete layer that generic maps under-represent.

## Trust & verifiability
`trust: trusted` — first-party data from LINK Scheme Ltd, the body that actually runs the UK ATM network, so the ATM locations are as authoritative as this data gets.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | link-cash-locator-app |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | geolocation, address → address, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | mobile-app |
| opsec | passive |
| human-in-loop | yes (account-login) |

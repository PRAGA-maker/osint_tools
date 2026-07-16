---
id: little-rock-ar-crime-search
name: Little Rock AR Crime Search
description: Use when you have an `address` or `geolocation` in Little Rock, AR and want reported crime incidents at/near it — returns incident records (offense, date, location) as `geolocation` context.
url: https://b2.caspio.com/dp.asp?AppKey=88321000961d92fc4ed343f38a0e
category: public-records
path:
- public-records
bestFor: Pulling reported crime incidents by address, ZIP, offense type, or date range in Little Rock, Arkansas.
selectorsIn:
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public crime-incident search; no account or payment.
opsec: passive
opsecNote: You query a public records database about a location, not a person's account — the subject is never contacted. Requires browser cookies enabled. Use a sock-puppet browser as routine hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A Caspio-hosted front-end over Little Rock crime data; incident records are official but this is a third-party portal, so corroborate against the LRPD/city source for anything evidentiary.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Little Rock crime incident search
tags:
- crime
- public-records
- arkansas
source: osint4all
lastVerified: '2026-07-16'
enrichment: full
---

# Little Rock AR Crime Search

> A searchable database of reported crime incidents in Little Rock, Arkansas — query by address, ZIP, offense type, or date to see what happened at or near a location.

## When to use
You have an `address`, ZIP, or rough `geolocation` in Little Rock and want the reported-crime context for it: incidents at a residence, near a last-known location, or within a date window relevant to a disappearance. It is a location/incident tool, not a name lookup — use it to corroborate or add context, not to identify a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Caspio search page (enable cookies if prompted) at the URL above.
2. Enter your criteria — incident number, offense type (aggravated assault, burglary, motor vehicle theft, robbery, shoplifting, etc.), location/address, ZIP (Little Rock range), and/or a from/to date range.
3. Read the returned incident rows: offense, date, and location.
4. Pivot: an incident at/near your subject's `address` in the relevant window is a lead to chase in LRPD reports or local news; a cluster gives area context.

## Inputs → Outputs
- **In:** `address` / ZIP / offense type / date range (Little Rock, AR only)
- **Out:** matching crime-incident records (offense, date, `geolocation`)
- **Empty/negative result looks like:** no rows returned — no reported incident matched those filters; widen the date range or offense type before concluding nothing happened.

## Gotchas & OpSec
- Geographic scope is Little Rock, AR only — useless outside that jurisdiction.
- Reported incidents ≠ convictions or confirmed facts; treat rows as reports to corroborate.
- OpSec: passive; you query a public dataset about a place, so no subject is alerted. Cookies must be enabled for the Caspio app to run.

## Overlaps ("do both")
- Pairs with LRPD/city open-data crime portals and local news search — this gives the structured incident row; those confirm and add narrative detail.

## Trust & verifiability
`trust: community` — a third-party Caspio portal over Little Rock crime data; the incidents originate from official reports, but verify anything you would act on against the primary LRPD/city source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | little-rock-ar-crime-search |
| category | public-records |
| selectorsIn → selectorsOut | address → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

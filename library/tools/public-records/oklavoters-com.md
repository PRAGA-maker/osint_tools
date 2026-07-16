---
id: oklavoters-com
name: Oklavoters.com
description: Use when you have a `name` in Oklahoma and want voter-registration details (address, party, precinct) — returns address, name, dob.
url: http://oklavoters.com/
category: public-records
path:
- public-records
bestFor: Looking up Oklahoma voter-registration records (address, party, registration status) by name from public state data.
selectorsIn:
- name
selectorsOut:
- address
- name
- dob
status: degraded
pricing: freemium
costNote: Oklahoma voter-registration data is public under state open-records law; third-party republishers like this may offer free name lookups and charge for bulk downloads or extra fields.
opsec: passive
opsecNote: Voter records are public and searches are not disclosed to the registrant. Use a clean browser; treat any residential address returned as sensitive and handle it per your engagement's rules.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party republisher of Oklahoma voter data, not the state election board; verify anything critical against the official OK Voter Portal.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- oklavoters
- Oklahoma voter search
tags:
- voter-records
- public-records
source: osint4all
lastVerified: '2026-07-16'
enrichment: full
---

# Oklavoters.com

> A third-party lookup over Oklahoma's public voter-registration data — name to address, party and precinct.

## When to use
You have a `name` believed to be in Oklahoma and want to confirm a current `address`, party affiliation, precinct and registration status. Voter records are one of the more reliable free routes to a current residential address in the US, which makes them valuable for placing a person geographically.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open `oklavoters.com` in a clean browser session.
2. Enter the subject's `name` (first + last; add county/city if the form allows, to cut common-name noise).
3. Read the results:
   - A record typically shows the registrant's name, residential `address`, party, precinct and status, and often a birth year (`dob` component).
   - Multiple same-name records mean you must disambiguate by address, age or precinct.
4. Pivot: the address feeds property records, neighbours and reverse-address lookups; the birth year narrows other people-search matches.

## Inputs → Outputs
- **In:** `name` (Oklahoma resident)
- **Out:** `address` (residential), `name` (registered spelling), `dob` (often birth year), plus party/precinct
- **Empty/negative result looks like:** no record — meaning the person isn't a registered Oklahoma voter under that name (they may be unregistered, moved, or in another state), not that they don't exist.

## Gotchas & OpSec
- **Degraded / verify:** this is a third-party republisher and was intermittently unreachable at last check; the authoritative source is the official **OK Voter Portal** (`okvoterportal.okelections.gov`) and the state Election Data Warehouse. Cross-check critical findings there.
- Voter data ages between registration updates — a listed address can be stale.
- OpSec: passive; the registrant is not notified. Residential addresses are sensitive PII — handle accordingly.

## Overlaps ("do both")
- Pairs with the official OK Voter Portal and with national voter aggregators (VoterRecords-style) — the official portal is authoritative, aggregators widen coverage beyond Oklahoma.

## Trust & verifiability
`trust: community` — a third-party mirror of public voter data; treat results as leads and confirm against the state election board before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | oklavoters-com |
| category | public-records |
| selectorsIn → selectorsOut | name → address, name, dob |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

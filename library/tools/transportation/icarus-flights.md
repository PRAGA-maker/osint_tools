---
id: icarus-flights
name: Icarus.flights
description: Use when you have an aircraft tail number (`vehicle-plate`) or an owner `name`/`employer-org` and want live and historical flight tracking with unfiltered ownership data — returns `geolocation`, `associate`, `employer-org`.
url: https://icarus.flights/
category: transportation
path:
- transportation
bestFor: Tracking an aircraft's live and historical movements and ownership when commercial trackers hide it.
selectorsIn:
- vehicle-plate
- name
- employer-org
selectorsOut:
- geolocation
- associate
- employer-org
status: live
pricing: free
costNote: Free service, but access is not open — you must contact C4ADS and be approved for an account before you can use it.
opsec: passive
opsecNote: Queries run against C4ADS's platform, not the aircraft owner, so the subject sees nothing. You are, however, identifiable to C4ADS under the account you register — use it for legitimate investigative work only, consistent with their terms.
humanInLoop: true
humanInLoopReason:
- account-login
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built and operated by C4ADS, an established non-profit investigative organization; data is transponder/ADS-B feeds plus curated ownership records, not a random scraper.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: true
relatedTools:
- osintcurious
aliases:
- Icarus Flights
- C4ADS Icarus
tags:
- flight-tracking
- aviation
- Maps, Geolocation and Transport
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Icarus.flights

> C4ADS's investigator-grade flight tracker: live and historical aircraft movements with the ownership data that commercial sites let owners hide.

## When to use
You have an aircraft tail/registration number (the "plate" of a plane), or an owner `name`/`employer-org`, and you need to reconstruct where an aircraft has been, who owns it, and which entities it links to. Unlike Flightradar24/FlightAware, Icarus deliberately does **not** honor owner-requested blocking (the FAA/ICAO privacy lists), so the exact planes an investigator cares about stay visible. Relevant to a missing-persons case when a subject or an associate has access to private aviation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Request access: Icarus is free but gated — apply through https://icarus.flights/ (C4ADS reviews and approves accounts). You cannot search until approved.
2. Log in at https://app.icarus.flights/.
3. Search by aircraft registration/tail number, operator, or owner name.
4. Read the output: a map/timeline of tracked positions (`geolocation`) plus ownership and operator records (`employer-org`, `associate`).
5. Pivot: an owner entity feeds corporate-records and people-search tools; a repeated destination airport feeds geolocation work; linked operators feed `associate` mapping.

## Inputs → Outputs
- **In:** `vehicle-plate` (aircraft tail number), `name`, or `employer-org`
- **Out:** `geolocation` (flight path/positions), `employer-org` and `associate` (ownership/operator links)
- **Empty/negative result looks like:** no tracked flights for the tail number (aircraft may be non-transponding, foreign-only, or long grounded) — absence is not proof the aircraft doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: access requires an account approved by C4ADS (manual review); there is no anonymous or instant use.
- OpSec: passive toward the target, but every query is tied to your approved account — use only for legitimate investigations.
- Coverage depends on ADS-B receiver density; remote regions have gaps.

## Overlaps ("do both")
- Pairs with `[[osintcurious]]` methodology write-ups and general aviation trackers — Icarus surfaces the owner-blocked aircraft that public trackers suppress, so cross-check a tail number in both.

## Trust & verifiability
`trust: trusted` — C4ADS is a recognized non-profit investigative organization; the data is authoritative transponder feeds and curated ownership records rather than an unvetted scrape.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | icarus-flights |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate, name, employer-org → geolocation, associate, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, manual-review) |

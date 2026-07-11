---
id: ufind-name
name: uFind.name
description: Use when you have a `name` (or a `phone`/`email`) in the US and want a consolidated people-search profile — returns addresses, phone numbers, emails, relatives and social profiles.
url: https://ufind.name/
category: people-search
path:
- people-search
bestFor: A single name-to-profile lookup that aggregates address history, phones, emails, relatives and (via VIN) vehicle links for US subjects.
selectorsIn:
- name
- phone
- email
selectorsOut:
- address
- phone
- email
- associate
- social-profile
- vin
status: live
pricing: freemium
costNote: Search and partial results are free; fuller reports (complete phone/address history, background details) are gated behind paid data-broker report tiers typical of US people-search sites.
opsec: passive
opsecNote: Querying is passive — the subject is not notified. However, aggregator sites log searcher IP/queries and may show ads/retargeting; use a clean browser and consider a VPN. Do not enter your own identifying details into any "unlock report" upsell.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A US data-broker-style aggregator; results are compiled from public records and third-party data of variable freshness and accuracy — corroborate before relying on any single field.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- ufind.name
- uFind people search
tags:
- people-search
- data-broker
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# uFind.name

> A free-to-search US people-aggregator that pulls address history, phones, emails, relatives and vehicle links into one profile.

## When to use
You have a subject `name` (optionally with a city/state to disambiguate), or a reverse selector like a `phone` or `email`, and want a fast consolidated snapshot for a US person: where they've lived, numbers and addresses associated with them, named relatives, and linked social/VIN data. Reach for it early as a broad people-search sweep to generate leads you then corroborate against primary records.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://ufind.name/ in a clean/VPN'd browser.
2. Enter the `name` (add a state/city to narrow), or run a reverse `phone`/`email` search.
3. Pick the matching person from the result list and open the profile: address history, phone numbers, emails, relatives (`associate`), social links, and any VIN/vehicle records.
4. Treat free fields as leads; the site upsells a fuller paid report — do not enter your own PII to "unlock."
5. Pivot: relatives feed family-network mapping, an address feeds property/voter records, a phone feeds carrier/Truecaller checks.

## Inputs → Outputs
- **In:** `name` (+ location) / `phone` / `email`
- **Out:** `address` history, `phone`, `email`, `associate` (relatives), `social-profile`, `vin`
- **Empty/negative result looks like:** no matching person, or a stub profile with only a name/city and no contact data — common for young, privacy-conscious, or non-US subjects; absence is not proof.

## Gotchas & OpSec
- Accuracy varies: aggregator data is often stale or conflates same-name people — verify every field against a primary source before acting.
- Upsell traps: "unlock full report" flows may charge or harvest your details; never enter the investigator's real PII.
- OpSec: passive to the subject, but the site logs your queries — use a clean session/VPN.

## Overlaps ("do both")
- Pairs with `[[thatsthem]]` and `[[411directoryassistance-ca]]` — different aggregators index different records, so run several and reconcile.
- Pairs with property/voter-record tools to confirm an address the aggregator suggests.

## Trust & verifiability
`trust: community` — a commercial data-broker aggregator, not an authoritative source; useful for lead generation but every result must be corroborated against primary public records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ufind-name |

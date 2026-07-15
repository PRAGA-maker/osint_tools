---
id: thatsthem-vin-search
name: ThatsThem VIN Search
description: Use when you have a `vin` and want to identify the vehicle and any linked owner records — returns vehicle make/model/year plus, where matched, the owner `name` and `address`.
url: https://thatsthem.com/vin-search
category: transportation
path:
- transportation
bestFor: Turning a US vehicle VIN into make/model/year and, when ThatsThem has a match, the associated owner's name and address.
selectorsIn:
- vin
selectorsOut:
- name
- address
- vehicle-plate
status: live
pricing: free
costNote: Free to search; no account required. ThatsThem is ad-supported and upsells paid background-report partners, but the core VIN and people lookups are free.
opsec: passive
opsecNote: Passive query against ThatsThem's aggregated public-records/marketing data — the vehicle owner is not notified. Your search and IP are logged by ThatsThem; use a sock-puppet browser/VPN for sensitive work. Note ThatsThem is a data-broker aggregator, so accuracy varies and some links are stale.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ThatsThem is a free US people-search/data-broker aggregator; coverage and freshness are inconsistent (a valid VIN may return no owner match). Treat owner links as leads, not proof.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- thatsthem VIN
- ThatsThem vehicle lookup
tags:
- vehicle
- vin
- people-search
source: metaosint
relatedTools:
- thats-them
- thatsthem
- thatsthem-2
- thatsthem-people-search
- thatsthem-phone-search
- vin-lookup
lastVerified: '2026-07-15'
enrichment: full
---

# ThatsThem VIN Search

> A free US VIN lookup that decodes the vehicle and, when it can, ties it to an owner's name and address from ThatsThem's aggregated records.

## When to use
You have a `vin` — from a vehicle photo, a document, or a plate-to-VIN step — and want to know both what the vehicle is (make/model/year) and who is linked to it. ThatsThem decodes the VIN and, where its aggregated people-data has a match, returns an owner `name` and `address`. Useful in missing-person and skip-trace work where a vehicle is the strongest lead to a current location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://thatsthem.com/vin-search in a sock-puppet browser.
2. Enter the full 17-character `vin` and submit.
3. Read the vehicle decode (make, model, year) and any linked owner record (`name`, `address`).
4. If no owner is linked, still capture the decode and pivot: use ThatsThem's reverse-address/name/phone searches on any partial lead, or cross-check the VIN on a dedicated VIN decoder.
5. Pivot: an owner name/address feeds `[[thatsthem]]` reverse-address and general people-search; the vehicle spec corroborates a sighting.

## Inputs → Outputs
- **In:** `vin` (17 characters)
- **Out:** vehicle make/model/year, and where matched owner `name` + `address`
- **Empty/negative result looks like:** the VIN decodes to a vehicle but "no owner information" — common, because ThatsThem's owner linkage is patchy. A valid VIN with no owner match is a coverage gap, not an invalid VIN.

## Gotchas & OpSec
- Owner linkage is inconsistent — ThatsThem is a marketing-data aggregator, not a DMV; absence of an owner is normal and presence should be corroborated.
- US-centric; foreign VINs may decode but will rarely have owner links.
- OpSec: **passive**; the owner is not alerted, but your query is logged — sock-puppet sensitive searches.

## Overlaps ("do both")
- Pairs with `[[thatsthem]]` (reverse name/address/phone/email) to expand a returned owner, and with a dedicated VIN decoder to validate the vehicle spec independently.

## Trust & verifiability
`trust: unverified` — a free data-broker aggregator whose owner matches are leads, not authoritative registration data; confirm any owner link through a second source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | thatsthem-vin-search |

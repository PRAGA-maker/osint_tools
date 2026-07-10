---
id: homemetry
name: Homemetry
description: Use when you have a US `address` (or `name`) and want the residents and property detail tied to it — returns current/recent resident `name`s, `phone`s, `associate`s, and property/`address` records.
url: https://homemetry.com
category: people-search
path:
- people-search
bestFor: US reverse-address lookup — resolving an address to its residents (with phones) and property history, or a name to associated addresses.
selectorsIn:
- address
- name
selectorsOut:
- name
- phone
- address
- associate
status: live
pricing: freemium
costNote: Free teaser data (residents, partial detail) with fuller records/reports gated behind a paywall/upsell, typical of US data brokers.
opsec: passive
opsecNote: You search an aggregator's compiled records, not the target — no notification. But it's a data-broker site: it logs and profiles searchers and pushes paid upsells. Use a clean/sock-puppet browser and treat results as leads, not facts.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial US address/people aggregator (117M+ properties) built from public records, tax assessments, and private sources; useful but often stale/conflated — corroborate every hit.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Homemetry
- HomeMetry
tags:
- people-investigations
- reverse-address-lookup
- property-records
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Homemetry

> A US reverse-address directory — put in an address and get its current/recent residents (with phones) and property history, or work a name back to associated addresses.

## When to use
You have a US `address` tied to a subject and want to know who lives/lived there and their contact details, or you have a `name` and want addresses associated with it. Strong for placing a person at a location, finding co-residents (`associate`s), and pulling property history in a missing-persons or background context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://homemetry.com in a clean/sock-puppet browser.
2. Enter a US `address` (reverse-address lookup) or a `name`.
3. Read the free result: current/recent residents (people and business tenants) with `phone`s, plus property detail (value, sales/tax history, size).
4. Note co-residents and prior residents as `associate` leads; use property history for an occupancy timeline.
5. Pivot: resident names/phones → `[[thats-them]]`/`[[thatsthem-phone-search]]` to confirm; property ownership → county assessor/deeds for the authoritative owner.

## Inputs → Outputs
- **In:** `address` (US) or `name`
- **Out:** resident `name`s (current/recent), `phone`s, `associate`s (co-/prior residents), property `address`/history
- **Empty/negative result looks like:** thin or no data, or paywalled teasers — common for new construction, rentals with turnover, or privacy-suppressed records. Absence/uncertainty means "corroborate elsewhere," not "no one lives there."

## Gotchas & OpSec
- Data-broker accuracy — residents can be outdated or conflated; verify before relying.
- US-only; the fuller detail is often behind a paywall/upsell.
- Passive toward the target; the broker profiles you — sock-puppet it.

## Overlaps ("do both")
- Pairs with `[[thats-them]]`, other reverse-address aggregators, and the county assessor/deeds registry — each holds different records; the assessor gives authoritative ownership, Homemetry gives residents/contacts.

## Trust & verifiability
`trust: community` — a commercial aggregator over public + private data. Treat every resident/phone as an unverified lead and confirm at a primary source.

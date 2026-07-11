---
id: publicrecordsnow
name: PublicRecordsNOW
description: Use when you have a `name`, `phone`, or `address` and want an aggregate people-search profile — teases addresses, phones, relatives, and background/criminal hits; unverified leads behind an upsell.
url: http://www.publicrecordsnow.com
category: people-search
path:
- people-search
bestFor: A fast aggregate lead-check on a US subject that points to records to confirm elsewhere.
selectorsIn:
- name
- phone
- address
selectorsOut:
- address
- phone
- associate
- name
status: live
pricing: freemium
costNote: Free search returns a teaser; full reports (contact detail, background/criminal) push toward a paid report or partner upsell.
opsec: passive
opsecNote: Searching is passive and doesn't notify the subject, but you're handing the target's identifiers to a commercial data broker that logs and monetizes queries. Use throwaway registration details and never enter real personal info.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial people-search/data-broker aggregator (claims 120B+ records from thousands of sources); compiled, often stale or conflated data — treat as leads.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Public Records Now
tags:
- toddington
- curated-directory
- people-search
- data-broker
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# PublicRecordsNOW

> A broad US data-broker aggregator: quick aggregate leads on a name/phone/address, unverified and upsell-driven — a pointer, not proof.

## When to use
You have a `name`, `phone`, or `address` and want a fast, wide net for associated addresses, phone numbers, relatives/associates, and background/criminal hints. PublicRecordsNOW compiles many sources into one profile, so it's useful early to surface threads — a possible relative, a prior address — that you then confirm against primary records.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.publicrecordsnow.com and search by `name` (add city/state), or run a reverse `phone`/`address` search.
2. Read the free teaser — it typically confirms records exist and previews partial matches.
3. Expect an upsell/paywall for full detail; decide whether the lead justifies paying (often a free primary source is better).
4. Pivot: take any surfaced `address`/`phone`/`associate` to a free authoritative source (reverse phone lookup, voter/property records, a separate search on the relative) and confirm before relying on it.

## Inputs → Outputs
- **In:** `name`, `phone`, or `address`
- **Out:** teased `address`, `phone`, `associate` (relatives), `name`, background/criminal hints (full detail gated)
- **Empty/negative result looks like:** "no records" or a teaser with no real matches. Brokers skew to US adults with a commercial footprint — thin coverage for the young, privacy-conscious, or non-US, so absence is weak evidence.

## Gotchas & OpSec
- Data quality is mixed: same-name conflation and stale addresses are common — never treat a hit as confirmed identity.
- Not FCRA-compliant — do not use for employment/tenant/credit decisions.
- OpSec: **passive** to the subject, but you're feeding a broker; use throwaway details.

## Overlaps ("do both")
- Pairs with other aggregators (`[[recordsfinder-people-search-ca]]`, TruePeopleSearch-style sites) and free primary records — run two brokers to triangulate (they disagree), then confirm the overlap at an authoritative source.

## Trust & verifiability
`trust: unverified` — a monetized aggregator with no accuracy guarantee; every field is a lead to corroborate, not a fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | publicrecordsnow |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, address → address, phone, associate, name |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |

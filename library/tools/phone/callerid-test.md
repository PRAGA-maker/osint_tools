---
id: callerid-test
name: CallerID Test
description: Use when you want the CNAM (caller-ID name) a number transmits — but the service has shut down; use a live CNAM/carrier tool instead.
url: https://calleridtest.com/
category: phone
path:
- phone
bestFor: (Defunct) CNAM caller-ID name lookup / test for a phone number.
input: Phone number
output: Caller-ID name (CNAM) the number transmits — service now discontinued.
selectorsIn:
- phone
selectorsOut:
- name
- metadata-exif
status: down
pricing: freemium
costNote: Was a paid/credit CNAM-test service; founder is refunding all customers after shutdown.
opsec: passive
opsecNote: CNAM lookups read directory metadata and do not place a call to the target; moot now that the service is closed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: untrustworthy
trustNote: Service shut down due to litigation threats under New Jersey's "Daniel's Law"; the site now serves only a closure/refund notice. Treat as defunct.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: true
relatedTools:
- carrier-lookup
aliases:
- calleridtest.com
tags:
- phone
- cnam
- defunct
source: arf-seed
lastVerified: '2026-06-13'
enrichment: full
---

# CallerID Test

> Formerly a CNAM (caller-ID name) testing/lookup service — now shut down following litigation, so it no longer returns data.

## When to use
Effectively: don't. The historical use was checking the `name` (CNAM) a `phone` number transmits on outbound calls — useful for confirming the business/person behind a number. The service has closed; route to a live CNAM/carrier alternative.

## How to use it (`bestInteractionPattern`: web-manual)
1. Visiting https://calleridtest.com/ now returns only a shutdown notice (closed after threats under New Jersey's "Daniel's Law"; refunds in progress).
2. There is no working lookup form.
3. Pivot to a live carrier/CNAM tool below.

## Inputs → Outputs
- **In:** `phone` (intended)
- **Out:** historically `name` (CNAM) and number `metadata-exif`; none available now.
- **Empty/negative result looks like:** the shutdown page — every visit.

## Gotchas & OpSec
- Status `down`/`deprecated`: the service no longer operates. Do not rely on it or attempt to register.
- OpSec: CNAM lookups are passive in principle, but here it's moot — there is nothing to query.

## Overlaps ("do both")
- Replace with `[[carrier-lookup]]` (US carrier/line type) and `[[advanced-background-checks]]` (free reverse phone to name/address); for UK carrier use `[[aql-com]]`.

## Trust & verifiability
`trust: untrustworthy` — verified 2026-06-13 that the site only serves a shutdown/refund notice. Marked `status: down`, `deprecated: true`; excluded from active use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | callerid-test |
| category | phone |
| selectorsIn → selectorsOut | phone → name (CNAM), metadata-exif — defunct |
| pricing / cost | freemium (service closed) |
| trust | untrustworthy |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

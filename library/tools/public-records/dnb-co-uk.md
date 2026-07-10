---
id: dnb-co-uk
name: dnb.co.uk
description: Use when you have a company `name` (or `employer-org`/`address`) and want to confirm the entity and its D-U-N-S number — returns `employer-org`, `address` and the D-U-N-S `document-id`.
url: https://www.dnb.co.uk/duns-number/lookup.html
category: public-records
path:
- public-records
bestFor: Free D-U-N-S Number lookup to confirm a business identity and pull its registered name and address.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- employer-org
- address
- document-id
status: live
pricing: freemium
costNote: The D-U-N-S Number lookup is free (search by company name + country → D-U-N-S, name, address). Full D&B business/credit reports and monitoring are paid.
opsec: passive
opsecNote: Passive — you query Dun & Bradstreet's business database; the company is not notified. The free lookup needs no account; full reports require registration/payment (a trail on your side). Use billing hygiene if buying reports.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Dun & Bradstreet is a major, long-established global business-data provider; the D-U-N-S identifier and core entity data are widely relied upon, though entries can lag corporate changes.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: true
localInstall: false
registration: false
aliases:
- Dun & Bradstreet UK
- DUNS lookup
tags:
- companysites
- Company Related Sites
- duns
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# dnb.co.uk

> Dun & Bradstreet's UK D-U-N-S lookup: confirm a business exists, get its registered name and address, and grab the D-U-N-S number that keys it across global corporate data.

## When to use
You have a company `name`, an `employer-org` linked to your subject, or a business `address`, and want to verify the entity and obtain its D-U-N-S Number — the universal identifier that lets you match the same firm across D&B and other corporate datasets. Useful for confirming a business is real, resolving which of several same-named entities you have, and pulling the registered address in a fraud or asset trace.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.dnb.co.uk/duns-number/lookup.html.
2. Enter the company `name` and select the country; submit.
3. Read the free result: matched business `name`, registered `address`, and the D-U-N-S `document-id`.
4. For directors, financials, credit scores, or corporate-family detail, buy a D&B report (registration/payment).
5. Pivot: the D-U-N-S number keys other D&B/corporate lookups; the address/name feed `[[companycheck-co-uk]]` (UK directors) or `[[info-clipper-com]]` (global).

## Inputs → Outputs
- **In:** company `name`, `employer-org`, or `address` (+ country)
- **Out:** confirmed `employer-org` name, registered `address`, D-U-N-S `document-id`
- **Empty/negative result looks like:** no match — the entity isn't in D&B's database for that country/name, or the name differs from the registered one. Try name variants; absence isn't proof the company doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: **payment-wall-partial** — the lookup is free; directors/financials sit behind paid reports.
- OpSec: **passive** to the target; buying reports needs an account/payment — use hygiene.
- Data can lag corporate changes; treat the D-U-N-S/entity match as a strong lead, then confirm current status at the official register.

## Overlaps ("do both")
- Pairs with `[[companycheck-co-uk]]` (UK Companies House depth) and `[[info-clipper-com]]` (global) — D&B confirms the entity and gives the D-U-N-S key; the others add directors and cross-border structure.

## Trust & verifiability
`trust: trusted` — a major, authoritative business-data provider. The D-U-N-S/entity data is reliable for matching; verify current filings against the official companies register.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dnb-co-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address → employer-org, address, document-id |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |

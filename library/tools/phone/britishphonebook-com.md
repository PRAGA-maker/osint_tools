---
id: britishphonebook-com
name: britishphonebook.com
description: Use when you have a UK name + town (or postcode) and want a listed residential landline number and address from a UK directory-enquiries site.
url: http://www.britishphonebook.com/search.php
category: phone
path:
- phone
bestFor: UK residential directory enquiries — name/town to listed landline number and address.
selectorsIn:
- name
- address
selectorsOut:
- phone
- address
status: live
pricing: free
costNote: Free directory search; ad-supported.
opsec: passive
opsecNote: Reads published UK directory listings; does not contact the subscriber.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Aggregates publicly published UK landline directory data; coverage is limited to listed (non-ex-directory) residential landlines and may be dated.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- britishphonebook.com
tags:
- mobilephone
- Mobile & Phone Related
- uk
- directory
source: uk-osint
lastVerified: '2026-06-13'
enrichment: full
---

# britishphonebook.com

> UK directory-enquiries site — search by surname + town (or postcode) to find a listed residential landline number and address.

## When to use
You have a `name` and an approximate `address`/town (or a postcode) for someone in the UK and want their listed landline `phone` and confirmed `address`. Useful for older/established residents who still hold a listed landline; weak for mobiles and ex-directory numbers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.britishphonebook.com/search.php.
2. Enter surname and city/town (a partial postcode can be entered in the city field).
3. Read the result: matching listed residents with landline `phone` and `address`.
4. Pivot: confirm the address against electoral/people-search tools; use the surname+area to expand to relatives.

## Inputs → Outputs
- **In:** `name`, `address` (town/postcode)
- **Out:** `phone` (listed landline), `address`
- **Empty/negative result looks like:** no listings — common, because most people are ex-directory or mobile-only; absence does not mean the person doesn't live there.

## Gotchas & OpSec
- Only listed residential landlines appear; ex-directory and mobile numbers are absent.
- Data can be stale; cross-check before relying on it.
- UK only.
- OpSec: passive; queries published directory data, no contact with the subject.

## Overlaps ("do both")
- Pairs with UK people-search (`[[192-uk]]`) for electoral/address corroboration and with `[[aql-com]]` to identify the carrier of any number found.

## Trust & verifiability
`trust: community` — aggregates public UK directory listings; reliable for listed landlines but limited in coverage and freshness.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | britishphonebook-com |
| category | phone |
| selectorsIn → selectorsOut | name, address → phone, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

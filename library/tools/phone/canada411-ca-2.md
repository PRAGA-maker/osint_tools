---
id: canada411-ca-2
name: canada411.ca
description: Use when you have a Canadian street address or postal code and want the names and listed phone numbers of people at that location.
url: https://www.canada411.ca/search/address.html
category: phone
path:
- phone
bestFor: Canadian reverse address lookup — address/postal code to residents' names and phone numbers.
selectorsIn:
- address
selectorsOut:
- name
- phone
- associate
status: live
pricing: free
costNote: Free directory search; ad-supported (operated by Yellow Pages Canada).
opsec: passive
opsecNote: Queries published Canadian directory listings; does not contact the residents.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: Canada411 is Canada's main online phone directory, operated by Yellow Pages (YP) Canada, sourcing listings from Bell, Telus, MTS and other carriers.
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- Canada411 address search
- canada411.ca
tags:
- mobilephone
- Mobile & Phone Related
- canada
- reverse-address
source: uk-osint
lastVerified: '2026-06-13'
enrichment: full
---

# canada411.ca (reverse address)

> Canada411's reverse-address search — enter a Canadian street address or postal code to find the people listed there and their phone numbers.

## When to use
You have a Canadian `address` (street + city + province, or a postal code) and want to know who lives/lived there: resident `name`s, listed `phone` numbers, and therefore likely `associate`s/household members of a subject. Strong for confirming an address, finding relatives at a known address, or identifying neighbours.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.canada411.ca/search/address.html.
2. Enter at minimum Street + City + Province, or just a Postal Code. Do not include apartment/suite numbers (the site advises against it). Solve any captcha.
3. Read the result: listed residents (`name`), their phone numbers (`phone`), and co-residents who become `associate` leads.
4. Pivot: take each resident name into the reverse phone search (`[[canada411-ca]]`) or people-search/social tools.

## Inputs → Outputs
- **In:** `address` (street/city/province or postal code)
- **Out:** `name`, `phone`, `associate` (co-residents)
- **Empty/negative result looks like:** "no listings found" — typical for apartments, ex-directory, or mobile-only households; absence ≠ vacant address.

## Gotchas & OpSec
- Human-in-the-loop: occasional captcha.
- Only listed landline subscribers appear; many residents will be missing.
- Canada only.
- OpSec: passive; published-directory query, no contact with residents.

## Overlaps ("do both")
- Pairs with `[[canada411-ca]]` (reverse phone → name/address) — pivot phone↔address to build out the household and contact network.

## Trust & verifiability
`trust: trusted` — authoritative Canadian directory (Yellow Pages Canada); listed-resident results are reliable, coverage limited to listed numbers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canada411-ca-2 |
| category | phone |
| selectorsIn → selectorsOut | address → name, phone, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |

---
id: coloradovoters-info
name: Coloradovoters.info
description: Use when you have a `name` in Colorado and want registered-voter data — returns `address`, approximate `dob`/age, party affiliation, and voting-status history from the public CO voter file.
url: https://coloradovoters.info/
category: public-records
path:
- public-records
bestFor: Free lookup of Colorado's public voter-registration file by name for address, age, and party.
selectorsIn:
- name
- address
selectorsOut:
- address
- dob
- associate
status: live
pricing: freemium
costNote: Free to search Colorado's public voter file; some sites in this niche add paid/enhanced features, but core CO voter lookups are free.
opsec: passive
opsecNote: Reading public voter data is passive and does not notify the subject. Voter data is sensitive PII — handle within your legal/ethical rules. Use a sock-puppet browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Republishes Colorado's official public voter-registration data; accurate to the source but can lag address changes, and it is a third-party site, not the Secretary of State.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- voter-records
- familytreenow
aliases:
- Colorado Voters
- coloradovoters.info
tags:
- voter-records
- colorado
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Coloradovoters.info

> A free front end to Colorado's public voter-registration file — put a name to a current address, age, and party, with other registrants at that address as household leads.

## When to use
You have a Colorado subject's `name` and want their registered `address`, approximate age/`dob`, and party affiliation. Colorado releases a rich public voter file, so this is a strong, current-ish locate source for CO residents; same-address registrants surface likely household members (`associate`).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://coloradovoters.info and search the subject `name` (add city/county to disambiguate).
2. Open the matching record: registered `address`, age (→ `dob` range), party, and registration/voting status.
3. Note other registrants at the same address as candidate household members.
4. Pivot: address feeds reverse-address people-search; co-registrants feed relative/associate lookups; cross-check nationally with `[[voter-records]]`.

## Inputs → Outputs
- **In:** `name` (+ CO city/county), or an `address`
- **Out:** `address`, approximate `dob`/age, party affiliation, same-address `associate`s
- **Empty/negative result looks like:** no record — the person may be unregistered, moved out of state, or registered under a variant name; absence is not conclusive.

## Gotchas & OpSec
- Colorado-only; useless outside CO.
- Voter files lag moves; a listed address may be prior — corroborate currency.
- Sensitive PII — use responsibly and lawfully.
- OpSec: passive; no notification to the subject. Use a sock puppet.

## Overlaps ("do both")
- Pairs with `[[voter-records]]` (multi-state) — use this for authoritative CO detail and that for breadth; feed addresses/relatives into `[[familytreenow]]`.

## Trust & verifiability
`trust: community` — faithful to Colorado's official voter data but a third-party republisher with possible lag. Treat as a strong lead and verify the address's currency against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | coloradovoters-info |
| category | public-records |
| selectorsIn → selectorsOut | name, address → address, dob, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

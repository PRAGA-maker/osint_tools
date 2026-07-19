---
id: unclaimed-property-free-search-officially-endorsed-by-the-states-provinces-and-naupa
name: Unclaimed Property FREE SEARCH (MissingMoney / NAUPA)
description: Use when you have a `name` and want unclaimed-property records — returns a last-known `address`, holder, and sometimes co-owner `associate` links across US states.
url: https://www.missingmoney.com
category: public-records
path:
- public-records
bestFor: Confirming a person's past presence and a last-known address by searching official multi-state unclaimed-property databases by name.
selectorsIn:
- name
- address
selectorsOut:
- address
- associate
status: live
pricing: free
costNote: Free official NAUPA-endorsed multi-state search; claiming property requires ID, but searching is free and open.
opsec: passive
opsecNote: Searching is an anonymous public-records lookup; the subject is not notified. Do NOT attempt to claim property that isn't yours — that crosses from OSINT into fraud.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official unclaimed-property search endorsed by NAUPA and participating US states/provinces; records come from state treasuries, so the name/address data is authoritative.
missingPersonsRelevance: medium
coverage:
- us
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- MissingMoney
- missingmoney.com
- NAUPA unclaimed property
tags:
- property
- unclaimed-property
source: metaosint
lastVerified: '2026-07-19'
enrichment: full
---

# Unclaimed Property FREE SEARCH (MissingMoney / NAUPA)

> The official NAUPA-endorsed unclaimed-property search — a name lookup that surfaces a person's last-known address (as held by state treasuries) and sometimes co-owners.

## When to use
You have a `name` and want to confirm the person existed at a given place and pull a **last-known address**. Unclaimed-property records (forgotten bank balances, refunds, deposits, insurance) are reported by businesses to state treasuries with the owner's last-known name and address — making this a quiet, authoritative way to tie a name to a location, and occasionally to a co-owner or relative listed on the same property.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.missingmoney.com.
2. Enter the `name` (and optionally a state/city) and search across participating states.
3. Read each result: owner name, reported `address`, the holder (bank/employer/company), and any co-owner `associate` listed.
4. Pivot: the last-known address seeds reverse-address and neighbour lookups; the holder (e.g. an employer or bank) is itself a lead; co-owners point to relatives/associates.

## Inputs → Outputs
- **In:** `name` (optionally + state/city)
- **Out:** last-known `address`, reporting holder, and co-owner `associate` names
- **Empty/negative result looks like:** no matches — the person has no reported unclaimed property (common), the name is spelled differently, or their state isn't in MissingMoney (a few states run separate sites). Check individual state unclaimed-property portals as a backup.

## Gotchas & OpSec
- **Not every state participates** in MissingMoney — for a state that runs its own site, search that state's treasury portal directly.
- Addresses are the last one the *holder* had, which may be years old — treat as a historical anchor, not current residence.
- OpSec: passive; but never file a claim on property that isn't yours.

## Overlaps ("do both")
- Pairs with individual state unclaimed-property portals (for non-participating states) and with reverse-address/people-search tools that turn the last-known address into current occupants and neighbours.

## Trust & verifiability
`trust: trusted` — official, NAUPA-endorsed, sourced from state treasuries. The name/address pairing is authoritative for the date it was reported; corroborate currency of the address against a fresher source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | unclaimed-property-free-search-officially-endorsed-by-the-states-provinces-and-naupa |
| category | public-records |
| selectorsIn → selectorsOut | name, address → address, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

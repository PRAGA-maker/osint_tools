---
id: bank-of-canada-unclaimed-balances
name: Bank of Canada Unclaimed Balances
description: Use when you have a `name` and want dormant Canadian bank accounts tied to it — returns account-holder name, last-known address fragment and balance from the official registry.
url: https://www.bankofcanada.ca/unclaimed-balances/
category: search-engines
path:
- search-engines
bestFor: Finding dormant/unclaimed Canadian bank balances registered to a person's name, with a last-known location hint.
selectorsIn:
- name
selectorsOut:
- address
- name
status: live
pricing: free
costNote: Free official Bank of Canada registry; no account or payment to search.
opsec: passive
opsecNote: Anonymous search of a public government registry. No login, nothing written, and the account holder is not notified that you searched. The data is officially published, so lookups are low-risk.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Bank of Canada; entries are the authoritative record of unclaimed balances remitted by federally-regulated banks, so a match is real (though based on the holder's info at the time of dormancy).
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- Unclaimed Balances Registry
- Bank of Canada unclaimed balance search
tags:
- toddington
- curated-directory
- specialty-search
- unclaimed-money
- financial-records
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Bank of Canada Unclaimed Balances

> The official registry of dormant Canadian bank accounts — search a name to find unclaimed balances, often with a last-known location that helps trace a person.

## When to use
You have a `name` with a Canadian connection and want a financial paper trail: dormant accounts (inactive 10+ years) are remitted to the Bank of Canada and published in a searchable registry. A hit confirms the person held an account, gives the last-known city/address fragment the bank had on file, the originating institution, and the balance — a genuinely useful lead for a missing person (last-known location, an institution to approach, evidence they existed at a place/time). It's especially valuable for tracing someone who dropped off the grid years ago.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.bankofcanada.ca/unclaimed-balances/ and go to the search.
2. Enter the person's name (try surname alone, and name variants/maiden names).
3. Read each match: holder name, last-known location, originating bank, balance, and the date it became unclaimed.
4. Use the last-known location and institution as investigative anchors; note the year of dormancy for timeline.
5. Pivot: the last-known `address`/city feeds Canadian people-search and directory lookups; the year narrows a timeline of when contact was lost.

## Inputs → Outputs
- **In:** `name` (Canadian bank account holder)
- **Out:** holder `name`, last-known `address`/city, originating institution, balance, date-unclaimed
- **Empty/negative result looks like:** no matching holder — meaning no dormant *federally-regulated* balance is registered under that name (they may still have active accounts, or accounts at provincial institutions not covered here).

## Gotchas & OpSec
- Human-in-the-loop: none; it's a simple public search.
- The location is the address the bank had *at the time the account went dormant* — potentially decades old; treat as a historical last-known point, not current.
- Only covers federally-regulated banks' balances remitted to the Bank of Canada; provincial credit unions and other unclaimed-property types are elsewhere.
- Common names produce multiple holders — disambiguate by city and institution.

## Overlaps ("do both")
- Pairs with provincial/US unclaimed-property registries and Canadian people-search — this is the federal Canadian bank slice; those cover other jurisdictions and confirm current whereabouts.

## Trust & verifiability
`trust: trusted` — the authoritative Bank of Canada registry; a match is a real remitted balance, with holder data accurate as of the dormancy date.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bank-of-canada-unclaimed-balances |
| category | search-engines |
| selectorsIn → selectorsOut | name → address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

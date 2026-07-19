---
id: bank-of-canada
name: Bank of Canada
description: Use when you have a `name` and want to check Canada's Unclaimed Balances registry (dormant bank accounts) — the Bank of Canada site's one genuinely people-relevant search; otherwise reference/economic info.
url: http://www.bank-banque-canada.ca/
category: search-engines
path:
- search-engines
bestFor: Reaching the Bank of Canada's Unclaimed Balances search (dormant/forgotten Canadian bank accounts) by name — plus authoritative economic/currency reference.
selectorsIn:
- name
selectorsOut:
- address
- document-id
status: live
pricing: free
costNote: Free official central-bank site and free Unclaimed Balances search; no account required.
opsec: passive
opsecNote: Searching a public government registry is passive and touches no target. No sock puppet needed for a routine public-record check.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Canada's central bank; its published data and the Unclaimed Balances registry are authoritative official records.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- Banque du Canada
- Bank of Canada Unclaimed Balances
tags:
- toddington
- curated-directory
- specialty-search
- unclaimed-property
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Bank of Canada

> Canada's central-bank site — mostly economic/currency reference, but it hosts the **Unclaimed Balances** registry, a genuinely useful name-based search for dormant/forgotten Canadian bank accounts.

## When to use
Two cases. (1) The people-relevant one: you have a `name` and want to check the Unclaimed Balances registry — dormant Canadian-dollar bank accounts unclaimed for 10+ years — which lists the holder's name, last-known address hint, and amount; useful for locating people, heirs, or confirming a Canadian banking footprint. (2) Reference: authoritative Canadian economic data, exchange rates, and currency info for background/context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the Bank of Canada site (bankofcanada.ca) and find the **Unclaimed Balances** search.
2. Enter the subject's `name` (try variants/initials); the registry returns matching dormant accounts.
3. Read each match: holder name, partial/last-known location, originating institution, and amount (`document-id`-style balance reference).
4. For non-people use, browse the economic/currency data sections.
5. Pivot: an unclaimed-balance hit gives a `name`+`address` corroboration and a bank link to chase further; the originating institution is a lead.

## Inputs → Outputs
- **In:** `name` (for Unclaimed Balances)
- **Out:** dormant-account records with holder name, location hint (`address`), institution, and balance `document-id`
- **Empty/negative result looks like:** no unclaimed balance under that name — the norm (most people have none). Absence means nothing beyond "no dormant balance recorded." General site content isn't a person search.

## Gotchas & OpSec
- The main site is a central-bank homepage — the only person-search value is the Unclaimed Balances registry; don't expect account or transaction lookups.
- Registry covers only long-dormant CAD accounts; common names collide — corroborate location before concluding identity.
- OpSec: passive public record.

## Overlaps ("do both")
- Pairs with US/other unclaimed-property registries and estate/probate records — each country has its own dormant-asset database; cross-check the relevant one for the subject's jurisdiction.

## Trust & verifiability
`trust: trusted` — an official central-bank source; the Unclaimed Balances registry is an authoritative record, so a match is reliable evidence of a dormant account (identity still needs corroboration for common names).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bank-of-canada |
| category | search-engines |
| selectorsIn → selectorsOut | name → address, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

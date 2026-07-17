---
id: unclaimed-property-administrators
name: Unclaimed Property Administrators (NAUPA / Unclaimed.org)
description: Use when you have a `name` and want to search official US/Canada unclaimed-property databases for money/assets owed to that person — returns confirmations tied to `name` and `address`.
url: https://www.unclaimed.org
category: public-records
path:
- public-records
bestFor: Finding a person via official state unclaimed-property records — a free, authoritative name-to-location signal.
selectorsIn:
- name
selectorsOut:
- name
- address
status: live
pricing: free
costNote: Genuinely free. NAUPA (National Association of Unclaimed Property Administrators) links to every state/province's official program and to MissingMoney.com; searching costs nothing — beware paid "finders" who charge for the same public data.
opsec: passive
opsecNote: You search government databases about a name, not the person, so there is no subject-side footprint. Do not initiate a claim (that requires identity/ownership proof and is not your role) — stop at the existence/location signal.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: NAUPA is the official association of state unclaimed-property administrators; it directs you only to authoritative government programs and the NAUPA-endorsed MissingMoney.com, not to data brokers.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- unclaimed-property-free-search-officially-endorsed-by-the-states-provinces-and-naupa
- unclaimed-and-abandoned-property-search-directory
- unclaimed-money-us-google-search
aliases:
- NAUPA
- Unclaimed.org
- Unclaimed Property Administrators
tags:
- property
- public-records
- unclaimed-property
source: metaosint
lastVerified: '2026-07-17'
enrichment: full
---

# Unclaimed Property Administrators (NAUPA / Unclaimed.org)

> The official gateway to US/Canada state unclaimed-property programs: search a name across government databases for forgotten bank balances, insurance payouts, and refunds — a free, authoritative person-locator signal.

## When to use
You have a `name` and want a cheap, authoritative confirmation that the person exists and is tied to a jurisdiction. States hold unclaimed property (dormant bank accounts, uncashed checks, insurance, deposits, wages) reported against a person's last-known name and address. A hit confirms the name is real, ties it to a state and often a prior `address`, and — because reported records include an address — can corroborate where someone lived. It's a well-known people-search pivot precisely because it's free and government-sourced.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.unclaimed.org and either use the interactive map to reach a specific state/province's official program, or go to the NAUPA-endorsed national search at MissingMoney.com.
2. Search the subject's `name` (try maiden/former names and middle-initial variants); add a state if known.
3. Read the results: each record shows the reported name, a reported city/`address`, the holder (e.g. a bank or employer), and sometimes a range for the amount.
4. Use the reported address and holder as leads — the holder (an employer/bank) is itself a pivot; the address corroborates residence history.
5. Do NOT file a claim — that requires proving identity/ownership and isn't part of an OSINT lookup. Stop at the informational signal.

## Inputs → Outputs
- **In:** `name` (US/Canada)
- **Out:** confirmed `name` matches with reported `address`/city, the holding institution, and amount range
- **Empty/negative result looks like:** no records — the person has no unclaimed property reported (the common case), a different name spelling, or a state not covered; absence says nothing about whether they exist.

## Gotchas & OpSec
- Beware paid finders: only use the official state programs / MissingMoney.com reached via NAUPA — third-party "we'll find your money for a fee" sites resell this free public data.
- Common-name collisions: match on address/holder, not name alone; a bare name hit is a lead, not an identification.
- Coverage/lag: not every state participates in MissingMoney; check the individual state program too, and records lag reporting cycles.
- OpSec: fully passive; never advance an actual claim.

## Overlaps ("do both")
- Pairs with `[[unclaimed-property-free-search-officially-endorsed-by-the-states-provinces-and-naupa]]`, `[[unclaimed-and-abandoned-property-search-directory]]`, and `[[unclaimed-money-us-google-search]]` — run the national NAUPA search and the individual state programs, since not every state feeds the national database.

## Trust & verifiability
`trust: trusted` — NAUPA is the official administrators' association pointing only to government programs; the records are authoritative government data you can cite, distinguishing them sharply from broker sites.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | unclaimed-property-administrators |
| category | public-records |
| selectorsIn → selectorsOut | name → name, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

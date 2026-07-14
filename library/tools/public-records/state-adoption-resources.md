---
id: state-adoption-resources
name: State Adoption Resources
description: Use when a missing-persons/family case involves adoption and you need each US state's rules for accessing (largely sealed) adoption records and reunion registries — returns the lawful pathway to birth-family associate/dob leads.
url: https://www.childwelfare.gov
category: public-records
path:
- public-records
bestFor: Finding each US state's adoption-record access rules and reunion-registry pathways.
selectorsIn:
- name
selectorsOut:
- associate
- dob
- name
status: live
pricing: free
costNote: Free US government resource (Child Welfare Information Gateway, HHS). No account or payment; obtaining actual records may involve state agency fees and eligibility processes.
opsec: passive
opsecNote: Reading the guidance is passive. Actual record access is an overt, identity-verified legal process (you must usually be an eligible party), and reunion registries are consent-based — this is a lawful-request pathway, not covert research.
humanInLoop: true
humanInLoopReason:
- legal-gate
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official US government (HHS Children's Bureau) information portal; authoritative on the law and process, though it holds no personal records itself.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Child Welfare Information Gateway
- childwelfare.gov
tags:
- genealogy
- family
- adoption
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# State Adoption Resources

> The US government's guide to how adoption records work state-by-state — the lawful map for reconnecting adoptees and birth family, where most records are sealed.

## When to use
Your case touches adoption — an adoptee seeking birth family, or a searcher trying to establish a `dob`/birth-family `associate` link — and you need to know what's legally accessible in a given US state: sealed vs. open records, mutual-consent reunion registries, confidential-intermediary programs, and how to request original birth certificates. It's the authoritative process reference, not a record lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to childwelfare.gov (Child Welfare Information Gateway) and find the adoption / access-to-records section for the relevant state.
2. Read that state's rules: whether records are sealed, who is eligible to request them, reunion-registry availability, and intermediary services.
3. Follow the lawful pathway — register with a reunion registry, or file an eligible request with the state agency (identity verification and eligibility apply).
4. Pivot: a successful match or unsealed record yields birth-family `name`/`associate` and `dob`, which feed people-search and vital-records work.

## Inputs → Outputs
- **In:** `name` / case context, plus the relevant US state
- **Out:** the legal pathway and, where eligible/consented, birth-family `associate`, `dob`, `name`
- **Empty/negative result looks like:** records sealed with no eligible pathway, or no consenting party in a mutual-consent registry — meaning the information is legally protected, not that no record exists.

## Gotchas & OpSec
- Adoption records are among the most protected US records: access is gated by eligibility and often mutual consent — this is a legal process, not a scrape.
- childwelfare.gov holds *no* personal data; it tells you the rules and where to go.
- Consider DNA-genealogy avenues in parallel, as they sometimes succeed where sealed records block direct access.

## Overlaps ("do both")
- Complements `[[state-public-records-laws]]` (general FOIA/records procedure) and vital-records/genealogy tools: this covers the adoption-specific legal gate that generic records tools don't.

## Trust & verifiability
`trust: trusted` — an official HHS government portal; authoritative on law and process, and any record you lawfully obtain through it is a primary source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | state-adoption-resources |
| category | public-records |
| selectorsIn → selectorsOut | name → associate, dob, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (legal-gate) |

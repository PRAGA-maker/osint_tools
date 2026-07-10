---
id: voter-records
name: Voter Records
description: Use when you have a US `name` and want registered-voter data — returns `address`, approximate `dob`/age, and political-party affiliation from public voter rolls.
url: https://voterrecords.com/
category: people-search
path:
- people-search
bestFor: Free search of US public voter-registration records by name to get current address, age, and party.
selectorsIn:
- name
- address
selectorsOut:
- address
- dob
- associate
status: live
pricing: free
costNote: Free, ad-supported aggregator of public voter-registration rolls; no account needed. Some links push to paid people-search partners.
opsec: passive
opsecNote: Reading public voter data is passive and does not notify the subject. You disclose the query to the site and its ad/partner network; use a sock-puppet browser. Be mindful that voter data is sensitive PII — handle per your legal/ethical rules.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Aggregates official state voter rolls, but coverage and freshness vary by state (some states restrict or don't release voter data), and records can lag moves; it is a third-party compiler, not the state registrar.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- new-york-state-voter-records
- thatsthem-phone-search
- white-pages
aliases:
- VoterRecords.com
- voter records
tags:
- people-investigations
- voter-records
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Voter Records

> A free aggregator of US public voter-registration rolls — put a name to a current address, approximate age, and political-party affiliation, often with household members.

## When to use
You have a US subject's `name` (ideally plus a state or city) and want their registered `address`, an age/approximate `dob`, and party affiliation. Voter rolls are refreshed for elections, so they can be a relatively current address source, and listings at the same address surface likely household members (`associate`) — useful for locating and network-mapping.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://voterrecords.com and search the subject `name`; add state/city to disambiguate common names.
2. Open the matching record: it shows registered `address`, age (implying `dob` range), party affiliation, and sometimes registration date/precinct.
3. Note other registrants at the same address as candidate household members (`associate`).
4. Ignore paid-partner upsell links unless you specifically need them.
5. Pivot: the address feeds reverse-address people-search; co-registrants feed relative/associate lookups; cross-check against phone/white-pages tools.

## Inputs → Outputs
- **In:** `name` (+ state/city), or an `address` to list registrants there
- **Out:** `address`, approximate `dob`/age, party affiliation, and same-address `associate` links
- **Empty/negative result looks like:** no record — the person may be unregistered, in a state that restricts voter-data release, or registered under a variant name; absence is not conclusive.

## Gotchas & OpSec
- State coverage is uneven: some states withhold or restrict voter data, so gaps reflect law/policy, not the person's absence.
- Records lag address changes; a listed address may be a prior residence — corroborate currency.
- Voter data is sensitive PII; use responsibly and within legal limits for your purpose/jurisdiction.
- OpSec: passive; the subject isn't notified. Use a sock puppet.

## Overlaps ("do both")
- Pairs with `[[new-york-state-voter-records]]` and other state-specific voter sources for authoritative single-state data.
- Feed addresses/associates into `[[thatsthem-phone-search]]` and `[[white-pages]]` to corroborate and expand.

## Trust & verifiability
`trust: community` — sourced from official voter rolls but compiled by a third party with variable freshness and coverage. Treat a hit as a strong lead and verify the address's currency against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | voter-records |
| category | people-search |
| selectorsIn → selectorsOut | name, address → address, dob, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

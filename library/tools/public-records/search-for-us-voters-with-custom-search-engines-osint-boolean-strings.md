---
id: search-for-us-voters-with-custom-search-engines-osint-boolean-strings
name: Search for US Voters with Custom Search Engines (Boolean Strings)
description: Use when you have a US `name` and want registered-voter public records — a Google Custom Search Engine technique over voterrecords.com that returns address, DOB/age, phone and party affiliation.
url: https://booleanstrings.com/2021/07/15/search-for-us-voters-with-custom-search-engines-osint/
category: public-records
path:
- public-records
bestFor: Structured searching of US voter-registration records (name → address, age, party) via a Google Custom Search Engine over voterrecords.com.
selectorsIn:
- name
selectorsOut:
- address
- dob
- phone
- associate
status: live
pricing: free
costNote: "The technique and the underlying voterrecords.com data are free; the author (Irina Shamaeva / Boolean Strings) upsells a paid book and CSE training course, but you do not need those to use the method."
opsec: passive
opsecNote: You are querying Google's index and a public records site, not the subject — no notification reaches them. Run searches from a clean/sock-puppet session as routine hygiene; voter records are public but sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-regarded OSINT/sourcing practitioner's documented method; the technique is sound but depends on voterrecords.com's coverage and on Google indexing, both of which vary by state and change over time.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Boolean Strings voter CSE
- US voter custom search engine
tags:
- public-records
- voter-records
- custom-search-engine
- technique
source: osint4all
lastVerified: '2026-07-15'
enrichment: full
---

# Search for US Voters with Custom Search Engines (Boolean Strings)

> A documented technique — a Google Custom Search Engine over voterrecords.com — that turns a US name into registered-voter details: address, age, party, and sometimes phone.

## When to use
You have a US subject's `name` and want their voter-registration footprint: current/prior `address`, approximate age/`dob`, party affiliation, and household members who register at the same address (`associate` leads). Especially useful for people who are "barely online" — voter records exist even when a subject has no social media. This is a method, not a one-click app: it uses a Google Custom Search Engine (CSE) and Schema.org operators to query the structured fields on voterrecords.com.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read the article (https://booleanstrings.com/2021/07/15/search-for-us-voters-with-custom-search-engines-osint/) and open the linked Google CSE it provides (a CSE scoped to voterrecords.com).
2. Search the subject `name`; narrow with a state or city to cut same-name noise.
3. Refine using the structured operators the article describes (e.g. `more:p:person-email:...`, filters by zip/area code/gender) to target specific fields rather than scrolling raw results.
4. Open the voterrecords.com entries the CSE surfaces to read address history, age, party, and co-registered household members.
5. Corroborate: voter data can be stale or reflect a prior address. Cross-check against another people-search source before relying on any field.
6. Pivot: an address feeds reverse-address and mapping tools; co-registered household members feed a fresh name search; age/DOB narrows records elsewhere.

## Inputs → Outputs
- **In:** `name` (+ optional state/city)
- **Out:** `address` (current/prior), `dob`/age, party affiliation, co-registered `associate`s, sometimes `phone`
- **Empty/negative result looks like:** the CSE returns no voterrecords.com hit — could mean the subject isn't registered, registered in a state voterrecords.com doesn't cover well, or Google hasn't indexed the page. Absence is not proof of non-registration.

## Gotchas & OpSec
- Human-in-the-loop: none — but this is a manual technique; you drive the CSE and interpret results, so expect same-name conflation.
- Coverage varies by state: voterrecords.com does not carry every state equally, and some states restrict voter data.
- OpSec: passive; you touch Google and a public site, never the subject. Use a compartmentalized browser session.
- Ignore the author's course/book upsell — the free CSE and method are the deliverable.

## Overlaps ("do both")
- Pairs with `[[usa-official-com]]` and other US people-search aggregators — voter records anchor address/household from an authoritative-ish public source, while aggregators add phones/emails; each covers the other's gaps.

## Trust & verifiability
`trust: community` — the method comes from an established sourcing practitioner and the underlying data is genuine public voter records, but results depend on voterrecords.com coverage and Google indexing, so verify before treating any field as current.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-for-us-voters-with-custom-search-engines-osint-boolean-strings |
| category | public-records |
| selectorsIn → selectorsOut | name → address, dob, phone, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

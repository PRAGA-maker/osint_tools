---
id: canlii-database
name: CanLII Database
description: Use when you have a `name` and want Canadian court and tribunal records mentioning them — returns associate, address, employer-org, and dob context from published case law.
url: https://www.canlii.org
category: public-records
path:
- public-records
bestFor: Finding a person named in Canadian litigation — parties, witnesses, addresses, and relationships disclosed in published judgments.
selectorsIn:
- name
selectorsOut:
- associate
- address
- employer-org
- dob
status: live
pricing: free
costNote: Free, non-profit public access to Canadian case law and legislation; no account or payment required to search or read.
opsec: passive
opsecNote: Reading published court decisions; parties are not notified. Standard web logging applies to you. Note that publishing/repeating identifying details from a decision may run into publication bans on some cases — read the ban notices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Federation of Law Societies of Canada; the authoritative free source for published Canadian court and tribunal decisions.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- canadian-legal-information-institute
aliases:
- CanLII
- Canadian Legal Information Institute
tags:
- toddington
- curated-directory
- reference-sites
- legal-records
- court-records
source: toddington-resources
lastVerified: '2026-07-20'
enrichment: full
---

# CanLII Database

> The free, authoritative index of Canadian case law and legislation — court and tribunal decisions are a rich, under-used source of names, relationships, and addresses.

## When to use
You have a `name` for someone with a possible Canadian legal footprint — civil suits, family law, bankruptcy, immigration/refugee decisions, criminal appeals, employment tribunals. Court decisions routinely disclose parties' full names, relationships (spouses, business partners, relatives), employers, addresses, and dates, making CanLII a strong pivot for building a network around a subject and for confirming identity/history.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.canlii.org and use the document search (search by party name in quotes).
2. Enter the target `name`; narrow by jurisdiction (province/court) or date if you have leads.
3. Open matching decisions and read the fact recital: parties, `associate` links, `employer-org`, `address`, and dates/`dob` often appear in the narrative.
4. Check each decision for a publication ban before repeating identifying details.
5. Pivot: relatives/partners named feed people-search; an employer or address narrows other public-records queries.

## Inputs → Outputs
- **In:** `name` (+ optional province/court, date)
- **Out:** `associate` (parties/relatives), `address`, `employer-org`, `dob`/dates from case narratives
- **Empty/negative result looks like:** no matching decisions — most people are never party to a *published* case, so absence is expected and not meaningful. Try name variants.

## Gotchas & OpSec
- Only *published* decisions are covered; many settled/lower matters never appear.
- Publication bans and anonymized styles of cause (e.g. initials in family/youth matters) can hide or restrict identities — respect them.
- Common names produce false positives; corroborate with jurisdiction/dates.
- OpSec: passive; you only read public records.

## Overlaps ("do both")
- Pairs with [[canadian-legal-information-institute]] and Canadian corporate/registry search: CanLII gives the litigation narrative, registries give the formal filings behind the same people/companies.

## Trust & verifiability
`trust: trusted` — a Federation of Law Societies non-profit publishing official court/tribunal decisions; text is authoritative, though you must interpret legal context carefully.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canlii-database |
| category | public-records |
| selectorsIn → selectorsOut | name → associate, address, employer-org, dob |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

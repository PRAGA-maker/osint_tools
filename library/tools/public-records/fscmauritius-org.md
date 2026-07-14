---
id: fscmauritius-org
name: FSC Mauritius
description: Use when you have a `name` or `employer-org` linked to Mauritius financial services and want to check the regulator's licensee register — returns employer-org, name, and document-id (licence) leads.
url: https://www.fscmauritius.org/en
category: public-records
path:
- public-records
bestFor: Checking whether a person or company is licensed by Mauritius's financial regulator, and confirming licence status for a Mauritius financial entity.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- name
- document-id
status: live
pricing: free
costNote: Free public regulator site; the licensee register and enforcement notices are freely searchable.
opsec: passive
opsecNote: Searching a regulator's public register does not notify anyone and needs no account. Standard passive browsing hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The Financial Services Commission is Mauritius's official integrated regulator for non-bank financial services; its register and enforcement actions are authoritative.
missingPersonsRelevance: high
coverage:
- mu
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- onlinesearch-mns-mu
- opencorporates
aliases:
- Financial Services Commission Mauritius
- FSC Mauritius register
tags:
- companysites
- Company Related Sites
- regulator
- mauritius
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# FSC Mauritius

> Mauritius's financial-services regulator — the place to confirm whether a person or company is licensed for financial activity in a common offshore jurisdiction, and to find enforcement actions against them.

## When to use
Your investigation involves a Mauritius financial entity or a person claiming to run one — a fund, management company, insurer, or intermediary. You have a `name` or `employer-org` and want to verify it against the FSC's licensee register (is this a real, licensed operator?) and check for enforcement/sanction notices. In fraud, asset-tracing, or due-diligence-flavored missing-persons cases touching Mauritius, this separates legitimate regulated entities from shells.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.fscmauritius.org/en.
2. Use the licensee register / "list of licensees" search for the `employer-org` or `name`.
3. Read the entry: licence type and number (`document-id`), status, and the licensed entity/individual details.
4. Check the enforcement/warnings section for actions, suspensions, or investor alerts naming the party.
5. Pivot: a licensed entity feeds the Mauritius company register `[[onlinesearch-mns-mu]]` for directors/address; an enforcement notice is a strong lead in itself.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** `employer-org` (licensed entity), `name` (licensed individuals/officers), `document-id` (licence number), status & enforcement notices
- **Empty/negative result looks like:** no licence found — the entity is not FSC-regulated (could be unlicensed, or regulated elsewhere/by the Bank of Mauritius for banking). Absence of a licence can itself be a red flag if they claim to be regulated.

## Gotchas & OpSec
- The FSC covers **non-bank** financial services; banks are regulated by the Bank of Mauritius, not here.
- A licence confirms regulation, not integrity — cross-check enforcement notices.
- Fully passive; no login.

## Overlaps ("do both")
- Pairs with `[[onlinesearch-mns-mu]]` (the Mauritius company register — directors, shareholders, address for the same entity) and `[[opencorporates]]`. FSC confirms the regulatory status; the registry gives the people behind it.

## Trust & verifiability
`trust: trusted` — the official Mauritius financial regulator. The register and enforcement notices are authoritative for licensing status.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fscmauritius-org |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, name, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

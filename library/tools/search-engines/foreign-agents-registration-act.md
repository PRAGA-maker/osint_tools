---
id: foreign-agents-registration-act
name: FARA — Foreign Agents Registration Act (DOJ)
description: Use when you have a `name` or `employer-org` and want to check US foreign-agent registrations — returns registrant/principal names, employers and disclosed activities.
url: https://efile.fara.gov/ords/f?p=1235:10
category: search-engines
path:
- search-engines
bestFor: Searching the US DOJ FARA database for individuals/firms registered as agents of foreign principals and the disclosed relationships.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
- associate
status: live
pricing: free
costNote: Free public US Department of Justice database; no account required to search or read filings.
opsec: passive
opsecNote: Searching a public government registry; nothing touches the subject and no login is needed. Passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the US DOJ National Security Division; filings are official, legally required disclosures.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- FARA
- FARA eFile
- Foreign Agents Registration Act
tags:
- toddington
- curated-directory
- specialty-search
- lobbying
- government-registry
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# FARA — Foreign Agents Registration Act (DOJ)

> The US Justice Department's public register of agents acting for foreign principals — search a person or firm to find their foreign-agent registration, who they represent, and the disclosed activities and payments.

## When to use
You have a `name` or `employer-org` and want to know whether they are (or were) a registered US foreign agent — lobbyists, PR firms, consultants, and law firms acting for foreign governments, parties or companies must file here. A hit reveals the registrant, the foreign principal they work for (`associate`/`employer-org`), the nature of the relationship, and disclosed compensation — valuable for due-diligence, network-mapping, and understanding a subject's political/business affiliations.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the FARA eFile search at https://efile.fara.gov/ (Quick Search / registrant and foreign-principal search).
2. Search by registrant `name`/firm or by foreign principal.
3. Open the registration: registrant, foreign principal(s), the described activities, short-form registrants (individuals), and filed documents (contracts, informational materials, disbursement reports).
4. Read the linked documents for named individuals, payments and specific activities.
5. Pivot: foreign principal → other registrants working for it; named individuals → people-search; firm → corporate registries and lobbying disclosures.

## Inputs → Outputs
- **In:** `name` (individual or firm) or `employer-org`/foreign principal
- **Out:** foreign-agent registration — registrant `name`, foreign principal (`employer-org`/`associate`), activities, payments, filed documents
- **Empty/negative result looks like:** no registration — the subject isn't a registered foreign agent (most people aren't; FARA is a narrow niche), or the name is spelled differently in filings; try the firm name and foreign-principal side.

## Gotchas & OpSec
- Narrow scope: only covers those legally required to register as foreign agents — niche in general, but high value when it applies.
- Coverage of enforcement is imperfect — absence isn't proof someone never acted for a foreign principal.
- US-only regime; other countries have separate (or no) registers.
- OpSec: passive, no account, no subject notification.

## Overlaps ("do both")
- Pairs with US lobbying-disclosure (Senate LDA) databases and corporate registries — FARA covers foreign-principal work specifically; those cover domestic lobbying and company structure.

## Trust & verifiability
`trust: trusted` — an authoritative DOJ registry of legally required disclosures; filings are official primary documents you can read and cite directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | foreign-agents-registration-act |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

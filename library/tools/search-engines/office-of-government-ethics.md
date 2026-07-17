---
id: office-of-government-ethics
name: Office of Government Ethics
description: Use when you have the `name` of a senior US executive-branch official and want their public financial disclosures — returns `employer-org`, `associate`, and asset/interest details.
url: https://www.oge.gov/
category: search-engines
path:
- search-engines
bestFor: Retrieving a US federal official's public financial disclosure report, ethics agreements, and divestiture certificates.
selectorsIn:
- name
selectorsOut:
- employer-org
- associate
- address
status: live
pricing: free
costNote: Free US federal government resource; no account or payment. Public financial disclosure documents are released by law.
opsec: passive
opsecNote: Reading public disclosure documents on a .gov site is passive and leaves no trace on the subject. These are legally published records; accessing them is unremarkable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The U.S. Office of Government Ethics is the authoritative federal agency for executive-branch ethics; documents here are official filings, not third-party aggregation.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- white-house-disclosures
aliases:
- OGE
- oge.gov
- US Office of Government Ethics
tags:
- toddington
- specialty-search
- financial-disclosure
- government-records
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Office of Government Ethics

> The US government's authoritative store of executive-branch financial disclosures: look up a senior federal official's assets, income, positions, and ethics agreements.

## When to use
Your subject is a senior US executive-branch official, nominee, or presidential appointee. OGE holds their legally required public financial disclosure reports (OGE Form 278e), ethics agreements, certificates of divestiture, and pledge waivers. These filings expose assets, outside income, prior `employer-org` roles, board seats, spouse/dependent interests (`associate` links), and sometimes real-property holdings — a rich, official corroboration layer for anyone in covered federal roles.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.oge.gov/ and go to the financial disclosure search ("Find an Individual's Ethics Document" / the online disclosure collection).
2. Search the official's `name`; select the individual and the filing year.
3. Read the 278e: reporting individual's positions, assets and income, transactions, liabilities, agreements, and gifts.
4. Note prior employers, board memberships, and family-held interests as pivots.
5. For lower-tier or older records not held centrally, request via the agency; for related datasets, cross-reference other disclosure sources.

## Inputs → Outputs
- **In:** `name` (a covered US federal official/nominee)
- **Out:** `employer-org` (current/prior positions, board seats), `associate` (spouse/business partners via joint interests), asset/income detail, sometimes property `address`
- **Empty/negative result looks like:** no document — the person is not in a covered senior filing category (most federal employees file confidentially, not publicly), or the filing predates the online collection; not proof of no financial interests.

## Gotchas & OpSec
- Coverage is senior filers only: rank-and-file federal employees file confidential 278-T/OGE-450 reports that are NOT public here.
- Point-in-time snapshots: a disclosure reflects the reporting period, not today's holdings.
- Values are reported in broad ranges, not exact figures.
- OpSec: fully passive; these are published public records.

## Overlaps ("do both")
- Pairs with `[[white-house-disclosures]]` — executive-office appointee disclosures overlap and complement OGE's holdings; check both for a complete appointee picture, and add congressional disclosure sources for legislative-branch figures.

## Trust & verifiability
`trust: trusted` — OGE is the official federal ethics authority and these are the filers' own signed legal documents, making them primary-source records you can cite directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | office-of-government-ethics |
| category | search-engines |
| selectorsIn → selectorsOut | name → employer-org, associate, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

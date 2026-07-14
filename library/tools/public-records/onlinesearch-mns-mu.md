---
id: onlinesearch-mns-mu
name: Mauritius CBRD Online Search
description: Use when you have a Mauritius company (`employer-org`) or a director's `name` and want official corporate registry data — returns directors/shareholders (name, associate) and the registered address.
url: https://onlinesearch.mns.mu/
category: public-records
path:
- public-records
bestFor: Looking up Mauritius companies and their directors/shareholders in the official Corporate and Business Registration Department (CBRD) register.
selectorsIn:
- employer-org
- name
selectorsOut:
- name
- associate
- address
- employer-org
status: live
pricing: freemium
costNote: Basic name/company existence search is free; full company file extracts (directors, shareholders, filings) are paid per-document via Mauritius Network Services (MNS).
opsec: passive
opsecNote: A registry lookup does not notify the company or its officers. Ordering paid extracts requires an MNS account and payment, which are logged; use investigative-context details.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official online search for Mauritius's Corporate and Business Registration Department, operated by Mauritius Network Services (the government-appointed e-services operator); authoritative for Mauritius entities.
missingPersonsRelevance: high
coverage:
- mu
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- opencorporates
- disputesregister-org
aliases:
- CBRD Online Search
- Mauritius Network Services company search
- companies.govmu
tags:
- companysites
- Company Related Sites
- corporate-records
- mauritius
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Mauritius CBRD Online Search

> The official online search for Mauritius's Corporate and Business Registration Department — connect a person to a Mauritius company, or a Mauritius company to its directors and address.

## When to use
Your investigation touches Mauritius — a common offshore/corporate jurisdiction. You have an `employer-org` (a Mauritius company name/number) and want its directors, shareholders, and registered address; or you have a `name` and want the Mauritius entities behind them. This is the authoritative government register, reached through Mauritius Network Services.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://onlinesearch.mns.mu/ (redirects to the MNS CBRD online search portal).
2. Run a free search by company name/number or by a person's `name` to confirm existence and status.
3. For details, register an MNS account and order the company file extract — a **paid per-document** purchase.
4. Read the extract: directors and shareholders (`name` / `associate`), shareholdings, registered `address`, incorporation date, and status.
5. Pivot: directors' names feed people-search and PEP/sanctions checks; the registered address feeds geolocation; co-directors feed associate mapping.

## Inputs → Outputs
- **In:** `employer-org` (company) or `name` (director/officer)
- **Out:** `name` (directors), `associate` (shareholders/co-directors), `address` (registered office), `employer-org` linkage, company status
- **Empty/negative result looks like:** no matching entity — the company may be dissolved, a Global Business (GBC) structure with limited public disclosure, or registered elsewhere. Absence isn't proof.

## Gotchas & OpSec
- Free tier confirms existence; the substantive officer/shareholder data is behind a **paid per-document** wall via MNS.
- Mauritius Global Business entities can have limited public disclosure — you may hit privacy structures common to offshore jurisdictions.
- Passive lookup; only the paid-order step exposes account/payment details.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]` (check there first for a free officer index of the same company) and `[[disputesregister-org]]` (registry directory for cross-border cases). Use free indices first; buy the official extract when you need the authoritative document.

## Trust & verifiability
`trust: trusted` — the official Mauritius CBRD register via the government's appointed e-services operator. Authoritative; just note free-tier data is minimal and full records are paid.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onlinesearch-mns-mu |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → name, associate, address, employer-org |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |

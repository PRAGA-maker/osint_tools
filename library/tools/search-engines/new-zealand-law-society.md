---
id: new-zealand-law-society
name: New Zealand Law Society
description: Use when you have a name and want to confirm a New Zealand lawyer — returns employer-org (firm), practising status, and location from the official register of lawyers.
url: https://www.lawsociety.org.nz/for-the-community/search-register-of-lawyers
category: search-engines
path:
- search-engines
bestFor: Verifying a New Zealand lawyer's practising status, firm, and location via the official Law Society register.
selectorsIn:
- name
- geolocation
selectorsOut:
- employer-org
- name
status: live
pricing: free
costNote: Free official register search from the New Zealand Law Society; no account required.
opsec: passive
opsecNote: Reads a public professional register; the lawyer is not notified. Standard web logging only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official New Zealand Law Society register of lawyers; authoritative for NZ practising status.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- NZ Law Society register
- Register of Lawyers New Zealand
- lawsociety.org.nz
tags:
- public-records
- lawyers
- new-zealand
- professional-register
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# New Zealand Law Society

> The official register of lawyers in New Zealand — confirm a person is a practising lawyer, find their firm and location, and check their practising status.

## When to use
You have a `name` and want to confirm the subject is a New Zealand lawyer, or to locate/identify the right lawyer by area and practice type. The register returns the lawyer's firm (`employer-org`), region, and practising status — useful for verifying a claimed profession, disambiguating a common name to a specific practitioner and firm, and confirming someone is genuinely authorised to practise.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.lawsociety.org.nz/for-the-community/search-register-of-lawyers.
2. Search by lawyer name; refine with location (region) and practice area filters.
3. Read the result: the lawyer's name, firm/organisation, region, and practising status.
4. Pivot: the firm (`employer-org`) and region anchor identity for cross-referencing the firm's website, court records, and news; a name absent from the register contradicts a claim to be a practising NZ lawyer.

## Inputs → Outputs
- **In:** `name` (optionally narrowed by `geolocation`/region and practice area)
- **Out:** `employer-org` (firm), `name` (verified lawyer), plus region and practising status
- **Empty/negative result looks like:** no match — the person isn't a currently-registered NZ lawyer (retired, struck off, never admitted, or practising in another country), or the name differs.

## Gotchas & OpSec
- Human-in-the-loop: none; open public search.
- OpSec: passive — the lawyer isn't notified.
- Scope: New Zealand practising lawyers only; other jurisdictions have their own bar/law-society registers. The Society provides a helpline for concerns about returned results.

## Overlaps ("do both")
- Pairs with other bar/law-society registers and court-record databases — this confirms the NZ credential and firm, court records show the cases and conduct behind the name.

## Trust & verifiability
`trust: trusted` — it is the official NZ Law Society register; practising status and firm are authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | new-zealand-law-society |
| category | search-engines |
| selectorsIn → selectorsOut | name, geolocation → employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

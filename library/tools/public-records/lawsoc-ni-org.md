---
id: lawsoc-ni-org
name: Law Society of Northern Ireland — Find a Solicitor
description: Use when you have a `name` or firm and want to confirm a Northern Ireland solicitor — returns the solicitor's firm, office address and professional status from the official regulator directory.
url: https://lawsoc-ni.org/using-a-solicitor/find-a-solicitor
category: public-records
path:
- public-records
bestFor: Verifying that a person is a practising solicitor in Northern Ireland and finding their firm and office address.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- name
status: live
pricing: free
costNote: Free official regulator directory; no account or payment.
opsec: passive
opsecNote: A public professional register — searching does not notify the solicitor. It returns professional/work details (firm, office), not personal data. Requests hit the Law Society server; use a sock-puppet browser if you'd rather not log searches against your IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Law Society of Northern Ireland, the statutory professional body for NI solicitors; authoritative for who is a currently-recognised solicitor and their practising firm.
missingPersonsRelevance: medium
coverage:
- gb-nir
auth: none
api: false
localInstall: false
registration: false
aliases:
- Law Society of Northern Ireland
- Find a Solicitor NI
- lawsoc-ni.org
tags:
- professionlicensing
- Profession & Licensing Sites
- solicitor
- professional-register
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Law Society of Northern Ireland — Find a Solicitor

> The official NI solicitor register — confirm someone practises law in Northern Ireland and pin down their firm and office address.

## When to use
You have a `name` (or a firm) and want to confirm the person is a practising solicitor in Northern Ireland, or find which firm and office a known solicitor works at. Useful for verifying a professional identity/credential a subject claims, locating a person via their practice, or tying an individual to an `employer-org` (law firm) and its address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://lawsoc-ni.org/using-a-solicitor/find-a-solicitor.
2. Search by solicitor `name` and/or firm name / location.
3. Read the result: the solicitor's firm (`employer-org`), office `address` and contact details, and that they are a recognised practitioner.
4. Note the firm to place the person geographically and professionally.
5. Pivot: the firm/office address gives a physical location and phone; the firm name feeds Companies House and news searches; confirmed professional status corroborates identity.

## Inputs → Outputs
- **In:** `name` and/or `employer-org` (firm)
- **Out:** firm (`employer-org`), office `address`/contact, confirmed solicitor `name`/status
- **Empty/negative result looks like:** no match — the person isn't a currently-registered NI solicitor (they may be a barrister, practise in a different UK/Irish jurisdiction, be retired/struck-off, or the name differs). Absence rules out only current NI solicitor status.

## Gotchas & OpSec
- NI solicitors only — barristers (Bar of NI) and solicitors in England/Wales, Scotland or the Republic are on separate registers.
- Returns professional/office data, not home addresses.
- A struck-off or retired practitioner may not appear — absence isn't proof they never practised.

## Overlaps ("do both")
- Pairs with the SRA (England/Wales), Law Society of Scotland, Law Society of Ireland and the Bar registers — use the right jurisdiction's regulator; each authoritatively covers its own practitioners.

## Trust & verifiability
`trust: trusted` — the statutory regulator's own register; authoritative for current NI solicitor status and practising firm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lawsoc-ni-org |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: lawsociety-org-uk
name: Law Society Find a Solicitor (England & Wales)
description: Use when you have a `name` or firm and want to confirm a solicitor's registration and workplace in England & Wales — returns the solicitor's status, firm/employer, and office address.
url: https://solicitors.lawsociety.org.uk/
category: public-records
path:
- public-records
bestFor: Confirming a person is a registered solicitor in England & Wales and locating their firm/office.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- name
- employer-org
- address
status: live
pricing: free
costNote: Free public directory operated by the Law Society; no account or payment required.
opsec: passive
opsecNote: Public register lookup — the solicitor is not notified. Anonymous; standard browsing hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Law Society "Find a Solicitor" register, drawing on SRA regulatory data — the authoritative source for solicitor registration in England & Wales.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- Find a Solicitor
- solicitors.lawsociety.org.uk
tags:
- professionlicensing
- Profession & Licensing Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Law Society Find a Solicitor (England & Wales)

> The official register of solicitors in England & Wales — confirms whether a person is a practising solicitor and ties them to a firm and office address.

## When to use
You have a `name` (or firm/`employer-org`) and want to confirm someone is a registered solicitor and where they practise. Useful for corroborating a stated profession, linking a person to a law firm, or getting a verifiable business `address` in a missing-person or identity workup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://solicitors.lawsociety.org.uk/ and search by person `name`, firm, or location.
2. Filter by area of law or region to disambiguate common names.
3. Read the result: the solicitor's name, regulatory status, the firm/`employer-org` they work at, and the office `address`/contact.
4. Cross-check the SRA register for the underlying regulatory record and any disciplinary history.
5. Pivot: the firm and office address feed company/records lookups and give a real contact route.

## Inputs → Outputs
- **In:** `name`, firm/`employer-org`, or location
- **Out:** solicitor `name`, status, firm/`employer-org`, office `address`
- **Empty/negative result looks like:** no match — the person isn't a currently registered solicitor in England & Wales (they may be in Scotland/NI, non-practising, or not a solicitor at all); absence is scope-limited, not proof.

## Gotchas & OpSec
- Jurisdiction: England & Wales only — Scotland (Law Society of Scotland) and Northern Ireland have separate registers.
- Directory vs regulator: this is the Law Society directory; the SRA holds the formal regulatory/disciplinary record — check both.
- OpSec: passive; the lookup is invisible to the subject.

## Overlaps ("do both")
- Pairs with Companies House and `[[gov-im]]`/`[[jerseyfsc-org]]` when the solicitor is also a company officer — the register confirms the profession, corporate records add the business footprint.

## Trust & verifiability
`trust: trusted` — the official Law Society register backed by SRA data; a match is authoritative confirmation of solicitor status in the jurisdiction.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lawsociety-org-uk |
| category | public-records |
| selectorsIn → selectorsOut | name → name, employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

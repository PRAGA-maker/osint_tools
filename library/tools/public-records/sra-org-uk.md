---
id: sra-org-uk
name: SRA Solicitors Register
description: Use when you have a `name` or firm and want to verify a solicitor in England & Wales — returns regulatory status, practising history and firm/employer details.
url: https://www.sra.org.uk/consumers/register/
category: public-records
path:
- public-records
bestFor: Confirming whether someone is (or was) a regulated solicitor in England & Wales and pulling their firm, roll number and regulatory history.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- name
- metadata-exif
status: live
pricing: free
costNote: Free public register operated by the Solicitors Regulation Authority; no account needed.
opsec: passive
opsecNote: Querying a public professional register is passive; the individual is not notified. Data is professional (firm, status), not home-life detail — use it to verify identity/employment, not for intrusive purposes.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official regulator's register for solicitors in England & Wales; authoritative for whether a person is entitled to practise and their regulatory record.
missingPersonsRelevance: medium
coverage:
- gb-eng
- gb-wls
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- '192'
aliases:
- Solicitors Regulation Authority
- SRA register
- sra.org.uk
tags:
- professionlicensing
- profession-licensing
- solicitors
- uk
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# SRA Solicitors Register

> The Solicitors Regulation Authority's public register — confirm whether a person is a regulated solicitor in England & Wales, and read their firm, roll number and regulatory status.

## When to use
You have a `name` (or a law-firm `employer-org`) and want to verify a claim to be a solicitor, place someone at a firm, or spot regulatory sanctions. A hit confirms professional identity and current/previous employer (the firm and office address), plus admission date and whether they hold a practising certificate — useful for identity verification and employment leads, and for exposing false claims of being a solicitor.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.sra.org.uk/consumers/register/ and search by individual `name` or by organisation/firm.
2. Open the record: SRA/roll number, admission date, current status (e.g. practising, not practising), and the regulated firm(s) with office address.
3. Check for any regulatory decisions/sanctions noted against the person or firm.
4. Use the firm and address to corroborate employment/location.
5. Pivot: the firm (`employer-org`) and office `address` feed company and people-search; a confirmed identity anchors other records. Place the person's home via `[[192]]`.

## Inputs → Outputs
- **In:** `name` or `employer-org` (law firm)
- **Out:** `employer-org` (firm), office `address`, confirmed `name`/roll number, and `metadata-exif` (status, admission date, sanctions)
- **Empty/negative result looks like:** no match — the person isn't an SRA-regulated solicitor (they may be a barrister — see the Bar register — a paralegal, or in Scotland/NI under different regulators); absence disproves only the solicitor claim.

## Gotchas & OpSec
- **Solicitors in England & Wales only** — barristers (BSB), Scotland (Law Society of Scotland) and NI are separate registers.
- It's professional data (firm/status), not personal contact detail; don't over-read.
- OpSec: passive public-register lookup.

## Overlaps ("do both")
- Pairs with `[[192]]` and company registries — SRA confirms the professional identity/firm; those attach home address and corporate ties. Do both to connect professional and personal footprints.

## Trust & verifiability
`trust: trusted` — authoritative regulator data; definitive for practising status, with the caveat that it only covers SRA-regulated solicitors.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sra-org-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, name, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>

---
id: lawscot-org-uk
name: lawscot.org.uk
description: Use when you have a `name` and want to verify/locate a Scottish solicitor — returns their practising status, firm (`employer-org`) and office `address` from the Law Society of Scotland's Find a Solicitor directory.
url: https://www.lawscot.org.uk/find-a-solicitor/
category: public-records
path:
- public-records
bestFor: Confirming a Scottish solicitor's registration and finding their firm and office location.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
- address
status: live
pricing: free
costNote: Free public directory from the Law Society of Scotland. No account or payment.
opsec: passive
opsecNote: You search a public professional directory; the solicitor is not contacted or notified. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Law Society of Scotland, the statutory professional body for Scottish solicitors — authoritative for who holds a current practising certificate.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- sra-org-uk
aliases:
- Law Society of Scotland Find a Solicitor
- lawscot.org.uk
tags:
- professionlicensing
- Profession & Licensing Sites
- solicitor
- scotland
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# lawscot.org.uk

> The Law Society of Scotland's "Find a Solicitor" directory — confirm a person is a registered Scottish solicitor and find the firm and office they work from.

## When to use
You have a `name` claimed to be a Scottish solicitor (or an `employer-org`/firm to enumerate) and want to verify it and locate them professionally. The directory confirms current practising status and lists the solicitor's firm (`employer-org`) and its office `address`, plus areas of practice. Useful for confirming a legal-professional claim, locating a solicitor through their firm when a personal address is unknown, and mapping who works at a given firm.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.lawscot.org.uk/find-a-solicitor/.
2. Search by solicitor `name`, firm/`employer-org`, location, or practice area.
3. Open the matching entry: name, firm, office `address`/contact, and practice areas.
4. Confirm the person holds a current practising status (the directory lists registered solicitors).
5. Pivot: the firm/office `address` narrows `geolocation`; the firm can be enumerated for `associate`s/colleagues; for England & Wales solicitors use the SRA equivalent (`[[sra-org-uk]]`).

## Inputs → Outputs
- **In:** `name` (or `employer-org`/firm, location, practice area)
- **Out:** solicitor `name`, firm `employer-org`, office `address`/contact, practice areas
- **Empty/negative result looks like:** no match — the person isn't a currently listed Scottish solicitor under that name (a variant, a non-practising/removed solicitor, or an England & Wales solicitor who'd appear on the SRA register instead).

## Gotchas & OpSec
- Human-in-the-loop: none; a directory lookup.
- OpSec: **passive** — a public professional directory; nobody is notified.
- Scotland-specific: solicitors elsewhere in the UK are on other registers (SRA for England & Wales). The directory reflects current listings, so a removed/struck-off solicitor may simply not appear.

## Overlaps ("do both")
- Pairs with `[[sra-org-uk]]` (England & Wales solicitors) — when a UK legal professional's jurisdiction is unclear, check both. lawscot is authoritative for Scotland.

## Trust & verifiability
`trust: trusted` — the statutory professional body's own directory, so listing implies current registration. Confirm the specific individual (common names) via firm and location details before relying on a match.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lawscot-org-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: cilexgroup-org-uk
name: cilexgroup.org.uk
description: Use when you have a `name` claimed to be a UK chartered legal executive (CILEX) and want to verify membership — returns membership status, grade and practising details from the official CILEX directory.
url: https://cilexportal.cilexgroup.org.uk/CILEx-Directory
category: public-records
path:
- public-records
bestFor: Verifying whether a person is a CILEX member/legal executive and their grade/status.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- document-id
status: live
pricing: free
costNote: Free official membership directory; no account to search.
opsec: passive
opsecNote: Read-only search of a professional-body directory; the member is not notified. Use a clean session for hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by CILEX (Chartered Institute of Legal Executives), the professional body — the authoritative source for CILEX membership status.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- nmc-uk-org
aliases:
- CILEx Directory
- Chartered Institute of Legal Executives
tags:
- professionlicensing
- Profession & Licensing Sites
- legal-register
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# cilexgroup.org.uk

> The CILEX membership directory — the authoritative check on whether someone is a chartered legal executive and their standing.

## When to use
You have a `name` for someone who claims (or is claimed) to be a UK legal executive / CILEX member, and you want to verify it: membership status, grade (e.g. Chartered Legal Executive, Paralegal), and any practising/firm detail. Confirms a professional identity and often the firm (`employer-org`), or disproves a false claim. As the professional body's own directory, it is authoritative for CILEX membership.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cilexportal.cilexgroup.org.uk/CILEx-Directory.
2. Search by `name` (or membership number if known).
3. Read the result: member `name`, grade/status, membership number (`document-id`), and any listed firm/practice (`employer-org`).
4. Use the grade to gauge seniority and the firm to place them; a membership number is a unique anchor.
5. Pivot: the firm feeds corporate/LinkedIn checks; a confirmed profession corroborates identity.

## Inputs → Outputs
- **In:** `name` (or CILEX membership number)
- **Out:** `name`, grade/status, membership number (`document-id`), firm/practice (`employer-org`)
- **Empty/negative result looks like:** no match — the person isn't a listed CILEX member, or the name differs. A non-match disproves a current CILEX-member claim (they might still be a solicitor/barrister — check the SRA/BSB registers instead).

## Gotchas & OpSec
- Covers CILEX (legal executives) only — solicitors and barristers are on the SRA and BSB registers respectively; check those for other legal roles.
- Members can opt out of directory listing, so absence isn't absolute proof.
- OpSec: **passive** — a professional-directory read.

## Overlaps ("do both")
- Pairs with `[[nmc-uk-org]]` and other professional registers — each confirms a claimed profession in its field; for other legal roles use the SRA (solicitors) and BSB (barristers) registers.

## Trust & verifiability
`trust: trusted` — first-party CILEX data; authoritative for CILEX membership, though members may opt out of public listing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cilexgroup-org-uk |
| category | public-records |
| selectorsIn → selectorsOut | name → name, employer-org, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

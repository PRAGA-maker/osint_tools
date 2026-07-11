---
id: ifa-org-uk
name: ifa.org.uk (Institute of Financial Accountants)
description: Use when you have an accountant's `name` and want to verify UK IFA membership/practising status — returns employer-org and address of the practice via the "Find an Accountant" directory.
url: https://www.ifa.org.uk/
category: public-records
path:
- public-records
bestFor: Verifying whether someone is a member of the Institute of Financial Accountants and locating their practice via the public "Find an Accountant" directory.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- address
- name
status: live
pricing: free
costNote: Free public "Find an Accountant" directory search; no account needed to verify membership or find a practising member.
opsec: passive
opsecNote: A professional-body directory lookup — searching does not notify the member and reveals only your IP to the IFA. Fully passive; use a sock-puppet browser only if the wider investigation is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party professional body (Institute of Financial Accountants, part of IPA Group); the membership directory is an authoritative statement of who it certifies.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- fca-org-uk
- companies-house
aliases:
- IFA
- Institute of Financial Accountants
- ifa.org.uk find an accountant
tags:
- professionlicensing
- Profession & Licensing Sites
- regulator-register
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# ifa.org.uk (Institute of Financial Accountants)

> The IFA's public "Find an Accountant" directory — verify whether a person is a certified financial accountant and locate their practice.

## When to use
You have a `name` for someone who claims to be an accountant/financial professional in the UK and you want to confirm the credential and find their practice. The IFA is a recognized professional body; its member directory corroborates an occupation claim, ties the person to a firm (`employer-org`), and gives a business `address` — useful for verifying identity, employment, or a professional footprint in a trace.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.ifa.org.uk/ and go to "Find an Accountant".
2. Search by the member's name or by location/firm.
3. Read the listing: the member's name, membership grade (which reflects their standing), their firm (`employer-org`), and the practice `address`/contact.
4. Absence from the directory means either not an IFA member or a non-practising/opted-out member — it does not confirm they lack accountancy credentials (they may belong to another body: ICAEW, ACCA, AAT, CIMA).
5. Pivot: the firm name/address feeds [[companies-house]] and property/records lookups; a mutual/financial entity they run feeds [[fca-org-uk]].

## Inputs → Outputs
- **In:** accountant's `name` (or firm/location)
- **Out:** membership/grade confirmation, firm (`employer-org`), practice `address`
- **Empty/negative result looks like:** no directory entry — not IFA-certified, non-practising, or a member of a different accountancy body; check ICAEW/ACCA/AAT before concluding they're not an accountant.

## Gotchas & OpSec
- The IFA is one of several UK accountancy bodies — a genuine accountant may be certified elsewhere and absent here; don't treat a non-match as "not an accountant."
- The public directory typically lists *practising* members offering services; salaried/non-practising members may not appear.
- OpSec: passive — a professional-body lookup notifies no one.

## Overlaps ("do both")
- Pairs with [[companies-house]] (the firm and the person's directorships) and [[fca-org-uk]] (if they run a regulated mutual/financial entity) — the IFA directory confirms the professional credential those don't.

## Trust & verifiability
`trust: trusted` — first-party professional body. A directory entry is an authoritative statement that the IFA certifies the person; verify the *scope* of the credential against other bodies if it matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ifa-org-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

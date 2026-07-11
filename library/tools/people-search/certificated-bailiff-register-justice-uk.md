---
id: certificated-bailiff-register-justice-uk
name: Certificated Bailiff Register – Justice UK
description: Use when you have a `name` of someone claiming to be an enforcement agent (bailiff) in England & Wales and want to verify them — returns whether they hold a valid certificate, their employer, and the certifying court.
url: https://certificatedbailiffs.justice.gov.uk
category: people-search
path:
- people-search
bestFor: Verifying that a purported bailiff/enforcement agent is genuinely certificated, and identifying their employer and issuing court.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
status: live
pricing: free
costNote: Free official government register; no account required.
opsec: passive
opsecNote: Read-only search of an official register; it does not notify the individual. Passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official GOV.UK / Ministry of Justice register of certificated enforcement agents (Crown copyright, Open Government Licence).
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- Certificated Enforcement Agent Register
- certificatedbailiffs.justice.gov.uk
tags:
- people-search
- professionlicensing
- uk
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Certificated Bailiff Register – Justice UK

> The official England & Wales register of certificated enforcement agents: is this person really a bailiff, and who certified them?

## When to use
Someone presents as a bailiff/enforcement agent and you have their `name` (or the firm's name). This register confirms whether they hold a valid court certificate to use the Taking Control of Goods procedure — a targeted verification, not a general people search. It's most useful for debunking bogus-bailiff scams and for tying an individual to an employer and a specific certifying court.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://certificatedbailiffs.justice.gov.uk.
2. Search by the enforcement agent's `name` or `employer-org`; tick the option to include similar spellings.
3. Read the result: a match confirms a valid certificate and shows the associated employer and the court that issued it.
4. If no match, use the register's guidance to email the relevant court (cbregister@justice.gov.uk) to verify.
5. Pivot: the employer (`employer-org`) feeds a company-register lookup; the issuing court frames where to seek further records.

## Inputs → Outputs
- **In:** `name` (or `employer-org`)
- **Out:** certificate validity (yes/no), agent `name`, `employer-org`, and certifying court
- **Empty/negative result looks like:** no listing — meaning no valid certificate under that spelling. Given the "similar spellings" option, a genuine absence is a strong signal the person is NOT a certificated bailiff (a common scam tell).

## Gotchas & OpSec
- Narrow scope: England & Wales certificated enforcement agents only — not Scotland (sheriff officers) or general people search, and it won't return DOB/contact details.
- Use the similar-spellings toggle before concluding someone is absent.
- OpSec: **passive**, official, read-only.

## Overlaps ("do both")
- Pairs with `[[companies-house]]`/company registers — verify the agent here, then check their firm's registration and officers to build the fuller picture.

## Trust & verifiability
`trust: trusted` — a first-party UK government register, so a match (or confirmed absence) is authoritative for certification status.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | certificated-bailiff-register-justice-uk |
| category | people-search |
| selectorsIn → selectorsOut | name → name, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: imiregister-org-uk
name: IMI Professional Register
description: Use when you have a `name` and think the subject is a UK automotive professional, and want to verify their accreditation and workplace — returns `name`, `employer-org`, `address` (place of work).
url: https://tide.theimi.org.uk/membership/professional-register
category: public-records
path:
- public-records
bestFor: Verifying a UK motor-industry professional's IMI accreditation and finding their place of work.
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
costNote: Free public register search; no account or payment.
opsec: passive
opsecNote: Public professional register; searching hits the IMI site, not the subject, and requires no login. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Institute of the Motor Industry (IMI), the UK professional body for the automotive sector — an authoritative accreditation source.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Institute of the Motor Industry register
- theimi.org.uk professional register
tags:
- professionlicensing
- Profession & Licensing Sites
- automotive
- accreditation
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# IMI Professional Register

> The Institute of the Motor Industry's public register of accredited UK automotive professionals — a place-of-work and credential lookup for anyone in the motor trade.

## When to use
You have a `name` and reason to believe the subject works in the UK automotive industry (technician, MOT tester, engineer, assessor), and you want to confirm their professional accreditation and, crucially for locating them, their **place of work**. The register ties a named individual to a business and location, which can narrow a subject's whereabouts and corroborate employment claims.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the register (https://tide.theimi.org.uk/membership/professional-register; may resolve to www.theimi.org.uk).
2. Search by member name or number, business name, or location (country, town/postcode, with a distance radius) and subsector.
3. Read results: individual's name, post-nominals (FIMI, MIMI, CAE, AAE, etc.), place of work, and location.
4. Use the post-nominals to gauge seniority/role and the place of work as an `employer-org` + `address` pivot.
5. Pivot: confirm the workplace against the business's own site and Companies House; feed the name into other UK records.

## Inputs → Outputs
- **In:** `name` (or `employer-org` / `address` to browse by area)
- **Out:** `name`, credentials/post-nominals, `employer-org` (place of work), `address`/location
- **Empty/negative result looks like:** no match — the subject isn't IMI-accredited (many motor-trade workers aren't), works under a different name, or has lapsed membership; absence doesn't disprove employment in the sector.

## Gotchas & OpSec
- Only covers **accredited IMI members**, a subset of everyone working in UK automotive — a blank result is common and not conclusive.
- "Place of work" is a business address, not a home address.
- UK-only scope.

## Overlaps ("do both")
- Pairs with Companies House and general people-search — the register confirms the professional accreditation and workplace, those add ownership/registration and residential leads.

## Trust & verifiability
`trust: trusted` — an official professional-body register, so an accreditation match is authoritative; still confirm the current workplace against a second source, as job locations change.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | imiregister-org-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address → name, employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

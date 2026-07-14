---
id: directaccessportal-co-uk
name: directaccessportal.co.uk
description: Use when you have a barrister's `name` (or need to identify one in England & Wales) and want their chambers, practice areas and contact route — returns a public professional profile.
url: https://www.directaccessportal.co.uk/
category: public-records
path:
- public-records
bestFor: Confirming a barrister in England & Wales is real and Public-Access qualified, plus their chambers and specialisms.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- name
- address
status: live
pricing: free
costNote: Free public directory operated by the Bar Council; no account needed to search or view profiles.
opsec: passive
opsecNote: Passive — you are reading a public professional directory, and searches are not attributed to you. Submitting an enquiry through the portal, however, sends your details to the barrister/chambers, so stop at the profile view for pure OSINT.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Bar Council of England & Wales; entries are self-listed by Public Access-qualified barristers, so it is authoritative for the fact of qualification but marketing-style for the profile text.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- barristers-register-bsb
aliases:
- Direct Access Portal
- Bar Council direct access
tags:
- professionlicensing
- Profession & Licensing Sites
- legal
- barristers
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# directaccessportal.co.uk

> The Bar Council's public directory of Public Access-qualified barristers in England & Wales — a way to verify a barrister and locate their chambers.

## When to use
You have a `name` that is claimed to be a barrister, or you need to identify/verify a legal professional in England & Wales. This portal lists barristers who are qualified to take instructions directly from the public (no solicitor intermediary), so it both confirms the person is a genuine, practising barrister and surfaces their chambers, practice areas and the contact route. Useful for vetting professional claims and for locating someone through their professional affiliation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.directaccessportal.co.uk/.
2. Search by barrister `name`, by chambers, by location, or by area of law.
3. Open the matching profile — read the barrister's name, chambers (`employer-org`), location, call date and listed specialisms.
4. Note that a listing here means Public Access-qualified; absence does *not* mean the person isn't a barrister (many barristers work solicitor-referral only and won't appear).
5. Pivot: the chambers name/address feeds a location, and the verified full name feeds the official BSB Barristers' Register for regulatory status.

## Inputs → Outputs
- **In:** `name` (or `employer-org` / chambers, or practice area)
- **Out:** `name`, `employer-org` (chambers), `address` (chambers location), practice areas
- **Empty/negative result looks like:** no matching profile — meaning the person isn't listed as Public Access-qualified here, which is not the same as "not a barrister." Cross-check the BSB register before concluding.

## Gotchas & OpSec
- Coverage is limited to Public Access barristers; the broader profession is on the regulator's register, not here.
- Profile prose is self-authored marketing — treat specialism claims as self-reported.
- Fully passive to browse; do not use the "make an enquiry" flow for OSINT, as it transmits your identity to the barrister.

## Overlaps ("do both")
- Pairs with `[[barristers-register-bsb]]` — the Bar Standards Board register is the authoritative regulatory record (practising status, disciplinary findings), while this portal adds direct-access qualification and richer contact/specialism detail.

## Trust & verifiability
`trust: trusted` — run by the Bar Council. The existence and direct-access qualification of a listed barrister is authoritative; the descriptive text is self-supplied, so verify regulatory standing against the BSB register.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | directaccessportal-co-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, name, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

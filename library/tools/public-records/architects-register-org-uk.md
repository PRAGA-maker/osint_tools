---
id: architects-register-org-uk
name: ARB Architects Register (UK)
description: Use when you have a `name` and think the subject is a UK-registered architect — returns their ARB registration record: registration `document-id`, practice (`employer-org`) and `address`.
url: http://architects-register.org.uk/
category: public-records
path:
- public-records
bestFor: Confirming a person is a UK-registered architect and reading their registration number, practice and location.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- name
- address
- employer-org
- document-id
status: live
pricing: free
costNote: Free public statutory register operated by the Architects Registration Board; no account or payment.
opsec: passive
opsecNote: A read-only search of an official register — the subject is not notified. The site sees your IP/query; a sock-puppet browser suffices for a sensitive name.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The ARB is the UK's statutory regulator for architects; only registered persons may legally use the title "architect", so a match is authoritative.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- eca-co-uk
aliases:
- Architects Registration Board register
- ARB register
- architects-register.org.uk
tags:
- professionlicensing
- Profession & Licensing Sites
- uk
- regulator
- architect
source: uk-osint
lastVerified: '2026-07-13'
enrichment: full
---

# ARB Architects Register (UK)

> The UK's statutory register of architects — a definitive check on whether a named person is legally registered, plus their registration number, practice and location.

## When to use
You have a `name` (optionally an `address`/area or practice `employer-org`) and want to confirm the subject is a UK-registered architect. Because only ARB-registered individuals may lawfully call themselves "architect", this both verifies a claimed profession and, via the listed practice and location, helps place a person geographically and professionally.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://architects-register.org.uk/ and choose "Search the Register".
2. Search by forename/surname, or by registration number, company name, address, or postcode radius (advanced search adds website/email).
3. Open a result's "View" for the full record: registration `document-id`, practice name (`employer-org`), and `address`/county.
4. Disambiguate a common name using the practice and location.
5. Pivot: the practice + address feed Companies House and business searches; a confirmed registration corroborates a claimed identity/career.

## Inputs → Outputs
- **In:** `name` (or registration number / company / address)
- **Out:** confirmed `name`, registration `document-id`, practice `employer-org`, `address`/county
- **Empty/negative result looks like:** no match — the person is not currently ARB-registered (never registered, lapsed, or removed), or is an architectural professional in a role that doesn't require registration. The site occasionally shows "searching is not currently working, try again" — retry rather than treating that as a negative.

## Gotchas & OpSec
- UK-only and title-specific: architectural technologists, technicians and unregistered designers won't appear.
- A lapsed/removed registration may not surface as "current"; note the status shown.
- OpSec: fully passive; a routine public-register lookup.

## Overlaps ("do both")
- Pairs with `[[eca-co-uk]]` and other UK profession registers — do both when pinning down which regulated body a subject belongs to, and with Companies House to tie the practice to a legal entity.

## Trust & verifiability
`trust: trusted` — first-party statutory regulator; a match (or clean non-match) is authoritative for ARB registration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | architects-register-org-uk |

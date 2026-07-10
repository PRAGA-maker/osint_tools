---
id: bizportal-gov-za
name: BizPortal (CIPC South Africa)
description: Use when you have a person's `name` or a company (`employer-org`) in South Africa and want to confirm company registration, status and directors — returns employer-org, name and co-director associate links.
url: https://bizportal.gov.za/default.aspx
category: public-records
path:
- public-records
bestFor: Confirming South African company registration details, status (active/deregistered) and director listings via the official CIPC portal.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- name
- associate
status: live
pricing: free
costNote: Company lookups (BizProfile) are free, but you must create/log in to a BizPortal account first (required under South Africa's POPIA privacy law). Registering a new company is a paid service (~R125–R175); searching existing records is free.
opsec: passive
opsecNote: You are querying the official CIPC registry, not the subject, so nothing is disclosed to the person of interest. However, BizPortal now requires a logged-in account to search, so your registered identity is recorded by CIPC — use a dedicated research account rather than a personal one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official portal of the Companies and Intellectual Property Commission (CIPC), the South African government company registrar; data is authoritative first-party registry data.
missingPersonsRelevance: high
coverage:
- za
auth: account
api: false
localInstall: false
registration: true
aliases:
- BizPortal
- CIPC BizProfile
- CIPC company search
tags:
- companysites
- Company Related Sites
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# BizPortal (CIPC South Africa)

> The South African government's official company portal (CIPC) — confirm whether a company is registered, its status, and who its directors are, tying a person to businesses they run.

## When to use
You have a South African `name` you suspect is a company director, or an `employer-org` you want to verify, and you need authoritative registry facts: is the company real and active or deregistered, when was it registered, and who are its directors? Director listings are the OSINT payoff — they link an individual to companies and to co-directors (`associate`), corroborating identity, business ties and sometimes an address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to BizPortal (https://www.bizportal.gov.za/) and log in — an account is now mandatory to search, per POPIA.
2. Open **BizProfile** and search by company `name` or registration number.
3. Read the profile: registration status (active/in business/deregistered), registration date, enterprise type, and the list of directors (`employer-org`, `associate`).
4. Cross-reference a director's name against other companies to build a business network.
5. Pivot: co-directors become new `name` leads; a company name feeds further corporate/tax/domain checks; deregistration dates anchor a timeline.

## Inputs → Outputs
- **In:** company `name`/registration number (or a person's `name` to check as a director where searchable)
- **Out:** `employer-org` (company, status, dates), `name` (directors), `associate` (co-directors)
- **Empty/negative result looks like:** "no records found" for the company name — meaning it isn't CIPC-registered under that name; note that BizPortal keys on the company, so finding a person usually means starting from a known company.

## Gotchas & OpSec
- **Login wall:** as of recent POPIA compliance changes you cannot search without an account; the classic anonymous CIPC entity search at `eservices.cipc.co.za` is an alternative but has its own login/fee model.
- BizProfile is company-centric — you generally confirm a director rather than search all companies for a person by name.
- OpSec: passive toward the subject, but your search account is logged by CIPC.

## Overlaps ("do both")
- Pairs with the CIPC eServices entity search and general company-registry aggregators — run both, since BizPortal gives the official record while aggregators may index directors more searchably.

## Trust & verifiability
`trust: trusted` — first-party South African government registrar (CIPC); the registration and director data is authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bizportal-gov-za |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, name, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |

---
id: e-gov-kw
name: e.gov.kw
description: Use when you have a Kuwaiti Civil ID or a `name` and want to check official Kuwait government status records (Civil ID validity, arrest warrants, travel bans, residency) — returns document-id and address/status confirmations.
url: https://e.gov.kw/sites/kgoenglish/Pages/HomePage.aspx
category: public-records
path:
- public-records
bestFor: Kuwait's official e-government portal for Civil ID, arrest-warrant, travel-ban and residency status inquiries.
selectorsIn:
- name
- document-id
selectorsOut:
- document-id
- address
- name
status: live
pricing: free
costNote: Government portal; the inquiry services are free, though many require the subject's own Civil ID / PACI login and are meant for self-service.
opsec: active
opsecNote: Queries hit a Kuwaiti government system and several services require authenticating as the subject (Civil ID + PIN / PACI login). Do not attempt to log in as a person you are investigating — that is impersonation. Restrict use to the open status-inquiry pages that take only a Civil ID number, and treat access as logged by the state.
humanInLoop: true
humanInLoopReason:
- account-login
- legal-gate
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the State of Kuwait (Kuwait Government Online / KGO); the records are authoritative first-party government data.
missingPersonsRelevance: high
coverage:
- kw
auth: account
api: false
localInstall: false
registration: false
relatedTools:
- moci-gov-kw
aliases:
- Kuwait Government Online
- KGO portal
tags:
- companysites
- Company Related Sites
- government
- kuwait
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# e.gov.kw

> Kuwait's official single-window e-government portal — the authoritative place to check a Civil ID's status, arrest warrants, travel bans and residency for people and businesses inside Kuwait.

## When to use
You are working a Kuwait-linked subject and have a `name` or, ideally, a Kuwaiti Civil ID number, and you want to corroborate official status: is the Civil ID valid, is there an arrest warrant or travel ban, has residency expired, are there traffic violations. It also fronts business-registration and government-service search, so it doubles as an `employer-org`/company entry point for Kuwait.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://e.gov.kw and switch to the English portal (KGO).
2. Use the main service search to reach the relevant inquiry: "Inquiring for Civil ID Status," "Inquiring about Arrest Warrants," residence-expiry / travel-ban checks, or traffic-violation queries.
3. For open status pages, enter the subject's Civil ID number (a `document-id`) and submit.
4. Read the returned status: Civil ID valid/expired, warrant present/absent, travel-ban flag, residency dates. Many deeper services instead demand a Civil ID + PIN or PACI login — stop there rather than authenticating as the subject.
5. Pivot: a confirmed Civil ID and address feed other Kuwait/GCC records; a company hit feeds [[moci-gov-kw]].

## Inputs → Outputs
- **In:** Kuwaiti Civil ID (`document-id`) for status pages; `name` for the service/company search
- **Out:** Civil ID validity, warrant/travel-ban/residency status, associated `address`/`name` confirmations
- **Empty/negative result looks like:** "no record" or an invalid-Civil-ID error — meaning the number is wrong or the person isn't in that system, not proof of clean status across all registries.

## Gotchas & OpSec
- Human-in-the-loop: most high-value services are gated behind a Civil ID PIN or PACI login intended for the record-holder; do NOT log in as your subject (impersonation, and a legal line).
- OpSec: **active** — you are touching a state system that logs access; use only the open inquiry pages and expect Arabic-first UI on many sub-pages (use the English portal or translate).
- Coverage is Kuwait-only; a "no record" here says nothing about other GCC states.

## Overlaps ("do both")
- Pairs with [[moci-gov-kw]] — the Ministry of Commerce & Industry portal covers company/commercial-registry detail while e.gov.kw covers the person-level Civil ID and status records, so run both when a Kuwait subject links to a business.

## Trust & verifiability
`trust: trusted` — it is the State of Kuwait's own government portal, so the status records are authoritative; the limitation is access (login gates), not data quality.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | e-gov-kw |
| category | public-records |
| selectorsIn → selectorsOut | name, document-id → document-id, address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login, legal-gate) |

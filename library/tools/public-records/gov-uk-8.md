---
id: gov-uk-8
name: SIA Register of Licence Holders
description: Use when you have a `name` or SIA licence number and want to confirm a person holds a valid UK private-security licence — returns licence validity, holder name, and sector.
url: https://services.sia.homeoffice.gov.uk/rolh
category: public-records
path:
- public-records
bestFor: Verifying whether a person holds a valid UK Security Industry Authority (door supervisor, security guard, CCTV, etc.) licence.
selectorsIn:
- name
- document-id
selectorsOut:
- name
- document-id
- employer-org
status: live
pricing: free
costNote: Free official UK government register (Security Industry Authority / Home Office); no account required.
opsec: passive
opsecNote: Public licence-status lookup; anonymous and server-side, with no notification to the licence holder. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Security Industry Authority (a UK Home Office body); the statutory register of private-security licence holders.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- SIA ROLH
- Security Industry Authority register
- check an SIA licence
tags:
- professionlicensing
- Profession & Licensing Sites
- uk
- security
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# SIA Register of Licence Holders

> The UK Security Industry Authority's public register: confirm whether a person holds a valid private-security licence (door supervisor, security guard, CCTV operator, close protection).

## When to use
You have a subject's `name` or an SIA licence number (`document-id`) and want to verify a claimed security role, or to move from a licence number to a name. A hit confirms the person is a real, currently-licensed security operative and identifies the licence sector — corroborating occupation and identity, and narrowing the person to the UK. Because you can search by name, it also helps disambiguate common names within the licensed-security population.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://services.sia.homeoffice.gov.uk/rolh (redirects to the SIA ROLH service).
2. Search by the holder's `name` or by SIA licence number (`document-id`).
3. Read the result: whether a valid licence exists, the holder's name, licence sector/type, and status/expiry.
4. Pivot: a confirmed name + security sector feeds people-search and employer checks; a licence number ties records together across contexts.

## Inputs → Outputs
- **In:** `name` or `document-id` (SIA licence number)
- **Out:** licence validity/status, holder `name`, licence sector (`employer-org`/role context), `document-id`
- **Empty/negative result looks like:** no matching licence — the person may not work in a licensable security role, may hold a lapsed/revoked licence, or the name may be spelled differently.

## Gotchas & OpSec
- Covers UK SIA-regulated roles only; not all "security" jobs require a licence, so absence doesn't disprove security work.
- It confirms licence status, not a home address — a verification tool, not a locator.
- OpSec: passive; the holder is not notified.

## Overlaps ("do both")
- Pairs with `[[tfl-gov-uk-2]]` and other UK licence registers, and with Companies House for any employing security firm — do both to move from "is this licensed" to "who employs them and where".

## Trust & verifiability
`trust: trusted` — first-party data from the Security Industry Authority, the UK statutory regulator.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gov-uk-8 |
| category | public-records |
| selectorsIn → selectorsOut | name, document-id → name, document-id, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

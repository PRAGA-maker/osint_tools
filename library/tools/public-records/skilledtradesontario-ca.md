---
id: skilledtradesontario-ca
name: Skilled Trades Ontario Public Register
description: Use when you have a `name` and want to verify whether a person holds a valid Ontario skilled-trades certification/registration — returns certification status and trade details.
url: https://www.skilledtradesontario.ca/public-register/
category: public-records
path:
- public-records
bestFor: Verifying whether a named person is a certified/registered tradesperson or apprentice in a compulsory trade in Ontario.
selectorsIn:
- name
- document-id
selectorsOut:
- name
- document-id
- employer-org
status: live
pricing: free
costNote: Free official Ontario government register; no account required.
opsec: passive
opsecNote: Public certification-register lookup; anonymous and server-side, with no notification to the tradesperson. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Skilled Trades Ontario, the provincial Crown agency responsible for trade certification.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- Skilled Trades Ontario register
- Ontario trades public register
tags:
- professionlicensing
- Profession & Licensing Sites
- canada
- ontario
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Skilled Trades Ontario Public Register

> Ontario's official trades register: confirm whether a named person is a certified tradesperson or apprentice authorized to work in a compulsory trade.

## When to use
You have a subject's `name` (or their Skilled Trades Ontario ID) and want to verify a claimed trade — electrician, plumber, automotive technician, etc. A hit confirms the person is a real, currently authorized tradesperson in Ontario and identifies their trade, which corroborates identity and occupation and can narrow location to the province. Because you can search by partial name, it also helps disambiguate common names within a trade.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.skilledtradesontario.ca/public-register/.
2. Enter all or part of the person's first or last `name`, or a Skilled Trades Ontario ID/Account Number (`document-id`).
3. Read the result: whether the person is legally authorized to perform a compulsory trade, plus trade/certification details.
4. Pivot: a confirmed trade + name narrows people-search and can be cross-referenced with employer records or trade-union/association listings (`employer-org`).

## Inputs → Outputs
- **In:** `name` (full or partial) or `document-id` (STO ID/account number)
- **Out:** certification/authorization status, trade, confirmed `name`, `document-id`, associated `employer-org` where shown
- **Empty/negative result looks like:** no match — the person may work only in a non-compulsory (voluntary) trade not requiring registration, be certified in another province, or use a different name spelling.

## Gotchas & OpSec
- The register centres on **compulsory** trades; voluntary-trade workers may not appear even if genuinely skilled.
- Coverage is Ontario only — other provinces have their own apprenticeship/certification bodies.
- OpSec: passive; no notification to the tradesperson.

## Overlaps ("do both")
- Do both with other provincial/national licensing registers and with employer/LinkedIn lookups — this confirms certification while those place the person at a workplace.

## Trust & verifiability
`trust: trusted` — first-party data from Skilled Trades Ontario, the provincial certification authority.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | skilledtradesontario-ca |
| category | public-records |
| selectorsIn → selectorsOut | name, document-id → name, document-id, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

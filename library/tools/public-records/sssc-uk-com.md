---
id: sssc-uk-com
name: SSSC Register (Scottish Social Services Council)
description: Use when you have a `name` and think the subject works in Scottish social care — returns their `employer-org`-linked registration record: registration number, role/part of register, status and any conditions.
url: https://www.sssc.uk.com/search-the-register/
category: public-records
path:
- public-records
bestFor: Confirming that a named person is a registered Scottish social care worker and reading their registration category, status and conditions.
selectorsIn:
- name
selectorsOut:
- employer-org
- name
- document-id
status: live
pricing: free
costNote: Free public statutory register; no account or payment.
opsec: passive
opsecNote: A read-only search of an official register — the subject is not notified. The SSSC site sees your IP/query; use a sock-puppet browser for a sensitive name. Do not attempt to file or amend a registration.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The SSSC is the statutory regulator for Scotland's social service workforce; its register is the authoritative, official source for who is registered.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Scottish Social Services Council register
- sssc.uk.com
tags:
- professionlicensing
- Profession & Licensing Sites
- scotland
- regulator
- social-care
source: uk-osint
lastVerified: '2026-07-13'
enrichment: full
---

# SSSC Register (Scottish Social Services Council)

> The statutory public register of Scotland's social service workforce — an authoritative yes/no on whether a named person is a registered care worker, plus their role and standing.

## When to use
You have a `name` and evidence or suspicion that the subject works in Scottish social care — care home staff, social workers, day-care and childminding workers, residential childcare. The register confirms registration, the part/category they are registered under (which implies their role), their registration status, and any conditions or removals recorded against them.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.sssc.uk.com/search-the-register/.
2. Search by the subject's name (a registration number, if you have one, narrows exact matches).
3. Read the matched record: registration number, the part of the register (role type), registration status (registered / lapsed / removed), and any conditions.
4. Disambiguate common names using the role type and any partial location/employer cues.
5. Pivot: the role/part of register corroborates a claimed occupation; a removal or condition is a notable lead; the confirmed employment sector narrows further employer/records searches.

## Inputs → Outputs
- **In:** `name` (or registration number)
- **Out:** registration record — role/part of register (`employer-org`-adjacent), registration `document-id` (number), status/conditions, confirmed `name`
- **Empty/negative result looks like:** no match — the person is not (or no longer) SSSC-registered, works in social care in a non-registered role, or works in another UK nation with its own regulator (e.g. Social Work England, Social Care Wales).

## Gotchas & OpSec
- Scotland-only: an English or Welsh care worker will not appear here — check the corresponding national regulator instead.
- The register lists the regulated role, not a home address; do not over-read it as a locator.
- OpSec: fully passive; a routine public-register lookup with no notification to the subject.

## Overlaps ("do both")
- Pairs with other UK profession/licensing registers — do both when you are pinning down which regulated body a subject belongs to, since each nation and profession maintains its own list.

## Trust & verifiability
`trust: trusted` — a first-party statutory regulator; a match (or clean non-match) is authoritative for SSSC registration specifically.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sssc-uk-com |

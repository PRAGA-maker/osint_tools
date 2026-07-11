---
id: government-electronic-directory-services-canada
name: Government Electronic Directory Services (GEDS) — Canada
description: Use when you have a `name` and think the person is a Canadian federal public servant — returns their title, department, work phone/email and organisational chain (manager/team).
url: http://sage-geds.tpsgc-pwgsc.gc.ca/en/GEDS
category: people-search
path:
- people-search
bestFor: Confirming and locating a Canadian federal employee — title, department, work contact details and reporting structure.
selectorsIn:
- name
selectorsOut:
- employer-org
- phone
- email
- associate
status: live
pricing: free
costNote: Free official Government of Canada directory; no account or payment.
opsec: passive
opsecNote: A public federal directory — searching does not notify the employee. It exposes work contact details, not home/personal data. Requests hit a Government of Canada server; use a sock-puppet browser if you'd rather not log searches against your IP, and handle contact data within your legal basis.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Government of Canada (PSPC); authoritative for federal public-service employees who are listed. Coverage is federal departments/agencies only, and some staff/roles may be omitted.
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: true
localInstall: false
registration: false
aliases:
- GEDS
- Government Electronic Directory Services
- geds-sage.gc.ca
tags:
- toddington
- curated-directory
- people-search
- government-employees
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# Government Electronic Directory Services (GEDS) — Canada

> The Government of Canada's official staff directory — the authoritative way to confirm a person is a federal public servant and pull their department, work contact details and team.

## When to use
You have a `name` and reason to think the subject works for the Canadian federal government. GEDS confirms employment and returns title, department/branch, work phone and email, and the organisational chain (their unit, sometimes manager/colleagues). Strong for confirming a person is alive and employed, locating them at a work address, and mapping workplace `associate`s.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://geds-sage.gc.ca/en/GEDS (the current GEDS URL; the older sage-geds address redirects).
2. Search by `name` (try surname; add given name / department to disambiguate).
3. Open the matching entry: title, department, work `phone`/`email`, office location, and organisation tree.
4. Browse the org unit to find colleagues/managers as `associate` leads.
5. Pivot: the work email/phone corroborates identity and enables (careful, lawful) contact; the department/title feeds LinkedIn and news searches; colleagues expand the network.

## Inputs → Outputs
- **In:** `name`
- **Out:** `employer-org` (department/branch), work `phone`, work `email`, colleagues/managers as `associate`
- **Empty/negative result looks like:** no match — the person isn't a federal employee, works for a Crown corporation or a provincial/municipal government (not in GEDS), is unlisted, or the name is spelled differently. Absence rules out only *listed federal* employment.

## Gotchas & OpSec
- Federal only: provincial/municipal staff, Crown corporations and many security/enforcement roles are not listed.
- Some employees opt out or are omitted; a miss isn't proof they don't work in government.
- Returns WORK contact data only — never home addresses; don't over-read it.

## Overlaps ("do both")
- Pairs with LinkedIn, `[[pibuzz]]`-style salary databases and provincial directories — GEDS authoritatively confirms federal employment and work contacts, while those add pay, private-sector and sub-national coverage it lacks.

## Trust & verifiability
`trust: trusted` — first-party Government of Canada data; authoritative for listed federal employees, bounded only by opt-outs and its federal-only scope.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | government-electronic-directory-services-canada |
| category | people-search |
| selectorsIn → selectorsOut | name → employer-org, phone, email, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

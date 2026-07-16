---
id: myewc-wales-2
name: myewc.wales (Education Workforce Council register)
description: Use when you have a `name` of a Welsh education practitioner and want registration status or disciplinary orders — returns employer-org context and document-id of any order.
url: https://www.myewc.wales/en/member-of-public/current-expired-disc-orders
category: public-records
path:
- public-records
bestFor: Checking whether a teacher/education worker in Wales is registered and whether they carry a current or expired disciplinary order.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- name
- document-id
status: live
pricing: free
costNote: Free public access to the Education Workforce Council register and disciplinary-orders list; no account required for the public search.
opsec: passive
opsecNote: Official regulator's public register — searching it does not notify the practitioner and reveals nothing about you beyond your IP to the EWC. Standard passive lookup; use a sock-puppet browser only if the wider case is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party regulator — the Education Workforce Council (EWC, formerly GTCW) is the statutory body for the education workforce in Wales; the register is authoritative.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- gov-uk-14
- myewc-wales
aliases:
- Education Workforce Council
- EWC Wales register
- GTCW register
tags:
- professionlicensing
- Profession & Licensing Sites
- regulator-register
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# myewc.wales (Education Workforce Council register)

> The statutory register of Wales's education workforce — confirms whether a named practitioner is registered and surfaces any disciplinary order against them.

## When to use
You have a `name` for someone who works (or claims to work) in education in Wales — teacher, learning-support worker, FE/work-based-learning practitioner, youth worker — and you want to confirm their professional registration and check for disciplinary history. Useful for verifying an occupation claim, corroborating an employer, or surfacing a documented disciplinary event that may be relevant to a background trace.

## How to use it (`bestInteractionPattern`: web-manual)
1. For disciplinary orders, open https://www.myewc.wales/en/member-of-public/current-expired-disc-orders and browse/search the current & expired orders list.
2. For registration status, use the public "search the register" function on myewc.wales and enter the practitioner's name.
3. Read the result: registration category/status (which corroborates their `employer-org`/role), and, if present, the disciplinary order with its reference (`document-id`) and outcome.
4. Pivot: a confirmed registration category corroborates an occupation; a disciplinary order's details (dates, restriction) feed the broader timeline. Cross-check other UK regulator registers for parallel professions.

## Inputs → Outputs
- **In:** `name` (practitioner)
- **Out:** registration status/category (role/`employer-org` context), disciplinary order reference (`document-id`) and outcome where applicable
- **Empty/negative result looks like:** no register entry — the person may not be (or no longer be) a registered Welsh education practitioner, or works in a different UK nation with its own regulator; absence isn't proof they never taught.

## Gotchas & OpSec
- Scope is **Wales only** — England (Teaching Regulation Agency), Scotland (GTCS), and NI use separate registers; check the right nation.
- The disciplinary list covers EWC orders only; historical or minor matters may not appear.
- OpSec: passive — an official public register; searching leaves no trace to the subject.

## Overlaps ("do both")
- Pairs with other UK public-record and regulator lookups (e.g. [[gov-uk-14]] for property/official records) — use this specifically to nail down the education-profession dimension in Wales.

## Trust & verifiability
`trust: trusted` — first-party statutory regulator (EWC). The register and disciplinary orders are authoritative; a hit is a verified regulatory fact, not an inference.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | myewc-wales-2 |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, name, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: gtcs-org-uk
name: gtcs.org.uk
description: Use when you have a `name` claimed to be a Scottish teacher and want to verify registration — returns registration status, number and qualifications from the official GTC Scotland register.
url: https://www.gtcs.org.uk/search-the-register/
category: public-records
path:
- public-records
bestFor: Verifying whether a person is a registered teacher in Scotland and their registration status.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- employer-org
status: live
pricing: free
costNote: Free official register search; no account.
opsec: passive
opsecNote: Read-only search of the statutory public teaching register; the registrant is not notified. Use a clean session for hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the General Teaching Council for Scotland (GTC Scotland), the statutory regulator — the authoritative source for Scottish teacher registration.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- nmc-uk-org
- cilexgroup-org-uk
aliases:
- GTC Scotland
- General Teaching Council for Scotland
tags:
- professionlicensing
- Profession & Licensing Sites
- teaching-register
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# gtcs.org.uk

> The GTC Scotland register search — the authoritative check on whether someone is a registered teacher in Scotland.

## When to use
You have a `name` for someone who claims (or is claimed) to be a teacher in Scotland, and you want to verify it: registration status, registration number (`document-id`), and registration category/qualifications. Confirms a professional identity, or disproves a false teaching claim. As the statutory regulator's register, it is authoritative for Scottish teachers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.gtcs.org.uk/search-the-register/.
2. Search by `name` (or registration number if known).
3. Read the result: registrant `name`, registration number (`document-id`), status (registered/removed/lapsed), and registration category (e.g. primary/secondary subject).
4. Use the registration number as a unique anchor and the category to characterise them.
5. Pivot: a confirmed profession corroborates identity; a "removed" status is itself a lead; the school/authority context feeds further checks.

## Inputs → Outputs
- **In:** `name` (or GTCS registration number)
- **Out:** `name`, registration number (`document-id`), status, registration category (`employer-org` context)
- **Empty/negative result looks like:** no match — the person isn't a registered Scottish teacher, or the name differs. Teachers in England/Wales/NI are on separate registers — check those instead.

## Gotchas & OpSec
- Covers **Scotland** only — England/Wales/NI teaching registration is handled by different bodies.
- Removed/lapsed entries may show with that status — read carefully.
- OpSec: **passive** — a statutory public-register read.

## Overlaps ("do both")
- Pairs with `[[nmc-uk-org]]` (nurses/midwives) and `[[cilexgroup-org-uk]]` (legal executives) — each verifies a claimed profession in its own field/jurisdiction.

## Trust & verifiability
`trust: trusted` — first-party GTC Scotland data; authoritative for Scottish teacher registration status.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gtcs-org-uk |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

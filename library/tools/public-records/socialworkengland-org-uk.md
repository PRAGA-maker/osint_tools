---
id: socialworkengland-org-uk
name: Social Work England — Register Search
description: Use when you have a `name` (or registration number) and want to confirm someone is a registered social worker in England and their practising status — returns town, registration document-id, employer/status context.
url: https://www.socialworkengland.org.uk/umbraco/surface/searchregister/results
category: public-records
path:
- public-records
bestFor: Verifying a person is a registered social worker in England and reading their register status, town and any conditions.
selectorsIn:
- name
- document-id
selectorsOut:
- name
- address
- document-id
- employer-org
status: live
pricing: free
costNote: Free public statutory register search; no account or payment.
opsec: passive
opsecNote: A public regulator register; searching is passive and the subject is not notified. No login required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Social Work England is the statutory regulator for social workers in England; the register is an authoritative, real-time first-party government/regulatory source.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Social Work England register
- SWE register search
tags:
- professionlicensing
- professional-register
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Social Work England — Register Search

> The statutory public register of social workers in England — confirm a person really is a registered social worker, in which town, and whether their registration is current or restricted.

## When to use
You have a `name` (or a Social Work England registration number) and need to verify a claimed social-work identity/employment, confirm current practising status, or locate the general town a registered social worker practises in. Useful for identity corroboration and for narrowing a person's location/profession in England.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the register search at https://www.socialworkengland.org.uk/ (Search the Register).
2. Search by first name, last name, town, or — quickest and most precise — the registration number (format like `SW#####`).
3. Read the result card: name, registration number, town, current status, any conditions, and renewal due date. The register updates in real time.
4. Pivot: a confirmed registration number + town corroborates identity and narrows location; combine with employer directories and general people-search.

## Inputs → Outputs
- **In:** `name` (with optional town) or registration `document-id` (`SW#####`)
- **Out:** confirmed `name`, town (`address`-level), registration `document-id`, practising status/conditions (`employer-org` context: they work as a social worker)
- **Empty/negative result looks like:** no matching entry — means the person is not on the England social-work register (they may be registered in Scotland/Wales/NI under a different regulator, or not a social worker at all). Common names can return multiple entries — disambiguate by town/registration number.

## Gotchas & OpSec
- England only: Scotland (SSSC), Wales (Social Care Wales) and Northern Ireland (NISCC) maintain separate registers — a no-hit here doesn't cover them.
- The register gives town, not a full address — treat it as a location narrowing, not a home address.
- OpSec: passive, authoritative regulator data; no subject notification.

## Overlaps ("do both")
- Pairs with other UK professional registers (GMC for doctors, SRA for solicitors, NMC for nurses) — pick the regulator matching the claimed profession to verify it.

## Trust & verifiability
`trust: trusted` — first-party statutory regulator; the register is the authoritative source of who is a registered social worker in England, updated in real time.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | socialworkengland-org-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, document-id → name, address, document-id, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

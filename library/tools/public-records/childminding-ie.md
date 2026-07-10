---
id: childminding-ie
name: childminding.ie
description: Use when you have an Irish county/`address` (or a childminder's `name`) and want to find registered childminders in that area — returns childminder listings with area and contact via Childminding Ireland's directory.
url: http://www.childminding.ie/childminders/find-a-childminder/
category: public-records
path:
- public-records
bestFor: Locating registered childminders by county in Ireland, or checking whether a named person is listed as one.
selectorsIn:
- name
- address
selectorsOut:
- name
- address
- employer-org
status: live
pricing: free
costNote: Free directory from Childminding Ireland (a support/membership body); access requires verifying an email address first.
opsec: passive
opsecNote: A directory lookup that doesn't contact the childminder directly. However, access is gated behind email verification, so use a sock-puppet email — the operator can associate the account with your searches.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Childminding Ireland is the national childminding membership/support organisation; the directory reflects its members, not a statutory register, so it is not an exhaustive record of all childminders.
missingPersonsRelevance: high
coverage:
- ie
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
relatedTools:
- ama-assn-org
aliases:
- Childminding Ireland
- Find a Childminder Ireland
tags:
- professionlicensing
- Profession & Licensing Sites
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# childminding.ie

> Childminding Ireland's "find a childminder" directory — a county-based lookup of member childminders across the Republic of Ireland.

## When to use
You have an Irish county or `address` and want registered childminders in that area, or you have a `name` and want to check whether that person is listed as a childminder with Childminding Ireland. Useful for confirming a subject's stated occupation/location, or for building a picture of caregivers connected to a household. Note it lists the organisation's members, not a statutory register, so it is not exhaustive.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.childminding.ie/childminders/find-a-childminder/.
2. Verify an email address (use a **sock-puppet** email) — access to the directory is gated behind an email-confirmation link.
3. Search by county (`address`) and browse listings; look for a specific `name` where the interface allows.
4. Read the results: childminder listings showing name, service area, and contact/enrolment status (`employer-org` in the sense of their registered childminding service).
5. Pivot: a confirmed name/area feeds Irish public-records and people-search; a service name feeds business-register checks.

## Inputs → Outputs
- **In:** county/`address` (or a `name` to confirm)
- **Out:** `name`, `address` (service area), `employer-org` (childminding service), contact details
- **Empty/negative result looks like:** no listings for the county, or the named person absent — meaning they're not a Childminding Ireland member (they may still childmind independently). Absence is not proof they don't provide childcare.

## Gotchas & OpSec
- Human-in-the-loop: **email verification required** before you can access the directory — use a puppet email.
- Membership directory, not a statutory register — coverage is partial; absence is uninformative.
- Republic of Ireland only.
- OpSec: **passive** — a directory read, but tied to the email you register.

## Overlaps ("do both")
- Conceptually pairs with other profession/licensing directories like `[[ama-assn-org]]` — each confirms a person's stated professional role in its own jurisdiction/field; use the one matching the subject's claimed occupation.

## Trust & verifiability
`trust: community` — a genuine national childminding organisation's member directory, but self-selected membership data rather than an authoritative register; corroborate any occupational claim.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | childminding-ie |
| category | public-records |
| selectorsIn → selectorsOut | name, address → name, address, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |

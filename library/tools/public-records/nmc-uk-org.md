---
id: nmc-uk-org
name: nmc-uk.org
description: Use when you have a `name` claimed to be a UK nurse or midwife and want to verify their registration — returns registration status, PIN, qualification and town from the official NMC register.
url: https://www.nmc.org.uk/search-the-register/
category: public-records
path:
- public-records
bestFor: Verifying whether a person is a registered UK nurse/midwife and their registration status.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- address
status: live
pricing: free
costNote: Free official register search; no account.
opsec: passive
opsecNote: Read-only search of the statutory public register; the registrant is not notified. Use a clean session for hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Nursing and Midwifery Council (NMC), the statutory UK regulator — the authoritative source for nurse/midwife registration.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- cilexgroup-org-uk
- ama-assn-org
aliases:
- NMC register
- Nursing and Midwifery Council
tags:
- professionlicensing
- Profession & Licensing Sites
- healthcare-register
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# nmc-uk.org

> The NMC's statutory register search — the authoritative check on whether someone is a registered UK nurse or midwife.

## When to use
You have a `name` for someone who claims (or is claimed) to be a UK nurse, midwife, or nursing associate, and you want to confirm it. A hit gives their registration status, PIN (`document-id`), qualifications, and registered town — corroborating identity and location, or disproving a false professional claim. As the statutory regulator's register, it is authoritative.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.nmc.org.uk/search-the-register/.
2. Search by `name` (or by NMC PIN if known).
3. Read the result: registrant `name`, PIN (`document-id`), registration status (registered/lapsed/struck off), qualifications, and registered town (`address` proxy).
4. Use the PIN as a unique anchor and the town to disambiguate namesakes.
5. Pivot: the town narrows people-search; a confirmed profession corroborates identity; a "struck off" status is itself a lead.

## Inputs → Outputs
- **In:** `name` (or NMC PIN)
- **Out:** `name`, PIN (`document-id`), registration status, qualifications, registered town (`address`)
- **Empty/negative result looks like:** no match — the person isn't (or never was) an NMC registrant, or the name is spelled differently. A non-match disproves a current UK nurse/midwife claim.

## Gotchas & OpSec
- Covers UK nurses/midwives/nursing associates only — not doctors (see medical-council registers) or other health professions.
- Struck-off/lapsed entries may still appear with that status — read the status carefully.
- OpSec: **passive** — a statutory public-register read.

## Overlaps ("do both")
- Pairs with other professional registers like `[[cilexgroup-org-uk]]` (legal executives) and `[[ama-assn-org]]` (US physicians) — each confirms a person's claimed profession in its own field/jurisdiction.

## Trust & verifiability
`trust: trusted` — first-party statutory NMC data; authoritative for UK nurse/midwife registration status.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nmc-uk-org |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: cpaverify-org
name: cpaverify.org
description: Use when you have a `name` and want to confirm whether someone is a licensed US CPA — returns license status, jurisdiction, and issuing-board details (employer-org/address hints).
url: https://cpaverify.org/
category: public-records
path:
- public-records
bestFor: Verifying a US Certified Public Accountant's license across participating state boards in one search.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- address
status: live
pricing: free
costNote: Free public lookup operated by NASBA; no account or payment.
opsec: passive
opsecNote: A public regulatory register — searching it does not contact or notify the subject. Queries go to NASBA's ALD service and are logged there; use a sock-puppet browser if you want to avoid tying the search to yourself. Nothing here is intrusive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by NASBA (National Association of State Boards of Accountancy); aggregates official state-board CPA license data. Authoritative, though not every state participates.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- thentiacloud-net
aliases:
- CPAverify
- NASBA CPA lookup
- ald.nasba.org
tags:
- professionlicensing
- Profession & Licensing Sites
- public-records
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# cpaverify.org

> NASBA's free national CPA license lookup: confirm whether a name holds a valid US CPA license and in which jurisdiction.

## When to use
You have a `name` and a claim (or suspicion) that the person is a licensed CPA, and want to confirm it against official state-board data. A match verifies the profession, ties them to a licensing `jurisdiction`/state (address hint) and issuing board, and can corroborate an `employer-org` claim. Useful for confirming identity/occupation of a subject who presents as an accountant.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cpaverify.org/ (it now routes to NASBA's ALD search at `ald.nasba.org/search/cpa`).
2. Search by name (and state to narrow), or by license/certificate number if you have it.
3. Read the result: name, license status (active/expired/revoked), jurisdiction, and issuing board.
4. Pivot: the license jurisdiction anchors the person to a state; feed the confirmed name to people-search and, for non-CPA professions, check regulator registers like `[[thentiacloud-net]]`.

## Inputs → Outputs
- **In:** `name` (optionally + state or license number)
- **Out:** confirmed `name`, licensing state (`address`/jurisdiction hint), issuing board / `employer-org` context, license status
- **Empty/negative result looks like:** no match — the person isn't a CPA, holds a license in a non-participating state, or the name differs from the licensed form; absence is not proof they never held a license.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — a public register; no subject notification.
- Coverage gap: not all 55 US jurisdictions feed CPAverify, so a "not found" can be a data gap, not a disqualification — check the specific state board directly if it matters.

## Overlaps ("do both")
- Pairs with `[[thentiacloud-net]]` and other professional-register lookups — CPAverify covers accountants; other regulators cover healthcare, law, engineering, etc.

## Trust & verifiability
`trust: trusted` — first-party aggregation by NASBA of official state-board data. A confirmed active license is authoritative; treat "not found" cautiously given partial state participation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cpaverify-org |
| category | public-records |
| selectorsIn → selectorsOut | name → name, employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: genesreunited-co-uk
name: genesreunited.co.uk
description: Use when you have a UK `name` and want genealogy/family-history records — returns census, birth/marriage/death and family-tree matches exposing relatives (`associate`), `dob` and historical `address`es.
url: https://www.genesreunited.co.uk/
category: public-records
path:
- public-records
bestFor: UK family-history research — census, BMD, and member trees to map relatives and historical addresses.
selectorsIn:
- name
selectorsOut:
- associate
- dob
- address
status: live
pricing: freemium
costNote: Free to search and register and see match counts; viewing full records/trees requires a paid subscription or pay-per-view credits.
opsec: passive
opsecNote: Read-only genealogy search; the subject is not notified. Registration and payment expose your identity to the operator (a DC Thomson/Findmypast-family service) — use a sock-puppet account and billing hygiene.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: An established UK genealogy service (part of the Findmypast/DC Thomson family); official records (census, BMD) are authoritative, but user-submitted family trees are unverified.
missingPersonsRelevance: high
coverage:
- uk
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
relatedTools:
- sortedbyname-com
- gro-gov-uk
aliases:
- Genes Reunited
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- family-history
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# genesreunited.co.uk

> A long-running UK family-history service — census, birth/marriage/death records, and member trees to map a subject's relatives and historical addresses.

## When to use
You have a UK `name` and want to build the family and historical-address picture: census entries (which place a household at an address in a given year), BMD records giving `dob`/dates, and member-submitted family trees that link relatives (`associate`). For a missing-persons case this helps identify next of kin, prior addresses, and family connections to approach — and can distinguish namesakes via family context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.genesreunited.co.uk/ and register (use a **sock-puppet** account) — free search shows match counts.
2. Search by `name`, adding approximate year/place to narrow.
3. Free tier: see how many census/BMD/tree matches exist. To view full records/trees, use a subscription or pay-per-view credits.
4. Read the records: census households (relatives + historical `address`), BMD dates (`dob`), and linked family trees.
5. Corroborate member-tree claims against official records before relying on them.
6. Pivot: relatives (`associate`) feed people-search; a death record feeds `[[gro-gov-uk]]`; cross-check names via `[[sortedbyname-com]]`.

## Inputs → Outputs
- **In:** UK `name` (+ approximate year/place)
- **Out:** census (relatives + historical `address`), BMD (`dob`/dates), member family trees (`associate`)
- **Empty/negative result looks like:** no matches, or matches locked behind the paywall — free search shows counts, so zero counts mean the name isn't in the indexed records (or is spelled differently).

## Gotchas & OpSec
- Human-in-the-loop: **account required**, and full records are **paywalled** (subscription/PPV).
- Member-submitted trees are **unverified** — treat as leads; official census/BMD are authoritative.
- Strongest for historical UK records; recent living-person detail is limited by data-protection.
- OpSec: **passive** toward the subject; your account/billing is visible to the operator.

## Overlaps ("do both")
- Pairs with `[[gro-gov-uk]]` (official UK BMD index) and `[[sortedbyname-com]]` — Genes Reunited adds census and family-tree structure; the GRO confirms the official birth/death record.

## Trust & verifiability
`trust: community` — authoritative official records plus unverified user trees; corroborate any tree-derived link against primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | genesreunited-co-uk |
| category | public-records |
| selectorsIn → selectorsOut | name → associate, dob, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, payment-wall-partial) |

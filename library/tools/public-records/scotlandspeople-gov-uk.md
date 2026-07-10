---
id: scotlandspeople-gov-uk
name: scotlandspeople.gov.uk
description: Use when you have a `name` with a Scottish life event and want official vital records — Scotland's registry returns birth/marriage/death, census, and valuation records with `dob` and `associate` links.
url: https://www.scotlandspeople.gov.uk/
category: public-records
path:
- public-records
bestFor: Official Scottish genealogy: statutory births/marriages/deaths, old parish registers, census, and valuation rolls.
selectorsIn:
- name
- address
selectorsOut:
- dob
- associate
- name
status: live
pricing: freemium
costNote: Free to search the indexes (see that a record exists); viewing/downloading a record image costs pay-per-view credits (about £1.50 per image / credit bundles). A free account is needed to buy and use credits.
opsec: passive
opsecNote: Searching official vital records is passive and does not notify anyone (subjects are typically historical/deceased). A registration and payment are needed to view images, tying that activity to your account — use a role-based identity if attribution matters.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official National Records of Scotland service; records are authoritative primary sources for Scotland.
missingPersonsRelevance: high
coverage:
- gb
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- scotlandspeople-gov-uk-2
- gro-gov-uk
- gov-im-2
aliases:
- ScotlandsPeople
- scotlandspeople.gov.uk
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- scotland
- vital-records
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# scotlandspeople.gov.uk

> Scotland's official genealogy service (National Records of Scotland) — statutory birth/marriage/death records, old parish registers, census, and valuation rolls, the primary sources for anyone with a Scottish life event.

## When to use
Your subject has a Scottish connection and you need authoritative vital-record detail: a birth (parents → `associate`, exact `dob`), marriage (spouse, witnesses), death (date/place, informant), a census household, or a valuation-roll address. These primary records anchor a family tree and confirm identity facts aggregators only estimate — invaluable for missing-persons and identity work involving Scotland.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.scotlandspeople.gov.uk/ and create a free account.
2. Search the relevant index (statutory BDM, OPR, census, valuation) by `name`, date range, and place.
3. The index search is free and confirms a record exists; buy pay-per-view credits to view/download the actual record image.
4. Read the record for `dob`/dates, parents/spouse/witnesses (`associate`), and addresses.
5. Pivot: named relatives become new leads; census/valuation addresses feed property and address lookups; for England & Wales use `[[gro-gov-uk]]` instead.

## Inputs → Outputs
- **In:** `name` + approximate date/place (Scotland)
- **Out:** official `dob`/death/marriage dates, `associate`s (parents, spouse, witnesses, household), addresses, confirmed `name`
- **Empty/negative result looks like:** no index match — check spelling/date range and that the event was Scottish (not England & Wales or Isle of Man); recent records are access-restricted by statutory closure periods.

## Gotchas & OpSec
- Human-in-the-loop: **free to search, paid to view** (credits) and an **account** is required — budget for image costs.
- Statutory closure periods restrict recent births/marriages/deaths; very recent records won't be viewable.
- Use the correct jurisdiction — Scotland is separate from England & Wales (`[[gro-gov-uk]]`) and the Isle of Man (`[[gov-im-2]]`).
- OpSec: passive toward subjects; your account/payment ties the activity to you.

## Overlaps ("do both")
- Complements `[[scotlandspeople-gov-uk-2]]` (same service, alternate entry) and sits beside `[[gro-gov-uk]]` and `[[gov-im-2]]` for other UK jurisdictions — pick where the event was registered.

## Trust & verifiability
`trust: trusted` — the official National Records of Scotland service, so records are authoritative primary evidence. The only friction is cost/closure periods, not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scotlandspeople-gov-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, address → dob, associate, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial, account-login) |

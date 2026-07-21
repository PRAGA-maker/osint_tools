---
id: nationwide-county-court-records
name: Nationwide County Court Records
description: Use when you have a `name` plus a county/state and want the official portal to search that jurisdiction's court records — returns links out to court systems that yield case records, `address` and `associate` leads.
url: https://www.publicrecordcenter.com/onlinecourtrecords.htm
category: public-records
path:
- public-records
- court-criminal-records
bestFor: A directory that routes you to the correct federal/state/county court record system so you can search cases by name.
selectorsIn:
- name
selectorsOut:
- document-id
- address
- associate
status: live
pricing: freemium
costNote: The directory and links are free; PACER (federal) charges per page for documents, and some state/county portals levy their own retrieval fees. Finding and searching is generally free.
opsec: passive
opsecNote: Passive at the directory level. The court portals it links to are also passive lookups, but some (e.g. PACER) require registration and log searches; use appropriate accounts and expect an audit trail on official systems.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A privately owned directory that links to official court resources; it stores no records itself, so trust the destination government portals, not the directory's framing.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- PublicRecordCenter court records
- online court records directory
tags:
- court-records
- directory
source: arf-seed
lastVerified: '2026-07-21'
enrichment: full
---

# Nationwide County Court Records

> A signpost, not a database: it points you to the correct federal, state, or county court system so you can run a name search at the authoritative source.

## When to use
You have a subject `name` and a jurisdiction (county + state, or "federal") and need the *right* court portal to search — civil, criminal, family, probate, or bankruptcy cases. Court records are one of the richest OSINT sources for locating and profiling a person: they expose addresses, relatives and associates (co-parties, co-defendants), employers, and life events. This directory saves you from guessing which of thousands of court systems to use.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.publicrecordcenter.com/onlinecourtrecords.htm.
2. Decide the level: **federal** (use the linked PACER / Federal Court Finder) or **state/county** (follow the link to the relevant state judiciary, then drill to the county).
3. Go to that official portal and run a party-name search there — this directory does not search for you.
4. On PACER, expect to register and pay per page for documents (search is free; fees are waived under a quarterly threshold). County portals vary: some free, some fee, some in-person only.
5. Pivot: a case caption yields co-parties (`associate`s), a listed `address`, and a `document-id`/case number to pull filings that often contain far more identifying detail.

## Inputs → Outputs
- **In:** a `name` + jurisdiction (county/state or federal)
- **Out:** links to the correct court system, where a name search yields case `document-id`s, `address`es, and `associate`/co-party names
- **Empty/negative result looks like:** the directory has no direct link for that county (it defers to the state judiciary site), or the destination portal returns no cases — meaning none in that court, not none anywhere.

## Gotchas & OpSec
- It's a **directory**, not a search engine — you still do the searching on the destination portal.
- Coverage of counties is uneven; for many you land on a state-level page and must navigate to the county yourself.
- PACER and some state systems require login and log your searches — a human-in-the-loop account step, and an audit trail to be aware of.

## Overlaps ("do both")
- Pairs with statewide court-record search portals and PACER front-ends — use this to *find* the right system, those to actually pull the records efficiently.

## Trust & verifiability
`trust: unverified` — a privately owned link directory (its own disclaimer: it does not create, verify, or store records); the authority lives entirely in the official government portals it routes you to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nationwide-county-court-records |
| category | public-records |
| selectorsIn → selectorsOut | name → document-id, address, associate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |

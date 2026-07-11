---
id: nb-courts-public-self-serve-website
name: New Brunswick Courts — Public Self-Serve
description: Use when you have a `name` and a New Brunswick (Canada) connection and want to find court cases involving that person — returns case participants, case type, location and case document-id.
url: https://www1.gnb.ca/nota/default.aspx
category: public-records
path:
- public-records
bestFor: Searching New Brunswick court cases (civil, small claims, bankruptcy, probate) by participant name.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- associate
status: live
pricing: free
costNote: Free public court-records search operated by the Government of New Brunswick; no account or payment.
opsec: passive
opsecNote: A public government court database; searching is passive and the subject is not notified. No login required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Government of New Brunswick (gnb.ca); authoritative first-party court record data.
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- NB Courts self-serve
- New Brunswick court case search
tags:
- court
- legal-records
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# New Brunswick Courts — Public Self-Serve

> New Brunswick's official online court case search — look up a person by name to see civil, small-claims, bankruptcy and probate matters they're involved in, and who else is party to them.

## When to use
You have a `name` and a New Brunswick (Canada) nexus and want to find court involvement: civil suits, small claims, bankruptcy, or probate. Court records tie a person to other parties (`associate`), dates and locations — useful for locate work, next-of-kin/estate (probate) leads, and building a subject's legal footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www1.gnb.ca/nota/default.aspx.
2. Search by participant name (results span eight regional courthouses: Moncton, Saint John, Fredericton, Woodstock, Edmundston, Campbellton, Bathurst, Miramichi).
3. Read the returned case(s): participants, case type, courthouse/location, and the case reference for follow-up.
4. Contact the listed courthouse for fuller records where needed.
5. Pivot: co-parties are `associate` leads; a probate case points to next-of-kin/executors (strong for missing-persons/estate work); case locations narrow geography.

## Inputs → Outputs
- **In:** `name` (participant)
- **Out:** case participants (`name`/`associate`), case type, location, and case reference (`document-id`)
- **Empty/negative result looks like:** no matching cases — the person may have no NB court involvement, or (note) recently filed cases lag before appearing, and Charlotte County probate is excluded. Absence is weak evidence.

## Gotchas & OpSec
- **Filing lag:** there's a delay between filing and appearance in search — recent matters may be missing.
- Coverage gaps: Charlotte County probate is excluded; some case detail requires contacting the courthouse.
- New Brunswick only — other provinces have separate systems (e.g. CanLII for judgments nationally).
- OpSec: passive, authoritative government data; no subject notification.

## Overlaps ("do both")
- Pairs with CanLII (published Canadian judgments) and other provincial court portals — this gives case existence/parties in NB; CanLII gives written decisions.

## Trust & verifiability
`trust: trusted` — first-party New Brunswick government court records. Case existence and parties are authoritative; for full detail, follow up with the named courthouse.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nb-courts-public-self-serve-website |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

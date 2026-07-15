---
id: sex-offender-korea
name: Sex Offender Korea
description: Use when you need to check South Korea's official sex-offender registry for a `name`/location — returns offender name, photo, address area and offence, but access is gated behind Korean real-name authentication.
url: https://www.sexoffender.go.kr/indexN.nsc
category: public-records
path:
- public-records
bestFor: Checking South Korea's official registry of registered sex offenders by name, location, or proximity to schools.
selectorsIn:
- name
- address
selectorsOut:
- name
- address
- image
- physical-description
status: live
pricing: free
costNote: Free government service, but viewing requires Korean real-name authentication (resident registration number, Korean mobile, i-PIN, or Digital OnePass) — effectively inaccessible without Korean ID.
opsec: passive
opsecNote: The lookup itself is passive against a government registry. However, access is logged against your authenticated Korean identity, and the law expressly forbids republishing or misusing the data (penalties under the Act on child/youth sexual-abuse crimes) — treat any information as legally restricted.
humanInLoop: true
humanInLoopReason:
- legal-gate
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: 성범죄자 알림e — the official public registry operated by South Korea's Ministry of Gender Equality and Family; an authoritative first-party source.
missingPersonsRelevance: high
coverage:
- kr
auth: account
api: false
localInstall: false
registration: true
aliases:
- 성범죄자 알림e
- Sex Offender Notification e
- sexoffender.go.kr
tags:
- sex-offender
- registry
- south-korea
- public-records
source: osint4all
lastVerified: '2026-07-15'
enrichment: full
---

# Sex Offender Korea

> 성범죄자 알림e — South Korea's official government sex-offender registry. Authoritative and photo-backed, but walled behind Korean real-name authentication and strict misuse laws.

## When to use
Your subject has a South Korean connection and you need to check whether they are a registered sex offender, or you want to screen a Korean location (near a school/residence) for registered offenders. Because this is the *official* MOGEF registry, a hit is authoritative — but you can only use it if you (or a Korean partner) can pass real-name authentication.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.sexoffender.go.kr/ — expect an immediate real-name authentication gate.
2. Authenticate via one of the accepted methods (resident registration number, Korean mobile, i-PIN, or Digital OnePass). Without Korean ID this is where non-Korean investigators stop; route through a Korean-resident collaborator with a lawful purpose.
3. Search by offender name/registration number, or map-search by district / school-proximity (1 km) / address radius (2 km).
4. Read the record: name, photo, offence summary, and address area. Pivot cautiously — the data is legally restricted.

## Inputs → Outputs
- **In:** `name` / `address` (location or school area)
- **Out:** offender `name`, `image` (photo), `address` (area), offence details / `physical-description`
- **Empty/negative result looks like:** no match — the person isn't on the registry, or (far more often for outside investigators) you never got past the authentication wall. Distinguish "no offender found" from "couldn't access."

## Gotchas & OpSec
- **Access wall** (`account-login`): Korean real-name authentication is mandatory; foreigners generally cannot access it directly.
- **Legal restriction** (`legal-gate`): the enabling Act limits use to child/youth protection and criminalizes internet republication/misuse — do not scrape, redistribute, or post the data.
- Data is district-level and purpose-bound; treat it as sensitive.
- OpSec: passive query, but access is identity-bound and audited.

## Overlaps ("do both")
- Pairs with Korean court/news records and, for other countries, their national registries (e.g. US NSOPW) — cross-jurisdiction offenders won't appear here, so check the relevant country's official registry too.

## Trust & verifiability
`trust: trusted` — an authoritative government registry with photos. Reliability is high; the binding constraints are lawful access and lawful use, not data quality.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sex-offender-korea |
| category | public-records |
| selectorsIn → selectorsOut | name, address → name, address, image, physical-description |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (legal-gate) |

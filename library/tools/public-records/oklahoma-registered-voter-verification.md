---
id: oklahoma-registered-voter-verification
name: Oklahoma Registered Voter Verification
description: Use when you have a `name` and want to confirm an Oklahoma voter registration — returns a registration match (and, on the official portal, precinct/last-known address context).
url: http://www.oklahomadata.com/voters.asp
category: public-records
path:
- public-records
bestFor: Confirming whether a name is a registered Oklahoma voter as a proof-of-presence/last-known-location lead.
selectorsIn:
- name
selectorsOut:
- address
status: degraded
pricing: free
costNote: Free to search; no payment. This third-party site (long GoDaddy-hosted) has been undergoing a migration, so availability is intermittent.
opsec: passive
opsecNote: A name-inquiry against published voter-roll data — nothing is written and the subject is not notified. Because this is a third-party mirror rather than the official state system, prefer the Oklahoma State Election Board's own voter-status tool when you need an authoritative, current answer.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party site presenting Oklahoma voter data, not the official State Election Board portal; treat a match as a lead and confirm against the official OK voter-status lookup.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- oklahoma-voters-search
aliases:
- oklahomadata.com voters
- OK voter name inquiry
tags:
- toddington
- curated-directory
- specialty-search
- voter-records
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Oklahoma Registered Voter Verification

> A free Oklahoma voter name-inquiry — search a name to confirm a registration and get a proof-of-presence lead in the state.

## When to use
You have a `name` with an Oklahoma connection and want to confirm the person is (or was) a registered voter there. A registration match is a useful proof-of-presence signal for a missing-persons or skip-trace timeline: it places the person in a jurisdiction and, via the official Election Board portal, ties to a precinct and the residential address on file. Use this third-party site as a quick first pass, then verify anything load-bearing against Oklahoma's official State Election Board voter-status lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.oklahomadata.com/voters.asp and search by last name plus first name (or first initials).
2. Review matches; note the registration and any location/precinct detail shown.
3. Confirm the result on the official Oklahoma State Election Board "Online Voter Tool" (authoritative, current status and precinct).
4. Pivot: a confirmed registration + precinct/`address` feeds people-search and a residential-history timeline.

## Inputs → Outputs
- **In:** `name` (Oklahoma)
- **Out:** voter-registration match → precinct / last-known `address` context (fullest on the official portal)
- **Empty/negative result looks like:** no match — meaning no registration under that name (or the site is mid-migration/unavailable); this does not prove the person never lived in Oklahoma.

## Gotchas & OpSec
- Human-in-the-loop: none, but the site has been migrating — if it errors, use the official State Election Board tool.
- Third-party mirror: treat as a lead; the official Oklahoma voter-status portal is authoritative.
- Common names return multiple registrants — disambiguate with county/DOB where the official tool allows.

## Overlaps ("do both")
- Pairs with `[[oklahoma-voters-search]]` and the official OK State Election Board lookup — cross-check the match and pull authoritative precinct/address detail.

## Trust & verifiability
`trust: community` — a third-party presentation of voter data, currently degraded by a migration; confirm every match against the official Oklahoma State Election Board voter-status tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | oklahoma-registered-voter-verification |
| category | public-records |
| selectorsIn → selectorsOut | name → address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

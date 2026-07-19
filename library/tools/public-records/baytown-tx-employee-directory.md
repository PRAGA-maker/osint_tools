---
id: baytown-tx-employee-directory
name: Baytown TX Employee Directory
description: Use when you have a `name` you suspect works for the City of Baytown, Texas and want to confirm — returns employee/department listing details.
url: https://c0ctb134.caspio.com/dp/c5f5200097e7aef4edb54e09bd5e
category: public-records
path:
- public-records
bestFor: Confirming whether a person is a City of Baytown (Texas) municipal employee and finding their department/role.
selectorsIn:
- name
selectorsOut:
- employer-org
status: degraded
pricing: free
costNote: Free public Caspio-hosted directory datapage; no login or payment.
opsec: passive
opsecNote: Passive lookup of a public municipal directory; the employee is not notified. It is a third-party Caspio embed, so your query hits Caspio's servers rather than a city domain — no target footprint.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A standalone Caspio datapage with no visible official City-of-Baytown branding on the embed URL; treat as an unofficial/mirrored directory and confirm any hit against the city's own site before relying on it.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Baytown Texas city employee directory
tags:
- public-records
- employee-directory
- municipal
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# Baytown TX Employee Directory

> A public Caspio-hosted employee directory datapage for the City of Baytown, Texas — a narrow lookup to confirm municipal employment and department for a named subject.

## When to use
You have a `name` and a lead that the person works (or worked) for the City of Baytown, TX, and you want to confirm it and pull their department/role. This is a hyper-local, single-jurisdiction resource — only useful when your subject is specifically tied to Baytown municipal government.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://c0ctb134.caspio.com/dp/c5f5200097e7aef4edb54e09bd5e (a Caspio "Employee_Directory_Display" datapage).
2. Search or browse by name.
3. Read the listing for department/role (`employer-org` confirmation) and any contact fields exposed.
4. Pivot: a confirmed municipal role feeds local news, public-salary, and records searches; the department narrows further inquiries.

## Inputs → Outputs
- **In:** `name`
- **Out:** `employer-org` confirmation (City of Baytown department/role)
- **Empty/negative result looks like:** no matching entry — the person isn't in this directory (not on staff, since separated, or the datapage is stale). The embed may also fail to load if the datapage has been retired.

## Gotchas & OpSec
- Single-jurisdiction and narrow — irrelevant unless the subject is tied to Baytown, TX.
- The URL is a bare Caspio datapage with no official city branding; verify any hit against Baytown's official website before trusting it. Directory may be outdated.
- OpSec: passive; no notification to the subject.

## Overlaps ("do both")
- Complements state/municipal public-salary and records tools — use this to confirm employment, those to enrich with salary/history.

## Trust & verifiability
`trust: unverified` — an unofficial-looking standalone datapage; a hit is a lead to confirm against the city's authoritative records, not proof on its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | baytown-tx-employee-directory |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

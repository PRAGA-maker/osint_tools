---
id: whocalld
name: WhoCalld
description: Use when you have a `phone` number and want caller-ID/spam context — DEFUNCT service, retained as a historical reference only; returns nothing usable today.
url: https://whocalld.com/
category: phone
path:
- phone
bestFor: Historical reference only — the service is defunct and should not be relied on in live casework.
selectorsIn:
- phone
selectorsOut:
- name
status: down
pricing: freemium
costNote: When operational it offered a free reverse-lookup tier with paid/API access; the service is now defunct so pricing is moot.
opsec: passive
opsecNote: Do not use in active casework — the service is marked defunct and its current behavior (redirects, parked domain, or resold traffic) cannot be trusted. Treat any page that loads there as untrusted; do not enter a real target number.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Defunct per project guidance; historical reverse-caller-ID service with no verifiable current operation or data quality.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: true
relatedTools:
- truecaller-search-engine
aliases:
- whocalld.com
tags:
- phone
- reverse-caller-id
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# WhoCalld

> A defunct reverse-caller-ID / spam-lookup service — kept in the library as a historical reference so agents recognize it and route to a live alternative instead.

## When to use
Effectively **never** in live casework. This entry exists so that if you encounter WhoCalld referenced in an old guide, blog, or link list, you know it is no longer a reliable tool. When you have a `phone` number and want caller-identity or spam context, skip this and use a maintained alternative (see Overlaps).

## How to use it (`bestInteractionPattern`: web-manual)
1. Do not enter a real target number. The domain is defunct; whatever loads there today is unverified and may be a parked page, a redirect, or resold traffic.
2. If you specifically need to document what WhoCalld historically provided, treat any live page as untrusted and observe only — do not register, log in, or submit data.
3. Route the actual lookup to a working reverse-phone tool instead.

## Inputs → Outputs
- **In:** `phone` (historically)
- **Out:** historically a caller `name` and spam/nuisance context; **today: nothing usable**
- **Empty/negative result looks like:** the expected state — the service does not return trustworthy data anymore; assume any output is stale or fabricated.

## Gotchas & OpSec
- Marked `deprecated`/`down` by project guidance; do not treat results as evidence.
- A dead OSINT domain is a classic candidate for takeover — a new owner could log or misuse any number you submit. Enter nothing real.
- OpSec: nominally passive, but the safe posture is to avoid the site entirely.

## Overlaps ("do both")
- Superseded by [[truecaller-search-engine]] and other maintained reverse-phone services — use those for live caller-ID and spam context instead of WhoCalld.

## Trust & verifiability
`trust: unverified` — the service is defunct with no verifiable current operator or data pipeline; retained only as a historical marker, not a usable source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whocalld |
| category | phone |
| selectorsIn → selectorsOut | phone → name |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |

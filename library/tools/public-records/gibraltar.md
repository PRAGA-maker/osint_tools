---
id: gibraltar
name: Gibraltar
description: Use when you have a Gibraltar company `employer-org` or a person's `name` and want the registered beneficial owners behind it — returns name, dob, and nationality of controlling persons (login-gated).
url: https://ubosearch.egov.gi/Login?ReturnUrl=%2f
category: public-records
path:
- public-records
bestFor: Identifying beneficial owners of Gibraltar-registered companies via the Gibraltar UBO search portal.
selectorsIn:
- employer-org
- name
selectorsOut:
- name
- dob
status: live
pricing: freemium
costNote: Gibraltar government UBO search portal. Requires an authenticated eGov account, and access to another entity's beneficial owners is subject to eligibility/legitimate-interest rules; some searches carry a fee.
opsec: active
opsecNote: Access is via authenticated Gibraltar eGov login and is logged against your identity. This is a named, auditable government interaction — not anonymous OSINT. Do not register or access under a false identity.
humanInLoop: true
humanInLoopReason:
- account-login
- legal-gate
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Gibraltar government beneficial-ownership register portal; filings are legally mandated and authoritative.
missingPersonsRelevance: high
coverage:
- gi
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- belgium
- austria
- opencorporates-com
aliases:
- Gibraltar UBO register
- ubosearch.egov.gi
tags:
- companysites
- Company Related Sites
- beneficial-ownership
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Gibraltar

> Gibraltar's UBO search portal: find the natural persons who ultimately own or control a Gibraltar company — behind an authenticated eGov login.

## When to use
You have a Gibraltar `employer-org` and need the beneficial owners behind it — relevant because Gibraltar is a common offshore incorporation jurisdiction, so piercing to the controlling natural persons (`name`, `dob`, nationality) can tie a subject to offshore structures, assets, and co-owners. Also usable to check which Gibraltar entities a given `name` beneficially owns.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://ubosearch.egov.gi/ and register/sign in with a Gibraltar eGov account.
2. Confirm your eligibility to search (access to third-party UBO data is gated by the applicable rules; a fee may apply).
3. Search by the company name or registration number.
4. Read the beneficial-owner record: names, dates of birth, nationality, and nature/extent of control.
5. Pivot: named owners feed people-search; the company number feeds the Gibraltar Companies House and [[opencorporates-com]] for directors and filings.

## Inputs → Outputs
- **In:** `employer-org` (company / registration number) or `name`
- **Out:** `name`, `dob`, nationality of beneficial owners, and control details
- **Empty/negative result looks like:** access denied (not eligible / not authenticated) or no registered owner returned — for offshore vehicles, absence may reflect nominee/complex structuring rather than genuinely no owner.

## Gotchas & OpSec
- Login and eligibility gate: general anonymous public browsing is not available.
- Offshore structures often use nominees and layered holdings — a single UBO record may not reveal the true controller; follow the chain.
- Human-in-the-loop: authenticated login and possible legitimate-interest/fee gate.
- OpSec: **active and named** — access is tied to your verified identity and logged.

## Overlaps ("do both")
- Mirrors [[belgium]] and [[austria]] as an EU/UK-adjacent beneficial-ownership register — use the same access/standing playbook — and pairs with [[opencorporates-com]] to identify the entity and its officers before (or without) the UBO gate.

## Trust & verifiability
`trust: trusted` — the official Gibraltar government UBO register, with legally mandated filings, so the data is authoritative where you have access; the limits are eligibility gating and offshore nominee structuring, not data quality.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gibraltar |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → name, dob |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login, legal-gate) |

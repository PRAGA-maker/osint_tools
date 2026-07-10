---
id: familytree
name: FamilyTree
description: Use when you have a `name` and want a free US map of relatives, past/current addresses and age — returns `associate`, `address`, `dob`, `phone`.
url: https://www.familytreenow.com/
category: people-search
path:
- people-search
bestFor: Free, no-login US people search that surfaces relatives/associates and an address history from one name.
selectorsIn:
- name
- address
- phone
selectorsOut:
- associate
- address
- dob
- phone
status: live
pricing: freemium
costNote: Core people/relatives/address search is genuinely free with no account. It monetises via upsell links to paid background-check partners for deeper reports; you can ignore those and stay on the free tier.
opsec: passive
opsecNote: Searches run against FamilyTreeNow's own aggregated database — the subject is not notified and does not see you. Browsing is passive. If you plan repeated queries, use a clean browser/IP; the site sets tracking cookies. Never enter your own real details into the (CAPTCHA-gated) opt-out flow from an investigative session.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running US data aggregator that recompiles public records; coverage is broad but data is often stale or conflated across same-name individuals — corroborate before acting.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- FamilyTreeNow
- familytreenow.com
tags:
- people-search
- relatives
- address-history
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# FamilyTree

> FamilyTreeNow — a free, no-registration US people-search that hands you a subject's relatives, associates, age, and address history from just a name.

## When to use
You have a `name` (optionally narrowed by a city/state, an old `address`, or a `phone`) for a US subject and you want to build out their network and location history at zero cost: known relatives, possible associates, current and prior addresses, and an approximate age/`dob`. It is one of the strongest free first-stop tools for missing-persons work because it exposes the family/associate graph you can then contact or trace.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.familytreenow.com/ and choose the People (or Address/Phone) search tab.
2. Enter the `name`; add city/state to disambiguate common names.
3. Solve the CAPTCHA if prompted, then open the best-matching record.
4. Read the profile: possible aliases, age/birth year (`dob`), current + past `address` list, `phone` numbers, and — most valuable — the "Possible Relatives" and "Possible Associates" lists.
5. Pivot: run each relative/associate name back through FamilyTreeNow or a court/records tool like `[[iowa-courts-online-search]]`; feed addresses into map/street-view checks.

## Inputs → Outputs
- **In:** `name` (+ optional city/state, `address`, or `phone`)
- **Out:** `associate` (relatives/associates), `address` history, `dob`/age, `phone`
- **Empty/negative result looks like:** no matching record, or a record with no relatives/addresses — common for young people, recent movers, or those who have opted out. Absence is not proof of non-existence.

## Gotchas & OpSec
- Human-in-the-loop: a **CAPTCHA** gates searches; solve it manually. Heavy querying may temporarily block you.
- OpSec: **passive** — the subject is never notified. Use a sock-puppet browser/IP for volume; expect tracking cookies.
- Data quality: records frequently conflate two same-name people and include outdated addresses. Treat every field as a lead, cross-check before relying on it.

## Overlaps ("do both")
- Pairs with `[[iowa-courts-online-search]]` and other public-records tools — FamilyTreeNow gives the relatives/address graph; court records confirm identity and add case detail.

## Trust & verifiability
`trust: community` — a well-known aggregator, but it recompiles public data with no privacy filtering and notable staleness/conflation. Verify names, ages, and addresses against a second source before acting on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | familytree |
| category | people-search |
| selectorsIn → selectorsOut | name, address, phone → associate, address, dob, phone |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |

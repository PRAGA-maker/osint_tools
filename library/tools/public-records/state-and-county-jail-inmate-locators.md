---
id: state-and-county-jail-inmate-locators
name: State and County Jail Inmate Locators
description: Use when you have a `name` and want to check whether a subject is currently or was recently incarcerated in a US state prison or county jail — returns offense, facility, and biographical record hints.
url: https://inmatesplus.com
category: public-records
path:
- public-records
bestFor: Checking whether a named person is incarcerated in a US state/county correctional facility.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
- address
status: live
pricing: freemium
costNote: The name search and basic hit list are free; some detail pages and background-report upsells route to paid third-party data brokers. Stay on the free official-record layer.
opsec: passive
opsecNote: Passive — you are querying an aggregator's index, not contacting the subject or a facility. The subject is not notified. Use a clean browser if you want to avoid the site profiling your interest, but no account is required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial inmate-locator aggregator, not an official corrections agency. Treat any hit as a lead to confirm against the relevant state DOC or county sheriff's official roster.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- InmatesPlus
- inmatesplus.com
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# State and County Jail Inmate Locators

> A commercial nationwide inmate-locator aggregator that lets you check a name against incarceration and criminal-offense records across all 50 US states plus DC in one search.

## When to use
You have a `name` (ideally plus a state or approximate `geolocation`) and need to know whether the subject is currently held, or was recently held, in a US state prison or county jail. This is a fast first pass when a missing person may have been arrested or detained: a hit gives you a facility, an offense, and an inmate/booking `document-id` you can then verify against the authoritative state Department of Corrections or county sheriff roster.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://inmatesplus.com in a browser.
2. Enter the subject's `name` and, if prompted, narrow by state (nationwide search is also offered).
3. Read the hit list: each result shows a name, offense description, sentencing detail, and current/past facility. Match on name + any known `dob` or `geolocation`.
4. Open a promising record for the facility name and inmate/booking number (`document-id`).
5. Pivot: confirm the hit on the authoritative source — the state DOC offender search (e.g. `[[kansas]]` for KS) or the county jail roster — before treating it as fact. The facility also gives you a physical location to work from.

## Inputs → Outputs
- **In:** `name` (+ optional state)
- **Out:** `name`, offense/charge, facility, sentencing dates, inmate/booking `document-id`, sometimes `dob`
- **Empty/negative result looks like:** no matching records, or only unrelated names. A blank result is NOT proof the person was never incarcerated — coverage is "select states" and aggregated, so absence here just means "not in this index"; check the specific state/county source directly.

## Gotchas & OpSec
- No login or captcha for the basic search, so this is low-friction and passive.
- Detail pages frequently funnel into paid "full background report" broker upsells — those are third-party data brokers, not corrections records. Don't pay for what the official DOC roster gives free.
- Common names produce many false hits; always corroborate with a second selector (`dob`, mugshot, middle name, facility location).
- Aggregated data lags reality — a released person may still show as incarcerated and vice versa.

## Overlaps ("do both")
- Pairs with authoritative state rosters like `[[kansas]]` (KASPER) and `[[oregon-offender-search]]` — this aggregator finds *which* state to look in; the official roster confirms and adds current status.
- Pairs with `[[sex-offender-search]]` for a parallel registry check.

## Trust & verifiability
`trust: unverified` — it is a commercial aggregator that re-indexes public corrections data, not a government system. The underlying facts are usually real but stale or incomplete; every hit must be confirmed against the official state DOC or county sheriff source before it is relied upon.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | state-and-county-jail-inmate-locators |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id, address |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

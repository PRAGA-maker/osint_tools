---
id: federal-inmate-locator
name: Federal Inmate Locator
description: Use when you have a `name` or BOP register number and want to know if the person is in US federal prison — returns facility, custody status, and release date.
url: https://www.bop.gov/inmateloc/
category: public-records
path:
- public-records
- court-criminal-records
bestFor: Confirming whether a person is (or was) in US federal custody and locating the facility and release date.
selectorsIn:
- name
- document-id
- dob
selectorsOut:
- geolocation
- name
- dob
status: live
pricing: free
costNote: Free official US Bureau of Prisons service; no account or payment.
opsec: passive
opsecNote: Public federal database queried anonymously; the inmate and the BOP get no signal identifying who searched. Fully passive. No login or footprint on the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the US Federal Bureau of Prisons (bop.gov); authoritative first-party government custody data, updated daily.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- federal-bureau-of-prisons-inmate-locator-us
- the-inmate-locator
- sorted-by-birth-date
aliases:
- BOP Inmate Locator
- Federal Bureau of Prisons inmate locator
tags:
- incarceration
- criminal-records
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Federal Inmate Locator

> The US Bureau of Prisons' official inmate locator — the authoritative "is this person in federal prison, and where" check.

## When to use
A subject has dropped off the map and you need to rule incarceration in or out. If they may be held in the *federal* system (federal crimes, immigration-related federal custody), this tells you the facility, custody status, and projected release date. A found record can explain a disappearance and gives you a physical location to make contact. Note: this is FEDERAL only — state prisons and county jails are separate systems (use state DOC locators and `[[the-inmate-locator]]`).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.bop.gov/inmateloc/.
2. Search either by **BOP Register Number** (exact) or by **name** — first/last, optionally with middle name, age/DOB, race, and sex to disambiguate.
3. Read the result: current facility (or "released"), register number, age, race, and release date.
4. Covers current inmates plus those in federal custody back to 1982 (and via microfilm records earlier), so it works for historical cases too.
5. Pivot: a facility → contact/visitation and mail channels; a register number → uniquely identifies the person across other corrections records; a "released" date → resume the search from that date forward.

## Inputs → Outputs
- **In:** `name` (+ optional `dob`/age, race, sex) or BOP register number (`document-id`)
- **Out:** facility `geolocation`, custody status, register number, age, release date, confirmed `name`
- **Empty/negative result looks like:** "0 results" — the person is not (and was not since 1982) in federal custody; they may still be in a *state* prison or *county* jail, which this database does not cover.

## Gotchas & OpSec
- Federal only. Most incarceration is state/county — a null here does NOT mean "not incarcerated." Always also check the relevant state DOC locator.
- Common names return multiple hits; use age/DOB/race and the register number to confirm the right person.
- Fully passive and anonymous — safe to run without any OpSec exposure to the subject.

## Overlaps ("do both")
- Pairs with `[[the-inmate-locator]]` and state DOC search tools — this covers federal; those cover state/county, and you should run both to fully rule out incarceration.

## Trust & verifiability
`trust: trusted` — first-party US government (Federal Bureau of Prisons) data, updated daily; among the most authoritative custody sources available.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | federal-inmate-locator |
| category | public-records |
| selectorsIn → selectorsOut | name, document-id, dob → geolocation, name, dob |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

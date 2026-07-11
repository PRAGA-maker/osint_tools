---
id: sex-offender-registry-websites
name: Sex Offender Registry Websites
description: Use when you have a `name` or `geolocation` and want to check US sex-offender registries — returns registrant `name`, `address`, `image`, `physical-description` and `dob` via the national/state public registries.
url: https://www.fbi.gov/scams-and-safety/sex-offender-registry
category: public-records
path:
- public-records
bestFor: Locating a registered sex offender by name or area across US national and state registries.
selectorsIn:
- name
- geolocation
- address
selectorsOut:
- name
- address
- image
- physical-description
- dob
status: live
pricing: free
costNote: Free public-safety registries. The FBI page is a gateway to NSOPW (the National Sex Offender Public Website) and individual state registries; all are free, no account.
opsec: passive
opsecNote: You search public safety registries; nothing is disclosed to the subject. Passive. Be aware registry data is legally restricted to lawful purposes — do not use it to harass, and don't rely on it for anything other than what the registry authorizes.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The FBI gateway links to NSOPW (a US Department of Justice service) and official state registries — authoritative government data. Currency varies by state, and registries only list convicted, registered offenders.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- nsopw
aliases:
- NSOPW
- National Sex Offender Public Website
- state sex offender registry
tags:
- court
- criminal-records
- registry
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# Sex Offender Registry Websites

> The FBI's gateway to US sex-offender registries — chiefly NSOPW, which searches all state, territorial, and tribal registries at once by name or by location.

## When to use
You have a `name` and want to check whether the subject is a registered sex offender, or you have a `geolocation`/`address` and want the registered offenders in that area. These registries return strongly identifying data: full `name` and aliases, current registered `address`, a photo (`image`), `physical-description` (height, weight, marks, scars, tattoos), and `dob` — valuable for confirming identity, locating a subject with a registration obligation, or vetting an area in a missing-person context.

## How to use it (`bestInteractionPattern`: web-manual)
1. From the FBI page (https://www.fbi.gov/scams-and-safety/sex-offender-registry) follow the link to NSOPW (nsopw.gov), the national search.
2. Search by `name` (national, across all jurisdictions) or by location/`address` radius.
3. Review results: each registrant record shows photo, aliases, registered address, physical description, and offense/registration details.
4. For deeper/local data, use the specific state registry the record points to (some states expose more fields than the national aggregator).
5. Pivot: a registered `address` narrows current location; the `image` feeds face/reverse-image search; `physical-description` corroborates other sightings.

## Inputs → Outputs
- **In:** `name` or `geolocation`/`address` (area search)
- **Out:** `name` + aliases, registered `address`, `image`, `physical-description`, `dob`, offense details
- **Empty/negative result looks like:** no match — the person isn't a registered offender in the searched jurisdictions (or uses a name variant). Registries only list registered convictions, so absence is not a general background check.

## Gotchas & OpSec
- Human-in-the-loop: none technically, but a hard **ethical/legal** frame — this data is provided for public safety, and misuse (harassment, discrimination) is unlawful in many states. Use only for legitimate investigative purposes.
- OpSec: **passive** — a public registry search; the subject is not notified.
- Coverage and freshness vary by state; a person may be registered in one state and not appear in another's search. Cross-check the national NSOPW and the relevant state site.

## Overlaps ("do both")
- Effectively a front for `[[nsopw]]` (the national aggregator) plus per-state registries — run the national search first for breadth, then the specific state registry for the fuller record and most current address.

## Trust & verifiability
`trust: trusted` — official DOJ/state government registries. Data is authoritative but only as current as each state's last update, and limited to registered offenders; verify the specific individual (photo + DOB) before acting on a name match.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sex-offender-registry-websites |
| category | public-records |
| selectorsIn → selectorsOut | name, geolocation, address → name, address, image, physical-description, dob |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

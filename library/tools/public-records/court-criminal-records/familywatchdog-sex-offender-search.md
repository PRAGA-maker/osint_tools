---
id: familywatchdog-sex-offender-search
name: Family Watchdog - Sex Offender Search
description: Use when you have a `name` or `address` and want to check US sex-offender registries — returns offender photo, registered `address`, and offense details on a map.
url: https://www.familywatchdog.us/
category: public-records
path:
- public-records
- court-criminal-records
bestFor: Free nationwide (US) sex-offender lookup by name or address, aggregating all state registries into one mapped interface.
selectorsIn:
- name
- address
selectorsOut:
- address
- image
- physical-description
status: live
pricing: free
costNote: Free to search and view offender maps; supported by ads and optional email alerts. No account needed to search.
opsec: passive
opsecNote: Passive — you query an aggregator's copy of public state registry data; the registrant is not notified. Note the legal gate below — registry data may only be used for public-safety purposes, not to harass an individual.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running aggregator of official state sex-offender registries, refreshed daily; it mirrors government data but is a third party, so confirm a hit against the authoritative state/NSOPW registry.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- familywatchdog.us
- Family Watchdog
tags:
- sex-offender
- registry
- public-records
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Family Watchdog - Sex Offender Search

> A free, daily-updated aggregator of every US state sex-offender registry with a single map/name search — one place to check a `name` or `address` against registrant records nationwide.

## When to use
You have a `name` or an `address` and want to know whether a registered sex offender is associated with it — a background check on a person of interest, a location, or the vicinity of a school/daycare. Because it merges all state registries and maps them, it's faster than checking states one by one, and useful in missing-persons or safeguarding contexts for surfacing a registrant's registered address, photo, and offense.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.familywatchdog.us/.
2. Search by **address / city / ZIP** to see a map of nearby registrants, or by **first/last name** to find a specific person.
3. Open a result for the offender's photo, registered address, physical description, and offense/conviction details.
4. Optionally set a location-based email alert (requires an email address).
5. Pivot: a registered `address` feeds property/neighbor OSINT; the `image` feeds reverse-image/face search; the offense details feed court-record lookups — and confirm the hit on the official state registry or NSOPW before relying on it.

## Inputs → Outputs
- **In:** `name` or `address` (US)
- **Out:** matching registrant records — registered `address`, `image` (photo), `physical-description`, and offense details
- **Empty/negative result looks like:** no match means no registrant by that name/at that location in the aggregated data — it is not proof of a clean record (data lags, and non-registerable offenses aren't listed); verify against the state registry.

## Gotchas & OpSec
- **Legal gate:** sex-offender registry data is published for public safety; using it to harass, intimidate, or discriminate against a registrant is illegal in most US jurisdictions. Keep use investigative and lawful.
- Third-party aggregator — it can lag or mis-map official data; always confirm a hit on the authoritative state registry or the federal NSOPW site.
- US-only; names are common, so corroborate a match with photo + address before concluding identity.

## Overlaps ("do both")
- Complements the federal NSOPW (nsopw.gov) and individual state registries — Family Watchdog is the fast one-search front end, and the official sources are the authority you confirm against.

## Trust & verifiability
`trust: community` — it faithfully aggregates official, public state-registry data on a daily refresh, but as a third party it can carry lag or mapping errors, so treat it as a lead generator and verify decisive findings at the government source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | familywatchdog-sex-offender-search |
| category | public-records |
| selectorsIn → selectorsOut | name, address → address, image, physical-description |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

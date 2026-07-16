---
id: sex-offender-search
name: Sex Offender Search
description: Use when you have a `name` and want to check US state sex-offender registries — returns registry listings with photo, offense, registered address, and DOB via a directory of all 50 states plus DC.
url: https://www.blackbookonline.info/usa-sex-offenders.aspx
category: public-records
path:
- public-records
bestFor: One-stop directory into every US state sex-offender registry for a name/address check.
selectorsIn:
- name
- address
selectorsOut:
- name
- dob
- address
- image
- physical-description
status: live
pricing: free
costNote: Free public-records portal; the state registries it links to are also free government sites. No account.
opsec: passive
opsecNote: Passive — you query public government registries, not the subject. Registrants are not notified of searches. The portal (Black Book Online) and each state site log traffic; use a clean browser if you want to avoid attributing the query.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known free public-records aggregator (Black Book Online, by investigator Robert Scott) that links to official state registries; the portal is a directory, so trust the linked government registry, not the portal, as the source of truth.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Black Book Online sex offender search
- blackbookonline.info
tags:
- court
- inmate
- sex-offender-registry
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- arrest-warrants
- black-book-online-criminal-search
- criminal-search-criminal-records-by-state-and
- free-aviation-records-black-book-online
- jail-records
- nationwide-county-court-records-by-state-and
- property-search-public-records-by-state
---

# Sex Offender Search

> A free directory that funnels you into the official US sex-offender registry for any of the 50 states plus DC — one launch point for a name or address check against public registry data.

## When to use
You have a `name` (and ideally a state or `address`) and need to check whether the subject appears on a US sex-offender registry, or you want to see who is registered near a known address. Registry records carry a photo, offense, and a registered `address` — high-value corroboration in a missing-person or safeguarding context. This portal saves you from remembering each state's registry URL.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.blackbookonline.info/usa-sex-offenders.aspx.
2. Pick the relevant state from the alphabetical list (or the national DOJ NSOPW if you don't know the state).
3. On the state registry, search by `name` (or browse by `address`/ZIP where offered).
4. Read the record: photo (`image`, `physical-description`), offense, `dob`, and registered `address`.
5. Match on photo + `dob` + name, then pivot: the registered address is a location lead; the photo feeds face/reverse-image tools.

## Inputs → Outputs
- **In:** `name` (or `address`/ZIP for area search)
- **Out:** registry listing — `name`, `dob`, `image`, `physical-description`, offense, registered `address`
- **Empty/negative result looks like:** no match in that state's registry. This is NOT proof of no record nationwide — check other states where the subject has lived, or use the national NSOPW search; registries are per-state.

## Gotchas & OpSec
- The portal is just a set of links; the actual search and data quality live on each state's official site. Cite the state registry, not Black Book Online.
- Registry data can lag (address changes, compliance status) and formats vary wildly by state.
- Name collisions happen; always confirm with the photo and `dob`.
- Passive and free; no login or captcha on the portal, though some state sites add their own captcha/terms click-through.

## Overlaps ("do both")
- Pairs with `[[state-and-county-jail-inmate-locators]]` and `[[kansas]]` — registries show community-registered offenders; inmate locators show those currently incarcerated. Check both for a full picture.
- The registered address feeds people-search/address tools like `[[searchpeoplefree]]`.

## Trust & verifiability
`trust: community` — the portal itself is an unofficial aggregator, but it links to authoritative state government registries. Verify and cite the state registry record directly; treat the portal purely as a convenient index, and heed its disclaimer that results aren't FCRA consumer reports.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sex-offender-search |
| category | public-records |
| selectorsIn → selectorsOut | name, address → name, dob, address, image, physical-description |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

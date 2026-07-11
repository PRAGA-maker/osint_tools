---
id: canadian-obituaries
name: Canadian Obituaries
description: Use when you have a `name` and want to check whether a subject (or relative) has a Canadian death/obituary notice — returns death confirmation, funeral home, location, and surviving family.
url: http://www.canadianobituaries.com
category: public-records
path:
- public-records
bestFor: Confirming a death and pulling funeral-home, location, and family (associate) details from Canadian obituary notices.
selectorsIn:
- name
selectorsOut:
- name
- address
- associate
status: live
pricing: free
costNote: Free to browse and search published notices; no account required.
opsec: passive
opsecNote: Reading published obituary notices is passive and non-attributable; these are intentionally public tributes. No sock puppet needed. Handle findings with sensitivity given the bereavement context.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An obituary publishing platform fed by funeral homes; notices are genuine but family-authored, and coverage skews to recent notices from participating homes rather than a complete national death index.
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
aliases:
- CanadianObituaries.com
tags:
- toddington
- curated-directory
- obituary
- genealogy
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# Canadian Obituaries

> A Canadian obituary-notice platform where funeral homes publish death notices — use it to confirm a subject has died and to harvest the funeral home, town, and named surviving relatives.

## When to use
You have a `name` and need to resolve the "are they deceased?" branch of a locate case, or you're building a family tree and want the relatives an obituary names. An obituary is a dense lead: it confirms death, pins a location and funeral home, and typically lists surviving spouse/children/siblings (`associate`s) by name — often the fastest route to living relatives to contact. Reach for it early when a Canadian subject's trail simply ends.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.canadianobituaries.com.
2. Use the header search for the subject's `name`, or browse by region (e.g. GTA, BC, Durham) if you know where they lived.
3. Open a matching notice: read the death date, funeral home, town, and the list of named relatives.
4. Cross-check the town/dates against your subject to confirm it's the right person (common names need care).
5. Pivot: named relatives (`associate`s) become new search subjects; the funeral home/town anchors `geolocation`; a confirmed death closes the locate or redirects to next-of-kin.

## Inputs → Outputs
- **In:** `name`
- **Out:** `name` (deceased), `address` (town/funeral home locale), `associate` (surviving family)
- **Empty/negative result looks like:** no notice found — the person isn't deceased, died outside this platform's coverage, or the notice was placed elsewhere (local paper, a different site). Absence is NOT proof of life; check other obituary/death sources.

## Gotchas & OpSec
- Human-in-the-loop: none.
- Coverage is **recent notices from participating Canadian funeral homes**, not a complete national death register — pair with other obituary aggregators and provincial vital-records where available.
- Family-authored notices can contain errors or omit relatives; corroborate names.
- OpSec: passive; handle bereavement data sensitively.

## Overlaps ("do both")
- Pairs with other obituary aggregators and genealogy/death-record tools — each funeral home publishes to different platforms, so run several to avoid missing a notice.

## Trust & verifiability
`trust: community` — genuine funeral-home-sourced notices, but not an authoritative death index and family-written; confirm identity by location/date and corroborate relatives.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canadian-obituaries |
| category | public-records |
| selectorsIn → selectorsOut | name → name, address, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: cloob-com
name: Cloob.com
description: Historical reference only — Iran's "Facebook" people search, permanently shut down in 2021; returns nothing today, so route to archives or other Iran-focused sources.
url: https://www.cloob.com/profile/search/index
category: people-search
path:
- people-search
bestFor: Historical reference only — former Iranian social-network people search (defunct since 2021).
selectorsIn:
- name
selectorsOut:
- name
- social-profile
status: down
pricing: free
costNote: The service was free while it operated; it has been deactivated since August 2021 and no longer functions.
opsec: passive
opsecNote: The live site is gone, so there is nothing to query. If you find a mirror or archive, treat it as historical data only. Do not enter targets into any current page claiming to be Cloob — it is not the operational network.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Cloob was a genuine, major Persian-language social network (peak ~2M users), but it was deactivated on 6 August 2021 after years of censorship battles; it is no longer a live source.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- wayback-machine
- yandex-people-search
aliases:
- Cloob
- cloob.com
- Iranian Facebook
tags:
- Universal Contact Search and Leaks Search
- iran
- defunct
source: cyb-detective
lastVerified: '2026-07-14'
enrichment: full
---

# Cloob.com

> Iran's long-running "answer to Facebook/Orkut" and its people search — permanently deactivated in 2021. Kept here so an agent recognises it and pivots to archives or other Iran-focused sources.

## When to use
Never, as a live tool — but you'll see Cloob cited in older Iran-focused OSINT lists as a way to search Persian-language profiles by name. Cloob launched in the mid-2000s, peaked at around two million Iranian users, and was deactivated on 6 August 2021 after repeated government blocking and censorship pressure. Recognise the reference; for Iranian subjects, work archives and other sources instead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Do not rely on cloob.com — the network is shut down and its people search no longer functions.
2. For historical Cloob content, check the Wayback Machine for archived profile/search pages (fragmentary at best).
3. For living Iranian-subject OSINT, pivot to Persian-language searches on mainstream platforms (Instagram, Telegram) and Yandex/Google dorks, plus breach/leak datasets.

## Inputs → Outputs
- **In:** `name` (historically, Persian-language)
- **Out:** nothing today; historically a profile `social-profile`/`name` match
- **Empty/negative result looks like:** the site failing to load, redirecting, or showing a shutdown/parked state — the expected condition, not a temporary outage.

## Gotchas & OpSec
- `status: down` — this is a tombstone; don't spend a step trying to query it.
- Any page currently presenting itself as a working Cloob is not the original network; don't enter target data.
- Archived copies are partial and dated — treat as historical, not current.

## Overlaps ("do both")
- Use `[[wayback-machine]]` for any archived Cloob pages, and `[[yandex-people-search]]` plus Persian-language dorking for living Iranian-subject leads that Cloob once would have covered.

## Trust & verifiability
`trust: unverified` — historically a real, significant platform, but defunct since 2021, so it cannot be treated as a current source. Rely on archives and other Iran-focused tools instead.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cloob-com |
| category | people-search |
| selectorsIn → selectorsOut | name → name, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

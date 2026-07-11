---
id: rip-ie
name: RIP.ie
description: Use when you have a `name` (and rough locality) of someone who may have died in Ireland and want the death/funeral notice — returns death notices with locality, family members (mourners) and funeral detail.
url: https://rip.ie/
category: public-records
path:
- public-records
bestFor: Confirming an Irish death and harvesting the family/associate network and locality from the published notice.
selectorsIn:
- name
- address
selectorsOut:
- name
- address
- associate
- dob
status: live
pricing: free
costNote: Free to search and read notices; no account required.
opsec: passive
opsecNote: Reading a public death notice does not contact or notify anyone. The notices are voluntarily published by families, but they contain living relatives' names — handle that PII responsibly and within your legal basis. Use a sock-puppet browser if you'd rather not log searches against your IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: RIP.ie is the dominant, long-established death-notice service in Ireland used by funeral directors nationally; notices are family/funeral-director sourced and reliable, though names and localities are as families choose to publish them.
missingPersonsRelevance: high
coverage:
- ie
auth: none
api: false
localInstall: false
registration: false
aliases:
- rip.ie
- Irish death notices
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- death-notices
- obituaries
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# RIP.ie

> Ireland's national death-notice site — the fastest authoritative way to confirm someone died in Ireland and to map their family, locality and funeral timeline from the published notice.

## When to use
You have a `name` (ideally with a county/town) and need to establish whether an Irish subject has died, or you want to exploit a known death to expand the family graph. Irish death notices name the deceased's locality and, crucially, list surviving relatives ("survived by … predeceased by …") and funeral arrangements — a rich `associate` map and a strong locality anchor for genealogy and missing-person work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://rip.ie/ and use the search (by `name`, and filter by county/town).
2. Open the matching notice; confirm identity via locality, age, and family detail.
3. Extract the network: spouse, children, siblings, grandchildren named as mourners are all `associate` leads; the address/parish gives locality; funeral home and dates give a timeline.
4. Note age/"in their 80th year" phrasing to approximate a `dob`.
5. Pivot: relatives' names feed people-search and social lookups; the locality narrows electoral-roll/genealogy searches; the funeral home can corroborate the death.

## Inputs → Outputs
- **In:** `name` (+ county/town for disambiguation)
- **Out:** confirmed death, deceased's locality/`address`, family `associate` network, approximate `dob`/age, funeral timeline
- **Empty/negative result looks like:** no notice — the person is alive, died abroad, or the family didn't publish (some don't). Absence is NOT proof of life; cross-check other death sources.

## Gotchas & OpSec
- Not every Irish death is posted (family choice), and pre-2000s deaths largely predate the site — absence proves nothing.
- Notices name living relatives; treat that PII carefully and lawfully.
- Common names need the county/town filter to disambiguate; verify with age/family detail.

## Overlaps ("do both")
- Pairs with the Irish civil registration index (irishgenealogy.ie), `[[findmypast-co-uk]]` and general genealogy sources — RIP.ie gives the recent notice and family network; official BMD indexes give the registered record.

## Trust & verifiability
`trust: trusted` — the de facto national death-notice platform used by Irish funeral directors; notices are sourced from families/undertakers and are reliable, limited only by what families choose to publish.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rip-ie |
| category | public-records |
| selectorsIn → selectorsOut | name, address → name, address, associate, dob |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

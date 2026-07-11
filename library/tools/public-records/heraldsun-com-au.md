---
id: heraldsun-com-au
name: Herald Sun Tributes
description: Use when you have a `name` of someone who may have died in Victoria, Australia and want the death/funeral notice — returns published tributes with locality, family names and funeral detail.
url: https://www.heraldsun.com.au/tributes
category: public-records
path:
- public-records
bestFor: Finding Australian (Victoria/Melbourne) death and funeral notices to confirm a death and map the family network.
selectorsIn:
- name
selectorsOut:
- name
- associate
- address
status: live
pricing: freemium
costNote: The tributes/death-notices section is generally free to search and read; the wider Herald Sun news site is largely subscriber-paywalled. Notices are placed (paid) by families/funeral directors.
opsec: passive
opsecNote: Reading a published tribute contacts no one and leaves no trace with any subject. Notices are voluntarily placed by families and name living relatives — handle that PII responsibly and lawfully. Use a sock-puppet browser if you'd rather not log searches.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Herald Sun is a major established Melbourne newspaper (News Corp Australia); its tributes are funeral-director/family sourced and reliable, limited to what families choose to publish. Australian death notices commonly aggregate here and on tributes.com.au.
missingPersonsRelevance: high
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
aliases:
- Herald Sun death notices
- heraldsun.com.au tributes
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- death-notices
- obituaries
- australia
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Herald Sun Tributes

> The death-notice and tribute section of Melbourne's Herald Sun — a fast way to confirm a Victorian death and pull the family network and funeral timeline from the notice.

## When to use
You have a `name` (ideally with a Melbourne/Victoria connection) and need to establish whether an Australian subject has died, or want to exploit a known death to expand the family graph. Placed notices name the deceased's locality and surviving relatives ("loved [spouse/children]…") and give funeral arrangements — a rich `associate` map and a locality anchor for genealogy and missing-person work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.heraldsun.com.au/tributes and search by `name`; filter/browse by date where possible.
2. Open the matching notice; confirm identity via locality, age and family detail.
3. Extract the network: spouse, children, siblings and grandchildren named as mourners are `associate` leads; the suburb/parish gives locality; funeral home and dates give a timeline.
4. Cross-check the same notice on tributes.com.au / other News Corp mastheads (notices often syndicate).
5. Pivot: relatives feed people-search and social lookups; the funeral home can corroborate the death; locality narrows Australian electoral/genealogy searches.

## Inputs → Outputs
- **In:** `name` (+ Victoria/Melbourne locality for disambiguation)
- **Out:** confirmed death, locality/suburb (`address`), family `associate` network, funeral timeline
- **Empty/negative result looks like:** no notice — the person is alive, died elsewhere/interstate, or the family didn't place a notice (many don't). Absence is NOT proof of life; check interstate mastheads and official BDM indexes.

## Gotchas & OpSec
- Not every death is published (family choice) and coverage skews Victoria/Melbourne — check other state newspapers for elsewhere.
- Notices name living relatives; treat that PII carefully and lawfully.
- Common names need the locality/date filter; verify with age/family detail.

## Overlaps ("do both")
- Pairs with tributes.com.au, other News Corp obituary pages and the state BDM (Births Deaths Marriages) indexes — the newspaper gives the recent notice and family network; official registries give the registered death record.

## Trust & verifiability
`trust: trusted` — a major established newspaper's notices, sourced from families/funeral directors; reliable, limited only by what families choose to publish and its Victorian skew.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | heraldsun-com-au |
| category | public-records |
| selectorsIn → selectorsOut | name → name, associate, address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

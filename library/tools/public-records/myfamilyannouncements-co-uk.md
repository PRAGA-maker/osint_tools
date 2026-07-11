---
id: myfamilyannouncements-co-uk
name: My Family Announcements (UK)
description: Use when you have a `name` and want UK newspaper family notices — births, deaths, marriages, in memoriam — returns published notices with dates, places, and named relatives.
url: https://www.myfamilyannouncements.co.uk/national
category: public-records
path:
- public-records
bestFor: Searching UK regional/national newspaper family notices (deaths, births, marriages, in memoriam) by name.
selectorsIn:
- name
- address
selectorsOut:
- name
- associate
- address
- dob
status: live
pricing: free
costNote: Searching and reading published notices is free. Placing a notice is a paid newspaper service.
opsec: passive
opsecNote: Passive lookup of publicly published newspaper notices — no subject is contacted or notified. Ordinary browsing hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Aggregator of notices submitted by families to UK regional newspapers (Reach/DC Thomson titles). The notices themselves are as reliable as what the family submitted; coverage depends on which papers participate.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- myfamilyannouncements.co.uk
- Family Announcements
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# My Family Announcements (UK)

> The aggregated family-notices board for dozens of UK newspapers — a searchable feed of births, deaths, marriages, and in-memoriam notices that often name the wider family.

## When to use
You have a `name` and want to confirm a life event or find relatives: a death/funeral notice can confirm a death and list surviving family, funeral director, and place; a marriage or in-memoriam notice ties people together. High value in missing-person and next-of-kin work because notices frequently name spouses, children, and siblings alongside dates and localities.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.myfamilyannouncements.co.uk/national (or a specific regional paper's board).
2. Search by surname/`name`; narrow by notice type (death, birth, marriage, in memoriam) and region where available.
3. Read matching notices: the deceased/celebrant's name, dates, town, and — critically — named relatives, funeral details, and sometimes an `address` or funeral director.
4. Note the network spans many regional titles, so try both the national board and the relevant local paper.
5. Pivot: named relatives become `associate` leads; a funeral director/date can confirm a death; localities feed records lookups.

## Inputs → Outputs
- **In:** `name` (surname), optionally region/`address`
- **Out:** family notices naming the person and `associate`s (relatives), dates (approx `dob`/death), places, funeral details
- **Empty/negative result looks like:** no notices — the family may not have placed one, or it ran in a non-participating paper; absence is not evidence of no event.

## Gotchas & OpSec
- Coverage gap: only notices placed in participating newspapers appear; many events are never announced here.
- Self-submitted: content reflects what the family wrote — usually accurate but not an official record.
- OpSec: passive; reading public notices touches nobody.

## Overlaps ("do both")
- Pairs with `[[thegazette-co-uk]]` (official deceased-estates/probate notices) and `[[curious-fox-united-kingdom]]` — newspaper notices name the family, the Gazette gives the legal/probate side, and Curious Fox connects you to researchers who know them.

## Trust & verifiability
`trust: community` — an aggregator of family-submitted newspaper notices; the notices are usually reliable primary statements from relatives but are not official vital records, so corroborate dates against the register.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | myfamilyannouncements-co-uk |
| category | public-records |
| selectorsIn → selectorsOut | name → name, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

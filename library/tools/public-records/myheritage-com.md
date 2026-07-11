---
id: myheritage-com
name: MyHeritage
description: Use when you have a `name` and want genealogical records and family-tree links — relatives, dates, places — to map a person's family network — returns name, associate (relatives), dob and address.
url: https://www.myheritage.com/
category: public-records
path:
- public-records
bestFor: Building a family/relative network and finding birth/marriage/death and census records from a name.
selectorsIn:
- name
selectorsOut:
- name
- associate
- dob
- address
status: live
pricing: freemium
costNote: Free to register, search, and build/view trees; viewing many historical record images and using DNA/record matches requires a paid subscription. Search hits (names, dates, record existence) are visible before you pay.
opsec: passive
opsecNote: Searching records/trees does not notify anyone living. Be careful with living people — MyHeritage restricts and privacy-masks living individuals, and building a tree from an account ties research to you. Use an investigation account, not a personal genealogy account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A major commercial genealogy platform. Historical records are reliable primary/secondary sources; user-submitted family trees are crowd data and can contain errors — verify tree claims against actual records.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- MyHeritage
- myheritage.com
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- family-tree
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# MyHeritage

> A major genealogy platform — search a name across historical records and user family trees to reconstruct a person's relatives, dates, and places.

## When to use
You have a `name` and want to map the person's family network and life-event data: relatives (`associate`s), dates of birth/death (`dob`), and historical addresses/places, drawn from census, birth/marriage/death, immigration, and other records plus crowd-sourced family trees. Especially useful for older subjects, deceased individuals, and establishing family relationships that open new lines of inquiry (next-of-kin, maiden names, siblings).

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a (investigation-dedicated) account and log in at https://www.myheritage.com/.
2. Use the record search (SuperSearch) and enter the `name` with any known year/place to narrow.
3. Review hits: matching records and tree profiles show names, dates, places, and linked relatives even before you pay to open full record images.
4. Follow relative links to expand the family graph; note maiden names and DOBs.
5. Pivot: relatives become new subjects and next-of-kin leads; a DOB/place anchors other records; a historical address feeds property/electoral sources.

## Inputs → Outputs
- **In:** `name` (optionally with year/place)
- **Out:** `name`, `associate` (relatives/family), `dob`, historical `address`/places
- **Empty/negative result looks like:** no record/tree matches — common for younger living people (privacy-masked) or names outside the digitised record set; not proof of no family record.

## Gotchas & OpSec
- **Living people are restricted/masked** — MyHeritage is strongest for historical and deceased individuals; expect little on a young living subject.
- User-submitted trees can be wrong — verify relationships against actual records before relying on them.
- Human-in-the-loop: account required; full record images are paywalled.

## Overlaps ("do both")
- Pairs with FamilySearch/Ancestry and official BMD registers — genealogy platforms overlap unevenly, so cross-search names across several, and confirm crowd-tree claims against primary registers.

## Trust & verifiability
`trust: community` — a large commercial platform mixing authoritative records with crowd-sourced trees. Weight the records highly and the trees as leads to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | myheritage-com |
| category | public-records |
| selectorsIn → selectorsOut | name → name, associate, dob, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |

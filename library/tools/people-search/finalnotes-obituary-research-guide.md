---
id: finalnotes-obituary-research-guide
name: FinalNotes Obituary Research Guide
description: Use when you have a `name` of a possibly-deceased person and want a methodology plus source list for finding and verifying their obituary — points to genealogy/obituary sources returning dob, address, and associate (kin) leads.
url: https://www.finalnotes.page/obituary-research-guide/
category: people-search
path:
- people-search
bestFor: A how-to guide and curated source list for obituary/death research — teaches the workflow, not a database itself.
selectorsIn:
- name
selectorsOut:
- dob
- address
- associate
- name
status: live
pricing: free
costNote: Free educational guide; the external sources it recommends (FamilySearch, Find a Grave, newspaper archives) have their own free/paid tiers.
opsec: passive
opsecNote: Reading the guide is inert. Downstream obituary/genealogy searches are also passive lookups of published records; nobody is notified. The subject here is typically deceased, but living relatives named in obituaries are real people — handle their data with care.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An independent educational resource/guide, not a records database. Value is in its methodology and source pointers; verify every downstream source on its own.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- FinalNotes obituary guide
tags:
- people-investigations
- obituary
- genealogy
- deceased
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# FinalNotes Obituary Research Guide

> A methodology guide and curated source hub for obituary research — how to find, read, and verify an obituary, and where the obituaries actually live.

## When to use
You have a `name` and suspect the person may be deceased (a missing-persons trail going cold, a break in records, an age that suggests it). An obituary is one of the richest single documents in people research: it typically names the deceased's `dob`/death date, last town (`address`), and a web of `associate` relatives (spouse, children, siblings). This guide teaches the search-and-verify workflow and lists where to look.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read the guide's "six steps" — collect identity details, run web/newspaper searches, check genealogy indexes and library/cemetery sources, then document and cross-verify.
2. Follow its source pointers (FamilySearch, Find a Grave, newspaper archives, funeral-home pages, cemetery records) with your subject's `name` + approximate place/era.
3. Cross-check any obituary against a second source (death certificate, cemetery record, census) before trusting it — the guide stresses this.
4. Pivot: relatives named in the obituary become new subjects for people-search; the last town narrows address history; the death date closes or reframes a timeline.

## Inputs → Outputs
- **In:** `name` (plus approximate location/era)
- **Out:** pointers to sources that yield `dob`/death date, last-known `address`, and `associate` (next-of-kin) leads
- **Empty/negative result looks like:** no matching obituary — common for private families, recent deaths not yet indexed, or someone still living. Absence is not proof of death or of life.

## Gotchas & OpSec
- It's a guide, not a search box — you still do the searching in the sources it names.
- Obituaries can contain errors or be written by grieving family; corroborate names/dates.
- OpSec: passive throughout; but relatives listed are living people — treat their details responsibly.

## Overlaps ("do both")
- Pairs with dedicated obituary/cemetery databases (Find a Grave, newspapers.com) and general people-search — this guide tells you the method, those tools return the records.

## Trust & verifiability
`trust: community` — an independent educational guide. Sound methodology, but it holds no records itself; reliability comes from the primary sources it directs you to, each of which you verify independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | finalnotes-obituary-research-guide |
| category | people-search |
| selectorsIn → selectorsOut | name → dob, address, associate, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

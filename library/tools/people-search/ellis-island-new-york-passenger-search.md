---
id: ellis-island-new-york-passenger-search
name: Ellis Island New York Passenger Search
description: Use when you have a historical immigrant's `name` and want their Port of New York / Ellis Island arrival record — returns arrival date, ship, port of origin, age, and fellow passengers.
url: https://www.libertyellisfoundation.org
category: people-search
path:
- people-search
bestFor: Finding an immigrant ancestor's Ellis Island arrival manifest (1892–1957) by name.
selectorsIn:
- name
selectorsOut:
- name
- dob
- associate
- address
status: live
pricing: free
costNote: The Statue of Liberty-Ellis Island Foundation's Arrival Records search is free to use; a free account lets you save records, and physical/framed copies are sold, but searching costs nothing.
opsec: passive
opsecNote: Passive and historical — you search a genealogical archive of century-old arrival manifests, not any living person's data. No target is contactable or notified.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official Statue of Liberty-Ellis Island Foundation database, digitised from the Port of New York passenger manifests; authoritative for what the original manifest recorded (subject to transcription errors).
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Ellis Island records
- Statue of Liberty-Ellis Island Foundation passenger search
- libertyellisfoundation.org
tags:
- toddington
- curated-directory
- people-search
- genealogy
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Ellis Island New York Passenger Search

> The official free search over the Port of New York / Ellis Island arrival manifests (1892–1957) — enter an immigrant's name to recover their arrival record, ship, origin, and travelling companions.

## When to use
You are doing genealogical or historical work and have an immigrant ancestor's `name` (and roughly when they arrived in the US via New York). The arrival manifest ties a person to a date, a ship, a place of origin, an age, and — crucially — the family members and companions listed alongside them, which extends a family tree and confirms relationships. This is a deep-history tool, not for living-subject location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.libertyellisfoundation.org (redirects to statueofliberty.org) and go to the Arrival Records Collection / passenger search.
2. Enter the immigrant's `name`; use variant spellings and wildcards — names were often transcribed phonetically from handwritten manifests.
3. Narrow by approximate arrival year, age, or origin if you have them.
4. Open a matching record to read: arrival date, ship name, port of departure, age (→ approximate `dob`), and other passengers on the manifest (`associate`s — often family).
5. Pivot: the manifest image, ship, and origin feed genealogy sites (FamilySearch, ancestry); companion names extend the family network; origin gives a `geolocation`/`address` lead in the old country.

## Inputs → Outputs
- **In:** `name` (+ optional arrival year/age/origin)
- **Out:** arrival date, ship, port of origin, age (`dob` estimate), fellow passengers (`associate`), sometimes last residence (`address`)
- **Empty/negative result looks like:** no matching manifest — the person may have arrived via a different port (Boston, Baltimore, Philadelphia), before 1892/after 1957, or under a differently-transcribed name. Absence isn't proof they didn't immigrate.

## Gotchas & OpSec
- Scope is the Port of New York (Ellis Island / Castle Garden era) only — other US ports need their own datasets.
- Transcription errors are rampant (handwriting, phonetic spelling); always try name variants and check the manifest image, not just the index.
- Records are historical (pre-1957); this is genealogy, not a way to find a living person's current whereabouts.
- Fully passive and free; a free account only adds save/annotate features.

## Overlaps ("do both")
- Pairs with genealogy/obituary sources like `[[canadian-obituaries]]` and family-tree databases — arrival records anchor the immigration event; those fill in births/deaths/marriages.
- Companion names feed general people-search for later generations.

## Trust & verifiability
`trust: trusted` — it is the official Foundation database digitised from the primary passenger manifests, authoritative for what the manifest recorded. The main caveat is transcription accuracy: verify against the scanned manifest image and corroborating genealogical records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ellis-island-new-york-passenger-search |
| category | people-search |
| selectorsIn → selectorsOut | name → name, dob, associate, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

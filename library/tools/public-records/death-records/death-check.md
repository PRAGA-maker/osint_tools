---
id: death-check
name: DeathIndexes.com
description: Use when you have a `name` (and rough US state/era) and want to check whether the person has died — returns links to state/county death indexes, obituaries, and SSDI resources.
url: https://www.deathindexes.com/
category: public-records
path:
- public-records
- death-records
bestFor: A US-wide directory routing you to the right online death index, obituary, or probate source by state and county.
selectorsIn:
- name
selectorsOut:
- dob
- name
- associate
status: live
pricing: free
costNote: The directory is free; some linked destination sites (commercial genealogy providers) may paywall the actual records.
opsec: passive
opsecNote: Browsing a link directory and public death indexes is read-only and never contacts any living subject. Some linked providers may require their own free account; the deceased has no privacy interest, but surviving relatives named in obituaries are living people — handle their data carefully.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running, well-regarded genealogy link directory (Joe Beine); it curates links to primary sources rather than hosting records itself.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- findagrave
- ssdi-search
- legacy-com-obituaries
- online-searchable-death-indexes-and-records-united-states
aliases:
- deathindexes.com
- Death Indexes
tags:
- death-records
- obituary
- genealogy
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# DeathIndexes.com

> A curated directory of online US death records — organized by state, county, and major city — that points you to the correct death index, obituary archive, SSDI, or probate resource for a given person.

## When to use
You have a `name` and need to establish whether the person is deceased, or find their death date/place — a critical branch in any missing-persons or people-tracing workflow, since a death record explains why a trail ends and unlocks obituaries that name relatives. DeathIndexes doesn't hold records itself; it routes you to the right primary source (state vital-records index, county records, newspaper obituary archive, Social Security Death Index) for the jurisdiction where the person likely died.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.deathindexes.com/ and pick the US state (then county/city) where the subject lived or may have died.
2. Follow the curated links to the relevant death index, obituary source, SSDI, or probate/cemetery resource.
3. Search that destination by `name` (add approximate year/age to disambiguate common names).
4. On a hit, capture the death date, place, and — from obituaries — surviving relatives (`associate`) and biographical detail confirming identity.
5. Pivot: relatives named in an obituary become new people-search targets; a confirmed death date closes or redirects the investigation.

## Inputs → Outputs
- **In:** `name` (+ rough US state/era to choose the right index)
- **Out:** `dob`/death date, `name` confirmation, `associate` (relatives from obituaries), place of death
- **Empty/negative result looks like:** no matching record in the chosen index — the person may be alive, died elsewhere, or the index doesn't cover that era/jurisdiction. Absence is not proof the person is alive; try adjacent states and the SSDI.

## Gotchas & OpSec
- It's a *directory of links*, not a database — coverage and cost depend on each destination site; some genealogy providers paywall the actual record.
- Indexes vary wildly by state/era; a gap means "not indexed here," not "did not die."
- OpSec: **passive** — but obituaries name living relatives; treat their details responsibly.

## Overlaps ("do both")
- Pairs with `[[findagrave]]` (cemetery/burial records with family links) and `[[ssdi-search]]` — each covers different deaths, so run the name through all three before concluding a person is alive or unfound.

## Trust & verifiability
`trust: trusted` — a well-established, carefully-maintained genealogy directory; the authoritativeness of any given record rests with the primary source it links to, which you should read directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | death-check |
| category | public-records |
| selectorsIn → selectorsOut | name → dob, name, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

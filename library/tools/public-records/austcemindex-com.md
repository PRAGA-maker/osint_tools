---
id: austcemindex-com
name: austcemindex.com
description: Use when you have a `name` of someone buried in Australia (esp. regional NSW) and want their cemetery/headstone record — returns headstone `image`, dates (`dob`), cemetery `address`, and family `associate`s.
url: https://www.austcemindex.com/
category: public-records
path:
- public-records
bestFor: Free search of Australian cemetery inscriptions and headstone photos to confirm a burial and extract family/date details.
selectorsIn:
- name
selectorsOut:
- name
- dob
- address
- associate
status: live
pricing: free
costNote: Free to search and view; a volunteer-driven index with no account required.
opsec: passive
opsecNote: Searching a public genealogy index concerning deceased people is passive and notifies no one. No login is required; queries are ordinary web requests.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: The Australian Cemeteries Index — a large volunteer-contributed database (1.7M+ records, 1,100+ cemeteries) strongest in regional NSW; coverage is partial and contributor-dependent.
missingPersonsRelevance: high
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
aliases:
- Australian Cemeteries Index
- austcemindex
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# austcemindex.com

> The Australian Cemeteries Index — a free, volunteer-built search of headstone inscriptions and photos across 1,100+ Australian cemeteries (strongest in regional NSW).

## When to use
You are tracing a deceased Australian subject or ancestor and want to confirm a burial, read the headstone inscription, or extract family details. Headstones commonly list multiple relatives on one plot (`associate`) and give birth/death dates (`dob`), and this index adds photos — useful for closing out a death, building a family tree, or corroborating an identity in Australian genealogy work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.austcemindex.com/ and use the name/cemetery search.
2. Enter the `name` (try surname variants); optionally narrow by cemetery or region.
3. Open a matching record: read the `name`, dates (`dob`/death), cemetery/location (`address`), the headstone `image`, and any other names on the memorial (`associate`).
4. Note the strong regional-NSW skew — a miss may reflect coverage, not absence of a grave.
5. Pivot: family names feed further genealogy searches; confirmed dates feed BDM/obituary records; the cemetery feeds a location.

## Inputs → Outputs
- **In:** `name` (+ optional cemetery/region)
- **Out:** `name`, dates (`dob`/death), cemetery `address`, headstone `image`, family `associate`s
- **Empty/negative result looks like:** no match — coverage is partial and volunteer-dependent (best in regional NSW, expanding elsewhere), and unmarked graves have no inscription. A null means "not indexed here," not "no grave exists."

## Gotchas & OpSec
- Coverage is uneven — regional NSW is strong, other states thinner; cross-check other indexes before concluding.
- Volunteer transcriptions can contain errors; verify against the photo where available.
- Index of inscriptions/photos, not an official burial register.

## Overlaps ("do both")
- Pairs with `[[findagrave]]`/`[[billiongraves]]` and Australian state BDM registries — the global grave sites and official registries cover records this index may lack, and vice versa.

## Trust & verifiability
`trust: community` — a credible, well-used volunteer index; verify individual entries against the headstone photo and official BDM records for precision.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | austcemindex-com |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, address, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

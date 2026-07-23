---
id: rupep
name: RuPEP
description: Use when you have a `name` from Russia/Belarus/Central Asia and want to check political exposure — returns positions, family, and business `associate` links.
url: https://rupep.org/en/
category: financial-crypto
path:
- financial-crypto
bestFor: Profiling politically exposed persons (PEPs) and their networks across Russia, Belarus, Kazakhstan and Kyrgyzstan.
selectorsIn:
- name
- employer-org
selectorsOut:
- associate
- employer-org
- dob
status: live
pricing: free
costNote: Free to search and read profiles; structured data is also available as a dataset/API (used by OpenSanctions and others).
opsec: passive
opsecNote: You read a public database; the subject is not notified and no query is tied to a target beyond RuPEP's own logs. Downloading the dataset and searching locally leaks nothing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Well-regarded investigative PEP database, referenced by Bellingcat and integrated into OpenSanctions; sources are documented per profile.
missingPersonsRelevance: low
coverage:
- ru
- by
- kz
- kg
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- RuPEP
- rupep.org
- Russian PEP database
tags:
- pep
- politically-exposed-persons
- due-diligence
- bellingcat-toolkit
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# RuPEP

> A curated database of politically exposed persons in Russia, Belarus and Central Asia — and, crucially, the family and business networks around them.

## When to use
You have a `name` (or `employer-org`) connected to Russia, Belarus, Kazakhstan, or Kyrgyzstan and need to know whether the person is politically exposed, what offices/roles they hold or held, and — the real value — who they're connected to: family members, business partners, and affiliated companies. That relationship graph makes RuPEP strong for tracing an `associate` network around a subject, which is directly useful when a person of interest is linked to a PEP. Relevance to people-tracing is medium (network expansion, identity confirmation via `dob`/roles).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://rupep.org/en/ (English toggle available; underlying data is Russian/local-language).
2. Search a `name` — try Cyrillic and transliterated spellings, since names transliterate many ways.
3. Open the profile and read: positions held (with dates), `dob`, related persons (family, associates) and related companies — each typically linked to their own profiles.
4. Pivot: click through related `associate`s and `employer-org`s to expand the network; feed names into people-search and company registries; cross-check designations against sanctions lists (OpenSanctions, OFAC).

## Inputs → Outputs
- **In:** `name` or `employer-org` (Russia/Belarus/Central Asia)
- **Out:** PEP status, positions/roles, `dob`, related `associate`s (family/business), related `employer-org`s
- **Empty/negative result looks like:** no profile — the person isn't in RuPEP's PEP scope; this doesn't rule out political exposure elsewhere, and common names may need `dob`/role to disambiguate.

## Gotchas & OpSec
- **Transliteration** is the main pitfall — search Cyrillic and multiple Latin spellings.
- Scope is regional (RU/BY/KZ/KG) and focused on *politically exposed* persons — an ordinary individual won't appear.
- Relationship data is curated but can lag real-world changes; note profile source dates.
- OpSec: passive public reading.

## Overlaps ("do both")
- Feeds and is fed by OpenSanctions (RuPEP is one of its sources) and pairs with sanctions lists like the `[[un-security-council-consolidated-list]]` and OFAC SDN — RuPEP gives the *network and roles*, sanctions lists give the *designation status*.

## Trust & verifiability
`trust: trusted` — a respected investigative resource with per-profile sourcing, integrated into OpenSanctions; still, verify individual claims via the cited sources and disambiguate common names carefully.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rupep |
| category | financial-crypto |
| selectorsIn → selectorsOut | name, employer-org → associate, employer-org, dob |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

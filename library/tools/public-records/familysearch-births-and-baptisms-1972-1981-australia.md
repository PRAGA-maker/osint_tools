---
id: familysearch-births-and-baptisms-1972-1981-australia
name: FamilySearch — Australia Births & Baptisms
description: Use when you have a `name` (and rough birth year/place in Australia) and want indexed birth/baptism records to confirm identity and parents — returns dob, associate and address leads.
url: https://familysearch.org/search/collection/1770729
category: public-records
path:
- public-records
bestFor: Confirming an Australian subject's birth/baptism and parentage from FamilySearch's free indexed birth-and-baptism collection.
selectorsIn:
- name
- dob
selectorsOut:
- dob
- associate
- address
status: live
pricing: free
costNote: Free — FamilySearch is a nonprofit; a free account may be required to view full index details. Due to privacy laws, recent records may be withheld.
opsec: passive
opsecNote: You search a historical genealogy index, not the living subject; no target-facing signal is sent. A free FamilySearch account is tied to you — register a sock-puppet identity for it.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: FamilySearch is operated by the nonprofit Genealogical Society of Utah; the index is authoritative though coverage is partial and transcriptions can contain errors.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- findmypast-ie
- ancestry
aliases:
- Australia Births and Baptisms 1792-1981
- FamilySearch collection 1770729
tags:
- toddington
- curated-directory
- specialty-search
- genealogy
- australia
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# FamilySearch — Australia Births & Baptisms

> A free FamilySearch index of selected Australian birth and baptism records (1792–1981) — for confirming a subject's birth details and parentage.

## When to use
You have a `name` and an approximate birth year and Australian locality, and you want to confirm the person's `dob`, birthplace, and parents. Birth/baptism records are a strong identity anchor and relationship lever: they tie a subject to `associate` links (parents, and often place of residence), which living-person databases rarely provide — especially useful for older or cold cases.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the collection at familysearch.org (collection 1770729); sign in with a free (sock-puppet) account if prompted.
2. Search by first/last name, birthplace, and birth year.
3. Read the indexed result: name, birth/baptism date and place, and parents' names.
4. Cross-check against other collections and spelling variants to confirm the individual.
5. Pivot: parents' names feed associate/family mapping; a confirmed `dob`/birthplace anchors other records; birthplace feeds `address` and locality research.

## Inputs → Outputs
- **In:** `name` (+ approximate birth year/place)
- **Out:** `dob` (birth/baptism date), `associate` (parents), `address` (birthplace/locality)
- **Empty/negative result looks like:** no match — coverage is partial ("only a few localities," varying by area), recent records are privacy-withheld, and names may be mis-transcribed. Try variants before concluding absence.

## Gotchas & OpSec
- Coverage is deliberately incomplete and locality-dependent; a miss is often a coverage gap, not evidence of nonexistence.
- Transcription/OCR errors are common — search fuzzily and verify against the source where images exist.
- OpSec: passive; a historical archive. Human-in-the-loop: a free login may be required.

## Overlaps ("do both")
- Pairs with `[[ancestry]]` and `[[findmypast-ie]]` and other state/territory registries — different providers digitise different Australian collections, so a record absent here may exist elsewhere.

## Trust & verifiability
`trust: trusted` — an authoritative nonprofit genealogy index; the records are reliable, but confirm transcriptions and remember coverage is partial.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | familysearch-births-and-baptisms-1972-1981-australia |
| category | public-records |
| selectorsIn → selectorsOut | name, dob → dob, associate, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |

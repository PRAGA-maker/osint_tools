---
id: banq-num-rique
name: BAnQ numérique
description: Use when you have a `name`/`address` connected to Québec and want historical records — returns civil-registry, newspaper, notarial, photo and genealogy hits from Québec's national archive.
url: https://numerique.banq.qc.ca/resultats
category: public-records
path:
- public-records
bestFor: Searching Québec's digitised civil registry, newspapers, notarial and photo archives for a person or place.
selectorsIn:
- name
- address
selectorsOut:
- name
- dob
- associate
- address
status: live
pricing: free
costNote: Free online access to 2M+ digitised items; some in-copyright material may be restricted to library terminals.
opsec: passive
opsecNote: You search a public library catalogue, not the subject — nobody is alerted. No login is needed to search public-domain material.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official platform of Bibliothèque et Archives nationales du Québec (Québec's national library and archives); primary-source records.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- BAnQ
- Bibliothèque et Archives nationales du Québec
tags:
- public-records
- genealogy
- archives
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# BAnQ numérique

> Québec's national digital archive — 2M+ items of newspapers, civil-registry records, notarial acts, photos and maps, free to search for people and places tied to Québec.

## When to use
You have a `name` (or an `address`/place) with a Québec connection and want historical or genealogical corroboration: birth/marriage/death via civil-registry and parish records, mentions in old newspapers, notarial acts naming parties, or historical photos. Strong for building family context and confirming identity in Québec cases; the civil-registry coverage is why this rates medium relevance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://numerique.banq.qc.ca/resultats.
2. Enter the `name` (try surname variants and French spellings) or a place `address`.
3. Filter by document type (journaux/newspapers, registres/registers, photographies), date, subject, location or creator.
4. Open a record to read/download the digitised item (public-domain items are viewable online).
5. Pivot: a marriage/parish record links `associate`s and dates (`dob`); a notarial act names other parties; a newspaper mention gives an `address` or event to chase.

## Inputs → Outputs
- **In:** `name` or place/`address` (French-language content)
- **Out:** `name` matches with `dob`/dates, family `associate`s, `address`es, from civil-registry, newspapers, notarial and photo records
- **Empty/negative result looks like:** few/no hits — often a spelling issue (French accents, anglicised names) or a subject with no Québec footprint. Retry with variants before concluding nothing exists.

## Gotchas & OpSec
- Human-in-the-loop: none to search; a small amount of in-copyright material may only open on-site.
- OpSec: passive; searching a public archive alerts no one.
- Content is overwhelmingly French and Québec-focused — irrelevant for subjects with no Québec/Canada tie; use accent-aware and phonetic name variants.

## Overlaps ("do both")
- Complements other national/genealogy archives — use BAnQ for the Québec record set specifically, and a broader genealogy source for records outside the province.

## Trust & verifiability
`trust: trusted` — an official government archive serving primary-source records; provenance and dating are authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | banq-num-rique |
| category | public-records |
| selectorsIn → selectorsOut | name, address → name, dob, associate, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

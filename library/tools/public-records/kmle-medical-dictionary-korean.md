---
id: kmle-medical-dictionary-korean
name: KMLE Medical Dictionary – Korean
description: Use when you have Korean-language medical terms in a subject's records and want them decoded (or need Korean medical-community context) — returns term definitions, not personal records.
url: http://www.kmle.com
category: public-records
path:
- public-records
bestFor: Decoding Korean/English medical terminology in documents and browsing a Korean medical-professional community as background context.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free Korean medical dictionary and community portal; the dictionary is open, some community boards require a free account.
opsec: passive
opsecNote: A public dictionary/community site — you look up terms, not people. Reading the dictionary leaves no target-side footprint. If you register to read gated community boards, use a sock-puppet account; those boards are frequented by Korean medical professionals who may recognise unusual activity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running, privately run Korean medical reference (KMLE) widely used by Korean med students and clinicians; the dictionary is reliable for terminology, community content is user-generated.
missingPersonsRelevance: medium
coverage:
- kr
auth: none
api: false
localInstall: false
registration: false
aliases:
- KMLE
- Korean Medical Library Engine
- kmle.com
tags:
- toddington
- curated-directory
- academic-scholarly-research-tools
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# KMLE Medical Dictionary – Korean

> A Korean medical dictionary and med-professional community portal — a terminology decoder and context source for cases involving Korean medical records or personnel, not a people-search.

## When to use
You are working a case with Korean-language medical material — a hospital record, prescription, obituary, licensing reference, or a subject who is a Korean medical professional — and you need to decode a term, drug name, or specialty, or understand the professional context. KMLE gives Korean⇄English medical definitions and hosts boards used by Korean medical students and doctors. It does **not** return an individual's records; treat it as reference and context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.kmle.com (a Korean-language site — use a browser translator if needed).
2. Enter the Korean or English medical term/abbreviation into the dictionary search.
3. Read the definition, English equivalent, and related terms to interpret the document you hold (`employer-org`/specialty context).
4. For background, browse the community/board sections on Korean medical training and practice (some require a free login).
5. Pivot: a decoded specialty or institution feeds Korean professional-registry and public-records searches for the actual person.

## Inputs → Outputs
- **In:** a Korean/English medical term, abbreviation, or specialty reference (`employer-org` context)
- **Out:** definitions, English equivalents, and specialty/field context (`employer-org`) — reference, not personal data
- **Empty/negative result looks like:** no dictionary hit — the term may be a brand name, a non-medical word, or misspelled/mis-transliterated; try the English equivalent or a broader term.

## Gotchas & OpSec
- Korean-language interface; expect to translate.
- This is terminology/community reference — it will not surface a named individual's medical or personal records (and you should not expect protected records here).
- Community boards may need a free account; isolate any account you create.

## Overlaps ("do both")
- Complements Korean professional-registry and public-records tools — KMLE decodes the medical language and context, those sources confirm the actual person, licence, or institution.

## Trust & verifiability
`trust: community` — a well-established, privately run Korean medical reference; dictionary definitions are dependable for terminology, while community/board content is user-generated and should be corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kmle-medical-dictionary-korean |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

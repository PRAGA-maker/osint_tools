---
id: portrait-search
name: Smithsonian National Portrait Gallery — Portrait Search
description: Use when you have a `name` of a notable/historical American and want catalogued portraits of them — returns portrait `image`s and biographical catalogue metadata. Niche; not for everyday missing-persons work.
url: http://npgportraits.si.edu/code/emuseum.asp
category: image-video-face
path:
- image-video-face
bestFor: Finding catalogued portraits and identity/biographical records of notable or historical people via the Smithsonian NPG collection.
selectorsIn:
- name
selectorsOut:
- image
status: degraded
pricing: free
costNote: Free public museum collection. The original eMuseum URL (npgportraits.si.edu) now 301-redirects to the Smithsonian National Portrait Gallery collection at npg.si.edu/portraits.
opsec: passive
opsecNote: You search a public museum catalogue — no subject interaction, no notification. Ordinary web-logging only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Smithsonian Institution (National Portrait Gallery) — an authoritative cultural-heritage catalogue, not a third-party scraper. The legacy eMuseum interface is retired; use the current npg.si.edu collection.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- NPG portrait search
- Smithsonian portrait collection
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- museum
source: toddington-resources
lastVerified: '2026-07-15'
enrichment: full
---

# Smithsonian National Portrait Gallery — Portrait Search

> A searchable catalogue of the Smithsonian's National Portrait Gallery — portraits and biographical records of notable and historical figures, chiefly Americans.

## When to use
This is a **niche** resource, not a general people-finder. Reach for it only when your subject is a notable, public, or historical figure (a politician, artist, scientist, military figure, etc.) and you want an authoritative catalogued portrait or identity record — for example to confirm what a historical person looked like, date a likeness, or corroborate a name against a museum-verified record. For ordinary living missing-persons work it will almost always return nothing; do not treat its inherited "high" relevance tag as meaning it fits everyday cases.

## How to use it (`bestInteractionPattern`: web-manual)
1. The legacy URL (npgportraits.si.edu) redirects to the current Smithsonian NPG collection at **npg.si.edu/portraits** — start there.
2. Search by `name` (and, if needed, era or medium).
3. Read the catalogue record: portrait `image`(s), sitter identity, artist, date, and biographical notes.
4. Pivot: a dated portrait and biographical notes corroborate identity, era, and appearance for a notable person; the catalogue record can seed further archival research.

## Inputs → Outputs
- **In:** `name` of a notable/historical person
- **Out:** catalogued portrait `image`(s) plus sitter/artist/date and biographical metadata
- **Empty/negative result looks like:** no match — expected for anyone who is not a catalogued public/historical figure; absence says nothing about a private individual.

## Gotchas & OpSec
- Scope is **notable/historical people**, mostly American — not a database of the general public.
- The old eMuseum interface is dead; only the redirected npg.si.edu collection works.
- OpSec: fully passive; a public museum catalogue.

## Overlaps ("do both")
- Complements reverse-image/face search and Wikipedia/Wikidata for notable subjects — the museum record is authoritative for a catalogued sitter, while reverse-image tools cover the open web.

## Trust & verifiability
`trust: trusted` — an authoritative Smithsonian catalogue; records are curated and reliable. The only caveat is coverage (notable/historical figures only) and the retired legacy URL.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | portrait-search |
| category | image-video-face |
| selectorsIn → selectorsOut | name → image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>

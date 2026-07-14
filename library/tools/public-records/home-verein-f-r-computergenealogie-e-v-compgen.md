---
id: home-verein-f-r-computergenealogie-e-v-compgen
name: CompGen (Verein für Computergenealogie)
description: Use when you have a German/Central-European `name` and want genealogical records — historical address books, gazetteers, and family databases — returns `associate` (family), `dob`/dates, `address`, and `name` links.
url: https://www.compgen.de
category: public-records
path:
- public-records
bestFor: German-language genealogy: historical address books, the GOV place gazetteer, and community family databases (GedBas, online OFBs).
selectorsIn:
- name
selectorsOut:
- associate
- dob
- address
- name
status: live
pricing: free
costNote: Run by a non-profit association; core databases (GedBas, Adressbücher, GOV, Metasuche) are free to search. Some services ask for registration or donations; no hard paywall for the main lookups.
opsec: passive
opsecNote: Passive — you search historical/genealogical databases, not living-person surveillance, and no subject is notified. German data-protection norms mean records skew historical (deceased persons); recent living-person data is limited by design.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: CompGen (Verein für Computergenealogie e.V.) is a long-established, reputable German genealogy non-profit; its digitized address books and databases are community-curated from real historical sources.
missingPersonsRelevance: high
coverage:
- de
auth: none
api: false
localInstall: false
registration: false
aliases:
- Verein für Computergenealogie
- compgen.de
- GenWiki
tags:
- genealogy
- family
- germany
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# CompGen (Verein für Computergenealogie)

> Germany's leading volunteer genealogy hub — digitized historical address books, a vast place-name gazetteer, and community family databases that reach where commercial people-search never goes.

## When to use
You have a German (or Central-European) `name` and need to build out family and historical context: ancestors, relatives (`associate`), birth/death dates (`dob`), and historical `address`es. Invaluable for cold cases, long-missing persons, diaspora tracing, and confirming identity through family structure — especially the digitized **Adressbücher** (historical city address books) that place a named person at an address in a given year, and **GOV**, which resolves old/renamed German place names.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.compgen.de and choose a database:
   - **Adressbücher** — historical German address books; search a surname to find people, occupations, and street addresses by city/year.
   - **GedBas** — community-submitted genealogy database; search a name for family trees, dates, and relatives.
   - **GOV** (Genealogical Gazetteer) — resolve historical/renamed place names to modern locations and jurisdictions.
   - **Metasuche** — cross-database name search.
2. Enter the `name` (try historical spelling variants; German umlauts/ß matter).
3. Read results: linked relatives (`associate`), dates (`dob`/death), and period `address`es.
4. Cross-reference across databases to corroborate a family line.
5. Pivot: an address+year feeds archival/civil-registry requests; relatives feed further genealogy and modern people-search for living descendants.

## Inputs → Outputs
- **In:** German/Central-European `name` (with a place and rough era ideally)
- **Out:** family `associate`s, `dob`/death dates, historical `address`es, confirmed `name` variants
- **Empty/negative result looks like:** no hits — common for a spelling variant, an uncovered region/period, or a very recent (living) person whom German privacy practice keeps out. Try variant spellings and adjacent places before concluding absence.

## Gotchas & OpSec
- **German-language interface and records** — use a translator and correct diacritics; surname spellings drift across centuries.
- Coverage is strongest for historical/deceased persons; living-person data is deliberately sparse under German data-protection norms.
- Community-contributed trees (GedBas) can contain errors — treat submissions as leads to verify against primary records.
- OpSec: fully passive; historical archive research.

## Overlaps ("do both")
- Pairs with international genealogy databases (FamilySearch, Ancestry) and German civil-registry/archive requests — CompGen's digitized address books and GOV gazetteer cover German specifics those miss, while the big genealogy platforms add breadth and living-descendant links.

## Trust & verifiability
`trust: trusted` — a reputable, long-standing non-profit digitizing genuine historical sources. The scanned address books are authoritative primary material; user-submitted family trees need corroboration. Verify a linkage across multiple databases/sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | home-verein-f-r-computergenealogie-e-v-compgen |
| category | public-records |
| selectorsIn → selectorsOut | name → associate, dob, address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

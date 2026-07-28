---
id: rechercher-par-r-gion-ou-type-de-travaux
name: RBQ Registre des licences — recherche par région ou type de travaux
description: Use when you have a `geolocation`/region or trade type in Québec and want to enumerate licensed construction contractors there — returns employer-org, address, document-id (licence numbers).
url: https://www.pes.rbq.gouv.qc.ca/RegistreLicences/Recherche?mode=RegionTypeTravaux
category: public-records
path:
- public-records
bestFor: Enumerating RBQ-licensed construction contractors in Québec by region and/or type of work.
selectorsIn:
- geolocation
- address
selectorsOut:
- employer-org
- address
- document-id
- name
status: live
pricing: free
costNote: Free public government registry (Régie du bâtiment du Québec); no account required.
opsec: passive
opsecNote: You are querying an official Québec government registry, not the subject. Fully passive from the target's perspective. Standard government-site logging of your visit applies; use a clean browser profile if you don't want the query tied to your other research.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Régie du bâtiment du Québec (RBQ), the provincial construction regulator; this is the authoritative licence registry, not a third-party aggregator.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- rechercher-par-entreprise
- rechercher-par-r-pondant
- alcool-r-gie-des-alcools-des-courses-et-des-jeux-racj
- banq-num-rique
- services-en-ligne
- trouver-une-d-cision
- association-assq-qc-ca
aliases:
- RBQ registre des licences
- Quebec construction licence registry
tags:
- public-records
- quebec
- business-registry
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# RBQ Registre des licences — recherche par région ou type de travaux

> Québec's official construction-licence registry, searched by geographic region or type of work — turns "who does this kind of work in this area" into a list of licensed contractors.

## When to use
Your subject is (or claims to be) a construction contractor in Québec, or you need to enumerate licensed trades in a region — e.g. to corroborate an employer, find a business tied to a person, or cross-reference a licence a subject cited. Enter a region and/or type of work and get the roster of RBQ licence holders. French-language interface.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the registry search page (mode: *par région ou type de travaux*).
2. Select the **région** and/or **type de travaux** (trade category).
3. Submit to get the list of matching licence holders.
4. Open a result for details: the licensed entity name (`employer-org`), licence number (`document-id`), address, and the natural person named as *répondant* (technical officer) where shown.
5. Pivot: an `employer-org` → Québec enterprise registry (REQ) for directors/`name`; a *répondant* name → people search; cross-check with the by-business and by-répondant search modes (`relatedTools`).

## Inputs → Outputs
- **In:** region and/or type of work (a `geolocation`/`address` context)
- **Out:** `employer-org` (licensed business), `document-id` (licence number), `address`, and sometimes an individual `name` (répondant)
- **Empty/negative result looks like:** no licence holders returned for the region/trade combination — meaning no RBQ-licensed contractor matches there, not that no one does that work (unlicensed operators won't appear).

## Gotchas & OpSec
- French-language government interface; use translation but keep trade-category terms exact.
- Only RBQ-licensed contractors appear — an absent name may mean unlicensed, out-of-scope, or lapsed, not nonexistent.
- Passive against the target; standard gov-site logging of your own visit.

## Overlaps ("do both")
- Pairs with `[[rechercher-par-entreprise]]` (search by business name) and `[[rechercher-par-r-pondant]]` (search by the named technical officer) — same registry, complementary entry points; run all three to fully resolve a contractor.

## Trust & verifiability
`trust: trusted` — the authoritative provincial regulator's registry. Licence status and numbers are official; the data is limited to what the RBQ licenses (Québec construction only).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rechercher-par-r-gion-ou-type-de-travaux |
| category | public-records |
| selectorsIn → selectorsOut | geolocation, address → employer-org, address, document-id, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: rechercher-par-r-pondant
name: Rechercher par répondant (RBQ Québec)
description: Use when you have a `name` and want to find the Québec construction licences that person is the designated responsible party for — returns linked contractor businesses and licence numbers.
url: https://www.pes.rbq.gouv.qc.ca/RegistreLicences/Recherche?mode=Repondant
category: public-records
path:
- public-records
bestFor: Searching Québec's RBQ contractor-licence registry by "répondant" (the individual accountable for a licence) to link a person to businesses.
selectorsIn:
- name
selectorsOut:
- employer-org
- document-id
status: live
pricing: free
costNote: Free public search on the Régie du bâtiment du Québec (RBQ) official licence registry; no account needed.
opsec: passive
opsecNote: Querying an official government registry is passive — the subject is not notified. Your search goes to a Québec government site (your IP is logged there); this is a public record, so the lookup itself is low-risk, but use a research connection if you prefer not to associate the query with you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party government registry operated by the Régie du bâtiment du Québec; authoritative licensing data for the province.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- rechercher-par-entreprise
- rechercher-par-r-gion-ou-type-de-travaux
- services-en-ligne
- alcool-r-gie-des-alcools-des-courses-et-des-jeux-racj
- association-assq-qc-ca
- banq-num-rique
- trouver-une-d-cision
aliases:
- RBQ search by respondent
- Registre des licences RBQ - répondant
tags:
- public-records
- licensing
- quebec
source: osint4all
lastVerified: '2026-08-05'
enrichment: full
---

# Rechercher par répondant (RBQ Québec)

> Québec's official contractor-licence registry, searched by the licence's "répondant" — the person legally accountable for it — linking an individual to the construction businesses they stand behind.

## When to use
You have a `name` and want to know whether that person is the designated responsible party (répondant) on any Québec construction licence. It ties an individual to contractor businesses and licence numbers — useful for confirming an occupation/employer, uncovering business affiliations, or corroborating a subject's presence and role in the province's construction sector.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the RBQ registry at the "Rechercher par répondant" mode URL.
2. Enter the person's `name` (surname/given name) as the répondant to search.
3. Review the returned licences: each links a répondant to a licensed business (`employer-org`) and a licence number (`document-id`), with status and categories of work.
4. Open a licence record for details (business address, licence class, validity).
5. Pivot: the linked business (`employer-org`) → Québec enterprise registry (REQ) and the sibling "Rechercher par entreprise" mode; the licence status/history → timeline and corroboration.

## Inputs → Outputs
- **In:** `name` (the répondant)
- **Out:** matching Québec construction licences → business (`employer-org`), licence number (`document-id`), status, and work categories
- **Empty/negative result looks like:** no matching répondant — the person may not hold a Québec licence, may use a name variant, or acts only through a company; try the "par entreprise" search or spelling variants before concluding.

## Gotchas & OpSec
- Name variants: French accents and given/surname order matter — try with and without accents and both name orders.
- Scope: Québec construction licences only; someone active elsewhere or in another trade won't appear here.
- OpSec: passive public-records lookup; the subject is not alerted.

## Overlaps ("do both")
- Pairs with [[rechercher-par-entreprise]] (same registry, business-side) and [[rechercher-par-r-gion-ou-type-de-travaux]] — search the person here, then confirm and expand via the business and region/work-type modes.

## Trust & verifiability
`trust: trusted` — a first-party Québec government registry; licence and répondant data are authoritative, though always confirm identity via cross-referencing (common names can collide).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rechercher-par-r-pondant |

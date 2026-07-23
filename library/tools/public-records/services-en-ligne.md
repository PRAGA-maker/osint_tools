---
id: services-en-ligne
name: Services en ligne (Commission des transports du Québec)
description: Use when you have a `name` or `employer-org` in Québec and want their transport-registry file — heavy-vehicle owner/operator status, permits and authorizations — returns registration status, `address` and `document-id` references.
url: https://www.pes.ctq.gouv.qc.ca/pes/faces/dossierclient/recherche.jsp
category: public-records
path:
- public-records
bestFor: Looking up a Québec individual or business in the heavy-vehicle owner/operator and transport-permit registries.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- document-id
status: live
pricing: free
costNote: Free public consultation service of the Commission des transports du Québec (CTQ); no account for the public register search.
opsec: passive
opsecNote: Public government registry lookup — you query the CTQ, not the subject, so there is no target-side exposure. Interface and results are in French.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Government of Québec (Commission des transports du Québec) registry; the registration, permit and operator data is authoritative public record.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- alcool-r-gie-des-alcools-des-courses-et-des-jeux-racj
- association-assq-qc-ca
- banq-num-rique
- rechercher-par-entreprise
- rechercher-par-r-gion-ou-type-de-travaux
- rechercher-par-r-pondant
- trouver-une-d-cision
aliases:
- CTQ Services en ligne
- Commission des transports du Québec dossier client
tags:
- quebec
- transport-registry
- public-records
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Services en ligne (Commission des transports du Québec)

> The Québec transport regulator's public consultation portal: search an individual or business against the heavy-vehicle owner/operator registry and transport permits/authorizations.

## When to use
You have a `name` or `employer-org` connected to Québec road transport — a trucking company, a heavy-vehicle owner, a licensed carrier or a transport-system respondent — and you want the regulator's file on them: are they registered, what permits do they hold, what's their operating status and safety record. Useful for corroborating that a business is real and licensed, and for tying a company to its registered address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CTQ online services (current entry point: the "Dossier d'une entreprise ou d'un individu" consultation, `pes.ctq.gouv.qc.ca`). The interface is in French.
2. Choose the register from the "Permis / Registres / Liste" menu (e.g. heavy-vehicle owners and operators / propriétaires et exploitants de véhicules lourds).
3. Search by business name/`employer-org`, individual `name`, or file/registration number.
4. Open the matching file: registration status, permit type, operator identification and address details.
5. Pivot: the `employer-org` + `address` feeds the Québec enterprise register (REQ) for directors/ownership; a `document-id`/permit number anchors further CTQ decision lookups.

## Inputs → Outputs
- **In:** `name` or `employer-org` (Québec transport context)
- **Out:** registration/permit status, operator `employer-org` identity, registered `address`, permit/file `document-id`
- **Empty/negative result looks like:** "aucun résultat" / no matching file — the person or business is not in that CTQ register (they may be unregistered, out of scope, or spelled differently — try name variants).

## Gotchas & OpSec
- French-language interface and records — expect French field labels and register names.
- Scope is Québec road-transport regulation only; it will not cover businesses outside transport or outside Québec.
- OpSec: passive — a public government registry; the subject sees nothing.

## Overlaps ("do both")
- Pairs with the Québec enterprise register (Registraire des entreprises) — CTQ confirms transport-permit status and operator identity, while the enterprise register adds incorporation, directors and ownership for the same `employer-org`.

## Trust & verifiability
`trust: trusted` — it is the Commission des transports du Québec's own public registry, so registration and permit data is authoritative government record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | services-en-ligne |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

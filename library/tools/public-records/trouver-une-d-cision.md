---
id: trouver-une-d-cision
name: Trouver une décision (SOQUIJ)
description: Use when you have a `name` and want Quebec/Canadian court and tribunal decisions that mention the person as a party, witness, or professional — returns document-id and associate leads.
url: http://citoyens.soquij.qc.ca/
category: public-records
path:
- public-records
bestFor: Searching Quebec (and some Canadian) court and administrative-tribunal decisions by party name to place a subject in litigation, disciplinary, or family-court records.
selectorsIn:
- name
selectorsOut:
- document-id
- associate
- address
status: live
pricing: freemium
costNote: The "Citoyens" portal offers free keyword/party-name searching and access to many decisions; the full SOQUIJ database and some full-text documents require a paid subscription or per-document purchase.
opsec: passive
opsecNote: You query SOQUIJ's public decision index, not the target — passive, no notification to the subject. No login needed for the free citizen search. Standard site logging applies; use a VPN/sock-puppet if you don't want the query tied to you.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: SOQUIJ is the official legal-information body of the Government of Québec; decisions are authoritative court/tribunal records, not third-party scrapes.
missingPersonsRelevance: medium
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
- services-en-ligne
aliases:
- SOQUIJ Citoyens
- citoyens.soquij.qc.ca
tags:
- legal
- court-records
- quebec
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# Trouver une décision (SOQUIJ)

> Québec's official portal for searching court and administrative-tribunal decisions by keyword or party name — a primary-source public record for anyone who has appeared in the province's justice system.

## When to use
You have a `name` (in French-language Québec/Canada context) and want to know whether the subject appears in a court judgment, a professional-discipline ruling, a family-court decision, a small-claims case, or an administrative tribunal. Decisions routinely name the parties, sometimes their municipality, employer, and the associates/counterparties involved — useful for building a subject's history, financial disputes, and network.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://citoyens.soquij.qc.ca/.
2. Use the free citizen search: enter the subject's `name` as a party, or a keyword; refine by court/tribunal, date range, and sort by date or relevance.
3. Read the results list — each hit is a decision with the deciding body, date, and file number. Open decisions to read the named parties, facts, and any location/employment details.
4. If a needed full-text decision is behind the paid SOQUIJ database, note the neutral citation/file number and retrieve it from a free source (CanLII) where possible.
5. Pivot: a file number is a `document-id` to pull the full record; named counterparties/counsel are `associate` leads; a stated municipality narrows an `address`.

## Inputs → Outputs
- **In:** `name` (party, sometimes professional/witness)
- **Out:** `document-id` (decision/file number + citation), `associate` (other parties, counsel), `address` (municipality/region when stated)
- **Empty/negative result looks like:** no decisions returned — the person has no indexed Québec/Canadian decision, or their case is sealed/anonymised (family and youth matters are often initialised). Absence is not proof of no litigation.

## Gotchas & OpSec
- Language: the interface and decisions are in French; search accordingly.
- Coverage/pricing: the free citizen portal indexes a large but not exhaustive set; deep full-text access is paywalled. Cross-check against CanLII for a free full text.
- Anonymisation: sensitive matters (youth, family, some civil) mask names — a common name may also collide, so confirm identity from case facts.

## Overlaps ("do both")
- Pairs with a national free legal database (CanLII) — SOQUIJ has strong Québec tribunal coverage and its own editorial summaries, while CanLII gives free full text across all Canadian jurisdictions.

## Trust & verifiability
`trust: trusted` — SOQUIJ is a Québec government body publishing official court/tribunal decisions, so a hit is an authoritative primary record you can cite by its neutral citation and file number.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trouver-une-d-cision |
| category | public-records |
| selectorsIn → selectorsOut | name → document-id, associate, address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |

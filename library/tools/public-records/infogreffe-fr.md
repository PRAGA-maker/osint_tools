---
id: infogreffe-fr
name: infogreffe.fr
description: Use when you have a company or director `name` in France and want official commercial-registry detail — returns company officers, registered `address`, incorporation data and official documents (Kbis).
url: https://www.infogreffe.fr/
category: public-records
path:
- public-records
bestFor: Official French corporate-registry lookups — directors, registered address, filings — to tie a person to a company.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- employer-org
- associate
- address
- name
status: live
pricing: freemium
costNote: Free to search companies and see basic identifiers; official documents (Kbis extract, statutes, accounts) and detailed reports are paid.
opsec: passive
opsecNote: Read-only registry search; the company/subject is not notified. Ordering paid documents requires payment details. This is the official commercial-court registry portal, so data quality is high.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Groupement d'Intérêt Économique Infogreffe on behalf of France's commercial-court registries (greffes des tribunaux de commerce) — the authoritative French corporate registry.
missingPersonsRelevance: high
coverage:
- fr
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- i-cyprus-com
aliases:
- Infogreffe
- greffe registry France
tags:
- companysites
- Company Related Sites
- corporate-registry
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# infogreffe.fr

> The official portal of France's commercial-court registries — authoritative company records tying people to French businesses via directorships, addresses, and filings.

## When to use
You have a `name` (person or company) connected to France and want the corporate picture: what companies a person runs or directs, the registered `address`, incorporation details, co-officers (`associate`), and official documents (the Kbis extract, statutes, filed accounts). As the authoritative registry (fed by the greffes des tribunaux de commerce), it's the primary source for confirming a French company's existence and mapping a subject's business links.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.infogreffe.fr/.
2. Search by company `name`, SIREN/SIRET, or (where supported) a director's `name`.
3. Free tier: confirm the company, see identifiers, officers, and registered address. For the Kbis, statutes, or accounts, order the paid document.
4. Read the record: dirigeants/officers (`associate`), registered `address`, incorporation date, activity, and filing history.
5. Pivot: a co-officer's `name` feeds people-search; the address feeds property/mapping; cross-check foreign entities via other registries.

## Inputs → Outputs
- **In:** company/director `name`, `employer-org`, SIREN/SIRET, or `address`
- **Out:** `employer-org` (companies), `associate` (officers/dirigeants), registered `address`, `name`, incorporation/filing data, Kbis (paid)
- **Empty/negative result looks like:** no company match — the entity isn't registered in France or the identifier is wrong. A free-tier match without documents just means the documents are paywalled, not missing.

## Gotchas & OpSec
- Human-in-the-loop: official documents are **paywalled** (`payment-wall-partial`); the free search still gives officers and address.
- France-only; for other jurisdictions use the corresponding national registry.
- OpSec: **passive** — an official registry read; mind billing hygiene when ordering documents.

## Overlaps ("do both")
- Pairs with `[[i-cyprus-com]]` and other national registries — a subject's companies often span countries, so run the registry for each domicile and cross-link recurring officers/addresses. (French open data is also available via the free INSEE/annuaire-entreprises services as a cross-check.)

## Trust & verifiability
`trust: trusted` — the authoritative French commercial registry; officer and address data are official, though the richest documents (Kbis, accounts) require payment.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | infogreffe-fr |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address → employer-org, associate, address, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |

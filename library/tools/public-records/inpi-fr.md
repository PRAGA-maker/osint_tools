---
id: inpi-fr
name: inpi.fr
description: Use when you have a French `name`, `employer-org`, or `address` and want official company records and directors/beneficial owners — returns `employer-org`, `name`, `address`, `associate`, and the SIREN `document-id`.
url: https://data.inpi.fr/
category: public-records
path:
- public-records
bestFor: Searching France's national business register (RNE) for a company, its officers, and beneficial owners.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- name
- address
- associate
- document-id
status: live
pricing: free
costNote: Free open-data portal from INPI; no account needed for search. Some full document downloads (statutes, acts) may require a free login.
opsec: passive
opsecNote: Querying the national register is passive — you search a government database, not the subject, who is not notified. No login is needed for basic search; queries are ordinary web requests.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by INPI (Institut National de la Propriété Industrielle), which maintains France's Registre National des Entreprises (RNE); data is authoritative public record.
missingPersonsRelevance: high
coverage:
- fr
auth: none
api: true
localInstall: false
registration: false
aliases:
- data.inpi.fr
- Registre National des Entreprises
- RNE
tags:
- companysites
- Company Related Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# inpi.fr

> France's national business register (RNE) as open data — search any French company and see its directors, beneficial owners, addresses, and filings, for free.

## When to use
Your subject is linked to a French company, or you have a person's `name`, a company `employer-org`, or a registered `address` and want to map French corporate affiliations. INPI's portal consolidates the RNE, exposing officers (dirigeants), beneficial owners (bénéficiaires effectifs), registered addresses, SIREN/SIRET identifiers, and deposited documents — a rich node for tracing business links or a person behind a company.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://data.inpi.fr/ (French; use translation).
2. Search by company `name`/`employer-org`, a person's `name` (dirigeant search), or SIREN/SIRET.
3. Open the entity: read the registered `employer-org`, `address`, status, officers and beneficial owners (`associate`, `name`), and the SIREN (`document-id`).
4. Download available acts/statutes for deeper detail (may need a free login).
5. Pivot: an officer name feeds French people-search; the SIREN links to `[[societe-com]]`/`[[pappers]]` and other registries; the address feeds mapping.

## Inputs → Outputs
- **In:** company `name`/`employer-org`, person `name` (director), `address`, or SIREN/SIRET
- **Out:** `employer-org`, `address`, officers/beneficial owners (`associate`, `name`), SIREN `document-id`, filed documents
- **Empty/negative result looks like:** no match — the entity may be dissolved, very new (registration lag), or spelled differently. Some personal data on beneficial owners has access limits following EU rulings; not every field is always public.

## Gotchas & OpSec
- French-language interface and legal terms (dirigeant, gérant, bénéficiaire effectif); use translation.
- Beneficial-ownership visibility has been restricted in places post-2022 EU court rulings — expect some redaction.
- SIREN is the strong key — carry it to other French corporate tools rather than re-searching by name.

## Overlaps ("do both")
- Pairs with `[[pappers]]` and `[[societe-com]]` — those wrap the same official data with friendlier UX and extra analytics, while INPI is the authoritative primary source and document repository.

## Trust & verifiability
`trust: trusted` — first-party French government register (INPI/RNE); company, officer, and filing data is authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | inpi-fr |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, name, address, associate, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

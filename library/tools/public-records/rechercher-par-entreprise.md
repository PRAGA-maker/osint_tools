---
id: rechercher-par-entreprise
name: Rechercher par entreprise (RBQ Québec)
description: Use when you have an `employer-org`/company name in Québec and want its construction-licence record — returns licence status, respondents, and business details.
url: https://www.pes.rbq.gouv.qc.ca/RegistreLicences/Recherche?mode=Entreprise
category: public-records
path:
- public-records
bestFor: Verifying a Québec construction contractor's RBQ licence and pulling the company's respondents and status from the public register.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- name
- address
status: live
pricing: free
costNote: Free, official government registry (Régie du bâtiment du Québec). No account or payment.
opsec: passive
opsecNote: A public government registry search; the subject is not notified and nothing ties the query to you beyond RBQ's own server logs. Use a neutral browser session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Québec government source (Régie du bâtiment du Québec) — the authoritative record for construction licences in the province.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- rechercher-par-r-gion-ou-type-de-travaux
- rechercher-par-r-pondant
aliases:
- RBQ Registre des détenteurs de licence
- Search by company (RBQ)
- Régie du bâtiment du Québec licence register
tags:
- public-records
- business-registry
- quebec
- construction-licence
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Rechercher par entreprise (RBQ Québec)

> The "search by company" front door to Québec's official construction-licence register: confirm a contractor is licensed and pull the people and details behind the business.

## When to use
You have an `employer-org` (a construction/renovation company operating in Québec) and want to verify it holds a valid Régie du bâtiment du Québec (RBQ) licence, or you want to pivot from a company to the individuals ("répondants") legally responsible for it. The register covers all current holders plus any that held a licence in the past 5 years, with validity status (valid / non-valid / restricted), bond-claim counts, and business identifiers. Direct missing-persons value is low; it shines for corporate due-diligence and linking a person to a Québec construction business.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.pes.rbq.gouv.qc.ca/RegistreLicences/Recherche?mode=Entreprise (the page loads via JavaScript — allow it a moment).
2. Enter the company `name` (or RBQ licence number) and submit. The form is French-language.
3. Read the record:
   - **Licence status** — valid, non-valid (suspended/cancelled in the last 5 years), or restricted (barred from public contracts).
   - **Respondents** — the named individuals responsible for the licence.
   - **Business details** — licence categories/subcategories, and address information.
4. Pivot: a respondent `name` feeds people-search and the Québec enterprise register (REQ); switch to the "par répondant" or "par région/type de travaux" modes to approach from the person or work-type angle.

## Inputs → Outputs
- **In:** `employer-org` (company name) or licence number
- **Out:** licence status, respondent `name`s, licence categories, business `address`
- **Empty/negative result looks like:** "no result" — the company has never held (or hasn't held within 5 years) an RBQ licence; note that unlicensed operators simply won't appear, which is itself a finding.

## Gotchas & OpSec
- Scope is **Québec construction licences only** — a company absent here may still be a legitimate business in another sector or province.
- French-language interface; company names should be entered as legally registered.
- The 5-year window means older defunct companies drop off.
- OpSec: passive public-records lookup; no subject notification.

## Overlaps ("do both")
- Pairs with `[[rechercher-par-r-pondant]]` (search by responsible person) and `[[rechercher-par-r-gion-ou-type-de-travaux]]` (search by region/work type) — same register, different entry points; and with the Québec enterprise register (REQ) to enrich the corporate entity.

## Trust & verifiability
`trust: trusted` — this is the Québec government's own authoritative licence register, so status and respondent data are official; coverage is strictly construction and provincial.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rechercher-par-entreprise |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, name, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

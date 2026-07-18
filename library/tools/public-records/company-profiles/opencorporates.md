---
id: opencorporates
name: OpenCorporates
description: Use when you have a `name` (person or company) and want corporate records across jurisdictions — returns companies, officers/directorships, registered `address`es, and corporate `associate` links.
url: https://opencorporates.com/
category: public-records
path:
- public-records
- company-profiles
bestFor: Cross-jurisdictional company and officer lookup — tie a person to the companies they direct/own and map corporate networks.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- associate
- name
status: live
pricing: freemium
costNote: Free to search company and officer records on the website. Bulk data and the API require registering for an API key; heavy/commercial use is paid. Basic officer/company web search needs no account.
opsec: passive
opsecNote: Queries hit OpenCorporates' aggregation of official registries, never the subject or their company directly, so the lookup is invisible to the target. No login is needed for web search, so nothing personal is attached to a casual query.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The largest open database of companies, sourced directly from official government business registries with provenance shown per datum; widely used by journalists, NGOs and regulators.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- the-investigator-s-handbook-a-guide-to-using-opencorporates
aliases:
- Open Corporates
tags:
- company
- corporate-registry
- officers
- arf-seed
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# OpenCorporates

> The largest open database of companies — 200M+ entities pulled straight from official registries worldwide, searchable by company or by the people who run them.

## When to use
You have a person's `name` and want to know what companies they direct, own, or are otherwise officially tied to — or you have a company (`employer-org`) and want its officers, registered address, and network of related entities. Officer search is the identity angle: a directorship record links a person to an address, co-directors (`associate`s), incorporation dates, and other companies, which corroborates or expands a subject's footprint. Especially useful when a subject is a business owner, self-employed, or connected to a company under investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://opencorporates.com/ and choose the **Officers** tab to search by person, or **Companies** to search by entity/registration number.
2. Enter the `name` (or company name / number). Narrow by jurisdiction if you know the country/state.
3. Read the results:
   - Officer hits show the person's name, role, the company, and its jurisdiction — click through for the registered `address`, appointment dates, and co-officers.
   - Company hits show status (active/dissolved), registered address, officers, and filings, each stamped with the source registry and retrieval date.
4. Follow the provenance link on any datum back to the official registry to confirm.
5. For bulk/programmatic work, register for the API key at opencorporates.com/api_accounts.
6. Pivot: co-directors → `associate` leads; registered address → address/property research; a company → its full officer list and related entities.

## Inputs → Outputs
- **In:** person `name` (officer search) or company name / `employer-org` / registration number
- **Out:** `employer-org` records, officer roles, registered `address`es, co-officer `associate`s, corporate `name`s
- **Empty/negative result looks like:** no officer/company rows — the person/entity isn't in a registry OpenCorporates has ingested (coverage varies by country); a common name may also return many unrelated officers, so disambiguate by jurisdiction and dates.

## Gotchas & OpSec
- Coverage and freshness vary sharply by jurisdiction — some registries are near-real-time, others lag or are absent.
- Officer records are not deduplicated by person: two "John Smith" directorships may or may not be the same human — confirm via shared address/company overlap.
- Full API and bulk downloads require an API key and, for heavy use, payment; the free web search covers most single-subject lookups.
- Passive and login-free — safe to run without alerting the target.

## Overlaps ("do both")
- Pairs with `[[the-investigator-s-handbook-a-guide-to-using-opencorporates]]` for advanced query technique, and with national registry lookups when you need the authoritative filing behind an OpenCorporates record.

## Trust & verifiability
`trust: trusted` — data comes directly from official government registries with per-field provenance (source + retrieval date) that you can follow back to the primary record, making findings independently verifiable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | opencorporates |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, associate, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

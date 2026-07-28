---
id: eu-sanctions-tool
name: EU Sanctions Map / Consolidated List
description: Use when you have a `name` or `employer-org` and want to check it against EU sanctions regimes — returns whether a person/entity is listed, plus the legal basis and identifiers.
url: https://www.sanctionsmap.eu/
category: public-records
path:
- public-records
- sanctions-screening
bestFor: Screening an individual or organization against official EU financial-sanctions and asset-freeze lists.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
- dob
status: live
pricing: free
costNote: Free official EU resource; no account. (The original sanctions-tool.ec.europa.eu host is retired; use the EU Sanctions Map / Consolidated FSD list.)
opsec: passive
opsecNote: You search the EU's own public list — passive, with no notification to the subject and no exposure of your investigation. Screening a name reveals nothing to that person.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official EU sanctions resource maintained by the EU institutions; the consolidated list (FSD) is the authoritative record of EU-sanctioned persons and entities.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- EU Sanctions Tool
- EU Sanctions Map
- EU Consolidated Sanctions List
tags:
- sanctions-screening
- public-records
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# EU Sanctions Map / Consolidated List

> The EU's official tools for checking whether a person or entity is under EU sanctions — the interactive Sanctions Map plus the authoritative Consolidated Financial Sanctions List (FSD) of 5,000+ listings with aliases.

## When to use
You have a `name` or `employer-org` and need to know if they are subject to EU restrictive measures (asset freezes, travel bans) — essential for due-diligence, AML/KYC context, and understanding a subject's legal exposure. Also lets you browse sanctions by regime/theme (terrorism, human rights, cyber, chemical weapons) and country.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the EU **Sanctions Map** at https://www.sanctionsmap.eu/ to explore regimes by country/theme, or use the search to look up a `name`/`employer-org`.
2. For authoritative screening, search the **Consolidated List (FSD)** — the EU's official database of sanctioned persons/entities, including aliases and alternative spellings and, where available, `dob` and identifiers. (The EU Sanctions Tracker at data.europa.eu also offers a searchable dashboard.)
3. Match carefully on name + identifiers (aliases and DOB reduce false positives on common names).
4. Read the listing's legal basis (regulation, listing date, reason).
5. Pivot: a confirmed listing gives official identifiers and reasons to chase; a non-match should still be cross-checked against other regimes (OFAC, UN, UK).

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** `name`, `employer-org`, and where available `dob`/identifiers, plus the legal basis for the listing
- **Empty/negative result looks like:** no match means the person/entity is not on the **EU** list at that time — it does NOT mean they're unsanctioned elsewhere (check OFAC/UN/UK) or that a near-name-match isn't the same person under an alias.

## Gotchas & OpSec
- **EU-only scope:** a clean result here says nothing about US (OFAC), UN, or UK lists — screen those separately.
- Watch for aliases/transliterations and use `dob`/identifiers to avoid false positives and false negatives on common names.
- Passive and authoritative; the subject is never alerted.

## Overlaps ("do both")
- Do both this and OFAC/UN/UK consolidated lists — sanctions regimes differ, and a person clean on one may be listed on another; screen across all major lists.

## Trust & verifiability
`trust: trusted` — the official EU sanctions resource; the Consolidated List is authoritative and citable, though you must still disambiguate common names using aliases and identifiers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | eu-sanctions-tool |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org, dob |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

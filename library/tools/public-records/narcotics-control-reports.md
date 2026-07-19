---
id: narcotics-control-reports
name: INCSR — International Narcotics Control Strategy Reports
description: Use when you have a country/region and want US State Dept assessments of its drug trafficking and money-laundering landscape — returns country-level context, not person data.
url: http://www.state.gov/j/inl/rls/nrcrpt/index.htm
category: public-records
path:
- public-records
bestFor: Country-level context on narcotics trafficking, chemical control, and money-laundering risk to frame an investigation's geography.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free US government publication (annual). The old state.gov/j/inl/rls/nrcrpt URL is legacy; current reports live at state.gov/international-narcotics-control-strategy-reports/.
opsec: passive
opsecNote: Passive reading of a public government report; no subject interaction and no person-level lookup. Zero target footprint.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official US Department of State (Bureau of International Narcotics and Law Enforcement Affairs) annual report; authoritative for US-government country assessments, though it reflects US policy perspective.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- terrorism-reports
- voter-registration-data
aliases:
- INCSR
- International Narcotics Control Strategy Report
- State Department narcotics report
tags:
- government
- narcotics
- country-reports
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# INCSR — International Narcotics Control Strategy Reports

> The US State Department's annual country-by-country assessment of drug trafficking, precursor-chemical control, and money laundering — geographic and policy context for an investigation, not a person lookup.

## When to use
Not a people tool. Reach for it when a case has an international narcotics or money-laundering dimension and you need authoritative country-level context: which jurisdictions are major drug-transit or -producing countries, their chemical-control and AML regimes, and US-government risk assessments. It frames the geography and regulatory environment around subjects, shipments, or financial flows you're investigating.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the current INCSR at state.gov/international-narcotics-control-strategy-reports/ (the legacy state.gov/j/inl/rls/nrcrpt link is retired).
2. Open the relevant year's volume (Volume I: Drug and Chemical Control; Volume II: Money Laundering).
3. Read the country chapter for trafficking routes, chemical control, AML gaps, and US assessments.
4. Pivot: use the country context to prioritize other records (sanctions lists, corporate registries, trade data) and to interpret a subject's jurisdiction risk.

## Inputs → Outputs
- **In:** a country/region (reference query)
- **Out:** country-level narcotics/AML assessment and context (no person-level data)
- **Empty/negative result looks like:** a country not separately covered — smaller jurisdictions may be grouped or omitted; the report never returns individual records.

## Gotchas & OpSec
- Country-level analysis only — it will not name or profile individuals.
- Reflects US-government perspective and is annual, so it can lag fast-moving situations.
- OpSec: passive government-document reading.

## Overlaps ("do both")
- Complements sanctions lists (OFAC), corporate registries, and trade-data tools — INCSR sets the jurisdictional context; those provide the entity- and person-level specifics.

## Trust & verifiability
`trust: trusted` — an authoritative first-party State Department publication; reliable for US-government country assessments within its policy framing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | narcotics-control-reports |
| category | public-records |
| selectorsIn → selectorsOut | (none) → (none) |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

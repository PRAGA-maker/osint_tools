---
id: samhsa
name: SAMHSA (data & treatment locator)
description: Use when you have a `geolocation` and want US behavioral-health context — returns treatment-facility `address` listings by area plus national substance-use/mental-health statistics.
url: https://www.samhsa.gov/data/
category: public-records
path:
- public-records
bestFor: Aggregate US substance-use / mental-health data and locating treatment facilities in an area (facility addresses, not patient records).
selectorsIn:
- geolocation
selectorsOut:
- address
status: live
pricing: free
costNote: Free US-government data and locator; no account or payment.
opsec: passive
opsecNote: Reading published government data and searching a public facility locator transmits nothing about any individual, and returns facility (not patient) information. Fully passive. Patient/treatment records are confidential (42 CFR Part 2 / HIPAA) and are NOT available here.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party US government agency (SAMHSA, part of HHS). Authoritative for national behavioral-health statistics and the official treatment-facility directory.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
aliases:
- Substance Abuse and Mental Health Services Administration
- FindTreatment.gov
- samhsa.gov
tags:
- toddington
- curated-directory
- academic-scholarly-research-tools
- public-health
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# SAMHSA (data & treatment locator)

> The US behavioral-health agency's public data hub and treatment-facility locator — national statistics plus a searchable directory of substance-use and mental-health facilities by area.

## When to use
You need US behavioral-health *context* rather than person-level data. Two uses: (1) SAMHSA's data portal gives authoritative national/state statistics on substance use and mental health (base rates, trends) to frame an analysis; (2) the linked FindTreatment.gov locator lists licensed treatment facilities by location — useful when building area context for a vulnerable or missing person who may be seeking treatment. Note: individual patient/treatment records are strictly confidential and are NOT here.

## How to use it (`bestInteractionPattern`: web-manual)
1. For statistics, open https://www.samhsa.gov/data/ and browse the reports/datasets (NSDUH, TEDS, N-SSATS) or query the data via its APIs.
2. For facilities, use FindTreatment.gov: enter a city/ZIP (`geolocation`) to list treatment facilities with names, addresses, and services.
3. Read the facility results for `address`, services offered, and payment/eligibility notes.
4. Use statistics to contextualise base rates; use facility listings to understand what services exist near a location of interest.
5. Pivot: facility addresses feed area/mapping work and lawful, appropriate outreach; statistics support risk/context assessment — never treat presence of facilities as evidence about a specific person.

## Inputs → Outputs
- **In:** `geolocation` (city/ZIP, for the locator) or a statistical topic
- **Out:** `address` (treatment-facility listings), aggregate substance-use / mental-health statistics
- **Empty/negative result looks like:** no facilities near the location, or no dataset for your query — sparse coverage in rural areas; broaden the radius or topic.

## Gotchas & OpSec
- **No person-level data.** Patient and treatment information is protected (42 CFR Part 2, HIPAA) — do not expect or attempt to obtain who is in treatment. This tool is context, not a locator of individuals.
- Statistics are aggregate; do not infer anything about a specific person from them.
- Fully passive and authoritative for what it does cover.

## Overlaps ("do both")
- Pairs with general mapping/people tools for area context — SAMHSA provides the authoritative facility directory and public-health baseline, which frame (never substitute for) person-level investigation done through lawful channels.

## Trust & verifiability
`trust: trusted` — a first-party US government agency; its statistics and facility directory are authoritative, with the firm boundary that no individual/patient data is (or should be) accessible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | samhsa |
| category | public-records |
| selectorsIn → selectorsOut | geolocation → address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

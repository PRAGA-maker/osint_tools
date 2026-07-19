---
id: mappingpoliceviolence-org
name: Mapping Police Violence
description: Use when you have a `name`, date, or `geolocation` and want to check whether a person was killed by U.S. police — returns documented killings with victim name, date, location, agency, and circumstances.
url: https://mappingpoliceviolence.org/
category: public-records
path:
- public-records
bestFor: Searching a U.S. database of people killed by police, by victim name, date, location, or agency.
selectorsIn:
- name
- geolocation
selectorsOut:
- document-id
- physical-description
- employer-org
status: live
pricing: free
costNote: Free public research database; no account required. Data is downloadable.
opsec: passive
opsecNote: You search a published research database compiled from public records and news; no one is notified. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A well-known research project aggregating police-killing data from news reports, public records, and databases (e.g. Fatal Encounters, official sources); widely cited, though counts are estimates dependent on reporting and may lag or vary by source.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- mappingpoliceviolence.org
- MPV
tags:
- police-violence
- public-records
- deaths
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# Mapping Police Violence

> A research database of people killed by U.S. police, compiled from news, public records, and other datasets — searchable and mappable by victim name, date, location, and agency. A source for confirming and detailing a death in police custody or a police encounter.

## When to use
You have a `name`, an approximate date, or a `geolocation` and need to know whether the person was killed by police in the U.S., or to profile police killings in an area/by an agency. Directly relevant to death investigations and to cases where a person's fate may involve law enforcement: it can confirm a death, supply the circumstances and responsible agency, and anchor date/place.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://mappingpoliceviolence.org/.
2. Use the search/filter and map to look up a victim `name`, or filter by state/city (`geolocation`), date range, or agency.
3. Open a record for the details: victim name, age/`physical-description` attributes (race, gender, age), date, location, the `employer-org` (police agency), and a summary of circumstances with source links.
4. Follow the cited sources (news, official documents) to verify each detail.
5. Pivot: the agency and date feed news-archive, court-record, and police-misconduct searches; victim identity feeds people/obituary searches for next of kin.

## Inputs → Outputs
- **In:** `name`, date, or `geolocation`
- **Out:** `document-id` (incident record with circumstances/sources), victim `physical-description` attributes, and the `employer-org` (police agency)
- **Empty/negative result looks like:** no matching record — the database captures *documented* police killings; absence means it isn't in this dataset (unreported, non-fatal, or outside scope), not that no incident occurred. Cross-check with Fatal Encounters/official data.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: fully **passive** — a published database of public records.
- Data caveats: counts are estimates dependent on media/public-records reporting and can lag, vary between databases, or be revised; always confirm a specific record against its cited primary sources.

## Overlaps ("do both")
- Pairs with Fatal Encounters, the Washington Post police-shootings database, and [[policecrime-bgsu-edu]] — MPV maps killings broadly; the others differ in scope (all fatal encounters, on-duty shootings, or officer arrests), so cross-referencing fills gaps and confirms details.

## Trust & verifiability
`trust: trusted` — a widely-cited research project built from public records and news with per-incident source links; reliable for documented cases, with the standard caveat that aggregate counts are reporting-dependent estimates to be verified against primary sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mappingpoliceviolence-org |
| category | public-records |
| selectorsIn → selectorsOut | name, geolocation → document-id, physical-description, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

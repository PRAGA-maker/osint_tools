---
id: the-philadelphia-police-misconduct-database
name: The Philadelphia Police Misconduct Database
description: Use when you have a Philadelphia police officer's `name` and want their disciplinary/arbitration history — returns per-officer misconduct case records and arbitration outcomes.
url: https://datawrapper.dwcdn.net/3GbVI/1/
category: public-records
path:
- public-records
bestFor: Looking up a named Philadelphia police officer's disciplinary and arbitration outcomes.
selectorsIn:
- name
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free, public searchable table (journalism data project); no account or payment.
opsec: passive
opsecNote: Passive — a static, public data visualization; searching it is not logged against you in any meaningful way and does not notify the officer. Standard browser hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A journalism-built database of ~170 arbitration outcomes since 2011; accurate to its sourced records but narrow in scope (arbitration cases, not the full disciplinary universe).
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Philadelphia police arbitration database
tags:
- police-misconduct
- accountability
- public-records
source: osint4all
lastVerified: '2026-07-21'
enrichment: full
relatedTools:
- arizona-le-database-abc15
- clearview-ai-us-taxpayer-funded-entities
- cop26-registered-attendees
- how-many-untested-rape-kits-does-your-city-police-department-or-county-sheriff-s-office-have
- independent-fundamental-baptist-sexual-misconduct-database
---

# The Philadelphia Police Misconduct Database

> A searchable journalism dataset of Philadelphia police arbitration outcomes — type an officer's name to pull the cases where discipline was imposed, reversed, or reduced.

## When to use
You have the `name` of a Philadelphia police officer and want their **disciplinary/arbitration record** — for accountability reporting, vetting, or corroborating a complaint. The dataset covers ~170 arbitration outcomes since 2011, documenting how often the Fraternal Order of Police reversed or reduced department discipline (more than two-thirds of the time). It's a narrow but concrete public-records source on a specific officer's history.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the searchable table at https://datawrapper.dwcdn.net/3GbVI/1/.
2. Type the officer's `name` in the search box.
3. Click a name to open the case record(s) — the misconduct at issue and the arbitration outcome (upheld / reduced / reversed).
4. Note the date and disposition for your timeline.
5. Pivot: a confirmed officer name + outcome feeds news-archive and court-record searches for the underlying incident, and other police-accountability databases in other jurisdictions.

## Inputs → Outputs
- **In:** a Philadelphia police officer `name`
- **Out:** matching misconduct/arbitration case record(s) and outcome(s) (`document-id`-style entries)
- **Empty/negative result looks like:** no match — the officer isn't among the ~170 arbitration cases (most officers aren't), the name is spelled differently, or their case predates/postdates the dataset; absence is not exoneration.

## Gotchas & OpSec
- **Scope is narrow**: arbitration outcomes only, Philadelphia only, 2011-onward — not a complete disciplinary or complaint record.
- It's a fixed dataset (a published chart); it won't reflect cases after its last update — treat it as historical.
- Same-name officers are possible; corroborate with the case details before attributing.

## Overlaps ("do both")
- Pairs with other jurisdiction police-accountability datasets (e.g. `[[arizona-le-database-abc15]]`) and with local court/news archives to flesh out an incident.

## Trust & verifiability
`trust: community` — a journalism data project; entries are as reliable as their sourced arbitration records, but confirm the underlying case in court/news records before publishing a claim.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-philadelphia-police-misconduct-database |
| category | public-records |
| selectorsIn → selectorsOut | name → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

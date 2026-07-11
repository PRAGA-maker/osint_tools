---
id: independent-fundamental-baptist-sexual-misconduct-database
name: Independent fundamental Baptist sexual misconduct database
description: Use when you have a `name` possibly tied to Independent Fundamental Baptist church abuse and want the Star-Telegram's documented cases — returns accused `name`, `employer-org` (church/school), and `geolocation` of where they worked.
url: https://datawrapper.dwcdn.net/UyECh/20/
category: public-records
path:
- public-records
bestFor: Checking a name against a journalistic database of documented IFB-church sexual-misconduct allegations and where the accused worked.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- geolocation
status: live
pricing: free
costNote: Free to view; a public interactive database embedded from the Fort Worth Star-Telegram investigation.
opsec: passive
opsecNote: Viewing a published journalistic database is passive and notifies no one. The data concerns allegations and convictions — handle it responsibly, avoid defamatory conclusions, and note that "alleged" entries are not proven guilt.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Compiled by Fort Worth Star-Telegram investigative reporters ("Spirit of Fear," 2018); a credible journalistic dataset, but entries mix convictions and allegations and it is a point-in-time snapshot.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Spirit of Fear database
- IFB sexual misconduct database
- Star-Telegram IFB abuse database
tags:
- misconduct
- abuse-database
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# Independent fundamental Baptist sexual misconduct database

> The Fort Worth Star-Telegram's "Spirit of Fear" investigation database — 400+ documented sexual-misconduct cases across Independent Fundamental Baptist churches/schools, searchable by name and place.

## When to use
You are vetting or tracing a subject connected to Independent Fundamental Baptist (IFB) churches, schools, camps, or ministries in the US/Canada and want to check them against a documented record of abuse allegations and convictions. The database also maps every church/school/camp where an identified accused person worked (including before/after the alleged abuse), which can explain a person's movements or connect a name to an institution.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the database (embedded at https://datawrapper.dwcdn.net/UyECh/20/; also reachable via the Star-Telegram "Spirit of Fear" series).
2. Search/scan for the subject's `name` or the `employer-org` (church/school/camp).
3. Read the entry: accused `name`, the institution(s) (`employer-org`), locations worked (`geolocation`), and the case status (allegation vs. conviction).
4. Distinguish alleged from adjudicated cases carefully before drawing any conclusion.
5. Pivot: an institution links to other names in the dataset; a conviction feeds court-record and sex-offender-registry checks; locations feed a movement timeline.

## Inputs → Outputs
- **In:** `name` (or church/institution `employer-org`)
- **Out:** accused `name`, `employer-org` (church/school/camp), `geolocation` of workplaces, case status
- **Empty/negative result looks like:** no entry — the database covers only the ~187 institutions and cases the 2018 investigation documented, so absence is NOT evidence of innocence or that no case exists; it means this specific dataset doesn't list them.

## Gotchas & OpSec
- Point-in-time (2018) and scoped to what the investigation documented — not a live or comprehensive registry.
- Entries mix allegations and convictions; never present an "alleged" entry as proven. Defamation risk if misused.
- Corroborate any actionable finding against court records and official registries.

## Overlaps ("do both")
- Pairs with state sex-offender registries and court-record search — the database gives the IFB-specific context and institutional links, while registries/courts give the authoritative legal status.

## Trust & verifiability
`trust: community` — a credible journalistic dataset from named investigative reporters; still verify each case's current legal status against primary court/registry sources before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | independent-fundamental-baptist-sexual-misconduct-database |
| category | public-records |
| selectorsIn → selectorsOut | name → name, employer-org, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

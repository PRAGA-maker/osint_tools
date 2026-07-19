---
id: ice-patrol
name: ICE Patrol
description: Use when you have a `name` or `employer-org` and want to check WikiLeaks' 2018 scrape of ~9,000 US ICE-linked LinkedIn profiles — returns job, location and school details.
url: https://ice.wikileaks.org/search
category: public-records
path:
- public-records
bestFor: Looking up whether a person appears in the 2018 ICEPatrol dataset of US Immigration & Customs Enforcement staff, searchable by name/location/employer/school.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
- address
- social-profile
status: degraded
pricing: free
costNote: Free to search; no account. A static 2018 snapshot, not maintained or updated.
opsec: passive
opsecNote: Read-only search of a published archive; queries are not attributed to your subject. The data names real individuals scraped from LinkedIn — handle as sensitive PII, and note that hosting/availability is intermittent (WikiLeaks infrastructure returns errors at times).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Published by WikiLeaks from data originally collected by researcher Sam Lavigne from public LinkedIn profiles. The source profiles were public, but the dataset is a frozen 2018 scrape and may be stale or contain mismatches.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- akp-email-database
- dnc-email-database
- gi-files
- leaked-cables
- macron-campaign-emails
- sony-archives
- wikileaks
- wikileaks-search
aliases:
- ICEPatrol
- WikiLeaks ICE database
tags:
- public-records
- wikileaks
- us
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# ICE Patrol

> WikiLeaks' searchable 2018 archive ("ICEPatrol") of ~9,000 LinkedIn profiles of people linked to US Immigration and Customs Enforcement, filterable by name, location, position, employer and school.

## When to use
You have a `name` or an `employer-org` (ICE, CBP, DHS or a contractor) and want to check whether a person appears in this frozen 2018 dataset of ICE-affiliated LinkedIn profiles. It can corroborate a subject's past government/immigration-enforcement employment, position, city and education. Scope is narrow and dated — it is only useful when your subject plausibly worked in that orbit around 2018.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ice.wikileaks.org/search (if it errors, retry later — the host is intermittently unavailable).
2. Search by name, or filter by location, job position, company/agency, school or field of study.
3. Open a matching entry to read the scraped profile fields — job title, `employer-org`, city (`address`), education, and the original `social-profile` reference.
4. Treat every hit as a 2018 snapshot: the person may have changed roles, and common-name collisions are possible.
5. Pivot: a confirmed name/employer feeds current people-search and LinkedIn checks to see what changed since 2018.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** `name`, `employer-org` (agency/position), `address` (city), `social-profile` (LinkedIn-derived), education
- **Empty/negative result looks like:** no match — the person wasn't in the 2018 scrape, used a different name on LinkedIn, or joined/left ICE outside that window. Absence proves nothing about current employment.

## Gotchas & OpSec
- Human-in-the-loop: none; but the host frequently returns errors/timeouts — availability is unreliable.
- OpSec: **passive**; the subject is not notified. The dataset is sensitive PII — handle accordingly and lawfully.
- Frozen at 2018 and scraped from self-reported LinkedIn data; expect staleness and occasional mismatches. Corroborate before drawing conclusions.

## Overlaps ("do both")
- Pairs with [[wikileaks-search]] and current LinkedIn/people-search tools — this gives the 2018 baseline, the others show what changed.

## Trust & verifiability
`trust: community` — a documented WikiLeaks publication built from originally-public LinkedIn data; authentic as an archive, but static, dated, and dependent on flaky hosting, so verify any match against current sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ice-patrol |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org, address, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

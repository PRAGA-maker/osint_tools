---
id: credibly-accused
name: ProPublica — Credibly Accused
description: Use when you have a `name` (or diocese/location) and want to check whether a US Catholic clergy member was named on a credibly-accused-of-abuse list — returns the name, diocese/order, and jurisdiction.
url: https://projects.propublica.org/credibly-accused/
category: public-records
path:
- public-records
bestFor: Checking whether a US Catholic clergy member appears on official credibly-accused-of-sexual-abuse lists, by name or diocese.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- geolocation
status: degraded
pricing: free
costNote: Free public database from ProPublica; no account or payment. Note it is a static snapshot last updated January 2020, not a live-maintained register.
opsec: passive
opsecNote: Searching a published journalistic database is passive and anonymous; no notification to anyone. Handle results responsibly — these are serious allegations compiled from diocesan disclosures; corroborate before acting.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Compiled and published by ProPublica from diocese/religious-order disclosure lists; a reputable, sourced aggregation of the church's own published names.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- ProPublica Credibly Accused
- Catholic clergy abuse database
tags:
- offenders
- background-check
- us
- clergy
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
relatedTools:
- 527-explorer
- coronavirus-bailouts-search-every-company-approved-for-federal-loans-over-150k
- nonprofit-explorer
- nursing-home-inspect
- parler-capitol-videos
- police-protest-videos
- the-nypd-files
---

# ProPublica — Credibly Accused

> ProPublica's searchable aggregation of US Catholic clergy named on dioceses' own "credibly accused of sexual abuse" lists — a background source keyed on name, diocese, and location.

## When to use
You have a subject `name` connected to the US Catholic Church (clergy, religious order) and want to check whether they appear on an official credibly-accused list. Because dioceses published these lists piecemeal (and some not at all), ProPublica consolidated ~6,770 names into one searchable place. A hit gives the accused's `name`, the diocese/order (`employer-org`), and the jurisdiction/location (`geolocation`) — useful for safeguarding and background context. Treat it as a pointer to the underlying diocesan disclosure, not a legal finding.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://projects.propublica.org/credibly-accused/.
2. Search by clergy `name`, diocese/city, or geographic location.
3. Read the record: accused `name`, affiliated diocese/order (`employer-org`), and which jurisdiction released the list.
4. Pivot: the diocese/order and jurisdiction point you to the original published list for the authoritative detail; the name feeds broader court/news searches for case specifics.

## Inputs → Outputs
- **In:** `name` (or diocese / location)
- **Out:** accused clergy `name`, diocese/order `employer-org`, jurisdiction `geolocation`
- **Empty/negative result looks like:** no match — the person may not be listed, their diocese may be among those that never released a list (≈41 orders/dioceses), or the 2020 snapshot predates a later disclosure. Absence is not exoneration or proof.

## Gotchas & OpSec
- **Static snapshot (Jan 2020)** — not updated since; newer disclosures won't appear, so cross-check the diocese's current list.
- "Credibly accused" reflects the church's own assessment, not a criminal conviction; represent it accurately and corroborate.
- OpSec: passive; nobody is notified.

## Overlaps ("do both")
- Do both with court-record and news-archive searches (for case outcomes) and the diocese's own current disclosure list, since this database is a consolidated but frozen 2020 view.

## Trust & verifiability
`trust: trusted` — a reputable ProPublica compilation sourced directly from dioceses' published lists; the main caveat is its age, not its sourcing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | credibly-accused |
| category | public-records |
| selectorsIn → selectorsOut | name → name, employer-org, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

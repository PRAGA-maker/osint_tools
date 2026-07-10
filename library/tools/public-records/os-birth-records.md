---
id: os-birth-records
name: OnlineSearches Birth Records
description: Use when you have a `name` and want a state-by-state directory of official birth/vital-record sources — returns links to `dob`, `name` and `associate` (parent/family) record lookups.
url: http://publicrecords.onlinesearches.com/birth-records.htm
category: public-records
path:
- public-records
bestFor: A free directory that routes you to the correct county/state government birth and vital-records office for a jurisdiction, rather than searching records itself.
selectorsIn:
- name
selectorsOut:
- associate
- dob
- name
status: degraded
pricing: free
costNote: The directory itself is free. It links to government offices (some free) and, for personal-detail lookups, may route to Intelius.com, which is paid. The specific /birth-records.htm deep link may 404 — navigate from the site root instead.
opsec: passive
opsecNote: Browsing a directory of record sources is passive and untied to the subject. Following a link to Intelius or a paid people-search is where you'd start leaving an account/payment trail — stop before that if you want to stay anonymous.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: OnlineSearches is an Intelius-affiliated directory of public-record links; useful as a jurisdiction router, but it monetizes by funneling to paid people-search, so it is not a neutral authority.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- OnlineSearches
- publicrecords.onlinesearches.com
- birth records directory
tags:
- genealogy
- family
- vital-records
- public-records
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# OnlineSearches Birth Records

> A free, Intelius-affiliated directory that points you to the right government birth/vital-records office for any US state or county — a router, not a search engine.

## When to use
You have a `name` and need the official source for birth or vital records in a specific jurisdiction, but you don't know which county/state office holds them or where its online lookup lives. OnlineSearches maps the fragmented US vital-records landscape so you land on the correct government portal. Birth records establish `dob` and, crucially, parent names — a strong `associate`/family pivot in genealogy and missing-person work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://publicrecords.onlinesearches.com/ (the deep `/birth-records.htm` link may 404 — start from the root and pick **Vital / Birth Records**).
2. Drill down by state, then county, to the relevant office.
3. Follow the link to the government source and run its search there, or note the offline request procedure. The directory tells you whether records are online-free, paid, or offline-only.
4. Be aware some paths route to **Intelius.com** for "additional details" — that is the paid, non-government branch; use it only if you accept the cost and trail.
5. Pivot: parent names from a birth record → `associate` mapping and reverse-genealogy; confirmed `dob` → people-search and public-records cross-checks.

## Inputs → Outputs
- **In:** `name` (plus jurisdiction to narrow)
- **Out:** links yielding `dob`, `name` (full legal), `associate` (parents/family) — depending on the destination office
- **Empty/negative result looks like:** the directory lists an office with no online search (records are request-only by mail/in-person), or the deep link 404s. That means "go offline/by-mail," not "no record exists."

## Gotchas & OpSec
- **It's a directory, not a database** — it rarely returns the record itself; it sends you to the source. Don't expect a name-in, record-out experience.
- Watch for the Intelius funnel: government links are free; the "get more details" links are paid people-search.
- The exact `birth-records.htm` URL is degraded/moved; navigate from the site root.
- OpSec: passive while browsing; following through to a paid lookup creates an account/payment trail.

## Overlaps ("do both")
- Pairs with genealogy platforms (FamilySearch, ancestry sites) and with `[[courthousedirect-com]]` for the property/family side — the directory finds the office, those tools pull the actual records.
- Cross-check any `dob`/parent lead against a people-search to confirm identity.

## Trust & verifiability
`trust: unverified` — a link directory with a commercial (Intelius) incentive. The government destinations it points to are authoritative; OnlineSearches itself is just the map, so verify at the official office.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | os-birth-records |
| category | public-records |
| selectorsIn → selectorsOut | name → associate, dob, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

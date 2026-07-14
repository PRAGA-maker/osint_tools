---
id: os-divorce-records
name: OS Divorce Records
description: Use when you have a `name` and want to reach the official US county/state agency that holds that person's divorce (dissolution) record — returns links to associate, dob and address leads.
url: http://publicrecords.onlinesearches.com/divorce-records.htm
category: public-records
path:
- public-records
bestFor: Finding which US county/state office to query for a subject's divorce/dissolution record.
selectorsIn:
- name
selectorsOut:
- associate
- address
- dob
status: live
pricing: free
costNote: The OnlineSearches directory itself is free (Intelius-operated); it hands you off to official county/state record portals, some of which charge per-copy fees for certified documents.
opsec: passive
opsecNote: Browsing the directory and the linked government portals is passive — you are reading public indexes, not alerting the subject. If a linked portal requires an account or logs searches, treat that specific hop as active and use a sock-puppet.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: OnlineSearches is a commercial directory (Intelius-powered) that aggregates links to genuine government record sources; the directory is a signpost, the authoritative data lives at the linked official agency.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- OnlineSearches Divorce Records
- publicrecords.onlinesearches.com
tags:
- genealogy
- family
- divorce-records
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# OS Divorce Records

> A free directory that routes a name-plus-location lead to the correct US county or state office holding divorce/dissolution records.

## When to use
You have a `name` and a rough `geolocation` (state/county) for a US subject and need to establish a former spouse (`associate`), a prior married surname, or a divorce date/venue that anchors an `address` at a point in time. OnlineSearches does not itself hold the record — it tells you *which* clerk-of-court or vital-records office to query, which is the hard part of US public-records work where jurisdiction is fragmented by county.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the OnlineSearches divorce-records section. If the deep link 404s (the site reorganizes its static pages), start at `http://publicrecords.onlinesearches.com/` and drill Divorce Records → State → County.
2. Pick the subject's state, then county, to reach the list of official offices (Clerk of Superior/Circuit Court, Department of Health / Vital Records) that hold dissolution filings for that jurisdiction.
3. Follow the outbound link to the official portal and run the actual name search there.
4. Read the record: a divorce filing typically yields both spouses' names (`associate`), the filing date, the court/venue (a `geolocation`/`address` anchor), and sometimes DOB or age.
5. Pivot: a former-spouse name feeds people-search and `[[the-law-pages]]`-style court lookups; a prior surname widens username/name enumeration.

## Inputs → Outputs
- **In:** `name` (+ US state/county to narrow jurisdiction)
- **Out:** `associate` (former spouse), `address`/venue lead, `dob`/age where the record exposes it
- **Empty/negative result looks like:** the county page lists only paid third-party links or "no online index available" — meaning the record exists only on paper at the courthouse, not that no divorce occurred. Absence here is not evidence of absence.

## Gotchas & OpSec
- Human-in-the-loop: you manually choose the jurisdiction and then work an external portal; there is no single search box that spans all US counties.
- Not an FCRA source — OnlineSearches states its data may not be used for employment, tenant, or credit decisions.
- Some links route to Intelius/partner paywalls; distinguish the free official-agency link from the upsell.

## Overlaps ("do both")
- Pairs with `[[find-people-search-us]]` because the people-search surfaces the associate/relative graph while this pins the authoritative court record behind it.

## Trust & verifiability
`trust: community` — the directory is a commercial aggregator, so verify every hit against the actual government source it links to; the value is the correct-jurisdiction pointer, not OnlineSearches' own data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | os-divorce-records |
| category | public-records |
| selectorsIn → selectorsOut | name → associate, address, dob |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |

---
id: us-federal-election-commission
name: US Federal Election Commission (FEC) Data
description: Use when you have a US `name` and want political donations that reveal address, employer and occupation — returns address, employer-org and dob-era leads.
url: https://fec.gov/data
category: public-records
path:
- public-records
- us-political-records
bestFor: Searching itemized US federal campaign contributions by donor name to recover self-reported address, employer and occupation.
selectorsIn:
- name
- employer-org
selectorsOut:
- address
- employer-org
- associate
status: live
pricing: free
costNote: Free official US government data and API; no account needed (an API key raises rate limits).
opsec: passive
opsecNote: Searching public, legally mandated disclosure records is fully passive and does not touch the subject. No sock puppet needed beyond normal hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Authoritative US federal agency; contributors self-report the data by law, so fields are as accurate as the donor's own filing.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- campaign-finance-reports-and-data
aliases:
- FEC
- fec.gov
- OpenFEC
tags:
- campaign-finance
- us
- public-records
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# US Federal Election Commission (FEC) Data

> The federal campaign-finance database — one of the richest free people-search sources in the US, because donors self-report their name, city, ZIP, employer, and occupation by law.

## When to use
You have a US `name` and want independent, government-held identity anchors. Anyone who has given to a federal campaign, PAC, or committee appears in itemized records with their **self-reported address (city/state/ZIP), employer, and occupation**, plus the date and amount. That single line can confirm a location, reveal a current/past `employer-org`, hint at ideology/associations, and — across multiple donations over years — build a residence-and-employment timeline. Excellent for confirming identity and locating people who are otherwise hard to place.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://fec.gov/data and open "Individual contributions" (or "Receipts").
2. Search by contributor `name`; filter by state, employer, date range, or recipient committee to disambiguate.
3. Read each record: name, city/state/ZIP, employer, occupation, amount, date, recipient.
4. For scale/automation, use the OpenFEC API (`/schedules/schedule_a/`) with a free API key.
5. Pivot: reported `address` → residence timeline and reverse-address lookups; `employer-org`/occupation → workplace confirmation; recipient committees and co-donors at the same address → household members/`associate`s and ideology.

## Inputs → Outputs
- **In:** `name` (optionally `employer-org`, state, or date to disambiguate)
- **Out:** `address` (city/state/ZIP), `employer-org` (+ occupation), `associate` (co-donors/household), plus donation dates
- **Empty/negative result looks like:** no itemized records — the person never gave above the itemization threshold, gave only to non-federal (state/local) campaigns, or used a name variant; absence is not proof of anything.

## Gotchas & OpSec
- Only **federal** contributions above the itemization threshold appear — small or state/local donations won't; check state campaign-finance sites separately.
- Data is **self-reported** by the donor and can be misspelled, abbreviated, or list "self/retired"; treat employer/occupation as leads.
- Common names collide — anchor on city/ZIP/employer before attributing.
- OpSec: passive; safe.

## Overlaps ("do both")
- Pairs with state campaign-finance databases and voter/records tools — FEC covers federal giving with rich employer/address fields; state sources and people-search fill the gaps and corroborate the address/employer it surfaces.

## Trust & verifiability
`trust: trusted` — an authoritative federal disclosure system; the records are genuine filings, though each field is only as accurate as the donor's self-report, so corroborate identity via the address/employer details.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | us-federal-election-commission |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → address, employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

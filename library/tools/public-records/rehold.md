---
id: rehold
name: Rehold
description: Use when you have a US `address` and want current/historical residents plus their phones — returns `name`, `phone`, `associate`, property details.
url: https://rehold.com/
category: public-records
path:
- public-records
bestFor: Reverse US address lookup returning current and past residents, neighbors and phone numbers.
selectorsIn:
- address
- name
- phone
selectorsOut:
- name
- phone
- associate
- address
status: live
pricing: freemium
costNote: Reverse address/phone lookups return free results; unlimited profile access and some contact details prompt a paid subscription.
opsec: passive
opsecNote: Queries Rehold's aggregated public-records dataset, not the subject; no notice reaches the person. As with all people-aggregators, treat results as leads and mind local data-protection rules when acting on them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial data-broker aggregation of public property and contact records; coverage is broad but records can be stale or conflated between people at the same address.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Rehold.com
- Rehold Address Directory
tags:
- property
- reverse-address
- people-search
- public-records
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Rehold

> A free US reverse-address directory — enter a street address and get current and historical residents, neighbors, phone numbers and property facts.

## When to use
You have a US `address` (or a `name`/`phone` you want to place at one) and you need to know who lives or lived there: current residents, historical occupants with move-in/out timing, neighbors, and associated phone numbers. Strong for building a residence timeline for a missing person or confirming an associate's address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://rehold.com/ and enter the property `address` (house number, street, city/state) in the reverse-address search — or use the reverse-phone/name entry points.
2. Open the property profile: current resident `name`(s), historical residents with timestamps, phone numbers, neighbors (`associate` leads), and property description/assessment/sales history.
3. Cross-reference the historical-resident timeline against your subject's known moves to date their presence at the address.
4. Note which fields are gated — some phone/contact details push a subscription; capture what free results give first.
5. Pivot: resident names feed people-search and social lookups; phones feed phone-OSINT; neighbors are interview/associate leads; sales history feeds county recorder records.

## Inputs → Outputs
- **In:** `address` (primary), or `name` / `phone`
- **Out:** current + historical residents (`name`), `phone` numbers, neighbors (`associate`), property description, assessment and sales history
- **Empty/negative result looks like:** a bare property record with no resident names (new construction, commercial, or thin data), or an address not in the dataset — absence does not mean the property is vacant.

## Gotchas & OpSec
- Human-in-the-loop: none to search; deeper contact fields prompt a paid plan.
- OpSec: **passive** — the subject is not notified. Data-broker records can conflate multiple people who shared an address; verify before attributing a phone to a specific person.
- US-only coverage; freshness varies — a "current resident" may reflect a lagging public-records snapshot.

## Overlaps ("do both")
- Combine with a county recorder / assessor lookup to confirm ownership vs. tenancy, since Rehold blends both.
- Pairs with a reverse-phone tool to validate the phone numbers Rehold surfaces before trusting them.

## Trust & verifiability
`trust: community` — a commercial aggregator of public records; broad and useful for leads, but individual name/phone associations should be corroborated against a primary source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rehold |
| category | public-records |
| selectorsIn → selectorsOut | address, name → name, phone, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: traderegistry-ae
name: traderegistry.ae
description: Use when you have a UAE `employer-org`, `name`, or `address` and want official-style trade-register company reports — returns `employer-org`, `address`, `name`, and `associate` (owners/managers).
url: https://traderegistry.ae/product/company-search-report/
category: public-records
path:
- public-records
bestFor: Ordering current/historical company reports and extracts for UAE-registered entities from a trade-register smart portal.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- address
- name
- associate
status: live
pricing: freemium
costNote: A basic company-name search/lookup is free, but the substantive Company Search Report and Trade Register Extract (with owners, managers, history, documents) are paid, per-report products.
opsec: passive
opsecNote: Searching and ordering a report queries a registry portal, not the subject, who is not notified. Purchasing a report ties the order to your payment/contact identity on the portal — use appropriate separation for sensitive inquiries.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial "smart portal" reselling UAE trade-register data; it is not the emirate government registry itself (e.g. DED / u.ae National Economic Register). Verify critical facts against the official government source.
missingPersonsRelevance: high
coverage:
- ae
auth: none
api: false
localInstall: false
registration: false
aliases:
- UAE Trade Registry Smart Portal
- traderegistry.ae
tags:
- companysites
- Company Related Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# traderegistry.ae

> A commercial UAE "trade-register smart portal" that sells company search reports and extracts — useful for UAE corporate detail, but not the official government registry.

## When to use
Your subject is tied to a UAE-registered company and you want its registered details, ownership/management, and history in one report. UAE company information is otherwise fragmented across emirate-level Departments of Economic Development and free zones, so a consolidated report can save legwork — provided you treat it as commercial data to verify, not an authoritative primary source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://traderegistry.ae/ and use the company search to look up the `employer-org` by name.
2. Confirm the entity in the free basic results.
3. To get detail, order the paid **Company Search Report** (current + historical info and documents) or the **Trade Register Extract** (basic official-style particulars).
4. Read the report: registered `employer-org`, `address`, and named owners/managers (`associate`, `name`).
5. Cross-check against the official UAE source (u.ae National Economic Register / the relevant emirate DED / free-zone registry) before relying on any fact. Pivot owner names into people-search.

## Inputs → Outputs
- **In:** `employer-org` (company name), or `name`/`address` to search
- **Out:** `employer-org`, `address`, owner/manager `name`s and `associate` links (in the paid report)
- **Empty/negative result looks like:** no match — the company may be in a free zone or emirate not covered by this reseller, dissolved, or registered under an Arabic name. Meaningful detail sits behind the paid report; the free search is only a name check.

## Gotchas & OpSec
- **Not the government registry.** It resells/compiles data; the authoritative sources are u.ae's National Economic Register and the emirate DEDs/free zones. Verify there.
- Paid per report — budget accordingly, and don't assume completeness across all emirates and free zones.
- Arabic vs. transliterated company names can cause misses; try variants.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]` and the official **u.ae National Economic Register** — use the official register to authoritatively confirm anything this portal reports, and OpenCorporates for free cross-border links.

## Trust & verifiability
`trust: unverified` — a commercial reseller, not the primary registry; treat its reports as leads and confirm against the official UAE government sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | traderegistry-ae |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, address, name, associate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |

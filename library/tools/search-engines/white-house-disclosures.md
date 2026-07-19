---
id: white-house-disclosures
name: White House Disclosures
description: Use when you have a `name` of a White House official or staffer and want their public financial-disclosure and ethics filings — returns OGE 278 financial disclosures, ethics waivers, transaction reports, and staff salary listings.
url: https://www.whitehouse.gov/disclosures/
category: search-engines
path:
- search-engines
bestFor: Retrieving White House staff financial disclosures, ethics waivers, periodic transaction reports, and salary/title listings.
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- employer-org
- associate
status: live
pricing: free
costNote: Free official U.S. government disclosures page; no account. Some individual OGE 278 reports require a simple request form.
opsec: passive
opsecNote: You download published U.S. government ethics filings; the official is not notified. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party whitehouse.gov publication of legally-required ethics/financial filings; authoritative, though the specific documents posted change with each administration and over time.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- whitehouse.gov disclosures
- White House financial disclosures
tags:
- government-data
- financial-disclosure
- ethics
- public-records
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# White House Disclosures

> The official whitehouse.gov repository of executive-office ethics and financial filings — OGE Form 278 financial disclosures, ethics waivers, periodic transaction (securities) reports, and annual staff title/salary listings. A primary source on the finances and interests of named officials.

## When to use
You have a `name` that is (or was) a White House official, senior appointee, or staffer, and you want their public financial picture: assets, income sources, outside positions, securities trades, granted ethics waivers, or their government salary/title. Financial disclosures are rich for OSINT — they list a person's assets, employers, board seats, and sometimes a spouse's income — making this valuable for profiling an official's interests, conflicts, and associations.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.whitehouse.gov/disclosures/.
2. Browse the sections: **Financial Disclosure Reports** (OGE 278), **Waivers**, **Periodic Transaction Reports**, and the **Annual Report to Congress** on staff titles/salaries.
3. Locate the official by name in the alphabetised lists and open the PDF; for individuals not pre-posted, use the provided request form.
4. Read the filing for assets, income, outside positions, and named entities/associates; note the report date.
5. Pivot: named employers/assets feed company-registry and financial searches; a spouse or business partner named feeds people-search; salary/title corroborates employment.

## Inputs → Outputs
- **In:** `name` (official/staffer) or `employer-org` (the administration/office)
- **Out:** `document-id` (OGE 278 filings, waivers, transaction reports), `employer-org`/asset names, and `associate`s (e.g. spouse, business ties) disclosed in filings
- **Empty/negative result looks like:** the person isn't listed — they may be below the disclosure threshold, in a different agency (check that agency or OGE), or their report requires the request form; absence here isn't proof they filed nothing anywhere.

## Gotchas & OpSec
- Human-in-the-loop: none for posted PDFs; some individual reports need a short request form.
- OpSec: fully **passive** — published government filings; no notification to the subject.
- The set of posted documents is administration- and time-specific; the page's contents change, and historical filings may move to the National Archives. For non-White-House federal officials, use the agency or the OGE/other disclosure portals instead.

## Overlaps ("do both")
- Pairs with congressional/financial-disclosure databases, OpenSecrets, and corporate registries — this covers executive-office filings; those cover legislators, campaign finance, and the companies named in a 278, letting you connect an official's disclosed interests to entities and people.

## Trust & verifiability
`trust: trusted` — first-party whitehouse.gov publication of legally-mandated ethics filings; the documents are authoritative primary sources, with the only caveat that which filings are posted varies by administration and over time.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | white-house-disclosures |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → document-id, employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

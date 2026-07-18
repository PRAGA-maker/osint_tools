---
id: ukons-standard-industrial-classifications-united-kingdom
name: UK ONS Standard Industrial Classifications (SIC)
description: Use when you have a UK company's SIC code or `employer-org` and want to decode its declared industry — returns employer-org context.
url: https://webarchive.nationalarchives.gov.uk/20160105230903/http://www.ons.gov.uk/ons/guide-method/classifications/current-standard-classifications/standard-industrial-classification/index.html
category: dark-web
path:
- dark-web
bestFor: Looking up and interpreting UK Standard Industrial Classification (SIC) codes attached to registered companies.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free UK government reference; no account needed.
opsec: passive
opsecNote: A static reference lookup on a National Archives snapshot — reveals nothing about the subject. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official UK Office for National Statistics classification, preserved on the UK National Archives web archive; authoritative reference data.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- UK SIC codes
- ONS Standard Industrial Classification
tags:
- reference
- company-classification
- uk
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# UK ONS Standard Industrial Classifications (SIC)

> The official UK code list that decodes what a registered company actually does — a reference for turning the cryptic SIC number on a Companies House record into a real industry.

## When to use
You are researching a UK company tied to a subject (an `employer-org` from a Companies House filing, a director search, or a business the person is linked to) and the record only gives a numeric SIC code. This reference translates that code into a human-readable industry sector, letting you understand the nature of the business, spot mismatches (e.g. a "consultancy" coded as something unrelated), and group related entities by activity. It is a lookup table, not a search engine over people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the archived index page (URL above) or the current ONS/Companies House SIC list.
2. Take the SIC code from the company record (Companies House shows it on the company overview).
3. Find the matching code to read its full sector/sub-sector description.
4. Pivot: the decoded activity contextualises the `employer-org`; use it alongside Companies House to interpret a person's business interests and to cluster multiple companies by shared activity.

## Inputs → Outputs
- **In:** `employer-org` (specifically its SIC code)
- **Out:** `employer-org` context — the industry/sector meaning of the code
- **Empty/negative result looks like:** the code isn't in the list (a superseded revision — check the current SIC 2007 edition) or the company filed the generic "non-trading"/"dormant" code, which tells you the entity is inactive.

## Gotchas & OpSec
- This is a **classification reference only** — it decodes codes; it does not look up companies or people. Get the code itself from Companies House first.
- The linked URL is an archived 2016 snapshot; SIC 2007 remains the current scheme, but confirm against the live ONS/Companies House list for the latest sub-codes.
- OpSec: passive reference lookup; nothing is disclosed.

## Overlaps ("do both")
- Pairs with UK Companies House and director-search tools — those give you the company and its SIC code; this turns that code into meaningful industry context.

## Trust & verifiability
`trust: trusted` — authoritative UK government (ONS) classification, preserved on the official National Archives web archive; the mapping is definitive for its scheme edition.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ukons-standard-industrial-classifications-united-kingdom |
| category | dark-web |
| selectorsIn → selectorsOut | employer-org → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

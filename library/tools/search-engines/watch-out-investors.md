---
id: watch-out-investors
name: Watch Out Investors
description: Use when you have a `name` or Indian ID (PAN/CIN/DIN) and want to know if that person or company has been named in an Indian regulatory or economic-offence action — returns matches to `employer-org`, `associate` and disqualification records.
url: http://www.watchoutinvestors.com/default2a.asp
category: search-engines
path:
- search-engines
bestFor: Screening an individual or company against India's aggregated database of economic offenders, defaulters and disqualified directors.
selectorsIn:
- name
- document-id
- employer-org
selectorsOut:
- employer-org
- associate
- address
status: live
pricing: free
costNote: Free public search; no account or payment required for the core name/ID lookup.
opsec: passive
opsecNote: Searches run against a third-party aggregator, not the target, so nothing is disclosed to the subject. Standard web hygiene (clean browser/IP) is enough; there is no notification back to any named party.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Operated as a public-interest database aggregating orders from ~46 Indian regulators (MCA, SEBI, RBI, etc.); a secondary aggregator, so always confirm hits against the primary regulator's order.
missingPersonsRelevance: medium
coverage:
- in
auth: none
api: false
localInstall: false
registration: false
aliases:
- watchoutinvestors.com
- WOI economic offenders database
tags:
- toddington
- curated-directory
- specialty-search
- financial-regulatory
- india
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Watch Out Investors

> A searchable Indian registry of "economic offenders" — people and companies flagged by regulators, courts and enforcement bodies for financial wrongdoing or disqualification.

## When to use
You have a `name`, company name, or an Indian identifier (PAN, CIN, DIN) and want to know whether that entity has been indicted, sanctioned, barred, or disqualified within India's financial/regulatory system. Useful for corroborating an alias, surfacing a subject's business associations, or explaining why someone may have relocated or gone dark after an enforcement action.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.watchoutinvestors.com and go to the search page.
2. Enter the subject's `name`, or a `document-id` (PAN / CIN / DIN) for a precise hit.
3. Submit and read the result list — each hit ties a person/entity to a regulator, an order type (e.g. defaulter, disqualified director, SEBI ban), and a date.
4. Open the underlying order reference and confirm it against the primary regulator (MCA/SEBI/RBI) before relying on it.
5. Pivot: a matched company (`employer-org`) or co-director (`associate`) gives you new entities to run through corporate-registry and people-search tools.

## Inputs → Outputs
- **In:** `name`, `document-id` (PAN/CIN/DIN), or `employer-org`
- **Out:** linked regulatory/court actions, associated companies (`employer-org`), co-parties (`associate`), sometimes a registered `address`
- **Empty/negative result looks like:** "no records found" — meaning the entity isn't in this aggregation of Indian economic-offence data, NOT that the person is clean globally.

## Gotchas & OpSec
- India-only scope: coverage is Indian regulators (~46 sources, 11M+ indexed entities). Irrelevant for subjects with no Indian financial footprint.
- It is an aggregator: entries can lag or mis-transcribe the source order — always verify against the primary regulator before treating a hit as fact.
- OpSec: passive; querying reveals nothing to the subject.

## Overlaps ("do both")
- Pairs with corporate-registry lookups (MCA/company-search tools) and sanctions/PEP screeners — this one specialises in Indian economic-offence and disqualification records that general company registries don't flag.

## Trust & verifiability
`trust: community` — a long-running public-interest aggregator (self-reported ~46 regulators, 11M+ records as of 2026), but secondary; the authoritative record is the underlying regulator's order, which you should open and confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | watch-out-investors |
| category | search-engines |
| selectorsIn → selectorsOut | name, document-id, employer-org → employer-org, associate, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

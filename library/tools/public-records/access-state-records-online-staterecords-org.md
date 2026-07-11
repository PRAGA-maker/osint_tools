---
id: access-state-records-online-staterecords-org
name: StateRecords.org
description: Use when you have a `name` and want a US public-records starting point (criminal, court, arrest, vital records) — returns aggregated record leads across 50 states, behind a paid third-party funnel.
url: https://staterecords.org/criminal.php
category: public-records
path:
- public-records
bestFor: A third-party aggregator entry point for US criminal/court/vital records searches by name.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: freemium
costNote: Free name search returns teaser/hit indications, but accessing actual record details is paywalled behind a paid subscription. The same records are often available free directly from official county/state sources.
opsec: passive
opsecNote: Searching is passive — the subject is not notified. You disclose your query to a private lead-gen company; use a sock-puppet account and disposable payment if you ever subscribe, and never enter real personal details.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: A privately owned aggregator, NOT a government source; it explicitly disclaims accuracy/completeness and is not an FCRA consumer-reporting agency. Treat everything as a lead and confirm against the official record.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- StateRecords.org
- staterecords.org
tags:
- court
- inmate
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# StateRecords.org

> A privately-run aggregator that markets one-stop access to US criminal, court, arrest, and vital records — useful as a lead index, but a paid funnel over data that's often free at the official source.

## When to use
You have a `name` and want a quick, nationwide first pass to see whether US court/criminal/arrest/vital records might exist for that person across the 50 states. Best treated as a pointer that tells you *where* to look, after which you should pull the authoritative record from the actual county/state source — not as a final answer.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://staterecords.org/ (e.g. the criminal search) in a sock-puppet browser.
2. Enter the `name` plus city/state to disambiguate.
3. Read the teaser: indications of matching arrest/court/criminal records and possible `dob`/case references (`document-id`).
4. Do NOT rely on the paywalled aggregator output — take the jurisdiction/case pointer and retrieve the record directly from the official county/state site (usually free and authoritative).
5. Pivot: a confirmed case/`document-id` feeds official court portals; a `dob` corroborates identity in people-search.

## Inputs → Outputs
- **In:** `name` (+ city/state)
- **Out:** aggregated record leads — possible criminal/court/arrest/vital-record hits, `dob`, case/`document-id` pointers
- **Empty/negative result looks like:** no hits, or generic "records may exist" upsell prompts. A hit is not proof (name collisions are common); a miss is not clearance — check the official source either way.

## Gotchas & OpSec
- Not official: it's a lead-gen aggregator that disclaims accuracy and isn't FCRA-compliant — never use for employment/tenant screening or as authoritative proof.
- Paywall + upsell: real detail is gated; the underlying records are frequently free from government portals.
- OpSec: passive to the subject, but you're feeding a marketing funnel — use a disposable identity.

## Overlaps ("do both")
- Pairs with official county/state court and inmate-locator portals — StateRecords points you at a jurisdiction; the government source gives the verifiable record. Always do the second step.

## Trust & verifiability
`trust: unverified` — a private aggregator, not a government registry; treat all output as unconfirmed leads to verify against the authoritative source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | access-state-records-online-staterecords-org |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |

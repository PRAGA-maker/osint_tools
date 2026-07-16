---
id: reverse-genie
name: Reverse Genie
description: Use when you have a US `phone` number and want quick reverse-lookup triage — returns a possible owner name, location and related listing details from aggregated public data.
url: https://www.reversegenie.com/phone.php
category: phone
path:
- phone
bestFor: Fast, free reverse-phone triage to attach a candidate name/location to a US number before deeper enrichment.
selectorsIn:
- phone
selectorsOut:
- name
- address
status: live
pricing: free
costNote: Free reverse-lookup triage; like most such sites, deeper/"full report" details are pushed toward paid data-broker upsells.
opsec: passive
opsecNote: The lookup runs through an aggregator, not against the number's owner, so it is passive and the target is not notified. The site logs your queries and shows upsells — use a clean browser and never enter your own details to "unlock" a report.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A reverse-lookup aggregator drawing on public/third-party data of variable freshness; a convenience triage tool, not an authoritative source.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- reversegenie.com
tags:
- phone
- reverse-phone
- data-broker
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- reverse-genie-license-plate-search
- reverse-genie-lookup
- reversegenie
---

# Reverse Genie

> A quick, free reverse-phone triage site — a fast first guess at who owns a US number before you commit to heavier people-search tools.

## When to use
You have a US `phone` number and want an immediate candidate name/location to decide whether it's worth deeper work. Reverse Genie aggregates public/third-party listing data and returns a possible owner and area. Reach for it as an early, low-effort triage step — then confirm anything promising against stronger sources, since aggregator data is often stale.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.reversegenie.com/phone.php in a clean/VPN'd browser.
2. Enter the 10-digit `phone` number.
3. Read the returned candidate owner `name`, location/`address`, and any listing details.
4. Ignore "full report" upsells; do not enter your own PII to unlock anything.
5. Pivot: a candidate name feeds `[[usphonebook]]`/`[[ufind-name]]` and `[[cid-db-opencnam-caller-id-data]]` (CNAM) to corroborate; a location narrows other searches.

## Inputs → Outputs
- **In:** `phone` (US, 10-digit)
- **Out:** possible owner `name`, location/`address`, related listing details
- **Empty/negative result looks like:** "no results" or a bare area/carrier with no name — very common for mobile/VoIP/ported numbers; treat absence as inconclusive.

## Gotchas & OpSec
- Triage only: results are a first guess from stale aggregator data — always corroborate before acting.
- Upsell traps: avoid paid "unlock" flows and never enter the investigator's real details.
- Coverage: US-centric and weak on mobiles.
- OpSec: passive to the subject; the site logs your queries.

## Overlaps ("do both")
- Pairs with `[[usphonebook]]` and `[[ufind-name]]` — different aggregators, different records; reconcile across them.
- Pairs with `[[cid-db-opencnam-caller-id-data]]` — CNAM gives the carrier-registered name to cross-check the aggregator's guess.

## Trust & verifiability
`trust: community` — a convenience aggregator, not authoritative; use its output purely as a lead to verify against carrier/CNAM and primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reverse-genie |

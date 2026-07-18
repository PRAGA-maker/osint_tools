---
id: rxlist
name: RxList
description: Use when you have a pill's imprint/shape/colour or a drug name and want to identify the medication — returns the drug identity, uses, and imagery.
url: https://www.rxlist.com/
category: public-records
path:
- public-records
bestFor: Identifying an unknown medication from its pill markings, or looking up a named drug's details.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free drug/medication reference (WebMD/RxList); no account required.
opsec: passive
opsecNote: A reference lookup against a drug database — no subject is involved and nothing is signalled. Purely informational; the investigative link is yours to make offline.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by RxList/WebMD using pharmaceutical reference data; authoritative for US drug information and pill identification.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- RxList pill identifier
- rxlist.com
tags:
- toddington
- curated-directory
- medical
- drug-reference
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# RxList

> A free drug reference and pill identifier — turn a medication's markings (or a drug name) into a positive identification and its clinical details.

## When to use
A narrow, supporting resource: you've found a medication — loose pills, a bottle, a reference in records — and need to identify it or understand it. Use the pill identifier to match an imprint code, shape, and colour to a specific drug, or look up a named medication's uses, dosages, and warnings. In death, overdose, or vulnerable-missing-person cases, identifying a medication can corroborate a health condition or timeline; outside that, its OSINT relevance is low.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.rxlist.com/.
2. For an unknown pill, open the **Pill Identifier** and enter the imprint code, shape, and colour.
3. For a known drug, search its name for the monograph (uses, dosage, side effects, images).
4. Read the output: candidate drug identity, strength, manufacturer, and reference imagery.
5. Pivot: an identified prescription medication can indicate a medical condition, prescriber, or pharmacy line to pursue through appropriate (often legally-gated) channels.

## Inputs → Outputs
- **In:** a pill's imprint/shape/colour, or a drug name
- **Out:** medication identity, strength/manufacturer, clinical details, imagery
- **Empty/negative result looks like:** no match for an imprint — the marking may be partial/worn, a non-US/OTC/supplement product, or a counterfeit; absence isn't identification.

## Gotchas & OpSec
- Coverage is **US medications**; foreign or illicit/counterfeit pills may not match.
- It's a **reference**, not a person lookup — it identifies drugs, not owners; any link to a person is inferential and may involve protected health information, so handle lawfully.
- OpSec: passive; purely informational.

## Overlaps ("do both")
- Pairs with the FDA/NIH pill identifier (Pillbox successors) and DailyMed — cross-check an imprint across databases, since a single source can miss a manufacturer.

## Trust & verifiability
`trust: trusted` — RxList/WebMD uses established pharmaceutical reference data, authoritative for US drug information. The limitation is scope (US drugs) and that identification is only as good as the imprint you can read.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rxlist |

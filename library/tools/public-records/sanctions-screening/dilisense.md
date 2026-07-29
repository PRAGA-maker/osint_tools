---
id: dilisense
name: dilisense
description: Use when you have a `name` (person or entity) and want to check it against global sanctions, PEP, and criminal watchlists — returns matching listings with source and jurisdiction.
url: https://dilisense.com/en
category: public-records
path:
- public-records
- sanctions-screening
bestFor: Free instant screening of a person or company against sanctions, PEP, and criminal watchlists worldwide.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- associate
status: live
pricing: freemium
costNote: The web search tool is free and needs no registration; paid tiers add REST API, Excel batch screening, on-prem database, and ongoing monitoring.
opsec: passive
opsecNote: Screening runs against dilisense's aggregated lists — you submit a name to their service, not to the subject, so the person is not alerted. Passive. Be mindful the query (a name) is sent to a third-party compliance vendor; use a neutral connection and don't include extra sensitive context in the search box.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Aggregates 9,000+ official sanctions/PEP/watchlist sources refreshed multiple times daily; a compliance-grade dataset, though matches are name-based and need identity confirmation.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- opensanctions
aliases:
- dilisense
- dilisense.com
tags:
- sanctions
- pep
- watchlist
- aml
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# dilisense

> Free, instant AML screening — check a person or company against sanctions, PEP, and criminal watchlists across 190+ jurisdictions, right from the website.

## When to use
You have a `name` (individual or organization) and need to know whether it appears on any sanctions list, is a Politically Exposed Person, or shows up on a criminal/enforcement watchlist. In an investigation this flags risk and context fast: a subject or an `associate`/`employer-org` in the network being sanctioned or politically exposed changes the picture and can explain movements, assets, or affiliations. Screens both people and entities.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://dilisense.com/en and use the free web search (no signup).
2. Enter the person's `name` or the company name (try transliteration variants for non-Latin names).
3. Review matches: which list (sanctions / PEP / criminal / adverse media), the source, jurisdiction, and any listed identifiers.
4. Confirm identity carefully — matches are name-based; check DOB, nationality, and other identifiers before treating a hit as your subject.
5. Pivot: a confirmed listing yields `employer-org`, `associate`, and jurisdiction leads; cross-check with `[[opensanctions]]`.

## Inputs → Outputs
- **In:** `name` (person or entity)
- **Out:** matching sanctions/PEP/criminal listings with source, jurisdiction, related `name`/`employer-org`/`associate`
- **Empty/negative result looks like:** "no matches" — the person isn't on the aggregated lists (good, but not proof of a clean record); a common name may also hide behind spelling variants — retry transliterations.

## Gotchas & OpSec
- **Name-based matching:** false positives (same-name different-person) and false negatives (spelling/transliteration) both occur — always confirm with secondary identifiers.
- Free tier is the web lookup; batch/API/monitoring are paid.
- OpSec: **passive** — the subject isn't notified; you are trusting a compliance vendor with the queried name.

## Overlaps ("do both")
- Pairs with `[[opensanctions]]` — both aggregate global sanctions/PEP data; run both and reconcile, since source coverage and update timing differ. Agreement raises confidence in a hit.

## Trust & verifiability
`trust: trusted` — built on thousands of official, frequently-refreshed sources; the data is authoritative, but each match still requires identity verification against the cited source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dilisense |
| category | public-records |
| selectorsIn → selectorsOut | name → name, employer-org, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

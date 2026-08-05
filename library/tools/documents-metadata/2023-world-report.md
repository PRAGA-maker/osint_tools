---
id: 2023-world-report
name: 2023 World Report
description: Use when you have a country tied to a case and want a documented human-rights summary for it — returns HRW's country-by-country account of events, actors, and abuses.
url: https://www.hrw.org/world-report/2023
category: documents-metadata
path:
- documents-metadata
bestFor: Authoritative country-level human-rights context for the year covered.
selectorsIn:
- address
selectorsOut:
- address
- employer-org
status: live
pricing: free
costNote: Free to read online and download as PDF; no account.
opsec: passive
opsecNote: Passive — you read a published NGO report; nothing about any subject is transmitted. Target-neutral reference material.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Human Rights Watch is a major, methodologically-rigorous human-rights NGO; the World Report is its flagship annual, sourced from field research, so it is an authoritative secondary source (with HRW's own framing, as with any advocacy body).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- HRW World Report 2023
- Human Rights Watch World Report
tags:
- toddington
- human-rights
- country-reports
source: toddington-resources
lastVerified: '2026-08-05'
enrichment: full
---

# 2023 World Report

> Human Rights Watch's flagship annual: a country-by-country account of human-rights conditions across ~100 countries, useful as documented background on a place.

## When to use
Your investigation touches a country and you need a credible, documented summary of its human-rights situation for that period — abuses, responsible institutions, conflict dynamics, treatment of specific groups (migrants, detainees, minorities). Context/reference material that frames the environment around a lead; it names governments and institutions, not private individuals you'd be searching for.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.hrw.org/world-report/2023.
2. Use "Browse Countries" to jump to the relevant country's chapter (nearly 100 covered).
3. Read the chapter for the year's events, the actors/institutions (`employer-org`, e.g. security forces, ministries) involved, and the specific abuses documented.
4. Download the full PDF if you need an offline, citable copy.
5. Pivot: named institutions and events feed further research (news archives, court records, sanctions lists); country conditions inform risk/plausibility assessments. For other years, browse HRW's World Report series.

## Inputs → Outputs
- **In:** a country/region (`address`-level context)
- **Out:** a documented human-rights narrative — events, locations (`address`), and responsible institutions (`employer-org`)
- **Empty/negative result looks like:** a country not covered, or a chapter that doesn't address your specific issue — HRW prioritises certain situations, so gaps exist. Complement with Amnesty, US State Department, and UN reporting.

## Gotchas & OpSec
- It's a secondary advocacy source with HRW's editorial framing; corroborate specific claims against primary reporting.
- Country coverage and depth vary year to year; this is the 2023 edition — use the matching year for your timeframe.
- Institution-level, not person-level — wrong tool for identifying an individual.
- OpSec: fully passive reference reading.

## Overlaps ("do both")
- Read alongside Amnesty International's annual report, the US State Department Human Rights Reports, and UN bodies — the major sources cover the same countries from different vantage points, and agreement across them strengthens a factual claim.

## Trust & verifiability
`trust: trusted` — a rigorous, widely-cited NGO source; authoritative as documented secondary reporting, with the standard caveat that it carries an advocacy perspective and should be corroborated for specific facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | 2023-world-report |

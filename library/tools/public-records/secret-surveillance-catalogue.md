---
id: secret-surveillance-catalogue
name: Secret Surveillance Catalogue
description: Use when you have a `device-id` / equipment name (an IMSI-catcher, cell-site simulator, or surveillance box) and want to understand its capabilities — returns a reference profile of the device and its maker.
url: https://theintercept.com/surveillance-catalogue/
category: public-records
path:
- public-records
bestFor: Identifying and understanding law-enforcement/military surveillance devices (IMSI-catchers, cell-site simulators) by name and capability.
selectorsIn:
- device-id
selectorsOut:
- device-id
- employer-org
status: live
pricing: free
costNote: Free to read; published by The Intercept as an investigative reference database. No account.
opsec: passive
opsecNote: You read a published journalism reference; nothing here queries a subject or device. Fully passive. It is a knowledge resource, not a live scanner.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A reference built by The Intercept from a leaked government catalogue of cellular-surveillance equipment; well-sourced investigative journalism, though it is a point-in-time (2015) snapshot of then-known devices.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Secret Surveillance Catalogue
- The Intercept Surveillance Catalogue
tags:
- surveillance-equipment
- reference
- imsi-catcher
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Secret Surveillance Catalogue

> The Intercept's reference database of cellular-surveillance hardware — IMSI-catchers, cell-site simulators, and related boxes — profiling each device's capabilities and manufacturer.

## When to use
You encounter a `device-id` or an equipment name — a Stingray, a Hailstorm, an IMSI-catcher model, a surveillance box referenced in a document, budget, procurement record, or leak — and you need to understand what it is and what it can do. This catalogue, built from a leaked US government document, profiles many such devices: their vendor (`employer-org`), interception capabilities, range, and intended use. It is a knowledge/reference resource for making sense of surveillance-equipment references, not a lookup that returns data about a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://theintercept.com/surveillance-catalogue/ and browse or search by device name/model.
2. Read the device profile: manufacturer, type (e.g. cell-site simulator), capabilities, and operating notes.
3. Use it to interpret a procurement record, budget line, or document that names such a device — the catalogue tells you what capability that purchase implies.
4. Treat it as a 2015 snapshot: newer devices won't appear, and specifics may have evolved; corroborate with more recent reporting for current models.
5. Pivot: the manufacturer (`employer-org`) feeds corporate/procurement research; a device name feeds FOIA/records work on which agencies bought it.

## Inputs → Outputs
- **In:** `device-id` / surveillance-equipment name
- **Out:** `device-id` capability profile and `employer-org` (manufacturer) — a reference description, not personal data
- **Empty/negative result looks like:** the device isn't listed — it postdates the 2015 catalogue, is a different class of equipment, or was never in the leaked document; use current investigative reporting instead.

## Gotchas & OpSec
- Reference, not a locator: it explains equipment; it never returns information about a person or a live device.
- Dated snapshot (2015): a fixed catalogue — newer models and capabilities are absent; don't assume it's exhaustive today.
- Low direct people-search relevance: valuable for context on surveillance capability, tangential to locating a person.
- OpSec: fully passive reading.

## Overlaps ("do both")
- Best combined with procurement/FOIA and corporate-records work — use the catalogue to identify a device and its maker, then research which agencies acquired it and when through public records and reporting.

## Trust & verifiability
`trust: trusted` — well-sourced investigative journalism grounded in a leaked government document; authoritative for the devices it profiles, with the caveat that it is a 2015 snapshot to supplement with current reporting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | secret-surveillance-catalogue |
| category | public-records |
| selectorsIn → selectorsOut | device-id → device-id, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

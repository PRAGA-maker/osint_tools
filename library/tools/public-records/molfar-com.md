---
id: molfar-com
name: Molfar Useful Apps & Registers
description: Use when you have a lead and need the right public register or OSINT app for a jurisdiction — Molfar's curated directory returns links to registers and tools for finding people, companies and records.
url: https://molfar.com/en/useful-apps-registers
category: public-records
path:
- public-records
bestFor: A curated jump-list of public registers and OSINT apps (people, company, sanction, vehicle, etc.), strong on Ukraine/CIS and international sources.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
- address
status: live
pricing: free
costNote: The useful-apps-and-registers directory is a free public resource. Molfar's actual investigations are a separate paid, analyst-delivered service.
opsec: passive
opsecNote: Browsing the directory is passive. The registers it links to vary — some are official/passive, others may log or rate-limit queries — so apply each linked tool's own OpSec (clean browser/VPN) when you follow through.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Curated by Molfar, a reputable Ukrainian private-intelligence firm; the directory is a well-maintained pointer list, though the quality/availability of each linked register is external to Molfar.
missingPersonsRelevance: high
coverage:
- global
- ua
auth: none
api: false
localInstall: false
registration: false
aliases:
- Molfar registers
- Molfar useful apps
tags:
- companysites
- Company Related Sites
- tool-directory
- registers
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Molfar Useful Apps & Registers

> A curated directory of public registers and OSINT apps from Ukrainian intelligence firm Molfar — the fast way to find the right official source for a given lead and jurisdiction.

## When to use
You have a `name`, `employer-org`, vehicle, or other lead and need to know *which* register or app will resolve it — especially for Ukraine/CIS and cross-border cases where the right source isn't obvious. Molfar's team maintains a categorised list of people-search, company, sanctions, court, vehicle and other registers/tools. Reach for it as a routing layer: pick the correct authoritative source, then do the actual lookup there.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://molfar.com/en/useful-apps-registers.
2. Browse to the category matching your lead (person, company, sanctions, vehicle, etc.).
3. Choose the register/app relevant to the subject's jurisdiction and open it.
4. Run the lookup on that external source, applying its own access/OpSec requirements.
5. Pivot: results from the linked register feed the rest of your workflow; note the tool for reuse on similar cases.

## Inputs → Outputs
- **In:** `name` / `employer-org` / other lead (used to choose a register), plus the jurisdiction
- **Out:** links to the appropriate registers/apps that then return `name`, `employer-org`, `address` and related records
- **Empty/negative result looks like:** no listed tool for your exact need/region — the directory is broad but not exhaustive; combine with other tool-maps (`[[malfrat-s-osint-map]]`).

## Gotchas & OpSec
- It's a directory, not a search: Molfar routes you to sources; the data comes from those external registers.
- Link rot: external registers change URLs/access over time — a listed tool may have moved.
- OpSec: passive to browse, but inherit each linked register's OpSec when you use it.

## Overlaps ("do both")
- Pairs with `[[malfrat-s-osint-map]]` — two curated maps that cover different tools; cross-reference for coverage.
- Pairs with jurisdiction registers like `[[france]]` (Infogreffe) that Molfar will often point you toward.

## Trust & verifiability
`trust: community` — a well-maintained pointer directory from a reputable intelligence firm; trust the routing, but verify each linked register at its source since Molfar doesn't own that data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | molfar-com |

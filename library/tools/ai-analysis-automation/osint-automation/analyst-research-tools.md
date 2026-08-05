---
id: analyst-research-tools
name: Analyst Research Tools
description: Use when you have a name, email, username, phone, plate or VIN and want a curated launchpad routing you to the right free lookup services across people-search, social, email, archives and domains — returns links to pivot into, not data itself.
url: https://analystresearchtools.com
category: ai-analysis-automation
path:
- ai-analysis-automation
- osint-automation
bestFor: A categorised portal of vetted OSINT lookup services to launch queries from a single page.
selectorsIn:
- name
- email
- username
- phone
- vehicle-plate
- vin
selectorsOut:
- social-profile
- email
- address
status: live
pricing: free
costNote: Free aggregation portal (© 2025, by Collin Tex / @collin_intel); the individual services it links vary from free to freemium.
opsec: passive
opsecNote: The portal itself just launches queries into third-party services, so your OpSec is inherited from whichever service you click through to. Use a sock-puppet browser and check each destination's own exposure (some people-search sites are active/log queries) before submitting a selector.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A curated one-person OSINT link portal; the curation is helpful but the linked tools' quality is the tools' own, not the portal's.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- ARTs
- analystresearchtools.com
tags:
- tool-collection
- osint-portal
source: arf-seed
lastVerified: '2026-08-05'
enrichment: full
---

# Analyst Research Tools

> A categorised launchpad of free OSINT services — pick your selector, jump straight to the right people-search, social, email, archive, or domain tool.

## When to use
Early in a lookup when you have a selector but aren't sure which service to use for it. Analyst Research Tools (ARTs) organises dozens of external lookups by category — people/PII search, social-media (40+ platforms), email/phone reverse lookups and breach DBs, CV databases, username permutators, vehicle VIN/plate lookups, archives, and domain research — so you can move from "I have an `email`" to "here are five services that resolve it" without hunting for links.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://analystresearchtools.com in a sock-puppet browser.
2. Go to the category matching your selector (People, Social Media, Email/Phone, Archives, Domain, Vehicle, etc.).
3. Pick a linked service and run your query there — the portal hands you off to the real tool.
4. Check that destination's own OpSec/pricing before submitting anything.
5. Pivot: results from the chosen service (profiles, addresses, breach hits) feed the next selector back into another ARTs category.

## Inputs → Outputs
- **In:** `name`, `email`, `username`, `phone`, `vehicle-plate`, `vin`
- **Out:** routes to services returning `social-profile`, `email`, `address`, breach and archive data
- **Empty/negative result looks like:** N/A for the portal itself — a dead end only appears in the linked service; if one category's tools all miss, try a different selector/category.

## Gotchas & OpSec
- **It's a directory, not a database** — it holds no data; everything comes from the third-party services it links.
- Link rot and coverage bias: some listed services may be defunct or paywalled; verify each on use.
- OpSec is inherited from the destination — some people-search sites log or actively query; treat each click-through on its own merits.

## Overlaps ("do both")
- Same role as other OSINT link frameworks (`[[hunt-osint-framework]]`, OSINT Framework); cross-check across portals since each curator lists different tools.

## Trust & verifiability
`trust: community` — a single curator's helpful index; trust the *organisation* but verify each linked tool independently, and treat their outputs as leads to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | analyst-research-tools |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | name, email, username, phone, vehicle-plate, vin → social-profile, email, address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

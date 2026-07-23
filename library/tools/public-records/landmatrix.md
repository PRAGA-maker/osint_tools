---
id: landmatrix
name: LandMatrix
description: Use when you have a company/investor `employer-org` or a country and want to find large-scale land acquisitions tied to it — returns land deals with investors, locations and `address`/`associate` links.
url: http://landmatrix.org
category: public-records
path:
- public-records
bestFor: Tracing large-scale land deals to the companies and investors behind them, by country or investor.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- associate
- address
status: live
pricing: free
costNote: Free, open, independently-run database; all maps, tables and charts are public with no account.
opsec: passive
opsecNote: Public research database — you query aggregated deal records, not any target; fully passive with no signal.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Independent global monitoring initiative (Land Matrix) run by a partnership of research institutions; deals are sourced and referenced, though completeness varies by country.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Land Matrix
tags:
- public-records
- land-deals
- corporate
- investigative
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# LandMatrix

> An open, independently-maintained database of large-scale land acquisitions in low- and middle-income countries — deal → investor → parent company, mapped and referenced.

## When to use
You are investigating an `employer-org`/investor, a beneficial owner, or activity in a particular country and want to know about large-scale land deals connected to it: who acquired what, where, from whom, and via which intermediary companies. Useful for corporate-network mapping, land-grab/agribusiness stories, and tracing `associate`s and holding structures behind an investment.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://landmatrix.org (https).
2. Use the interactive map, or the deals/investors tables filtered by country, investor `employer-org`, or intention of investment.
3. Open a deal to see the investor chain (operating company → parent), location/`address`, size, and source references.
4. Pivot: investor and parent `employer-org` names and linked `associate`s feed corporate registries (`[[occrp-aleph]]`, `[[eu-consolidated-corporate-registers]]`) for beneficial-ownership follow-up.

## Inputs → Outputs
- **In:** company/investor `employer-org` or country (also a person `name` behind an investor)
- **Out:** land deals with investor chains (`employer-org`, `associate`), locations/`address`
- **Empty/negative result looks like:** no deals for your filter — the target isn't recorded (coverage is deal-reported and country-uneven), not proof none exist.

## Gotchas & OpSec
- Coverage depends on what has been reported and verified; smaller or newer deals may be missing or provisional.
- Investor chains reflect what's documented — the ultimate beneficial owner may sit behind a shell not captured here.
- Focus is low/middle-income countries; not a global land registry.

## Overlaps ("do both")
- Pairs with `[[occrp-aleph]]` and corporate registries — Land Matrix names the deal and the investor; those resolve the investor to its owners and other holdings.

## Trust & verifiability
`trust: trusted` — a well-established academic/NGO monitoring initiative with sourced entries; treat individual deals per their cited references and status flags.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | landmatrix |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, associate, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

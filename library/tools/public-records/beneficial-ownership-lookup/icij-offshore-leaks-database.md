---
id: icij-offshore-leaks-database
name: ICIJ Offshore Leaks Database
description: Use when you have a `name`, company (`employer-org`), or `address` and want hidden offshore ownership/company links from ICIJ's leaks — returns connected entities, officers (`associate`), and `address`.
url: https://offshoreleaks.icij.org/
category: public-records
path:
- public-records
- beneficial-ownership-lookup
bestFor: Tracing offshore companies, officers, and beneficial-ownership networks from the Panama/Paradise/Pandora Papers and other leaks.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- associate
- employer-org
- address
status: live
pricing: free
costNote: Free public database; the full data is downloadable in bulk and available as structured data.
opsec: passive
opsecNote: Public database queries — subjects are not notified and nothing touches them. For sensitive work still use a clean session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by the International Consortium of Investigative Journalists (ICIJ) from verified leaked datasets; authoritative, but records reflect the leak's date, not necessarily current ownership.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- lux-leaks
aliases:
- Offshore Leaks
- ICIJ Offshore Leaks
tags:
- offshore
- beneficial-ownership
- leaks
- corporate
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# ICIJ Offshore Leaks Database

> A searchable graph of the people, companies, and addresses named in the biggest financial leaks — Panama, Paradise, Pandora Papers and more — with the relationships mapped for you.

## When to use
You have a `name`, a company (`employer-org`), or an `address` and want to know whether it appears in offshore/shell-company structures: who the officers and intermediaries are, which entities connect to which, and across which jurisdictions. Powerful for financial-investigation and asset-tracing angles, and for surfacing hidden `associate` relationships behind a person or company.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://offshoreleaks.icij.org/ and search a `name`, entity, or `address`.
2. Open a result to see its record — type (entity/officer/intermediary/address), jurisdiction, linked data source (which leak), and connected nodes.
3. Explore the **network graph**: each edge is a documented relationship (officer of, connected to, registered address), letting you walk from a person to their companies to their co-officers (`associate`).
4. For scale, download the bulk data / use the structured data to run your own graph queries.
5. Pivot: linked officers are `associate` leads; company names feed corporate registries; addresses feed people/property searches.

## Inputs → Outputs
- **In:** `name`, `employer-org` (company), or `address`
- **Out:** connected entities/officers (`associate`), companies (`employer-org`), and `address`es, with a relationship graph and source jurisdiction
- **Empty/negative result looks like:** no match — the person/company isn't in any indexed leak (most people aren't); absence is not exoneration or proof of no offshore holdings.

## Gotchas & OpSec
- ICIJ's own disclaimer applies: **appearing here is NOT evidence of wrongdoing** — many uses of offshore entities are legal. Report findings carefully.
- Data is historical (as of each leak) and may name people with common names — corroborate identity before attributing.
- OpSec: passive public lookup; nothing reaches the subject.

## Overlaps ("do both")
- Pair with corporate registries and [[lux-leaks]] — Offshore Leaks reveals the leaked network; live registries confirm current status and fill gaps outside the leaks.

## Trust & verifiability
`trust: trusted` — a rigorously-vetted ICIJ dataset; the relationships are documented from source records, though you must still verify that a matched name is your subject.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | icij-offshore-leaks-database |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address → associate, employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: inteltechniques-business-search-tool
name: IntelTechniques Business Search Tool
description: Use when you have a company `employer-org` or a business owner's `name` and want to sweep many business-record sources at once — returns registrations, filings, and associated people.
url: https://inteltechniques.com/tools/business.html
category: public-records
path:
- public-records
bestFor: A one-page query launcher that fires a company/owner name across dozens of business-records search engines.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- associate
- address
- document-id
status: live
pricing: free
costNote: Free to use (last updated Nov 2024; a supplement to Bazzell & Edison's OSINT Techniques, 11th ed). Training-member login is optional and only adds saved/extra features.
opsec: passive
opsecNote: The tool itself just builds and opens searches on third-party business-record sites — it holds no data and never contacts the subject. Your exposure is to each destination site (registries, SEC EDGAR, business directories); use a sock-puppet browser and mind any site that requires its own login.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A reputable query aggregator by Michael Bazzell; it dispatches to authoritative sources, so trust rests on the destination registries rather than the tool.
missingPersonsRelevance: high
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- IntelTechniques Business Search
- Bazzell business tool
tags:
- court
- business-records
- company-search
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# IntelTechniques Business Search Tool

> Michael Bazzell's business-records launcher — type a company or owner name once and it fans the query across dozens of registries, filing databases, and directories.

## When to use
You have an `employer-org` (a company) or a person's `name` you believe owns/runs a business, and you want to hit the many scattered business-records sources — state incorporation registries, SEC EDGAR, business directories, trademark/patent, licensing — without visiting each by hand. It's a time-saver for corporate-affiliation mapping and for linking a person to the entities behind them.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open `https://inteltechniques.com/tools/business.html`.
2. Enter the company or owner `name` in the input field.
3. Click through the individual source buttons (each opens that source's search pre-filled), or use the "submit all" style options.
4. Work each destination: read the authoritative record on the registry/EDGAR/etc.
5. Pivot: officers/registered agents → `associate` and people-search; a registered `address` → property/records; filing IDs (`document-id`) → the authoritative filing; the company → `[[kompass]]` / `[[londonstockexchange-com]]`.

## Inputs → Outputs
- **In:** `employer-org`, `name`
- **Out:** `employer-org` (registration), `associate` (officers/agents), `address`, `document-id` (filing/registration numbers) — sourced from the destination sites
- **Empty/negative result looks like:** the dispatched searches return nothing on a given source — the entity isn't registered there, or the name needs a jurisdiction. It's a launcher, so "empty" is per-destination, not global.

## Gotchas & OpSec
- It builds queries; results and reliability are entirely the destination sources'. Read the actual registry, don't trust the launcher.
- Bazzell periodically revises/relocates his tools — if a button 404s, go to `inteltechniques.com/tools/` for the current version.
- OpSec: **passive** toward the subject; exposure is to each destination site.

## Overlaps ("do both")
- Pairs with `[[kompass]]`, `[[londonstockexchange-com]]`, and Companies House — the tool routes you to registries fast; those give the authoritative company/officer records to confirm affiliations.

## Trust & verifiability
`trust: community` — a reputable, maintained launcher; the authority comes from the registries it opens, so cite the destination record, not the tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | inteltechniques-business-search-tool |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, associate, address, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

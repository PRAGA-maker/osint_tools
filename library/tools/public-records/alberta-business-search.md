---
id: alberta-business-search
name: Alberta Business Search (AlbertaCorporations.com)
description: Use when you have a company `name`/number or a person's `name` and want Alberta (Canada) corporate records — returns registered address, directors, and registry-event history as associate/address leads.
url: https://albertacorporations.com/
category: public-records
path:
- public-records
bestFor: Free Alberta corporate registry lookup — company profiles with directors, registered address, and filing history.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: free
costNote: Free to search and view company profiles — no account, no per-search fee. It is an independent index; the official Alberta registry charges per search/document and is the legal source of record.
opsec: passive
opsecNote: You query a third-party index built from published public notices, not a government login, so there is no alert to any subject. Records are public corporate filings; note you're using an unofficial mirror, so verify anything material against the official Alberta registry before relying on it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent index compiled from the Alberta Gazette / Registrar's Periodical; convenient and free, but not the authoritative government registry.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- Alberta Corporations
- AlbertaCorporations.com
tags:
- corporate-registry
- canada
- business-search
- public-records
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Alberta Business Search (AlbertaCorporations.com)

> A free, no-login index of Alberta corporate records — search a company or person and get the registered address, directors, and a timeline of registry filings.

## When to use
You're placing someone in Alberta, Canada and want their business footprint: a company `name`/number to profile, or a person's `name` to find corporations they direct. Returns registered-office `address`, associated directors (`associate`), incorporation/dissolution dates, and a filing timeline — strong corroboration for linking a person to a business, an address, or co-directors in a missing-persons or due-diligence workflow.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://albertacorporations.com/.
2. Search by company `name`, corporate number, registered `address`, or city; you can also browse by industry tag or by recently registered / struck-off entities.
3. Open a result's profile: read status, incorporation/dissolution dates, registered office `address`, directors, and the registry-event history (`selectorsOut`).
4. Pivot: a registered address feeds address/people search; co-directors are `associate` leads; confirm any critical detail against the official Alberta registry.

## Inputs → Outputs
- **In:** `name` (company or person), `employer-org`, or `address`
- **Out:** `employer-org` (company profile), `address` (registered office), `associate` (directors/officers), registry-event timeline
- **Empty/negative result looks like:** no matching company — meaning nothing in Alberta's public index under that term, not proof the person has no business anywhere.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive — an unofficial public-records mirror; nobody is notified.
- It's a third-party index built from published notices, so it can lag or miss recent changes; the official Alberta registry is the legal source for binding searches and current documents.

## Overlaps ("do both")
- Complements the official [Alberta.ca corporate registry] and pan-Canadian corporate search tools — use this free index for fast discovery, then the official registry for authoritative, current filings.

## Trust & verifiability
`trust: community` — an independent index compiled from the Alberta Gazette and Registrar's Periodical. Good for lead generation and public data, but verify anything you'll act on against the government registry of record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | alberta-business-search |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address → employer-org, address, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

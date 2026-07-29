---
id: ofac-sanctioned-search-engine
name: OFAC Sanctioned Search Engine
description: Use when you have a `name` or `employer-org` and want to check exposure to US Treasury/OFAC sanctions sources in one search — returns sanctions-list mentions and links.
url: https://cse.google.com/cse?cx=e96467889fb82b9b0
category: public-records
path:
- public-records
bestFor: A first-pass sanctions screen of a person or entity across OFAC-related sites via a curated Google Custom Search.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
status: degraded
pricing: free
costNote: Free — it is a Google Custom Search Engine over OFAC-related sources; no account required.
opsec: passive
opsecNote: A Google Custom Search query. It touches Google, not the subject, and reveals nothing to the target. Standard search-engine privacy applies; use a clean session if you want the query off your Google history.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party-configured Google CSE, not an official Treasury tool — coverage is only as good as the sites its creator indexed and can drift over time. Confirm hits against OFAC's official SDN search.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- OFAC sanctions CSE
- OFAC search engine
tags:
- sanctions
- public-records
- corporate
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# OFAC Sanctioned Search Engine

> A curated Google Custom Search over OFAC/sanctions-related sources — a quick screening pass, not the authoritative sanctions database.

## When to use
You have a `name` or `employer-org` and want a fast check for any tie to US Treasury/OFAC sanctions before deeper due diligence. It searches a pre-selected set of sanctions-related sites in one query, which is handy for a broad screen. For any positive, you must confirm on OFAC's official Sanctions List Search — this CSE is a convenience layer, not the source of truth.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE at the URL.
2. Enter the person's `name` or the entity/`employer-org`.
3. Read the results — links into OFAC-related pages/lists mentioning the query.
4. **Confirm any hit** on the official OFAC Sanctions List Search (sanctionssearch.ofac.treas.gov) with full identifiers (DOB, address) to rule out name collisions.
5. Pivot: a confirmed listing surfaces associated entities/`associate`s and addresses in the SDN entry.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** sanctions-list mentions and links; on confirmation, associated entities (`associate`) and org data
- **Empty/negative result looks like:** no results — treat as "no hit in this CSE's indexed sources," not as a cleared sanctions check; the official OFAC search is authoritative.

## Gotchas & OpSec
- **Not official**: this is a community-built Google CSE; its site list can go stale or miss recent designations. Never rely on it alone for a compliance decision.
- Common names collide — a hit is a lead requiring identity confirmation via full SDN identifiers.
- CSE coverage may degrade silently as indexed sites change.

## Overlaps ("do both")
- Always pair with the **official OFAC Sanctions List Search** and broader watchlist tools — this CSE is the fast screen; the official database is the authority you cite.

## Trust & verifiability
`trust: community` — a third-party Google Custom Search, not a Treasury product; useful for discovery but every hit must be verified against OFAC's official list before it counts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ofac-sanctioned-search-engine |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

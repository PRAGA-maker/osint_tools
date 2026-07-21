---
id: fidonet-nodelist
name: Fidonet nodelist
description: Use when you have a person's name or a rough location tied to old BBS/FidoNet activity and want to find their sysop node entry — returns a `geolocation` (city/region), node number and sysop `name` from 1986–present nodelists.
url: https://nodehist.fidonet.org.ua/
category: social-networks
path:
- social-networks
bestFor: Resolving an old FidoNet node number or sysop name to a city/region and time window across 40 years of weekly nodelists.
selectorsIn:
- name
- geolocation
selectorsOut:
- name
- geolocation
status: live
pricing: free
costNote: Free public search interface over the historical FidoNet nodelist archive; no account.
opsec: passive
opsecNote: Fully passive — you are querying a static historical archive, not contacting anyone. Nothing about your search reaches the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-run nodelist history search (nodehist.fidonet.org.ua) built from the official weekly nodelists; the underlying data is authoritative, the interface community-maintained.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- FidoNet nodelist history
- nodehist
tags:
- Social Media
- Fidonet
- historical
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Fidonet nodelist

> A searchable history of every weekly FidoNet nodelist since 1986 — a niche but precise way to place an old BBS sysop in a city and time.

## When to use
The subject has a paper trail in 1980s–2000s bulletin-board / FidoNet culture and you have their sysop `name`, a node number, or a rough `geolocation`. Because each weekly nodelist records the sysop's name, node address, and location, this can pin a historical online identity to a city and a date range — useful for cold cases, genealogy-style tracing, or confirming an alias predates the modern internet.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://nodehist.fidonet.org.ua/.
2. Search by 3D FidoNet address (zone:net/node), sysop name, or location string.
3. Read the timeline of matching nodelist entries — each row shows the nodelist date, so you get a first-seen / last-seen window plus the city and system name recorded at the time.
4. Pivot: a real name recovered from a node entry feeds people-search; a city + era narrows other archival searches; a system/BBS name can be searched in text archives.

## Inputs → Outputs
- **In:** sysop `name`, node number, or `geolocation`
- **Out:** sysop `name`, node `geolocation` (city/region), node number, and the date window it was active
- **Empty/negative result looks like:** no matching rows — the person was never a listed FidoNet node (many users were points/callers, not sysops, and never appeared in the nodelist).

## Gotchas & OpSec
- Only **sysops** (system operators) appear; ordinary BBS callers do not, so absence proves nothing about someone's BBS-era activity.
- Names in old nodelists were often handles or abbreviated; corroborate before treating as a legal name.
- Coverage spans the first 1986 nodelist through recent 2020s ones, so it captures the long tail of hobbyist FidoNet still running.

## Overlaps ("do both")
- Pairs with newsgroup/Usenet and old-web archive searches — FidoNet gives the node/location, those give the person's writings from the same era.

## Trust & verifiability
`trust: community` — the search UI is community-run, but it indexes the genuine, published weekly nodelists, so a hit is verifiable against the dated source file.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fidonet-nodelist |
| category | social-networks |
| selectorsIn → selectorsOut | name, geolocation → name, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

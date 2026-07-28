---
id: wikipedia-list-of-registers
name: Wikipedia — List of official business registers
description: Use when you have an `employer-org`/country and need to find the authoritative company register for that jurisdiction — an index page linking national registries; returns employer-org, associate leads.
url: https://en.wikipedia.org/wiki/List_of_official_business_registers
category: financial-crypto
path:
- financial-crypto
bestFor: Finding the correct official company/business register for any country before doing corporate lookups.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free Wikipedia article; no account. The registers it links to may themselves charge for detailed filings.
opsec: passive
opsecNote: Reading a Wikipedia index is passive and reveals nothing about your subject. Note that the destination registers vary in OpSec: some log searches or require accounts — assess each linked registry on its own before querying.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-maintained Wikipedia list; it's a signpost, not a data source. Registry URLs can go stale — treat it as a starting index and confirm the current official site for each jurisdiction.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- opencorporates
- aleph-occrp
tags:
- bellingcat-toolkit
- companies-finance
- business-registry
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# Wikipedia — List of official business registers

> A country-by-country index of official company registers — the map you consult first to find *which* authoritative registry to search for a company in a given jurisdiction.

## When to use
You have an `employer-org` (or a person you're tying to a company) and need the official business register for its country — the primary source for directors, incorporation dates, and filings. Rather than guessing the registry, look it up here, then go to the jurisdiction's real register.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Wikipedia article.
2. Find the country/jurisdiction in the table.
3. Follow the link to that jurisdiction's official register (companies house / commercial register / etc.).
4. Verify you've landed on the genuine official site (check the domain) before searching.
5. Pivot: the registry → directors/officers (`name`, `associate`), incorporation and address data; aggregate cross-border via `[[opencorporates]]`.

## Inputs → Outputs
- **In:** an `employer-org` and its country (or the country you need to search)
- **Out:** a pointer to the official register → from there, `employer-org` details and `associate` (officers/directors)
- **Empty/negative result looks like:** the country isn't listed or the link is dead — meaning use the aggregator/search route instead, not that no register exists.

## Gotchas & OpSec
- It's an **index, not data** — you still do the lookup at the linked registry, each with its own fees, languages, and access rules.
- Links can be outdated; confirm the current official registry domain to avoid look-alike/paid middlemen sites.
- Passive to read; evaluate each destination register's OpSec separately.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]` (cross-jurisdiction company aggregator — faster for a first sweep) and `[[aleph-occrp]]`; use this list when you need the *authoritative* national source rather than an aggregate.

## Trust & verifiability
`trust: community` — a Wikipedia signpost. Reliable as a directory of where to look; always verify the destination registry is the official one and rely on *its* data, not the list.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikipedia-list-of-registers |
| category | financial-crypto |
| selectorsIn → selectorsOut | employer-org, name → employer-org, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

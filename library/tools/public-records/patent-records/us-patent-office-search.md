---
id: us-patent-office-search
name: US Patent Office Search
description: Use when you have an inventor `name` (or a company) and want their US patents — returns inventor `name` + city/state (`address`), the `employer-org` assignee, and co-inventors (`associate`s).
url: https://www.uspto.gov/patents/search
category: public-records
path:
- public-records
- patent-records
bestFor: Finding a person's US patents to place them at an employer, a city, and among named co-inventors.
selectorsIn:
- name
- employer-org
selectorsOut:
- address
- employer-org
- associate
status: live
pricing: free
costNote: Free official USPTO service (Patent Public Search); also has a free Open Data Portal API. No account required for basic search.
opsec: passive
opsecNote: Passive — querying the government patent database does not notify anyone. It's a public record search; standard sock-puppet hygiene is more than enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official United States Patent and Trademark Office database — authoritative primary-source records.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- patent-attorneys-agent-search
- tess
aliases:
- USPTO Patent Public Search
- PPUBS
tags:
- patents
- public-records
source: arf-seed
lastVerified: '2026-07-21'
enrichment: full
---

# US Patent Office Search

> The official USPTO patent database — an authoritative way to tie an inventor's name to an employer, a city, and a network of co-inventors.

## When to use
You have a subject who is (or might be) an inventor — an engineer, scientist, founder — and you have their `name` or the `employer-org` they worked for. Patents are signed public records: each names the inventor(s) with their **city and state**, the **assignee** (usually the employer), the filing/grant dates, and co-inventors. That's a clean way to confirm where someone worked, roughly where they lived at filing time, and who they collaborated with.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.uspto.gov/patents/search and launch **Patent Public Search (PPUBS)**.
2. Search by inventor name (use the field-tagged query, e.g. `IN/"Smith; John"`) or by assignee/company (`AN/"Acme Corp"`); combine with a date range to narrow.
3. Open a result: read the inventor block (names + residence city/state), the assignee (`employer-org`), and the co-inventors.
4. For ownership changes, cross-check the **Assignment Center**; for bulk work use the free Open Data Portal API.
5. Pivot: an inventor's city feeds people-search in that area; the assignee feeds a business-registry/LinkedIn lookup; co-inventors are strong `associate` leads.

## Inputs → Outputs
- **In:** inventor `name` (or `employer-org`/assignee), optionally a keyword or date range
- **Out:** inventor `name` + residence city/state (`address`), assignee `employer-org`, co-inventor `associate`s, patent/application numbers
- **Empty/negative result looks like:** no matching patents — the person never filed (most people haven't), the name is spelled differently, or their work was assigned so the inventor field uses a variant; absence says nothing beyond "no US patent under that exact name."

## Gotchas & OpSec
- Residence is **as-of-filing**, sometimes years old — a lead to a past location, not necessarily current.
- Common names collide; disambiguate using the assignee, technology area, and co-inventors.
- Only issued patents and published applications appear; unpublished/abandoned filings may not.

## Overlaps ("do both")
- Pairs with the patent attorney/agent search and legacy TESS trademark search for the same entity, and with business-registry lookups to resolve the assignee to people.

## Trust & verifiability
`trust: trusted` — the primary USPTO record; every field is verifiable in the official document, so findings are court-grade with the patent number as citation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | us-patent-office-search |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → address, employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: estonia
name: Estonia e-Business Register
description: Use when you have a `name` or `employer-org` linked to Estonia and want registered companies, board members, beneficial owners and registered addresses — returns `employer-org`, `associate`, `address`, `name`.
url: https://ariregister.rik.ee/eng
category: public-records
path:
- public-records
bestFor: Tying an Estonian person to the companies they own, direct or serve on the board of, plus registered addresses.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- employer-org
- associate
- address
- name
status: live
pricing: freemium
costNote: Free official state register — quick search of legal entities, officers and beneficial owners is no-cost. Some detailed/bulk features are reserved for contractual clients, but core people/company lookups are free.
opsec: passive
opsecNote: Official government register; queries hit the state portal, not the subject. Passive. No login needed for basic search, so no account of yours is exposed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Estonian Centre of Registers and Information Systems / Tartu County Court registration department — an authoritative primary source.
missingPersonsRelevance: medium
coverage:
- ee
auth: none
api: true
localInstall: false
registration: false
aliases:
- ariregister
- Estonian e-Business Register
- Äriregister
tags:
- companysites
- Company Related Sites
- corporate-registry
- beneficial-ownership
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Estonia e-Business Register

> Estonia's official companies register (ariregister.rik.ee): the authoritative source for who owns, directs and is the beneficial owner of any Estonian legal entity.

## When to use
You have a `name` (or a company `employer-org`) with an Estonian connection and want to establish the corporate footprint: which companies a person owns or sits on the board of, who the co-directors and beneficial owners are (`associate` links), and the registered addresses. Estonia's register is unusually open and English-accessible, making it a strong node when a subject or their money touches Estonian entities.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ariregister.rik.ee/eng.
2. Use quick search for a company name or registry code; use detailed search for extended parameters. You can also search on a person to find their board memberships.
3. Open an entity to read its officers/board members, beneficial owners, registered address, status and reporting.
4. Note co-officers and beneficial owners as `associate` pivots, and the registered `address`.
5. Pivot: run associates back through the register to build the network; cross-check addresses in mapping tools and the person against other EU registers.

## Inputs → Outputs
- **In:** `name`, company `employer-org`, or `address`
- **Out:** `employer-org` (companies), `associate` (co-officers/owners), `address`, `name` (officers/beneficial owners)
- **Empty/negative result looks like:** no matching entity/officer — the subject has no Estonian company role (or it's under a different name-transliteration); try alternate spellings of Estonian names.

## Gotchas & OpSec
- Name transliteration matters (Estonian characters õ/ä/ö/ü); try variants.
- A registered address is the company's, not necessarily a person's home.
- Some deep/bulk data and documents sit behind the paid contractual-client tier; the free tier still gives officers, beneficial owners and addresses.
- An official API exists for programmatic access if you need scale.

## Overlaps ("do both")
- Pairs with pan-EU aggregators (OpenCorporates, the Business Registers Interconnection System) — use this primary register to confirm what an aggregator reports, since the state source is the ground truth.

## Trust & verifiability
`trust: trusted` — it is the Estonian state's primary corporate register; data is authoritative, though always sanity-check that a common name matches the right individual before asserting a link.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | estonia |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address → employer-org, associate, address, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: intelligence-x
name: Intelligence X (Tools)
description: Use when you have any selector (`email`, `domain`, `ip-address`, `username`, `name`, `phone`, `crypto-wallet`, `vin`) and want a one-stop launcher of specialist lookups for it — returns links into services that yield `document-id`/`social-profile`.
url: https://intelx.io/tools
category: search-engines
path:
- search-engines
bestFor: A curated launcher page of free selector-specific OSINT lookups (email, domain, IP, username, person, phone, bitcoin, VIN, image, hash) plus social-media graph tools.
selectorsIn:
- email
- domain
- ip-address
- username
- name
- phone
- crypto-wallet
selectorsOut:
- document-id
- social-profile
status: live
pricing: freemium
costNote: The /tools launcher and its selector lookups are free; Intelligence X's own leak/darkweb archive search (separate product) is freemium with paid tiers for full results.
opsec: passive
opsecNote: The Tools page mostly hands off to third-party lookups; treat each downstream service on its own merits. The launcher itself is passive, but some linked services (e.g. account-existence checks) are active — read each tool's own note before running it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Intelligence X is a well-known OSINT/archival company; its Tools page is a maintained, widely-used launcher, though the destinations are third-party services of varying quality.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- facebook-graph-searcher-intelligencex
- intelligence-x-2
- intelligence-x-person-tools
- intelligence-x-telegram-search
- intelligencex
- intelligencex-linkedin-search
- intelx-io
aliases:
- IntelX
- intelx.io tools
tags:
- speciality-search-engines
- selector-search
source: awesome-osint
lastVerified: '2026-07-16'
enrichment: full
---

# Intelligence X (Tools)

> A single launcher page of free, selector-specific OSINT lookups — pick your selector type and it points you at the right specialist tools for it.

## When to use
You have a selector — an `email`, `domain`, `ip-address`, `username`, `name`, `phone`, `crypto-wallet`/bitcoin address, `vin`, image, or hash — and want a fast, organized menu of the lookups worth trying for that selector, plus social-media graph tools (Facebook Graph, X/Twitter, LinkedIn, Telegram, YouTube). It is an orientation/launcher hub rather than a single database.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://intelx.io/tools .
2. Find the section matching your selector (email lookup, domain, IP, username, person, phone, bitcoin, VIN, hash, image, location, or the social-media tools).
3. Launch the relevant lookup(s) and enter your selector there.
4. Read the output: results from the linked service — typically records/pages (`document-id`) or profiles (`social-profile`).
5. Pivot: chain outputs across sections (e.g. an email → username → person tools); use the "Selector Extraction" tool to pull selectors out of a document to feed back in.
6. For breach/leak coverage specifically, use Intelligence X's separate archive search (freemium) rather than this launcher.

## Inputs → Outputs
- **In:** `email`, `domain`, `ip-address`, `username`, `name`, `phone`, `crypto-wallet` (and more)
- **Out:** `document-id`, `social-profile` (via the linked specialist services)
- **Empty/negative result looks like:** a linked service returns nothing — that reflects the destination tool, not IntelX; try another lookup in the same section.

## Gotchas & OpSec
- It largely aggregates/links to third-party services — quality, freshness and privacy vary by destination; vet each one.
- Don't confuse the free Tools launcher with IntelX's paid leak/darkweb archive (a distinct freemium product).
- OpSec: the launcher is passive, but some destinations are active (account-existence, direct queries) — check before running.

## Overlaps ("do both")
- Pairs with its sibling IntelX tools — `[[intelligence-x-person-tools]]`, `[[intelligence-x-telegram-search]]`, `[[facebook-graph-searcher-intelligencex]]`, `[[intelligencex-linkedin-search]]` — run the specific ones relevant to your selector rather than only the launcher.

## Trust & verifiability
`trust: community` — a reputable, well-maintained launcher from a known OSINT company; reliability of any given result depends on the third-party service it links to, so verify at the destination.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | intelligence-x |
| category | search-engines |
| selectorsIn → selectorsOut | email, domain, ip-address, username, name, phone, crypto-wallet → document-id, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

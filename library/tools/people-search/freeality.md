---
id: freeality
name: Freeality
description: Use when you have a `name`, `phone`, `email`, or `address` in the US and want a fast link-hub of free reverse-lookup searches — returns pre-built queries to many people/reverse directories yielding address, phone, and associate leads.
url: http://www.freeality.com/finde.htm
category: people-search
path:
- people-search
bestFor: A legacy one-page launcher of many free US reverse-lookup searches by name, phone, email, or address.
selectorsIn:
- name
- phone
- email
- address
selectorsOut:
- address
- phone
- social-profile
- associate
status: degraded
pricing: free
costNote: Free link hub; no account. Many of the third-party directories it points to now charge or have changed, so hit-rate varies.
opsec: passive
opsecNote: Freeality just builds and launches searches against other sites in your browser — the actual queries hit those third parties, so your browser/IP reaches them. Use a sock-puppet browser. No subject is notified.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing free people-search portal (link aggregator). It hosts no data itself; result quality depends entirely on the destination directories, many of which are dated.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- inteltechniques-tools-search-engines-suite
aliases:
- Freeality
- freeality.com
tags:
- toddington
- curated-directory
- people-search
- link-hub
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# Freeality

> A classic one-page launcher for free US reverse-lookup searches — feed it a name, phone, email, or address and it fires queries at many people directories.

## When to use
You have a US selector (`name`, `phone`, `email`, or `address`) and want a quick breadth-first sweep across many free reverse-lookup directories without visiting each by hand. It's a legacy convenience hub — good for a fast first pass, weak as a primary source because it only forwards you to third-party sites whose quality varies.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.freeality.com/finde.htm in a sock-puppet browser.
2. Pick the search type (reverse phone, email, name, address) and enter the value.
3. It launches the query against a linked directory; work through the offered engines, since coverage differs per source.
4. Pivot: promising hits (address, relatives) feed a dedicated people-search; for a broader, better-maintained launcher use `[[inteltechniques-tools-search-engines-suite]]`.

## Inputs → Outputs
- **In:** `name` / `phone` / `email` / `address` (US)
- **Out:** `address`, `phone`, `associate` (relatives/neighbors), `social-profile` links — surfaced from destination directories
- **Empty/negative result looks like:** the linked directory returns nothing or now demands payment — a dead/paywalled downstream source, not proof the person is absent; try the other listed engines.

## Gotchas & OpSec
- Human-in-the-loop: none, but expect to click through several stale links.
- OpSec: **passive** — queries go from your browser to third parties; sock-puppet it.
- **Degraded:** it's an old aggregator; many linked services have changed or gone paywalled, so treat it as a launcher, not a data source.

## Overlaps ("do both")
- Pairs with `[[inteltechniques-tools-search-engines-suite]]` — both are query launchers; IntelTechniques is better maintained, Freeality occasionally reaches older directories the newer suite drops.

## Trust & verifiability
`trust: community` — a hosting-nothing link aggregator; reliability is entirely that of the sites it forwards to. Verify any hit on the destination source directly, and note downstream data is often years out of date.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | freeality |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, email, address → address, phone, social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

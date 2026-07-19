---
id: app-store-and-itunes-search-engine
name: App Store and iTunes Search (fnd.io)
description: Use when you have a developer/company `name` or app name and want to find their App Store/iTunes apps and developer identity — returns app listings, developer names and links.
url: https://fnd.io/
category: search-engines
path:
- search-engines
bestFor: A web front-end to search Apple's App Store/iTunes catalogue by app or developer, from any browser without iTunes installed.
selectorsIn:
- name
- username
selectorsOut:
- employer-org
- social-profile
status: live
pricing: freemium
costNote: Free to search and browse listings; the apps/media themselves are sold on Apple's stores (fnd just surfaces the catalogue).
opsec: passive
opsecNote: Searching a catalogue front-end is passive; the developer/target is not notified. It queries Apple's public catalogue via a third party — use a sock-puppet browser if you want the lookup unattributed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party web interface over Apple's App Store/iTunes catalogue; data originates from Apple, but the front-end is community-run and could lag or change.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- fnd.io
- fnd App Store search
tags:
- app-store
- itunes
- apple
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# App Store and iTunes Search (fnd.io)

> A browser front-end to Apple's App Store/iTunes catalogue — search apps and developers without opening iTunes, useful for tying a subject to the apps they've published or for enumerating a developer's portfolio.

## When to use
You want to connect a person or `employer-org` to Apple ecosystem apps: find every app a developer has published, identify the developer/company name behind an app, or check an app's details (name, publisher, links). Given a developer/company `name`, app name, or handle, fnd.io surfaces the catalogue entries and developer identity from any browser.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://fnd.io/ and search by app name, developer/company `name`, or keyword.
2. Open a result to see the app's publisher/developer, description, and store links.
3. From the developer name, pivot to their other apps to map a portfolio.
4. Cross-check the developer identity against Apple's live App Store page to confirm current data.
5. Pivot: a developer `employer-org`/`social-profile` (support URL, website) feeds domain/company OSINT; app support links often reveal contact details.

## Inputs → Outputs
- **In:** app name, developer/company `name`, or `username`
- **Out:** app listings, publisher/`employer-org` identity, and developer `social-profile`/support links
- **Empty/negative result looks like:** no matching apps — the subject may have published nothing on Apple's stores, uses a different developer name, or the front-end's data is stale. Confirm on Apple's own App Store.

## Gotchas & OpSec
- Third-party front-end — data can lag Apple's live catalogue; verify key facts on the official store.
- App developer names can be corporate shells; the publisher name isn't always the individual.
- OpSec: passive; use a sock puppet if you want the search unattributed.

## Overlaps ("do both")
- Pairs with Google Play/developer searches and app-privacy/permission analysers — this covers the Apple side, while Play and teardown tools cover Android and an app's data behaviour.

## Trust & verifiability
`trust: unverified` — a community front-end over authoritative Apple catalogue data; treat listings as reliable-but-possibly-stale and confirm anything important on the official App Store.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | app-store-and-itunes-search-engine |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → employer-org, social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

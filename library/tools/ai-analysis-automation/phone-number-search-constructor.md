---
id: phone-number-search-constructor
name: Phone Number Search Constructor
description: Use when you have a `phone` and want one-click search queries/links across dozens of engines, social sites and lookup services — returns social-profile, name and associate leads.
url: https://cipher387.github.io/phonenumberqueryconstructor/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Generating ready-to-run search queries and lookup links for a phone number across many services at once.
selectorsIn:
- phone
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free, static browser tool hosted on GitHub Pages (cipher387). No account or install; it only builds links, it doesn't call paid APIs itself.
opsec: passive
opsecNote: The constructor itself is passive — it just builds URLs in your browser and reveals nothing to anyone. OpSec depends on which generated links you then click: some open search engines (low exposure), others open a service that may log or notify. Open generated links in a sock-puppet browser and review where each points before clicking.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Made by cipher387, a prolific OSINT tool author; it's a transparent link/dork builder — trustworthy as a launcher, though the destination services' quality varies.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- phonenumberqueryconstructor
- Phone Number Query Constructor
tags:
- My Projects
- phone-osint
- dork-builder
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Phone Number Search Constructor

> A one-page "dork builder" for phone numbers — type a number once and it generates search queries and direct lookup links across dozens of engines, social platforms, and phone-OSINT services.

## When to use
You have a `phone` number and want to run it through many places fast without hand-crafting each query: Google/Bing dorks, social-network search URLs, messenger checks, and phone-reputation/lookup services. The constructor saves the tedium of formatting the number for each service and gives you a launch pad of clickable links. Ideal as the opening move of phone-number OSINT, before drilling into whichever service returns a hit.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cipher387.github.io/phonenumberqueryconstructor/ in a sock-puppet browser.
2. Enter the `phone` number (mind the format/country code as the tool specifies).
3. It generates a list of search queries and direct links across services.
4. Review where each link points, then open the relevant ones (start with passive search-engine links).
5. Pivot: a hit on a social/lookup service → follow into that platform's tooling; a matched `name`/handle → people and username search.

## Inputs → Outputs
- **In:** a `phone` number
- **Out:** ready-to-run search queries and lookup links; following them can surface `social-profile`s, an owner `name`, and linked `associate`s
- **Empty/negative result looks like:** the tool always builds links — "empty" is when every destination returns nothing, meaning the number has a thin online footprint (common for private/mobile numbers), not a tool failure.

## Gotchas & OpSec
- It only builds links — the actual data (and its quality) comes from each destination service; some are stale or region-limited.
- Some generated links open services that log or notify — read the target before clicking; use a sock-puppet.
- Format matters — enter the number as each service expects (with/without country code).

## Overlaps ("do both")
- Complements dedicated phone tools (PhoneInfoga, Truecaller-style lookups) — the constructor is the broad launcher; those give depth on a single service.

## Trust & verifiability
`trust: community` — a transparent, well-regarded link builder; trust the launcher, but verify every result at its source since destinations vary widely in reliability.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | phone-number-search-constructor |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | phone → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

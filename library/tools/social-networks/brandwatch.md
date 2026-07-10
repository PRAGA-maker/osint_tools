---
id: brandwatch
name: Brandwatch
description: Use when you have a `name`, handle, or keyword and want enterprise-scale social listening across platforms — returns aggregated mentions, sentiment, and trend/audience analytics (not individual-profile lookup).
url: https://www.brandwatch.com
category: social-networks
path:
- social-networks
bestFor: Large-scale monitoring of mentions/sentiment for a name, brand, or keyword across social and web.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Enterprise SaaS — effectively paid-only. There is no self-serve free tier; access is via a sales demo/trial and paid contract. Author-accurate pricing is "gated behind enterprise sales," so treat as inaccessible without a paid account.
opsec: passive
opsecNote: Passive — it analyses publicly posted content at aggregate scale, not by contacting targets. But it requires a corporate account tied to your organisation, so usage is fully attributable to you; it is not a covert individual-lookup tool.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Brandwatch is a major, legitimate enterprise social-listening/analytics vendor; strong for aggregate trends, weak/ill-suited for pinpointing a single individual.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Brandwatch Consumer Intelligence
- brandwatch.com
tags:
- real-time-search-social-media-search-and-general-social-media-tools
- social-listening
- analytics
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Brandwatch

> An enterprise social-listening platform that ingests billions of public posts to track mentions, sentiment, and trends for a keyword or name at scale — powerful for aggregate monitoring, but a corporate tool, not a person-finder.

## When to use
You have a `name`, handle, or keyword and need broad, historical, cross-platform monitoring — every public mention of a term, sentiment over time, who's amplifying it, where conversation clusters. This suits reputation, threat-trend, and network-scale analysis. It is poorly suited to the core missing-person task of resolving one individual's accounts/whereabouts, and it's gated behind an enterprise contract, so reach for it only when you already have access and the question is genuinely aggregate.

## How to use it (`bestInteractionPattern`: web-manual)
1. Access requires a Brandwatch account (enterprise contract / sales-arranged trial) — there is no public self-serve entry.
2. Build a query for the `name`/keyword/handle, with boolean filters, date range, platform, and location scoping.
3. Run it to get aggregated mentions, sentiment breakdown, top authors/`social-profile`s, and trend charts.
4. Drill into top authors and specific mentions for leads; export via dashboards or the API.
5. Pivot: surfaced author handles feed username enumeration (`[[snoop]]`, `[[gaddr]]`); a mention pinpointing a location/event feeds geolocation work.

## Inputs → Outputs
- **In:** `name` / `username` / keyword query
- **Out:** aggregated mentions, sentiment, top authors (`social-profile`), trend/audience analytics
- **Empty/negative result looks like:** few or no mentions for the term — meaning low public conversation volume, not that a person doesn't exist. This tool measures conversation, not identity.

## Gotchas & OpSec
- Enterprise-gated: no usable free tier — without a paid account you cannot run it. That's the main barrier for most investigators.
- Built for aggregate insight, not individual attribution — don't expect a per-person profile dossier.
- Coverage depends on platform data-licensing (which shifts, e.g. reduced Twitter/X access industry-wide); recent-data completeness varies.
- Usage is tied to a corporate account — attributable, not covert.

## Overlaps ("do both")
- For individual-account discovery use username enumerators (`[[snoop]]`, `[[gaddr]]`, `[[360username-com]]`) instead — Brandwatch complements them only at the aggregate/trend layer.
- Author handles it surfaces feed those enumerators and face/image tooling.

## Trust & verifiability
`trust: community` — a reputable enterprise vendor whose aggregate analytics are sound, but it's the wrong altitude for pinpointing one person and is paywalled. Treat its output as conversation-level intelligence and drill down to primary posts before attributing anything to an individual.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | brandwatch |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, payment-wall-partial) |

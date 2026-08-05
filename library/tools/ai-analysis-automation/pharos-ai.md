---
id: pharos-ai
name: Pharos AI (Conflicts)
description: Use when you have a region or ongoing conflict and want an AI-curated live feed of events, actors, and signals mapped from open sources — returns geolocated event/actor intelligence (no subject PII).
url: https://conflicts.app
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Getting a live, AI-curated situational picture of a conflict — events, actors, and signals on a map.
selectorsIn: []
selectorsOut:
- geolocation
- employer-org
status: live
pricing: free
costNote: Free to access; the project takes voluntary donations to cover server costs.
opsec: passive
opsecNote: You read a published conflict-monitoring dashboard — nothing you do reaches any subject. Only your own browsing is visible to the service.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An AI-curated conflict-intelligence aggregator; useful for situational awareness, but AI-summarised events must be traced back to their cited primary sources before being relied on.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- conflicts.app
- Pharos
tags:
- threat-intelligence
- conflict-monitoring
- geopolitical
- osint-feed
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# Pharos AI (Conflicts)

> A live, AI-curated conflict observatory: it pulls open-source reporting into a map of events, actors, and signals so you can read the state of a conflict at a glance rather than trawling feeds yourself.

## When to use
An investigation intersects a geopolitical conflict or unstable region — a subject's location, a claimed event, an organisation's activity — and you need fast situational context: what is happening where, who the actors are, and what recent signals matter. Pharos returns event/actor/geographic intelligence, not data about a private individual, so it sets context rather than identifying people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://conflicts.app (no login).
2. Browse the sections — EVENTS, ACTORS, SIGNALS, BRIEF, MAP, DATA — or focus on the region/conflict of interest.
3. Read the AI-curated feed: dated events, the actors involved, and geolocated markers on the map.
4. **Trace before trusting:** follow each event to its cited primary source before relying on it.
5. Pivot: a confirmed event/location grounds a timeline or a subject's whereabouts; named actors/orgs feed entity and org OSINT.

## Inputs → Outputs
- **In:** a region or conflict you browse toward (no subject PII entered)
- **Out:** geolocated events, actor profiles, and signals (`geolocation`, `employer-org`/actor names)
- **Empty/negative result looks like:** thin or stale coverage for a low-salience area — the AI curation favours active, well-reported conflicts, so quiet regions may be sparsely covered.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive — you only read a public dashboard; it does not touch your subject.
- It is AI-curated: events can be mis-summarised, mislocated, or duplicated. Always verify a decisive event against the primary reporting it links to.

## Overlaps ("do both")
- Pairs with authoritative conflict datasets (e.g. ACLED) and live mapping/verification tools — Pharos gives a fast AI-curated overview, those give vetted, citable event records; corroborate before you act.

## Trust & verifiability
`trust: community` — a community-run AI aggregator, not a primary authority. Its value is speed and synthesis; the credibility of any individual event rests on the source it cites, so trace it there before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pharos-ai |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  → geolocation, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

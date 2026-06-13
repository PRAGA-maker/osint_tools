---
id: beholder
name: Beholder
description: Use when you want a geolocated, real-time map of crisis/incident signals for a US area — but expect access to be gated behind InfraGard membership/login.
url: https://beholder.infragard.io/
category: geolocation
path:
- geolocation
- map-reporting-tools
bestFor: Monitoring mapped, real-time incident/crisis signals over a geographic area (access-gated).
selectorsIn: [geolocation, address]
selectorsOut: [geolocation]
status: degraded
pricing: free
costNote: No per-use fee, but the site is gated — the public endpoint returns HTTP 403 and it sits on the InfraGard (infragard.io) domain, which is a vetted, membership-only US program; usable access likely requires InfraGard membership/login.
opsec: passive
opsecNote: A read-only situational map; it does not contact any person of interest. Access requires authenticating to an InfraGard account, which ties your usage to a vetted real identity.
humanInLoop: true
humanInLoopReason: [account-login, legal-gate]
bestInteractionPattern: web-manual
trust: community
trustNote: Hosted on infragard.io, the domain of InfraGard (an FBI-private-sector partnership); legitimate but access-restricted to vetted members, and the public URL is not openly reachable (403).
missingPersonsRelevance: low
coverage: [us]
auth: account
api: false
localInstall: false
registration: true
invitationOnly: true
deprecated: false
relatedTools: [arcgis, bing-maps]
aliases: [beholder-infragard]
tags: [infragard, situational-awareness, incident-map, gated]
source: arf-seed
lastVerified: '2026-06-13'
enrichment: full
---

# Beholder

> An InfraGard-hosted situational-awareness map of geolocated incident/crisis signals — but the public endpoint is access-gated (returns HTTP 403), so it's only usable to vetted InfraGard members.

## When to use
You're monitoring a US `geolocation`/`address` and want real-time, mapped incident or crisis signals layered over it (e.g. to understand current conditions in a search area). In practice, reach for this only if you already hold InfraGard membership: the open URL does not load for the public, so for most investigators this is a "know it exists, can't open it" entry rather than a working tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Navigate to https://beholder.infragard.io/. Unauthenticated requests currently return **HTTP 403 Forbidden**.
2. Access requires an InfraGard account — InfraGard is a vetted, members-only FBI/private-sector partnership; membership is application-and-screening based (US persons).
3. If you are a member, sign in via the InfraGard portal and then open Beholder to view the mapped event feed for your area of interest.
4. Read the map for incidents with source context/timelines; filter by geography.
5. Pivot: for open alternatives, use `[[arcgis]]` live-feed layers or `[[bing-maps]]` instead.

## Inputs -> Outputs
- **In:** `geolocation`, `address` (the area you filter the map to)
- **Out:** `geolocation` (mapped events/incident points)
- **Empty/negative result looks like:** the 403/login wall if you're not a member; for members, no events in a quiet area.

## Gotchas & OpSec
- **Access-gated:** the public endpoint is Forbidden; without InfraGard membership you cannot use it. Do not try to bypass authentication.
- Membership is a legal/vetting gate (US-person screening) — this is not an anonymous tool, and use is tied to your real, vetted identity.
- Scope is US situational awareness, not people-finding; relevance to a specific missing person is indirect.

## Overlaps ("do both")
- Use `[[arcgis]]` Living Atlas live feeds (weather/fire/traffic) as an open substitute for situational layers.
- Pairs with `[[bing-maps]]` for base imagery of the same area.

## Trust & verifiability
`trust: community` — hosted on the legitimate InfraGard domain (an FBI–private-sector partnership), but the public endpoint is not reachable (403) and real access is membership-gated. Marked `status: degraded` because it exists and is legitimate yet is not openly usable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | beholder |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free (membership-gated) |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, legal-gate) |

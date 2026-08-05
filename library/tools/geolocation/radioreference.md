---
id: radioreference
name: RadioReference
description: Use when you have a `geolocation`/`address` or an agency name and want the radio frequencies, talkgroups, and scanner systems serving that area — returns local comms infrastructure tied to `employer-org`.
url: https://www.radioreference.com/apps/db/
category: geolocation
path:
- geolocation
bestFor: Looking up police/fire/EMS and other radio frequencies and trunked systems by US county, city, or agency.
selectorsIn:
- geolocation
- address
- employer-org
selectorsOut:
- employer-org
status: live
pricing: freemium
costNote: Core database browsing (frequencies, agencies, systems by location) is free; a paid Premium subscription unlocks full trunking/talkgroup detail, downloads, and live audio feeds.
opsec: passive
opsecNote: You are browsing a public database of publicly licensed radio infrastructure — no target is queried and nothing is notified. Optional free/Premium account ties browsing to an identity; browse logged-out or with a sock-puppet account to avoid linking searches to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running, well-known crowd-sourced database (RadioReference/RadioReference.com) cross-referenced with FCC ULS licensing data; entries are user-submitted so freshness varies by locality.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- radioreference-communications-wiki
- radioreference-station-search
aliases:
- RadioReference Database
- RR DB
tags:
- radio-frequencies
- scanner
source: osint4all
lastVerified: '2026-08-05'
enrichment: full
---

# RadioReference

> The US master database of radio frequencies, trunked systems, and talkgroups, browsable by location or agency — the map from a place to the public-safety comms that cover it.

## When to use
You have a search area — a county, city, or `address` — or a specific agency (`employer-org`, e.g. a sheriff's office), and you want to know what radio systems and frequencies operate there. In a missing-persons or field context this tells you which police/fire/EMS/aviation channels cover a search zone, so you can locate a live scanner feed, understand who is responding, or corroborate an agency's presence in an area.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.radioreference.com/apps/db/.
2. Browse **by location** (drill State → County) or use the text search for an agency/system name; "Near Me" uses your location.
3. Read the listing: individual frequencies, licensees, trunked systems and their sites, and talkgroups. Cross-referenced FCC license data shows the licensed agency (`employer-org`).
4. For live monitoring, jump to the matching **live audio feed** (feeds may require a free/Premium account).
5. Pivot: an agency name → confirm jurisdiction/coverage of a search area; a frequency → a scanner feed you can monitor; FCC licensee data → an org/address lead.

## Inputs → Outputs
- **In:** `geolocation` / `address` (county/city) or `employer-org` (agency/system name)
- **Out:** frequencies, trunked systems, talkgroups, and the licensed agency (`employer-org`) serving that location
- **Empty/negative result looks like:** a county with sparse or "no data" entries (rural areas and encrypted systems are under-documented) — absence means "not submitted / encrypted," not "no radio system exists."

## Gotchas & OpSec
- Human-in-the-loop: none for browsing; live feeds and full trunking detail may prompt a free or Premium login.
- Coverage: US-centric and crowd-sourced — dense in urban areas, thin in rural ones; increasingly agencies are encrypted, so listed frequencies may no longer be monitorable in the clear.
- OpSec: passive — this is public licensing/infrastructure data; browsing does not touch any subject.

## Overlaps ("do both")
- Pairs with [[radioreference-communications-wiki]] (narrative/how-to context on systems) and [[radioreference-station-search]] (station-level lookups) — the DB gives the frequency table, the wiki explains the system, and station search resolves specific transmitters.

## Trust & verifiability
`trust: community` — a mature, widely used crowd-sourced database backed by FCC license cross-references; core facts (licensed frequencies/agencies) are authoritative via FCC, while talkgroup/feed details are user-maintained and vary in freshness.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | radioreference |

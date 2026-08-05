---
id: osint-on-the-ocean
name: OSINT on the Ocean
description: Use when your subject involves a ship, port, or the sea and you want a method — returns a techniques playbook pointing to `geolocation`/vessel (`employer-org`) sources.
url: https://wondersmithrae.medium.com/osint-on-the-ocean-maritime-intelligence-gathering-techniques-2ee39e554fe1
category: transportation
path:
- transportation
bestFor: Learning the workflow and source list for maritime/vessel intelligence before running the actual lookups.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: A free public Medium article; no paywall required to read the techniques (Medium may show a soft metered wall — open in a private window if so).
opsec: passive
opsecNote: It's a blog post — reading it involves only Medium, not the subject. The techniques it teaches (AIS lookups, port cams) are themselves passive; note that some downstream vessel-tracking sites gate history behind accounts.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An educational write-up by a well-regarded OSINT practitioner (wondersmithrae); it's a methodology guide, not a data source, so verify current tool availability yourself.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- fleetmon
- ais-ships-map
- ais-boatnerd-com
aliases:
- Maritime Intelligence Gathering Techniques
- OSINT on the Ocean (wondersmithrae)
tags:
- maritime
- vessel-tracking
- methodology
- guide
source: osint4all
lastVerified: '2026-08-05'
enrichment: full
---

# OSINT on the Ocean

> A practitioner's how-to for maritime intelligence — the reading you do before you start chasing a vessel, so you know which AIS, registry, and imagery sources exist and how they fit together.

## When to use
Your case touches the sea: a subject on or near a ship, a container/cargo question, a coastal `geolocation`, a fishing or leisure vessel, a port. This guide by wondersmithrae walks the maritime OSINT workflow — identifying and tracking vessels via AIS, reading ship identifiers (IMO/MMSI/call sign), using port webcams and satellite imagery, and finding ownership/registry records. Treat it as the map that tells you which specific tool to open next, not as a lookup itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the article (private window if Medium meters you).
2. Read for the *method*: how to go from a ship name/photo to an IMO/MMSI, then to live and historical position, then to owner/operator (`employer-org`).
3. Note the concrete sources it recommends and the order of operations.
4. Execute against the live tools: track position with `[[ais-ships-map]]` / `[[fleetmon]]`, cross-check with `[[ais-boatnerd-com]]`, and pull registry/ownership from the appropriate national vessel registry.

## Inputs → Outputs
- **In:** `geolocation` / a maritime lead (ship name, port, coastal point)
- **Out:** a technique + source list that leads to `geolocation` (vessel position) and vessel operator `employer-org`
- **Empty/negative result looks like:** N/A for the article itself; downstream, an AIS lookup returns nothing when a vessel has AIS off, is too small to be required to transmit, or is out of receiver range — a common and meaningful signal in itself.

## Gotchas & OpSec
- It's a guide, not live data — some named tools may have changed pricing or gone behind logins since publication; verify each before relying on it.
- Small craft and vessels with AIS disabled are invisible to AIS trackers; don't read absence as proof a vessel wasn't there.
- OpSec: passive reading; the downstream AIS/imagery lookups are also passive.

## Overlaps ("do both")
- This is the methodology; the execution tools are `[[ais-ships-map]]`, `[[fleetmon]]`, and `[[ais-boatnerd-com]]` — read the guide, then run all three since AIS coverage differs by receiver network.

## Trust & verifiability
`trust: community` — a respected practitioner's tutorial; it's reliable as *guidance*, but always confirm a tracked position or ownership fact against the primary AIS/registry source before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-on-the-ocean |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

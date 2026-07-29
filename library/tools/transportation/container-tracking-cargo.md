---
id: container-tracking-cargo
name: container-tracking.org
description: Use when you have a shipping container number and don't know its carrier — returns links into the right carrier/lessor tracking portal to locate the container.
url: https://container-tracking.org
category: transportation
path:
- transportation
bestFor: A directory/gateway of container and leasing-company tracking portals — the fast way to find which carrier's tracker to use for a given container.
selectorsIn:
- document-id
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free directory of carrier/lessor tracking links; no account. Tracking itself happens on each carrier's own site.
opsec: passive
opsecNote: A directory of links — you disclose only the container number to whichever carrier portal you follow; shipment parties aren't notified. As with any single-source tracker, cross-checking is wise.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A convenience aggregator/directory pointing to carriers' official trackers; the authoritative data lives on each carrier's site, so trust those, not the directory itself.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- maersk-tracking
- vesselfinder
- marinetraffic
- container-tracking
aliases:
- container-tracking.org
- Container-Tracking directory
tags:
- container-tracking
- shipping
- logistics
- transport
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# container-tracking.org

> A directory/gateway to shipping-container and leasing-company tracking portals — start here when you have a container number but don't know which carrier's tracker to use.

## When to use
You have a container number (the four-letter prefix + digits) from a document, photo, or manifest, and need to find where the box is — but you don't yet know the carrier or leasing company. container-tracking.org points you to the right tracking portal (including per-lessor subdomains like `textainer.container-tracking.org`), so you can jump straight to the source that actually tracks it. The container's prefix (owner code) tells you which operator, which this directory helps you resolve.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://container-tracking.org.
2. Identify the container's owner from its 4-letter prefix (e.g. `MSCU`, `TEMU`), and pick the matching carrier/lessor from the directory.
3. Follow the link to that operator's official tracker and enter the container number (or bill-of-lading/booking number).
4. Read the milestones/status on the carrier's site — origin/destination, latest port event, ETA (`geolocation` context).
5. Pivot: note the carrying vessel, then get its live position from `[[vesselfinder]]`/`[[marinetraffic]]`; if it's a Maersk box, go straight to `[[maersk-tracking]]`.

## Inputs → Outputs
- **In:** `document-id` — a container number (or B/L / booking number on the carrier's own tracker).
- **Out:** `geolocation` context — via the carrier portal it routes you to (route, port milestones, status).
- **Empty/negative result looks like:** no matching operator in the directory, or the carrier's tracker returns nothing for the number — check the prefix/owner code and try the operator directly, or a multi-carrier aggregator.

## Gotchas & OpSec
- Human-in-the-loop: none, but you must identify the right carrier from the container prefix.
- OpSec: **passive** — no shipment party is alerted; you only submit the number to the carrier's site you choose.
- It's a directory, not the data source: accuracy/coverage lives on each carrier's tracker, and directory links can go stale. Confirm on the operator's official site.
- Owner-code lookups (BIC) can help when the prefix isn't obvious.

## Overlaps ("do both")
- Pairs with `[[maersk-tracking]]` and other carrier-specific trackers — this directory routes you to them; go direct when you already know the carrier.
- Feeds `[[vesselfinder]]` / `[[marinetraffic]]` — once you have the vessel, track its live position there.

## Trust & verifiability
`trust: community` — a convenience directory. The authoritative tracking data is the carriers' own portals it links to, so verify status on the operator's site rather than treating the directory as the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | container-tracking-cargo |
| category | transportation |
| selectorsIn → selectorsOut | document-id → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

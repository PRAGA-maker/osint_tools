---
id: snapintel
name: SnapIntel
description: Use when you have a Snapchat `username` and want that account's public content — returns stories, spotlights, lenses, bitmoji and an upload-time heatmap.
url: https://github.com/Kr0wZ/SnapIntel
category: social-networks
path:
- social-networks
bestFor: Pulling and archiving a Snapchat user's public stories, spotlights, highlights, lenses and bitmoji from just their username.
selectorsIn:
- username
selectorsOut:
- image
- social-profile
- geolocation
status: live
pricing: free
costNote: Free and open source (AGPL-3.0); install locally with pip. No account, no API key.
opsec: active
opsecNote: The tool fetches public Snapchat endpoints for the target username from your machine — requests originate from your IP, so run it from a VPN/sock-puppet environment. It pulls only public content and does not require logging in as anyone, but downloading media is a footprint against Snapchat's servers; do not hammer it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Community open-source project (~325 stars) actively maintained into 2025; verify the code before running and pin to a reviewed commit.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- neutrosint
aliases:
- Kr0wZ SnapIntel
tags:
- snapchat
- python
source: gh-topic-osint-resources
lastVerified: '2026-07-18'
enrichment: full
---

# SnapIntel

> An open-source Python CLI that turns a Snapchat `username` into that account's public content — stories, spotlights, highlights, lenses, bitmoji — plus an upload-time heatmap.

## When to use
You have a Snapchat `username` for a subject and want everything the account exposes publicly: current and highlighted stories, spotlight clips, lenses, and their bitmoji avatar. The upload-timing heatmap can hint at a person's active hours/timezone, and story/spotlight media may contain background detail (`geolocation` clues, faces, companions) worth geolocating. Strong for confirming an account is live and harvesting media before it disappears.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and install: `git clone https://github.com/Kr0wZ/SnapIntel && cd SnapIntel && pip install .` (review the code first).
2. Run against the target: `snapintel -u <username>` (add the download flag to save media to a directory).
3. Read the output: listed stories/spotlights/highlights/lenses, the bitmoji, statistics, and the upload-date heatmap.
4. Pivot: downloaded media feeds reverse-image/face and geolocation tools; the heatmap's active hours corroborate a timezone; a bitmoji can confirm identity against other platforms.

## Inputs → Outputs
- **In:** `username` (Snapchat handle)
- **Out:** `image`/video media, `social-profile` (public account content), `geolocation` clues from media + activity heatmap
- **Empty/negative result looks like:** the username resolves but returns no public stories/spotlights — the account exists but is private or inactive; a non-resolving username means no such public account.

## Gotchas & OpSec
- Snapchat changes its unofficial endpoints; a version that worked last month may break — check for updates or open issues if it errors.
- Only public content is retrievable; there is no way (and no lawful reason) to reach a private account's snaps.
- OpSec: **active** — requests come from your IP; use a VPN and avoid excessive scraping that could get you rate-limited or flagged.

## Overlaps ("do both")
- Pairs with `[[neutrosint]]` and other username-pivot tools — SnapIntel deep-harvests one Snapchat account while cross-platform username tools confirm the same handle elsewhere.

## Trust & verifiability
`trust: community` — actively maintained open-source project, but it depends on undocumented Snapchat endpoints; read the source and treat output as public-content only.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | snapintel |
| category | social-networks |
| selectorsIn → selectorsOut | username → image, social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |

---
id: exportdata
name: ExportData
description: Use when you have a Twitter/X `username` and want to export their followers, followings, and tweet history at scale — returns associate links, social-profile and metadata.
url: https://www.exportdata.io/
category: social-networks
path:
- social-networks
bestFor: Bulk-exporting a Twitter/X account's followers, followings, and timeline to CSV/Excel for network and activity analysis.
selectorsIn:
- username
selectorsOut:
- associate
- social-profile
status: live
pricing: freemium
costNote: Pay-as-you-go — small exports/previews are cheap or free, but large follower/timeline exports consume paid credits. No subscription lock-in.
opsec: passive
opsecNote: You query public Twitter/X data through a third party; the target's account gets no interaction (no follow/view), so it is passive toward them. ExportData sees which handles you export — use a sock-puppet account and avoid exporting anything that signals your investigation.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: An established commercial Twitter-data service; data is scraped from public Twitter/X, so completeness depends on platform access at export time.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- ExportData.io
tags:
- twitter
- social-network-export
source: awesome-osint
lastVerified: '2026-07-14'
enrichment: full
---

# ExportData

> A no-code Twitter/X data exporter — turn a public account's followers, followings, and tweets into a downloadable CSV/Excel spreadsheet for analysis.

## When to use
You have a Twitter/X `username` and want the account's *network* and *history* as structured data rather than scrolling the timeline by hand. Exporting followers/followings surfaces `associate` links (who interacts with the subject), and exporting the timeline gives you a searchable record of posts, dates, and mentions — useful for building a subject's contact graph and activity pattern.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a sock-puppet account at https://www.exportdata.io/.
2. Choose an export type: followers, followings, timeline/historical tweets.
3. Enter the target `username` and run the export (large exports consume pay-as-you-go credits).
4. Download the CSV/Excel and analyse: sort followings for close associates, scan tweets for locations, mentions, and timeline.
5. Pivot: exported associate handles feed further username/social-profile enrichment; tweet content feeds geolocation and timeline reconstruction.

## Inputs → Outputs
- **In:** Twitter/X `username`
- **Out:** `associate` (followers/followings), `social-profile` (linked accounts), tweet `metadata` (dates, mentions, content)
- **Empty/negative result looks like:** empty or truncated export — the account is private, suspended, renamed, or platform rate-limits capped the pull. A partial export is not the full network.

## Gotchas & OpSec
- Twitter/X access restrictions change often; exports can be incomplete or fail — treat counts as a floor, not the truth.
- Large exports cost credits; scope the pull before spending.
- OpSec: passive toward the target, but the service logs the handles you export; use a burner login.

## Overlaps ("do both")
- Pairs with username-enumeration and profile tools — ExportData gives you the raw follower/following lists; carry the notable handles into per-account enrichment.

## Trust & verifiability
`trust: community` — a commercial scraper of public Twitter data; the data is authentic to the platform but only as complete as access allows, so verify key associates directly on X.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | exportdata |
| category | social-networks |
| selectorsIn → selectorsOut | username → associate, social-profile, metadata |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, payment-wall-partial) |

---
id: instagram-location-search
name: Instagram Location Search
description: Use when you have a `geolocation` (lat/long) and want the Instagram location tags near that point — returns location tag IDs to pivot into `social-profile` posts from that place.
url: https://github.com/bellingcat/instagram-location-search
category: social-networks
path:
- social-networks
bestFor: Finding Instagram location-tag IDs near a set of coordinates so you can then pull public posts geotagged at that place.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- social-profile
status: live
pricing: free
costNote: Free and open source (Bellingcat). No cost beyond running the Python script; you supply your own Instagram session cookie.
opsec: active
opsecNote: The tool queries Instagram's internal endpoints using YOUR logged-in session cookie, so activity is tied to that account and visible to Instagram. Always use a dedicated sock-puppet Instagram account and a clean IP, never a personal one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: trusted
trustNote: Published and maintained by Bellingcat as part of their open-source investigation toolkit; code is auditable on GitHub.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
relatedTools:
- auto-archiver
- bellingcat-tiktok-hashtag-analysis
- shadow-finder
- telegram-phone-number-checker-github-com
- wayback-google-analytics
aliases:
- bellingcat instagram-location-search
tags:
- bellingcat-toolkit
- instagram
- geosocial
source: bellingcat-toolkit
lastVerified: '2026-07-16'
enrichment: full
---

# Instagram Location Search

> A Bellingcat command-line tool that turns a set of coordinates into the Instagram location tags nearby — the first step to finding public posts made at a specific place.

## When to use
You have a `geolocation` (latitude/longitude) — a last-known location, a landmark, a place of interest — and want to discover which Instagram location tags exist near that point. Those tag IDs then let you browse public posts geotagged there, which can surface the subject or witnesses/`social-profile` who posted from the location.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/bellingcat/instagram-location-search and install its Python requirements.
2. Obtain an Instagram `sessionid` cookie from a **sock-puppet** account logged in via a browser, and supply it to the tool.
3. Run the script with the target latitude and longitude (and radius).
4. Read the output: nearby Instagram location tags with their IDs, names and coordinates (`geolocation`).
5. Pivot: open a location tag on Instagram to view public posts made there, collecting accounts (`social-profile`) and imagery; archive anything relevant with `[[auto-archiver]]`.

## Inputs → Outputs
- **In:** `geolocation` (lat/long + radius)
- **Out:** `geolocation` (Instagram location-tag IDs near the point), then `social-profile` (accounts posting at that tag)
- **Empty/negative result looks like:** no location tags returned for remote/sparse coordinates, or an auth error if the session cookie is invalid/expired.

## Gotchas & OpSec
- Requires a valid Instagram session cookie — it depends on Instagram's internal endpoints, which change and may rate-limit or block; expect occasional breakage.
- **Active/attributable:** all requests carry your session. Use a throwaway account and clean IP; assume Instagram logs the activity.
- Location tags are user-applied and can be inaccurate or spoofed — corroborate before concluding someone was physically present.

## Overlaps ("do both")
- Pairs with `[[auto-archiver]]` (preserve found posts) and other geosocial tools — this finds the location tags; the archiver captures the evidence before it disappears.

## Trust & verifiability
`trust: trusted` — an auditable Bellingcat toolkit project. The tool is reliable; the underlying data (user-applied geotags) still needs corroboration, and Instagram endpoint changes can affect it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | instagram-location-search |
| category | social-networks |
| selectorsIn → selectorsOut | geolocation → geolocation, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login) |

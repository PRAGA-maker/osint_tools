---
id: tinfoleak-py
name: Tinfoleak
description: Use when you have a Twitter/X `username` and want an automated intelligence report — profile, activity, geolocation history, media EXIF, and network — returns geolocation, social-profile, associates, and image metadata.
url: https://github.com/vaguileradiaz/tinfoleak
category: social-networks
path:
- social-networks
- twitter
- analytics
bestFor: Generating an automated Twitter/X intelligence report (activity, geolocation, media metadata, network) for a username.
selectorsIn:
- username
selectorsOut:
- geolocation
- social-profile
- associate
- image
- metadata-exif
status: degraded
pricing: free
costNote: The tool is free and open source, but it depends on Twitter/X API credentials — and since the 2023 API pricing overhaul, meaningful access requires a paid API tier, which is what actually gates it.
opsec: active
opsecNote: Runs from your machine against Twitter/X APIs using your API keys, tying the collection to your developer account. Use dedicated throwaway API credentials and, ideally, a VPN; heavy automated pulls can trip rate limits or account flags.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: A long-established, well-regarded open-source SOCMINT tool by Vicente Aguilera Díaz; the code is public, but functionality now hinges on unstable/paid Twitter API access.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- tinfoleak
- vaguileradiaz/tinfoleak
tags:
- twitter
- socmint
- geolocation
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# Tinfoleak

> A long-standing open-source Twitter/X intelligence tool: feed it a username and it builds a report of activity, geolocation history, media EXIF, and network — now gated by Twitter's paid API.

## When to use
You have a Twitter/X `username` and want a consolidated intelligence picture rather than manual scrolling: when/where the account posts, the devices/apps it uses, geolocated tweets and inferred routes, media with extractable EXIF, hashtags/mentions, and follower/friend relationships. Strong for building a subject's pattern-of-life and surfacing location leads in missing-persons and SOCMINT work — *if* you can supply working API access.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/vaguileradiaz/tinfoleak` and install Python deps: `tweepy`, `pillow`, `exifread`, `jinja2`, `oauth2`.
2. Obtain Twitter/X API credentials (Consumer Key/Secret, Access Token/Secret) at a tier that permits the endpoints you need, and configure them.
3. Run the CLI against the target `username`, selecting the modules you want (user info, geolocation, media, network, etc.).
4. Read the generated HTML report; export geolocations and media for follow-up.
5. Pivot: geolocated tweets → mapping/geo tools; media EXIF → `[[exiftool]]`-style analysis; associates → account-network expansion.

## Inputs → Outputs
- **In:** `username` (plus optional coordinates/keywords for geo/topic filters)
- **Out:** `geolocation` history, `social-profile` (activity, devices, hashtags), `associate` network, tweeted `image`s and their `metadata-exif`
- **Empty/negative result looks like:** API auth errors or empty modules — almost always an API-access/tier problem now, not that the account has no data.

## Gotchas & OpSec
- **Degraded by design changes:** Twitter's post-2022 API lockdown means the free tier can't run most modules; expect to need paid API access or the tool will largely fail.
- Media EXIF is frequently stripped by Twitter on upload — don't assume GPS survives.
- **OpSec (active):** collection is tied to your API keys; use throwaway developer credentials and pace requests to avoid rate-limit flags.

## Overlaps ("do both")
- Do both with browser-based X advanced-search tools (which need no API) for coverage when your API tier is limited, and with EXIF tools for any recovered media.

## Trust & verifiability
`trust: community` — a reputable, inspectable open-source project; treat outputs as reliable *if* it runs, but verify anything location-critical, since API limitations can silently truncate results.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tinfoleak-py |
| category | social-networks |
| selectorsIn → selectorsOut | username → geolocation, social-profile, associate, image, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key) |

---
id: bellingcat-tiktok-hashtag-analysis
name: Bellingcat TikTok Hashtag Analysis
description: Use when you have a hashtag tied to a person, event or place and want to archive the TikTok posts under it — returns downloaded videos/images plus post metadata and co-occurring-hashtag maps.
url: https://github.com/bellingcat/tiktok-hashtag-analysis
category: archives-cache
path:
- archives-cache
bestFor: Bulk-archiving TikTok posts under one or more hashtags and analysing which hashtags co-occur.
selectorsIn:
- name
- geolocation
selectorsOut:
- social-profile
- metadata-exif
- image
status: live
pricing: free
costNote: Free and open-source (MIT).
opsec: active
opsecNote: It scrapes TikTok via the unofficial TikTokApi package and yt-dlp and can require TikTok session credentials in its config; use a throwaway/sock-puppet TikTok account and a research IP, since bulk scraping can trigger TikTok anti-bot measures against whatever session you supply.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: trusted
trustNote: Published and maintained by Bellingcat, a reputable open-source investigations organisation.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
relatedTools:
- auto-archiver
- instagram-location-search
- shadow-finder
- telegram-phone-number-checker-github-com
- wayback-google-analytics
aliases:
- tiktok-hashtag-analysis
tags:
- bellingcat-toolkit
- archiving
- tiktok
source: bellingcat-toolkit
lastVerified: '2026-08-04'
enrichment: full
---

# Bellingcat TikTok Hashtag Analysis

> Bellingcat's CLI for pulling every TikTok post under a hashtag — videos, images and metadata — plus a co-occurring-hashtag frequency analysis.

## When to use
You have a hashtag connected to a subject, an event, or a location (a missing person's known tag, a local place tag, an event handle) and want to snapshot the TikTok content under it before it disappears, then see which other hashtags cluster with it to find related accounts and posts.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install tiktok-hashtag-analysis`.
2. Configure credentials if prompted: `tiktok-hashtag-analysis --config` (stores a TikTok session for scraping).
3. Scrape one or more tags: `tiktok-hashtag-analysis london paris newyork`.
4. Add `--download` to save `.mp4`/image files, `--plot` for visualisations, and `--table` for a co-occurring-hashtag frequency table.
5. Review `posts.json` for author handles and post metadata; pivot on the `social-profile` authors and co-occurring tags to widen the net.

## Inputs → Outputs
- **In:** one or more hashtags (derived from a `name`, `geolocation`, or event).
- **Out:** downloaded videos/images, `metadata-exif`-style post metadata (author, timestamps, captions) in `posts.json`, author `social-profile` handles, and co-hashtag frequency data.
- **Empty/negative result looks like:** an empty/near-empty `posts.json` — a rare/blocked tag, a bad session, or TikTok throttling; re-auth or try a broader tag.

## Gotchas & OpSec
- Human-in-the-loop: relies on the unofficial TikTokApi and can need a logged-in TikTok session — use a sock-puppet account, never your own.
- Scraping at volume is fragile: TikTok API changes and rate limits break runs; pin versions and expect maintenance.
- Downloaded media metadata reflects TikTok's re-encoding, not necessarily original capture data — don't over-read EXIF/geo from downloaded files.

## Overlaps ("do both")
- Part of the Bellingcat toolkit — pair with `[[auto-archiver]]` to preserve the posts you find in a durable archive, and `[[instagram-location-search]]` to cross-reference the same place/event on another platform.

## Trust & verifiability
`trust: trusted` — maintained by Bellingcat; the tooling is reputable, though the underlying data is scraped from TikTok and should be preserved (archived) as you collect it to keep it verifiable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bellingcat-tiktok-hashtag-analysis |
| category | archives-cache |
| selectorsIn → selectorsOut | name, geolocation → social-profile, metadata-exif, image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login) |

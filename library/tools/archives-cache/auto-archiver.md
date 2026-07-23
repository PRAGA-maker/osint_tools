---
id: auto-archiver
name: Auto Archiver
description: Use when you have a list of social-media/webpage URLs (a `social-profile`, video, or post) and want to preserve them in a verifiable way — returns local/cloud archives with hashes and metadata.
url: https://github.com/bellingcat/auto-archiver
category: archives-cache
path:
- archives-cache
bestFor: Bulk, tamper-evident archiving of social media posts, videos and images from a CSV or Google Sheet.
selectorsIn:
- social-profile
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (MIT). Self-hosted; you only pay for optional cloud storage (S3/Google Drive) or third-party enrichers you enable.
opsec: active
opsecNote: Archiving fetches each target URL, so requests originate from wherever you run it — the platform (and potentially the poster) can see a viewer/download hit. Run it from a non-attributable host/VPN and beware that some enrichers call external APIs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Maintained by Bellingcat, a leading open-source investigations org; widely used for evidence preservation with an active contributor community.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Bellingcat Auto Archiver
tags:
- archives-cache
- evidence-preservation
- social-media
- cli
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- bellingcat-tiktok-hashtag-analysis
- instagram-location-search
- shadow-finder
- telegram-phone-number-checker-github-com
- wayback-google-analytics
---

# Auto Archiver

> Bellingcat's evidence-grade archiver — feed it a spreadsheet of URLs and it captures each post/video/image with hashes and metadata so the archive stands up later.

## When to use
You have one or many URLs tied to a subject (a `social-profile`, a specific post, an image or video) and need to preserve them before they are deleted or edited — with a verifiable record (hashes, timestamps, screenshots) suitable for an investigation or legal context. Ideal for monitoring a Google Sheet of leads and auto-capturing new rows.

## How to use it (`bestInteractionPattern`: cli)
1. Install via pip or run the Docker image: see https://github.com/bellingcat/auto-archiver. Configure an orchestration YAML (feeders, archivers, enrichers, storage).
2. Point it at a feeder: CLI arg, a CSV, or a Google Sheet column of URLs.
3. Run it; each URL is archived (to local disk, S3, or Google Drive) with a hash and metadata, and status is written back to the CSV/Sheet.
4. Pivot: the preserved content (and extracted `metadata-exif`, thumbnails) feeds geolocation, facial, and reverse-image work; the hash gives you integrity for later use.

## Inputs → Outputs
- **In:** URL(s) / `social-profile` links (via CLI, CSV, or Google Sheet)
- **Out:** archived media + `metadata-exif`/hashes/screenshots in local or cloud storage, with a status report
- **Empty/negative result looks like:** a URL that fails to archive (private/deleted content, unsupported platform, or an auth-walled page) — logged as an error row rather than a capture.

## Gotchas & OpSec
- Archiving is active — it fetches the target URL, so use a non-attributable egress.
- Coverage depends on the enabled archiver modules; some platforms (heavily auth-walled) won't capture without cookies.
- Optional enrichers may call external services (e.g. Whisper, thumbnails) — review what you enable for data leakage.

## Overlaps ("do both")
- Complements one-off web archivers (`[[wayback-machine]]`) — use Wayback for a single quick save, Auto Archiver for bulk, verifiable, media-rich preservation at scale.

## Trust & verifiability
`trust: trusted` — a Bellingcat project purpose-built for verifiable archiving; open-source and auditable, and the hashing gives you provenance you can defend.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | auto-archiver |
| category | archives-cache |
| selectorsIn → selectorsOut | social-profile → metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |

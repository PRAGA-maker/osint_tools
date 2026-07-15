---
id: tweet-metadata
name: Tweet Metadata
description: Use when you have a tweet or a `social-profile`'s exported data and need to interpret the metadata fields forensically — returns field-level meaning for timestamps, source, and geo data.
url: https://www.wsj.com/public/resources/documents/TweetMetadata.pdf
category: social-networks
path:
- social-networks
- twitter
- analytics
bestFor: Reading and interpreting the metadata fields inside tweet/account JSON for forensic analysis.
selectorsIn:
- social-profile
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free reference document hosted by the Wall Street Journal.
opsec: passive
opsecNote: A documentation resource — reading it and analysing already-collected tweet data touches no live target and alerts no one.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A WSJ-published reference mapping tweet metadata fields; the field definitions mirror Twitter/X's documented object model, though the API/object schema has evolved since publication.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- WSJ Tweet Metadata reference
- tweet metadata fields
tags:
- twitter
- metadata
- forensics
source: arf-seed
lastVerified: '2026-07-15'
enrichment: full
---

# Tweet Metadata

> A reference document mapping the metadata fields embedded in a tweet — created-at, source (posting app/device), geo/place, user fields — so you can read a collected tweet's JSON forensically instead of guessing.

## When to use
You've captured a tweet or account export (via API, a scraper, or a legal-process return) and need to interpret the raw fields. A single tweet's metadata can reveal the **device/app** it was posted from (`source`), the **exact timestamp**, and sometimes **geo/place** — powerful for timelines and for corroborating a subject's location or which phone they use. This doc tells you what each field means.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the reference at https://www.wsj.com/public/resources/documents/TweetMetadata.pdf.
2. Match it against your collected tweet/account JSON field by field — pay attention to `created_at`, `source`, `coordinates`/`place`, and the nested `user` object.
3. Extract forensic signals: posting device, precise time (convert timezones carefully), and any geo data.
4. Pivot: a `source` device/app narrows the subject's tech; `place`/`coordinates` feed `geolocation`; account-creation and profile fields corroborate identity.

## Inputs → Outputs
- **In:** a tweet/account's exported metadata (you already have the `social-profile` data)
- **Out:** field-level interpretation → posting `metadata-exif`-style signals, `geolocation`, precise timestamps
- **Empty/negative result looks like:** many modern tweets carry no geo (geotagging is off by default), and X has removed/renamed fields over time — a missing field is common, not an error.

## Gotchas & OpSec
- **Schema drift**: Twitter→X changed and deprecated fields since this reference was written; treat it as a strong baseline, not gospel, and confirm against current X object docs.
- Geo fields are usually empty (users rarely geotag) — don't expect coordinates on most tweets.
- OpSec: **passive** — you're analysing data you already hold; nothing is queried live.

## Overlaps ("do both")
- Pairs with `[[twitter-com]]` (collect the media/posts) and archive tools — this turns the raw metadata behind those posts into interpretable forensic signal.

## Trust & verifiability
`trust: community` — a solid, widely-cited field reference, but published at a point in time; verify specific field names against X's current schema before drawing firm conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tweet-metadata |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → metadata-exif, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

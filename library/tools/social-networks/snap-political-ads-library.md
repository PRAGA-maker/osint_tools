---
id: snap-political-ads-library
name: Snap Political Ads Library
description: Use when you have an advertiser `name`/`employer-org` and want their Snapchat political-ad history — returns advertiser org, spend, reach and targeting.
url: https://www.snap.com/en-GB/political-ads
category: social-networks
path:
- social-networks
bestFor: Researching who paid for political/advocacy advertising on Snapchat and how the campaigns were targeted.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- name
status: live
pricing: free
costNote: Free public transparency archive; downloadable as annual CSV/ZIP files, no account or payment required.
opsec: passive
opsecNote: You download static archive files from Snap's servers; no query names a specific person and nothing is disclosed to the advertiser. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party transparency data published by Snap Inc. itself; authoritative for what it covers (paid political/advocacy ads only).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Snapchat Political Ads Library
- Snap Ads Transparency
tags:
- snapchat
- political-ads
- transparency
source: osintambition-social
lastVerified: '2026-07-22'
enrichment: full
---

# Snap Political Ads Library

> Snap's first-party transparency archive of every political and advocacy ad run on Snapchat, downloadable year-by-year as spreadsheets.

## When to use
You are profiling an organisation, campaign or individual advertiser (`name` / `employer-org`) and want to know whether they ran political or advocacy ads on Snapchat, how much they spent, how many people they reached, and how they targeted them (geography, age, gender, interests). Useful for influence-mapping and corroborating an entity's public-facing activity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.snap.com/en-GB/political-ads.
2. Download the archive ZIP for the year(s) of interest — the data is hosted as CSV files on Google Cloud Storage.
3. Open the CSV in a spreadsheet and filter by the `PayingAdvertiserName` / organisation column to find your subject.
4. Read the spend, impressions, dates and targeting columns for each matching ad.
5. Pivot: an advertiser org name feeds company-registry and people-search lookups; targeting fields corroborate geographic focus.

## Inputs → Outputs
- **In:** advertiser `name` or `employer-org` (searched within the CSV)
- **Out:** `employer-org` / paying-advertiser identity, spend, impressions, date range and targeting parameters
- **Empty/negative result looks like:** no matching row in the archive — the advertiser simply did not run political ads on Snapchat; it says nothing about their activity on other platforms.

## Gotchas & OpSec
- Covers only paid political/advocacy ads on Snapchat — not organic content and not other platforms.
- The archive is bulk CSV, not a search box: you filter locally, so expect to handle large files.
- OpSec: fully passive; no target is notified.

## Overlaps ("do both")
- Pairs with Meta and Google political-ad libraries and with company-registry tools to build a cross-platform picture of an advertiser's spend and identity.

## Trust & verifiability
`trust: trusted` — published directly by Snap Inc. as a legal transparency obligation; the figures are the platform's own records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | snap-political-ads-library |

---
id: twtdata-download-twitter-data
name: twtData (Download Twitter Data)
description: Use when you have a Twitter/X `username` and want its followers/following or tweets as a spreadsheet — returns CSV/XLSX exports of an account's network and posts for analysis.
url: https://www.twtdata.com/
category: social-networks
path:
- social-networks
bestFor: Exporting a Twitter/X account's followers/following or tweets to CSV/XLSX for network analysis.
selectorsIn:
- username
selectorsOut:
- username
- social-profile
status: live
pricing: freemium
costNote: A free sample export is available; full follower/following/tweet exports are paid (per-record pricing, roughly a few dollars minimum for small accounts). Delivered by email.
opsec: passive
opsecNote: Passive toward the subject — twtData pulls public Twitter/X data server-side; you don't interact with the account, and the target isn't notified. You must give twtData an email for delivery, so use a research/sock-puppet address; treat the exported list as sensitive personal data and handle it lawfully.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party commercial data-export service; results reflect what it can pull from X at export time (subject to X's API limits/changes), so completeness and freshness vary.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Download Twitter Data
- twtdata.com
tags:
- twitter
- export
- csv
source: osintambition-social
lastVerified: '2026-07-23'
enrichment: full
---

# twtData (Download Twitter Data)

> A commercial exporter that turns a Twitter/X account's followers, following, or tweets into a downloadable CSV/XLSX — for network mapping and content analysis without scraping it yourself.

## When to use
You have a Twitter/X `username` and want its social graph or post history as structured data — to map who follows whom, find overlap between two accounts' audiences, or analyse tweet content in bulk. Reach for twtData when a spreadsheet of followers/following/tweets would save you hours of manual collection, and X's own export/API isn't an option. It handles the pull server-side and emails you the file.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.twtdata.com/ and enter the target X `username`.
2. Choose the dataset (followers, following, tweets, list members) and format (CSV/XLSX), and provide a delivery email (use a research address).
3. Use the free sample to sanity-check the data before paying for a full export; small accounts export quickly.
4. Receive the file by email and load it into your analysis tool.
5. Pivot: the follower/following `username`s and `social-profile` links become new leads — cross-account overlap and mutuals are especially useful for mapping a network.

## Inputs → Outputs
- **In:** a Twitter/X `username`
- **Out:** CSV/XLSX of that account's followers/following or tweets — lists of `username`s and `social-profile` links
- **Empty/negative result looks like:** a private/suspended account, or a very large account where X's limits truncate the pull — the export may be partial or unavailable; the sample will reveal this before you pay.

## Gotchas & OpSec
- Human-in-the-loop / payment-wall: only a sample is free; full exports are paid per record.
- Completeness depends on X's ever-changing API/limits at export time — big accounts may come back incomplete; verify counts against the profile.
- OpSec: passive toward the target, but you hand twtData an email and receive personal data — use a sock-puppet address and handle the list responsibly/lawfully.

## Overlaps ("do both")
- Pairs with follower/network-analysis tools and general X-OSINT — twtData *gets* the graph as data, those *analyse* it. Cross-check a sample against the live profile to gauge freshness before relying on a paid export.

## Trust & verifiability
`trust: unverified` — a commercial third-party exporter; the data is a lead set whose completeness varies with X's limits, so verify follower counts and spot-check entries against the live account.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twtdata-download-twitter-data |
| category | social-networks |
| selectorsIn → selectorsOut | username → username, social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |

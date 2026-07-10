---
id: metatube-com
name: MetaTube
description: Use when you have a `name`/`username` or keyword and want to find videos about a subject aggregated from across platforms — returns social-profile links and video metadata.
url: https://www.metatube.com/
category: image-video-face
path:
- image-video-face
bestFor: Keyword/name search across aggregated third-party video content to surface clips featuring or posted by a subject.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free to browse and search; no account required.
opsec: passive
opsecNote: Read-only browsing of an aggregator; you never contact the subject or the original poster, so nothing is disclosed to them. Standard web-server logging applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Independent third-party video-aggregation site with no editorial vetting; it re-hosts/links content from other platforms, so provenance of any clip must be checked at the original source.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- metatube
- metatube.com
tags:
- videosites
- Video Related Sites
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# MetaTube

> A video-aggregation site that curates and organises clips from across the web by category and keyword — a secondary search surface for finding video of or by a subject.

## When to use
You want to find video content connected to a subject and mainstream searches (YouTube, TikTok directly) haven't surfaced it, or you want a single keyword search across aggregated sources. Search by `name`, a reused `username`/channel term, or a topic, and look for clips that feature the subject or link back to their posting `social-profile`. This is a discovery/aggregation tool, not a face-recognition engine — despite its media category, it does not match faces; it matches text and tags.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.metatube.com/ and use the search box / category tags.
2. Enter the subject's `name`, channel `username`, or a distinctive keyword.
3. Scan results (thumbnails, titles, dates) for clips featuring or posted by the subject.
4. Open a promising result and follow it to the **original source platform** to confirm the poster and context.
5. Extract the source link/handle (`social-profile`) and posting details (`metadata`: title, date); pivot the source channel into platform-native OSINT.

## Inputs → Outputs
- **In:** `name`, `username`, or keyword
- **Out:** `social-profile` (link back to the original channel/poster), `metadata` (video title, date, source)
- **Empty/negative result looks like:** no relevant clips, or only unrelated trending videos — MetaTube's index is partial and skews toward popular/trending content, so absence proves nothing.

## Gotchas & OpSec
- It is an aggregator: always follow through to the original platform to verify who posted a clip and when — don't treat the MetaTube listing as the source of truth.
- Index is shallow and trend-driven; niche or private content won't appear.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with direct platform searches (YouTube/TikTok) and reverse-image/video tools — MetaTube may surface a clip you then verify and expand on the native platform.

## Trust & verifiability
`trust: unverified` — an anonymous third-party aggregator with no vetting; use it only as a lead generator and confirm every clip at its original source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | metatube-com |
| category | image-video-face |
| selectorsIn → selectorsOut | name, username → social-profile, username |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

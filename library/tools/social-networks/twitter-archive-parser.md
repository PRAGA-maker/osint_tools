---
id: twitter-archive-parser
name: Twitter Archive Parser
description: Use when you have a downloaded Twitter/X account archive and want it turned into readable, media-embedded tweets plus follower lists — returns a `social-profile`'s tweets, media (`metadata-exif`) and `associate` connections.
url: https://github.com/timhutton/twitter-archive-parser
category: social-networks
path:
- social-networks
bestFor: Converting a raw Twitter/X data-export .zip into browsable Markdown/HTML with embedded media, un-shortened links, and exported follower/following lists.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
- associate
- metadata-exif
status: live
pricing: free
costNote: Free and open source (GPL-3.0). Only cost is having the account's own archive export and Python installed locally.
opsec: passive
opsecNote: Runs entirely offline on an archive you already possess; it makes no network calls to Twitter (aside from optionally resolving missing handles). Nothing is sent to the target. Passive by construction.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source project (Tim Hutton, ~2.4k GitHub stars); code is auditable and 100% Python.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- twitter-archive-parser
aliases:
- twitter-archive-parser
- Twitter/X archive parser
tags:
- Social Media
- Twitter
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# Twitter Archive Parser

> A Python script that turns Twitter/X's clunky data-export .zip into clean, media-rich, readable Markdown/HTML — plus a dump of the account's follower and following lists.

## When to use
You (or a cooperating account owner, e.g. a missing person's family with access to their credentials) have downloaded the Twitter/X archive .zip and want it in a usable form: every tweet with images/videos embedded inline, t.co links restored to their real URLs, and the full follower/following lists exported as leads (`associate`). Ideal when the live account is suspended, deleted, or you simply want an offline, searchable copy.

## How to use it (`bestInteractionPattern`: cli)
1. Have the account owner download their archive from X settings ("Download an archive of your data") — this step needs their login (`account-login`).
2. Unzip the downloaded folder.
3. Download `parser.py` from https://github.com/timhutton/twitter-archive-parser and save it into that unzipped folder.
4. Open a terminal in the folder and run: `python parser.py` (it can auto-install the optional `requests` and `imagesize` helpers).
5. Read the output: Markdown/HTML files of all tweets with embedded media and de-obfuscated links, copied media in an output folder, and follower/following list files.
6. Pivot: mine the follower/following exports for `associate` leads and the media for `metadata-exif`; feed usernames into other social-network lookups.

## Inputs → Outputs
- **In:** `social-profile` (a Twitter/X archive .zip for the account)
- **Out:** `social-profile` (readable tweet history), `associate` (follower/following lists), `metadata-exif` (extracted media files)
- **Empty/negative result looks like:** an incomplete or corrupted archive produces missing media or empty output folders — re-download the full archive.

## Gotchas & OpSec
- **You must already have the archive.** This does NOT scrape someone else's account; it only reformats an export you legitimately possess (getting that export requires the account's login).
- Twitter's own export omits some data (e.g. certain DMs/handles); the parser retrieves some missing handles but cannot invent data the export never contained.
- OpSec: fully offline/passive; safe to run without alerting anyone.

## Overlaps ("do both")
- Complements live-account tools: use this for a possessed archive, and username-based social lookups when you only have the handle and no export.

## Trust & verifiability
`trust: community` — a well-starred, auditable open-source project. Output fidelity is bounded by what Twitter/X included in the archive, not by the tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitter-archive-parser |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → social-profile, associate, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (account-login) |

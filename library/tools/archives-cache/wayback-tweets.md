---
id: wayback-tweets
name: Wayback Tweets
description: Use when you have a Twitter/X `username` and want their deleted or historical tweets — returns archived tweet captures pulled from the Wayback Machine.
url: https://waybacktweets.streamlit.app/
category: archives-cache
path:
- archives-cache
bestFor: Recovering deleted or historical tweets for an account from Internet Archive captures.
selectorsIn:
- username
selectorsOut:
- social-profile
- geolocation
- associate
status: live
pricing: free
costNote: Free open-source app (by Claromes); queries the Internet Archive's free CDX/Wayback API.
opsec: passive
opsecNote: Pulls captures from archive.org, not from Twitter/X, so the account owner isn't notified and X doesn't see the query. Passive. Your IP is visible only to the Internet Archive.
humanInLoop: false
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source tool (github.com/claromes/waybacktweets) that surfaces Wayback Machine captures; the tweets shown are archive.org snapshots, so authoritative as archived (subject to what was captured).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- wayback-machine
- waybackpy
- tweeterid
aliases:
- waybacktweets
- Wayback Tweets
tags:
- twitter
- archive
- wayback
- deleted-tweets
source: osintambition-social
lastVerified: '2026-07-17'
enrichment: full
---

# Wayback Tweets

> An open-source app that pulls a Twitter/X account's archived tweets from the Wayback Machine — a way to recover deleted or historical posts now that X's own search is locked down.

## When to use
You have a subject's Twitter/X `username` and need tweets that are deleted, from a suspended account, or predate what X will show you. Since X's API/search became largely inaccessible, the Internet Archive is one of the few ways to recover old tweets. Wayback Tweets queries archive.org for captures of that handle's tweet URLs and displays what was archived — useful for recovering statements, locations mentioned, and named contacts from a since-scrubbed timeline.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://waybacktweets.streamlit.app/ (or self-host from github.com/claromes/waybacktweets).
2. Enter the Twitter/X username (without @) and set options (date range, limits).
3. It returns archived captures of that account's tweets — view them, and note which are no longer on the live account (i.e. deleted).
4. Be patient: it hits the Internet Archive's API and can be slow or rate-limited on prolific accounts.
5. Pivot: recovered content → places/handles/people mentioned feed geolocation and associate work; a specific archived tweet URL → open the full capture in `[[wayback-machine]]`.

## Inputs → Outputs
- **In:** a Twitter/X `username`
- **Out:** archived tweet captures (text/media snapshots) → `social-profile` history, `geolocation`/`associate` leads
- **Empty/negative result looks like:** few/no captures — the account or its tweets were never archived by the Wayback Machine (most tweets aren't unless someone triggered a capture); absence ≠ the tweets never existed.

## Gotchas & OpSec
- Coverage depends entirely on what the Internet Archive happened to capture — many tweets were never archived, so results are partial and patchy.
- The hosted Streamlit app can be asleep/slow or rate-limited; self-host for heavy use.
- Archived media may be missing even when text was captured.
- Passive — routes through archive.org, so X and the account owner get no signal.

## Overlaps ("do both")
- Pairs with `[[wayback-machine]]` — Wayback Tweets is a tweet-focused front-end; the Wayback Machine directly gives the full capture list for a profile URL. Use it to dig deeper on a specific capture.
- Pairs with `[[waybackpy]]` to script bulk retrieval of a handle's archived URLs.

## Trust & verifiability
`trust: community` — an open-source tool, but it only surfaces Internet Archive captures, which are authoritative snapshots. Verify a critical tweet by opening its underlying Wayback capture directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wayback-tweets |
| category | archives-cache |
| selectorsIn → selectorsOut | username → social-profile, geolocation, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

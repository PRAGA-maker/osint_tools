---
id: twdown-net
name: twdown.net
description: Use when you have a `social-profile` (a tweet/X post URL) and want to archive its video before deletion — returns the downloaded video/`image` and its `metadata-exif`.
url: https://twdown.net/
category: social-networks
path:
- social-networks
bestFor: Free, no-login download of Twitter/X videos (and MP3 audio) from a tweet URL.
selectorsIn:
- social-profile
selectorsOut:
- image
- metadata-exif
status: live
pricing: free
costNote: Completely free, no registration, no stated download limit; ad-supported.
opsec: passive
opsecNote: You paste a public tweet URL; twdown's server fetches the media, so the target isn't notified and never sees your IP. twdown's servers (and their ad networks) see the URL you submit and set trackers — use a hardened/sock-puppet browser and an ad blocker. Never submit private/authenticated post URLs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A functional but anonymous, ad-heavy third-party downloader; it works, but there's no accountable operator, so verify the media against the live tweet.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- twdown
- twdown.net
tags:
- xtwitter
- X / Twitter Related Sites
- media-archival
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# twdown.net

> A free, no-login web tool that pulls the video (or MP3 audio) out of any public tweet/X post so you can archive it before the poster deletes it.

## When to use
You have a `social-profile` reference — specifically a public tweet/X post URL containing video — and you need a durable local copy for evidence before it's removed. Preserve footage showing a missing person, a vehicle, a location, or an event, along with any surviving `metadata-exif`. It's an archival step, not a search tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. On X/Twitter, copy the URL of the post containing the video (e.g. `https://twitter.com/user/status/…`).
2. Go to https://twdown.net/ (use an ad blocker; the site is ad-heavy).
3. Paste the URL and submit; twdown returns direct download links in several qualities, plus an MP3 option.
4. Save the highest-quality file locally, then run it through an EXIF/metadata viewer for any residual `metadata-exif`.
5. Pivot: feed a still frame into `[[tracepoint]]` for scene geolocation, or a face into reverse-image/face tools.

## Inputs → Outputs
- **In:** `social-profile` (a public tweet/X post URL)
- **Out:** downloaded video/`image` file (+ MP3), any residual `metadata-exif`
- **Empty/negative result looks like:** "invalid URL" / no media — the post is protected, deleted, text-only, or the URL wasn't a status link. X strips most upload EXIF, so expect little embedded metadata.

## Gotchas & OpSec
- Human-in-the-loop: none, but the ad-heavy interface has deceptive "download" buttons — click carefully.
- OpSec: **passive** to the target (server-side fetch); twdown and its ad networks log your submitted URL and set trackers. Use a hardened browser + ad blocker.
- Third-party proxy: always compare the archived file to the live tweet before treating it as authoritative.

## Overlaps ("do both")
- Same archival role as `[[publer-io-3]]` (Threads) — use the right downloader per platform, then `[[tracepoint]]` to geolocate a frame.

## Trust & verifiability
`trust: unverified` — it works but is an anonymous, ad-supported operator with no accountability. Verify every archived clip against the original post.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twdown-net |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → image, metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

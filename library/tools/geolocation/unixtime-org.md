---
id: unixtime-org
name: unixtime.org
description: Use when you have a Unix/epoch timestamp from `metadata-exif`, logs, or filenames and want the human date/time — returns the converted calendar date.
url: https://unixtime.org/
category: geolocation
path:
- geolocation
bestFor: Converting Unix/epoch timestamps (seconds or milliseconds) found in metadata, logs, or URLs into human-readable dates, and back.
selectorsIn:
- metadata-exif
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free, no account, no ads-of-consequence; runs entirely in the browser.
opsec: passive
opsecNote: A pure client-side date-math utility; the timestamp you enter is not tied to any subject and nothing is queried about a target. No footprint at all.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A simple, long-running epoch-conversion utility (© 2011–2026); the arithmetic is deterministic and trivially verifiable, so trust rests on correct timezone handling by the user.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Unix timestamp converter
- epoch converter
tags:
- timezones
- Time Zones & Converters
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# unixtime.org

> A no-friction epoch↔date converter: turn a raw Unix timestamp pulled from EXIF, a log line, a cookie, or a filename into a human date, and vice versa.

## When to use
You've extracted a Unix/epoch timestamp — a 10-digit (seconds) or 13-digit (milliseconds) number — from image `metadata-exif`, an app database, a server log, a URL parameter, or a filename, and you need the actual calendar date/time to place an event on a timeline. Also useful in reverse: convert a known date to an epoch value so you can grep or filter coded datasets.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://unixtime.org/.
2. Paste the epoch number to get the human date, or enter a date to get the epoch value.
3. Note whether the source uses seconds vs milliseconds (drop the last 3 digits for ms→s) and confirm the timezone — the tool shows UTC and local; timeline errors usually come from timezone confusion.
4. Pivot: the resolved date anchors the artifact in your event timeline and cross-references with other dated evidence.

## Inputs → Outputs
- **In:** `metadata-exif` (a Unix/epoch timestamp) — or a human date
- **Out:** the converted human date/time (or epoch value)
- **Empty/negative result looks like:** a nonsensical date (e.g. 1970 or far-future) — usually means you fed milliseconds as seconds, or the number wasn't actually an epoch timestamp.

## Gotchas & OpSec
- Seconds vs milliseconds is the classic trap — a 13-digit value is almost always milliseconds; divide by 1000.
- Always pin the timezone before using a converted time in a timeline; the raw epoch is UTC.
- OpSec: passive, offline-equivalent math; zero footprint.

## Overlaps ("do both")
- Complements EXIF/metadata extractors — those pull the raw timestamp, this converts it to a usable date.

## Trust & verifiability
`trust: community` — deterministic date arithmetic that you can re-verify with any other converter or `date -d @<epoch>`; effectively self-checking.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | unixtime-org |
| category | geolocation |
| selectorsIn → selectorsOut | metadata-exif → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

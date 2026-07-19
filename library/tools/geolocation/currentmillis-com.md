---
id: currentmillis-com
name: currentmillis.com
description: Use when you have a raw Unix/epoch timestamp (`metadata-exif`) from a URL, log, cookie or export and want the real UTC/local date-time — returns human-readable timestamps and format conversions.
url: https://currentmillis.com/
category: geolocation
path:
- geolocation
bestFor: Converting epoch-millisecond and other machine timestamps to human-readable UTC/local date-time.
selectorsIn:
- metadata-exif
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free; no account, no payment, runs client-side in the browser.
opsec: passive
opsecNote: Conversion happens in your browser — the timestamp you type is not sent to a subject and reveals nothing about your target. Fully passive; no special hygiene beyond not pasting sensitive full strings you don't want cached.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-standing, single-purpose utility with transparent client-side conversion; the arithmetic is verifiable and deterministic.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- currentmillis
- epoch converter
tags:
- timezones
- Time Zones & Converters
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# currentmillis.com

> A no-frills epoch/timestamp converter: paste a Unix-milliseconds value and get the real UTC and local date-time, plus ISO 8601, GPS and other formats.

## When to use
You've pulled a machine timestamp out of an artifact — a `metadata-exif` field, a URL parameter (`?t=1712345678901`), a cookie, a JSON/API response, a database export — and need the actual date and time it encodes. Converting timestamps is a routine step in building a timeline from digital evidence.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://currentmillis.com/.
2. Paste the epoch value into the milliseconds (or seconds) box; it instantly shows the corresponding UTC and local date-time.
3. Use the bi-directional fields to go the other way (date → millis) or to convert into ISO 8601, Julian, GPS or HTTP formats.
4. Mind the unit: 10-digit values are usually seconds, 13-digit are milliseconds — pick the right box or you'll be off by 1000×.
5. Pivot: the resolved timestamp anchors the artifact on your case timeline and can be cross-checked against `metadata-exif` capture times or post dates.

## Inputs → Outputs
- **In:** a raw epoch/machine timestamp (`metadata-exif`)
- **Out:** human-readable UTC + local date-time and alternate time formats (a normalized `metadata-exif` value)
- **Empty/negative result looks like:** an implausible date (e.g. 1970 or year 55000) — a sign you used the wrong unit (seconds vs milliseconds) or the value wasn't a Unix epoch at all.

## Gotchas & OpSec
- Seconds-vs-milliseconds is the classic error; sanity-check that the resulting date is plausible.
- Local-time output depends on *your* machine's timezone — record results in UTC to avoid ambiguity in evidence.
- OpSec: fully passive and client-side; nothing leaves your browser meaningfully and no subject is involved.

## Overlaps ("do both")
- Pairs with EXIF/metadata viewers and any timezone converter — those extract the raw timestamp; currentmillis turns it into a dated, timezone-explicit moment for the timeline.

## Trust & verifiability
`trust: trusted` — a transparent, single-purpose converter; the conversion is deterministic math you can verify with any second epoch tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | currentmillis-com |
| category | geolocation |
| selectorsIn → selectorsOut | metadata-exif → metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

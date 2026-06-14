---
id: gaijin-at
name: gaijin.at
description: Use when you have raw email headers and want them parsed into the mail path, originating IP, and timestamps (German/English tools site).
url: https://www.gaijin.at/de/tools/e-mail-header-analyzer
category: email
path:
- email
bestFor: Parsing raw email headers into a readable relay path with originating IP and timestamps.
selectorsIn:
- metadata-exif
- email
selectorsOut:
- ip-address
- metadata-exif
status: live
pricing: free
costNote: Free browser tool; gaijin.at hosts many free network/admin utilities.
opsec: passive
opsecNote: Headers are pasted into a third-party site; the message metadata (addresses, subject, IPs) is sent to gaijin.at.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: gaijin.at is a long-standing German freeware/utilities site; the header analyzer deterministically parses headers you supply, so output is verifiable against the source.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- emailheaders
- Email Header Related Sites
relatedTools:
- forensicosint-com
- google-analyzeheader
source: uk-osint
lastVerified: ''
enrichment: full
---

# gaijin.at — E-Mail Header Analyzer

> A free header analyzer (German/English) that turns a raw email's headers into a readable trace of its path, origin IP, and timestamps.

## When to use
You hold the raw headers of a received email and want the `Received:` chain, originating `ip-address`, and timestamps parsed out — same job as other header analyzers, useful as a cross-check when one parser chokes on malformed headers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Copy the full raw header block from the source email ("Show original" / "View source").
2. Go to the URL (the German UI also has English equivalents) and paste the headers.
3. Read the parsed relay path, originating IP, server hostnames, and timestamps.
4. Pivot: geolocate the originating `ip-address`; cross-check the parse against `[[google-analyzeheader]]` or `[[forensicosint-com]]`.

## Inputs → Outputs
- **In:** raw email headers (`metadata-exif`-style message metadata)
- **Out:** relay path, originating `ip-address`, timestamps, server names
- **Empty/negative result looks like:** only provider relays resolve and the client IP is absent — typical when the sender used webmail (Gmail/Outlook strip the client IP).

## Gotchas & OpSec
- UI is primarily German; the function is straightforward (paste → parse).
- As with all header parsing, webmail hides the sender's real client IP; headers can also be forged — weigh SPF/DKIM/DMARC over the visible `From:`.
- OpSec: passive, but headers (with addresses/subject) are disclosed to the site.

## Overlaps ("do both")
- Use alongside `[[forensicosint-com]]` and `[[google-analyzeheader]]`; different parsers occasionally surface different hops.

## Trust & verifiability
`trust: community` — established freeware utilities site; the analyzer's output is a deterministic parse you can verify against the raw headers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gaijin-at |
| category | email |
| selectorsIn → selectorsOut | metadata-exif, email → ip-address, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

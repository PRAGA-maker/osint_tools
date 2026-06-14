---
id: google-analyzeheader
name: Google AnalyzeHeader
description: Use when you have raw email headers and want Google's own tool to parse the delivery path, hop delays, and authentication results.
url: https://toolbox.googleapps.com/apps/messageheader/analyzeheader
category: email
path:
- email
bestFor: Parsing raw email headers into a clean delivery timeline with per-hop delays and SPF/DKIM/DMARC results.
selectorsIn:
- metadata-exif
- email
selectorsOut:
- ip-address
- metadata-exif
status: live
pricing: free
costNote: Free first-party Google tool (Google Admin Toolbox / Messageheader).
opsec: passive
opsecNote: Headers are pasted into Google's web tool. The subject is not contacted, but the message metadata (addresses, subject, IPs) is sent to Google.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Google Admin Toolbox utility ("Messageheader"); a reliable, deterministic header parser whose output you can verify against the raw headers.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Messageheader
- Google Admin Toolbox Messageheader
tags:
- email
relatedTools:
- forensicosint-com
- gaijin-at
- gmail
source: metaosint
lastVerified: ''
enrichment: full
---

# Google AnalyzeHeader (Messageheader)

> Google's first-party header parser — turns raw email headers into a delivery timeline with per-hop delays and authentication verdicts.

## When to use
You have the raw headers of a received email and want a trustworthy, vendor-neutral parse: the `Received:` chain rendered as a timeline (so you can spot suspicious hop delays), the originating `ip-address`, and SPF/DKIM/DMARC results to judge whether the message is authentic or spoofed.

## How to use it (`bestInteractionPattern`: web-manual)
1. In the source client, open the original message and copy the full header block (in Gmail: "Show original").
2. Go to the URL and paste the headers.
3. Read the output: a hop-by-hop timeline with delays, sending server IPs/hostnames, and SPF/DKIM/DMARC status.
4. Pivot: take the originating `ip-address` into IP geolocation; if SPF/DKIM fail, treat the `From:` as untrusted.

## Inputs → Outputs
- **In:** raw email headers (`metadata-exif`-style message metadata)
- **Out:** delivery timeline, per-hop delays, originating `ip-address`, SPF/DKIM/DMARC verdicts
- **Empty/negative result looks like:** earliest resolvable hop is the sender's webmail provider (client IP stripped), or auth fields show "none" because the sending domain published no SPF/DKIM.

## Gotchas & OpSec
- Webmail providers hide the sender's client IP, so the first IP you see may be the provider, not the person.
- Trust the cryptographic auth (DKIM) results over the visible `From:` — headers are trivially forgeable.
- OpSec: passive, but you are sending full headers (with addresses/subject) to Google.

## Overlaps ("do both")
- Cross-check with `[[forensicosint-com]]` and `[[gaijin-at]]`; pair with `[[gmail]]`, the most common source of the headers you paste here.

## Trust & verifiability
`trust: trusted` — first-party Google utility; deterministic parsing you can verify line-by-line against the raw headers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-analyzeheader |
| category | email |
| selectorsIn → selectorsOut | metadata-exif, email → ip-address, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

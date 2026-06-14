---
id: mxtoolbox-com-2
name: mxtoolbox.com
description: Use when you have the raw headers of an email to/from a subject and want to trace the delivery path and originating IP — returns the hop-by-hop route and source IP/geo.
url: http://www.mxtoolbox.com/emailheaders.aspx
category: email
path:
- email
bestFor: Parsing raw email headers to extract the originating IP and relay path.
selectorsIn:
- email
- metadata-exif
selectorsOut:
- ip-address
- geolocation
- metadata-exif
status: live
pricing: free
costNote: Free header-analyzer page; broader MxToolbox features/monitoring are paid.
opsec: passive
opsecNote: Fully passive — header parsing happens server-side at MxToolbox on text you paste; no contact is made with the target or their mail server. Be aware MxToolbox receives the headers you submit, which may contain personal data.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: MxToolbox is a reputable, widely used email/DNS diagnostics service; the Email Header Analyzer is a standard, well-documented feature.
missingPersonsRelevance: high
coverage: []
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- mxtoolbox
aliases:
- MxToolbox Email Header Analyzer
tags:
- emailheaders
- Email Header Related Sites
source: uk-osint
lastVerified: ''
enrichment: full
---

# mxtoolbox.com (Email Header Analyzer)

> The MxToolbox Email Header Analyzer — paste raw headers and it reconstructs the relay path and surfaces the originating IP.

## When to use
You have an actual email message connected to a missing-persons case (a message the subject sent, or one a tipster received from them) and can access its **raw headers**. Tracing them can reveal the originating `ip-address` and an approximate `geolocation` — strong leads on where a message was sent from.

## How to use it (`bestInteractionPattern`: web-manual)
1. In the source mail client, open the original/raw message and copy the full headers.
2. Go to mxtoolbox.com/emailheaders.aspx and paste them.
3. Read the parsed output: the ordered Received hops, the earliest originating IP, timestamps, and auth (SPF/DKIM) results.
4. Pivot: take the originating `ip-address` to an IP-geolocation/ISP lookup; cross-check timestamps against the case timeline.

## Inputs → Outputs
- **In:** raw email headers (`metadata-exif`) tied to an `email`
- **Out:** `ip-address` (originating), `geolocation` (approximate), relay/timestamp metadata (`metadata-exif`)
- **Empty/negative result looks like:** only the provider's egress IP visible (common for Gmail/Outlook webmail, which strip the client IP). That tells you the provider, not the device location.

## Gotchas & OpSec
- Major webmail providers hide the sender's real client IP; you often only get the provider's relay — manage expectations.
- The earliest "Received" hop can be forged in spam/spoofed mail; verify SPF/DKIM before trusting it.
- You are uploading message headers to a third party; redact unrelated personal data if policy requires.

## Trust & verifiability
`trust: trusted` — reputable MxToolbox feature with transparent, well-understood header-parsing behavior. The investigative value depends on whether the provider exposed the originating IP.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mxtoolbox-com-2 |
| category | email |
| selectorsIn → selectorsOut | email, metadata-exif → ip-address, geolocation, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |

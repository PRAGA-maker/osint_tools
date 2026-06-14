---
id: forensicosint-com
name: forensicosint.com
description: Use when you have the raw headers of an email and need to trace its originating IP, mail path, and authentication results.
url: https://www.forensicosint.com/free-tools/email-header-analyzer
category: email
path:
- email
bestFor: Parsing raw email headers to find originating IP, relay path, and SPF/DKIM/DMARC results.
selectorsIn:
- metadata-exif
- email
selectorsOut:
- ip-address
- metadata-exif
status: live
pricing: free
costNote: Free web tool; the parent site also sells paid OSINT services.
opsec: passive
opsecNote: Header text is pasted into a third-party site. Strip nothing of evidentiary value, but be aware the headers (and any PII inside them) are sent to the vendor.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Free header-analyzer from ForensicOSINT, a known OSINT-services vendor; output is a parse of headers you already hold, so accuracy is verifiable against the raw source.
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
- google-analyzeheader
- gaijin-at
source: uk-osint
lastVerified: ''
enrichment: full
---

# forensicosint.com — Email Header Analyzer

> Free web tool that parses raw email headers into a readable trace of the message's path, origin IP, and authentication results.

## When to use
You have received an email (a tip, a ransom/contact message, correspondence from a missing person) and can copy its full raw headers. You want to extract the originating `ip-address`, the relay hops, timestamps, and SPF/DKIM/DMARC verdicts to assess authenticity and geolocate the sender.

## How to use it (`bestInteractionPattern`: web-manual)
1. In the source email client, open the original/raw message and copy the full header block ("Show original" in Gmail, "View source" in others).
2. Go to the URL and paste the headers into the analyzer.
3. Read the parsed output: `Received:` chain, originating IP, sending mail servers, and auth (SPF/DKIM/DMARC) results.
4. Pivot: feed the originating `ip-address` into an IP-geolocation / reverse-IP tool; cross-check the parse with `[[google-analyzeheader]]`.

## Inputs → Outputs
- **In:** raw email headers (`metadata-exif`-style message metadata)
- **Out:** originating `ip-address`, relay path, timestamps, auth results
- **Empty/negative result looks like:** only the recipient-side relays resolve (originating IP hidden behind the provider, e.g. Gmail strips client IP) — common for webmail senders.

## Gotchas & OpSec
- Major webmail providers (Gmail, Outlook.com) hide the sender's client IP, so the earliest IP you see may be the provider, not the person.
- Headers can be forged; trust the auth (SPF/DKIM/DMARC) results over the raw `From:`.
- OpSec: passive, but you are pasting full headers (which contain addresses and subjects) into a third-party site.

## Overlaps ("do both")
- Cross-check with `[[google-analyzeheader]]` and `[[gaijin-at]]` — different parsers occasionally surface different hops or flag malformed headers.

## Trust & verifiability
`trust: community` — vendor-provided free tool; its output is a deterministic parse of headers you supply, so you can verify every claim against the raw text.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | forensicosint-com |
| category | email |
| selectorsIn → selectorsOut | metadata-exif, email → ip-address, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: email-header-analyzer
name: Email Header Analyzer
description: Use when you have raw email headers and want to trace delivery and authentication — returns the relay hops, originating IP, delay times, and SPF/DKIM results.
url: https://mxtoolbox.com/EmailHeaders.aspx
category: email
path:
- email
bestFor: Parsing raw email headers into a readable delivery path with hop delays and SPF/DKIM/DMARC results.
selectorsIn:
- metadata
selectorsOut:
- ip-address
- domain
- metadata
status: live
pricing: freemium
costNote: Free header analysis on MXToolbox; deeper monitoring/diagnostics and the API are paid.
opsec: passive
opsecNote: Parsing runs on headers you paste; the sender is not contacted. You are pasting message headers into MXToolbox, so avoid sensitive content.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: MXToolbox is an industry-standard mail/DNS diagnostics provider; the header parser is reliable, but origin tracing is limited by what the headers expose.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- MXToolbox Email Headers
tags:
- emailheaders
- email
source: osint4all
lastVerified: ''
enrichment: full
---

# Email Header Analyzer

> MXToolbox's email header analyzer: paste raw headers and get a clean delivery timeline, originating IP, and SPF/DKIM/DMARC verdicts.

## When to use
You have the full raw headers of an email tied to a person of interest and want to trace where it originated and whether it was spoofed. The originating `ip-address` and sending `domain` are pivots (geolocate, WHOIS, compare across messages), and the authentication results help judge whether the From address is forged.

## How to use it (`bestInteractionPattern`: web-manual)
1. In the source mail client, "Show original" / "View source" and copy the full raw headers.
2. Go to https://mxtoolbox.com/EmailHeaders.aspx.
3. Paste the headers and submit.
4. Read the hop-by-hop timeline (with per-hop delays), the originating IP, and SPF/DKIM/DMARC pass/fail.
5. Pivot: send the originating `ip-address` to IP geolocation/WHOIS and the sending `domain` to `[[email-dossier]]`.

## Inputs → Outputs
- **In:** raw email headers (`metadata`)
- **Out:** relay `ip-address`es, sending `domain`, hop delays + SPF/DKIM/DMARC results (`metadata`)
- **Empty/negative result looks like:** only the recipient provider's servers appear, or chains are stripped/forged. Major webmail (Gmail/Outlook) masks the sender's client IP, so origin tracing dead-ends at their servers.

## Gotchas & OpSec
- Human-in-the-loop: none for the free analyzer.
- OpSec: passive toward the sender, but you are pasting headers into a third party — don't use for sensitive material; use a local parser if so.
- Authentication "pass" only validates the path, not the human; webmail masks client IPs.

## Overlaps ("do both")
- Pairs with `[[dnschecker-org]]` — run both parsers on the same headers and compare; they surface forged/nested `Received:` lines differently.

## Trust & verifiability
`trust: community` — industry-standard diagnostics vendor; parsing is dependable, with the usual limits of header-based origin tracing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | email-header-analyzer |
| category | email |
| selectorsIn → selectorsOut | metadata → ip-address, domain, metadata |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: dnschecker-org
name: dnschecker.org
description: Use when you have raw email headers and want to trace the sending path — returns originating IP, mail-server hops, and timestamps.
url: https://dnschecker.org/email-header-analyzer.php
category: email
path:
- email
bestFor: Parsing raw email headers to extract the originating IP and the chain of relay servers.
selectorsIn:
- metadata
selectorsOut:
- ip-address
- domain
- metadata
status: live
pricing: free
costNote: Free web tool; DNS Checker monetizes with ads, no account needed.
opsec: passive
opsecNote: Analysis is done on headers you paste; the sender is not contacted. Avoid pasting headers into a third-party site if message contents are sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: DNS Checker is a well-known DNS/diagnostics site; the header analyzer is a standard parser, but it is a third-party host so treat pasted headers as exposed.
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
source: uk-osint
lastVerified: ''
enrichment: full
---

# dnschecker.org (Email Header Analyzer)

> A free web parser that turns raw email headers into a readable delivery path: originating IP, each relay hop, and timestamps.

## When to use
You have the full raw headers of an email (from a tipster, a person of interest, or a message tied to a missing person) and want to find where it actually came from. The originating `ip-address` and sending server `domain` are pivots: geolocate the IP, check it against an ISP/region, or compare it with other messages to confirm a shared sender.

## How to use it (`bestInteractionPattern`: web-manual)
1. In the source mail client, open the message and choose "Show original" / "View source" to copy the full raw headers (not just From/Subject).
2. Go to https://dnschecker.org/email-header-analyzer.php.
3. Paste the headers into the box and submit.
4. Read the parsed `Received:` hops top-to-bottom; the lowest hop is usually closest to the true origin.
5. Pivot: feed the originating `ip-address` to an IP geolocation/WHOIS tool and the sending `domain` to `[[email-dossier]]`.

## Inputs → Outputs
- **In:** raw email headers (`metadata`)
- **Out:** `ip-address` (originating + relays), sending `domain`, hop timestamps (`metadata`)
- **Empty/negative result looks like:** only the recipient's own provider IPs appear, or `Received:` chains are stripped/forged — common with major webmail (Gmail/Outlook hide the client IP), so origin tracing fails for those.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive toward the sender, but you are pasting message headers into a third-party website — do not use for sensitive material; prefer a local parser if so.
- Webmail providers mask the sender's client IP, so a "clean" trace often just points back to Gmail/Outlook servers, not the person.

## Overlaps ("do both")
- Pairs with `[[email-header-analyzer]]` (MXToolbox) — run both and compare; parsers differ in how they surface forged or nested `Received:` headers.

## Trust & verifiability
`trust: community` — DNS Checker is a reputable diagnostics provider, but results are only as good as the headers you supply and it is an external host.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dnschecker-org |
| category | email |
| selectorsIn → selectorsOut | metadata → ip-address, domain, metadata |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

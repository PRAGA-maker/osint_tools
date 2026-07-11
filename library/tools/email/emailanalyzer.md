---
id: emailanalyzer
name: EmailAnalyzer
description: Use when you have an email message (.eml) and want to extract its headers, originating IP, and check links/attachments — returns sender path, IP, and reputation signals.
url: https://github.com/keraattin/EmailAnalyzer
category: email
path:
- email
bestFor: Parsing a raw .eml file to surface originating IP, sender routing headers, and malicious link/attachment indicators.
selectorsIn:
- email
selectorsOut:
- ip-address
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (Python CLI); VirusTotal link/attachment checks need your own free VirusTotal API key.
opsec: passive
opsecNote: Runs locally on an email file you already possess — parsing headers touches nothing external and alerts no one. The exception is the optional VirusTotal lookups, which submit URLs/hashes (not the email body) to VirusTotal; avoid submitting anything sensitive you don't want shared with a third party.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Small open-source email-forensics utility (keraattin/EmailAnalyzer); inspectable and does standard header parsing, but a niche community tool rather than a hardened product.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
invitationOnly: false
deprecated: false
aliases:
- EmailAnalyzer
tags:
- Emails
- email-headers
- forensics
source: cyb-detective
lastVerified: '2026-07-11'
enrichment: full
---

# EmailAnalyzer

> A local CLI that cracks open a raw `.eml` file — pulling the full header chain, the originating IP, SPF/DKIM/routing details, and flagging suspicious links/attachments via VirusTotal — to tell you where an email really came from.

## When to use
You have an actual email message (a `.eml` you were sent or recovered) and want to extract intelligence from it: the true originating IP and sending server (past the display name), the routing path, authentication results, and whether embedded links/attachments are known-bad. This turns a message into leads — an originating `ip-address` to geolocate, sender infrastructure to pivot on, and phishing/attribution signals. Reach for it whenever the email itself, not just an address, is in hand.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/keraattin/EmailAnalyzer` and install its Python dependencies.
2. Save the target message as a `.eml` file (export "original"/"raw" from the mail client).
3. Run the analyzer against the file to dump parsed headers, the originating IP, and routing.
4. Optionally add a VirusTotal API key to check links/attachments for known-malicious indicators.
5. Pivot: the originating `ip-address` → IP geolocation/ASN tools; sender domains → domain/WHOIS; link infrastructure → further OSINT.

## Inputs → Outputs
- **In:** `email` message file (`.eml`)
- **Out:** `ip-address` (originating), `metadata-exif` (full headers, routing, auth results, link/attachment findings)
- **Empty/negative result looks like:** thin headers or no originating IP — common when the sender used a big provider (Gmail/Outlook strip/normalize originating IPs) or the file wasn't the raw original. Not tool failure; the provider simply didn't expose the IP.

## Gotchas & OpSec
- Human-in-the-loop: VirusTotal checks need an **API key**; header parsing needs none.
- You must supply the **raw** message — a forwarded copy loses the original headers. Big webmail providers hide the true originating IP.
- OpSec: passive/local for parsing; VirusTotal submissions go to a third party — don't submit sensitive content.

## Overlaps ("do both")
- Pairs with email-address enrichment (e.g. `[[holehe-2]]`) and IP-geolocation/WHOIS tools — those work the address; EmailAnalyzer works the *message* to recover IP and infrastructure the address alone won't give.

## Trust & verifiability
`trust: community` — an inspectable open-source utility doing standard, verifiable header parsing; outputs are as trustworthy as the headers themselves (which can be forged, so corroborate the originating IP).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | emailanalyzer |
| category | email |
| selectorsIn → selectorsOut | email → ip-address, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |

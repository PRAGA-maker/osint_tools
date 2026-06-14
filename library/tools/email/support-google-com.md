---
id: support-google-com
name: support.google.com
description: Use when you have an email you received and need to read its full headers — Gmail's help page on viewing the original message to extract sender IP/route metadata.
url: https://support.google.com/mail/answer/29436?hl=en-GB#zippy=%2Cother-email-services%2Cgmail
category: email
path:
- email
bestFor: Learning how to view full email headers ("Show original") in Gmail and other clients to extract routing metadata.
selectorsIn:
- email
selectorsOut:
- ip-address
- domain
- metadata-exif
status: live
pricing: free
costNote: Free official Google support documentation.
opsec: passive
opsecNote: Reading headers of a message you already hold is fully passive — no contact with the sender, nothing leaks to the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Google/Gmail support documentation; authoritative for the procedure it describes.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- email
- email-headers
- Email Header Related Sites
source: uk-osint
lastVerified: ''
enrichment: full
---

# support.google.com

> Gmail's official help page for viewing full email headers — the doorway to a message's routing metadata.

## When to use
You have received an `email` from or about a person of interest and need to extract the sender's originating `ip-address`, sending `domain`, and routing `metadata-exif` from the raw headers. This page documents the "Show original" procedure; the analysis itself is done by reading the headers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read the support page for the exact steps for Gmail (and links for other clients).
2. In Gmail, open the message → three-dot menu → "Show original" to see the full headers and the original raw `.eml`.
3. Read the `Received:` chain bottom-to-top for the originating `ip-address`, plus `Return-Path`, `From`, and authentication (SPF/DKIM/DMARC) results.
4. Pivot: feed the originating IP into geolocation/reputation tools (e.g. `[[spamhaus]]`) and the sending domain into WHOIS/domain research.

## Inputs → Outputs
- **In:** `email` (a message you possess)
- **Out:** sender `ip-address`, sending `domain`, routing/auth `metadata-exif`
- **Empty/negative result looks like:** the originating IP is a Google/relay server (common for webmail) rather than the sender's real address, or headers are sparse for internal mail.

## Gotchas & OpSec
- Webmail (Gmail-to-Gmail) often hides the sender's true IP behind provider servers — header IP analysis works best for mail sent via standalone clients/servers.
- OpSec: fully passive; you only inspect a message you already have. The sender is never notified.

## Overlaps ("do both")
- Pairs with `[[spamhaus]]` (reputation of the extracted IP/domain) and contrasts with `[[support-cloudhq-net]]` (active pixel tracking) — headers are the passive route to the same IP/metadata.

## Trust & verifiability
`trust: trusted` — official Google documentation; the procedure is authoritative and current.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | support-google-com |
| category | email |
| selectorsIn → selectorsOut | email → ip-address, domain, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

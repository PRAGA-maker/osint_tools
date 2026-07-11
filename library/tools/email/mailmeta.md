---
id: mailmeta
name: mailMeta
description: Use when you have a raw `email` (with full headers) and want to analyze its headers to spot spoofing and trace origin — returns sender/origin `ip-address` and authentication verdicts.
url: https://github.com/gr33nm0nk2802/mailMeta
category: email
path:
- email
bestFor: Parsing email headers to detect spoofing and extract the originating server/IP and SPF/DKIM/DMARC results.
selectorsIn:
- email
selectorsOut:
- ip-address
- email
status: live
pricing: free
costNote: Free, open-source Python CLI. No account or API key.
opsec: passive
opsecNote: Entirely offline analysis of a message you already possess — it parses the header text locally and contacts no one, so there is zero footprint against the sender. Only handle emails you are authorized to inspect.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source header-analysis utility; results are a straightforward parse of the message headers, so accuracy equals the headers' own reliability (which spoofers can partially forge).
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- mailMeta
- gr33nm0nk2802/mailMeta
tags:
- Emails
- headers
- spoofing
source: cyb-detective
lastVerified: '2026-07-11'
enrichment: full
---

# mailMeta

> A small Python CLI that reads email headers to flag spoofing and surface where a message really came from.

## When to use
You have a full email (with raw headers) tied to your subject or investigation and need to know whether it's genuine or spoofed, and where it originated. Header analysis reveals the sending server and originating `ip-address`, the true `From`/`Return-Path`, and SPF/DKIM/DMARC authentication outcomes — key for verifying a threatening/phishing message's source or corroborating that an email really came from a claimed sender.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and set up: `git clone https://github.com/gr33nm0nk2802/mailMeta`, install its Python requirements.
2. Export the target message's **full headers/source** (e.g. "Show original" in Gmail) to a file.
3. Run mailMeta against the header file per its README.
4. Read the output: originating IP/server, authentication (SPF/DKIM/DMARC) pass/fail, and mismatches that indicate spoofing.
5. Pivot: the originating `ip-address` feeds IP geolocation/`[[shodan]]` and reverse-DNS; a spoofing verdict changes how much you trust the address as a selector.

## Inputs → Outputs
- **In:** `email` message with full raw headers
- **Out:** originating `ip-address`/server, true sender `email`, SPF/DKIM/DMARC verdicts, spoofing indicators
- **Empty/negative result looks like:** clean auth results with a consistent chain — suggests genuine, but a sophisticated spoof or a relayed message can still mislead. Missing/partial headers (common after forwarding) limit what can be determined.

## Gotchas & OpSec
- Needs the **raw** headers, not the displayed message — forwarding strips/alters them, so capture the original source.
- Headers can be partially forged; treat a single indicator cautiously and corroborate.
- The originating IP is often a mail provider's server, not the sender's personal IP.

## Overlaps ("do both")
- Pairs with online header analyzers (e.g. MXToolbox) and IP-OSINT tools — mailMeta gives a fast local, no-disclosure parse, while IP tools enrich the extracted originating address.

## Trust & verifiability
`trust: community` — open-source and inspectable; its verdicts are a faithful parse of the headers, whose own trustworthiness (auth results) is the real limiting factor.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mailmeta |
| category | email |
| selectorsIn → selectorsOut | email → ip-address, email |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |

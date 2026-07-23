---
id: user-agent-parser
name: User Agent Parser
description: Use when you have a User-Agent string (from logs, headers or a tool config) and want it decoded — returns the device, OS and browser it describes.
url: https://developers.whatismybrowser.com/useragents/parse/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Decoding a raw User-Agent string into device, operating system and browser details.
selectorsIn:
- device-id
selectorsOut:
- device-id
status: live
pricing: freemium
costNote: Free web parser, no account. WhatIsMyBrowser also sells a paid parsing API/database for bulk use; the interactive single-string parse is free.
opsec: passive
opsecNote: You paste a string you already have into a parser — nothing is sent to the string's owner or any target. Only WhatIsMyBrowser sees the UA you submit; avoid pasting a string that itself contains sensitive identifiers if that matters to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: WhatIsMyBrowser is a well-known browser-detection service; parsing is heuristic (UA strings can be spoofed or faked), so treat the decoded device/OS as "claimed", not verified.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- whatismybrowser-com
aliases:
- WhatIsMyBrowser user agent parser
- UA parser
tags:
- Domain/IP/Links
- user-agent
- log-analysis
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# User Agent Parser

> Paste a raw User-Agent string and get back the device, OS version and browser it claims to be — for making sense of the UAs sitting in server logs, email headers, or tool configs.

## When to use
You have a User-Agent string — pulled from your own site's access logs, an email header, a leaked/collected request, or a piece of malware/tooling — and want to know what device and software it represents. Decoding a UA can corroborate what platform a subject used (e.g. a specific iPhone model + iOS version, or a bespoke bot), which becomes a small but useful pattern-of-life or attribution signal.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://developers.whatismybrowser.com/useragents/parse/ .
2. Paste the raw User-Agent string and submit.
3. Read the parsed breakdown: browser + version, operating system + version, device type/model, and whether it looks like a known bot/crawler.
4. Sanity-check: UA strings are trivially spoofable, so treat the result as what the client *claimed*, and look for inconsistencies (impossible OS/browser combos hint at faking).
5. Pivot: a distinctive device/OS corroborates other device signals; an unusual/custom UA becomes a search term to hunt the same client elsewhere.

## Inputs → Outputs
- **In:** a raw User-Agent string (a `device-id`-class fingerprint)
- **Out:** decoded device, OS, and browser (a normalised `device-id` description)
- **Empty/negative result looks like:** "unknown" / unrecognised fields — a malformed, truncated, or deliberately obfuscated UA; note it as suspicious rather than resolved.

## Gotchas & OpSec
- UA strings are self-reported and easily forged; the parser tells you what the string *says*, never proves it's true.
- Very new or very obscure devices may parse as "unknown" until the database catches up.
- OpSec: **passive** — you're decoding data you hold; nothing reaches the target.

## Overlaps ("do both")
- Pairs with `[[whatismybrowser-com]]` (the same provider's live browser-fingerprint view) — this decodes a UA you supply, that shows what your own browser broadcasts.

## Trust & verifiability
`trust: community` — a reputable, widely used detection service. The parsing is reliable for real strings but inherits the fundamental limitation that UAs can lie; corroborate device claims with independent signals.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | user-agent-parser |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | device-id → device-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

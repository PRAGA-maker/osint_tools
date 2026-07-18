---
id: useragentstring-com
name: UserAgentString.com
description: Use when you need a believable browser `user-agent` string to spoof, or to decode one you captured — returns parsed browser/OS/device details.
url: https://www.useragentstring.com/pages/useragentstring.php
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
- spoof-user-agent
bestFor: Picking a plausible real-world user-agent string to blend in, and parsing captured UA strings.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free reference directory; no account, key, or payment (© 2005–2025, actively maintained).
opsec: passive
opsecNote: This is your own tooling — you look up strings to configure your investigative browser. It never touches the target. Copy a current, common UA (not a rare/old one that stands out in the target's logs).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running independent reference catalogue of UA strings; widely cited, not a first-party vendor source, so treat its parsing as best-effort.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- useragentstring.com
- UAS parser
tags:
- opsec
- user-agent
- browser-fingerprint
- anonymity
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# UserAgentString.com

> A catalogue-plus-parser of browser user-agent strings — pick one to blend in, or decode one you scraped from a log/header.

## When to use
Two cases. (1) You are setting up a sock-puppet / investigative browser and want a **current, common** UA string so your requests don't stand out (blank or exotic UAs get flagged and can tip off a target watching their server logs). (2) You captured a UA string (from an email header, web log, or an exposed request) and want it decoded into browser, OS, and device.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the site.
2. To **find** a UA: browse the category tree (Browsers → Chrome, Mobile Browsers, Crawlers, etc.) and copy a recent, high-share string.
3. To **parse** a UA: paste the string into the analyzer / "explain" field to break out browser type, version, OS, and device.
4. Apply the chosen UA in your browser or HTTP client's headers before you begin collection.
5. Pivot: use alongside VPN/DNS/IPv6 leak checks so your header fingerprint and network egress tell the same story.

## Inputs → Outputs
- **In:** (optional) a raw user-agent string to decode, or a browsing goal ("give me a current Chrome-on-Windows UA")
- **Out:** parsed browser/OS/device fields, or a copy-paste UA string
- **Empty/negative result looks like:** an unrecognised/garbled string returns no clean parse — that itself is a signal the UA is spoofed, malformed, or from a very new/old client.

## Gotchas & OpSec
- Human-in-the-loop: none; purely a lookup.
- The catalogue can lag the newest browser releases, so a "latest" string here may already be a version or two behind — cross-check against your own real browser's UA.
- OpSec: passive and self-directed. The risk isn't this site; it's choosing a UA so rare it *increases* your distinctiveness. Match the mainstream.

## Overlaps ("do both")
- Pairs with [[ipv6-leak-tests]] — one hardens your HTTP fingerprint (what your browser claims to be), the other hardens your network fingerprint (what IP you actually leak); do both before touching a target.

## Trust & verifiability
`trust: community` — a long-lived independent reference, not an official browser-vendor source, so its parses are best-effort; verify anything security-critical against the live client.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | useragentstring-com |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

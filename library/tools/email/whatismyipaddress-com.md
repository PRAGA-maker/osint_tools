---
id: whatismyipaddress-com
name: Whatismyipaddress.com
description: Use when you have a raw email's full headers and want the originating IP and its approximate geolocation — paste headers into the Email Trace analyzer to extract and map the source IP.
url: https://whatismyipaddress.com/trace-email
category: email
path:
- email
bestFor: Extracting and geolocating the originating IP from pasted email headers (header → ip-address → location).
selectorsIn:
- email
- metadata
selectorsOut:
- ip-address
- geolocation
status: live
pricing: free
costNote: Free web tool; no account needed.
opsec: passive
opsecNote: You paste headers you already have; the tool parses them and geolocates the IP. It never contacts the sender or the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing public IP-utilities site (whatismyipaddress.com). Header parsing is reliable; IP geolocation is city/ISP-level and approximate.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- WhatIsMyIPAddress Email Trace
- whatismyipaddress.com/trace-email
tags:
- email
- email-headers
- ip-geolocation
source: metaosint
lastVerified: ''
enrichment: full
---

# Whatismyipaddress.com

> The "Trace Email Analyzer" on whatismyipaddress.com — paste a message's full headers and it pulls out the originating IP address and shows an approximate geolocation/ISP for it.

## When to use
You have an `email` from or about a subject and access to its full raw headers (`metadata`), and you want to know where it likely originated — the sending `ip-address` and a rough `geolocation`/ISP. Useful for corroborating or contradicting a sender's claimed location in a missing-persons contact thread, or for pivoting an IP into WHOIS/ISP inquiry.

## How to use it (`bestInteractionPattern`: web-manual)
1. In your mail client, open the message and "show original / view source" to copy the **full** headers.
2. Go to https://whatismyipaddress.com/trace-email and paste the headers into the analyzer box.
3. Submit; read the extracted originating IP and the approximate location/ISP it maps to.
4. Pivot: take the `ip-address` into a WHOIS/IP-intel lookup and the `geolocation` into your location hypothesis. If you need to learn how to read the headers yourself, see [[web-archive-org-2]].

## Inputs → Outputs
- **In:** `email` headers (`metadata`)
- **Out:** `ip-address`, `geolocation` (approximate city/ISP of the originating IP)
- **Empty/negative result looks like:** no usable originating IP found — common when the message came through Gmail/Outlook/etc., which substitute their own server IP and strip the sender's real one.

## Gotchas & OpSec
- You must paste the **complete** headers; partial/quoted headers won't parse.
- Webmail hides the sender's true IP behind the provider's infrastructure, so consumer mail often yields only the provider's datacenter location, not the person's.
- IP geolocation is approximate (city/ISP at best, often just the ISP's registration city) — never treat it as a precise `address`.
- OpSec: **passive** — you process headers you already hold; nothing is sent to the target.

## Overlaps ("do both")
- Pairs with [[web-archive-org-2]] (the haltabuse header-reading guide) — read that to understand which `Received:` line is the true origin, then let this tool extract and map it.

## Trust & verifiability
`trust: community` — a well-known general IP-utilities site. Header extraction is dependable; the geolocation is best-effort IP mapping and should be corroborated, not taken as exact location.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whatismyipaddress-com |
| category | email |
| selectorsIn → selectorsOut | email, metadata → ip-address, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

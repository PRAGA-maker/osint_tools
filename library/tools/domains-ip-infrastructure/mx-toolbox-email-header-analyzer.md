---
id: mx-toolbox-email-header-analyzer
name: MXToolbox Email Header Analyzer
description: Use when you have raw email headers and want the sending path and originating IP — returns ip-address and geolocation.
url: http://mxtoolbox.com/EmailHeaders.aspx
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Parsing raw email headers into a readable delivery chain to recover the originating IP and mail servers.
selectorsIn:
- email
selectorsOut:
- ip-address
- geolocation
- domain
status: live
pricing: freemium
costNote: The header analyzer is free and needs no account; MXToolbox's monitoring/bulk features are paid.
opsec: passive
opsecNote: You paste header text you already possess — nothing is sent to the sender, so it is passive. Note the header text is submitted to MXToolbox's servers; for sensitive material, parse headers locally instead.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: MXToolbox is a long-established, widely trusted email/DNS diagnostics provider; the parser is deterministic.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- ipaddress-tools
- email-header-analyzer
- mx-toolbox-blacklist-check
- mx-toolbox-reverse-ip-search
- mx-toolbox-whois-lookup
- mxtoolbox
- mxtoolbox-blacklists
- mxtoolbox-com
- mxtoolbox-com-2
aliases:
- MXToolbox Email Headers
- mxtoolbox header analyzer
tags:
- email-headers
- ip-lookup
- email
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# MXToolbox Email Header Analyzer

> Paste the full raw headers of an email and it lays out the delivery hops — the practical way to pull the originating IP and mail servers out of a message.

## When to use
You have an actual email from or about the subject (a message they sent, a signup confirmation, a header the subject shared) and you want to trace where it originated. The header analyzer parses the `Received:` chain top-to-bottom and surfaces the earliest/originating `ip-address`, the sending mail servers (`domain`), timestamps, and authentication results (SPF/DKIM/DMARC). That IP then geolocates to a coarse `geolocation` and can be pivoted to a provider.

## How to use it (`bestInteractionPattern`: web-manual)
1. In the target email, open **"show original" / "view source"** and copy the **full raw headers** (not just From/Subject).
2. Go to http://mxtoolbox.com/EmailHeaders.aspx, paste the headers, and analyze.
3. Read the parsed hops from the bottom up — the **earliest `Received:`** line usually holds the originating IP (beware forged headers above trusted hops).
4. Take the originating IP into an IP lookup (`[[ipaddress-tools]]`) for owner/ASN/geo.
5. Pivot: originating IP → ISP/hosting provider (legal-process target) and coarse location; sending domain → infrastructure/WHOIS; SPF/DKIM failures → possible spoofing.

## Inputs → Outputs
- **In:** raw email headers (from an `email` you possess)
- **Out:** `ip-address` (originating/relay IPs), `geolocation` (coarse, from the IP), `domain` (mail servers), plus auth results
- **Empty/negative result looks like:** headers show only the provider's outbound relays (Gmail, Outlook) with no client IP — major webmail hides the sender's real IP, so the trail stops at the provider.

## Gotchas & OpSec
- Modern webmail (Gmail/Outlook) strips the sender's originating IP — expect the chain to end at the provider's servers, not the person's device.
- Headers above the first trusted hop can be **forged**; only trust `Received:` lines added by servers you trust.
- OpSec: passive (you already hold the email); but the pasted headers go to a third party — parse locally if the content is sensitive.

## Overlaps ("do both")
- Pairs with `[[ipaddress-tools]]` — this extracts the IP from headers; that resolves the IP to owner, ASN, and geolocation. Run header analysis first, IP lookup second.

## Trust & verifiability
`trust: trusted` — a reputable diagnostics provider and a deterministic parser; the parse is reliable, but your *interpretation* (which hop is the real origin) is where errors creep in — reason carefully about forged/trusted boundaries.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mx-toolbox-email-header-analyzer |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | email → ip-address, geolocation, domain |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

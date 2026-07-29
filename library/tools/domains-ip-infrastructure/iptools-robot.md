---
id: iptools-robot
name: '@iptools_robot'
description: Use when you have a `domain` or `ip-address` and want a one-message Telegram bot to return whois, DNS, SSL, open ports, geolocation, threat reports, cookies and page metadata — returns ip-address, domain, geolocation and metadata-exif leads.
url: https://t.me/iptools_robot
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Fast all-in-one domain/IP recon from inside Telegram — whois, DNS, SSL, ports, geo, threat and metadata in one reply.
selectorsIn:
- domain
- ip-address
selectorsOut:
- ip-address
- domain
- geolocation
- metadata-exif
status: live
pricing: freemium
costNote: Free to query via Telegram; may rate-limit heavy use or gate advanced checks. No API key needed for basic lookups.
opsec: passive
opsecNote: The bot performs the lookups from its own infrastructure, so your IP does not touch the target — but you disclose your query (and your Telegram identity) to a third-party bot of unknown operator. Use a sock-puppet Telegram account and never query anything you must keep confidential.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: mobile-app
trust: unverified
trustNote: Third-party Telegram bot of unknown operator; convenient aggregator but not authoritative. Confirm any actionable result on a first-party source.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- iptools_robot
- IP Tools Telegram bot
tags:
- Domain/IP/Links
- Domain/IP investigation
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# @iptools_robot

> A universal domain/IP investigation Telegram bot: send it a host, get back whois, DNS, SSL, ports, geolocation, threat reports, cookies and page metadata in a single reply.

## When to use
You have a `domain` or `ip-address` and want a fast, consolidated recon snapshot without opening a dozen web tools — handy from a phone or when triaging a lead mid-conversation. The bot rolls whois ownership, DNS records, SSL cert details, open-port/threat reports, geolocation, and even page metadata (e.g. Facebook app id, cookies) into one message. Treat it as a triage aggregator; verify anything you'll act on.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Open https://t.me/iptools_robot in Telegram and start the bot.
2. Send the target `domain` (e.g. `example.com`) or `ip-address`.
3. Read the consolidated reply: whois, DNS, SSL, ports/threats, geolocation, metadata.
4. If prompted, pick a specific report type from the bot's menu for deeper detail.
5. Pivot: whois email/registrant → email tooling; resolved IP + geolocation → hosting/ASN maps; page metadata (FB app id, trackers) → cross-site correlation.

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** whois/registrant, DNS records, SSL cert, open ports + threat reports, `geolocation`, cookies and page `metadata-exif`-style fields
- **Empty/negative result looks like:** "no data"/empty sections for an unregistered or unresolvable host, or a rate-limit message asking you to wait — retry later or confirm on a first-party lookup.

## Gotchas & OpSec
- Human-in-the-loop: heavy use is rate-limited; you may need to slow down or wait.
- OpSec: passive on the target (the bot does the lookups), but you expose your query and Telegram identity to an unknown operator — use a sock-puppet account.
- Aggregated data can be stale or wrong; verify actionable facts on authoritative sources.

## Overlaps ("do both")
- Overlaps with `[[manytools]]` and dedicated whois/DNS tools — this bot is the fast mobile generalist; use a first-party whois/DNS/SSL source to confirm before acting.

## Trust & verifiability
`trust: unverified` — third-party bot, unknown operator; a convenient aggregator, not an authority. Cross-check every result that matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | iptools-robot |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → ip-address, domain, geolocation, metadata-exif |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | mobile-app |
| opsec | passive |
| human-in-loop | yes (rate-limit) |

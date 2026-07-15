---
id: whoisdombot
name: WhoisDomBot
description: Use when you have a `domain` or `ip-address` and want registration and DNS data from inside Telegram — returns WHOIS records plus dig/traceroute results for the domain/IP.
url: https://t.me/WhoisDomBot
category: messaging
path:
- messaging
bestFor: Quick WHOIS + dig/trace lookups on a domain or IP without leaving Telegram.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
- name
- email
status: live
pricing: free
costNote: Free Telegram bot; requires a Telegram account.
opsec: active
opsecNote: WHOIS/dig/trace queries touch registry and DNS infrastructure for the domain/IP, not the site itself — low exposure to the target, but you are querying through a third-party Telegram bot that sees every lookup you run. Use a sock-puppet Telegram account and avoid entering anything that identifies you or your case.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A community Telegram utility bot wrapping standard WHOIS/dig/trace; results reflect public registry/DNS data. As with any third-party bot, it can log your queries — trust the data, not the operator.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- WhoisDomBot
- Telegram whois bot
tags:
- telegram
- whois
- domain
- dns
source: awesome-osint
lastVerified: '2026-07-15'
enrichment: full
---

# WhoisDomBot

> A Telegram bot that returns WHOIS registration data for domains and IPs and runs dig/traceroute — command-line-grade domain recon from inside a chat.

## When to use
You have a `domain` or `ip-address` (say, from a scam site, a suspect's website, or an email header) and want its registration and DNS footprint quickly, on mobile, without a terminal. Registrant details (where not privacy-shielded), name servers, creation/expiry dates, and dig/trace output help attribute infrastructure and pivot to associated domains/hosts.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://t.me/WhoisDomBot in Telegram (web or app) with a sock-puppet account and start the bot.
2. Send a domain (e.g. `example.com`) or an IP to get its WHOIS record.
3. Use the bot's dig / trace commands for DNS records and routing path.
4. Read the output: registrar, registrant (if not redacted), name servers, dates; DNS records and hops.
5. Pivot: registrant email/name (if exposed) feeds email/people OSINT; name servers and shared registrant details link related domains; IP feeds hosting/geolocation lookups.

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** WHOIS fields (registrar, dates, name servers, and registrant `name`/`email` where not privacy-protected), plus dig/trace DNS data
- **Empty/negative result looks like:** GDPR/registrar privacy redaction hides registrant identity on most modern domains (you'll see "REDACTED FOR PRIVACY"), and some ccTLDs return minimal data — a redacted WHOIS is normal, not a tool failure.

## Gotchas & OpSec
- Registrant identity is usually privacy-shielded now; don't expect a name/email on most domains. Historical WHOIS tools may hold pre-redaction records.
- Third-party bot: it can log every lookup — use a sock-puppet Telegram account and enter only the domain/IP, nothing case-identifying.
- Data is only as fresh as the bot's WHOIS/DNS sources; corroborate critical findings with a first-party WHOIS/dig.

## Overlaps ("do both")
- Pairs with historical-WHOIS and passive-DNS services (which can reveal pre-privacy registrant data and subdomains the live WHOIS won't) — this bot is the fast live check; those add depth and history.

## Trust & verifiability
`trust: community` — a community utility bot over public WHOIS/DNS; the underlying data is verifiable against a first-party `whois`/`dig`, so confirm anything load-bearing directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whoisdombot |
| category | messaging |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address, name, email |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |

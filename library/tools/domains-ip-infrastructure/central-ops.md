---
id: central-ops
name: Central Ops
description: Use when you have a `domain`, `ip-address`, or `email` and want registration, DNS, and network records in one report — returns `domain`, `ip-address`, and owner details.
url: https://centralops.net/co/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-stop web dashboard for WHOIS, DNS, traceroute, and email verification without installing anything.
selectorsIn:
- domain
- ip-address
- email
selectorsOut:
- domain
- ip-address
- address
status: live
pricing: free
costNote: Free for limited interactive use with no login, ads, or CAPTCHA. Operated by Hexillion (Plano, TX); heavier/automated use is sold via the paid Hexillion API.
opsec: active
opsecNote: Queries run from CentralOps' servers, not yours — WHOIS/DNS lookups don't reveal your IP. But "Email Dossier" does a live SMTP probe of the target mail server (connects and checks the mailbox), which the receiving server can log. Use Domain/IP lookups freely; treat the email check as a touch on the target's infrastructure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running service by Hexillion, a private tools vendor; results are drawn from authoritative public records (registry WHOIS, DNS, ARIN/RIPE).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- domain-dossier
- email-dossier
- free-online-network-tools
aliases:
- CentralOps.net
- Hexillion CentralOps
tags:
- domain-and-ip-research
- whois
- dns
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Central Ops

> A free browser dashboard that bundles WHOIS, DNS, traceroute, ping, and email verification into single "Dossier" reports — no install, no account.

## When to use
You have a `domain`, an `ip-address`, or an `email` and want a fast, consolidated public-records report: who registered a domain, what DNS/name servers and IPs it uses, what network/ASN an IP belongs to, or whether an email's mail server accepts that mailbox. For a missing-person case this matters when your subject runs a website or when you're vetting where a suspicious message came from — it maps the digital infrastructure around a lead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://centralops.net/co/.
2. **Domain Dossier** — enter a `domain` or `ip-address` to get registrant WHOIS, DNS records, and a network-owner report in one page.
3. **Email Dossier** — enter an `email` to validate the address: it resolves the MX host and does an SMTP handshake to check whether the mailbox is accepted (without sending mail).
4. Use the à-la-carte tools (Ping, Traceroute, NsLookup, AutoWhois) for a single record type.
5. Pivot: registrant name/address feeds people-search; name servers and IPs feed reverse-IP and subdomain tools like `[[amass]]`.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, or `email`
- **Out:** registrant `address`/org, `domain` (name servers, MX), `ip-address` (A records, network owner/ASN), email-deliverability verdict
- **Empty/negative result looks like:** privacy-protected WHOIS ("REDACTED FOR PRIVACY" / a proxy registrant), or Email Dossier returning "mailbox unavailable"/timeout — meaning the address is invalid or the server refuses verification.

## Gotchas & OpSec
- Domain/IP lookups run from CentralOps' servers, so they don't expose your own IP to the target.
- Email Dossier's SMTP probe is **active** — the target's mail server sees a real connection and may log it; increasingly, providers block verification so results can be inconclusive.
- Free tier is rate-limited for interactive use; bulk/automated querying requires the paid Hexillion API.

## Overlaps ("do both")
- Pairs with `[[domain-dossier]]` and `[[email-dossier]]` (its own component reports) and with `[[amass]]` — CentralOps gives the registration/DNS snapshot, Amass expands it into the full subdomain map.

## Trust & verifiability
`trust: trusted` — a long-established commercial-grade service (Hexillion) that surfaces authoritative registry/DNS/ARIN data rather than a scraped or crowd-sourced dataset.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | central-ops |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address, email → domain, ip-address, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |

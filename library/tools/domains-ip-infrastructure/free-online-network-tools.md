---
id: free-online-network-tools
name: Free online network tools (CentralOps)
description: Use when you have a `domain`, `ip-address` or `email` and want a combined WHOIS/DNS/traceroute/email-validation dossier — returns registration, DNS and network detail in one report.
url: https://centralops.net/co/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-page "Domain Dossier"/"Email Dossier" combining WHOIS, DNS, traceroute and network lookups.
selectorsIn:
- domain
- ip-address
- email
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Free to use with per-session query limits; heavier use is rate-limited or gated. No account for basic lookups.
opsec: active
opsecNote: Mostly passive lookups (WHOIS/DNS), but Domain Dossier can run a traceroute and connect to the target's mail/servers, which touches the subject's infrastructure. Email Dossier probes the mail server (without sending mail). Use a research IP; the checks originate from CentralOps, not you, but some steps reach the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-established free network-tools site (CentralOps.net / Hexillion); aggregates standard WHOIS/DNS/network lookups.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- central-ops
- domain-dossier
- email-dossier
aliases:
- CentralOps
- CentralOps.net
tags:
- whois
- dns
- network-tools
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Free online network tools (CentralOps)

> CentralOps.net's free toolkit — its "Domain Dossier" and "Email Dossier" bundle WHOIS, DNS, traceroute and mail-server checks into one report.

## When to use
You have a `domain`, `ip-address` or `email` and want a fast, consolidated infrastructure read without stringing together separate WHOIS/DNS/traceroute tools. Domain Dossier gives registration + DNS + network context for a domain/IP; Email Dossier validates an email address and probes its mail server. Infrastructure-focused; useful for characterising a domain/host tied to a subject or checking whether an email is deliverable.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://centralops.net/co/.
2. Pick a tool: **Domain Dossier** (domain/IP) or **Email Dossier** (email), plus WHOIS/DNS/traceroute utilities.
3. Enter the selector and select the checks you want (WHOIS, DNS records, traceroute, service scan).
4. Read the combined report: registrar/owner, name servers, DNS records, network route, mail-server validity.
5. Pivot: hosting IP/registrar feeds further mapping; a validated email feeds email-OSINT tools.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, or `email`
- **Out:** `domain` (WHOIS, DNS), `ip-address` (network/route), email deliverability/mail-server signals
- **Empty/negative result looks like:** redacted/privacy WHOIS, or an Email Dossier that can't verify because the mail server hides validity — treat "unknown" as inconclusive, not "invalid."

## Gotchas & OpSec
- Human-in-the-loop: none, but free use is rate-limited per session.
- OpSec: WHOIS/DNS are passive, but traceroute and mail-server/service checks in Domain/Email Dossier **touch the target** — the connection comes from CentralOps, yet the target still sees a probe. Avoid the active checks if you must stay silent.
- Email Dossier tests deliverability without sending a message, but some servers accept-all, giving false positives.

## Overlaps ("do both")
- Bundles what `[[domain-dossier]]` and `[[email-dossier]]` do individually — use this for a one-shot combined report, and dedicated WHOIS/DNS tools when you need deeper, authoritative detail.

## Trust & verifiability
`trust: community` — a long-established free network-tools site surfacing standard registry/DNS data; verify actionable WHOIS/DNS results against the authoritative registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | free-online-network-tools |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address, email → domain, ip-address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |

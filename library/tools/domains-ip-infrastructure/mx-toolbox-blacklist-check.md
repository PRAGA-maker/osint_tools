---
id: mx-toolbox-blacklist-check
name: MX Toolbox Blacklist Check
description: Use when you have a `domain` or `ip-address` and want to know if it's on spam/abuse blacklists — returns which DNSBLs list it, a reputation signal for the host.
url: https://mxtoolbox.com/blacklists.aspx
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Checking a domain/IP against dozens of DNS blacklists at once to gauge its spam/abuse reputation.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free web check against many blacklists in one query; MXToolbox sells monitoring, but the on-demand check is free with no account.
opsec: passive
opsecNote: MXToolbox performs the blacklist queries from its own servers, so the target host never sees your IP. Only MXToolbox logs what you looked up; a clean session suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: MXToolbox is a well-established DNS/email diagnostics provider; it queries the actual DNSBL operators live, so a listing result is authoritative (subject to each blacklist's own accuracy).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- email-header-analyzer
- mx-toolbox-email-header-analyzer
- mx-toolbox-reverse-ip-search
- mx-toolbox-whois-lookup
- mxtoolbox
- mxtoolbox-blacklists
- mxtoolbox-com
- mxtoolbox-com-2
aliases:
- MXToolbox Blacklist Check
- MXToolbox blacklists
tags:
- toddington
- curated-directory
- whois-ip-lookups-website-analysis
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# MX Toolbox Blacklist Check

> One-shot reputation check — feed a domain or IP and see which of dozens of spam/abuse blacklists (DNSBLs) currently list it.

## When to use
You have a `domain` or `ip-address` — a mail server behind a suspicious email, a host serving a scam site, an IP from a header trace — and want a quick read on its reputation. Being listed on multiple DNSBLs (Spamhaus, SORBS, Barracuda, etc.) flags a host associated with spam, malware, or compromised infrastructure, which helps you judge whether an email/site is likely malicious and corroborates other infrastructure findings. It's a reputation signal, not an identity lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://mxtoolbox.com/blacklists.aspx.
2. Enter the `domain` or `ip-address` and run the check.
3. Read the results: each blacklist is shown as **Listed** (with the reason/return code) or **OK**. A cluster of listings indicates a bad-reputation host.
4. For a listed host, note *which* blacklists and why (spam source, dynamic IP, botnet, etc.).
5. Pivot: combine with WHOIS, reverse-IP, and DNS lookups on the same host to build the infrastructure picture; a clean result adds confidence that a mail source is legitimate.

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** per-blacklist Listed/OK status (a reputation profile of the host/`domain`/`ip-address`)
- **Empty/negative result looks like:** "OK" across all lists — the host isn't currently blacklisted. That's not proof of legitimacy (new or low-volume malicious hosts may be unlisted), just absence of a bad reputation.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — MXToolbox does the querying; the target host isn't touched by you.
- A listing reflects **reputation, not identity** — it tells you nothing about who owns/operates the host, only how it behaves. Use it alongside identity-oriented tools.
- Blacklists have false positives (shared hosting, dynamic ranges) and lag; weigh multiple lists rather than a single hit.

## Overlaps ("do both")
- Pairs with `[[mx-toolbox-whois-lookup]]`, `[[mx-toolbox-reverse-ip-search]]` and `[[mxtoolbox-com]]` — run the same host through blacklist + WHOIS + reverse-IP to combine reputation with ownership and co-hosting. Feed a mail header via `[[email-header-analyzer]]` to get the IP to check here.

## Trust & verifiability
`trust: trusted` — MXToolbox queries the DNSBL operators live, so listings are authoritative; the caveat is the accuracy/policy of each individual blacklist, not the tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mx-toolbox-blacklist-check |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

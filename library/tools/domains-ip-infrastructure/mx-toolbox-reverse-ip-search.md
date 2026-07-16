---
id: mx-toolbox-reverse-ip-search
name: MX Toolbox Reverse IP Search
description: Use when you have an `ip-address` and want its reverse-DNS (PTR) hostname to map it to a domain/host — returns domain and hosting leads.
url: https://mxtoolbox.com/ReverseLookup.aspx
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Turning an IP address into its reverse-DNS (PTR) hostname to identify the host/domain behind it.
selectorsIn:
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free single reverse-DNS (PTR) lookups on the web page; bulk/monitoring and some diagnostics require a paid MXToolbox account, but the basic lookup is free with no login.
opsec: passive
opsecNote: A PTR query goes to DNS, not to the target host, so the subject is not contacted or alerted. Run it from a neutral network anyway; the lookup itself reveals nothing about you to the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: MXToolbox is a long-established, widely used DNS/mail diagnostics provider; PTR results come straight from authoritative DNS.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- MXToolbox Reverse Lookup
- mxtoolbox PTR lookup
tags:
- toddington
- curated-directory
- whois-ip-lookups-website-analysis
- reverse-dns
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
relatedTools:
- email-header-analyzer
- mx-toolbox-blacklist-check
- mx-toolbox-email-header-analyzer
- mx-toolbox-whois-lookup
- mxtoolbox
- mxtoolbox-blacklists
- mxtoolbox-com
- mxtoolbox-com-2
---

# MX Toolbox Reverse IP Search

> MXToolbox's reverse-DNS (PTR) lookup: give it an IP address and it returns the hostname that IP resolves back to.

## When to use
You have an `ip-address` — from an email header, a server log, a connection, or a WHOIS record — and want to know what host/domain it belongs to. The PTR (reverse-DNS) record often exposes a mail server, ISP, hosting provider, or organisation name embedded in the hostname (e.g. `mail.example-corp.com`), giving you a `domain` to pivot on. Best treated as a quick infrastructure-attribution step, not a people-finder.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://mxtoolbox.com/ReverseLookup.aspx.
2. Enter the target `ip-address` and run the lookup.
3. Read the PTR result — the hostname the IP maps back to (if any), plus the resolving DNS server.
4. Pivot: take the returned hostname to a WHOIS/domain tool (`[[mx-toolbox-whois-lookup]]`) to identify the registrant/provider, and forward-resolve the domain to confirm it maps back to the same IP.

## Inputs → Outputs
- **In:** `ip-address`
- **Out:** reverse-DNS `domain`/hostname for that IP (and the `ip-address` confirmed), pointing at the host/provider.
- **Empty/negative result looks like:** "no PTR record" / no hostname returned — many IPs (especially residential/dynamic) have no reverse record, so the absence is normal and not a dead end for other tools.

## Gotchas & OpSec
- A PTR record is set by the IP's *operator*, not the end user, so a generic ISP hostname tells you the provider, not the individual.
- Residential and mobile IPs frequently have no meaningful PTR, or a dynamic-pool name that changes.
- Confirm attribution with a forward lookup (does the hostname resolve back to this IP?) before trusting it.

## Overlaps ("do both")
- Pairs with `[[mx-toolbox-whois-lookup]]` and `[[email-header-analyzer]]` — reverse DNS names the host, WHOIS names who runs it, and header analysis is where you often get the IP in the first place.

## Trust & verifiability
`trust: trusted` — MXToolbox is a reputable DNS/mail diagnostics service and PTR data comes from authoritative DNS, so results are reliable; interpretation (host ≠ person) is where care is needed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mx-toolbox-reverse-ip-search |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → domain, ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

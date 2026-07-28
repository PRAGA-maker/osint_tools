---
id: remote-dns-lookup
name: Remote DNS Lookup
description: Use when you have an `ip-address` and want the domain name(s) and ISP behind it — returns reverse-DNS host and provider, a pivot from IP back to infrastructure.
url: https://remote.12dt.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Reverse-DNS lookup of an IP address to its associated domain/host and ISP.
selectorsIn:
- ip-address
selectorsOut:
- domain
status: live
pricing: free
costNote: Free, no account; capped at ~75 lookups per 24 hours per user.
opsec: passive
opsecNote: You query the tool's resolver, not the target's server, so the subject is not alerted. It performs registry/PTR-style resolution; standard third-party site logging applies, so use a clean browser if you don't want the lookup tied to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Small free utility; useful for a quick reverse lookup but corroborate results with an authoritative DNS/PTR query for anything decisive.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- remote.12dt.com
- reverse DNS lookup
tags:
- domain-and-ip-research
- reverse-dns
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Remote DNS Lookup

> A free reverse-DNS utility: give it an IP and it returns the domain/host and ISP tied to that address — the pivot from a bare IP back to named infrastructure.

## When to use
You have an `ip-address` — pulled from an email header, a server log, a connection record, or a WHOIS/hosting lookup — and want to know what domain or host name it resolves to and which provider owns it. It turns an anonymous IP into a lead (a hostname to research, an ISP to note), which is a common step when tracing where a message or a site was served from.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://remote.12dt.com in a browser (use a clean session if you don't want the query associated with you).
2. Enter the target `ip-address` (dotted-quad IPv4).
3. Read the result: the associated domain/host name (reverse/PTR) and the assigned ISP.
4. Mind the cap — roughly 75 lookups per 24 hours.
5. Pivot: research the returned host name; a mismatch between the reverse-DNS name and a claimed identity is worth flagging.

## Inputs → Outputs
- **In:** `ip-address`
- **Out:** associated `domain`/host name and ISP
- **Empty/negative result looks like:** no PTR record / "no domain found" — many IPs (especially residential and cloud) have generic or absent reverse DNS, so a blank is common and not conclusive.

## Gotchas & OpSec
- Reverse DNS is only as good as the operator's PTR records — plenty of legitimate IPs have generic (`*.isp.net`) or no reverse name; absence proves nothing.
- Rate-limited (~75/day); batch your queries.
- OpSec: **passive** — you hit the tool, not the subject, so no alert reaches the target.

## Overlaps ("do both")
- Do both with a forward WHOIS/hosting lookup: reverse DNS gives you the host name for an IP, while WHOIS on that IP/domain gives the registrant and network owner — together they map the infrastructure.

## Trust & verifiability
`trust: community` — a small free reverse-lookup utility. Handy for a fast answer; confirm anything decisive with an authoritative PTR/DNS query (e.g. `dig -x`).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | remote-dns-lookup |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

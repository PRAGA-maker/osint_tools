---
id: r3con1z3r
name: r3con1z3r
description: Use when you have a `domain` and want a one-command passive footprint bundled into an HTML report — returns WHOIS, DNS, headers, links and the host `ip-address` in a single file.
url: https://github.com/deven96/r3con1z3r
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: A quick, single-command passive footprint of a domain, output as a readable HTML report.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: degraded
pricing: free
costNote: Free and open-source (Python, pip installable); no account.
opsec: passive
opsecNote: The core modules (WHOIS, DNS, HTTP headers, link extraction) are passive lookups. Note it can also invoke an Nmap port scan and traceroute, which ARE active and touch the target host — skip those, or run them only from a sock-puppet egress, if you need to stay passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Small community footprinting tool; the fork lineage (abdulgaphy → deven96) is largely inactive, so treat it as a convenience wrapper around standard lookups rather than a maintained product.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- r3con1z3r
tags:
- web-recon
- whois
- dns
source: gh-topic-footprinting
lastVerified: '2026-07-29'
enrichment: full
---

# r3con1z3r

> A lightweight one-shot footprinting wrapper: give it a domain, get an HTML report bundling WHOIS, DNS, headers and links.

## When to use
You have a `domain` and want a fast, all-in-one passive recon snapshot without running five separate tools — WHOIS, DNS records, HTTP headers, and page hyperlinks collated into one shareable HTML file. Good for an initial triage pass on a subject's site; the collated links and header data can surface further pivots (emails, other domains, tech stack).

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install r3con1z3r` (Python 2/3).
2. Run against a target: `r3con1z3r -d example.com`.
3. Open the generated `example.com-r3con1z3r.html` report.
4. Read: WHOIS/registrant, DNS records, host `ip-address`, HTTP headers (server/tech), and extracted hyperlinks.
5. Pivot: registrant details feed people/WHOIS-history tools; the host IP feeds reverse-IP/ASN; extracted links may reveal social profiles or other domains.

## Inputs → Outputs
- **In:** `domain`
- **Out:** HTML report with WHOIS, DNS, HTTP headers, hyperlinks, and host `ip-address`
- **Empty/negative result looks like:** sparse sections (redacted WHOIS, no links) — the domain uses privacy protection / is a bare parked page; not a tool failure.

## Gotchas & OpSec
- Mostly passive, but the optional **Nmap scan and traceroute modules are active** and hit the target — omit them to stay passive.
- The project is largely unmaintained; if install/deps break, run the underlying lookups (whois, dig, curl -I) directly instead.
- It aggregates standard sources — treat it as convenience, not unique data.

## Overlaps ("do both")
- Overlaps with any WHOIS + DNS + header toolchain; r3con1z3r's value is bundling them into one report — use dedicated tools (`[[dnsx]]`, a WHOIS-history service) when you need depth on one facet.

## Trust & verifiability
`trust: community` — a thin wrapper over public lookups you can re-run by hand, so its data is verifiable; the tool itself is inactive, hence `status: degraded`.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | r3con1z3r |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |

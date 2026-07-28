---
id: ronin-recon
name: ronin-recon
description: Use when you have a `domain` or `ip-address` and want a recursive automated recon sweep (subdomains, DNS, ports, TLS certs) that feeds findings back into itself — returns domain, ip-address.
url: https://github.com/ronin-rb/ronin-recon
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Recursive infrastructure recon that keeps expanding from discovered subdomains/IPs/certs automatically.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open-source (Ruby gem, part of the Ronin toolkit). Install via RubyGems; no account.
opsec: active
opsecNote: ronin-recon performs active DNS resolution, port scanning, and TLS/cert fetching against the target and its discovered assets — this traffic reaches the target and can be logged. Its recursive nature amplifies volume as it expands, so scope carefully and run only against infrastructure you're authorised to test, from a suitable host/VPN.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Part of the actively-developed Ronin Ruby security toolkit (ronin-rb). Open-source and inspectable; results are as good as its worker modules and your scoping.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- dnsdumpster
- cloudmare
- sn1per
tags:
- recon-engine
- dns
- port-scan
- tls
source: gh-topic-footprinting
lastVerified: '2026-07-28'
enrichment: full
---

# ronin-recon

> A recursive recon engine from the Ronin Ruby toolkit: seed it a domain or IP and it fans out through subdomains, DNS, open ports, and TLS certs — feeding each discovery back in to find more.

## When to use
You have a `domain` or `ip-address` for infrastructure you're **authorised to assess** and want an automated, self-expanding map of its footprint (subdomains, resolved hosts, open ports, certificate SANs that reveal sibling domains). Infra/pentest-oriented; low relevance to a person-centric case unless it pivots to an org's network.

## How to use it (`bestInteractionPattern`: cli)
1. Install the gem: `gem install ronin-recon` (part of the Ronin toolkit).
2. Run against a target: `ronin-recon run <domain-or-ip>` (add scoping/output flags).
3. Let it recurse — new subdomains/IPs/cert names discovered become fresh inputs, so watch scope and set boundaries.
4. Review the graph of discovered `domain`s, `ip-address`es, open ports, and TLS cert data.
5. Pivot: cert SANs → additional related domains; open ports → service enumeration; feed hosts into other tools for deeper analysis.

## Inputs → Outputs
- **In:** `domain` or `ip-address` (seed)
- **Out:** `domain` (subdomains, cert-derived names), `ip-address` (resolved hosts), open ports, TLS cert details
- **Empty/negative result looks like:** little expansion — a well-locked-down target with no extra subdomains/exposed services returns a sparse graph, which is a real finding, not a failure.

## Gotchas & OpSec
- **Recursive = loud:** volume grows as it discovers more. Scope tightly and authorise before running; the traffic hits the target and is logged.
- Ruby toolchain required; integrates with the rest of the Ronin suite.
- Only assess infrastructure you own or are contracted to test.

## Overlaps ("do both")
- For passive-first mapping use `[[dnsdumpster]]`; `[[cloudmare]]` for origin-IP behind CDNs; `[[sn1per]]` for a broader multi-tool pentest workflow. Use ronin-recon when you want automated recursive expansion in a scriptable Ruby pipeline.

## Trust & verifiability
`trust: community` — open-source and part of a maintained toolkit; inspect its modules. Findings are machine-generated leads — verify discovered assets belong to the target before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ronin-recon |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |

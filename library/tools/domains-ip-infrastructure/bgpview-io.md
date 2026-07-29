---
id: bgpview-io
name: Bgpview.io
description: Use when you have an `ip-address`, ASN, or `domain` and want to map the routing/hosting infrastructure and owning organisation behind it — returns ip-address, domain, employer-org.
url: https://bgpview.io
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Mapping the ASN, ISP, prefixes and owning org behind an IP or domain.
selectorsIn:
- ip-address
- domain
selectorsOut:
- ip-address
- domain
- employer-org
status: live
pricing: free
costNote: Free public BGP toolkit and JSON API (api.bgpview.io); no account or API key required.
opsec: passive
opsecNote: Passive — you query BGPView's own cached routing tables and RIR WHOIS data, not the target's infrastructure, so nothing is sent to the subject or the host being investigated.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent BGP toolkit widely used by network engineers; data is sourced from public routing tables and Regional Internet Registry WHOIS, so it is verifiable against those primary sources.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
aliases:
- BGPView
- bgpview.io
tags:
- domain-and-ip-research
- asn
- bgp
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Bgpview.io

> A free BGP/ASN toolkit that turns an IP, ASN, or domain into the routing picture around it — which network announces it, who owns that network, and what else that owner controls.

## When to use
You have an `ip-address` (say, the address a message header, login log, or geolocation lookup surfaced) or a `domain`, and you want to know **which organisation's network it lives on** and what else that organisation runs. BGPView answers "what ASN is this IP in, who owns that ASN, what other prefixes/IP ranges do they announce, and who are their upstream providers." That converts a bare IP into an `employer-org`/hosting-provider lead and lets you spot when several addresses trace back to the same operator.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://bgpview.io and enter an IP address, an ASN (e.g. `AS15169`), or a domain in the search box.
2. Read the result page:
   - For an **IP**, it shows the announcing ASN, the enclosing prefix, and the organisation/ISP that owns it.
   - For an **ASN**, it lists all IPv4/IPv6 prefixes, upstream and downstream peers, IX presence, and the registered org name/contact.
3. For automation, hit the free JSON API directly — e.g. `https://api.bgpview.io/ip/8.8.8.8` or `https://api.bgpview.io/asn/15169/prefixes` — no key needed.
4. Pivot: the owning-org name feeds a company/registry lookup; the full prefix list lets you check whether other IPs of interest belong to the same operator; hosting-provider IPs tell you the subject was behind shared infrastructure (so the IP won't map to a person).

## Inputs → Outputs
- **In:** `ip-address`, ASN, or `domain`
- **Out:** announcing ASN and `employer-org`/ISP name, enclosing `ip-address` prefix range, related `domain`/prefix inventory, upstream/peer relationships
- **Empty/negative result looks like:** "No results" or an IP that resolves only to a large cloud/CDN ASN (Cloudflare, Google, AWS) — meaning the address is shared hosting infrastructure and identifies the provider, not the subject.

## Gotchas & OpSec
- No human-in-the-loop, no login, no CAPTCHA.
- Passive: all data is from public routing/WHOIS, so the lookup never touches the subject.
- Routing data tells you the **network operator**, not the end user. A residential IP maps to an ISP; a server IP maps to a host. Neither is a person by itself.

## Overlaps ("do both")
- Pairs with an IP-geolocation tool like `[[utrace]]` or `[[geo-data-tool]]` — those estimate a physical location while BGPView gives the authoritative network/owner, and together they corroborate (or contradict) each other.

## Trust & verifiability
`trust: community` — a long-running independent toolkit whose data mirrors public BGP tables and RIR WHOIS; cross-check any critical finding against the relevant registry (RIPE/ARIN/APNIC) directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bgpview-io |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → ip-address, domain, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

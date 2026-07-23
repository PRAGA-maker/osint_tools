---
id: dns-history
name: DNS History
description: Use when you have a `domain` and want to see how its nameservers changed over time — returns a timeline of historical NS records to reveal past hosting/registrar moves.
url: https://completedns.com/dns-history/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Tracing a domain's nameserver history to spot hosting/registrar changes and infrastructure links.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free single-domain lookups with a small daily quota (a few reports); bulk checking (up to 5,000 domains) and exports are paid.
opsec: passive
opsecNote: Passive — you query CompleteDNS's historical database, not the target domain's live infrastructure, so the domain owner is not contacted. Only CompleteDNS logs your lookup.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent service (CompleteDNS) that has logged nameserver changes since 2002 with billions of records; widely used, though it is a third party, not an authoritative registry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- CompleteDNS
- completedns.com
tags:
- domain-and-ip-research
- dns
- historical
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# DNS History

> A long-running archive of nameserver changes: enter a domain and see which nameservers it used, and when — a way to follow a domain's infrastructure through time.

## When to use
You have a `domain` and want its *history*, not just its current DNS. Reach for this to spot when a domain switched hosting or registrar, to correlate a group of domains that all moved to the same nameservers at the same time (a common ownership signal), or to reconstruct what a domain looked like before it was parked or repurposed. It tracks nameserver (NS) changes specifically, which is often enough to tie infrastructure together.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://completedns.com/dns-history/ and enter the target `domain`.
2. Read the chronological list of nameserver records with the dates each was seen — this is the domain's NS timeline.
3. Look for transitions: a change of nameserver often marks a change of host, owner, or purpose.
4. Cross-reference: if several domains share the same unusual nameservers over the same window, they may share an operator.
5. Pivot: past nameservers/hosts feed WHOIS-history and passive-DNS tools for deeper infrastructure mapping. (Free lookups are quota-limited; queue the most important domains first.)

## Inputs → Outputs
- **In:** `domain`
- **Out:** a dated timeline of historical nameserver records (and thus hosting/registrar shifts)
- **Empty/negative result looks like:** little or no history for a very new domain, or gaps where CompleteDNS wasn't observing — absence of records is not proof the domain didn't exist then.

## Gotchas & OpSec
- It focuses on nameserver history, not full A/MX/TXT history — pair with passive-DNS for IP-level history.
- Free tier is capped to a few lookups per day; heavy use needs a paid plan.
- OpSec: passive and safe; the target is never queried directly.

## Overlaps ("do both")
- Pairs with WHOIS-history and passive-DNS tools — this gives the nameserver timeline, those give registrant and IP timelines. Together they reconstruct a domain's full lifecycle and reveal co-owned infrastructure.

## Trust & verifiability
`trust: community` — an established third-party historical-DNS service; its records are a strong lead for infrastructure analysis, but confirm ownership conclusions against WHOIS/passive-DNS rather than relying on NS overlap alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dns-history |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

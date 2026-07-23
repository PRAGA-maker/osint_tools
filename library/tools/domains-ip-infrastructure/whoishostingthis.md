---
id: whoishostingthis
name: WhoIsHostingThis
description: Use when you have a `domain` and want to know which company hosts it — returns the hosting provider plus basic WHOIS/ownership context.
url: https://www.whoishostingthis.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: A one-box lookup of which hosting provider serves a given website.
selectorsIn:
- domain
selectorsOut:
- ip-address
- employer-org
status: degraded
pricing: free
costNote: The lookup tool is free; the site is now mostly affiliate-driven hosting reviews with the tool as one small feature.
opsec: passive
opsecNote: "The lookup resolves the domain and reads its hosting/IP footprint from public data, so the target site is not meaningfully probed by you — passive. WhoIsHostingThis logs your queries; use a sock-puppet session for sensitive domains. Cross-check its answer, as the identified host can be a CDN/reseller rather than the true origin."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running but now affiliate/review-focused site; the hosting-lookup feature still works but is secondary, and results (especially behind a CDN) should be corroborated with a direct WHOIS/DNS check.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Who Is Hosting This
- whoishostingthis.com
tags:
- domain-and-ip-research
- hosting-lookup
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# WhoIsHostingThis

> A simple "who hosts this site?" lookup — enter a domain, get its hosting provider and basic ownership context. (The site has since become mostly hosting-review content, but the tool still runs.)

## When to use
You have a `domain` and want a quick read on which company hosts it — an early step in mapping a target's infrastructure, spotting shared hosting, or identifying the provider to approach for records. It's a convenience wrapper over WHOIS/DNS/IP data. Infrastructure-oriented, so low direct missing-persons relevance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.whoishostingthis.com and find the "Enter a Website URL" lookup box (amid the review content).
2. Enter the target `domain` and submit.
3. Read the result: identified hosting provider (`employer-org`), resolving `ip-address`, and basic WHOIS/ownership hints.
4. **Corroborate** with a direct WHOIS + DNS lookup — if the answer is a CDN (Cloudflare, Fastly) or reseller, the true origin host is hidden and needs deeper recon.
5. Pivot the `ip-address` into passive-DNS/reverse-IP tools for co-hosted domains.

## Inputs → Outputs
- **In:** `domain`
- **Out:** hosting provider (`employer-org`), `ip-address`, basic WHOIS context
- **Empty/negative result looks like:** "Cloudflare"/CDN only, or no clear provider — the real origin is masked behind a proxy; treat this as "CDN in front," not the actual host.

## Gotchas & OpSec
- The site is now dominated by affiliate hosting reviews; the lookup is a minor feature — don't mistake the review content for tool output.
- CDN/proxy fronting will hide the true origin host; always confirm with an independent WHOIS/DNS query.
- Data can be cached/stale; verify anything decision-critical against a live authoritative source.

## Overlaps ("do both")
- Pairs with passive-DNS and IP tools like [[dns-dumpster]] and [[ipinfo-map]] — WhoIsHostingThis gives a fast provider guess, those confirm the IP footprint and neighbors.

## Trust & verifiability
`trust: community` — a long-running but now review-focused site; the hosting answer is a useful starting hint, not authoritative, so corroborate with a direct WHOIS/DNS lookup before relying on it.

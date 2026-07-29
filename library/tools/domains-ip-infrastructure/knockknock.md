---
id: knockknock
name: KnockKnock
description: Use when you have a `domain` and want other domains likely owned by the same person/company — a Go CLI over the ViewDNS API returning related `domain`s.
url: https://github.com/harleo/knockknock
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Quickly pulling a list of domains associated with a target domain (reverse-WHOIS style) to find same-owner infrastructure.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: The tool is free and open source; it queries the free tier of the ViewDNS.info API (capped around 500 results). Heavier ViewDNS use needs a paid ViewDNS API key.
opsec: passive
opsecNote: You don't touch the target's servers — the query goes to ViewDNS.info, which sees your API request (and IP). It's passive against the subject, but ViewDNS logs the lookup; use it from neutral infrastructure. Results are inferential (shared registrant data), so treat "related" domains as leads, not proof of common ownership.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: An open-source Go CLI (harleo/knockknock) that wraps the ViewDNS.info reverse-lookup API; the tool is a thin, auditable client and the data quality is ViewDNS's, not the tool's.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- knockknock
- harleo knockknock
tags:
- Domain/IP/Links
- Dorks/Pentest/Vulnerabilities
- reverse-whois
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# KnockKnock

> A fast Go CLI that queries the ViewDNS.info API to list domains related to a target domain — a scriptable reverse-lookup for same-owner infrastructure discovery.

## When to use
You have one `domain` tied to a subject and want to find the rest of their web footprint — other domains that share registrant details, historical ownership, or DNS links, which "could theoretically belong to the same person or company." Useful for pivoting from a single known site to an infrastructure cluster in domain/company investigations. It's a convenience wrapper around ViewDNS reverse lookups, made scriptable.

## How to use it (`bestInteractionPattern`: cli)
1. Install from GitHub (Go): clone and `go build`, or grab a release binary.
2. Run it against the target `domain` (see the repo's usage for exact flags).
3. It calls the ViewDNS.info API and returns related domains (free tier ≈ 500 results).
4. Read the list; each entry is a *candidate* same-owner domain, not a confirmation.
5. Pivot: verify promising candidates with full WHOIS, passive DNS, and hosting/analytics-ID checks before asserting common ownership.

## Inputs → Outputs
- **In:** `domain`
- **Out:** a list of related `domain`s (candidate same-owner infrastructure)
- **Empty/negative result looks like:** few or no related domains — the registrant is privacy-protected or the domain is isolated; absence doesn't rule out other holdings behind WHOIS privacy.

## Gotchas & OpSec
- Passive against the subject, but ViewDNS logs your lookups — use neutral infrastructure.
- Free tier caps results (~500); large registrants get truncated, and modern WHOIS privacy weakens reverse-WHOIS signal.
- "Related" is inferential — always corroborate ownership with independent signals (analytics IDs, TLS certs, passive DNS).

## Overlaps ("do both")
- Pairs with WHOIS/reverse-WHOIS, passive-DNS, and analytics-ID tools — KnockKnock generates the candidate domain list; those confirm which candidates genuinely share an owner.

## Trust & verifiability
`trust: community` — an open-source, auditable CLI; its findings are only as good as the underlying ViewDNS reverse-lookup data, so treat outputs as leads to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | knockknock |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |

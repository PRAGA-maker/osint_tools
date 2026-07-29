---
id: sitedossier
name: Sitedossier
description: Use when you have a `domain` or `ip-address` and want related infrastructure — returns other domains on the same host/name servers, plus a domain profile.
url: https://www.sitedossier.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- analytics
bestFor: Finding sibling domains via reverse-IP / shared name servers and getting a quick profile of a domain's infrastructure.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free web lookup; no account. May throttle heavy automated use with a CAPTCHA.
opsec: passive
opsecNote: Queries Sitedossier's own aggregated index rather than the target's servers, so the subject is not contacted or alerted. Standard third-party logging applies; use a clean session for attribution hygiene.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running independent domain-profiling service. Its reverse-IP/name-server data is a useful pivot but can be incomplete or stale — corroborate before drawing firm links.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- viewdns-info
- securitytrails
- whoxy
aliases:
- sitedossier.com
tags:
- reverse-ip
- domain-intel
- infrastructure
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# Sitedossier

> A domain-profiling service — look up a `domain` or `ip-address` and see the other sites sharing its host and name servers, a fast way to expand a subject's infrastructure.

## When to use
You have one `domain` or `ip-address` tied to your subject and want to find related properties: sites on the same IP (reverse-IP), domains using the same name servers, and a summary of the domain's hosting. Useful for expanding from a single known site to a cluster of connected domains an individual or organisation controls.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.sitedossier.com/.
2. Enter the `domain` (or navigate to an `ip-address` / name-server page) and submit; solve a CAPTCHA if prompted.
3. Read the profile: hosting IP, name servers, and — most useful — lists of neighbouring domains on the same IP or name servers.
4. Filter the neighbours: shared cheap-shared-hosting IPs yield many unrelated domains, while a dedicated IP or unusual name server is a stronger link.
5. Pivot: candidate related `domain`s feed WHOIS/history tools; the `ip-address` feeds `[[securitytrails]]` / `[[viewdns-info]]` for deeper reverse-DNS.

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** related `domain`s (reverse-IP, shared name servers), hosting `ip-address`, name servers
- **Empty/negative result looks like:** thin or no neighbour data — the domain is new, uses a big CDN/shared host (so neighbours are meaningless), or Sitedossier hasn't indexed it; use a dedicated reverse-IP service.

## Gotchas & OpSec
- Reverse-IP on shared hosting/CDN produces huge, mostly-unrelated neighbour lists — weight links by how dedicated the infrastructure is.
- Data can be stale; treat associations as leads to confirm with a current DNS/WHOIS source.
- Heavy querying triggers CAPTCHAs; use an API-backed tool for bulk work.

## Overlaps ("do both")
- Pairs with `[[securitytrails]]` and `[[viewdns-info]]` (fresher, API-driven reverse-DNS and history) and `[[whoxy]]` (reverse-WHOIS by registrant). Do both: Sitedossier for a quick free neighbour view, the others to confirm and add historical depth.

## Trust & verifiability
`trust: community` — a useful, long-lived free pivot service, but coverage/freshness aren't guaranteed. Confirm any inferred relationship against a current, authoritative DNS/WHOIS source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sitedossier |

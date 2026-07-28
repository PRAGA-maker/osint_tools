---
id: amass
name: Amass
description: Use when you have a `domain` and want to map its full external footprint — returns subdomains and their `ip-address` infrastructure.
url: https://github.com/owasp-amass/amass
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- saas-footprinting
bestFor: Deep subdomain enumeration and external attack-surface mapping for a target domain.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open-source (Apache-2.0). No cost to run; some optional data-source integrations use free API keys.
opsec: active
opsecNote: Passive mode (`enum -passive`) queries only third-party data sources and never touches the target. Active/brute modes do DNS resolution and brute-force lookups that hit the target's authoritative DNS and can be logged — run those from an attribution-safe host.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: trusted
trustNote: OWASP flagship project, ~15k GitHub stars, actively maintained by the OWASP Amass team.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- dork-dump
aliases:
- OWASP Amass
- amass enum
tags:
- subdomain-enumeration
- attack-surface
- dns
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# Amass

> OWASP's attack-surface mapper: hand it a domain and it enumerates every subdomain and piece of infrastructure it can correlate from public sources plus active probing.

## When to use
You have a `domain` tied to your subject — a personal site, a small business they run, a vanity domain — and you want the full picture of what hangs off it: subdomains, mail hosts, dev/staging boxes, hosting `ip-address` ranges. Amass is the tool when a single WHOIS/DNS lookup isn't enough and you need exhaustive breadth. For a missing-person case its value is indirect (infrastructure, not people), but it can surface a self-hosted service, blog, or forum that in turn leaks names, emails, or account handles.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `go install -v github.com/owasp-amass/amass/v4/...@master`, or run the maintained Docker image (`docker run caffix/amass`).
2. Passive sweep (quiet, no packets at the target): `amass enum -passive -d example.com`.
3. Full enumeration (adds active DNS resolution + brute force): `amass enum -active -d example.com -brute`.
4. Optionally drop free API keys (Shodan, SecurityTrails, VirusTotal, etc.) into `config.yaml` to widen the passive data sources.
5. Read the output: subdomains with resolved `ip-address` records. Feed interesting hosts to a WHOIS/reverse-IP tool or open them in a browser.

## Inputs → Outputs
- **In:** `domain`
- **Out:** `domain` (subdomains/FQDNs), `ip-address` (resolved hosts and infrastructure)
- **Empty/negative result looks like:** only the apex domain resolves and no subdomains are returned — common for domains parked on shared hosting or fronted entirely by a CDN.

## Gotchas & OpSec
- Human-in-the-loop: only to obtain and paste free API keys for extra data sources; the tool itself is fully automated.
- OpSec: `-active` and `-brute` generate DNS traffic against the target's servers and can be logged — use `-passive` when attribution matters.
- Large domains can take many minutes and generate heavy traffic; scope the run.

## Overlaps ("do both")
- Pairs with `[[dork-dump]]` — Amass maps the hosts, then dork-dump harvests the indexed documents (and their metadata) sitting on those hosts.

## Trust & verifiability
`trust: trusted` — OWASP flagship, open-source and independently auditable, with an active maintainer team and a large user base.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | amass |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key) |

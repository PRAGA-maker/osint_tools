---
id: owasp-amass
name: OWASP Amass
description: Use when you have a `domain` and want its full external attack surface — returns subdomains, associated IPs, ASNs, and related infrastructure via passive and active reconnaissance.
url: https://github.com/OWASP/Amass
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Deep subdomain enumeration and external asset/infrastructure mapping for a domain, aggregating dozens of OSINT sources plus optional active DNS.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open-source (Apache-2.0), maintained under OWASP. CLI; some data sources yield more with free API keys, but core use needs none.
opsec: active
opsecNote: Amass has a passive mode (queries third-party sources only — no target contact) and an active mode (DNS resolution, brute force, zone transfers that touch the target and its resolvers). Use passive for stealth; run active enumeration from a sock-puppet host and only against domains you're authorised to probe.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: The flagship OWASP asset-discovery project; widely used and community-audited. Aggregated results still include stale/dead subdomains — resolve before relying on them.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- subfinder
- crt-sh
- hosthunter
- owasp-d4n155
aliases:
- Amass
- OWASP Amass
tags:
- Domain/IP/Links
- subdomain-enumeration
- attack-surface
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# OWASP Amass

> The heavyweight of subdomain/asset discovery: give it a domain and it aggregates dozens of OSINT sources (and optional active DNS) into a full map of subdomains, IPs, and related infrastructure.

## When to use
You have a `domain` tied to a subject or organisation and need the widest possible view of its external footprint — every subdomain, the IPs and netblocks behind them, ASNs, and related domains. Amass pulls from certificate transparency, passive DNS, search engines, and more, then can actively resolve and brute-force to fill gaps. It's the go-to when a quick cert search isn't exhaustive enough. Infrastructure recon; missing-persons relevance is indirect.

## How to use it (`bestInteractionPattern`: cli)
1. Install (Go binary, Homebrew, Docker, or `snap`): e.g. `go install -v github.com/owasp-amass/amass/v4/...@master`.
2. **Passive** (stealthy, third-party sources only): `amass enum -passive -d example.com -o out.txt`.
3. **Active** (adds DNS resolution/brute force — noisier, authorised targets only): `amass enum -active -d example.com -brute`.
4. Read the output: subdomains with resolved IPs; use `amass intel` for org/ASN → domain discovery and `amass viz`/DB for relationship graphs.
5. Pivot: feed live subdomains into `[[hosthunter]]`/`[[crt-sh]]` to cross-fill, and IPs into Shodan/reverse-IP for services and neighbours.

## Inputs → Outputs
- **In:** `domain` (or an org name/ASN via `amass intel`).
- **Out:** `domain` (subdomains, related domains) and `ip-address` (resolved IPs, netblocks/ASNs).
- **Empty/negative result looks like:** few subdomains — a small footprint, aggressive rate-limiting on sources, or missing API keys. Passive-only runs miss unresolved/internal names; absence isn't proof of a small surface.

## Gotchas & OpSec
- Human-in-the-loop: none, but large enumerations take time and produce noisy results (dead/parked subdomains) that need resolving.
- OpSec: **active** modes hit the target's DNS/resolvers and can be logged or trip defences; **passive** mode touches only third parties. Choose deliberately; run active from a sock puppet and only where authorised.
- Adding free API keys to the config markedly improves coverage — worth doing for serious runs.

## Overlaps ("do both")
- Overlaps with `[[subfinder]]` — Subfinder is faster/passive-focused; run both since each source set differs, then union the results.
- Feeds `[[crt-sh]]` and `[[hosthunter]]` — cross-check cert logs and reverse-IP to confirm and extend Amass's findings.

## Trust & verifiability
`trust: trusted` — a mature, community-audited OWASP project. Discovery is reliable, but aggregated subdomains include stale entries — always resolve/verify a host before treating it as live infrastructure.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | owasp-amass |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |

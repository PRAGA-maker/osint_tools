---
id: dnsreaper
name: dnsReaper
description: Use when you have a `domain` (or a set of DNS records) and want to find subdomains vulnerable to takeover — returns the dangling `domain` names an attacker could claim.
url: https://github.com/punk-security/dnsReaper
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Fast subdomain-takeover scanning of a domain against 50+ takeover signatures.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source (AGPL-3.0, Punk Security); run via Python or Docker. Fetching records from cloud DNS providers needs your own provider API credentials.
opsec: active
opsecNote: dnsReaper resolves and probes each candidate subdomain, so it sends live requests to the target's DNS and the third-party services referenced by dangling records. That traffic is attributable — only scan domains you're authorised to test, and use a sock-puppet IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Maintained by Punk Security, a known offensive-security firm; open source and widely used in CI pipelines for takeover detection.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- punk-security/dnsReaper
tags:
- Domain/IP/Links
- Subdomains scan/brute
- takeover
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- subfinder
---

# dnsReaper

> Subdomain-takeover scanner: point it at a domain and it flags the DNS records pointing at unclaimed, hijackable services.

## When to use
You have a target `domain` and want to know which of its subdomains are vulnerable to takeover — a CNAME/record pointing at a deprovisioned cloud service (S3 bucket, Azure host, GitHub Pages, Heroku app, etc.) that an attacker could re-register and control. Useful both defensively (audit your own attack surface) and offensively (bug-bounty/recon) to find hijackable infrastructure attached to a person or organisation.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `docker run punksecurity/dnsreaper` or clone and `pip install -r requirements.txt`.
2. Provide targets: a single domain (`--domain example.com`), a file of subdomains (`--filename subs.txt`), or auto-fetch from a provider (`--provider aws`/`cloudflare`/etc. with your API keys).
3. Run — it tests ~50 subdomains/sec against 50+ takeover signatures.
4. Read the CSV/JSON output: each finding names the vulnerable `domain`, the signature matched, and confidence.
5. Pivot: confirm a flagged takeover manually before acting; feed the enumerated subdomains into further infrastructure recon.

## Inputs → Outputs
- **In:** a `domain`, a subdomain list, or DNS records fetched from a cloud provider
- **Out:** vulnerable/dangling `domain` names with the matched takeover signature (CSV/JSON)
- **Empty/negative result looks like:** no findings — no dangling records matched a known signature; not a guarantee of safety (new services appear), just no current match.

## Gotchas & OpSec
- OpSec: **active** — it probes live DNS and third-party endpoints; only scan domains you are authorised to test.
- Signatures can false-positive on services in transition; always manually confirm before reporting a takeover.
- You still need a separate tool to enumerate the subdomain list unless you let dnsReaper pull records from a provider you control.

## Overlaps ("do both")
- Pairs with `[[subfinder]]` — subfinder enumerates the full subdomain list, which you then feed into dnsReaper to test each one for takeover; discovery plus takeover-check in sequence.

## Trust & verifiability
`trust: community` — open source from a recognised security vendor and used in production CI; findings are signature-based leads that must be manually verified.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dnsreaper |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |

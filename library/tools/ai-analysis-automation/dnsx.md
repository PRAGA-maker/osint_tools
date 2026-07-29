---
id: dnsx
name: dnsx
description: Use when you have a `domain` (or a list of subdomains) and want fast, scriptable DNS resolution/brute-force — returns resolved records and the `ip-address`(es) behind each host.
url: https://github.com/projectdiscovery/dnsx
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: High-speed DNS resolution, record enumeration, and subdomain brute-forcing from the command line.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open-source (ProjectDiscovery, Go); no key required for core DNS use.
opsec: passive
opsecNote: Resolving records queries public/recursive DNS, not the target's own servers, so it is passive. Brute-forcing subdomains sends many queries to resolvers (and, for records that exist, the authoritative NS) — noisy on your own network, but not direct contact with the subject's web server. Use trusted resolvers you control.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Maintained by ProjectDiscovery, a well-known security-tooling team; open-source and widely used, actively developed.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- alertx
- cve-map
- subfinder
aliases:
- projectdiscovery/dnsx
tags:
- dns
- infrastructure-enumeration
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# dnsx

> ProjectDiscovery's fast DNS toolkit: pipe in hosts, get back records and the IPs behind them — the resolution workhorse in a subdomain-enumeration pipeline.

## When to use
You have a `domain` connected to your subject (a personal site, an org they're linked to) and want to map its DNS surface: which subdomains actually resolve, what `ip-address` they point to, and their MX/NS/TXT records. It shines as the resolver stage after a discovery tool like subfinder — turning a big candidate list into live, resolved hosts to investigate.

## How to use it (`bestInteractionPattern`: cli)
1. Install (Go 1.21+): `go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest`.
2. Resolve a subdomain list and show A records: `subfinder -silent -d example.com | dnsx -silent -a -resp`.
3. Brute-force with a wordlist: `dnsx -silent -d example.com -w dns_wordlist.txt`.
4. Extract specific records to JSON: `dnsx -l hosts.txt -json -o out.json` (add `-cname`, `-mx`, `-txt`, etc.).
5. Pivot: feed resolved `ip-address` values into reverse-IP / ASN / reputation lookups, and TXT/MX records into email-infrastructure analysis.

## Inputs → Outputs
- **In:** `domain` / subdomain list (file or stdin) + optional wordlist
- **Out:** resolved records (A/AAAA/CNAME/MX/NS/TXT/…) and the `ip-address`(es) per live host
- **Empty/negative result looks like:** hosts silently dropped (they don't resolve) — an empty output means nothing in your list is live, or your resolvers are failing.

## Gotchas & OpSec
- Passive for resolution; brute-forcing is high-volume DNS traffic — use resolvers you trust and rate-limit if needed.
- Results are only as good as your input list and wordlist; dnsx resolves, it does not discover names on its own.
- Wildcard DNS can produce false "resolved" hosts — use `-wd <domain>` wildcard filtering.

## Overlaps ("do both")
- Chains with `[[subfinder]]` (discovery → dnsx resolution) and feeds `[[cve-map]]`/`[[alertx]]`; the trio is a standard passive-recon pipeline.

## Trust & verifiability
`trust: community` — open-source and inspectable from a reputable maintainer (ProjectDiscovery); output is deterministic DNS you can independently re-query with `dig`.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dnsx |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |

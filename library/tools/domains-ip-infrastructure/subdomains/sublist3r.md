---
id: sublist3r
name: Sublist3r
description: Use when you have a `domain` and want to enumerate its subdomains — returns a consolidated list of subdomains from search engines, cert data and optional brute-force.
url: https://github.com/aboul3la/Sublist3r
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- subdomains
bestFor: Fast first-pass subdomain enumeration for a domain, combining passive OSINT sources with optional brute-force.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source (MIT); run locally with Python.
opsec: passive
opsecNote: The default (passive) mode only queries third-party sources — Google, Bing, VirusTotal, Netcraft, etc. — so it doesn't touch the target. The optional `-b` brute-force mode sends DNS queries that can be logged; skip it if you need to stay quiet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular, long-standing tool (11k+ stars) but only lightly maintained now (Python 2.7/3.4 era). Reliable for a quick pass; modern engines find more.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- amass
aliases: []
tags:
- subdomain-enumeration
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# Sublist3r

> A quick Python subdomain enumerator — point it at a domain and it harvests subdomains from search engines, cert data and passive DNS, with optional brute-force.

## When to use
You have a `domain` tied to a subject or organisation and want to map its attack/footprint surface — subdomains often expose staging sites, mail/VPN/admin hosts, old projects and personal side-domains that reveal more about the owner. A fast first pass before reaching for heavier tooling. Infrastructure-focused; low direct missing-persons relevance.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and install: `git clone https://github.com/aboul3la/Sublist3r && pip install -r requirements.txt`.
2. Passive run: `python sublist3r.py -d example.com` (queries OSINT sources only).
3. Add brute-force if you accept the noise: `python sublist3r.py -b -d example.com`.
4. Use `-v` for real-time output and `-o out.txt` to save.
5. Pivot: each subdomain → resolve to IPs, fingerprint the stack, or check for exposed panels; unexpected hosts hint at the owner's other projects.

## Inputs → Outputs
- **In:** `domain`
- **Out:** a consolidated list of `domain` subdomains
- **Empty/negative result looks like:** few/no subdomains — the domain is small/new, or (common) some upstream search sources rate-limited or blocked the queries. Re-run and cross-check with a modern enumerator before concluding.

## Gotchas & OpSec
- Human-in-the-loop: none, but search-engine sources frequently rate-limit/CAPTCHA, thinning results.
- OpSec: **passive** by default; the `-b` brute-force is **active** DNS and detectable — choose deliberately.
- The project is dated and less maintained; treat its output as a baseline, not comprehensive.

## Overlaps ("do both")
- Pairs with `[[amass]]` — Amass is the deeper, actively-maintained enumerator; run Sublist3r for a quick look and Amass for thorough coverage, then union the results.

## Trust & verifiability
`trust: community` — a well-known open-source tool; results are real subdomains but coverage is partial and source-dependent, so verify completeness with a second engine.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sublist3r |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |

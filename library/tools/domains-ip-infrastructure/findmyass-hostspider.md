---
id: findmyass-hostspider
name: HostSpider (FindMyAss)
description: Use when you have a `domain` and want a one-shot recon dump — returns subdomains, DNS records, WHOIS data, and Cloudflare detection.
url: https://github.com/h3x0crypt/HostSpider
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: A fast local first-pass on a domain that bundles subdomain discovery, DNS, and WHOIS into one command.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
- email
- name
- address
status: degraded
pricing: free
costNote: Free and open source (MIT); the GitHub repo is archived/read-only, so install and run it locally.
opsec: active
opsecNote: HostSpider actively queries DNS, WHOIS, and enumerates subdomains against the target's infrastructure — these lookups can appear in the target's DNS/authoritative logs. Run from a VPN/attributable-free host, and prefer passive sources first if you need to stay quiet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Community-authored open-source tool, unmaintained since it was archived in 2022; the code is auditable but some data sources it queries may have changed — verify anything critical with a current tool.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- HostSpider
- FindMyAss
tags:
- domain-recon
- subdomains
- dns
- whois
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# HostSpider (FindMyAss)

> A small Python CLI that bundles subdomain discovery, DNS-record collection, WHOIS, and Cloudflare detection into a single recon pass against a domain.

## When to use
You have a `domain` and want a quick, scriptable first look at its infrastructure without opening five separate web tools. HostSpider gathers subdomains, DNS records (A, AAAA, NS, MX, SOA, TXT), and WHOIS in one run — WHOIS in particular can surface a registrant `name`, `email`, and `address` when the domain isn't privacy-protected.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo: `git clone https://github.com/h3x0crypt/HostSpider` (it's archived but still clonable).
2. Install dependencies: `pip install -r requirements.txt` (Python 3.9).
3. Run it: `python3 FindMyAss.py` and supply the target `domain`.
4. Review the report: subdomains and DNS records map the target's hosts and mail setup; the WHOIS block may expose registrant `name`/`email`/`address`; Cloudflare detection tells you whether the real origin IP is hidden.
5. Pivot: feed discovered subdomains/`ip-address`es into IP-reputation and port tools, and any registrant `email`/`name` into people/email OSINT.

## Inputs → Outputs
- **In:** `domain`
- **Out:** subdomains and `domain`s, `ip-address`es, DNS records, and WHOIS-derived `name`/`email`/`address`
- **Empty/negative result looks like:** few/no subdomains and a privacy-redacted WHOIS ("REDACTED FOR PRIVACY", registrar proxy) — means the target uses WHOIS privacy and a small footprint, not that the tool failed.

## Gotchas & OpSec
- Human-in-the-loop: none, but you must install it locally (`localInstall: true`).
- OpSec: **active** — DNS/WHOIS queries and subdomain enumeration touch the target's infrastructure and can be logged. Run behind a VPN and consider passive alternatives first.
- Archived in 2022 and unmaintained: dependencies or upstream data sources may have drifted. Confirm important findings with a currently-maintained recon tool.

## Overlaps ("do both")
- Pairs with passive DNS / certificate-transparency search — HostSpider actively enumerates while CT logs and passive DNS reveal historical and hidden subdomains without touching the target; combine for both coverage and stealth.

## Trust & verifiability
`trust: community` — auditable open-source code, but stale; the raw DNS/WHOIS it returns is verifiable against a live lookup, which you should do for anything you rely on.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | findmyass-hostspider |

---
id: raymond
name: Raymond
description: Use when you have a `domain` and want a scripted first-pass recon sweep from the CLI — returns DNS/WHOIS, subdomains and related hosts pulled via HackerTarget's API.
url: https://github.com/hamza07-w/raymond
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-command CLI website recon (DNS, WHOIS, subdomains) via the HackerTarget API.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free open-source Python script; requires a free HackerTarget API key, whose free tier is rate-limited (a few hundred queries/day).
opsec: passive
opsecNote: Lookups run through HackerTarget's servers, not directly from you to the target, so the target doesn't see your IP — but HackerTarget sees every domain you query and ties it to your API key. Use a dedicated key for investigations you want compartmentalized.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: unverified
trustNote: A small individual GitHub project (few dozen stars) that wraps the HackerTarget API; the data quality is HackerTarget's, the convenience is the script's.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
relatedTools: []
aliases:
- raymond recon
tags:
- Domain/IP/Links
- Domain/IP investigation
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Raymond

> A small Python CLI that wraps the HackerTarget API to run a quick website-recon sweep — DNS, WHOIS, subdomains and related hosts — from one command.

## When to use
You have a `domain` and want a fast, scriptable first look at its infrastructure without opening a browser: DNS records, WHOIS, subdomain enumeration and reverse-lookup style pivots. It's a convenience front-end over HackerTarget's hosted lookups — good for automation or when you want CLI output you can pipe.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo: `git clone https://github.com/hamza07-w/raymond`.
2. Register for a free HackerTarget API key and paste it into the script where indicated.
3. Install Python 3 and run: `python3 raymond(lin).py -u <domain>` (or the `(win)` variant on Windows).
4. Read the output — DNS records, WHOIS, discovered subdomains and associated `ip-address`es.
5. Pivot: feed subdomains/IPs into passive-DNS, certificate-transparency or WHOIS-history tooling for deeper mapping.

## Inputs → Outputs
- **In:** `domain`
- **Out:** DNS records, WHOIS data, subdomains, related `ip-address`es
- **Empty/negative result looks like:** empty sections or an API error — often the HackerTarget free-tier rate limit was hit, or the record type isn't set; retry later or check quota rather than concluding the asset is empty.

## Gotchas & OpSec
- Human-in-the-loop: you must obtain and insert a HackerTarget API key before it runs.
- OpSec: **passive** toward the target (HackerTarget queries on your behalf), but HackerTarget logs your queries against your key.
- Free-tier rate limits cap how much you can pull per day; heavy enumeration will throttle.

## Overlaps ("do both")
- Use alongside dedicated subdomain enumerators and certificate-transparency search — Raymond gives a quick HackerTarget-backed sweep; those find hosts HackerTarget's dataset misses.

## Trust & verifiability
`trust: unverified` — a small individual project; verify results against the underlying HackerTarget lookups or a second recon source before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | raymond |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |

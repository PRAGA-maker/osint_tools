---
id: webosint
name: WEBOSINT
description: Use when you have a `domain` and want a guided, step-by-step passive recon sweep (WHOIS, DNS, reverse-IP, certs, subdomains) — returns domain, ip-address and geolocation detail.
url: https://github.com/C3n7ral051nt4g3ncy/webosint
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Interactive, single-domain passive reconnaissance walkthrough in Python.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
- geolocation
status: live
pricing: freemium
costNote: The script is free/open-source. It calls HackerTarget (optional key), WhoisXML API and WhoisFreaks — the latter two need API keys (free trial tiers available); a "free" run mode limits some steps.
opsec: passive
opsecNote: Passive toward the subject — it queries third-party WHOIS/DNS/cert services, not the target's server directly. Note that your queried domains are seen by those upstream APIs (HackerTarget, WhoisXML, WhoisFreaks), so use research-only API keys.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: unverified
trustNote: Small single-author OSINT script (C3n7ral051nt4g3ncy); functional but not widely audited — verify outputs against the underlying services.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
relatedTools:
- curl-for-osint
- masto
- osint-tactical
- prot1ntelligence
- whatsmyname-python
aliases:
- webosint.py
tags:
- Domain/IP/Links
- Dorks/Pentest/Vulnerabilities
- domain-recon
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# WEBOSINT

> A Python CLI that walks you through passive domain reconnaissance one step at a time, wiring together HackerTarget, WhoisXML and WhoisFreaks.

## When to use
You have a single `domain` (for example a website tied to a subject, business, or scam) and want a structured passive sweep — registration/WHOIS, IP geolocation, reverse-IP neighbours, DNS records, certificate transparency (crt.sh), reputation, subdomains, and historical WHOIS — without manually visiting each service. Best for domain/infrastructure work rather than direct people-finding.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and install requirements, or run the container: `docker run -it scorpix06/webosint`.
2. Obtain the API keys it expects (WhoisXML, WhoisFreaks — free trials; HackerTarget key optional). This is the human-in-the-loop gate.
3. Run `python3 webosint.py`; it prompts interactively for the target `domain` and whether to use the free or paid API path.
4. Step through the modules: WHOIS → IP geolocation → reverse IP → DNS → crt.sh certs → reputation → subdomains → historical WHOIS.
5. Pivot: reverse-IP neighbours and subdomains feed further domain mapping; historical WHOIS can surface an earlier, un-redacted registrant name/email.

## Inputs → Outputs
- **In:** `domain`
- **Out:** `domain` (WHOIS, subdomains, certs), `ip-address` (hosting + reverse-IP neighbours), `geolocation` (IP-level)
- **Empty/negative result looks like:** redacted/privacy WHOIS, empty reverse-IP set (dedicated host), or an API-key/quota error on the WhoisXML/WhoisFreaks steps.

## Gotchas & OpSec
- Human-in-the-loop: mandatory API keys for WhoisXML and WhoisFreaks (`api-key`); free trials are limited.
- OpSec: passive — the subject's server is not hit directly, but each queried domain is visible to the upstream APIs; use dedicated research keys.
- It is a thin orchestrator over third-party APIs, so its accuracy and freshness are only as good as those services on the day.

## Overlaps ("do both")
- Pairs with `[[curl-for-osint]]` and `[[osint-tactical]]` for manual verification of individual records, and with `[[whatsmyname-python]]` once you pivot from a domain to a username/identity.

## Trust & verifiability
`trust: unverified` — a small, single-maintainer script; treat it as a convenience wrapper and confirm any actionable WHOIS/DNS/cert finding directly against the authoritative source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | webosint |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address, geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |

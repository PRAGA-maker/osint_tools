---
id: domain-intelligence
name: Domain Intelligence
description: Use when you have a `domain` and want WHOIS/DNS/SSL/subdomains/email-security in one JSON call — returns registration, records, certs, subdomains and SPF/DMARC posture.
url: https://oti-labs.com/domain-intelligence-api
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-call aggregated domain reconnaissance (WHOIS/RDAP, DNS, SSL, subdomains, email-auth) via a REST API.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
- email
status: live
pricing: freemium
costNote: Freemium via RapidAPI — free tier ~1,000 requests/month, no credit card; paid tiers $9.99–$149.99/month for higher volume.
opsec: passive
opsecNote: Queries go to the API provider (and are edge-cached), so the provider sees which domains you research — not the domain owner. It performs passive lookups (WHOIS/DNS/cert transparency), so it doesn't touch the target's servers directly; use an API key tied to a non-attributable account.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: api
trust: community
trustNote: A third-party aggregation API (Osiris Technical Institute) distributed on RapidAPI; the underlying data (WHOIS/DNS/CT) is authoritative, but you're trusting their aggregation/normalisation layer.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- OTI Domain Intelligence API
- oti-labs domain intelligence
tags:
- domain
- dns
- whois
- api
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Domain Intelligence

> One REST call that returns everything passive about a domain — WHOIS/RDAP, DNS records, SSL certificate details, subdomain enumeration, and an SPF/DMARC/DKIM audit — as normalised JSON.

## When to use
You have a `domain` tied to a subject or organisation and want the standard passive footprint fast and machine-readable: who registered it, its DNS and mail setup, its certificate history and SANs (which often leak related hostnames), and its subdomains. Good for scripting domain enrichment into a larger pipeline.

## How to use it (`bestInteractionPattern`: api)
1. Get an API key from the RapidAPI listing linked at https://oti-labs.com/domain-intelligence-api (free tier, no card).
2. Call the endpoint with the target `domain`; try the site's live demo first to see the response shape.
3. Parse the JSON: WHOIS/RDAP registrant data, A/AAAA/MX/NS/TXT/CAA/SOA records, SSL issuer/validity/SANs, subdomains, and email-auth (SPF/DMARC/DKIM) findings.
4. Pivot: SAN entries and subdomains reveal related `domain`s/hosts; MX/DNS point to providers; registrant fields (if not privacy-masked) can yield `email`/`name` leads.

## Inputs → Outputs
- **In:** `domain`
- **Out:** `domain` (subdomains/SANs), `ip-address` (DNS), `email` (registrant/abuse where exposed)
- **Empty/negative result looks like:** privacy-masked WHOIS and no extra subdomains means the owner is well-hidden — lean on the certificate/DNS data and passive-DNS history instead.

## Gotchas & OpSec
- Human-in-the-loop: requires registering for an API key (`api-key`).
- Free tier is capped (~1,000/month) — fine for manual work, plan for paid tiers if you script at scale.
- It's an aggregator — spot-check critical fields against primary sources (RDAP, crt.sh) before relying on them.

## Overlaps ("do both")
- Overlaps with crt.sh (certs), SecurityTrails/passive-DNS, and WHOIS tools individually; Domain Intelligence bundles them into one call — use it for speed, the primaries for authoritative confirmation.

## Trust & verifiability
`trust: community` — a third-party API over authoritative data sources; the raw signals (WHOIS/DNS/CT) are solid, so verify anything pivotal directly at the source when it matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | domain-intelligence |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address, email |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | api |
| opsec | passive |
| human-in-loop | yes (api-key) |

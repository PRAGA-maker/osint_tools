---
id: iqwhois
name: IQWhois
description: Use when you have a `name`, `address`, `phone`, `email`, or `employer-org` and want to reverse-search WHOIS records for domains registered with those details — returns matching `domain`s and their full registrant records.
url: https://iqwhois.com/advanced-search
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Reverse WHOIS — finding every domain a person or organisation registered, pivoting from personal details rather than a domain name.
selectorsIn:
- name
- email
- phone
- address
- employer-org
selectorsOut:
- domain
- email
- phone
- address
status: live
pricing: freemium
costNote: Advanced multi-field search is usable with a free account; bulk WHOIS-database and WHOIS-history downloads are separate paid products. Free-tier results and quotas are capped.
opsec: passive
opsecNote: You query IQWhois's own historical WHOIS index, not the target's infrastructure, so the subject is never contacted or alerted. You do reveal your search terms to IQWhois and must create an account, so register with a research identity, not your real one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party aggregator of historical WHOIS data; useful but data can be stale (registrant privacy/redaction post-GDPR) and completeness is not guaranteed — corroborate hits against live WHOIS.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- IQ Whois
- iqwhois advanced search
tags:
- whois
- reverse-whois
- domains
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# IQWhois

> A reverse-WHOIS search engine: instead of "who owns this domain?", ask "what domains did this person/phone/address register?"

## When to use
You have a personal or organisational selector — a `name`, `email`, `phone`, postal `address`, or `employer-org` — and want to find domains registered with those details. This is the inverse of normal WHOIS and a strong pivot: a person's domain registrations expose the email, phone, and address they used, which can tie aliases together, reveal a current contact point, or link a subject to a business. Reach for it when a domain lead is missing but you have identity details, or when you want to expand from one known domain to the registrant's whole portfolio.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a free account and open https://iqwhois.com/advanced-search.
2. Fill one or more of the registrant fields — Name, Organization, Email, Street, City, State, Postal Code, Country, Telephone, Fax — optionally scoping to a WHOIS section (Registrant / Admin / Technical / Billing).
3. Submit. Keep filters balanced: too many returns nothing, too few returns millions.
4. Read the result set: each hit is a `domain` plus its recorded registrant `email`/`phone`/`address`.
5. Pivot: a returned email/phone becomes the seed for further reverse searches and email/phone OSINT; a returned domain feeds infrastructure and site-history tools.

## Inputs → Outputs
- **In:** `name`, `email`, `phone`, `address`, or `employer-org`
- **Out:** `domain`, plus the associated registrant `email`, `phone`, `address`
- **Empty/negative result looks like:** "no results" (often from over-filtering, or because the registrant used WHOIS privacy/redaction) — loosen filters and remember post-GDPR records are frequently masked, so absence is not proof.

## Gotchas & OpSec
- Human-in-the-loop: an account (`account-login`) is required to run advanced searches.
- Data currency: much WHOIS is redacted since GDPR; IQWhois leans on historical records, so hits may be years old — always confirm against live WHOIS before relying on a value.
- Free tier is quota-limited; the full/bulk database is a paid upsell.

## Overlaps ("do both")
- Complements forward-WHOIS and domain-history tools: use IQWhois to go *from a person to their domains*, then a live WHOIS/DNS-history tool to see the current state and ownership of each domain it surfaces.

## Trust & verifiability
`trust: community` — a useful third-party WHOIS aggregator, but completeness and freshness aren't guaranteed and privacy redaction limits coverage; treat results as leads to verify, not as authoritative registration records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | iqwhois |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | name, email, phone, address, employer-org → domain, email, phone, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |

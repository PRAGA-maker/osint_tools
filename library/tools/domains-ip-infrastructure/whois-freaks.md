---
id: whois-freaks
name: Whois Freaks
description: Use when you have a person `name`, company, or email and want every domain registered with those details — returns matching `domain`s via reverse-WHOIS (430M+ domains since 1986).
url: https://whoisfreaks.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Reverse-WHOIS — finding all domains linked to a registrant name, company, or email.
selectorsIn:
- name
- email
- employer-org
selectorsOut:
- domain
status: live
pricing: freemium
costNote: 500 free credits on signup; heavier/bulk use is paid via tiered API plans. Data in JSON/XML.
opsec: passive
opsecNote: You query WhoisFreaks' historical WHOIS database, not the registrant — passive, no signal to the target. You do log into a third-party account, so use a sock-puppet registration.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: api
trust: community
trustNote: Commercial WHOIS/DNS data vendor; large historical corpus, but registrant data is increasingly redacted by GDPR/privacy so coverage skews to older/business registrations.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
aliases:
- WhoisFreaks
tags:
- domains-ip-infrastructure
- whois
- reverse-whois
- api
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Whois Freaks

> A reverse-WHOIS engine over 430M+ domains back to 1986 — turn a registrant name, email, or company into the list of domains they registered.

## When to use
You have a subject's `name`, `email`, or company `employer-org` and want to find every `domain` registered with those details — a classic pivot from a person to their web infrastructure (personal sites, businesses, past projects). Also useful for current + historical WHOIS on a known domain.

## How to use it (`bestInteractionPattern`: api)
1. Register at https://whoisfreaks.com/ (500 free credits) and get an API key.
2. Call the Reverse WHOIS API (or use the web lookup) with the registrant `name`, `email`, or company as the query.
3. Parse the JSON/XML: matching domains, plus registration/expiry dates and contacts where available.
4. Pivot: each returned `domain` feeds live WHOIS, DNS, and content review; a cluster of domains around one registrant maps the subject's online footprint.

## Inputs → Outputs
- **In:** registrant `name`, `email`, or `employer-org` (or a `domain` for forward WHOIS/history)
- **Out:** matching `domain`s with registration metadata
- **Empty/negative result looks like:** no domains returned — the registrant used WHOIS privacy/redaction (very common post-GDPR), a different identity, or simply owns none in the corpus.

## Gotchas & OpSec
- Reverse-WHOIS is only as good as unredacted records; modern registrations are frequently privacy-protected, so expect gaps for recent/personal domains.
- Free credits are limited; bulk work needs a paid plan.
- Requires an account/API key — register with a sock puppet.

## Overlaps ("do both")
- Pairs with `[[viewdns-info]]`/`[[whoxy]]`-style reverse-WHOIS and historical-WHOIS tools — cross-check across providers because each corpus and redaction handling differs.

## Trust & verifiability
`trust: community` — an established commercial data vendor; the domain data is generally reliable but registrant attribution is limited by privacy redaction, so corroborate ownership before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whois-freaks |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | name, email, employer-org → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | api |
| opsec | passive |
| human-in-loop | yes (api-key) |

---
id: reversewhois-io
name: reversewhois.io
description: Use when you have a registrant `name` or `email` and want every domain registered with it — returns the list of `domain`s tied to that registrant.
url: https://www.reversewhois.io/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Reverse WHOIS — finding all domains owned by a person or company from their name or email.
selectorsIn:
- name
- email
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free reverse-WHOIS search in the browser; the free view shows a capped list of results, with fuller/exportable results behind a paid tier.
opsec: passive
opsecNote: Queries hit reversewhois.io's historical WHOIS index, not the domains or their owners — the subject is not alerted. Nothing you search is exposed to the registrant.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party reverse-WHOIS service drawing on historical WHOIS records; useful but not authoritative — records predate GDPR redaction unevenly, so coverage is partial. Corroborate before attributing ownership.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- reverse whois io
tags:
- domainsandips
- Domains & IPs
- reverse-whois
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# reversewhois.io

> Reverse WHOIS in one box — put in a name or email, get back every domain that WHOIS ever tied to it.

## When to use
You have a registrant `name` or an `email` (from a WHOIS record, a data breach, or a subject's known address) and you want to find the *other* domains that same identity registered. This is a classic pivot for uncovering a person's or company's wider web presence — sock-puppet sites, old ventures, related infrastructure — that share the same registrant details.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.reversewhois.io/.
2. Enter a registrant `name` (as it would appear in WHOIS, e.g. "John Smith") or an `email` address.
3. Read the results: a list of `domain`s whose historical WHOIS records contain that name/email.
4. Note the free view is capped — for a large owner you'll see a subset. Prioritise the domains that matter, then WHOIS each directly to confirm the match.
5. Pivot: each recovered `domain` → full WHOIS, DNS/host history, and Wayback for what the site was; a shared registrant across several domains strengthens attribution.

## Inputs → Outputs
- **In:** registrant `name` or `email`
- **Out:** list of `domain`s associated with that registrant in historical WHOIS
- **Empty/negative result looks like:** no domains, or only weak partial-name matches — because modern WHOIS redacts registrant data (GDPR/privacy proxies), recently registered domains often carry no name/email to match. A blank result is not proof the person owns no domains.

## Gotchas & OpSec
- Coverage skews to **pre-redaction** records; privacy-protected and post-GDPR registrations are frequently invisible here. Combine with breach-sourced emails to catch more.
- Common names return noisy matches — verify each candidate domain's actual WHOIS/content before attributing ownership.
- The free tier caps results and hides export; treat it as a sampling tool, not an exhaustive list.

## Overlaps ("do both")
- Do both with other reverse-WHOIS / passive-DNS sources (ViewDNS, WhoisXML, SecurityTrails) — each has a different historical corpus, so running several catches domains any single index misses. Feed recovered domains into the rest of your domain-OSINT chain.

## Trust & verifiability
`trust: community` — a third-party aggregator of historical WHOIS; results are leads drawn from records of uneven completeness, not an authoritative ownership registry. Always confirm a candidate domain's own WHOIS before relying on the link.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reversewhois-io |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | name, email → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

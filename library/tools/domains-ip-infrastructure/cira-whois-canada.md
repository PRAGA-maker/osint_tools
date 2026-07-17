---
id: cira-whois-canada
name: CIRA WHOIS (Canada)
description: Use when you have a `.ca` `domain` and want its authoritative registration record — returns registrar, status, and (where not privacy-redacted) registrant details from Canada's official registry.
url: https://cira.ca/ca-domains/whois
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Authoritative WHOIS for Canadian .ca domains, direct from the registry (CIRA).
selectorsIn:
- domain
selectorsOut:
- domain
- name
- email
status: live
pricing: free
costNote: Free public WHOIS run by CIRA, the .ca registry. No account or key; a CAPTCHA gates each lookup.
opsec: passive
opsecNote: The query goes to CIRA's registry, not the target's website, so the domain owner is not alerted. CIRA sees your IP and rate-limits/CAPTCHAs abusive use. Individual .ca registrant contact info is redacted by default under CIRA privacy; organization registrants may still be shown.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: CIRA is the official registry operator for the .ca TLD; this is the authoritative source for .ca registration data.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- team-cyru-ip-to-asn-lookup
- viewdns-info
- whoxy
aliases:
- CIRA WHOIS
- .ca whois
tags:
- toddington
- curated-directory
- whois-ip-lookups-website-analysis
- canada
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# CIRA WHOIS (Canada)

> The official WHOIS service of CIRA, operator of the `.ca` TLD — the authoritative place to look up registration data for any Canadian domain.

## When to use
You have a `.ca` `domain` and want its registration record straight from the source rather than a third-party mirror. For organization-registered `.ca` domains this can still expose the registrant `name`/`email` and admin contacts; for individual registrants CIRA redacts personal details by default, but you still get registrar, creation/expiry dates, status, and nameservers — enough to characterize the domain and pivot on its infrastructure.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://cira.ca/ca-domains/whois and enter the `.ca` domain.
2. Solve the CAPTCHA and submit.
3. Read the record: registrar, domain status, registration/expiry dates, nameservers, and — for organizations or non-private registrants — the registrant `name`/`email` and contacts.
4. If contact details are redacted ("Registrant privacy"), note the registrar and nameservers instead and pivot via DNS/hosting.
5. Pivot: an org registrant → Canadian corporate registries; nameservers → hosting clustering; any exposed email → email-OSINT tools.

## Inputs → Outputs
- **In:** `domain` (`.ca` only)
- **Out:** `domain` record (registrar, dates, status, nameservers) and, when not redacted, registrant `name` / `email`
- **Empty/negative result looks like:** "Domain status: available" / no record — the domain isn't registered — or a record with all contact fields showing "Registrant privacy," meaning an individual registrant whose details CIRA withholds.

## Gotchas & OpSec
- Only works for `.ca`; use the relevant registry/WHOIS for other TLDs.
- Individual-registrant privacy is the default under CIRA policy, so blank contact fields are expected, not a lookup failure — organizations are more likely to be visible.
- Human-in-the-loop: a CAPTCHA is required per lookup. OpSec: **passive** — the registry query never touches the target's site.

## Overlaps ("do both")
- Pairs with `[[whoxy]]` and `[[viewdns-info]]` — those add historical/reverse WHOIS (including pre-privacy `.ca` records) that the live CIRA record no longer shows, so run both for current + historical ownership.

## Trust & verifiability
`trust: trusted` — CIRA is the official `.ca` registry, so the record is authoritative; only the *completeness* is limited by privacy redaction, not the accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cira-whois-canada |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, name, email |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |

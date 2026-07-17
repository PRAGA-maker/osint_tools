---
id: godaddy-com
name: godaddy.com
description: Use when you have a `domain` and want its WHOIS registration and availability — returns registrar, dates, name servers, and (where public) registrant contact.
url: https://www.godaddy.com/en-ca/whois
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Quick WHOIS lookups — registrar, registration/expiry dates, name servers, and any public registrant details for a domain.
selectorsIn:
- domain
selectorsOut:
- domain
- name
- email
status: live
pricing: free
costNote: Free WHOIS lookup; GoDaddy is a registrar, so the page also upsells domain purchases, but the WHOIS query itself is free.
opsec: passive
opsecNote: A WHOIS query reads public registry data and doesn't touch the domain's live server or notify the owner. Passive. (GoDaddy may show a CAPTCHA on repeated lookups.)
humanInLoop: false
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: GoDaddy is the world's largest domain registrar; its WHOIS reflects authoritative registry data, though registrant details are often masked by privacy services.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- whois
- icann-lookup
- whoisxmlapi
- cyclect
- godaddy
- godaddy-whois-lookup
aliases:
- GoDaddy WHOIS
- godaddy whois lookup
tags:
- domainsandips
- Domains & IPs
- whois
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# godaddy.com

> The world's biggest registrar's WHOIS lookup — a fast way to pull a domain's registration record and check availability.

## When to use
You have a `domain` tied to a case (a subject's site, a scam page, a business) and want its WHOIS: who registered it, when, through which registrar, on what name servers, and whether registrant contact is public. GoDaddy's WHOIS is a convenient front-end; note that most registrant details are now masked by privacy/redaction, so this is often a starting point rather than a source of a real name.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.godaddy.com/whois (or /en-ca/whois) and enter the domain.
2. Read the record: registrar, creation/updated/expiry dates, name servers, registrant org/contact if unredacted.
3. Solve a CAPTCHA if prompted on repeated queries.
4. If contact is privacy-masked (common), note the registrar and dates — still useful for correlation and for a possible registrar/legal request.
5. Pivot: name servers/registrar → hosting and related domains; any real email/name → email- and name-OSINT; for historical (pre-privacy) records use `[[whoisxmlapi]]`/WHOIS history tools.

## Inputs → Outputs
- **In:** a `domain`
- **Out:** registrar, registration/expiry dates, name servers, and public registrant `name`/`email` where not redacted
- **Empty/negative result looks like:** "available"/no record (domain unregistered), or a fully privacy-redacted record showing only the registrar and dates — the real registrant is masked, not absent.

## Gotchas & OpSec
- GDPR/registrar privacy masks most registrant PII now — expect redaction; the value is often the metadata (dates, name servers, registrar), not a name.
- It's a registrar site with purchase upsell; ignore the buy prompts.
- CAPTCHAs appear on repeated lookups — for bulk/automated WHOIS use a dedicated WHOIS tool/API.

## Overlaps ("do both")
- Pairs with `[[whois]]` and `[[icann-lookup]]` — authoritative registry WHOIS without the registrar upsell; cross-check the same domain.
- Pairs with `[[whoisxmlapi]]` for WHOIS *history*, which can reveal pre-redaction registrant details.

## Trust & verifiability
`trust: trusted` — GoDaddy is a major, legitimate registrar and its WHOIS reflects real registry data. The record is authoritative; redaction limits what registrant detail you can see, not the accuracy of what's shown.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | godaddy-com |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, name, email |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |

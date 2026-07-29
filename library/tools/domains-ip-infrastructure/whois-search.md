---
id: whois-search
name: Verisign WHOIS Search
description: Use when you have a `domain` and want authoritative registration data — returns registrar, registration/expiry dates, name servers, and EPP status.
url: https://webwhois.verisign.com/webwhois-ui/index.jsp?language=en_US
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Authoritative WHOIS lookups for .com/.net (and other) domains from the registry operator itself.
selectorsIn:
- domain
selectorsOut:
- domain
- name
status: live
pricing: free
costNote: Free public WHOIS from Verisign; no account. Registrar-level detail comes from the sponsoring registrar's WHOIS/RDAP.
opsec: passive
opsecNote: A standard WHOIS query to the registry — you don't contact the domain's owner or their servers, and no alert is generated. Verisign may rate-limit or CAPTCHA abusive query volumes. Registrant personal data is usually redacted post-GDPR.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Verisign is the registry operator for .com and .net — this is authoritative registry WHOIS, not a third-party reseller cache.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- whois-domaintools
- whoxy
- viewdns-info
- verisign-whois-lookup
aliases:
- Verisign WHOIS
- webwhois.verisign.com
tags:
- whois
- domain-registration
- dns
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Verisign WHOIS Search

> Registry-authoritative WHOIS for .com/.net — look up a domain's registration facts straight from the operator, not a third-party cache.

## When to use
You have a `domain` tied to your subject and want its registration record: sponsoring registrar, creation/expiry/updated dates, name servers, and EPP status codes. Use Verisign's WHOIS when you want the authoritative registry answer (especially to confirm registrar and dates), then follow the registrar link for any further detail.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://webwhois.verisign.com/webwhois-ui/index.jsp.
2. Enter the `domain` and submit (solve a CAPTCHA if prompted for heavier use).
3. Read the record: registrar, key dates, name servers, and EPP status (e.g. `clientTransferProhibited`, `serverHold`).
4. For registrant/contact detail (usually redacted), follow the sponsoring registrar's own WHOIS/RDAP.
5. Pivot: name servers and registrar feed hosting/infrastructure mapping; registration dates corroborate a domain's age and timeline; historical WHOIS tools recover pre-redaction owners.

## Inputs → Outputs
- **In:** `domain`
- **Out:** registrar, creation/expiry/updated dates, name servers, EPP status; occasionally registrant `name`/org if not redacted
- **Empty/negative result looks like:** "No match for domain" — the name is unregistered (or in a TLD this registry doesn't operate); use the relevant TLD registry/registrar WHOIS instead.

## Gotchas & OpSec
- Post-GDPR, registrant contact fields are typically redacted here — for current owner detail you often need the registrar, RDAP, or historical-WHOIS services.
- Registry WHOIS is thin by design (registrar + status + dates); the sponsoring registrar holds the fuller record.
- Heavy automated querying gets rate-limited/CAPTCHA'd; use a WHOIS/RDAP API for bulk work.

## Overlaps ("do both")
- Pairs with `[[whois-domaintools]]` / `[[whoxy]]` (historical WHOIS, reverse-WHOIS by registrant) and `[[viewdns-info]]` (reverse-IP, DNS). Do both: Verisign for the authoritative current record, the others for history and pivots the registry doesn't expose.

## Trust & verifiability
`trust: trusted` — first-party registry data, authoritative for .com/.net registration facts. Contact fields may be redacted; verify owner attribution via historical/registrar sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whois-search |

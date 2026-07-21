---
id: weare-ie
name: .ie Domain Registry (weare.ie)
description: Use when you have an Irish `.ie` `domain` and want registry-backed WHOIS and registrar details — returns registration status, registrar, and (limited) registrant information.
url: https://www.weare.ie/privacy-policy/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Authoritative WHOIS and registrar lookup for Ireland's .ie country-code domains.
selectorsIn:
- domain
selectorsOut:
- domain
- employer-org
status: live
pricing: free
costNote: Free WHOIS/registrar lookup on the registry site; registering or managing domains involves accredited registrars and fees, but lookups are free.
opsec: passive
opsecNote: A WHOIS query hits the registry, not the domain owner; the registrant is not notified. Registrant personal data is minimized under the registry's privacy policy, so expect limited detail.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: weare.ie is the operator of Ireland's national .ie registry (formerly IEDR); authoritative for .ie registration data.
missingPersonsRelevance: medium
coverage:
- ie
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- whois-arin
- arin-net
aliases:
- weare.ie
- .ie registry
- IEDR
tags:
- domainsandips
- Domains & IPs
- whois
- ireland
source: uk-osint
lastVerified: '2026-07-21'
enrichment: full
---

# .ie Domain Registry (weare.ie)

> The authoritative operator of Ireland's `.ie` domain space — the source of truth for whether a `.ie` domain is registered, by which registrar, and what limited registrant data is public.

## When to use
Your investigation touches an Irish `.ie` domain and you want registry-grade facts rather than a third-party WHOIS cache. weare.ie (formerly IEDR) runs the .ie namespace, so its lookup gives the definitive registration status, the accredited registrar behind the domain, and dates. Historically .ie required a real Irish connection to register, so a `.ie` domain can itself be a signal that the registrant is a real Irish person or business.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to weare.ie and open its WHOIS / domain lookup (the site also hosts policy pages such as the privacy policy linked here).
2. Enter the `.ie` `domain`.
3. Read the result: registration status, registrar, key dates, and any public registrant fields.
4. If the registrant is redacted, note the registrar and pivot to it, or use the domain's website/mail records for further leads.
5. Pivot: the registrar and any org name feed corporate registries; mail/host records feed DNS/IP OSINT.

## Inputs → Outputs
- **In:** an Irish `.ie` `domain`
- **Out:** registration status, registrar, dates, and (often minimized) registrant `employer-org`/contact fields
- **Empty/negative result looks like:** "not registered / available" (the domain isn't taken) or a record with registrant personal data withheld under privacy rules — expected, not an error.

## Gotchas & OpSec
- Registrant personal data is deliberately minimized under the registry's privacy policy; you'll often get only registrar + status.
- Scope is strictly `.ie`; other TLDs need their own registry/WHOIS.
- OpSec: passive; the owner isn't alerted.

## Overlaps ("do both")
- Pairs with generic WHOIS/RDAP and the Irish company register — the registry gives authoritative .ie status, those add historical records and the business behind an org name.

## Trust & verifiability
`trust: trusted` — weare.ie is the national .ie registry operator itself, so its registration data is authoritative for that namespace.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | weare-ie |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

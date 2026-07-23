---
id: icann-lookup
name: ICANN Lookup
description: Use when you have a `domain` and want its authoritative registration data — returns the official RDAP/WHOIS record (registrar, dates, status, name servers).
url: https://lookup.icann.org/en/lookup
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Authoritative WHOIS/RDAP lookup of a domain's registration from ICANN's own portal.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free official ICANN lookup; no account.
opsec: passive
opsecNote: A standard registration-data query against ICANN's RDAP service — passive, no signal to the domain owner.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by ICANN, the body that coordinates the domain-name system; the authoritative front-end for registration data (RDAP/WHOIS).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ICANN WHOIS
- ICANN RDAP lookup
tags:
- domains-ip-infrastructure
- whois
- rdap
- registration
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- icann-whois-lookup
- rdrs-icann-org
---

# ICANN Lookup

> ICANN's own domain-registration lookup — the authoritative front-end for RDAP/WHOIS data on any domain.

## When to use
You have a `domain` and want its canonical registration record straight from ICANN: sponsoring registrar, creation/updated/expiry dates, domain status codes (e.g. clientTransferProhibited), name servers, and — where not privacy-redacted — registrant contact. A trustworthy baseline before using third-party WHOIS aggregators.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://lookup.icann.org/en/lookup.
2. Enter the `domain` and submit (solve any CAPTCHA).
3. Read the RDAP record: registrar, key dates, status codes, name servers, and any available contact fields.
4. Pivot: name servers and registrar feed infrastructure mapping; creation date and status help assess the domain's age/legitimacy; unredacted contacts feed reverse-WHOIS (`[[whois-freaks]]`).

## Inputs → Outputs
- **In:** `domain`
- **Out:** authoritative registration record (registrar, dates, status, name servers) for the `domain`
- **Empty/negative result looks like:** "no matching record" for an unregistered/invalid domain; for TLDs/ccTLDs not in ICANN's RDAP, it may point you to the relevant registry instead.

## Gotchas & OpSec
- Registrant contact is usually GDPR/privacy-redacted — expect the human details to be hidden.
- Some ccTLDs aren't served here; use the country's registry for those.
- It gives the *current* record; for historical WHOIS use a history provider.

## Overlaps ("do both")
- Pairs with `[[whois-freaks]]` (reverse/historical WHOIS) — ICANN gives the authoritative current record; those add ownership history and reverse lookups.

## Trust & verifiability
`trust: trusted` — ICANN's official lookup, the authoritative source for registration data; only registrant-contact redaction limits it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | icann-lookup |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

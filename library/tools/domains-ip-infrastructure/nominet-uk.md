---
id: nominet-uk
name: nominet.uk
description: Use when you have a `.uk` `domain` and want the authoritative registry WHOIS — registrar, registration/expiry dates and (for orgs) registrant — returns domain and employer-org leads.
url: https://www.nominet.uk/lookup/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Authoritative WHOIS for .uk domains (registrar, dates, nameservers, and business registrant where not opted out).
selectorsIn:
- domain
selectorsOut:
- domain
- employer-org
status: live
pricing: free
costNote: Free registry WHOIS lookup from Nominet, the official .uk registry; no account. Rate-limited to deter bulk scraping.
opsec: passive
opsecNote: A registry WHOIS query does not notify the domain owner. Note that Nominet hides individual (non-trading) registrants' personal details by default under UK data-protection rules, so a blank registrant is privacy protection, not necessarily concealment.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Nominet is the official registry operator for .uk; its WHOIS is the authoritative source for .uk registration data.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Nominet WHOIS
- nominet.uk lookup
tags:
- domainsandips
- Domains & IPs
- whois
- uk
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# nominet.uk

> The official .uk registry WHOIS: look up any `.uk` / `.co.uk` domain for its registrar, registration and expiry dates, nameservers, and — for businesses — the registrant.

## When to use
You have a `.uk` `domain` tied to your subject or their business and want authoritative registration facts. Nominet's WHOIS is the source of record for `.uk`: it confirms the registrar, when the domain was registered/renewed (a timeline signal), the nameservers (hosting/infra pivot), and, for domains registered by a trading business, the registrant `employer-org`. Individual registrants' personal details are withheld by default.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.nominet.uk/lookup/.
2. Enter the `.uk` / `.co.uk` domain and run the lookup (solve any anti-bot check).
3. Read the record: registrant (for businesses / those not opted out), registrar, registration & expiry dates, and nameservers.
4. Pivot: registrant business name → `employer-org` and Companies House lookup; nameservers/registrar → hosting infrastructure; registration date → activity timeline.

## Inputs → Outputs
- **In:** `.uk` `domain`
- **Out:** registrar, registration/expiry dates, nameservers, and (for business registrants) the registrant `employer-org` / related `domain` infrastructure.
- **Empty/negative result looks like:** "no match" (domain unregistered) or a record with registrant details withheld — the latter means an individual opted for privacy under UK law, not that the lookup failed.

## Gotchas & OpSec
- Personal registrant data is hidden by default for non-trading individuals — a blank registrant is normal, not evasion.
- Only covers `.uk` namespace; use a different registry/WHOIS for other TLDs.
- Rate-limited and behind anti-bot checks; don't script bulk queries against it.

## Overlaps ("do both")
- Pairs with a generic WHOIS tool and Companies House — Nominet is authoritative for the .uk registration facts, while those add cross-TLD context and (for businesses) director/company detail.

## Trust & verifiability
`trust: trusted` — Nominet is the official .uk registry, so its WHOIS is the authoritative source for .uk domains; the only caveat is deliberate, lawful redaction of individuals' details.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nominet-uk |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

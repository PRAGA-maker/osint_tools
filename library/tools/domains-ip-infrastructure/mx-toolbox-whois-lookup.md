---
id: mx-toolbox-whois-lookup
name: MX Toolbox Whois Lookup
description: Use when you have a `domain` or `ip-address` and want quick WHOIS registration details — returns registrar, registrant/org, dates and nameservers alongside MXToolbox's other DNS tools.
url: https://mxtoolbox.com/Whois.aspx
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Fast browser WHOIS lookup for a domain or IP, with one-click pivots to MXToolbox's DNS/blacklist tools.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- employer-org
- email
status: live
pricing: freemium
costNote: Free web WHOIS and most DNS lookups; bulk monitoring, alerts, and the API are paid MXToolbox plans.
opsec: passive
opsecNote: The WHOIS query hits MXToolbox / registry data, not the target's own servers, so the domain owner isn't notified. MXToolbox logs your lookups; use a clean session for sensitive domains. Avoid the "test this server" tools if you want to stay fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: MXToolbox is a long-established, reputable DNS/email diagnostics provider; its WHOIS reflects registry/registrar data accurately.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- mxtoolbox
- mx-toolbox-reverse-ip-search
- iana-whois-service
- email-header-analyzer
- mx-toolbox-blacklist-check
- mx-toolbox-email-header-analyzer
- mxtoolbox-blacklists
- mxtoolbox-com
- mxtoolbox-com-2
aliases:
- MXToolbox WHOIS
- mxtoolbox.com/Whois.aspx
tags:
- whois
- dns
- domain
- infrastructure
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# MX Toolbox Whois Lookup

> A fast, clean web WHOIS from a trusted DNS-tools provider — with the rest of MXToolbox's DNS/blacklist arsenal one click away.

## When to use
You have a `domain` or `ip-address` and want its WHOIS registration data quickly: registrar, registrant/organisation (where not privacy-masked), creation/expiry dates, and nameservers. Use it to attribute a domain, check how old it is (freshly-registered domains are a fraud signal), read the org/contact behind it, and then jump straight into MXToolbox's reverse-IP, blacklist, and DNS tools for the same target without changing sites.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://mxtoolbox.com/Whois.aspx.
2. Enter the `domain` (or `ip-address`) and run the lookup.
3. Read the WHOIS: registrar, registrant/`employer-org` and any exposed `email`, registration/expiry dates, and nameservers.
4. Note privacy redaction (many registrants use WHOIS privacy) — the org/dates/NS are still informative even when the name is hidden.
5. Pivot: use the toolbar to run Reverse IP, Blacklist, and DNS lookups on the same target; nameservers/registrant feed infrastructure-clustering tools like `[[dnslytics-com]]`.

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** registrar, registrant `employer-org`/`email` (if unmasked), dates, nameservers
- **Empty/negative result looks like:** heavily-redacted WHOIS (GDPR/privacy) or "no match" for an unregistered/invalid domain — redaction is normal and doesn't mean the domain is fake; use dates/NS and reverse tools instead.

## Gotchas & OpSec
- Registrant details are often privacy-masked; lean on registration dates, registrar, and nameservers when the name is hidden.
- Free tier is generous for lookups; automation/monitoring needs a paid plan.
- OpSec: passive; the target's servers aren't touched by a WHOIS. Skip the active "test server" utilities if staying non-attributable.

## Overlaps ("do both")
- Pairs with `[[iana-whois-service]]` (to find the authoritative registry for exotic TLDs first) and `[[mx-toolbox-reverse-ip-search]]` — do the WHOIS here, then reverse-IP/DNS on the same toolbar to map the surrounding infrastructure.

## Trust & verifiability
`trust: trusted` — MXToolbox is an established DNS/email diagnostics company; its WHOIS output mirrors registry/registrar records. The only limitation is upstream privacy redaction, not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mx-toolbox-whois-lookup |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, employer-org, email |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

---
id: whois-search-com
name: Whois-Search.com
description: Use when you have a `domain` or `ip-address` and want its registration record — returns registrant/contact details, registrar, creation/expiry dates and nameservers via WHOIS/RDAP.
url: http://www.whois-search.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Free WHOIS/RDAP lookups on a domain or IP to surface registrant, dates and nameservers.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- email
status: live
pricing: free
costNote: Free web WHOIS/RDAP lookups; no account or payment.
opsec: passive
opsecNote: The service performs the WHOIS/RDAP query from its own servers, so the target's registrar/DNS never sees your IP. Only Whois-Search.com logs your query; a clean session is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party WHOIS front-end; the records it shows come straight from registries/registrars, but presentation varies and privacy-redaction/GDPR masking limits what's visible.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- mx-toolbox-whois-lookup
- mxtoolbox-com
aliases:
- Whois Search
- whois-search.com
tags:
- toddington
- curated-directory
- whois-ip-lookups-website-analysis
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Whois-Search.com

> A free WHOIS/RDAP lookup front-end — turn a domain or IP into its registration record: registrant, registrar, key dates and nameservers.

## When to use
You have a `domain` (from an email, a website, a link the subject posted) or an `ip-address` and want to know who registered it and when. WHOIS can expose a registrant name, organisation, contact `email`/phone, and the creation date (useful for establishing when an online presence began). Even when personal fields are privacy-masked, the registrar, nameservers, and dates are still investigative signals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.whois-search.com.
2. Enter the `domain` or `ip-address` and run the lookup (try the **RDAP** view too — it's the modern, structured successor to legacy WHOIS).
3. Read the record: **registrant** name/org (if not redacted), **contact email/phone**, **registrar**, **creation / updated / expiry dates**, and **nameservers**.
4. Pivot: an exposed registrant email feeds email OSINT; nameservers/registrar feed infrastructure mapping; the creation date bounds when the site/persona appeared.

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** registrant/contact details incl. `email`, registrar, dates, and authoritative `domain` (nameservers)
- **Empty/negative result looks like:** "No match" (unregistered/expired domain), or a record where registrant fields read "REDACTED FOR PRIVACY" / a privacy-service proxy — the domain exists but personal data is withheld.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — the front-end queries on your behalf; the target's infrastructure isn't touched by you.
- Post-GDPR, most registrant personal fields are redacted or hidden behind privacy services; don't expect a name/email on modern registrations. Historic WHOIS tools may still hold pre-redaction data.
- A single WHOIS front-end can format or cache records differently; corroborate a critical field against another WHOIS/RDAP source.

## Overlaps ("do both")
- Pairs with `[[mx-toolbox-whois-lookup]]` and `[[mxtoolbox-com]]` — run the same domain through more than one WHOIS/DNS source, since redaction and record freshness differ between providers.

## Trust & verifiability
`trust: community` — a third-party WHOIS viewer; the data originates from authoritative registries but is filtered by privacy rules and the front-end's presentation, so verify anything load-bearing against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whois-search-com |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, email |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |

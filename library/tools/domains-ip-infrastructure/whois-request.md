---
id: whois-request
name: Whois Request
description: Use when you have a `domain` or `ip-address` and want its WHOIS registration — returns registrant/contact details, registrar, dates and nameservers, plus newly-registered-domain tracking.
url: https://whoisrequest.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Free WHOIS lookups on a domain/IP, with the bonus of browsing newly-registered / recently-dropped domains.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- email
status: live
pricing: free
costNote: Free WHOIS lookups and newly-registered-domain lists; no account required.
opsec: passive
opsecNote: WhoisRequest queries registries/registrars on your behalf, so the target's infrastructure isn't touched by your IP. Only WhoisRequest logs your query; a clean session suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party WHOIS front-end (also known for its daily newly-registered-domain feeds); records come from authoritative registries but are subject to GDPR/privacy redaction and the site's presentation.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- whoisrequest
- whois-search-com
- mx-toolbox-whois-lookup
aliases:
- WhoisRequest
- whoisrequest.com
tags:
- toddington
- curated-directory
- whois-ip-lookups-website-analysis
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Whois Request

> A free WHOIS lookup service — registrant, registrar, dates and nameservers for a domain or IP — that also publishes lists of newly-registered domains.

## When to use
You have a `domain` or `ip-address` and want its registration record: who registered it (where not redacted), the registrar, creation/expiry dates, and nameservers. WhoisRequest also maintains **newly-registered / recently-expired domain** feeds, which are useful for spotting a subject's freshly-created sites, typosquats, or scam domains as they appear. Use it like any WHOIS source — the creation date bounds when an online presence began, and any exposed contact is a pivot.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://whoisrequest.com and enter the `domain` (or `ip-address`).
2. Read the WHOIS record: **registrant** name/org (if unredacted), **contact email**, **registrar**, **creation / updated / expiry** dates, and **nameservers**.
3. For monitoring, browse the newly-registered-domain listings (e.g. filter by keyword/brand) to catch fresh domains of interest.
4. Pivot: an exposed registrant email feeds email OSINT; nameservers/registrar feed infrastructure mapping; the creation date bounds a persona's timeline.

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** registrant/contact details incl. `email`, registrar, dates, authoritative `domain` (nameservers)
- **Empty/negative result looks like:** "no match" (unregistered/expired) or a record with registrant fields "REDACTED FOR PRIVACY" behind a proxy — the domain exists but personal data is withheld (post-GDPR default).

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — the front-end queries on your behalf; the target isn't contacted.
- Since GDPR, most registrant personal fields are redacted; expect registrar/dates/nameservers rather than a name/email on modern registrations. Historic-WHOIS tools may hold pre-redaction data.
- WHOIS front-ends can cache or format differently — corroborate a load-bearing field against a second source.

## Overlaps ("do both")
- Pairs with `[[whois-search-com]]` and `[[mx-toolbox-whois-lookup]]` — run the same domain through more than one WHOIS source (redaction/freshness differ), and feed the network side to `[[hurricane-electric-internet-services]]`.

## Trust & verifiability
`trust: community` — a third-party WHOIS viewer over authoritative registry data; reliable for registrar/dates/nameservers, limited by privacy redaction, so verify anything critical against a second WHOIS/RDAP source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whois-request |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, email |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
